# ==============================================================================
# GitGalaxy - AI Guardrails
# ==============================================================================
import logging
from typing import List, Dict, Any


class DevAgentFirewall:
    """
    Evaluates the codebase specifically to determine if it is safe to let
    an autonomous AI agent (Claude, Cursor, etc.) modify the code.
    """

    def __init__(self, parent_logger=None):
        self.logger = parent_logger.getChild("guardrails") if parent_logger else logging.getLogger("guardrails")

    def evaluate_ecosystem(self, parsed_files: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        self.logger.info("Executing Agentic Firewall & Token Physics Checks...")

        for file_data in parsed_files:
            token_mass = file_data.get("token_mass", 0)
            network_metrics = file_data.get("telemetry", {}).get("network_metrics", {})
            risk_vector = file_data.get("risk_vector", [])  # Assuming standard 0-100 risk scores

            # Extract relevant physics safely handling None values from Zero-Dependency Mode
            pagerank = network_metrics.get("normalized_blast_radius") or 0.0
            max_big_o = file_data.get("max_big_o") or 1

            guardrails = {
                "is_agentic_black_hole": False,
                "requires_hitl": False,  # Human-in-the-Loop
                "hallucination_zone": False,
                "warnings": [],
            }

            # 1. The Context Window Shredder (The Black Hole)
            # If it burns > 8k tokens AND has terrible algorithmic complexity, the AI will fail.
            if token_mass is not None and token_mass > 8000 and max_big_o >= 3:
                guardrails["is_agentic_black_hole"] = True
                guardrails["warnings"].append(
                    f"CRITICAL: Black Hole detected. Token mass ({token_mass}) and O(N^{max_big_o}) complexity will shred agent context."
                )

            # 2. The HITL Mandate (Blast Radius + Danger)
            if pagerank > 1.0 and sum(risk_vector) > 200:
                guardrails["requires_hitl"] = True
                guardrails["warnings"].append(
                    "WARNING: High Blast Radius with severe risk debt. Human-in-the-Loop required for modifications."
                )

            # 3. The Hallucination Zone (Metaprogramming + Low Docs)
            meta_heavy = file_data.get("telemetry", {}).get("reflection_metaprogramming", 0) > 2
            doc_density = file_data.get("telemetry", {}).get("doc_density", 1.0)

            if meta_heavy and doc_density < 0.2:
                guardrails["hallucination_zone"] = True
                guardrails["warnings"].append(
                    "DANGER: Hallucination Zone. Dynamic metaprogramming detected with < 20% documentation density. AI will likely hallucinate missing methods."
                )

            # 4. The Silent Mutation Risk (High Flux + High Blast + No Tests)
            state_flux = file_data.get("telemetry", {}).get("state_flux", 0)
            in_degree = network_metrics.get("in_degree", 0)
            has_tests = file_data.get("telemetry", {}).get("has_tests", False)

            if state_flux > 50 and in_degree > 5 and not has_tests:
                guardrails["silent_mutation_risk"] = True
                guardrails["warnings"].append(
                    f"CRITICAL: Silent Mutation Risk. Flux ({state_flux}) and Blast Radius ({in_degree} deps) are high, but zero tests exist. AI cannot verify its own fixes."
                )

            # Inject the firewall report back into the file's telemetry
            if "telemetry" not in file_data:
                file_data["telemetry"] = {}
            file_data["telemetry"]["ai_guardrails"] = guardrails

        return parsed_files
