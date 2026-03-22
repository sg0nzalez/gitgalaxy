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
import argparse
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any
from . import gitgalaxy_standards_v011 as config

# ==============================================================================
# GitGalaxy Phase 8 & 9: Astrograph Auditor (The Forensic Record)
# Strategy v6.2.0 Protocol: Raw-Matter Preservation & Columnar Decoding
# Stage 2.5: Total Feature Parity (Descriptive Descriptors + Performance)
# ==============================================================================

class AuditRecorder:
    """
    The GitGalaxy Audit Recorder.
    
    PURPOSE: Generates a verbose, human-readable forensic log from live RAM data.
    Designed for compliance, debugging, and deep-dive analysis.
    """

    def __init__(self, parent_logger=None):
        import logging
        self.logger = parent_logger.getChild("audit_recorder") if parent_logger else logging.getLogger("audit_recorder")

        # --- DYNAMIC SCHEMA FETCH ---
        schemas = getattr(config, "RECORDING_SCHEMAS", {})
        self.RISK_SCHEMA = schemas.get("RISK_SCHEMA", [])
        # Note: The pipeline calls it SIGNAL_SCHEMA, but the Auditor references it as HIT_SCHEMA
        self.HIT_SCHEMA = schemas.get("SIGNAL_SCHEMA", []) 

        # Performance optimization: Pre-cache all labels to avoid regex on the hot path
        self._label_cache = {}
        self._friendly_map = schemas.get("FRIENDLY_MAP", {})

    def format_label(self, key: str) -> str:
        """Translates raw keys into descriptive labels using a fast-lookup cache."""
        if key in self._label_cache:
            return self._label_cache[key]
            
        clean_key = re.sub(r'_x\d+$', '', key)
        label = self._friendly_map.get(clean_key)
        
        if not label:
            label = " ".join(word.capitalize() for word in clean_key.split('_'))
            
        self._label_cache[key] = label
        return label

    def descale(self, key: str, value: Any, default_scalar: float = 1.0) -> Any:
        """Dynamically scales integers back to floats using a fixed-string check."""
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            return value
            
        if key.endswith("_x1000"):
            return round(value / 1000.0, 3)
        if key.endswith("_x10"):
            return round(value / 10.0, 3)
            
        if default_scalar != 1.0:
            return round(value / default_scalar, 3)
        return value

    def generate_report(self, stars, singularity, summary, forensic_report, session_meta, output_path):
        """
        Subphase 2.3: Transforms raw pipeline data into a verbose forensic manifest.
        Optimized to handle projects with 10,000+ files efficiently.
        """
        # 1. Forensic Traceability Anchor
        git_audit = session_meta.get("git_audit", {})
        forensic_trail = {
            "Analysis Context": {
                "Engine Identity": session_meta.get("engine", "GitGalaxy Scope v6.2.0"),
                "Target Root Name": session_meta.get("target", "Unknown"),
                "Absolute Project Path": session_meta.get("target_directory", "Unknown"),
                "Analysis ISO Timestamp": session_meta.get("timestamp"),
                "Total Scan Duration": f"{session_meta.get('duration_seconds', 0.0)} seconds"
            },
            "Source Control Footprint (Immutable Anchor)": {
                "Active Branch": git_audit.get("branch", "N/A"),
                "Commit Hash (SHA-1)": git_audit.get("commit_hash", "N/A"),
                "Remote Origin URL": git_audit.get("remote_url", "Local/Disconnected"),
                "Last Code Integration Date": git_audit.get("latest_commit_date", "Unknown")
            }
        }

        # --- DYNAMIC TRANSLATION FETCH ---
        schemas = getattr(config, "RECORDING_SCHEMAS", {})
        exposure_labels = schemas.get("EXPOSURE_LABELS", {})

        # Pre-calculate labels for vectors to avoid repeating work in the loop
        risk_labels = [exposure_labels.get(k, self.format_label(k)) for k in self.RISK_SCHEMA]
        hit_labels = [self.format_label(k) for k in self.HIT_SCHEMA]

        # --- NEW CONSTELLATION SORTING & HIERARCHY ---
        pretty_constellations = {}
        constellations_meta = summary.get("constellations", {})
        
        # Sort folders by mass descending
        sorted_constellations = sorted(
            constellations_meta.items(), 
            key=lambda x: x[1].get("total_mass", 0.0), 
            reverse=True
        )

        # Initialize the ordered dictionary with constellation-level metrics
        for c_name, c_data in sorted_constellations:
            pretty_constellations[c_name] = {
                "Constellation Mass": c_data.get("total_mass", 0.0),
                "File Count": c_data.get("file_count", 0),
                "Average Risk Exposures": {
                    exposure_labels.get(k, self.format_label(k)): f"{v}%" 
                    for k, v in c_data.get("avg_exposures", {}).items()
                },
                "Stars / Files": {}
            }

        # 2. Row Reconstruction (Visible Stars) mapped into Constellations
        for star in stars:
            path = star.get("path", "Unknown")
            telemetry = star.get("telemetry", {})
            lang_raw = str(star.get("lang_id", "Unknown")).lower()
            c_name = star.get("constellation", "__monolith__")
            
            # --- THE ULTIMATE UPSTREAM BYPASS FIX ---
            doc_languages = {"markdown", "plaintext", "rst", "text", "md"}
            if lang_raw in doc_languages and len(star.get("risk_vector", [])) < len(self.RISK_SCHEMA):
                # Inject 13-point synthetic Risk Blanket
                star["risk_vector"] = [0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 100.0, 0.0, 100.0, 0.0]
                telemetry["control_flow_ratio"] = 0.0
                if not star.get("file_impact"):
                    star["file_impact"] = round(max(star.get("total_loc", 1) / 50.0, 1.0), 2)
            
            # --- SYSTEM LEVEL FIX: Dynamic Identity Block ---
            identity_block = {
                "Filename": star.get("name", Path(path).name),
                "Path": path,
                "Language": str(star.get("lang_id", "Unknown")).title(),
                "Architect": telemetry.get("ownership", "Unknown Architect")
            }
            
            domain_data = telemetry.get("domain_context", {})
            for custom_key, custom_val in domain_data.items():
                if custom_key != "ownership":
                    display_key = custom_key.replace('_', ' ').title()
                    if display_key == "Purpose":
                        display_key = "Museum Entry"
                    identity_block[display_key] = custom_val

            identity_block["Lock Tier"] = star.get("lock_tier", telemetry.get("identity_lock_tier", 4))
            identity_block["Identity Proof"] = telemetry.get("identity_source_proof", star.get("source_proof", "Discovery"))
            
            # --- THE FACTION INTERCEPTOR ---
            exposures_dict = {}
            for label, v in zip(risk_labels, star.get("risk_vector") or [0.0] * len(risk_labels)):
                if label == "Civil War Exposure":
                    if v == 0.0: 
                        exposures_dict[label] = "Team Tabs"
                    elif v == 100.0: 
                        exposures_dict[label] = "Team Spaces"
                    elif v == 50.0: 
                        exposures_dict[label] = "Neutral / Deadlocked"
                    else: 
                        exposures_dict[label] = f"Mixed ({100-v:.1f}% Tabs / {v:.1f}% Spaces)"
                else:
                    exposures_dict[label] = f"{round(v, 2)}%"

            # Assemble the star profile
            star_profile = {
                "1. Identity": identity_block,
                "2. Spatial Coordinates": {
                    "X": star.get("pos_x", 0.0), 
                    "Y": star.get("pos_y", 0.0), 
                    "Z": star.get("pos_z", 0.0)
                },
                "3. Galactic Profile": {
                    "Total LOC": star.get("total_loc", 0),
                    "coding LOC": star.get("coding_loc", 0),
                    "Documentation LOC": star.get("doc_loc", 0),
                    "Structural Mass": round(star.get("file_impact", 0.0), 3),
                    "Control Flow Ratio": f"{round(telemetry.get('control_flow_ratio', 0.0) * 100, 1)}%",
                    "Popularity Rank": telemetry.get("popularity", 0)
                },
                "4. Risk Exposures": exposures_dict,
                "5. Function Analysis (Satellites)": [
                    {
                        "Function Name": sat.get("name", "Unknown"),
                        "Structural Impact": sat.get("impact", sat.get("magnitude", 0.0)),
                        "Lines of Code (LOC)": sat.get("loc", 0),
                        "Control Flow Branches": sat.get("branch", sat.get("branch_count", 0)),
                        "Input Parameters": sat.get("args", sat.get("args_count", 0)),
                        "Control Flow Ratio": f"{round(sat.get('control_flow_ratio', sat.get('cf_ratio', 0.0)) * 100, 1)}%",
                        "Start Line": sat.get("start_line", 0),
                        "End Line": sat.get("end_line", 0)
                    }
                    for sat in star.get("satellites", []) if isinstance(sat, dict)
                ],
                "6. Structural DNA (Raw Hits)": {
                    label: v for label, v in zip(hit_labels, star.get("hit_vector") or [0] * len(hit_labels))
                },
                "7. Extracted Dependencies": sorted(list(star.get("raw_imports", [])))
            }
            
            # Map the star into its parent constellation
            if c_name not in pretty_constellations:
                pretty_constellations[c_name] = {"Constellation Mass": 0.0, "Stars / Files": {}}
            pretty_constellations[c_name]["Stars / Files"][path] = star_profile

        # 3. Format Dark Matter (Excluded Artifacts)
        pretty_singularity = []
        target_dir = Path(session_meta.get("target_directory", ""))

        # 3.1 Format standard excluded items for the JSON output
        for dark in singularity:
            rel_path = dark.get("path", "Unknown")
            abs_path = target_dir / rel_path
            
            # Physically weighs the file on disk if the pipeline dropped the byte count
            try:
                actual_size = os.path.getsize(abs_path) if abs_path.exists() else dark.get('size_bytes', 0)
            except Exception:
                actual_size = dark.get('size_bytes', 0)

            pretty_singularity.append({
                "Path": rel_path,
                "Forensic Category": "Dark Matter (Excluded Artifact)",
                "Diagnostic Reason": dark.get("reason", "Engine Shielding (Format Excluded)"),
                "Size": f"{actual_size} bytes",
                "Identity Confidence": f"{round(dark.get('identity_confidence', 0.0) * 100, 1)}%",
                "Discovery Proof": dark.get("identity_source_proof", "Radar Scan")
            })

        # 3.2 Append optically bypassed artifacts to the local output list
        for anon_path in summary.get("singularity", {}).get("unparsable_artifacts", []):
            pretty_singularity.append({
                "Path": anon_path,
                "Forensic Category": "Dark Matter (Optical Bypass)",
                "Diagnostic Reason": "Engine Bypass (Dense Structure or Unrecognized Syntax)",
                "Size": "Unknown (Prism Bypass)",
                "Identity Confidence": "0.0% (Scan Yielded No Data)",
                "Discovery Proof": "Logic Splicer Shielding"
            })

        # 4. Final Mission Archive Packaging
        mission_audit = {
            "Audit Protocol": "GitGalaxy v6.2.0-Audit",
            "1. Forensic Trail (Traceability)": forensic_trail,
            "2. Global Synthesis Summary": summary,
            "3. High-Value Forensic Report": forensic_report,
            "4. Dark Matter (Excluded Artifacts)": pretty_singularity,
            "5. Visible Matter (Scanned Artifacts)": pretty_constellations
        }

        # --- ABSOLUTE ROUTING LOGIC ---
        base_dir = Path("/srv/storage_16tb/projects/gitgalaxy/data")
        base_dir.mkdir(parents=True, exist_ok=True)
        safe_filename = Path(output_path).name
        target_path = base_dir / safe_filename

        try:
            with open(target_path, 'w', encoding='utf-8') as f:
                json.dump(mission_audit, f, indent=4, ensure_ascii=False)
            self.logger.info(f"Audit Success: Forensic manifest sealed -> {target_path}")
        except Exception as e:
            self.logger.error(f"Audit Write Error: {e}")

def decode_galaxy(input_path, output_path=None):
    """Standalone decoding logic preserved for CLI compatibility."""
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GitGalaxy v6.2.0 Astrograph Auditor CLI")
    parser.add_argument("input", help="Path to columnar galaxy.json")
    parser.add_argument("--out", help="Optional output path")
    args = parser.parse_args()