# ==============================================================================
# GitGalaxy
# Copyright (c) 2026 Joe Esquibel
# ==============================================================================
import logging
import math
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from gitgalaxy.standards.analysis_lens import RECORDING_SCHEMAS

HAS_NETWORKX = False
try:
    import networkx as nx
    from networkx.algorithms import community

    HAS_NETWORKX = True
except ImportError:
    pass


class NetworkRiskSensor:
    """
    The GitGalaxy Network Risk Sensor (Graph Topology & Blast Radius).

    PURPOSE: Ingests the flat universe of stars, wires them into a Directed Graph
    using raw_imports, and calculates Ecosystem Roles, PageRank, and
    Vector-Weighted Systemic Threats.
    """

    def __init__(self, parent_logger: Optional[logging.Logger] = None):
        self.logger = (
            parent_logger.getChild("network_sensor")
            if parent_logger
            else logging.getLogger("network_sensor")
        )
        self.RISK_SCHEMA = RECORDING_SCHEMAS.get("RISK_SCHEMA", [])

    def extract_test_coverage_mapping(
        self, files: List[Dict[str, Any]]
    ) -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
        """
        Maps function calls from test files to their imported production targets.
        Returns a dictionary mapping: production_file_path -> { production_function_name: [test_function_data] }
        """
        coverage_map = {}
        resolution_map = {}

        # 1. Build resolution map
        for f in files:
            path = f.get("path", "")
            if path:
                resolution_map[path] = path
                resolution_map[Path(path).name] = path
                resolution_map[Path(path).stem] = path

        # 2. Identify Test Files and extract their outgoing invocations
        for f in files:
            path = f.get("path", "")
            low_path = path.lower()

            # Structural heuristic for test files
            is_test = any(
                x in low_path
                for x in ["/test/", "/tests/", "test_", "_test", ".spec.", ".test."]
            )
            if not is_test:
                continue

            # Identify which production files this test file imports
            target_paths = set()
            for imp in f.get("raw_imports", []):
                target_token = (
                    imp[0] if isinstance(imp, tuple) and len(imp) == 2 else imp
                )
                target_path = resolution_map.get(target_token)

                if target_path and target_path != path:
                    target_paths.add(target_path)

            if not target_paths:
                continue

            # Map each test function's payload to the production functions it calls
            for test_func in f.get("functions", []):
                calls_out = test_func.get("calls_out_to", [])
                if not calls_out:
                    continue

                target_count = len(calls_out)
                test_payload = {
                    "impact": test_func.get("impact", 0.0),
                    "target_count": target_count,
                    "test_hits": test_func.get("hit_vector", {}).get("test", 0),
                    "test_skip_hits": test_func.get("hit_vector", {}).get(
                        "test_skip", 0
                    ),
                    "decorators": test_func.get("hit_vector", {}).get("decorators", 0),
                }

                for target_path in target_paths:
                    if target_path not in coverage_map:
                        coverage_map[target_path] = {}

                    for called_func_name in calls_out:
                        if called_func_name not in coverage_map[target_path]:
                            coverage_map[target_path][called_func_name] = []
                        coverage_map[target_path][called_func_name].append(test_payload)

        return coverage_map

    def map_ecosystem(
        self, stars: List[Dict[str, Any]]
    ) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Builds the directed graph and calculates multi-dimensional risk vectors.
        Modifies the 'telemetry' dictionary of each star in place.
        """
        if not HAS_NETWORKX:
            return self._fallback_map_ecosystem(stars)

        self.logger.info(
            f"Network Risk Sensor: Initializing Directed Graph for {len(stars)} nodes..."
        )

        G = nx.DiGraph()

        # 1. Build the Resolution Map (Fast Path Lookup)
        resolution_map = {}
        for s in stars:
            path = s.get("path", "")
            name = s.get("name", Path(path).name)
            stem = Path(path).stem
            if path:
                resolution_map[path] = path
            if name:
                resolution_map[name] = path
            if stem:
                resolution_map[stem] = path

            # Extract Max Algorithmic Complexity for the node
            sats = s.get("satellites", [])
            max_big_o = max([sat.get("big_o_depth", 1) for sat in sats]) if sats else 1
            is_recursive = any([sat.get("is_recursive", False) for sat in sats])

            # Add Node with Vector and O(N) properties
            G.add_node(
                path,
                risk_vector=s.get("risk_vector", [0.0] * len(self.RISK_SCHEMA)),
                max_big_o=max_big_o,
                is_recursive=is_recursive,
                db_complexity=(
                    max([sat.get("db_complexity", 0) for sat in sats]) if sats else 0
                ),
            )

        # 2. Wire the Edges (File-to-File Level 1 & Entity Level 2)
        for s in stars:
            curr_path = s.get("path", "")
            raw_imports = s.get("raw_imports", [])

            for imp in raw_imports:
                # Check if it's a Level 2 Tuple (Entity Import) or Level 1 String
                if isinstance(imp, tuple) and len(imp) == 2:
                    target_token, entity = imp
                else:
                    target_token = imp
                    entity = None

                if target_token in resolution_map:
                    target_path = resolution_map[target_token]
                    if target_path != curr_path:
                        # Edge weight can be increased if specific entities are highly coupled
                        weight = 1.5 if entity else 1.0
                        if G.has_edge(curr_path, target_path):
                            G[curr_path][target_path]["weight"] += weight
                        else:
                            G.add_edge(curr_path, target_path, weight=weight)

        # 3. Network Mathematics (Blast Radius & Centrality)
        # PageRank determines the absolute "Load-Bearing" gravity of a file
        try:
            pagerank = nx.pagerank(G, weight="weight")

            # THE FIX: Drop the exact threshold from 5000 down to 500.
            # Force a maximum sample size of 100 nodes for anything larger.
            k_val = min(len(G.nodes()), 100) if len(G.nodes()) > 500 else None
            betweenness = nx.betweenness_centrality(G, k=k_val, weight="weight")

            # THE FIX: Closeness Centrality has no built-in sampling.
            # Drop the bypass threshold from 5000 to 1500 to prevent minute-long hangs.
            if len(G.nodes()) > 1500:
                self.logger.warning(
                    "Graph too massive for exact Closeness Centrality. Bypassing."
                )
                closeness = {n: 0.0 for n in G.nodes()}
            else:
                closeness = nx.closeness_centrality(G)

        except Exception as e:
            self.logger.warning(
                f"Network math failed to converge, defaulting to 0: {e}"
            )
            pagerank = {n: 0.0 for n in G.nodes()}
            betweenness = {n: 0.0 for n in G.nodes()}
            closeness = {n: 0.0 for n in G.nodes()}

        in_degrees = dict(G.in_degree())
        out_degrees = dict(G.out_degree())

        # 4. Vector Cross-Multiplication & Bottleneck Identification
        for s in stars:
            path = s.get("path", "")
            if path not in G:
                continue

            pr_score = pagerank.get(path, 0.0)
            in_d = in_degrees.get(path, 0)
            out_d = out_degrees.get(path, 0)

            # --- Ecosystem Role Ratio ---
            total_edges = in_d + out_d
            if total_edges == 0:
                ecosystem_role = "Isolated/Orphan"
                producer_ratio = 0.0
            else:
                producer_ratio = in_d / total_edges
                if producer_ratio > 0.8:
                    ecosystem_role = "Pure Producer (Foundation)"
                elif producer_ratio < 0.2:
                    ecosystem_role = "Pure Consumer (Orchestrator)"
                else:
                    ecosystem_role = "Transceiver (Middle-Tier)"

            # --- Multi-Dimensional Systemic Threat Vector ---
            # PageRank is usually a tiny decimal (e.g., 0.0005). We normalize it.
            # Multiply by 1000 to make the scale human/LLM readable.
            pr_normalized = pr_score * 1000
            local_risk_vector = s.get("risk_vector", [0.0] * len(self.RISK_SCHEMA))

            systemic_threat_vector = []
            for local_risk in local_risk_vector:
                # Systemic Threat = Blast Radius * Local Risk
                systemic_threat_vector.append(
                    round(pr_normalized * (local_risk / 100.0), 3)
                )

            # --- Algorithmic Network Bottleneck Detection ---
            max_big_o = G.nodes[path].get("max_big_o", 1)
            is_recursive = G.nodes[path].get("is_recursive", False)

            # A node is an Algorithmic Bottleneck if it is highly central AND highly complex
            is_algorithmic_bottleneck = False
            if pr_normalized > 1.0 and (is_recursive or max_big_o >= 3):
                is_algorithmic_bottleneck = True

            # 5. Write Telemetry Back to the Star
            if "telemetry" not in s:
                s["telemetry"] = {}

            s["telemetry"]["network_metrics"] = {
                "pagerank_score": round(pr_score, 6),
                "normalized_blast_radius": round(pr_normalized, 3),
                "betweenness_score": round(betweenness.get(path, 0.0), 6),
                "closeness_score": round(closeness.get(path, 0.0), 6),
                "in_degree": in_d,
                "out_degree": out_d,
                "producer_ratio": round(producer_ratio, 3),
                "ecosystem_role": ecosystem_role,
                "systemic_threat_vector": systemic_threat_vector,
                "is_algorithmic_bottleneck": is_algorithmic_bottleneck,
            }

            # Overwrite the old "popularity" integer with the strict in_degree
            s["telemetry"]["popularity"] = in_d

        # =========================================================================
        # 6. MACRO-ECOSYSTEM PHYSICS (Repo-Level Health & Resilience)
        # =========================================================================
        macro_metrics = {
            "modularity": 0.0,
            "assortativity": 0.0,
            "cyclic_density": 0.0,
            "avg_path_length": 0.0,
            "articulation_points": 0,
        }

        if len(G) > 0:
            try:
                U = G.to_undirected()

                # A. Modularity (Spaghetti vs Microservice)
                try:
                    if len(U) > 5000:
                        self.logger.warning(
                            "Graph too massive for Modularity. Bypassing."
                        )
                        macro_metrics["modularity"] = 0.0
                    else:
                        # THE FIX: Attempt Louvain (blazing fast), fallback to Greedy (slow)
                        try:
                            communities = community.louvain_communities(U)
                        except AttributeError:
                            communities = community.greedy_modularity_communities(U)

                        macro_metrics["modularity"] = round(
                            community.modularity(U, communities), 4
                        )
                except Exception:
                    pass

                # B. Assortativity (Resiliency)
                try:
                    assort = nx.degree_assortativity_coefficient(G)
                    macro_metrics["assortativity"] = (
                        round(assort, 4) if not math.isnan(assort) else 0.0
                    )
                except Exception:
                    pass

                # C. Cyclic Density (Static Friction / Dependency Loops)
                try:
                    sccs = list(nx.strongly_connected_components(G))
                    nodes_in_cycles = sum(len(c) for c in sccs if len(c) > 1)
                    macro_metrics["cyclic_density"] = round(nodes_in_cycles / len(G), 4)
                except Exception:
                    pass

                # D. Average Shortest Path (Coupling Distance)
                try:
                    if len(U) > 5000:
                        self.logger.warning(
                            "Graph too massive for Avg Path Length. Bypassing."
                        )
                        macro_metrics["avg_path_length"] = 0.0
                    else:
                        largest_cc = max(nx.connected_components(U), key=len)
                        subgraph = U.subgraph(largest_cc)
                        macro_metrics["avg_path_length"] = round(
                            nx.average_shortest_path_length(subgraph), 4
                        )
                except Exception:
                    pass

                # E. Articulation Points (Shatter Risk)
                try:
                    macro_metrics["articulation_points"] = len(
                        list(nx.articulation_points(U))
                    )
                except Exception:
                    pass

            except Exception as e:
                self.logger.warning(f"Macro network math failed: {e}")

        self.logger.info(
            "Network Risk Sensor: Vector Mathematics & Graph Topology Complete."
        )
        return stars, macro_metrics

    def _fallback_map_ecosystem(
        self, stars: List[Dict[str, Any]]
    ) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        self.logger.warning(
            "[!] 'networkx' not found. Operating in Zero-Dependency Mode. Using linear counting for Ecosystem Roles."
        )

        resolution_map = {}
        for s in stars:
            p = s.get("path", "")
            if p:
                resolution_map[p] = p
            name = s.get("name", Path(p).name)
            if name:
                resolution_map[name] = p
            stem = Path(p).stem
            if stem:
                resolution_map[stem] = p

        in_degrees = {s.get("path", ""): 0 for s in stars}
        out_degrees = {s.get("path", ""): 0 for s in stars}

        for s in stars:
            curr_path = s.get("path", "")
            for imp in s.get("raw_imports", []):
                target_token = (
                    imp[0] if isinstance(imp, tuple) and len(imp) == 2 else imp
                )
                if target_token in resolution_map:
                    target_path = resolution_map[target_token]
                    if target_path != curr_path:
                        out_degrees[curr_path] = out_degrees.get(curr_path, 0) + 1
                        in_degrees[target_path] = in_degrees.get(target_path, 0) + 1

        for s in stars:
            path = s.get("path", "")
            in_d = in_degrees.get(path, 0)
            out_d = out_degrees.get(path, 0)

            total_edges = in_d + out_d
            if total_edges == 0:
                ecosystem_role = "Isolated/Orphan"
                producer_ratio = 0.0
            else:
                producer_ratio = in_d / total_edges
                if producer_ratio > 0.8:
                    ecosystem_role = "Pure Producer (Foundation)"
                elif producer_ratio < 0.2:
                    ecosystem_role = "Pure Consumer (Orchestrator)"
                else:
                    ecosystem_role = "Transceiver (Middle-Tier)"

            if "telemetry" not in s:
                s["telemetry"] = {}
            s["telemetry"]["network_metrics"] = {
                "pagerank_score": 0.0,
                "normalized_blast_radius": 0.0,
                "betweenness_score": 0.0,
                "closeness_score": 0.0,
                "in_degree": in_d,
                "out_degree": out_d,
                "producer_ratio": round(producer_ratio, 3),
                "ecosystem_role": ecosystem_role,
                "systemic_threat_vector": [],
                "is_algorithmic_bottleneck": False,
            }
            s["telemetry"]["popularity"] = in_d

        macro_metrics = {
            "modularity": None,
            "assortativity": None,
            "cyclic_density": None,
            "avg_path_length": None,
            "articulation_points": None,
        }
        return stars, macro_metrics
