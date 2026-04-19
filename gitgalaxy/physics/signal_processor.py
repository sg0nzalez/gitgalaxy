# ==============================================================================
# GitGalaxy
# Copyright (c) 2026 Joe Esquibel
#
# This source code is licensed under the PolyForm Noncommercial License 1.0.0.
# You may not use this file except in compliance with the License.
# A copy of the license can be found in the LICENSE file in the root directory
# of this project, or at https://polyformproject.org/licenses/noncommercial/1.0.0/
# ==============================================================================
import math
import logging
import re
import statistics
from typing import Dict, Any, List, Optional, Tuple
from gitgalaxy.standards import analysis_lens as config
from gitgalaxy.standards import analysis_lens

# ==============================================================================
# GitGalaxy Phase 4: Signal Processor (The Physics Engine)
# Strategy v6.2.0 Protocol: Temporal Normalization & Universal Exposure
# ==============================================================================

class SignalProcessor:
    """
    The GitGalaxy Signal Processor.
    
    PURPOSE: Converts raw logic counts and temporal telemetry into "Exposure Vectors" 
    and generates high-fidelity forensic reports identifying structural risks.
    
    ARCHITECTURE (v6.2.0):
    1. Temporal Consolidation: Math formulas for Churn and Stability now live here.
    2. Two-Pass Normalization: Auto-scales Churn based on the galaxy's global maximum.
    3. Sigmoid Armor: `try/except OverflowError` guarantees survival on extreme file densities.
    4. Flexible Risk Schema: Vector indexing is dynamic, preventing offset bugs.
    """

    # ==========================================================================
    # SCHEMA BINDING (Single Source of Truth)
    # Dynamically inherited from gitgalaxy_standards_v011.py
    # ==========================================================================
    
    # The 60-Point Spectral Sync (Standard + Security Lens)
    SIGNAL_SCHEMA = config.RECORDING_SCHEMAS.get("SIGNAL_SCHEMA", [])
    
    # The 18-Point Risk Exposure Schema
    RISK_SCHEMA = config.RECORDING_SCHEMAS.get("RISK_SCHEMA", [])

    def __init__(
        self, 
        aperture_config: Optional[Dict[str, Any]] = None,
        parent_logger: Optional[logging.Logger] = None
    ):
        """Initializes the physics engine with forensic constants and telemetry."""
        if parent_logger:
            self.logger = parent_logger.getChild("processing")
            self.logger.setLevel(parent_logger.level)
        else:
            self.logger = logging.getLogger("processing")
            self.logger.setLevel(logging.INFO) 

        self.logger.debug("Initializing Universal Exposure Framework...")
        self.config = aperture_config or {}
    
        # ======================================================================
        # 🧠 FETCH THE ML INFERENCE BRAINS (Global & Local)
        # ======================================================================
        # ---> NEW (DYNAMIC) <---
        ml_brain = getattr(config, "GENERAL_FILE_INFERENCE_MODEL", {})
        self.SCALER_MEDIANS = ml_brain.get("SCALER_MEDIANS", [0.0] * 100) # Safe fallback size
        self.SCALER_IQRS = ml_brain.get("SCALER_IQRS", [1.0] * 100)
        
        # Dynamically grab whichever ARCHETYPES_K key exists (e.g. ARCHETYPES_K9)
        arch_key = next((k for k in ml_brain.keys() if k.startswith('ARCHETYPES_K')), None)
        self.GLOBAL_ARCHETYPES = ml_brain.get(arch_key, {}) if arch_key else {}
        
        # ---> NEW: Fetch Language-Specific Micro-Species Brains <---
        self.LANGUAGE_INFERENCE_BRAINS = getattr(config, "SPECIFIC_FILE_INFERENCE_MODEL", {})

        # Fetch Physics Constants
        physics = getattr(config, "PHYSICS_CONSTANTS", {})
        self.WEIGHT_RISK = physics.get("WEIGHT_RISK", 2.5)
        self.WEIGHT_DEFENSE = physics.get("WEIGHT_DEFENSE", 1.0)
        self.TIER_VARS = physics.get("TIER_VARS", {
            "tier1": {"fc": 1.0,  "irc": 0}, 
            "tier2": {"fc": 0.85, "irc": 2}, 
            "tier3": {"fc": 0.60, "irc": 5}
        })
        self.MASSIVE_FILE_THRESHOLD = physics.get("MASSIVE_FILE_THRESHOLD", 300)
        self.TESTING_RISK_FLOOR = physics.get("TESTING_RISK_FLOOR", 15.0)

        # Fetch Path Modifiers & Asset Masks
        self.path_modifiers = getattr(config, "PATH_MODIFIERS", {})
        self.asset_masks = getattr(config, "PHYSICS_ASSET_MASKS", {})
        self.risk_tuning = getattr(config, "RISK_EQUATION_TUNING", {})
        self.is_paranoid = self.config.get("PARANOID_MODE", False) 
        
        # ======================================================================
        # THE CONTEXT VS. ENTITY MATRIX (Domain Ontologies)
        # ======================================================================
        # We now fetch this dynamically from gitgalaxy_standards_v1.py instead of hardcoding it!
        security_profiles = getattr(config, "LANGUAGE_SECURITY_PROFILES", {})
        self.ECOSYSTEMS = security_profiles.get("ECOSYSTEMS", {})
        self.NATIVE_WEIGHTS = security_profiles.get("NATIVE_WEIGHTS", {})
        
        # Fetch ALIEN_WEIGHTS dynamically, with a fallback to the hardcoded dictionary
        self.ALIEN_WEIGHTS = security_profiles.get("ALIEN_WEIGHTS", {
            "systems_in_web": {"memory": 5.0, "logic_bomb": 3.0}, # C code hiding in a JS app = Trojan
            "infra_in_web":   {"logic_bomb": 4.0},                # Shell script hiding in a JS app = Backdoor
            "web_in_systems": {"flux": 3.0}                       # JS embedded in C firmware = Bizarre architecture
        })
        
        # ---> NEW: Fetch the Archetype Matrix
        self.ARCHETYPE_VIOLATION_MATRIX = security_profiles.get("ARCHETYPE_VIOLATION_MATRIX", {})
        
        self.logger.info(f"Signal Processor Online | Context-Aware Risk Schema & ML Archetypes loaded.")
        
    def _classify_archetype(self, scaled_vector: List[float], archetypes_dict: Dict[str, List[float]]) -> Tuple[str, float, Dict[str, float]]:
        """
        Dynamically calculates the Euclidean Distance for any provided K-Means dictionary.
        Returns: Best Match Name, Minimum Distance (Drift), Full Fingerprint.
        """
        fingerprint = {}
        best_match = "Unknown Archetype"
        min_dist = float('inf')
        
        if not archetypes_dict:
            return best_match, 0.0, fingerprint
            
        for arch_name, centroid_vector in archetypes_dict.items():
            dist_sq = 0.0
            
            for i in range(min(len(scaled_vector), len(centroid_vector))):
                dist_sq += (scaled_vector[i] - centroid_vector[i]) ** 2
                
            distance = math.sqrt(dist_sq)
            fingerprint[arch_name] = round(distance, 3) 
            
            if distance < min_dist:
                min_dist = distance
                best_match = arch_name
                
        return best_match, round(min_dist, 3), fingerprint
    
    def _get_context_multipliers(self, file_lang: str, folder_lang: str) -> Dict[str, float]:
        """
        Calculates risk multipliers by comparing a file's language to its neighborhood.
        Prevents the 'Apollo Paradox' and catches 'Trojan Horse' entities.
        """
        # Default multipliers if no specific context rules apply
        multipliers = {"memory": 1.0, "logic_bomb": 1.0, "flux": 1.0, "injection": 1.0}
        
        file_lang = file_lang.lower()
        folder_lang = folder_lang.lower() if folder_lang else file_lang

        # Determine the ecosystem of the specific File
        file_eco = "backend" # Default fallback
        for eco, langs in self.ECOSYSTEMS.items():
            if file_lang in langs:
                file_eco = eco
                break
                
        # Determine the ecosystem of the surrounding Folder
        folder_eco = "backend"
        for eco, langs in self.ECOSYSTEMS.items():
            if folder_lang in langs:
                folder_eco = eco
                break

        # SCENARIO 1: The Entity matches the Context (Native)
        if file_eco == folder_eco:
            return self.NATIVE_WEIGHTS.get(file_eco, multipliers)

        # SCENARIO 2: The Entity is an Alien (Context Mismatch)
        alien_key = f"{file_eco}_in_{folder_eco}"
        alien_penalties = self.ALIEN_WEIGHTS.get(alien_key, {})
        
        # Apply standard weights of the file, but overwrite with severe alien penalties
        base_weights = self.NATIVE_WEIGHTS.get(file_eco, multipliers).copy()
        base_weights.update(alien_penalties)
        
        if alien_penalties:
            self.logger.warning(f"👽 ALIEN ENTITY DETECTED: {file_lang} file hiding in a {folder_eco} neighborhood. Applying severe penalties: {alien_penalties}")

        return base_weights
    
    def _calculate_silo_risk(self, authors: dict) -> float:
        """
        Calculates the 'Bus Factor' risk of a file.
        100% = A single developer wrote the entire file (High Silo Risk).
        0% = Perfectly distributed across multiple developers (Low Silo Risk).
        """
        if not authors:
            return 0.0 
            
        total_commits = sum(authors.values())
        if total_commits == 0:
            return 0.0
            
        dominant_commits = max(authors.values())
        ownership_ratio = dominant_commits / total_commits
        
        return round(ownership_ratio * 100.0, 1)

    def calculate_risk_vector(self, meta: Dict[str, Any], equations: Dict[str, int], umbrella_bonus: float = 0.0) -> Dict[str, Any]:
        """Calculates risk exposure, temporal physics, and per-file physical impact."""
        loc = max(meta.get("coding_loc", 1), 1)
        total_loc = max(meta.get("total_loc", loc), 1)
        doc_lines = meta.get("doc_loc", 0)
        lang_id = meta.get("lang_id", "undeterminable")
        rel_path = meta.get("path", "unknown")
        
        try:
            import os
            filename = os.path.basename(rel_path).lower()
            ext = f".{filename.split('.')[-1]}" if '.' in filename else ""
            ghost_meta = meta.get("metadata", {})

            # ==================================================================
            # THE EXTENSION DECEPTION SENSOR
            # Punishes files claiming to be inert data but evaluated as executable code
            # ==================================================================
            if ext:
                inert_disguises = {".txt", ".md", ".csv", ".json", ".yaml", ".yml", ".xml", ".log", ".png", ".jpg", ".jpeg", ".gif", ".mp4"}
                executable_langs = {"shell", "python", "javascript", "typescript", "ruby", "perl", "php", "c", "cpp", "rust", "go", "java", "powershell"}
                
                if ext in inert_disguises and lang_id.lower() in executable_langs:
                    self.logger.warning(f"🚨 DECEPTION DETECTED: {rel_path} claims to be {ext} but executed as {lang_id}!")
                    equations["sec_extension_mismatch"] = 1
            
            # ==================================================================
            # THE EXPOSED SECRET BYPASS PROTOCOL
            # Treat exposed keyfiles as structural vulnerabilities, skipping math
            # ==================================================================
            aperture_cfg = getattr(config, "APERTURE_CONFIG", {})
            secrets_exts = aperture_cfg.get("SECRETS_EXTENSIONS", set())
            secrets_exact = aperture_cfg.get("SECRETS_EXACT", set())
            aperture_reason = ghost_meta.get("aperture_reason", "")
            
            is_critical_leak = "CRITICAL LEAK" in aperture_reason or ext in secrets_exts or filename in secrets_exact
            
            if is_critical_leak:
                temporal_data = meta.get("temporal_telemetry", {})
                _, raw_churn_freq = self._calc_raw_temporal_signals(temporal_data)
                authors_map = meta.get("authors", {})
                
                dominant_author = max(authors_map, key=authors_map.get) if authors_map else ghost_meta.get("ownership", "Unknown Architect")
                
                # 1. Base array of zeroes
                blanket_risk_vector = [0.0] * len(self.RISK_SCHEMA)
                
                # 2. Spike Hardcoded Secrets Exposure to Maximum
                if "secrets_risk" in self.RISK_SCHEMA:
                    secrets_idx = self.RISK_SCHEMA.index("secrets_risk")
                    blanket_risk_vector[secrets_idx] = 100.0
                    
                # 3. Retain Churn so we know if the secret is actively being modified
                if "churn" in self.RISK_SCHEMA:
                    churn_idx = self.RISK_SCHEMA.index("churn")
                    blanket_risk_vector[churn_idx] = min(raw_churn_freq * 10, 100.0)

                return {
                    "risk_vector": blanket_risk_vector,
                    "hit_vector": [0] * len(self.SIGNAL_SCHEMA), 
                    "file_impact": 150.0, # Massive physical footprint for the 3D map
                    "telemetry": {
                        "archetype": getattr(config, "STATIC_ARCHETYPES", {}).get("data", "Static: Declarative Data & Configurations"),
                        "control_flow_ratio": 0.0,
                        "ownership_entropy": self._calc_ownership_entropy(authors_map),
                        "author_distribution": self._calculate_silo_risk(authors_map),
                        "ownership": dominant_author,
                        "domain_context": {"alert": "CRITICAL LEAK BYPASS", **ghost_meta}
                    }
                }

            # ==================================================================
            # THE MINIFIED / VENDOR TRIPWIRE PROTOCOL
            # ==================================================================
            is_minified = meta.get("is_minified", False)
            if is_minified:
                # 1. Zero out all standard architectural risks
                blanket_risk_vector = [0.0] * len(self.RISK_SCHEMA)
                
                # 2. Check for ANY malicious intent (eval, network fetching, etc.)
                intent_mass = equations.get("sec_danger", 0) + equations.get("sec_io", 0) + equations.get("sec_safety_neg", 0)
                
                if intent_mass > 0:
                    self.logger.critical(f"🚨 MINIFIED TRIPWIRE TRIGGERED: {rel_path} contains obscured execution/IO!")
                    if "obscured_payload" in self.RISK_SCHEMA:
                        blanket_risk_vector[self.RISK_SCHEMA.index("obscured_payload")] = 100.0
                    if "logic_bomb" in self.RISK_SCHEMA:
                        blanket_risk_vector[self.RISK_SCHEMA.index("logic_bomb")] = 100.0
                    if "injection_surface" in self.RISK_SCHEMA:
                        blanket_risk_vector[self.RISK_SCHEMA.index("injection_surface")] = 100.0

                return {
                    "risk_vector": blanket_risk_vector,
                    "hit_vector": [equations.get(k, 0) for k in self.SIGNAL_SCHEMA], 
                    "file_impact": 1.0, # Minified files don't carry architectural weight
                    "telemetry": {
                        "archetype": getattr(config, "STATIC_ARCHETYPES", {}).get("minified", "Static: Minified & Vendor Opaque Mass"),
                        "control_flow_ratio": 0.0,
                        "ownership_entropy": 0.0,
                        "author_distribution": 0.0,
                        "ownership": ghost_meta.get("ownership", "Unknown Architect"),
                        "domain_context": {"alert": "MINIFIED VENDOR BYPASS", **ghost_meta}
                    }
                }

            # ==================================================================
            # THE DOCUMENTATION BYPASS PROTOCOL
            # Treat pure literature as static structural assets, skipping logic math
            # ==================================================================
            doc_languages = self.asset_masks.get("DOCUMENTATION_LANGUAGES", {"markdown", "plaintext", "rst", "text"})
                        
            if lang_id.lower() in doc_languages:
                temporal_data = meta.get("temporal_telemetry", {})
                _, raw_churn_freq = self._calc_raw_temporal_signals(temporal_data)
                authors_map = meta.get("authors", {})
                
                dominant_author = max(authors_map, key=authors_map.get) if authors_map else ghost_meta.get("ownership", "Unknown Architect")

                blanket_risk_vector = [0.0] * len(self.RISK_SCHEMA)
                
                if "churn" in self.RISK_SCHEMA:
                    blanket_risk_vector[self.RISK_SCHEMA.index("churn")] = min(raw_churn_freq * 10, 100.0)
                if "documentation" in self.RISK_SCHEMA:
                    blanket_risk_vector[self.RISK_SCHEMA.index("documentation")] = 0.0 # <-- The Fix! 0% Risk.
                if "civil_war" in self.RISK_SCHEMA:
                    blanket_risk_vector[self.RISK_SCHEMA.index("civil_war")] = 50.0

                return {
                    "risk_vector": blanket_risk_vector,
                    "hit_vector": [0] * len(self.SIGNAL_SCHEMA), 
                    "file_impact": round(max(total_loc / 50.0, 1.0), 2),
                    "telemetry": {
                        "archetype": getattr(config, "STATIC_ARCHETYPES", {}).get("literature", "Static: Literature & Documentation"),
                        "control_flow_ratio": 0.0,
                        "ownership_entropy": 0.0,     # <-- FIX: Documentation has no logic entropy
                        "author_distribution": 0.0,   # <-- FIX: Plaintext changelogs don't have a Bus Factor
                        "ownership": dominant_author,
                        "domain_context": ghost_meta
                    }
                }

            # ==================================================================
            # 1. ACTIVE PHYSICS ENGINE (For normal executable code)
            # ==================================================================
            tier = self._get_tier(lang_id)
            fc = self.TIER_VARS[tier]["fc"]
            irc = self.TIER_VARS[tier]["irc"]
            
            # Environmental Context (Path-based overrides)
            mp_map = self._get_locational_multipliers(rel_path)
            
            folder_lang = ghost_meta.get("folder_dominant_lang", lang_id)
            eco_mp = self._get_context_multipliers(lang_id, folder_lang)

            self.logger.debug(f"[{rel_path}] Physics Calc | Lang: {lang_id} (Fc: {fc:.2f}, Irc: {irc})")

            hit_vector = [equations.get(key, 0) for key in self.SIGNAL_SCHEMA]

            # ==================================================================
            # 1. ACTIVE PHYSICS ENGINE (For normal executable code)
            # ==================================================================
            tier = self._get_tier(lang_id)
            fc = self.TIER_VARS[tier]["fc"]
            irc = self.TIER_VARS[tier]["irc"]
            
            # Environmental Context (Path-based overrides)
            mp_map = self._get_locational_multipliers(rel_path)
            
            folder_lang = ghost_meta.get("folder_dominant_lang", lang_id)
            eco_mp = self._get_context_multipliers(lang_id, folder_lang)

            self.logger.debug(f"[{rel_path}] Physics Calc | Lang: {lang_id} (Fc: {fc:.2f}, Irc: {irc})")

            hit_vector = [equations.get(key, 0) for key in self.SIGNAL_SCHEMA]

            # ------------------------------------------------------------------
            # 1. TEMPORAL PRE-PROCESSING (Raw Extraction)
            # ------------------------------------------------------------------
            temporal_data = meta.get("temporal_telemetry", {})
            stability_score, raw_churn_freq = self._calc_raw_temporal_signals(temporal_data)

            # ------------------------------------------------------------------
            # 1.5 BUILD THE ML VECTOR & CLASSIFY ARCHETYPE
            # ------------------------------------------------------------------
            cfr = meta.get("control_flow_ratio", 0.0) 
            
            # ---> NEW: THE ENCAPSULATION RATIO <---
            # How much of the file's data is safely locked inside functions?
            total_vars = equations.get("core_var_decl", 0)
            global_vars = equations.get("globals", 0)
            
            if total_vars == 0 and global_vars == 0:
                encapsulation_ratio = 1.0 # Safe by default if no state exists
            else:
                # 1.0 = Perfect (0 globals). 0.0 = Terrible (All globals).
                encapsulation_ratio = max(0.0, 1.0 - (global_vars / max(total_vars + global_vars, 1)))

            logic_loc = max(int(round(meta.get("coding_loc", 0) * cfr)), 1)
            safe_denom = max(logic_loc, meta.get("coding_loc", 1))
            
            # ---> START FUNCTION-LEVEL ML CLASSIFICATION <---
            satellites = meta.get("satellites", [])
            max_func_comp = 0
            avg_func_args = 0.0
            func_gini = 0.0
            max_big_o = 1
            max_db_complexity = 0
            
            func_ml_brain = getattr(analysis_lens, "GENERAL_FUNCTION_INFERENCE_MODEL", {})
            f_features = func_ml_brain.get("features", [])
            f_medians = func_ml_brain.get("SCALER_MEDIANS", [])
            f_iqrs = func_ml_brain.get("SCALER_IQRS", [])
            f_arch_key = next((k for k in func_ml_brain.keys() if k.startswith('ARCHETYPES_K')), None)
            f_centroids = func_ml_brain.get(f_arch_key, {}) if f_arch_key else {}
            
            # Bulletproof fallback names if the model dictionary forgets them
            f_names = func_ml_brain.get("cluster_names", [
                "Utility/Helper", "Data Router", "State Mutator", "God Function", 
                "Math Engine", "I/O Bridge", "Constructor", "Callback/Event", 
                "API Endpoint", "Validator", "Renderer", "Loop Processor"
            ])

            # ---> NEW: DIAGNOSTIC ML LOGGING <---
            if satellites and not f_centroids:
                self.logger.warning(f"⚠️ FUNCTION ML SILENT BYPASS: Brain loaded? {bool(func_ml_brain)} | Centroids: {len(f_centroids)} | Arch Key: {f_arch_key}")

            # Initialize has_recursion before the if block
            has_recursion = False
            
            if satellites:
                complexities = [s.get("branch", 0) for s in satellites]
                max_func_comp = max(complexities)
                avg_func_args = sum([s.get("args", 0) for s in satellites]) / len(satellites)
                max_big_o = max([s.get("big_o_depth", 1) for s in satellites])
                max_db_complexity = max([s.get("db_complexity", 0) for s in satellites])
                has_recursion = any([s.get("is_recursive", False) for s in satellites])
                
                # 1. Z-Scores Mathematics
                func_count = len(satellites)
                mean_comp = statistics.mean(complexities) if func_count > 0 else 0.0
                std_comp = statistics.pstdev(complexities) if func_count > 1 else 0.0

                for s in satellites:
                    # Apply Z-Score directly to RAM dictionary
                    c = s.get("branch", 0)
                    z_val = (c - mean_comp) / std_comp if std_comp > 0 else 0.0
                    s["z_score"] = round(z_val, 3)

                    # 2. Archetype Euclidean Classification
                    s["archetype"] = 'Unclassified'
                    if f_centroids: # <--- REMOVED f_features STRICT REQUIREMENT
                        raw_vec = [
                            float(s.get("branch", 0)),
                            float(s.get("loc", 0)),
                            float(s.get("args", 0)),
                            float(s.get("keyword_density", 0.0)),
                            float(s.get("control_flow_ratio", s.get("cf_ratio", 0.0)))
                        ]

                        scaled_vec = []
                        for i, val in enumerate(raw_vec):
                            med = f_medians[i] if i < len(f_medians) else 0.0
                            iqr = f_iqrs[i] if i < len(f_iqrs) and f_iqrs[i] > 0 else 1.0
                            scaled_vec.append((val - med) / iqr)

                        min_dist = float('inf')
                        for c_key, centroid in f_centroids.items():
                            dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(scaled_vec, centroid)))
                            if dist < min_dist:
                                min_dist = dist
                                try:
                                    # If the key is numbered like "Cluster 0", extract the 0
                                    c_idx = int(str(c_key).split(" ")[-1])
                                    s["archetype"] = f_names[c_idx] if c_idx < len(f_names) else c_key
                                except ValueError:
                                    # If the key is already the name (e.g., "Interfaces"), use it directly!
                                    s["archetype"] = str(c_key)

                # 3. Calculate Structural Inequality (Gini)
                if len(complexities) > 1 and sum(complexities) > 0:
                    sorted_comps = sorted(float(c) for c in complexities)
                    n = len(sorted_comps)
                    index = range(1, n + 1)
                    func_gini = (sum((2 * i - n - 1) * c for i, c in zip(index, sorted_comps))) / (n * sum(sorted_comps))
            # ---> END FUNCTION-LEVEL ML CLASSIFICATION <---
            
            raw_imports_count = len(meta.get("raw_imports", []))
            popularity = meta.get("popularity", 0) 

            log_logic_loc = math.log1p(logic_loc)
            log_imports_out = math.log1p(raw_imports_count)
            log_popularity_in = math.log1p(popularity)
            log_max_func_comp = math.log1p(max_func_comp)
            log_avg_func_args = math.log1p(avg_func_args)
            log_churn = math.log1p(raw_churn_freq)

            raw_vector = []
            for key in self.SIGNAL_SCHEMA:
                # ---> THE DIMENSIONAL FIX: Ignore hardware_bridge and cryptography <---
                if key in {"civil_war", "indent_tabs", "indent_spaces", "hardware_bridge", "cryptography"} or key.startswith("sec_"):
                    continue
                raw_hit = equations.get(key, 0)
                raw_density = (raw_hit / safe_denom) * 100.0
                raw_vector.append(math.log1p(raw_density))
                
            raw_vector.extend([
                cfr, log_logic_loc, log_imports_out, log_popularity_in,
                log_max_func_comp, log_avg_func_args, log_churn
            ])

            # ------------------------------------------------------------------
            # 1.6 BIAXIAL ANOMALY DETECTION (Global vs Local)
            # ------------------------------------------------------------------
            # A) GLOBAL MACRO-SPECIES
            scaled_vector_global = []
            for i, val in enumerate(raw_vector):
                median = self.SCALER_MEDIANS[i] if i < len(self.SCALER_MEDIANS) else 0.0
                safe_iqr = self.SCALER_IQRS[i] if i < len(self.SCALER_IQRS) and self.SCALER_IQRS[i] > 0 else 1.0 
                scaled_vector_global.append((val - median) / safe_iqr)

            global_archetype, global_drift, arch_fingerprint = self._classify_archetype(scaled_vector_global, self.GLOBAL_ARCHETYPES)
            
            # B) LOCAL MICRO-SPECIES
            local_archetype = None
            local_drift = 0.0
            local_fingerprint = {}

            lang_brain = self.LANGUAGE_INFERENCE_BRAINS.get(lang_id.lower())
            if lang_brain:
                lang_medians = lang_brain.get("SCALER_MEDIANS", [])
                lang_iqrs = lang_brain.get("SCALER_IQRS", [])

                # Find the dynamic K-key (e.g., ARCHETYPES_K11)
                arch_key = next((k for k in lang_brain.keys() if k.startswith('ARCHETYPES_K')), None)
                lang_archetypes = lang_brain.get(arch_key, {}) if arch_key else {}

                if lang_medians and lang_iqrs and lang_archetypes:
                    scaled_vector_local = []
                    for i, val in enumerate(raw_vector):
                        median = lang_medians[i] if i < len(lang_medians) else self.SCALER_MEDIANS[i]
                        iqr = lang_iqrs[i] if i < len(lang_iqrs) else self.SCALER_IQRS[i]
                        safe_iqr = iqr if iqr > 0 else 1.0
                        scaled_vector_local.append((val - median) / safe_iqr)

                    local_archetype, local_drift, local_fingerprint = self._classify_archetype(scaled_vector_local, lang_archetypes)

            # ------------------------------------------------------------------
            # 2. CORE RISK EXPOSURE CALCULATIONS
            # ------------------------------------------------------------------
            # ---> HIGHER-ORDER SYNTHESIS: The OOM (Out of Memory) Bomb <---
            # If O(N^3) or recursive, AND high flux, AND NO lazy_evaluation -> Massive Flux Multiplier
            oom_multiplier = 1.0
            if (max_big_o >= 3 or has_recursion) and equations.get("flux", 0) > 0:
                if equations.get("lazy_evaluation", 0) == 0:
                    oom_multiplier = 3.0 # Ticking OOM bomb (Bloating RAM)
                else:
                    oom_multiplier = 0.5 # Safely streamed (O(1) memory)
                    
            mp_map["flux"] = mp_map.get("flux", 1.0) * oom_multiplier
            # --------------------------------------------------------------

            cog_score, cog_raw = self._calc_cog_load(loc, equations, irc, fc, mp_map.get("cog", 1.0), func_gini)
            saf_score = self._calc_safety(loc, equations, irc, fc, mp_map.get("safety", 1.0))
            debt_score = self._calc_tech_debt(loc, equations, irc, mp_map.get("debt", 1.0))
            
            test_score = self._calc_verification(
                loc, rel_path, meta.get("is_protected", False), equations, irc, fc, mp_map.get("test", 1.0), umbrella_bonus=umbrella_bonus, popularity=popularity
            )
            
            doc_score = self._calc_documentation(loc, doc_lines, equations, fc, irc, mp_map.get("doc", 1.0), satellites)
            spec_score = self._calc_spec_alignment(equations, mp_map.get("spec", 1.0))
            
            bureaucracy_dampener = min(loc / 15.0, 1.0)
            test_score *= bureaucracy_dampener
            doc_score *= bureaucracy_dampener
            spec_score *= bureaucracy_dampener

            exposure_vector = {
                "cognitive_load": cog_score,
                "safety_score":   saf_score,
                "tech_debt":      debt_score,
                "verification":   test_score,
                "api_exposure":   self._calc_api_exposure(equations, total_loc, popularity),
                "concurrency":    self._calc_concurrency(loc, equations, irc, mp_map.get("async", 1.0), satellites),
                "state_flux":     self._calc_state_flux(loc, equations, irc, mp_map.get("flux", 1.0)),
                "graveyard":      self._calc_graveyard(total_loc, equations, mp_map.get("dead", 1.0)),
                "spec_match":     spec_score,
                "stability":      stability_score,
                "churn":          0.0, 
                "documentation":  doc_score,
                "civil_war":      self._calc_civil_war(equations),
                
                # ---> BIAXIAL WEAPONIZATION <---
                "obscured_payload":  self._calc_obscured_payload(loc, equations, mp_map.get("obscured", 1.0), global_archetype, global_drift, local_drift),
                "logic_bomb":        self._calc_logic_bomb(loc, equations, mp_map.get("logic_bomb", 1.0) * eco_mp.get("logic_bomb", 1.0), global_archetype, global_drift, local_drift),
                "injection_surface": self._calc_injection_surface(loc, equations, mp_map.get("injection", 1.0) * eco_mp.get("injection", 1.0), global_archetype),
                "memory_corruption": self._calc_memory_corruption(loc, equations, mp_map.get("memory", 1.0) * eco_mp.get("memory", 1.0), lang_id, global_archetype), 
                "secrets_risk":      self._calc_secrets_risk(loc, equations, mp_map.get("secrets", 1.0))
            }
            
            # ------------------------------------------------------------------
            # 3. VECTOR ASSEMBLY (Locked to RISK_SCHEMA order)
            # ------------------------------------------------------------------
            risk_vector_ordered = [round(exposure_vector[key], 4) for key in self.RISK_SCHEMA]

            # ------------------------------------------------------------------
            # 4. CALCULATE FILE IMPACT (The Mass)
            # ------------------------------------------------------------------
            satellites = meta.get("satellites", [])
            func_start = equations.get("func_start", 0)
            
            if satellites:
                sum_function_impacts = sum(sat.get("impact", 0) for sat in satellites)
            else:
                if func_start == 0:
                    temp_branches = 0
                    temp_args = 0
                else:
                    temp_branches = equations.get("branch", 0)
                    temp_args = equations.get("args", 0)
                    
                temp_signals = temp_branches + temp_args
                temp_effective_loc = min(loc, (temp_signals + 1) * 10)
                temp_arg_multiplier = math.sqrt(temp_args + 1)
                
                sum_function_impacts = ((temp_branches + 1) * temp_arg_multiplier + (0.05 * temp_effective_loc)) * 10
                
            api_exposure = equations.get("api", 0)
            concurrency = equations.get("concurrency", 0)
            flux = equations.get("flux", 0)
            
            file_mass = sum_function_impacts + api_exposure + concurrency + flux + (loc / 50.0)

            # ------------------------------------------------------------------
            # 5. EXECUTE OWNERSHIP ENTROPY MATH & SILO RISK
            # ------------------------------------------------------------------
            authors_map = meta.get("authors", {})
            ownership_score = self._calc_ownership_entropy(authors_map)
            silo_exposure = self._calculate_silo_risk(authors_map)
            
            if authors_map:
                dominant_author = max(authors_map, key=authors_map.get)
            else:
                dominant_author = ghost_meta.get("ownership", "Unknown Architect")
                
            telemetry_payload = {
                "archetype": global_archetype,
                "global_drift": global_drift,
                "archetype_fingerprint": arch_fingerprint,
                "local_archetype": local_archetype,
                "local_drift": local_drift,
                "local_fingerprint": local_fingerprint,
                "densities": {"cog_raw": round(cog_raw, 3)},
                "raw_churn_freq": raw_churn_freq,
                "func_complexity_gini": func_gini,
                "max_algorithmic_complexity": "O(2^N) [Recursive]" if has_recursion else (f"O(N^{max_big_o})" if max_big_o > 1 else "O(N)"),
                "max_db_complexity": max_db_complexity,
                "ownership_entropy": ownership_score,
                "author_distribution": silo_exposure,
                "ownership": dominant_author,          
                "domain_context": ghost_meta,
                "mitigation_telemetry": meta.get("mitigation_telemetry", {})
            }
            
            if mp_map:
                telemetry_payload["multipliers"] = mp_map

            return {
                "risk_vector": risk_vector_ordered,
                "hit_vector": hit_vector,
                "file_impact": round(file_mass, 2),
                "telemetry": telemetry_payload
            }

        except Exception as e:
            self.logger.error(f"Catastrophic physics failure on artifact '{rel_path}': {e}", exc_info=True)
            return {
                "risk_vector": [0.0] * len(self.RISK_SCHEMA),
                "hit_vector": [equations.get(k, 0) for k in self.SIGNAL_SCHEMA],
                "file_impact": max(loc / 50.0, 1.0),
                "telemetry": {"error": str(e)}
            }
                           
    # ==========================================================================
    # GLOBAL SYNTHESIS & 2-PASS NORMALIZATION
    # ==========================================================================

    def summarize_galaxy_metrics(self, stars: List[Dict[str, Any]], singularity: List[Dict[str, Any]]) -> Dict[str, Any]:
        """[GLOBAL SYNTHESIS] Executes Pass 2 Normalization and aggregates health metrics."""
        
        # Execute Pass 2: Temporal Normalization across the Universe
        self._normalize_temporal_metrics(stars)
        
        total_files = len(stars) + len(singularity)
        if total_files == 0: 
            return {}

        self.logger.info(f"Synthesizing galaxy metrics across {total_files} artifacts ({len(stars)} visible, {len(singularity)} dark matter)...")
        
        # Safely extract score averages from the risk_vector list via mapping
        def get_avg(metric_name):
            if metric_name not in self.RISK_SCHEMA: return 0.0
            idx = self.RISK_SCHEMA.index(metric_name)
            scores = [s["risk_vector"][idx] for s in stars if "risk_vector" in s and len(s["risk_vector"]) > idx]
            return round(statistics.mean(scores), 3) if scores else 0.0

        lang_comp = {}
        total_loc = 0
        for s in stars:
            lang = s.get("lang_id", "unknown")
            loc = s.get("coding_loc", 0)
            impact = s.get("file_impact", 0.0) # <-- ADD THIS
            total_loc += loc
            if lang not in lang_comp: 
                lang_comp[lang] = {"files": 0, "loc": 0, "impact": 0.0}
            lang_comp[lang]["files"] += 1
            lang_comp[lang]["loc"] += loc
            lang_comp[lang]["impact"] += impact # <-- ADD THIS

        churn_idx = self.RISK_SCHEMA.index("churn")
        high_volatility = len([s for s in stars if "risk_vector" in s and len(s["risk_vector"]) > churn_idx and s["risk_vector"][churn_idx] > 80.0])
        volatility_idx = round(high_volatility / max(len(stars), 1), 3)
        darkness_ratio = round(len(singularity) / max(total_files, 1), 3)

        self.logger.info(f"Synthesis Complete | Volatility Index: {volatility_idx:.2f} | Darkness Ratio: {darkness_ratio * 100:.1f}%")

        # --- NEW: Constellation Aggregation Logic ---
        constellations_data = {}
        for s in stars:
            c_name = s.get("constellation", "__monolith__")
            if c_name not in constellations_data: 
                constellations_data[c_name] = {"count": 0, "mass": 0.0, "risks": [0.0] * len(self.RISK_SCHEMA)}
            
            constellations_data[c_name]["count"] += 1
            constellations_data[c_name]["mass"] += s.get("file_impact", 0.0)
            
            for i, val in enumerate(s.get("risk_vector", [])):
                if i < len(self.RISK_SCHEMA): 
                    constellations_data[c_name]["risks"][i] += val
                    
        c_metrics = {
            name: {
                "file_count": data["count"], 
                "total_mass": round(data["mass"], 2), 
                "avg_exposures": {
                    self.RISK_SCHEMA[i]: round(data["risks"][i] / data["count"], 2) 
                    for i in range(len(self.RISK_SCHEMA))
                }
            } 
            for name, data in constellations_data.items()
        }

        # --- NEW: Ecosystem Fingerprint (Archetype Ratios) ---
        # --- NEW: Ecosystem Fingerprint (Archetype Ratios & Counts) ---
        archetype_counts = {}
        static_counts = {}
        
        for s in stars:
            arch = s.get("telemetry", {}).get("archetype", "Unknown")
            if arch.startswith("Static:"):
                static_counts[arch] = static_counts.get(arch, 0) + 1
            else:
                archetype_counts[arch] = archetype_counts.get(arch, 0) + 1
                
        ecosystem_fingerprint = {"ml_clusters": {}, "static_mass": {}}
        if len(stars) > 0:
            ecosystem_fingerprint["ml_clusters"] = {
                name: {"count": count, "pct": round((count / len(stars)) * 100.0, 1)}
                for name, count in sorted(archetype_counts.items(), key=lambda x: x[1], reverse=True)
            }
            ecosystem_fingerprint["static_mass"] = {
                name: {"count": count, "pct": round((count / len(stars)) * 100.0, 1)}
                for name, count in sorted(static_counts.items(), key=lambda x: x[1], reverse=True)
            }

        # --- NEW: AI TOPOLOGY & LLM INTELLIGENCE ---
        ai_sensor_keys = ["llm_api", "llm_orchestrator", "llm_vector_store", "llm_local_compute", "ai_tools", "ai_memory", "ai_logic_loop", "ml_traditional", "dl_frameworks"]
        ai_indices = {k: self.SIGNAL_SCHEMA.index(k) for k in ai_sensor_keys if k in self.SIGNAL_SCHEMA}
        
        # Isolate the physical files harboring AI logic
        ai_stars = []
        for s in stars:
            hv = s.get("hit_vector", [])
            star_ai_mass = sum(hv[idx] for k, idx in ai_indices.items() if idx < len(hv))
            if star_ai_mass > 0:
                ai_stars.append(s)

        llm_api_total = sum(s.get("hit_vector", [])[self.SIGNAL_SCHEMA.index("llm_api")] if "llm_api" in self.SIGNAL_SCHEMA and len(s.get("hit_vector", [])) > self.SIGNAL_SCHEMA.index("llm_api") else 0 for s in stars)
        llm_orch_total = sum(s.get("hit_vector", [])[self.SIGNAL_SCHEMA.index("llm_orchestrator")] if "llm_orchestrator" in self.SIGNAL_SCHEMA and len(s.get("hit_vector", [])) > self.SIGNAL_SCHEMA.index("llm_orchestrator") else 0 for s in stars)
        llm_vector_total = sum(s.get("hit_vector", [])[self.SIGNAL_SCHEMA.index("llm_vector_store")] if "llm_vector_store" in self.SIGNAL_SCHEMA and len(s.get("hit_vector", [])) > self.SIGNAL_SCHEMA.index("llm_vector_store") else 0 for s in stars)
        llm_local_total = sum(s.get("hit_vector", [])[self.SIGNAL_SCHEMA.index("llm_local_compute")] if "llm_local_compute" in self.SIGNAL_SCHEMA and len(s.get("hit_vector", [])) > self.SIGNAL_SCHEMA.index("llm_local_compute") else 0 for s in stars)
        
        # Agentic Sensors
        ai_tools_total = sum(s.get("hit_vector", [])[self.SIGNAL_SCHEMA.index("ai_tools")] if "ai_tools" in self.SIGNAL_SCHEMA and len(s.get("hit_vector", [])) > self.SIGNAL_SCHEMA.index("ai_tools") else 0 for s in stars)
        ai_memory_total = sum(s.get("hit_vector", [])[self.SIGNAL_SCHEMA.index("ai_memory")] if "ai_memory" in self.SIGNAL_SCHEMA and len(s.get("hit_vector", [])) > self.SIGNAL_SCHEMA.index("ai_memory") else 0 for s in stars)
        ai_loop_total = sum(s.get("hit_vector", [])[self.SIGNAL_SCHEMA.index("ai_logic_loop")] if "ai_logic_loop" in self.SIGNAL_SCHEMA and len(s.get("hit_vector", [])) > self.SIGNAL_SCHEMA.index("ai_logic_loop") else 0 for s in stars)

        # ML/DL Sensors
        ml_total = sum(s.get("hit_vector", [])[self.SIGNAL_SCHEMA.index("ml_traditional")] if "ml_traditional" in self.SIGNAL_SCHEMA and len(s.get("hit_vector", [])) > self.SIGNAL_SCHEMA.index("ml_traditional") else 0 for s in stars)
        dl_total = sum(s.get("hit_vector", [])[self.SIGNAL_SCHEMA.index("dl_frameworks")] if "dl_frameworks" in self.SIGNAL_SCHEMA and len(s.get("hit_vector", [])) > self.SIGNAL_SCHEMA.index("dl_frameworks") else 0 for s in stars)

        ai_topology = {"classification": "Non-AI / Traditional", "insights": []}
        
        total_ai_mass = llm_api_total + llm_orch_total + llm_vector_total + llm_local_total + ai_tools_total + ai_memory_total + ai_loop_total + ml_total + dl_total
        
        if total_ai_mass > 0:
            # Assess Agentic Autonomy First (Highest Complexity)
            if ai_loop_total > 0 and ai_tools_total > 0:
                ai_topology["classification"] = "Autonomous Agentic Fleet (Level 4)"
                ai_topology["insights"].append("High density of bound tools and cyclic reasoning loops (ReAct). Agents possess autonomy to execute code. Critical risk of non-deterministic runtime behavior.")
                if ai_memory_total == 0:
                    ai_topology["insights"].append("WARNING: High autonomy but low memory density. Agents may suffer from context amnesia between loops.")
            elif ai_tools_total > 0:
                ai_topology["classification"] = "Tool-Augmented LLM (Level 3)"
                ai_topology["insights"].append("LLM is explicitly bound to external functions/tools. High blast radius if prompt injection occurs.")
            elif llm_local_total > 0:
                ai_topology["classification"] = "Local Sovereignty (Heavy Compute)"
                ai_topology["insights"].append("Repository contains local model execution or tensor math. Expect heavy GPU memory allocation.")
            elif llm_vector_total > 0 and llm_api_total > 0:
                ai_topology["classification"] = "RAG Pipeline (Retrieval-Augmented Generation)"
                ai_topology["insights"].append("Active vector database integration detected. Architecture centers around data chunking and context retrieval.")
            elif llm_orch_total > (llm_api_total * 2):
                ai_topology["classification"] = "Framework-Heavy Orchestration"
                ai_topology["insights"].append("Heavy reliance on agentic frameworks (e.g., LangChain). High cognitive load and abstraction risk.")
            elif dl_total > 0:
                ai_topology["classification"] = "Deep Learning Architecture"
                ai_topology["insights"].append("Heavy neural network footprint detected (PyTorch/TensorFlow/JAX). Optimized for tensor math and gradient descent.")
            elif ml_total > 0:
                ai_topology["classification"] = "Statistical Machine Learning"
                ai_topology["insights"].append("Traditional ML architecture detected (XGBoost/Scikit-Learn). Focus on decision trees, regressions, and structured data.")
            else:
                ai_topology["classification"] = "Cloud API Wrapper"
                ai_topology["insights"].append("Thin wrapper around external LLM APIs. Low local compute mass, but high vendor lock-in risk.")
                
            # ---> N-DIMENSIONAL AI NETWORK POSTURE <---
            if ai_stars:
                # Find the most heavily relied-upon AI node in the graph
                ai_stars.sort(key=lambda x: x.get("telemetry", {}).get("network_metrics", {}).get("pagerank_score", 0.0), reverse=True)
                primary_ai_node = ai_stars[0]
                net_mets = primary_ai_node.get("telemetry", {}).get("network_metrics", {})
                
                role = net_mets.get("ecosystem_role", "Unknown")
                pr = net_mets.get("normalized_blast_radius", 0.0)
                btw = net_mets.get("betweenness_score", 0.0)
                
                ai_topology["insights"].append(f"Structural Posture: The primary AI integration acts as a '{role}' within the repository.")
                
                if pr > 1.0:
                    ai_topology["insights"].append(f"Systemic Risk (High): The AI components are deeply embedded with a massive Blast Radius (PageRank: {pr}). Hallucinations or prompt injections here will cascade catastrophically across the system.")
                elif pr < 0.2:
                    ai_topology["insights"].append("Containment (Low Risk): The AI components are safely isolated at the edge of the network with a minimal blast radius.")
                    
                if btw > 0.05:
                    ai_topology["insights"].append("Cognitive Choke Point: The AI sits on the shortest path between major system domains (High Betweenness). It is acting as an intelligent router, filter, or mandatory data transformer.")

            ai_topology["signal_mass"] = {
                "Cloud APIs": llm_api_total,
                "Orchestrators": llm_orch_total,
                "Vector Stores": llm_vector_total,
                "Local Compute": llm_local_total,
                "Agent Tools": ai_tools_total,
                "Agent Memory": ai_memory_total,
                "Agent Loops": ai_loop_total,
                "Traditional ML": ml_total,
                "Deep Learning": dl_total
            }

        # --- NEW: Repo Macro-Species Calculation ---
        repo_brain = getattr(config, "GENERAL_REPO_INFERENCE_MODEL", None)
        repo_macro_data = {"name": "Unclassified", "id": -1, "z_score": 0.0, "raw_drift": 0.0}
        
        if repo_brain and stars:
            # Rebuild the ratios based purely on the K-Means features
            feature_counts = {feat: archetype_counts.get(feat, 0) for feat in repo_brain["features"]}
            live_ratios = [feature_counts[feat] / len(stars) for feat in repo_brain["features"]]
            
            distances = []
            for i in range(repo_brain["k_clusters"]):
                centroid = repo_brain["centroids"][f"Cluster {i}"]
                dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(live_ratios, centroid)))
                distances.append(dist)
                
            assigned_idx = distances.index(min(distances))
            raw_drift = distances[assigned_idx]
            
            z_params = repo_brain["z_score_params"][f"Cluster {assigned_idx}"]
            z_score = (raw_drift - z_params["mean"]) / z_params["std"]
            
            cluster_names = repo_brain.get("cluster_names", [f"Cluster {i}" for i in range(repo_brain["k_clusters"])])
            
            repo_macro_data = {
                "name": cluster_names[assigned_idx],
                "id": assigned_idx,
                "z_score": round(z_score, 3),
                "raw_drift": round(raw_drift, 3)
            }
            
            # Inject into stars so security_auditor and gpu_recorder have it in RAM
            for s in stars:
                s["telemetry"]["repo_macro_species"] = assigned_idx
                s["telemetry"]["repo_z_score"] = repo_macro_data["z_score"]
                for i, d in enumerate(distances):
                    s["telemetry"][f"dist_to_{i}"] = d

        return {
            "summary": {
                "total_files": total_files,
                "visible_stars": len(stars),
                "total_loc": total_loc,
                "dominant_language": self._get_dominant_lang(lang_comp),
                "volatility_index": volatility_idx,
                "Percent_Visible": round((1 - darkness_ratio) * 100, 1)
            },
            "repo_macro_species": repo_macro_data,  # <--- NEW
            "singularity": {
                "ambig_file_count": len(singularity),
            },
            "singularity": {
                "ambig_file_count": len(singularity),
            },
            "health": {
                "avg_cognitive_load": get_avg("cognitive_load"),
                "avg_safety_score": get_avg("safety_score"),
                "avg_tech_debt": get_avg("tech_debt"),
                "avg_documentation": get_avg("documentation")
            },
            "composition": lang_comp,
            "ecosystem_fingerprint": ecosystem_fingerprint,
            "ai_topology": ai_topology,
            "constellations": c_metrics
        }
        
    def _normalize_temporal_metrics(self, stars: List[Dict[str, Any]]):
        """[PASS 2] Normalizes churn using a Logarithmic Curve for better UI gradients."""
        if not stars: return
        max_freq = 0.0
        
        # Pass 2.A: Find the volcano (Global Max)
        for s in stars:
            freq = s.get("telemetry", {}).get("raw_churn_freq", 0.0)
            if freq > max_freq:
                max_freq = freq
                
        # THE FIX: Apply a logarithmic curve to the maximum ceiling
        # math.log1p safely handles 0 values (log(1 + x))
        safe_max_f = math.log1p(max(max_freq, 1.0))
        idx = self.RISK_SCHEMA.index("churn")
        
        # Pass 2.B: Normalize every star against the logarithmic curve
        for s in stars:
            freq = s.get("telemetry", {}).get("raw_churn_freq", 0.0)
            
            # THE FIX: Apply the same logarithmic curve to the individual file
            base_score = (math.log1p(freq) / safe_max_f) * 100.0
            
            mp = s.get("telemetry", {}).get("multipliers", {}).get("churn", 1.0)
            final_churn = min(base_score * mp, 100.0)
            
            # Inject Churn directly into the correct Risk Vector index
            if "risk_vector" in s and len(s["risk_vector"]) > idx:
                s["risk_vector"][idx] = round(final_churn, 2)

    # ==========================================================================
    # FORENSIC EQUATIONS (The Physics Models)
    # ==========================================================================
   
    def _calc_raw_temporal_signals(self, temp: Dict[str, Any]) -> Tuple[float, float]:
        """Calculates Stability (Age) and Raw Churn (Seismic Frequency)."""
        if not temp or not temp.get("is_git_tracked", False):
            return 50.0, 0.0 

        mtime = temp.get("mtime", 0.0)
        repo_min = temp.get("repo_min_time", mtime)
        repo_max = temp.get("repo_max_time", mtime)
        commits = temp.get("commit_count", 0)

        # ---> THE FIX: Clamp the time difference so it never goes negative <---
        seconds_from_max = max(repo_max - mtime, 0.0)
        time_range = max(repo_max - repo_min, 1.0)
        
        # 1. Stability (0 = Newest/Surface, 100 = Oldest/Bedrock)
        stability_ratio = seconds_from_max / time_range
        stability_score = min(stability_ratio * 100.0, 100.0)

        # 2. Raw Churn Frequency 
        age_weeks = max(seconds_from_max / 604800.0, 1.0) 
        raw_churn_freq = commits / math.sqrt(age_weeks)
        
        return stability_score, raw_churn_freq

    def _calc_ownership_entropy(self, authors: Dict[str, int]) -> float:
        """
        Calculates Ownership Entropy (Shannon Entropy) for the file.
        0 = Single Author (Pure Ownership/Stable), 100 = Highly Distributed (Vibrating/White).
        """
        if not authors:
            return 0.0
            
        total_commits = sum(authors.values())
        if total_commits == 0:
            return 0.0
            
        entropy = 0.0
        for count in authors.values():
            if count > 0:
                p_i = count / total_commits
                entropy -= p_i * math.log2(p_i)
                
        # Scale to 0-100 score as defined in spec: OwnershipScore = min(H * 32, 100)
        ownership_score = min(entropy * 32.0, 100.0)
        
        return round(ownership_score, 2)

    def _calc_civil_war(self, eq: Dict[str, int]) -> float:
        """
        Calculates Layout Unity (Tabs vs Spaces). 
        0 = Pure Tabs (Green), 100 = Pure Spaces (Yellow), 50 = War Zone (Blue).
        """
        tab_lines = eq.get('indent_tabs', 0)
        space_lines = eq.get('indent_spaces', 0)
        
        l_total = tab_lines + space_lines
        
        # 2. Handle Void States (No indentation at all)
        if l_total == 0:
            return 50.0 # Default to Neutral Blue
            
        # 3. Calculate Space-Ratio (R)
        space_ratio = space_lines / l_total
        
        # 4. Final Score Mapping (0-100)
        return space_ratio * 100.0
    
    def _calc_cog_load(self, loc: int, eq: Dict[str, int], irc: int, fc: float, mp: float, func_gini: float = 0.0) -> Tuple[float, float]:
        safe_loc = max(loc, 1)
        t = self.risk_tuning.get("cognitive_load", {})
        
        if safe_loc < 15:
            total_density = sum([eq.get(k, 0) for k in ["branch", "flux", "concurrency", "heat_triggers", "danger"]]) / safe_loc + (irc / safe_loc)
            return 5.0, total_density
            
        branches = eq.get("branch", 0)
        if branches == 0 and safe_loc > 50:
            return 0.0, 0.0
            
        branch_density = branches / safe_loc
        flux_density = eq.get("flux", 0) / safe_loc
        concurrency_density = eq.get("concurrency", 0) / safe_loc
        heat_density = eq.get("heat_triggers", 0) / safe_loc
        danger_density = eq.get("danger", 0) / safe_loc
        
        clamped_branch = min(branch_density * 1.0, t.get("branch_clamp", 0.5))
        clamped_flux = min(flux_density * t.get("flux_mult", 2.0), t.get("flux_clamp", 0.75)) 
        heavy_logic = (concurrency_density * t.get("async_mult", 3.0)) + (heat_density * t.get("heat_mult", 5.0)) + (danger_density * t.get("danger_mult", 5.0))
        
        # ---> THE GOD FUNCTION PENALTY <---
        # If complexity is heavily skewed into a single massive function (High Gini),
        # reading the file requires jarring mental context switches. Spike the load.
        gini_multiplier = 1.0
        if func_gini > 0.7:
            gini_multiplier = 1.0 + (func_gini * 0.5)
            
        total_density = (clamped_branch + clamped_flux + heavy_logic + (irc / safe_loc)) * gini_multiplier
        
        if safe_loc <= 2 and total_density == 0:
            return 0.0, total_density
            
        try:
            raw_score = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 4.0) * (total_density - t.get("sigmoid_offset", 0.75))))
        except OverflowError:
            raw_score = 100.0 if total_density > t.get("sigmoid_offset", 0.75) else 0.0
            
        doc_coverage = (eq.get("doc", 0) * t.get("doc_mult", 10.0)) / safe_loc
        cooling = max(0.5, 1.0 - (doc_coverage * fc))
        
        return min(raw_score * cooling * mp, 100.0), total_density

    def _calc_safety(self, loc: int, eq: Dict[str, int], irc: int, fc: float, mp: float) -> float:
        safe_loc = max(loc, 1)
        t = self.risk_tuning.get("safety", {})
        
        attack_hits = (eq.get("danger", 0) * t.get("danger_weight", 4.0)) + (eq.get("safety_neg", 0) * t.get("safety_neg_weight", 1.5)) + (eq.get("flux", 0) * t.get("flux_weight", 0.5))
        defense_hits = (eq.get("safety", 0) * self.WEIGHT_DEFENSE) + (eq.get("test", 0) * t.get("test_weight", 0.5)) + (eq.get("doc", 0) * t.get("doc_weight", 0.1))
        
        if attack_hits == 0:
            return 0.0
            
        smoothed_loc = safe_loc + t.get("laplace_smoothing", 20.0)
        attack = ((attack_hits + irc) / smoothed_loc) * mp
        defense = (defense_hits / smoothed_loc) * fc
        
        systems_buffer = t.get("systems_buffer", 0.25) if fc < 1.0 else 0.0
        net_exposure = (attack - defense) - systems_buffer
        
        try:
            score = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 12.0) * net_exposure))
        except OverflowError:
            score = 100.0 if net_exposure > 0 else 0.0

        danger_density = (eq.get("danger", 0) + eq.get("safety_neg", 0)) / safe_loc
        if danger_density > t.get("breach_density_min", 0.03) and attack > defense:
            floor = min(t.get("breach_floor_max", 80.0), 30.0 + (danger_density * t.get("breach_floor_mult", 500.0)))
            score = max(score, floor)
            
        return max(score, 0.0)

    def _calc_tech_debt(self, loc: int, eq: Dict[str, int], irc: int, mp: float) -> float:
        t = self.risk_tuning.get("tech_debt", {})
        good_debt = eq.get("planned_debt", 0)
        bad_debt = eq.get("fragile_debt", eq.get("keyword_debt", 0))
        stubs = eq.get("func_empty", 0)
        
        # --- NEW: UNACKNOWLEDGED DEBT (SLOP) ---
        orphans = eq.get("design_slop_orphans", 0)
        duplicates = eq.get("design_slop_duplicates", 0)
        
        if good_debt == 0 and bad_debt == 0 and stubs == 0 and orphans == 0 and duplicates == 0:
            return 0.0
        
        # Slop carries a heavier baseline penalty because it is invisible to standard linters
        slop_stress = (orphans * 2.0) + (duplicates * 5.0)
        
        stress = (good_debt * t.get("good_debt_weight", 1.0)) + \
                 (bad_debt * t.get("bad_debt_weight", 3.0)) + \
                 (stubs * t.get("stub_weight", 0.5)) + \
                 (irc * t.get("irc_weight", 0.5)) + \
                 slop_stress
                 
        # If there is active slop AND acknowledged debt, they multiply each other's severity
        if slop_stress > 0 and (good_debt > 0 or bad_debt > 0):
            stress *= 1.5

        density = (stress / max(loc, 1)) * 100.0
        threshold = t.get("threshold", 5.0)
        
        try:
            raw_score = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 0.5) * (density - threshold)))
        except OverflowError:
            raw_score = 100.0 if density > threshold else 0.0
            
        return min(raw_score * mp, 100.0)

    def _calc_documentation(self, loc: int, doc_loc: int, eq: Dict[str, int], fc: float, irc: int, mp: float, satellites: List[Dict[str, Any]] = None) -> float:
        t = self.risk_tuning.get("documentation", {})
        weighted_points = (eq.get("doc", 0) * t.get("doc_weight", 1.0)) + (eq.get("ownership", 0) * t.get("ownership_weight", 0.5)) + (doc_loc * t.get("doc_loc_weight", 0.33))
        
        # ---> THE BLIND COMPLEXITY PENALTY <---
        # If the file contains incredibly heavy logic blocks or bad Big-O
        # but the specific functions lack docstrings, the baseline coverage is a lie.
        blind_penalty = 0.0
        if satellites:
            for sat in satellites:
                if (sat.get("impact", 0) > 50 or sat.get("big_o_depth", 1) >= 3) and not sat.get("docstring"):
                    blind_penalty += 15.0 # Flat 15% risk penalty per undocumented God Function

        density = (weighted_points / max(loc, 1)) * 100.0
        
        if loc <= 2 and doc_loc == 0:
            return 0
        
        threshold = (t.get("threshold_base", 10.0) + irc) * mp
        try:
            raw_risk = 100.0 / (1.0 + math.exp(t.get("sigmoid_slope", 0.2) * (density - threshold)))
        except OverflowError:
            raw_risk = 0.0 if density > threshold else 100.0
            
        return min((raw_risk * (2.0 - fc)) + blind_penalty, 100.0)

    def _calc_verification(self, loc: int, rel_path: str, is_protected: bool, eq: Dict[str, int], irc: int, fc: float, mp: float, umbrella_bonus: float = 0.0, popularity: int = 0) -> float:
        """
        YIN: Test assertions (test).
        YANG: Bypassed/Mocked tests (test_skip).
        Returns 100.0 for HIGH risk (no tests), 0.0 for LOW risk (well tested).
        """
        tuning = self.risk_tuning.get("verification", {})
        loc_padding = tuning.get("loc_padding", 150)
        
        test_hits = float(eq.get("test", 0))
        test_skips = float(eq.get("test_skip", 0))
        
        # THERMODYNAMIC BALANCE: Penalize "Safety Theater".
        # 1 bypassed test neutralizes 2 real assertions.
        true_verification = max(0.0, test_hits - (test_skips * 2.0))
        
        density = true_verification / max(loc + loc_padding, 1)
        
        threshold = tuning.get("threshold_base", 15.0)
        slope = tuning.get("sigmoid_slope", 0.25)
        
        # Calculate coverage (100% = fully tested)
        coverage = self._sigmoid(density, threshold, slope) * 100.0
        
        # Re-apply the architectural bonuses
        coverage = min(coverage + umbrella_bonus, 100.0)
        
        # Mass Penalty: Massive files require exponentially more tests to prove safety.
        mass_penalty = 0.0
        if loc > 300:
            mass_penalty = min(((loc - 300) / 100) * 5.0, 40.0)
            
        # ---> THE LOAD-BEARER PENALTY <---
        # If this file is a foundational pillar (highly imported), a lack of tests 
        # threatens the entire ecosystem.
        if popularity > 5:
            mass_penalty += min(popularity * 2.0, 30.0)
            
        final_coverage = max(0.0, coverage - mass_penalty)
        
        # INVERT FOR RISK: 100% Coverage = 0% Risk Exposure.
        return 100.0 - final_coverage
    
    def _calc_graveyard(self, total_loc: float, eq: Dict[str, int], mp: float) -> float:
        hits = eq.get("graveyard", 0)
        if hits == 0:
            return 0.0
            
        t = self.risk_tuning.get("graveyard", {})
        ghost_lines = hits * t.get("hit_mult", 3.0)
        density = (ghost_lines / max(total_loc, t.get("safe_mass_floor", 50.0))) * 100.0
        
        threshold = t.get("threshold_base", 10.0) / max(mp, 0.1) 
        try:
            score = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 0.3) * (density - threshold)))
        except OverflowError:
            score = 100.0 if density > threshold else 0.0
            
        return min(score, 100.0)

    def _calc_api_exposure(self, eq: dict, total_loc: int, popularity: int = 0) -> float:
        """
        YIN: Publicly exposed surfaces (api).
        YANG: Internal/Private boundaries (encapsulation).
        """
        api_hits = float(eq.get("api", 0))
        encapsulation = float(eq.get("encapsulation", 0))
        
        if api_hits == 0:
            return 0.0
            
        # THERMODYNAMIC BALANCE (Ratio): Public / (Public + Private)
        exposure_ratio = api_hits / max(api_hits + encapsulation, 1.0)
        
        # ---> THE ECHO CHAMBER FIX <---
        # If a file exposes 50 APIs but has 0 inbound network edges, it's screaming into the void.
        # We dampen the risk. If it has massive popularity, we amplify it.
        network_multiplier = 1.0
        if popularity == 0:
            network_multiplier = 0.2 # 80% reduction for orphaned APIs
        else:
            network_multiplier = min(1.0 + (math.log1p(popularity) / 5.0), 2.0)
            
        # LOGARITHMIC MASS CORRECTION
        volume_weight = math.log1p(api_hits) / math.log1p(max(total_loc, 10))
        
        return min(exposure_ratio * volume_weight * network_multiplier * 100.0, 100.0)

    def _calc_concurrency(self, loc: int, eq: Dict[str, int], irc: int, mp: float, satellites: List[Dict[str, Any]] = None) -> float:
        """
        YIN: Threads/Async execution + Thread Starvation (O(N) Bombs).
        YANG: Mutex/Locks/Semaphores (sync_locks).
        """
        tuning = self.risk_tuning.get("concurrency", {})
        loc_padding = tuning.get("loc_padding", 150)
        
        raw_concurrency = float(eq.get("concurrency", 0))
        sync_locks = float(eq.get("sync_locks", 0))
        
        # --- THE THREAD STARVATION BOMB ---
        # If an individual function has concurrency hits AND terrible Big-O, it spikes the risk.
        starvation_multiplier = 1.0
        if satellites:
            for sat in satellites:
                if sat.get("hit_vector", {}).get("concurrency", 0) > 0:
                    big_o = sat.get("big_o_depth", 1)
                    is_rec = sat.get("is_recursive", False)
                    if is_rec:
                        starvation_multiplier = max(starvation_multiplier, 5.0)
                    elif big_o >= 3:
                        starvation_multiplier = max(starvation_multiplier, 4.0)
                    elif big_o == 2:
                        starvation_multiplier = max(starvation_multiplier, 2.0)
        
        # THERMODYNAMIC BALANCE: 1 lock mitigates 1.5 thread spawns.
        net_concurrency = max(0.0, raw_concurrency - (sync_locks * 1.5))
        
        if net_concurrency == 0:
            return 0.0
            
        density = (net_concurrency * starvation_multiplier) / max(loc + loc_padding, 1)
        
        threshold = tuning.get("threshold_base", 4.0) # Matches your config!
        slope = tuning.get("sigmoid_slope", 0.4)
        
        return self._sigmoid(density, threshold, slope) * 100.0 * mp

    def _calc_state_flux(self, loc: int, eq: Dict[str, int], irc: int, mp: float) -> float:
        """
        YIN: State mutation (flux).
        YANG: Immutability enforcements (freeze_hits).
        """
        tuning = self.risk_tuning.get("state_flux", {})
        
        # THE FIX: Dropped padding to 0 so mutations immediately impact density
        loc_padding = tuning.get("loc_padding", 0) 
        
        raw_flux = float(eq.get("flux", 0))
        freeze_hits = float(eq.get("freeze_hits", 0))
        
        # THERMODYNAMIC BALANCE: Subtract immutability from raw mutation.
        net_volatility = max(0.0, raw_flux - (freeze_hits * 0.5))
        
        if net_volatility == 0:
            return 0.0
            
        density = net_volatility / max(loc + loc_padding, 1)
        
        # THE FIX: Dropped threshold from 45.0 back to the original 15.0
        threshold = tuning.get("threshold_base", 15.0)
        slope = tuning.get("sigmoid_slope", 0.2)
        
        return self._sigmoid(density, threshold, slope) * 100.0 * mp
    
    def _calc_spec_alignment(self, eq: Dict[str, int], mp: float) -> float:
        entities = max(eq.get("func_start", 0) + eq.get("class_start", 0), 1)
        ratio = min(eq.get("spec_exposure", 0) / entities, 1.0)
        return min((1.0 - ratio) * 100.0 * mp, 100.0)

    def _sigmoid(self, density: float, threshold: float, slope: float) -> float:
        """Safely calculates the sigmoid curve, clamping extreme densities."""
        try:
            return 1.0 / (1.0 + math.exp(-slope * (density - threshold)))
        except OverflowError:
            return 1.0 if density > threshold else 0.0
    
    def _calc_obscured_payload(self, loc: int, eq: Dict[str, int], mp: float, archetype: str, global_drift: float, local_drift: float) -> float:
        """
        Calculates Obscured Payload Exposure (Malicious Intent Density).
        Combines passive Security Lens observers with hardcoded secret detection.
        """
        # Fetch the archetype multiplier
        arch_matrix = self.ARCHETYPE_VIOLATION_MATRIX.get(archetype, {})
        arch_multiplier = arch_matrix.get("obscured_payload_multiplier", 1.0)
        
        glassworm = (eq.get("sec_heat_triggers", 0) * 5.0) + (eq.get("sec_bitwise_hits", 0) * 2.0)
        trojan = eq.get("sec_safety_neg", 0) * 3.0
        exfiltration = eq.get("sec_io", 0) * 4.0
        executioner = eq.get("sec_danger", 0) * 5.0
        poisoning = eq.get("sec_flux", 0) * 3.0
        shadow_logic = eq.get("sec_graveyard", 0) * 2.0
        secrets = eq.get("sec_private_info", 0) * 1.5
        
        # Extension mismatch is proof of active evasion. Assign it a massive 20.0x mass.
        steganography = (eq.get("sec_shadow_imports", 0) * 10.0) + (eq.get("sec_extension_mismatch", 0) * 20.0)
        
        # DOWNGRADE: Greek letters in math/science libs are normal. Drop from 10.0 to 1.0.
        unicode_smuggling = eq.get("sec_homoglyphs", 0) * 1.0

        # 1. Group the threat vectors into Behavior vs Intent
        obfuscation_mass = glassworm + shadow_logic + steganography + unicode_smuggling
        intent_mass = trojan + exfiltration + executioner + poisoning + secrets
        
        # ---> THE AGENTIC / SCIENCE SHIELD <---
        # Forgive scientific/math libraries for having high entropy and weird unicode.
        science_dampener = 1.0 + (eq.get("scientific", 0) * 2.0)
        obfuscation_mass = obfuscation_mass / science_dampener

        # ---> APPLY THE ARCHETYPE CONTEXT <---
        total_threat_mass = (obfuscation_mass + intent_mass) * arch_multiplier
        
        if total_threat_mass == 0:
            return 0.0

        if not getattr(self, 'is_paranoid', False):
            if obfuscation_mass > 0 and intent_mass == 0: total_threat_mass *= 0.05  
            elif intent_mass > 0 and obfuscation_mass == 0: total_threat_mass *= 0.10  

        # ---> THE BIAXIAL TROJAN SPIKE <---
        if local_drift > 0 and global_drift > 0:
            drift_delta = local_drift / global_drift
            # If the file blends in globally but violates local language physics
            if drift_delta > 1.5:
                total_threat_mass *= drift_delta 

        # ---> NEW: THE PROFESSIONALISM QUOTIENT & CRYPTO SHIELD <---
        # Malware authors don't write 500 lines of documentation or meticulous try/catch blocks.
        docs_and_safety = (eq.get("doc", 0) * 0.5) + eq.get("safety", 0)
        prof_dampener = 1.0 + (docs_and_safety * 0.05) 
        
        # Cryptography libraries naturally have high entropy/obfuscation.
        crypto_dampener = 1.0 + (eq.get("cryptography", 0) * 5.0)

        # Apply the dampeners
        total_threat_mass = (total_threat_mass / prof_dampener) / crypto_dampener

        # 3. Fetch the decoupled tuning parameters from the standards configuration
        t = self.risk_tuning.get("obscured_payload", {})
        
        # 4. Use the dynamically fetched LOC padding (+150 by default)
        density = (total_threat_mass / max(loc + t.get("loc_padding", 150), 1)) * 100.0

        # 5. Use the dynamically fetched thresholds based on the active mode
        if getattr(self, 'is_paranoid', False):
            threshold = t.get("paranoid_threshold", 2.0)
            slope = t.get("paranoid_slope", 1.5)
        else:
            threshold = t.get("std_threshold", 15.0)
            slope = t.get("std_slope", 1.0)

        try:
            score = 100.0 / (1.0 + math.exp(-slope * (density - threshold)))
        except OverflowError:
            score = 100.0 if density > threshold else 0.0

        return min(score * mp, 100.0)
    
    def _calc_logic_bomb(self, loc: int, eq: Dict[str, int], mp: float, archetype: str, global_drift: float, local_drift: float) -> float:        
        """
        Calculates Logic Bomb / Sabotage Exposure.
        Looks for delayed or condition-heavy execution leading to destructive commands.
        """
        # Fetch the archetype multiplier
        arch_matrix = self.ARCHETYPE_VIOLATION_MATRIX.get(archetype, {})
        arch_multiplier = arch_matrix.get("logic_bomb_multiplier", 1.0)

        trigger = eq.get("branch", 0) + (eq.get("halt_hits", 0) * 3.0)
        payload = (eq.get("bailout_hits", 0) * 2.0) + (eq.get("cleanup", 0) * 1.5) + (eq.get("sec_danger", 0) * 4.0)

        # ---> THE AGENTIC SHIELD <---
        # AI/Robotics natively use dynamic execution. Dampen the payload if ML math is present.
        agent_dampener = 1.0 + (eq.get("scientific", 0) * 2.0) + (eq.get("llm_orchestrator", 0) * 3.0) + (eq.get("llm_local_compute", 0) * 2.0)
        hardware_dampener = 1.0 + (eq.get("hardware_bridge", 0) * 3.0)
        payload = payload / agent_dampener
        payload = payload / hardware_dampener
        
        # ---> APPLY THE ARCHETYPE CONTEXT <---
        sabotage_mass = (trigger * payload) * arch_multiplier

        # ---> THE TAINT SPIKE <---
        # If the LHS Slicer confirmed data crossed from I/O to Danger, risk is absolute.
        taint_confirmed = eq.get("sec_tainted_injection", 0)
        if taint_confirmed > 0: sabotage_mass += (taint_confirmed * 500.0) 

        # ---> THE BIAXIAL TROJAN SPIKE <---
        if local_drift > 0 and global_drift > 0:
            drift_delta = local_drift / global_drift
            if drift_delta > 1.5:
                sabotage_mass *= drift_delta 

        if sabotage_mass == 0: return 0.0

        explicit_threats = eq.get("sec_graveyard", 0) + eq.get("sec_heat_triggers", 0)
        if explicit_threats == 0 and taint_confirmed == 0 and getattr(self, 'is_paranoid', False) == False:
            sabotage_mass *= 0.05

        # Fetch tuning parameters
        t = self.risk_tuning.get("logic_bomb", {})
        density = (sabotage_mass / max(loc + t.get("loc_padding", 150), 1)) * 100.0

        if getattr(self, 'is_paranoid', False):
            threshold = t.get("paranoid_threshold", 10.0)
            slope = t.get("paranoid_slope", 0.5)
        else:
            threshold = t.get("std_threshold", 75.0)
            slope = t.get("std_slope", 0.2)

        try:
            score = 100.0 / (1.0 + math.exp(-slope * (density - threshold)))
        except OverflowError:
            score = 100.0 if density > threshold else 0.0

        return min(score * mp, 100.0)
    
    def _calc_injection_surface(self, loc: int, eq: Dict[str, int], mp: float, archetype: str) -> float:
        """
        Calculates Injection Surface Exposure (XSS, SQLi, RCE, SSTI).
        Looks for external network input flowing near dynamic execution without safety nets.
        """
        # Fetch the archetype multiplier
        arch_matrix = self.ARCHETYPE_VIOLATION_MATRIX.get(archetype, {})
        arch_multiplier = arch_matrix.get("injection_surface_multiplier", 1.0)

        input_vectors = eq.get("sec_io", 0) + (eq.get("ssr_boundaries", 0) * 2.0)
        execution_vectors = (eq.get("sec_danger", 0) * 4.0) + (eq.get("sec_safety_neg", 0) * 2.0)
        
        # ---> THE AGENTIC RCE SPIKE (Prompt Injection to Exec) <---
        if eq.get("sec_danger", 0) > 0 and (eq.get("llm_orchestrator", 0) > 0 or eq.get("ai_tools", 0) > 0):
            # If an AI can trigger eval/exec/OS commands, it's a massive vulnerability
            execution_vectors *= 10.0
            input_vectors += 5.0 # Treat the LLM itself as a hostile input vector
        else:
            # ---> THE AGENTIC SHIELD (Standard safe agents) <---
            agent_dampener = 1.0 + (eq.get("scientific", 0) * 2.0) + (eq.get("llm_local_compute", 0) * 2.0)
            execution_vectors = execution_vectors / agent_dampener
        
        # Hardware bridges natively take external input (usb/serial) and execute it.
        hardware_dampener = 1.0 + (eq.get("hardware_bridge", 0) * 3.0)
        execution_vectors = execution_vectors / hardware_dampener

        # ---> APPLY THE ARCHETYPE CONTEXT <---
        injection_mass = (input_vectors * execution_vectors) * arch_multiplier

        # ---> THE TAINT SPIKE <---
        taint_confirmed = eq.get("sec_tainted_injection", 0)
        if taint_confirmed > 0:
            injection_mass += (taint_confirmed * 500.0) # Massive gravity spike

        if injection_mass == 0:
            return 0.0
            
        explicit_threats = eq.get("sec_danger", 0) + eq.get("sec_io", 0)
        if explicit_threats == 0 and taint_confirmed == 0 and getattr(self, 'is_paranoid', False) == False:
            injection_mass *= 0.10

        # Fetch tuning parameters
        t = self.risk_tuning.get("injection_surface", {})
        density = (injection_mass / max(loc + t.get("loc_padding", 150), 1)) * 100.0

        if getattr(self, 'is_paranoid', False):
            threshold = t.get("paranoid_threshold", 3.0)
            slope = t.get("paranoid_slope", 1.2)
        else:
            threshold = t.get("std_threshold", 40.0)
            slope = t.get("std_slope", 0.4)

        try:
            score = 100.0 / (1.0 + math.exp(-slope * (density - threshold)))
        except OverflowError:
            score = 100.0 if density > threshold else 0.0

        return min(score * mp, 100.0)
    
    def _calc_memory_corruption(self, loc: int, eq: Dict[str, int], mp: float, lang_id: str = "", archetype: str = "") -> float:
        """
        Calculates Memory Corruption Exposure (Buffer Overflows, UAF).
        Strictly Opt-In: Only applies to languages with manual memory/pointers.
        """
        # Fetch the archetype multiplier
        arch_matrix = self.ARCHETYPE_VIOLATION_MATRIX.get(archetype, {})
        arch_multiplier = arch_matrix.get("memory_corruption_multiplier", 1.0)
        
        # ---> THE ARCHITECTURAL FIX: Opt-In Vulnerability Whitelist <---
        native_memory_langs = {"c", "cpp", "objective-c", "rust", "zig", "assembly", "agc_assembly", "nim"}
        
        # If it's not a native memory language, it physically cannot have these exploits.
        if lang_id.lower() not in native_memory_langs:
            return 0.0

        raw_memory_mass = (eq.get("pointers", 0) * 2.5) + \
                          (eq.get("memory_alloc", 0) * 3.0) + \
                          (eq.get("inline_asm", 0) * 5.0) + \
                          (eq.get("cast_hits", 0) * 1.5)

        if raw_memory_mass == 0:
            return 0.0

        mitigation_mass = eq.get("cleanup", 0) + (eq.get("safety", 0) * 1.5)
        
        net_risk = max(raw_memory_mass - mitigation_mass, 0.0) * arch_multiplier
                
        explicit_threats = eq.get("sec_danger", 0) + eq.get("sec_safety_neg", 0) + eq.get("sec_heat_triggers", 0)
        if explicit_threats == 0 and getattr(self, 'is_paranoid', False) == False:
            net_risk *= 0.05

        # 1. Fetch the decoupled tuning parameters
        t = self.risk_tuning.get("memory_corruption", {})

        # 2. Use the dynamically fetched LOC padding
        density = (net_risk / max(loc + t.get("loc_padding", 150), 1)) * 100.0

        # 3. Use the dynamically fetched thresholds based on the active mode
        if getattr(self, 'is_paranoid', False):
            threshold = t.get("paranoid_threshold", 4.0)
            slope = t.get("paranoid_slope", 0.8)
        else:
            threshold = t.get("std_threshold", 25.0)
            slope = t.get("std_slope", 0.4)

        try:
            score = 100.0 / (1.0 + math.exp(-slope * (density - threshold)))
        except OverflowError:
            score = 100.0 if density > threshold else 0.0

        return min(score * mp, 100.0)
    
    def _calc_secrets_risk(self, loc: int, eq: Dict[str, int], mp: float) -> float:
        """
        Calculates Secrets Risk Exposure (Data Hemorrhage).
        Looks for hardcoded credentials. Trusts the SecurityLens RHS-string sensor.
        """
        base_leak = eq.get("sec_private_info", 0) * 10.0
        
        if base_leak == 0:
            return 0.0

        careless_amplifiers = 1.0 + eq.get("print_hits", 0) + eq.get("graveyard", 0) + eq.get("globals", 0)
        
        # LLM API keys are massive targets. If they are calling APIs without globals, spike the risk.
        if eq.get("llm_api", 0) > 0 and eq.get("globals", 0) == 0:
            careless_amplifiers *= 3.0

        if getattr(self, 'is_paranoid', False) == False and eq.get("sec_heat_triggers", 0) == 0:
            careless_amplifiers = min(careless_amplifiers, 2.0)

        leak_mass = base_leak * careless_amplifiers

        # 1. Fetch the decoupled tuning parameters
        t = self.risk_tuning.get("secrets_risk", {})

        # 2. Use the dynamically fetched LOC padding (defaults to 50 because secrets are highly sensitive regardless of file size)
        density = (leak_mass / max(loc + t.get("loc_padding", 50), 1)) * 100.0

        # 3. Use the dynamically fetched thresholds based on the active mode
        if getattr(self, 'is_paranoid', False):
            threshold = t.get("paranoid_threshold", 0.5)
            slope = t.get("paranoid_slope", 2.0)
        else:
            threshold = t.get("std_threshold", 3.0)
            slope = t.get("std_slope", 1.0)

        try:
            score = 100.0 / (1.0 + math.exp(-slope * (density - threshold)))
        except OverflowError:
            score = 100.0 if density > threshold else 0.0

        if score < 5.0:
            score = 0.0

        return min(score * mp, 100.0)
    
    # --------------------------------------------------------------------------
    # REPORTING UTILITIES
    # --------------------------------------------------------------------------

    def generate_forensic_report(self, stars: List[Dict[str, Any]]) -> Dict[str, Any]:
        """[FORENSIC RANKING] Generates Top/Bottom 3 for dynamically indexed exposures."""
        if not stars: return {}
        self.logger.info("Generating forensic exposure rankings...")

        # ====================================================================
        # THE ACTIVE LOGIC MASK
        # 1. Define the structural assets that should be invisible to risk rankings
        # ====================================================================
        STRUCTURAL_ASSETS = self.asset_masks.get("STRUCTURAL_ASSETS", set())

        # 2. Filter the stars to ONLY include active executable logic
        active_stars = [
            star for star in stars 
            if star.get("lang_id", "unknown").lower() not in STRUCTURAL_ASSETS
        ]

        # 3. Fallback: If a repo is *only* markdown/data files, don't crash
        if not active_stars:
            active_stars = stars

        # ====================================================================
        # NEW: CALCULATE CUMULATIVE RISK (Excluding Civil War)
        # ====================================================================
        civil_war_idx = self.RISK_SCHEMA.index("civil_war") if "civil_war" in self.RISK_SCHEMA else -1
        
        def get_cumulative_risk(s):
            rv = s.get("risk_vector", [])
            # Sum all exposures except civil_war
            return sum(val for i, val in enumerate(rv) if i != civil_war_idx and i < len(rv))

        sorted_by_cumulative = sorted(active_stars, key=get_cumulative_risk, reverse=True)

        # --- NEW: CALCULATE N-DIMENSIONAL SYSTEMIC BOTTLENECKS ---
        flux_idx = self.RISK_SCHEMA.index("state_flux") if "state_flux" in self.RISK_SCHEMA else -1
        err_idx = self.RISK_SCHEMA.index("safety_score") if "safety_score" in self.RISK_SCHEMA else -1
        doc_idx = self.RISK_SCHEMA.index("documentation") if "documentation" in self.RISK_SCHEMA else -1
        
        bottlenecks = {"contagious_mutation": [], "house_of_cards": [], "blind_bottleneck": []}
        
        for s in active_stars:
            net = s.get("telemetry", {}).get("network_metrics", {})
            rv = s.get("risk_vector", [])
            p = s.get("path", "")
            
            btw = net.get("betweenness_score", 0.0)
            close = net.get("closeness_score", 0.0)
            pr = net.get("normalized_blast_radius", 0.0)
            
            flux_risk = rv[flux_idx] if flux_idx >= 0 and len(rv) > flux_idx else 0.0
            err_risk = rv[err_idx] if err_idx >= 0 and len(rv) > err_idx else 0.0
            doc_risk = rv[doc_idx] if doc_idx >= 0 and len(rv) > doc_idx else 0.0
            
            bottlenecks["contagious_mutation"].append({"path": p, "score": round(btw * flux_risk, 3), "btw": round(btw, 4), "flux": flux_risk})
            bottlenecks["house_of_cards"].append({"path": p, "score": round(close * err_risk, 3), "close": round(close, 4), "err": err_risk})
            bottlenecks["blind_bottleneck"].append({"path": p, "score": round(pr * doc_risk, 3), "pr": round(pr, 4), "doc": doc_risk})
            
        bottlenecks["contagious_mutation"].sort(key=lambda x: x["score"], reverse=True)
        bottlenecks["house_of_cards"].sort(key=lambda x: x["score"], reverse=True)
        bottlenecks["blind_bottleneck"].sort(key=lambda x: x["score"], reverse=True)

        # 4. Generate rankings using ONLY the masked `active_stars` list
        report = {
            "exposures": {},
            "file_impact": self._rank_list(active_stars, key_path=["file_impact"]),
            "function_impact": self._generate_function_rankings(active_stars),
            "systemic_bottlenecks": {k: v[:5] for k, v in bottlenecks.items()},
            # Inject the new Cumulative Risk ranking directly into the root of the report
            "cumulative_risk": {
                "highest": [{"name": s.get("name", "unknown"), "path": s.get("path", ""), "value": round(get_cumulative_risk(s), 2)} for s in sorted_by_cumulative[:10]],
                "lowest": [{"name": s.get("name", "unknown"), "path": s.get("path", ""), "value": round(get_cumulative_risk(s), 2)} for s in reversed(sorted_by_cumulative[-3:])]
            }
        }

        for idx, rk in enumerate(self.RISK_SCHEMA):
            report["exposures"][rk] = self._rank_list(active_stars, key_path=["risk_vector", idx])
            
        return report
    
    def _get_locational_multipliers(self, path: str) -> Dict[str, float]:
        """Matches path against regex configurations and extracts applicable Modifiers."""
        active_multipliers = {}
        bridge = {
            'Cognitive Load Exposure': 'cog', 
            'Error & Exception Exposure': 'safety',
            'Tech Debt Exposure': 'debt', 
            'Documentation Exposure': 'doc',
            'Testing Exposure': 'test', 
            'Dead Code Exposure': 'dead',
            'API Exposure': 'api', 
            'Concurrency Exposure': 'async',
            'State Flux Exposure': 'flux', 
            'Specification Exposure': 'spec',
            'Churn Exposure': 'churn', 
            
            # --- SECURITY LENSES ---
            'Obscured Payload Exposure': 'obscured',
            'Logic Bomb Exposure': 'logic_bomb',
            'Injection Vector Exposure': 'injection',
            'Memory Corruption Exposure': 'memory',
            'Hardcoded Secrets Exposure': 'secrets'
        }

        for category, modifiers in self.path_modifiers.items():
            signal_key = bridge.get(category)
            if not signal_key: continue
            
            for pattern, multiplier in modifiers:
                if hasattr(pattern, 'search') and pattern.search(path):
                    active_multipliers[signal_key] = multiplier
                    break
                elif isinstance(pattern, str) and re.search(pattern, path):
                    active_multipliers[signal_key] = multiplier
                    break
                    
        return active_multipliers

    def _rank_list(self, stars: List[Dict[str, Any]], key_path: List[Any]) -> Dict[str, List[Dict[str, Any]]]:
        """Extracts top and bottom ranks safely navigating dictionaries and lists."""
        def get_val(s):
            curr = s
            for k in key_path: 
                if isinstance(curr, dict):
                    curr = curr.get(k, 0.0)
                elif isinstance(curr, list) and isinstance(k, int) and k < len(curr):
                    curr = curr[k]
                else:
                    return 0.0
            return float(curr) if isinstance(curr, (int, float)) else 0.0
        
        sorted_stars = sorted(stars, key=get_val, reverse=True)
        return {
            "highest": [{"name": s.get("name", "unknown"), "path": s.get("path", ""), "value": get_val(s)} for s in sorted_stars[:3]],
            "lowest": [{"name": s.get("name", "unknown"), "path": s.get("path", ""), "value": get_val(s)} for s in reversed(sorted_stars[-3:])]
        }

    def _generate_function_rankings(self, stars: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        all_funcs = []
        for s in stars:
            for sat in s.get("satellites", []):
                if isinstance(sat, dict):
                    all_funcs.append({
                        "name": sat.get("name", "anon"), 
                        "file": s.get("name", "unknown"), 
                        "impact": sat.get("impact", 0), 
                        "loc": sat.get("loc", 0)
                    })
        all_funcs.sort(key=lambda x: x["impact"], reverse=True)
        return {"highest": all_funcs[:3], "lowest": all_funcs[-3:] if len(all_funcs) >= 3 else all_funcs}

    def _get_tier(self, lang_id: str) -> str:
        explicit = {'rust', 'go', 'swift', 'java', 'typescript', 'csharp', 'dart'}
        structured = {'python', 'javascript', 'cpp', 'c', 'ruby', 'kotlin', 'php'}
        if lang_id in explicit: return "tier1"
        if lang_id in structured: return "tier2"
        return "tier3"

    def _get_dominant_lang(self, composition: Dict[str, Dict[str, Any]]) -> str:
        if not composition: return "mixed"
        # Sort by active structural impact instead of raw lines of code
        return max(composition.items(), key=lambda x: x[1].get('impact', 0.0))[0]