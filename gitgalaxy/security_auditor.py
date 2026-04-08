# ==============================================================================
# security_auditor.py
# GitGalaxy Phase 7.8: Advanced Machine Learning Threat Hunting
# ==============================================================================
import logging
import math
import numpy as np
from pathlib import Path
from collections import Counter

try:
    import pandas as pd
    import xgboost as xgb
    ML_AVAILABLE = True
except ImportError:
    ML_AVAILABLE = False

from . import gitgalaxy_standards_v1 as config

class SecurityAuditor:
    """Calculates deep dependency graphs and executes XGBoost Threat Inference."""
    
    def __init__(self, model_path="gitgalaxy_malware_xgb.json", parent_logger=None):
        self.logger = parent_logger.getChild("ml_auditor") if parent_logger else logging.getLogger("ml_auditor")
        
        # Load the Universal Schemas to map the raw vectors back to names
        schemas = getattr(config, "RECORDING_SCHEMAS", {})
        self.SIGNAL_SCHEMA = schemas.get("SIGNAL_SCHEMA", [])
        
        self.model = None
        self.feature_names = []
        
        if ML_AVAILABLE:
            # ---> THE FIX: Always resolve the model path relative to this script's location <---
            model_file = Path(__file__).parent / model_path
            
            if model_file.exists():
                try:
                    self.model = xgb.XGBClassifier()
                    self.model.load_model(str(model_file))
                    self.feature_names = self.model.feature_names_in_
                    self.logger.info(f"🧠 XGBoost Threat Model loaded: {model_file.name}")
                except Exception as e:
                    self.logger.error(f"Failed to load XGBoost model: {e}")
            else:
                self.logger.warning(f"XGBoost model not found at {model_file}. Running graph resolution only.")
        else:
            self.logger.warning("Pandas or XGBoost not installed. Running graph resolution only.")

    def audit_galaxy(self, stars):
        if not stars: return stars
        
        self.logger.info("Resolving N-th degree dependency graphs...")
        stars = self._resolve_dependency_graph(stars)
        
        if not self.model:
            return stars
            
        self.logger.info("Executing XGBoost Threat Inference across all artifacts...")
        
        # 1. Build the DataFrame matching the training extraction
        df = self._construct_feature_matrix(stars)
        
        # 2. Reindex to guarantee columns match the exact training schema (fills missing langs with 0)
        X = df.reindex(columns=self.feature_names, fill_value=0)
        
        # 3. Predict
        probabilities = self.model.predict_proba(X)[:, 1] # Probability of being class 1 (Malware)
        predictions = self.model.predict(X)
        
        # 4. Inject back into RAM
        for i, star in enumerate(stars):
            ml_score = round(float(probabilities[i]) * 100.0, 2)
            is_threat = bool(predictions[i])
            
            # Inject into the domain context so the UI and JSON recorders pick it up automatically
            if "domain_context" not in star["telemetry"]:
                star["telemetry"]["domain_context"] = {}
                
            star["telemetry"]["domain_context"]["AI Threat Score"] = f"{ml_score}%"
            star["is_ml_threat"] = is_threat
            
            if is_threat:
                self.logger.warning(f"🚨 AI THREAT DETECTED: {star.get('path')} (Confidence: {ml_score}%)")
                
        return stars

    def _resolve_dependency_graph(self, stars):
        """Moved from audit_recorder.py: Resolves transitive fragility and blast radius."""
        resolution_map = {}
        for s in stars:
            p = s.get("path", "")
            name = s.get("name", Path(p).name)
            stem = Path(p).stem
            if p: resolution_map[p] = p
            if name: resolution_map[name] = p
            if stem: resolution_map[stem] = p

        outbound_graph = {s.get("path", ""): [] for s in stars}
        inbound_graph = {s.get("path", ""): [] for s in stars}

        for s in stars:
            curr = s.get("path", "")
            for imp in s.get("raw_imports", []):
                if imp in resolution_map:
                    target = resolution_map[imp]
                    if target != curr:
                        if target not in outbound_graph[curr]: outbound_graph[curr].append(target)
                        if curr not in inbound_graph[target]: inbound_graph[target].append(curr)

        def get_nth_degree(start, graph):
            visited = set()
            queue = [start]
            while queue:
                node = queue.pop(0)
                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return len(visited)

        for s in stars:
            path = s.get("path", "")
            dir_up = len(s.get("raw_imports", []))
            dir_down = s.get("telemetry", {}).get("popularity", 0)
            tot_up = get_nth_degree(path, outbound_graph)
            tot_down = get_nth_degree(path, inbound_graph)
            
            # Save deeply into the star's RAM for the recorders and the AI
            s["dependency_network"] = {
                "direct_upstream": dir_up,
                "direct_downstream": dir_down,
                "total_upstream": tot_up,
                "total_downstream": tot_down
            }
        return stars

    def _construct_feature_matrix(self, stars):
        """Reconstructs the Pandas DataFrame exactly as build_master_db.py did."""
        
# --- 1. BUILD THE ROW DICTIONARY ---
        rows = []
        for s in stars:
            tel = s.get("telemetry", {})
            dep = s.get("dependency_network", {})
            hits = s.get("hit_vector", [0] * len(self.SIGNAL_SCHEMA))
            
            # 1. Base Variables
            cfr = tel.get("control_flow_ratio", 0.0)
            coding_loc = s.get("coding_loc", 0)
            logic_loc = max(int(round(coding_loc * cfr)), 1)
            safe_denom = max(logic_loc, coding_loc, 1)
            
            sats = s.get("satellites", [])
            max_func_comp = max([sat.get("branch", 0) for sat in sats] + [0])
            avg_func_args = sum([sat.get("args", 0) for sat in sats]) / max(len(sats), 1)

            # Map the flat hit array back to a dictionary using the schema
            hit_dict = {self.SIGNAL_SCHEMA[i]: hits[i] for i in range(len(self.SIGNAL_SCHEMA)) if i < len(hits)}

            # 2. Build the Row Dictionary
            row = {
                "language": s.get("lang_id", "unknown").lower(),
                "structural_mass": s.get("file_impact", 0.0),
                "cog_raw": tel.get("densities", {}).get("cog_raw", 0.0),
                "ownership_entropy": tel.get("ownership_entropy", 0.0),
                "silo_risk": tel.get("author_distribution", 0.0),
                "control_flow_ratio": cfr,
                "popularity": dep.get("direct_downstream", 0),
                "import_count": dep.get("direct_upstream", 0),
                
                # Log Transforms
                "log_logic_loc": np.log1p(logic_loc),
                "log_max_func_complexity": np.log1p(max_func_comp),
                "log_avg_func_args": np.log1p(avg_func_args),
                "log_direct_upstream": np.log1p(dep.get("direct_upstream", 0)),
                "log_direct_downstream": np.log1p(dep.get("direct_downstream", 0)),
                "log_total_upstream": np.log1p(dep.get("total_upstream", 0)),
                "log_total_downstream": np.log1p(dep.get("total_downstream", 0)),
            }

            # 3. Reconstruct Density Signatures
            exclusion_list = {
                'hit_structural_tab_indentations', 'hit_structural_space_indentations', 
                'hit_indentation_faction', 'hit_manual_memory_allocation',
                'hit_asynchronous_concurrent_execution', 'hit_sec_tainted_injection',
                'hit_embedded_credentials_and_keys', 'hit_non_standard_unicode_homoglyphs',
                'hit_dynamic_code_execution_eval_exec', 'hit_high_entropy_obfuscated_logic',
                'hit_raw_memory_manipulation', 'hit_safety_and_constraint_bypasses',
                'hit_external_network_and_i_o_hooks', 'hit_global_environment_mutation',
                'hit_commented_out_executable_logic', 'hit_low_level_bitwise_cryptographic_math',
                'hit_non_standard_steganographic_imports'
            }
            
            for key, val in hit_dict.items():
                col_name = f"hit_{key}"
                if col_name not in exclusion_list:
                    raw_density = (val / safe_denom) * 100.0
                    row[f"log_density_{col_name}"] = np.log1p(raw_density)

            # 4. Contextual/Mitigation Columns
            contextual = [
                ("raw_danger", hit_dict.get("danger", 0) + hit_dict.get("sec_danger", 0)),
                ("raw_sec_private_info", hit_dict.get("sec_private_info", 0)),
                ("raw_sec_tainted_injection", hit_dict.get("sec_tainted_injection", 0))
            ]
            for col_name, val in contextual:
                raw_density = (val / safe_denom) * 100.0
                row[f"log_density_{col_name}"] = np.log1p(raw_density)

            # Inject the live repo-level context already calculated by the Signal Processor
            row["assigned_macro_species"] = tel.get("repo_macro_species", 0)
            row["primary_z_score"] = tel.get("repo_z_score", 0.0)
            for i in range(11):
                row[f"dist_to_{i}"] = tel.get(f"dist_to_{i}", 0.0)

            rows.append(row)

        df = pd.DataFrame(rows)
        # One-Hot Encode Languages
        df = pd.get_dummies(df, columns=['language'], dummy_na=False)
        return df