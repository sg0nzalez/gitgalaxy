import json
import logging
import os
import gc
from pathlib import Path
from typing import List, Dict, Any, Optional
import gitgalaxy_standards_v011 as config

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

        # --- POSITION-SENSITIVE SCHEMAS ---
        self.RISK_SCHEMA = schemas.get("RISK_SCHEMA", [])
        self.HIT_SCHEMA = schemas.get("SIGNAL_SCHEMA", [])
        self.SAT_SCHEMA = schemas.get("SAT_SCHEMA", ["name", "loc", "branch", "angle_x10", "args", "type_id", "control_flow_x1000", "mag_x10", "start_line", "end_line"])

        self.SAT_SCHEMA = [
            "name", "loc", "branch", "angle_x10", "args", "type_id", "control_flow_x1000", "mag_x10", "start_line", "end_line"
        ]

    def _minify_satellites(self, satellites: list) -> list:
        """
        Compresses the verbose satellite dictionaries into the strict 10-point SAT_SCHEMA array.
        Multiplies floats by 10 or 1000 to convert them to integers for smaller JSON payloads.
        """
        minified = []
        for sat in satellites:
            # Resolve the string to an integer ID using your existing lookup dictionaries
            name_id = self._intern(sat.get("name", "Unknown"), self.purpose_lookup)
            type_id = self._intern(sat.get("type_id", "standard"), self.texture_lookup)

            # SAT_SCHEMA: [name_id, loc, branch, angle_x10, args, type_id, ratio_x1000, mag_x10, start_line, end_line]
            mini_sat = [
                name_id,
                int(sat.get("loc", 1)),
                int(sat.get("branch", 0)),
                int(sat.get("angle", 0.0) * 10),
                int(sat.get("args", 0)),
                type_id,
                int(sat.get("control_flow_ratio", 0.0) * 1000),
                int(sat.get("impact", 0.0) * 10),
                int(sat.get("start_line", 0)),   # <-- NEW: Extracted Start Line
                int(sat.get("end_line", 0))      # <-- NEW: Extracted End Line
            ]
            minified.append(mini_sat)

        # Sort them by impact (index 7, highest to lowest) so the UI displays the biggest functions first
        minified.sort(key=lambda x: x[7], reverse=True)
        return minified

    def record_mission(self, stars: List[Dict], singularity: List[Dict], summary: Dict, forensic_report: Dict, repo_name: str) -> Dict:
        """
        Orchestrates the synthesis and implementation of Stage 3.3: Destructive RAM Eviction.
        Iteratively destroys the input lists to free memory while building the columnar manifest.
        """
        self.logger.info("GPU_RECORDER: Engaging Stage 3.3 Destructive RAM Eviction.")

        columns = {
            "names": [], "paths": [], "lang_ids": [], "locs": [], "m_locs": [], "d_locs": [],
            "mass": [], "author_distribution": [], "pos_x": [], "pos_y": [], "pos_z": [],
            "risks": [], "hits": [], "telemetry": [], "satellites": [],
            "imports": [], # <--- NEW: The dependency string lookup column
            "c_ids": [],   # <--- NEW: The Constellation Mapping Column
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
            
            # --- NEW: Map the file to its Constellation via Interning ---
            c_name = s.get("constellation", "__monolith__")
            columns["c_ids"].append(self._intern(c_name, self.const_lookup))
            
            columns["paths"].append(path)
            columns["names"].append(s.get("name", Path(path).name))
            columns["lang_ids"].append(self._intern(str(s.get("lang_id", "unknown")), self.lang_lookup))
            columns["locs"].append(int(s.get("total_loc", 0)))
            columns["m_locs"].append(int(s.get("coding_loc", 0)))
            columns["d_locs"].append(int(s.get("doc_loc", 0))) # <-- NEW: Comment LOC

            # Quantization
            columns["mass"].append(int(round(s.get("file_impact", 0.0) * 10)))
            columns["author_distribution"].append(int(round(s.get("telemetry", {}).get("author_distribution", 0.0) * 1000)))
            columns["pos_x"].append(int(round(s.get("pos_x", 0.0) * 10)))
            columns["pos_y"].append(int(round(s.get("pos_y", 0.0) * 10)))
            columns["pos_z"].append(int(round(s.get("pos_z", 0.0) * 10)))

            # Vector Quantization
            columns["risks"].append([int(v * 10) for v in s.get("risk_vector", [0]*len(self.RISK_SCHEMA))])
            columns["hits"].append([int(v) for v in s.get("hit_vector", [0]*len(self.HIT_SCHEMA))])

            # Telemetry Interning
            tel = s.get("telemetry", {})
            columns["telemetry"].append(
                {
                    "aid": self._intern(
                        tel.get("ownership", "unknown"), self.author_lookup
                    ),
                    "pid": self._intern(
                        tel.get("identity_source_proof", "Discovery"), self.proof_lookup
                    ),
                    "purp": self._intern(
                        tel.get("purpose", "Standard Logic Matrix"), self.purpose_lookup
                    ),
                    "lt": tel.get("identity_lock_tier", 4),
                    "pop": tel.get("popularity", 0),
                    "cfr": int(
                        round(s.get("total_control_flow_ratio", 0.0) * 1000)
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
                    int(sat.get("magnitude", 0) * 10),
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
                        "constellations": self.const_lookup # <--- NEW: Expose the mapped names to the UI
                    }
                }
            },
            "global_summary": summary, # <--- UI gets the average risk exposures from summary["constellations"] here!
            "galaxy": columns,
            "singularity": sing_cols
        }

    def _intern(self, val: str, registry: List[str]) -> int:
        if val not in registry: 
            registry.append(val)
        return registry.index(val)

    def save_minified(self, payload: Dict[str, Any], filename: str):
        """Serializes with maximum JSON compression to a dedicated storage drive."""

        # 1. Define the target directory
        base_dir = Path("/srv/storage_16tb/projects/gitgalaxy/data")

        # 2. Ensure the directory exists (creates parent folders if needed)
        base_dir.mkdir(parents=True, exist_ok=True)

        # 3. Strip any existing paths from the filename and append it to the base directory
        # This prevents errors if someone passes a filename like "data/output.json"
        safe_filename = Path(filename).name
        target_path = base_dir / safe_filename

        try:
            # 4. Save using the new absolute target_path
            with open(target_path, 'w', encoding='utf-8') as f:
                json.dump(payload, f, indent=None, separators=(',', ':'), ensure_ascii=False)
            self.logger.info(f"GPU Manifest Sealed -> {target_path}")
        except Exception as e:
            self.logger.error(f"Failed to seal GPU manifest: {e}")