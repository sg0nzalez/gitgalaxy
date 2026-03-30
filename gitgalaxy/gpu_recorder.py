# ==============================================================================
# GitGalaxy
# Copyright (c) 2026 Joe Esquibel
#
# This source code is licensed under the PolyForm Noncommercial License 1.0.0.
# You may not use this file except in compliance with the License.
# A copy of the license can be found in the LICENSE file in the root directory
# of this project, or at https://polyformproject.org/licenses/noncommercial/1.0.0/
# ==============================================================================
import json
import logging
import gc
from pathlib import Path
from typing import List, Dict, Any, Optional
from . import gitgalaxy_standards_v1 as config

# ==============================================================================
# GitGalaxy Phase 9: GPU Recorder (Formerly RecordKeeper)
# Strategy v6.2.0 Protocol: Destructive Columnar Pivot & Text Interning
# Stage 3.3: Destructive RAM Eviction (Final Roadmap Phase)
# ==============================================================================

class GPURecorder:
    """
    The GitGalaxy GPU Recorder.
    
    PURPOSE: Transforms row-based data into numerical columns for GPU processing.
    Minifies text via String Interning (Lookups) and removes forensic overhead.
    Stage 3.3: Aggressively clears RAM via destructive .pop() and garbage collection.
    """

    def __init__(self, version: str, parent_logger: Optional[logging.Logger] = None):
        self.version = version
        self.logger = parent_logger.getChild("gpu_recorder") if parent_logger else logging.getLogger("gpu_recorder")

        # --- DYNAMIC SCHEMA FETCH ---
        schemas = getattr(config, "RECORDING_SCHEMAS", {})

        # --- INTERNING REGISTRIES ---
        self.lang_lookup: List[str] = []
        self.author_lookup: List[str] = []
        self.proof_lookup: List[str] = []
        self.purpose_lookup: List[str] = [] 
        self.reason_lookup: List[str] = []
        self.ext_lookup: List[str] = [] # <--- NEW: Vectorized Extension Registry
        self.import_lookup: List[str] = [] # <--- NEW: Vectorized Import Registry
        self.texture_lookup: List[str] = schemas.get("GPU_TEXTURE_LOOKUPS", [])
        self.const_lookup: List[str] = [] # <--- NEW: Vectorized Constellation Registry
        self.archetype_lookup: List[str] = [] # <--- NEW: Vectorized ML Archetypes

        # --- POSITION-SENSITIVE SCHEMAS ---
        self.RISK_SCHEMA = schemas.get("RISK_SCHEMA", [])
        self.HIT_SCHEMA = schemas.get("SIGNAL_SCHEMA", [])
        self.SAT_SCHEMA = schemas.get("SAT_SCHEMA", [])

    def record_mission(self, stars: List[Dict], singularity: List[Dict], summary: Dict, forensic_report: Dict, repo_name: str) -> Dict:
        """
        Orchestrates the synthesis and implementation of Stage 3.3: Destructive RAM Eviction.
        Iteratively destroys the input lists to free memory while building the columnar manifest.
        """
        self.logger.info("GPU_RECORDER: Engaging Stage 3.3 Destructive RAM Eviction.")

        columns = {
            "names": [], "paths": [], "lang_ids": [], "locs": [], "m_locs": [], "d_locs": [],
            "mass": [], "author_distribution": [], 
            "ownership_entropy": [], "raw_churn_freq": [], "cog_raw": [], # <--- ADDED THE 3 DNA COLUMNS
            "pos_x": [], "pos_y": [], "pos_z": [],
            "risks": [], "hits": [], "telemetry": [], "satellites": [],
            "imports": [], # <--- NEW: The dependency string lookup column
            "c_ids": [],   # <--- NEW: The Constellation Mapping Column
            "a_ids": [],   # <--- NEW: Machine Learning Archetype IDs
            "edges": [],    # <--- NEW: Integer pointers for 3D WebGL lines
            "outbound_edges": []
        }

        sing_cols = {
            "paths": [], "exts": [], "reasons": [], "sizes": [], "confidences": []
        }

        # --- NEW: Build the Dependency Resolution Map BEFORE destruction ---
        # Because .pop() takes from the end of the list, stars[-1] becomes column index 0.
        resolution_map = {}
        for idx, s in enumerate(reversed(stars)):
            path = s.get("path", "")
            name = s.get("name", Path(path).name)
            stem = Path(path).stem # e.g., "module_sf_clm" without the .F
            
            # Map multiple variations so string imports match easily
            if path: resolution_map[path] = idx
            if name: resolution_map[name] = idx
            if stem: resolution_map[stem] = idx

        # ---> THE NEW ADDITION <---
        # Pre-allocate the "Imported By" array for all stars
        inbound_edges = [[] for _ in range(len(stars))]

        # --- DESTRUCTIVE PIVOT: Visible Stars ---
        # Subphase 3.3: Use while loop with pop() to ensure the list is physically emptied
        while stars:
            current_idx = len(columns["paths"]) # Tracks the exact column index being built
            s = stars.pop()
            path = s.get("path", "")
            tel = s.get("telemetry", {})  # Pre-extract telemetry dict
            
            # --- NEW: Map the file to its Constellation via Interning ---
            c_name = s.get("constellation", "__monolith__")
            columns["c_ids"].append(self._intern(c_name, self.const_lookup))
            
            # --- NEW: Map the file to its ML Archetype via Interning ---
            arch_name = tel.get("archetype", "Unknown Archetype")
            columns["a_ids"].append(self._intern(arch_name, self.archetype_lookup))
            
            columns["paths"].append(path)
            columns["names"].append(s.get("name", Path(path).name))
            columns["lang_ids"].append(self._intern(str(s.get("lang_id", "unknown")), self.lang_lookup))
            columns["locs"].append(int(s.get("total_loc", 0)))
            columns["m_locs"].append(int(s.get("coding_loc", 0)))
            columns["d_locs"].append(int(s.get("doc_loc", 0))) # <-- NEW: Comment LOC

            # Quantization & DNA Fingerprinting (The 3 new columns)
            columns["mass"].append(int(round(s.get("file_impact", 0.0) * 10)))
            columns["author_distribution"].append(int(round(tel.get("author_distribution", 0.0) * 1000)))
            columns["ownership_entropy"].append(int(round(tel.get("ownership_entropy", 0.0) * 1000)))
            columns["raw_churn_freq"].append(int(round(tel.get("raw_churn_freq", 0.0) * 1000)))
            columns["cog_raw"].append(int(round(tel.get("densities", {}).get("cog_raw", 0.0) * 1000)))

            columns["pos_x"].append(int(round(s.get("pos_x", 0.0) * 10)))
            columns["pos_y"].append(int(round(s.get("pos_y", 0.0) * 10)))
            columns["pos_z"].append(int(round(s.get("pos_z", 0.0) * 10)))

            # Vector Quantization
            columns["risks"].append([int(v * 10) for v in s.get("risk_vector", [0]*len(self.RISK_SCHEMA))])
            columns["hits"].append([int(v) for v in s.get("hit_vector", [0]*len(self.HIT_SCHEMA))])

            # Telemetry Interning
            domain_ctx = tel.get("domain_context", {}) # <-- FIXED BUG: purpose was nested here
            columns["telemetry"].append(
                {
                    "aid": self._intern(
                        tel.get("ownership", "unknown"), self.author_lookup
                    ),
                    "pid": self._intern(
                        tel.get("identity_source_proof", "Discovery"), self.proof_lookup
                    ),
                    "purp": self._intern(
                        domain_ctx.get("purpose", "Standard Logic Matrix"), self.purpose_lookup # <-- FIXED BUG
                    ),
                    "lt": tel.get("identity_lock_tier", 4),
                    "pop": tel.get("popularity", 0),
                    "cfr": int(
                        round(tel.get("control_flow_ratio", 0.0) * 1000) # <-- FIXED BUG: was grabbing from root
                    ),
                }
            )

            # Satellite Minification (Internal Destructive Loop)
            sat_list = []
            s_sats = s.get("satellites", [])
            while s_sats:
                sat = s_sats.pop()
                sat_list.append([
                    sat.get("name", "unk"), 
                    sat.get("loc", 0), 
                    sat.get("branch", 0), 
                    int(sat.get("angle", 0) * 10),
                    sat.get("args", 0),
                    self._intern(sat.get("texture", "standard"), self.texture_lookup),
                    int(sat.get("control_flow_ratio", 0.0) * 1000),
                    int(sat.get("impact", sat.get("magnitude", 0)) * 10), # <-- FIXED BUG: Added impact
                    int(sat.get("start_line", 0)),
                    int(sat.get("end_line", 0))
                ])

            # ---> FLIP THE ARRAY BACK TO HIGHEST-FIRST <---
            sat_list.reverse()

            columns["satellites"].append(sat_list)

            # --- DEPENDENCY INTERNING & EDGE RESOLUTION ---
            # Cast to a sorted list for determinism, then convert strings to integer IDs
            raw_imports = sorted(list(s.get("raw_imports", [])))
            columns["imports"].append([self._intern(imp, self.import_lookup) for imp in raw_imports])

            # ---> THE REVERSED LOGIC & NEW OUTBOUND LOGIC <---
            current_outbound = []
            
            for imp in raw_imports:
                if imp in resolution_map:
                    target_idx = resolution_map[imp]
                    if target_idx != current_idx: 
                        # 1. INBOUND (Gold): Inject current file's ID into the TARGET file's list
                        inbound_edges[target_idx].append(current_idx)
                        
                        # 2. OUTBOUND (Magenta): Inject the TARGET's ID into the current file's list
                        current_outbound.append(target_idx)

            # Store the unique outbound edges for the current file into the new column
            columns["outbound_edges"].append(list(set(current_outbound)))

            # Subphase 3.3: Explicitly delete the individual star dict reference
            # as it is no longer tied to the 'stars' list
            del s

        # Clean up duplicates and assign to the final columnar output
        columns["edges"] = [list(set(edges)) for edges in inbound_edges]

        # --- DESTRUCTIVE PIVOT: Singularity ---
        while singularity:
            d = singularity.pop()
            path = d.get("path", "")

            # Safely extract and format the extension for interning
            ext = Path(path).suffix.lower() if Path(path).suffix else "none"

            sing_cols["paths"].append(path)
            sing_cols["exts"].append(self._intern(ext, self.ext_lookup)) # Vectorized Extension
            sing_cols["reasons"].append(self._intern(d.get("reason", "anomaly"), self.reason_lookup))
            sing_cols["sizes"].append(int(d.get("size_bytes", 0)))
            sing_cols["confidences"].append(int(round(d.get("identity_confidence", 0.0) * 1000)))
            del d

        # Final memory cleanup trigger
        gc.collect()
        self.logger.debug("GPU_RECORDER: RAM Eviction complete. Python GC cycle triggered.")
        
        # --- FLATTEN SINGULARITY SUMMARY FOR UI ---
        # Transforms the heavily nested composition dict into a flat "breakdown" object
        sig_sum = summary.get("singularity", {})
        breakdown = {
            "binary": sig_sum.get("binary", 0),
            "unparsable": sig_sum.get("unparsable", 0),
            "no_extension": sig_sum.get("no_extension", 0),
            "size_limit": sig_sum.get("size_limit", 0),
            "os_permissions": sig_sum.get("os_permissions", 0)
        }

        # Unpack the nested extensions into UI-friendly keys WITH reason details
        comp = sig_sum.get("composition_by_extension_and_reason", {})
        for ext, reasons in comp.items():
            total = sum(reasons.values())
            if total > 0:
                safe_ext = ext if ext and ext != "no_extension" else "unknown"

                # THIS IS THE CRITICAL NESTED DICT THE UI NEEDS:
                breakdown[f"Format [{safe_ext}]"] = {
                    "count": total,
                    "details": reasons
                }

        summary["singularity"]["breakdown"] = breakdown

        # --- DYNAMIC LORE INJECTION ---
        # Fetch the story registry, defaulting to an empty dict if it doesn't exist
        project_stories = getattr(config, "PROJECT_STORIES", {})
        
        # Grab the specific story, OR generate the blank template
        # Explicitly defining the empty artifacts schema so the external merge script can target the keys
        story_payload = project_stories.get(repo_name, {
            "status": "",
            "why": "",
            "who": "",
            "significance": "",
            "link": "",
            "artifacts": [
                {
                    "title": "",
                    "url": "",
                    "description": ""
                }
            ]
        })
        
        return {
            "meta": {
                "schemas": {
                    "galaxy_columns": list(columns.keys()), 
                    "singularity_columns": list(sing_cols.keys()),
                    "risk_vector_x1000": self.RISK_SCHEMA,
                    "hit_vector": self.HIT_SCHEMA,
                    "satellites": self.SAT_SCHEMA,
                    "scalars": {"exposure": 1000, "physics": 10},
                    "lookups": {
                        "languages": self.lang_lookup,
                        "textures": self.texture_lookup,
                        "authors": self.author_lookup,
                        "proofs": self.proof_lookup,
                        "purposes": self.purpose_lookup,
                        "reasons": self.reason_lookup,
                        "exts": self.ext_lookup, 
                        "imports": self.import_lookup,
                        "constellations": self.const_lookup,
                        "archetypes": self.archetype_lookup
                    }
                }
            },
            "global_summary": summary, 
            "galaxy": columns,
            "singularity": sing_cols,
            "story": story_payload  # <--- INJECTED HERE
        }

    def _intern(self, val: str, registry: List[str]) -> int:
        if val not in registry: 
            registry.append(val)
        return registry.index(val)

    def save_minified(self, payload: Dict[str, Any], filename: str):
        """Serializes with maximum JSON compression to the provided output path."""
        from pathlib import Path
        
        # Convert the path handed to us by the orchestrator into a Path object
        target_path = Path(filename)

        # Ensure the parent directory exists just to be safe
        target_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            # Save using the safe target_path
            with open(target_path, 'w', encoding='utf-8') as f:
                json.dump(payload, f, indent=None, separators=(',', ':'), ensure_ascii=False)
            self.logger.info(f"GPU Manifest Sealed -> {target_path}")
        except Exception as e:
            self.logger.error(f"Failed to seal GPU manifest: {e}")