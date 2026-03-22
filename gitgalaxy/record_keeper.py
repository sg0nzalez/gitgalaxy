import json
import logging
import math
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Any, Optional

# ==============================================================================
# GitGalaxy Phase 8: Record Keeper (The Astrograph)
# Strategy v6.2.0 Protocol: Columnar Pivot, GPU-Native Formatting & SBOM
# ==============================================================================

class SchemaCorruptionError(Exception):
    """Raised when parallel arrays in the columnar pivot lose alignment or type integrity."""
    pass

class RecordKeeper:
    """
    The GitGalaxy Record Keeper (Astrograph).
    
    PURPOSE: Transforms row-based forensic data into a miniaturized columnar 
    manifest. Optimized for GPU-native rendering, minimal memory footprint, 
    and forensic transparency.
    """

    def __init__(self, version: str, parent_logger: Optional[logging.Logger] = None):
        """Initializes lookups, standardizes schemas, and synchronizes telemetry."""
        self.version = version
        
        if parent_logger:
            self.logger = parent_logger.getChild("recordkeeper")
            self.logger.setLevel(parent_logger.level)
        else:
            self.logger = logging.getLogger("recordkeeper")
            self.logger.setLevel(logging.INFO) 

        self.logger.debug("Initializing Record Keeper (Astrograph) schemas...")

        # --- FIXED SCHEMAS (Position-Sensitive) ---
        self.RISK_SCHEMA = [
            "cognitive_load", "safety_score", "tech_debt", "verification", 
            "api_exposure", "concurrency", "state_flux", "graveyard", 
            "spec_match", "stability", "churn", "documentation", "civil_war"
        ]
        
        self.HIT_SCHEMA = [
            "branch", "args", "linear", "func_start", "class_start", "import", "api", "decorators",
            "safety", "safety_neg", "danger", "flux", "heat_triggers", "keyword_debt", "private_info",
            "io", "concurrency", "ui_framework", "events", "ssr_boundaries", "dependency_injection",
            "scientific", "generics", "comprehensions", "closures", "globals", "telemetry", "test",
            "macros", "pointers", "memory_alloc", "inline_asm", "func_empty",
            "graveyard", "doc", "ownership", "spec_exposure", "planned_debt", "fragile_debt", "civil_war",
            "indent_tabs", "indent_spaces" # <--- Added these to maintain perfect alignment!
        ]
        
        self.SAT_SCHEMA = ["name", "loc", "branch", "angle_x10", "args", "type_id", "ratio_x1000", "mag_x10"]
        self.GALAXY_SCHEMA = ["names", "paths", "lang_ids", "locs", "m_locs", "mass", "entropy", "pos_x", "pos_y", "pos_z"]
        
        # String Interning Registries
        self.lang_lookup: List[str] = []
        self.author_lookup: List[str] = [] 
        self.proof_lookup: List[str] = []
        self.reason_lookup: List[str] = []
        self.texture_lookup: List[str] = [
            "standard", "crystalline", "plates", "digital", "metallic", "necrosis", 
            "io", "check", "verification", "mutation", "event", "logic", "danger"
        ]

    def record_mission(
        self, 
        stars: List[Dict[str, Any]], 
        singularity: List[Dict[str, Any]],
        summary: Dict[str, Any],
        forensic_report: Dict[str, Any],
        repo_name: str,
        lang_registry: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Orchestrates the Columnar Pivot, destructively evicts RAM, and seals the manifest.
        """
        if lang_registry:
            self.lang_lookup.extend([l for l in lang_registry if l not in self.lang_lookup])
            
        visible_count = len(stars)
        dark_count = len(singularity)
        total_artifacts = visible_count + dark_count
        
        self.logger.info(f"Astrograph: Initiating columnar pivot for '{repo_name}' ({total_artifacts} artifacts)...")

        # ----------------------------------------------------------------------
        # FORENSIC REPORT FORMATTING & TIE RESOLUTION
        # Re-calculate top/bottom 3 using the full stars array to detect massive
        # ties (e.g., 10 files at 100%). Formats floats into string percentages.
        # ----------------------------------------------------------------------
        def format_tier(lst, reverse_sort):
            if not lst: return []
            
            # Group files by value (rounded to 2 decimals to prevent float drift)
            groups = {}
            for x in lst:
                val = round(self._safe_float(x["value"]), 2)
                if val not in groups:
                    groups[val] = []
                groups[val].append(x)
            
            results = []
            sorted_vals = sorted(groups.keys(), reverse=reverse_sort)
            
            for val in sorted_vals:
                group = groups[val]
                
                # If a tie exceeds our remaining display slots, group them into one entry
                slots_left = 3 - len(results)
                if len(group) > slots_left and len(group) > 1:
                    results.append({
                        "name": f"[{len(group)} artifacts tied]",
                        "path": "Multiple Sectors",
                        "value": f"{val}%"
                    })
                    break # Chart is effectively full
                else:
                    for item in group:
                        results.append({
                            "name": item["name"],
                            "path": item["path"],
                            "value": f"{val}%"
                        })
                        if len(results) >= 3:
                            break
                if len(results) >= 3:
                    break
            return results

        if forensic_report and "exposures" in forensic_report:
            for idx, risk_key in enumerate(self.RISK_SCHEMA):
                if risk_key not in forensic_report["exposures"]:
                    continue
                
                # 1. Extract all valid values for this specific risk from the entire galaxy
                extracted = []
                for s in stars:
                    rv = s.get("risk_vector")
                    if rv and len(rv) > idx:
                        extracted.append({
                            "name": s.get("name", "unknown"),
                            "path": s.get("path", "unknown"),
                            "value": rv[idx]
                        })
                
                if not extracted: 
                    continue

                # 2. Override the forensic report natively before saving
                forensic_report["exposures"][risk_key] = {
                    "highest": format_tier(extracted, reverse_sort=True),
                    "lowest": format_tier(extracted, reverse_sort=False)
                }

        # 1. Initialize GPU Parallel Arrays
        columns: Dict[str, List[Any]] = {
            "names": [], "paths": [], "lang_ids": [],
            "locs": [], "m_locs": [], "mass": [], "entropy": [],
            "pos_x": [], "pos_y": [], "pos_z": [],
            "risks": [], "hits": [], "satellites": [], "telemetry": []
        }
        
        singularity_columns: Dict[str, List[Any]] = {
            "paths": [], "reasons": [], "sizes": [], 
            "failed_claims": [], "lock_tiers": [], "confidences": [], "proofs": []
        }

        # 2. Destructive Vectorization (O(1) Memory Eviction Loop)
        processed_stars = 0
        self.logger.debug("Pivoting Visible Matter...")
        while stars:
            try:
                self._process_star(stars.pop(), columns)
                processed_stars += 1
            except Exception as e:
                self.logger.error(f"Astrograph Anomaly: Dropped corrupted star to preserve array alignment. {e}", exc_info=True)

        processed_dark = 0
        self.logger.debug("Pivoting Dark Matter (Singularity)...")
        while singularity:
            try:
                self._process_singularity(singularity.pop(), singularity_columns)
                processed_dark += 1
            except Exception as e:
                self.logger.error(f"Astrograph Anomaly: Dropped corrupted dark matter. {e}", exc_info=True)
        
        self.logger.debug(f"Vectorization complete. Processed {processed_stars} Stars, {processed_dark} Dark Matter.")

        self._enforce_schema_integrity(columns, "galaxy")
        self._enforce_schema_integrity(singularity_columns, "singularity")

        # 3. Final Manifest Synthesis (Maintains Orchestrator compatibility)
        return {
            "meta": {
                "session": {
                    "engine": f"GitGalaxy Scope v{self.version}",
                    "target": repo_name,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                },
                "schemas": {
                    "galaxy": self.GALAXY_SCHEMA,
                    "galaxy_columns": list(columns.keys()), 
                    "singularity_columns": list(singularity_columns.keys()),
                    "risk_vector_x1000": list(self.RISK_SCHEMA),
                    "hit_vector": list(self.HIT_SCHEMA),
                    "satellites": list(self.SAT_SCHEMA),
                    "scalars": {"exposure": 1000, "physics": 10},
                    "lookups": {
                        "languages": self.lang_lookup,
                        "textures": self.texture_lookup,
                        "authors": self.author_lookup,
                        "proofs": self.proof_lookup,
                        "reasons": self.reason_lookup
                    }
                }
            },
            "global_summary": summary,
            "galaxy": columns,
            "singularity": singularity_columns,
            "forensic_report": forensic_report

        }

    def _process_star(self, star: Dict[str, Any], columns: Dict[str, List[Any]]):
        path = self._sanitize_text(star.get("path", "unknown"))
        name = self._sanitize_text(star.get("name", Path(path).name))
        lang_idx = self._intern_string(str(star.get("lang_id", "unknown")), self.lang_lookup)
        
        loc = self._safe_int(star.get("total_loc", 0))
        m_loc = self._safe_int(star.get("coding_loc", 0))
        
        risk_vector_x1000 = self._quantize_risk_vector(star.get("risk_vector", []))
        mass_x10 = int(round(self._safe_float(star.get("file_impact", 0.0)) * 10))
        
        churn_val = star.get("risk_vector", [0]*len(self.RISK_SCHEMA))[self.RISK_SCHEMA.index("churn")] if "churn" in self.RISK_SCHEMA and len(star.get("risk_vector", [])) > self.RISK_SCHEMA.index("churn") else star.get("entropy", 0.0)
        entropy_x1000 = int(round(max(0.0, min(100.0, self._safe_float(churn_val))) * 10))
        
        pos_x = int(round(self._safe_float(star.get("pos_x", 0.0)) * 10))
        pos_y = int(round(self._safe_float(star.get("pos_y", 0.0)) * 10))
        pos_z = int(round(self._safe_float(star.get("pos_z", 0.0)) * 10))
        
        raw_hits = star.get("hit_vector", [])
        if not isinstance(raw_hits, list) or len(raw_hits) != len(self.HIT_SCHEMA):
            raw_hits = [0] * len(self.HIT_SCHEMA)
        hits = [self._safe_int(h) for h in raw_hits]
        
        sat_vectors = self._vectorize_satellites(star.get("satellites", []))
        
        raw_tel = star.get("telemetry", {})
        telemetry = {}
        
        owner = raw_tel.get("ownership")
        if owner:
            telemetry["author_id"] = self._intern_string(owner, self.author_lookup)
            
        proof = raw_tel.get("identity_source_proof", star.get("source_proof"))
        if proof:
            telemetry["proof_id"] = self._intern_string(proof, self.proof_lookup)
            telemetry["lock_tier"] = self._safe_int(raw_tel.get("identity_lock_tier", star.get("lock_tier", 4)))
            
        if "densities" in raw_tel: telemetry["densities"] = raw_tel["densities"]
        if "raw_churn_freq" in raw_tel: telemetry["raw_churn_freq"] = raw_tel["raw_churn_freq"]
        if "popularity" in raw_tel: telemetry["popularity"] = raw_tel["popularity"]
        if "purpose" in raw_tel: telemetry["purpose"] = raw_tel["purpose"]
        if "ownership_entropy" in raw_tel: telemetry["ownership_entropy"] = raw_tel["ownership_entropy"]

        columns["names"].append(name)
        columns["paths"].append(path)
        columns["lang_ids"].append(lang_idx)
        columns["locs"].append(loc)
        columns["m_locs"].append(m_loc)
        columns["risks"].append(risk_vector_x1000)
        columns["hits"].append(hits)
        columns["mass"].append(mass_x10)
        columns["entropy"].append(entropy_x1000)
        columns["satellites"].append(sat_vectors)
        columns["pos_x"].append(pos_x)
        columns["pos_y"].append(pos_y)
        columns["pos_z"].append(pos_z)
        columns["telemetry"].append(telemetry)

    def _process_singularity(self, dark_star: Dict[str, Any], columns: Dict[str, List[Any]]):
        path = self._sanitize_text(dark_star.get("path", "unknown"))
        size_bytes = self._safe_int(dark_star.get("size_bytes", 0))
        reason_idx = self._intern_string(dark_star.get("reason", "Unknown Anomaly"), self.reason_lookup)
        
        claim_idx = self._intern_string(str(dark_star.get("failed_claim", "unknown")), self.lang_lookup)
        tier = self._safe_int(dark_star.get("identity_lock_tier", 4))
        conf_x1000 = int(round(self._safe_float(dark_star.get("identity_confidence", 0.0)) * 1000))
        proof_idx = self._intern_string(str(dark_star.get("identity_source_proof", "Discovery")), self.proof_lookup)
        
        columns["paths"].append(path)
        columns["reasons"].append(reason_idx)
        columns["sizes"].append(size_bytes)
        columns["failed_claims"].append(claim_idx)
        columns["lock_tiers"].append(tier)
        columns["confidences"].append(conf_x1000)
        columns["proofs"].append(proof_idx)

    def _quantize_risk_vector(self, risks: Any) -> List[int]:
        quantized = []
        if isinstance(risks, list):
            for val in risks:
                scaled = int(round(max(0.0, min(100.0, self._safe_float(val))) * 10)) 
                quantized.append(scaled)
        elif isinstance(risks, dict):
            for key in self.RISK_SCHEMA:
                val = self._safe_float(risks.get(key, 0.0))
                scaled = int(round(max(0.0, min(100.0, val)) * 10)) 
                quantized.append(scaled)
        
        while len(quantized) < len(self.RISK_SCHEMA):
            quantized.append(0)
            
        return quantized[:len(self.RISK_SCHEMA)]

    def _vectorize_satellites(self, satellites: Any) -> List[List[Any]]:
        vectorized = []
        if not isinstance(satellites, list):
            return vectorized
            
        for sat in satellites:
            if not isinstance(sat, dict): continue
            vectorized.append([
                self._sanitize_text(sat.get("name", "anon")),                         
                self._safe_int(sat.get("loc", 0)),                                     
                self._safe_int(sat.get("branch_count", sat.get("branch", 0))),         
                int(round(self._safe_float(sat.get("angle", 0.0)) * 10)),              
                self._safe_int(sat.get("args", 0)),                                    
                self._intern_string(sat.get("type_id", "standard"), self.texture_lookup), 
                int(round(self._safe_float(sat.get("ratio", 0.0)) * 1000)),           
                int(round(self._safe_float(sat.get("mag", 0.0)) * 10))                
            ])
        return vectorized

    def _safe_float(self, val: Any) -> float:
        if val is None: return 0.0
        try:
            f_val = float(val)
            if math.isnan(f_val) or math.isinf(f_val): return 0.0
            return f_val
        except (ValueError, TypeError):
            return 0.0
            
    def _safe_int(self, val: Any) -> int:
        if val is None: return 0
        try:
            return int(float(val))
        except (ValueError, TypeError):
            return 0

    def _intern_string(self, value: Any, registry: List[str]) -> int:
        val_str = self._sanitize_text(str(value))
        if val_str not in registry:
            registry.append(val_str)
        return registry.index(val_str)

    def _sanitize_text(self, text: Any) -> str:
        if text is None: return ""
        if not isinstance(text, str):
            text = text
        return "".join(char for char in text if char.isprintable())

    def _enforce_schema_integrity(self, columns: Dict[str, List[Any]], target_name: str):
        lengths = {k: len(v) for k, v in columns.items()}
        unique_lengths = set(lengths.values())
        
        if len(unique_lengths) > 1:
            self.logger.error(f"Schema Corruption ({target_name}): Array alignment lost! Lengths: {lengths}")
            raise SchemaCorruptionError(f"CRITICAL: Column alignment mismatch in {target_name}: {lengths}")
                
        self.logger.debug(f"{target_name.capitalize()} integrity verified. Matrix perfectly aligned at length {list(unique_lengths)[0] if unique_lengths else 0}.")

    def save_minified(self, payload: Dict[str, Any], filename: str):
        temp_file = f"{filename}.tmp"
        try:
            self.logger.debug(f"Astrograph: Serializing payload to temporary buffer '{temp_file}'...")
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(
                    payload, f, 
                    indent=None, 
                    ensure_ascii=False, 
                    separators=(',', ':')
                )
            
            if not os.path.exists(temp_file) or os.path.getsize(temp_file) == 0:
                raise IOError("Temporary manifest file is empty or missing post-serialization.")
            
            os.replace(temp_file, filename)
            
            kb_size = os.path.getsize(filename) / 1024.0
            mb_size = kb_size / 1024.0
            
            size_str = f"{mb_size:.2f} MB" if mb_size > 1.0 else f"{kb_size:.1f} KB"
            self.logger.info(f"Astrograph: Manifest sealed successfully -> {filename} ({size_str})")
            
        except Exception as e:
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except OSError:
                    pass
            self.logger.error(f"Atomic Save Failure: Could not serialize manifest: {e}", exc_info=True)
            raise