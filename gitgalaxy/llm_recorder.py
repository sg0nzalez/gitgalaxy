# ==============================================================================
# GitGalaxy
# Copyright (c) 2026 Joe Esquibel
#
# This source code is licensed under the PolyForm Noncommercial License 1.0.0.
# You may not use this file except in compliance with the License.
# A copy of the license can be found in the LICENSE file in the root directory
# of this project, or at https://polyformproject.org/licenses/noncommercial/1.0.0/
# ==============================================================================
import sqlite3
import logging
import statistics
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
from . import gitgalaxy_standards_v011 as config

# ==============================================================================
# GitGalaxy Phase 10: LLM Recorder (The AI Translation Layer)
# Strategy v6.3.0 Protocol: Token Density, Distribution Physics & RAG Graphs
# ==============================================================================

class LLMRecorder:
    """
    PURPOSE: Translates raw GitGalaxy telemetry into AI-optimized artifacts.
    
    FEATURES:
    1. Statistical Physics: Calculates Min/Max/Mean/Median/Mode for all risks.
    2. Syntactic Bottlenecks: Isolates I/O and Dependency choke points.
    3. God Functions: Ranks top 10 satellites by individual magnitude.
    4. Relational Knowledge Graph: Builds a SQLite DB for autonomous agents.
    5. Markdown Brief: Token-compressed text for standard LLM context windows.
    """

    def __init__(self, parent_logger: Optional[logging.Logger] = None):
        if parent_logger:
            self.logger = parent_logger.getChild("llm_recorder")
            self.logger.setLevel(parent_logger.level)
        else:
            self.logger = logging.getLogger("llm_recorder")
            self.logger.setLevel(logging.INFO)

        # --- DYNAMIC SCHEMA FETCH ---
        schemas = getattr(config, "RECORDING_SCHEMAS", {})
        self.RISK_SCHEMA = schemas.get("RISK_SCHEMA", [])
        self.SIGNAL_SCHEMA = schemas.get("SIGNAL_SCHEMA", [])

    def generate_artifacts(
        self, 
        stars: List[Dict[str, Any]], 
        singularity: List[Dict[str, Any]], 
        summary: Dict[str, Any], 
        session_meta: Dict[str, Any], 
        output_dir: str,
        forensic_report: Optional[Dict[str, Any]] = None
    ):
        """Generates the dual-output AI artifacts: Markdown and SQLite."""
        if forensic_report is None:
            forensic_report = {}
            
        # --- ABSOLUTE ROUTING LOGIC (Matching Audit Recorder) ---
        base_dir = Path("/srv/storage_16tb/projects/gitgalaxy/data")
        base_dir.mkdir(parents=True, exist_ok=True)
            
        target_name = session_meta.get("target", "unknown_project")
        output_path_md = base_dir / f"{target_name}_galaxy_llm.md"
        output_path_db = base_dir / f"{target_name}_galaxy_graph.sqlite"
        
        self.logger.info(f"Initiating LLM Artifact Generation for '{target_name}'...")
        
        # --- REVERSE DEPENDENCY RESOLUTION (Calculated once for both outputs) ---
        resolution_map = {}
        for s in stars:
            path = s.get("path", "")
            name = s.get("name", Path(path).name)
            stem = Path(path).stem
            if path: resolution_map[path] = path
            if name: resolution_map[name] = path
            if stem: resolution_map[stem] = path

        inbound_map = {s.get("path", ""): [] for s in stars}
        for s in stars:
            curr = s.get("path", "")
            for imp in s.get("raw_imports", []):
                if imp in resolution_map:
                    target_path = resolution_map[imp]
                    if target_path != curr and curr not in inbound_map[target_path]:
                        inbound_map[target_path].append(curr)

        # 1. Build the Relational Knowledge Graph
        self._generate_sqlite_graph(stars, singularity, summary, session_meta, output_path_db, inbound_map)
        
        # 2. Build the Token-Optimized Markdown Brief
        md_content = self._build_markdown(stars, singularity, summary, session_meta, forensic_report, inbound_map)
        
        try:
            with open(output_path_md, "w", encoding="utf-8") as f:
                f.write(md_content)
            self.logger.info(f"AI Mission Complete:\n -> Markdown: {output_path_md}\n -> SQLite: {output_path_db}")
        except Exception as e:
            self.logger.error(f"Failed to seal LLM brief: {e}", exc_info=True)
    
    def _build_dependency_analysis(self, stars: List[Dict]) -> str:
        """Generates rankings for the most critical architectural dependencies."""
        if not stars:
            return ""

        # 1. Top Structural Pillars (Imported By / Blast Radius)
        # Sorts by 'popularity' telemetry which tracks inbound connections
        pillars = sorted(
            stars, 
            key=lambda x: x.get("telemetry", {}).get("popularity", 0) if isinstance(x.get("telemetry"), dict) else 0, 
            reverse=True
        )[:5]

        # 2. Top Orchestrators (Imports / Fragility Index)
        # Sorts by the length of the raw_imports array
        orchestrators = sorted(
            stars,
            key=lambda x: len(x.get("raw_imports", [])) if isinstance(x.get("raw_imports"), list) else 0,
            reverse=True
        )[:5]

        lines = ["### 5. Architectural Dependencies\n"]
        
        lines.append("#### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)")
        lines.append("These files act as core load-bearing infrastructure. Changes here carry a high risk of cascading breaks.\n")
        for rank, star in enumerate(pillars, 1):
            name = star.get("name", "Unknown")
            path = star.get("path", "Unknown")
            count = star.get("telemetry", {}).get("popularity", 0) if isinstance(star.get("telemetry"), dict) else 0
            lines.append(f"{rank}. **{name}** (`{path}`) — {count} inbound connections")
        lines.append("\n")

        lines.append("#### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)")
        lines.append("These files pull in the most external dependencies. They are highly coupled and fragile to API changes.\n")
        for rank, star in enumerate(orchestrators, 1):
            name = star.get("name", "Unknown")
            path = star.get("path", "Unknown")
            count = len(star.get("raw_imports", [])) if isinstance(star.get("raw_imports"), list) else 0
            lines.append(f"{rank}. **{name}** (`{path}`) — {count} outbound dependencies")
        lines.append("\n")

        return "\n".join(lines)
    
    def _build_markdown(
        self, 
        stars: List[Dict[str, Any]], 
        singularity: List[Dict[str, Any]], 
        summary: Dict[str, Any], 
        session_meta: Dict[str, Any],
        forensic_report: Dict[str, Any],
        inbound_map: Dict[str, List[str]]
    ) -> str:
        """Constructs a high-density Markdown brief for LLM context windows."""
        target = session_meta.get("target", "Project")
        sum_data = summary.get("summary", {})
        health = summary.get("health", {})
        comp = summary.get("composition", {})
        git_audit = session_meta.get("git_audit", {})
        
        bypassed_count = summary.get("singularity", {}).get("unparsable", 0)
        total_excluded = len(singularity) + bypassed_count
        visible_count = sum_data.get("visible_stars", len(stars))
        
        lines = []
        lines.append(f"# ARCHITECTURAL_BRIEF: {target}")
        lines.append("> INSTRUCTION: Deterministic Syntactic Physics. Scores are %. Base refactoring on Mass and God Functions.\n")
        
        # --- 0. FORENSIC TRACEABILITY ---
        lines.append("## 0. FORENSIC TRACEABILITY")
        lines.append("| Metadata | Value |")
        lines.append("|---|---|")
        lines.append(f"| **Engine** | `{session_meta.get('engine', 'Unknown')}` |")
        lines.append(f"| **Target Path** | `{session_meta.get('target_directory', 'Unknown')}` |")
        lines.append(f"| **Timestamp** | `{session_meta.get('timestamp', 'Unknown')}` |")
        lines.append(f"| **Scan Duration** | `{session_meta.get('duration_seconds', 0.0)}s` |")
        lines.append(f"| **Git Branch** | `{git_audit.get('branch', 'N/A')}` |")
        lines.append(f"| **Git Commit** | `{git_audit.get('commit_hash', 'N/A')}` |")
        lines.append(f"| **Git Remote** | `{git_audit.get('remote_url', 'N/A')}` |")
        lines.append("")
        
        # --- CRITICAL SYSTEM INSTRUCTIONS ---
        lines.append("## SYSTEM INSTRUCTIONS")
        lines.append("> **CRITICAL PARADIGM:** This data does NOT assess 'Bad Code'. All 0-100% metrics measure **EXPOSURE TO RISK** (100% = Maximum Vulnerability).")
        lines.append("> **EMPATHY & CONTEXT:** Never judge the developers or the code. There is always a business reason for risk. High 'Tech Debt' usually means a team survived a mountain of sprints to hit a ruthless production deadline. Prototyping needs also differ vastly from production needs, and we do not know this project's current phase. Frame all insights as helpful, blameless observations.")
        lines.append("> **THE MATH:** GitGalaxy's risk equations are rough approximations meant to highlight *general trends* (e.g., High vs. Low risk), not to argue over tiny 1% differences. The math drives the visual overlay and can be customized to a team's standards.")
        lines.append("> ")
        lines.append("> **METRIC DEFINITIONS:**")
        lines.append("> * **Testing Exposure:** Risk of unshielded logic melting down in production (100% = 0 tests).")
        lines.append("> * **Specification Exposure (The Map vs. The Territory):** Measures 'Architectural Maturity'. 0% (Blueprint Indigo) means logic is safely anchored to a written requirement. 100% (Rogue Red) means exploratory or prototype logic operating without a formal contract.")
        lines.append(">   * *LLM DIRECTIVE:* This is a new paradigm. Most legacy projects will score 100% here. **Do not fault them.** Instead, gently nudge them that embedding `[audit]` or `[SPEC]` tags into their code turns a static README into a living Engineering Roadmap, surfacing the real bottom-up technical hurdles the team is solving rather than rigid, top-down 'God Specs'.")
        lines.append("> * **Cognitive Load Exposure:** How hard it is for a human to safely modify the logic.")
        lines.append("> * **Documentation Exposure:** The risk to the team if the original architect leaves.")
        lines.append("> * **Safety Exposure:** Structural brittleness caused by a lack of defensive programming.")
        lines.append("> * **Civil War Exposure:** A lighthearted metric tracking indentation formatting (Team Tabs vs. Team Spaces). Do NOT use this for serious risk or refactoring analysis.")
        lines.append("> Base all refactoring advice on mitigating these high exposures in high-mass files.\n")
        
        # --- 1. MACRO ECOSYSTEM ---
        lines.append("## 1. MACRO STATE")
        lines.append("| Metric | Value |")
        lines.append("|---|---|")
        lines.append(f"| Total Artifacts | {sum_data.get('total_files', 0)} |")
        lines.append(f"| Visible Matter (Scanned) | {visible_count} |")
        lines.append(f"| Dark Matter (Excluded) | {total_excluded} |")
        lines.append(f"| Total LOC | {sum_data.get('total_loc', 0)} |")
        lines.append(f"| Volatility Index | {sum_data.get('volatility_index', 0.0)} |")
        lines.append(f"| Darkness Ratio | {100 - sum_data.get('Percent_Visible', 0)}% |")
        lines.append(f"| Dominant Lang | {sum_data.get('dominant_language', 'UNK').upper()} |")
        lines.append("")

        # --- 2. LINGUISTIC COMPOSITION ---
        lines.append("## 2. COMPOSITION")
        if comp:
            lines.append("| Lang | Files | LOC | Share |")
            lines.append("|---|---|---|---|")
            total_visible = max(visible_count, 1)
            for lang, stats in sorted(comp.items(), key=lambda x: x[1].get("files", 0), reverse=True):
                pct = (stats.get('files', 0) / total_visible) * 100
                lines.append(f"| {lang.upper()} | {stats.get('files', 0)} | {stats.get('loc', 0)} | {pct:.1f}% |")
        lines.append("")

        # --- 3. DARK MATTER ---
        lines.append("## 3. DARK MATTER (EXCLUDED ARTIFACTS)")
        lines.append(f"*Total Excluded Artifacts: {total_excluded}*\n")
        
        comp_breakdown = summary.get("singularity", {}).get("composition_by_extension_and_reason", {})
        
        if comp_breakdown:
            lines.append("**Composition by Extension & Reason:**")
            for ext, reasons in list(comp_breakdown.items())[:15]:
                clean_reasons = []
                for rsn, count in list(reasons.items())[:3]:
                    safe_rsn = (rsn.replace("Unparsable", "Unrecognized Syntax")
                                   .replace("Structural Saturation", "Dense Structure")
                                   .replace("Singularity", "Dark Matter")
                                   .replace("Necrosis", "Optical Bypass")
                                   .replace("Blocked", "Excluded"))
                    clean_reasons.append(f"{count}x {safe_rsn.strip()}")
                
                reason_str = ", ".join(clean_reasons)
                lines.append(f"- `{ext}`: {reason_str}")
        else:
            legacy_breakdown = summary.get("singularity", {}).get("breakdown", {})
            sing_items = []
            for k, v in sorted(legacy_breakdown.items(), key=lambda x: x[1] if isinstance(x[1], int) else 0, reverse=True):
                if isinstance(v, int) and v > 0:
                    safe_k = k.replace("unparsable", "optical_bypass")
                    sing_items.append(f"`{safe_k}`:{v}")
            lines.append(" | ".join(sing_items))
            
        lines.append("")

        # --- 4. RISK DISTRIBUTIONS ---
        lines.append("## 4. RISK EXPOSURE PHYSICS (0-100%)")
        lines.append("| Risk Vector | Min | Max | Mean | Med | Mode |")
        lines.append("|---|---|---|---|---|---|")
        
        schemas = getattr(config, "RECORDING_SCHEMAS", {})
        exposure_labels = schemas.get("EXPOSURE_LABELS", {})
        
        for i, risk_slug in enumerate(self.RISK_SCHEMA):
            vals = [s.get("risk_vector", [])[i] for s in stars if len(s.get("risk_vector", [])) > i]
            risk_label = exposure_labels.get(risk_slug, risk_slug.replace('_', ' ').title())
            
            if vals:
                v_min, v_max = round(min(vals), 1), round(max(vals), 1)
                v_mean, v_med = round(statistics.mean(vals), 1), round(statistics.median(vals), 1)
                try: v_mode = round(statistics.mode(vals), 1)
                except statistics.StatisticsError: v_mode = "N/A"
                lines.append(f"| {risk_label} | {v_min} | {v_max} | {v_mean} | {v_med} | {v_mode} |")
            else:
                lines.append(f"| {risk_label} | - | - | - | - | - |")
        lines.append("")

        # --- 5. SYNTACTIC BOTTLE-NECKS & DEPENDENCIES ---
        lines.append("## 5. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES")
        
        # 5.A: I/O Bottlenecks
        io_idx = self.SIGNAL_SCHEMA.index("io") if "io" in self.SIGNAL_SCHEMA else -1
        if io_idx >= 0:
            top_io = sorted(stars, key=lambda x: x.get("hit_vector", [])[io_idx] if len(x.get("hit_vector", [])) > io_idx else 0, reverse=True)[:3]
            lines.append("### Top I/O Latency Risks")
            for s in top_io: 
                lines.append(f"- `{s.get('path')}` (Hits: {s.get('hit_vector', [])[io_idx]})")
            lines.append("")

        # 5.B: Structural Pillars (Imported By)
        pillars = sorted(stars, key=lambda x: len(inbound_map.get(x.get("path", ""), [])), reverse=True)[:5]
        lines.append("### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)")
        lines.append("These files act as core load-bearing infrastructure. Changes here carry a high risk of cascading breaks.\n")
        for rank, star in enumerate(pillars, 1):
            name = star.get("name", "Unknown")
            path = star.get("path", "Unknown")
            count = len(inbound_map.get(path, []))
            lines.append(f"{rank}. **{name}** (`{path}`) — {count} inbound connections")
        lines.append("")

        # 5.C: Orchestrators (Imports)
        orchestrators = sorted(stars, key=lambda x: len(x.get("raw_imports", [])) if isinstance(x.get("raw_imports"), list) else 0, reverse=True)[:5]
        lines.append("### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)")
        lines.append("These files pull in the most external dependencies. They are highly coupled and fragile to API changes.\n")
        for rank, star in enumerate(orchestrators, 1):
            name = star.get("name", "Unknown")
            path = star.get("path", "Unknown")
            count = len(star.get("raw_imports", [])) if isinstance(star.get("raw_imports"), list) else 0
            lines.append(f"{rank}. **{name}** (`{path}`) — {count} outbound dependencies")
        lines.append("")

        # --- 6. GOD FUNCTIONS (THE SATELLITES) ---
        lines.append("## 6. SATELLITE HITLIST (God Functions)")
        func_impacts = forensic_report.get("function_impact", {}).get("highest", [])
        if func_impacts:
            for f in func_impacts[:10]:
                lines.append(f"- `{f.get('name')}` (@ `{f.get('file')}`) -> Impact: {f.get('impact')} | LOC: {f.get('loc')}")
        else:
            lines.append("*No complex satellites detected.*")
        lines.append("")

        # --- 7. TOP CONSTELLATIONS ---
        lines.append("## 7. CONSTELLATIONS (Top 10 Heaviest Folders)")
        constellations = summary.get("constellations", {})
        if constellations:
            lines.append("| Folder Path | Files | Total Mass | Avg Cog Load | Avg Debt |")
            lines.append("|---|---|---|---|---|")
            
            sorted_consts = sorted(
                constellations.items(), 
                key=lambda x: x[1].get("total_mass", 0.0), 
                reverse=True
            )[:10]
            
            for c_name, c_data in sorted_consts:
                mass = c_data.get('total_mass', 0.0)
                count = c_data.get('file_count', 0)
                exposures = c_data.get('avg_exposures', {})
                cog = exposures.get('cognitive_load', 0.0)
                debt = exposures.get('tech_debt', 0.0)
                lines.append(f"| `{c_name}` | {count} | {mass} | {cog}% | {debt}% |")
        else:
            lines.append("*No deep folder structures detected.*")
        lines.append("")

        # --- 8. ARCHITECTURAL HITLIST ---
        lines.append("## 8. VISIBLE MATTER HITLIST (Top 20 Mass)")
        sorted_stars = sorted(stars, key=lambda x: x.get("file_impact", 0.0), reverse=True)[:20]
        
        for s in sorted_stars:
            p = s.get("path", "UNK")
            l = s.get("lang_id", "UNK").upper()
            m = s.get("file_impact", 0.0)
            loc = s.get("total_loc", 0)
            
            rv = s.get("risk_vector", [])
            tel = s.get("telemetry", {})
            cog = rv[0] if len(rv) > 0 else 0.0
            flux = rv[6] if len(rv) > 6 else 0.0
            
            hv = s.get("hit_vector", [])
            dna = sorted([(self.SIGNAL_SCHEMA[i], val) for i, val in enumerate(hv) if val > 0 and i < len(self.SIGNAL_SCHEMA)], key=lambda x: x[1], reverse=True)[:4]
            dna_str = ", ".join([f"{k}:{v}" for k, v in dna])
            
            lines.append(f"### `{p}` ({l})")
            lines.append(f"- `Impact`: {m} | `LOC`: {loc} | `CtrlFlow`: {round(tel.get('control_flow_ratio', 0.0) * 100, 1)}% | `AuthorDist`: {round(tel.get('author_distribution', 0.0), 1)}%")
            lines.append(f"- `Risk`: CogLoad {cog}%, Flux {flux}%")
            lines.append(f"- `DNA`: {dna_str}")
            
            inbound = sorted(inbound_map.get(p, []))
            if inbound:
                imp_str = ", ".join([Path(x).name for x in inbound[:5]])
                if len(inbound) > 5:
                    imp_str += f" ... (+{len(inbound) - 5} more)"
                lines.append(f"- `Imported By`: {imp_str}")
            else:
                lines.append(f"- `Imported By`: None (Orphan / Entrypoint)")
                
            outbound = s.get("raw_imports", [])
            if outbound:
                lines.append(f"- `Imports`: {len(outbound)} dependencies")
            else:
                lines.append(f"- `Imports`: 0 dependencies")
                
            lines.append("") 
            
        return "\n".join(lines)
    
    def _generate_sqlite_graph(
        self, 
        stars: List[Dict[str, Any]], 
        singularity: List[Dict[str, Any]], 
        summary: Dict[str, Any], 
        session: Dict[str, Any], 
        db_path: Path,
        inbound_map: Dict[str, List[str]]
    ):
        """Creates a relational database for advanced SQL-based AI analysis."""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute('DROP TABLE IF EXISTS meta')
            cursor.execute('CREATE TABLE meta (key TEXT, value TEXT)')
            cursor.executemany('INSERT INTO meta VALUES (?, ?)', [
                ("engine", session.get("engine")),
                ("project", session.get("target")),
                ("timestamp", session.get("timestamp")),
                ("branch", session.get("git_audit", {}).get("branch")),
                ("commit", session.get("git_audit", {}).get("commit_hash"))
            ])

            cursor.execute('DROP TABLE IF EXISTS stars')
            risk_cols = ", ".join([f"{r} REAL" for r in self.RISK_SCHEMA])
            cursor.execute(f'''
                CREATE TABLE stars (
                    id INTEGER PRIMARY KEY,
                    path TEXT,
                    filename TEXT,
                    constellation TEXT,
                    language TEXT,
                    lock_tier INTEGER,
                    total_loc INTEGER,
                    coding_loc INTEGER,
                    file_impact REAL,
                    control_flow_ratio REAL,
                    author_distribution REAL,
                    popularity INTEGER,
                    {risk_cols}
                )
            ''')

            cursor.execute('DROP TABLE IF EXISTS constellations')
            cursor.execute('''
                CREATE TABLE constellations (
                    name TEXT PRIMARY KEY,
                    file_count INTEGER,
                    total_mass REAL,
                    avg_cognitive_load REAL,
                    avg_safety_score REAL,
                    avg_tech_debt REAL,
                    avg_verification REAL
                )
            ''')

            cursor.execute('DROP TABLE IF EXISTS satellites')
            cursor.execute('''
                CREATE TABLE satellites (
                    id INTEGER PRIMARY KEY,
                    star_id INTEGER,
                    name TEXT,
                    type_id TEXT,
                    loc INTEGER,
                    impact REAL,
                    FOREIGN KEY(star_id) REFERENCES stars(id)
                )
            ''')

            cursor.execute('DROP TABLE IF EXISTS dna_hits')
            cursor.execute('''
                CREATE TABLE dna_hits (
                    star_id INTEGER,
                    signal_type TEXT,
                    hit_count INTEGER,
                    FOREIGN KEY(star_id) REFERENCES stars(id)
                )
            ''')

            # --- NEW: Explicit Bi-Directional Dependency Tables ---
            cursor.execute('DROP TABLE IF EXISTS outbound_dependencies')
            cursor.execute('''
                CREATE TABLE outbound_dependencies (
                    star_id INTEGER,
                    imported_path TEXT,
                    FOREIGN KEY(star_id) REFERENCES stars(id)
                )
            ''')

            cursor.execute('DROP TABLE IF EXISTS inbound_dependencies')
            cursor.execute('''
                CREATE TABLE inbound_dependencies (
                    star_id INTEGER,
                    imported_by_path TEXT,
                    FOREIGN KEY(star_id) REFERENCES stars(id)
                )
            ''')

            const_meta = summary.get("constellations", {})
            for c_name, c_data in const_meta.items():
                exps = c_data.get("avg_exposures", {})
                cursor.execute('''
                    INSERT INTO constellations (name, file_count, total_mass, avg_cognitive_load, avg_safety_score, avg_tech_debt, avg_verification)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    c_name, 
                    c_data.get("file_count", 0), 
                    c_data.get("total_mass", 0.0),
                    exps.get("cognitive_load", 0.0),
                    exps.get("safety_score", 0.0),
                    exps.get("tech_debt", 0.0),
                    exps.get("verification", 0.0)
                ))

            for star in stars:
                p = star.get("path")
                c_name = star.get("constellation", "__monolith__")
                tel = star.get("telemetry", {})
                rv = star.get("risk_vector", [0.0] * 13)
                
                # We inject the len() of the inbound map directly into the popularity column!
                pop_count = len(inbound_map.get(p, []))
                
                cursor.execute(f'''
                    INSERT INTO stars (path, filename, constellation, language, lock_tier, total_loc, coding_loc, file_impact, control_flow_ratio, author_distribution, popularity, {", ".join(self.RISK_SCHEMA)})
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, {", ".join(['?'] * len(self.RISK_SCHEMA))})
                ''', (
                    p, Path(p).name, c_name, star.get("lang_id"), star.get("lock_tier"), 
                    star.get("total_loc"), star.get("coding_loc"), star.get("file_impact"),
                    tel.get("control_flow_ratio"), tel.get("author_distribution"), pop_count,
                    *rv
                ))
                
                sid = cursor.lastrowid
                
                hv = star.get("hit_vector", [])
                dna_data = [(sid, self.SIGNAL_SCHEMA[i], hv[i]) for i in range(len(hv)) if hv[i] > 0]
                cursor.executemany('INSERT INTO dna_hits VALUES (?, ?, ?)', dna_data)
                
                for sat in star.get("satellites", []):
                    cursor.execute('INSERT INTO satellites (star_id, name, type_id, loc, impact) VALUES (?, ?, ?, ?, ?)', (
                        sid, sat.get("name"), sat.get("type_id"), sat.get("loc"), sat.get("impact")
                    ))

                # Inject Outbound Data
                raw_imports = star.get("raw_imports", [])
                if raw_imports:
                    out_data = [(sid, imp) for imp in raw_imports]
                    cursor.executemany('INSERT INTO outbound_dependencies VALUES (?, ?)', out_data)

                # Inject Inbound Data
                inbound = inbound_map.get(p, [])
                if inbound:
                    in_data = [(sid, imp_by) for imp_by in inbound]
                    cursor.executemany('INSERT INTO inbound_dependencies VALUES (?, ?)', in_data)

            conn.commit()
            conn.close()
        except Exception as e:
            self.logger.error(f"SQL Graph generation failed: {e}", exc_info=True)