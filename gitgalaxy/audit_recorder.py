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
from . import analysis_lens as config

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

        # Track archetypes per folder for the Constellation Fingerprint
        folder_archetype_counts = {}
        
        # Track archetypes per folder for the Constellation Fingerprint
        folder_archetype_counts = {}

        # 2. Row Reconstruction (Visible Stars) mapped into Constellations
        for star in stars:
            path = star.get("path", "Unknown")
            telemetry = star.get("telemetry", {})
            lang_raw = str(star.get("lang_id", "Unknown")).lower()
            c_name = star.get("constellation", "__monolith__")
            
            # --- THE ULTIMATE UPSTREAM BYPASS FIX ---
            doc_languages = {"markdown", "plaintext", "rst", "text", "md"}
            if lang_raw in doc_languages and len(star.get("risk_vector", [])) < len(self.RISK_SCHEMA):
                # Inject 18-point synthetic Risk Blanket
                star["risk_vector"] = [0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 100.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
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
                # Hide it from the generic loop so we can format it explicitly below
                if custom_key not in ["ownership", "AI Threat Score"]: 
                    display_key = custom_key.replace('_', ' ').title()
                    if display_key == "Purpose":
                        display_key = "Museum Entry"
                    identity_block[display_key] = custom_val

            identity_block["Lock Tier"] = star.get("lock_tier", telemetry.get("identity_lock_tier", 4))
            identity_block["Identity Proof"] = telemetry.get("identity_source_proof", star.get("source_proof", "Discovery"))
            
            # ---> NEW: EXPLICITLY INJECT AI SCORE <---
            if "AI Threat Score" in domain_data:
                identity_block["AI Threat Confidence"] = domain_data["AI Threat Score"]
            
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

            # Track the archetype for the folder-level summary
            arch = telemetry.get("archetype", "Unknown Archetype")
            if c_name not in folder_archetype_counts:
                folder_archetype_counts[c_name] = {}
            folder_archetype_counts[c_name][arch] = folder_archetype_counts[c_name].get(arch, 0) + 1

            # ---> NEW: FORMAT MITIGATIONS <---
            mitigation_data = telemetry.get("mitigation_telemetry", {})
            formatted_mitigations = {
                key.replace('_', ' ').title(): f"{val} instances"
                for key, val in mitigation_data.items() if val > 0
            }

            # Assemble the star profile
            star_profile = {
                "1. Identity": identity_block,
                "2. Spatial Coordinates": {
                    "X": star.get("pos_x", 0.0), 
                    "Y": star.get("pos_y", 0.0), 
                    "Z": star.get("pos_z", 0.0)
                },
                "3. Architectural Profile": {
                    "Repository Archetype": arch,
                    "Repository Drift (Z-Score)": telemetry.get("global_drift", 0.0),
                    "Repository Fingerprint": {k: round(v, 3) for k, v in telemetry.get("archetype_fingerprint", {}).items()} if isinstance(telemetry.get("archetype_fingerprint"), dict) else {},
                    
                    "File Archetype": telemetry.get("local_archetype", "N/A"),
                    "File Drift (Z-Score)": telemetry.get("local_drift", 0.0),
                    "File Fingerprint": {k: round(v, 3) for k, v in telemetry.get("local_fingerprint", {}).items()} if isinstance(telemetry.get("local_fingerprint"), dict) else {},
                    "Total LOC": star.get("total_loc", 0),
                    "coding LOC": star.get("coding_loc", 0),
                    "Documentation LOC": star.get("doc_loc", 0),
                    "Structural Mass": round(star.get("file_impact", 0.0), 3),
                    "Control Flow Ratio": f"{round(telemetry.get('control_flow_ratio', 0.0) * 100, 1)}%",
                    "Popularity Rank": telemetry.get("popularity", 0),
                    "Raw Churn Frequency": telemetry.get("raw_churn_freq", 0.0),
                    "Author Distribution": telemetry.get("author_distribution", 0.0),
                    "Ownership Entropy": telemetry.get("ownership_entropy", 0.0),
                    "Raw Cognitive Density": telemetry.get("densities", {}).get("cog_raw", 0.0)
                },
                "4. Risk Exposures": exposures_dict,
                "5. Function Analysis (Satellites)": [
                    {
                        "Function Name": sat.get("name", "Unknown"),
                        "Structural Impact": sat.get("impact", sat.get("magnitude", 0.0)),
                        "Lines of Code (LOC)": sat.get("loc", 0),
                        "Control Flow Branches": sat.get("branch", sat.get("branch_count", 0)),
                        "Input Parameters": sat.get("args", sat.get("args_count", 0)),
                        "Control Flow Ratio": f"{round((sat.get('control_flow_ratio') or sat.get('cf_ratio') or 0.0) * 100, 1)}%",
                        "Start Line": sat.get("start_line", 0),
                        "End Line": sat.get("end_line", 0)
                    }
                    for sat in star.get("satellites", []) if isinstance(sat, dict)
                ],
                "6. Contextual Mitigations & Amplifications": formatted_mitigations if formatted_mitigations else "None Detected",
                "7. Structural DNA (Net Mitigated Signals)": {
                    label: v for label, v in zip(hit_labels, star.get("hit_vector") or [0] * len(hit_labels))
                },
                # ---> THE 4 DEPENDENCY METRICS (Read cleanly from RAM) <---
                "8. Dependency Network": {
                    "Direct Upstream (Fragility)": star.get("dependency_network", {}).get("direct_upstream", len(star.get("raw_imports", []))),
                    "Direct Downstream (Blast Radius)": star.get("dependency_network", {}).get("direct_downstream", telemetry.get("popularity", 0)),
                    "Total Upstream (Absolute Fragility)": star.get("dependency_network", {}).get("total_upstream", 0),
                    "Total Downstream (Absolute Blast Radius)": star.get("dependency_network", {}).get("total_downstream", 0)
                },
                
                "9. Extracted Dependencies": sorted(list(star.get("raw_imports", [])))
            }
            
            # Map the star into its parent constellation
            if c_name not in pretty_constellations:
                pretty_constellations[c_name] = {"Constellation Mass": 0.0, "Stars / Files": {}}
            pretty_constellations[c_name]["Stars / Files"][path] = star_profile

        # --- CALCULATE FOLDER-LEVEL ARCHETYPE SUMMARIES ---
        for c_name, c_data in pretty_constellations.items():
            folder_files = len(c_data.get("Stars / Files", {}))
            arch_counts = folder_archetype_counts.get(c_name, {})
            
            if folder_files > 0 and arch_counts:
                # Calculate percentages and sort highest to lowest
                fingerprint = {
                    name: f"{round((count / folder_files) * 100.0, 1)}%" 
                    for name, count in sorted(arch_counts.items(), key=lambda x: x[1], reverse=True)
                }
                
                # Reconstruct the dictionary so the Fingerprint sits cleanly at the top of the JSON
                reordered_c_data = {
                    "Constellation Mass": c_data.get("Constellation Mass", 0.0),
                    "File Count": c_data.get("File Count", folder_files),
                    "Ecosystem Fingerprint (Archetypes)": fingerprint,
                    "Average Risk Exposures": c_data.get("Average Risk Exposures", {}),
                    "Stars / Files": c_data.get("Stars / Files", {})
                }
                pretty_constellations[c_name] = reordered_c_data

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

        # ==========================================================
        # 4. FORENSIC SECURITY & VULNERABILITY AUDIT (Section 3)
        # ==========================================================
        sec_risk_mapping = {
            "secrets_risk": {"label": "Secrets Risk Exposure", "threshold": 0.1},
            "obscured_payload": {"label": "Hidden Malware Risk Exposure", "threshold": 60.0},
            "logic_bomb": {"label": "Logic Bomb / Sabotage Risk Exposure", "threshold": 50.0},
            "injection_surface": {"label": "Injection Surface Risk Exposure", "threshold": 65.0},
            "memory_corruption": {"label": "Memory Corruption Risk Exposure", "threshold": 60.0}
        }
        
        sec_hit_mapping = {
            "sec_danger": "Dangerous Code Execution (Eval/Exec)",
            "sec_safety_neg": "Security Rule Bypasses",
            "sec_io": "Suspicious Network Connections",
            "sec_flux": "Global Environment Tampering",
            "sec_heat_triggers": "Scrambled / Obfuscated Code",
            "sec_graveyard": "Shadow Logic (Hidden Code)",
            "sec_bitwise_hits": "Sub-Atomic Decryption (Custom XOR)",
            "sec_shadow_imports": "Steganographic Execution (Shadow Imports)",
            "sec_homoglyphs": "Unicode Smuggling (Homoglyph Imports)"
        }

        quarantined_files = []
        ml_threat_files = [] # ---> NEW: Container for XGBoost hits
        
        vuln_exposures = {
            data["label"]: {
                "Alert Threshold": f">= {data['threshold']}%", 
                "Artifacts Flagged": 0, 
                "Critical Files": []
            } for key, data in sec_risk_mapping.items()
        }
        
        raw_threat_hits = {
            "_description": "The total number of times these specific malicious regex patterns were triggered across all scanned files.",
            **{label: 0 for label in sec_hit_mapping.values()}
        }

        # Safe index lookups
        risk_indices = {k: self.RISK_SCHEMA.index(k) for k in sec_risk_mapping.keys() if k in self.RISK_SCHEMA}
        hit_indices = {k: self.HIT_SCHEMA.index(k) for k in sec_hit_mapping.keys() if k in self.HIT_SCHEMA}

        # Sweep the stars for security anomalies
        for star in stars:
            path = star.get("path", "Unknown")
            domain_ctx = star.get("telemetry", {}).get("domain_context", {})

            # ---> NEW: HARVEST ML SCORES <---
            is_ml_threat = star.get("is_ml_threat", False)
            ai_score_str = domain_ctx.get("AI Threat Score", "0.0%")
            
            try:
                ai_score_float = float(str(ai_score_str).replace('%', ''))
            except ValueError:
                ai_score_float = 0.0

            if is_ml_threat or ai_score_float >= 50.0:
                ml_threat_files.append({
                    "Path": path,
                    "AI_Confidence": ai_score_float,
                    "Formatted_Score": ai_score_str
                })
            
            # THE FIX: Read the exact bypass alert injected by the SignalProcessor Shunt
            
            if domain_ctx.get("alert") == "CRITICAL LEAK BYPASS":
                quarantined_files.append({
                    "Path": path,
                    "Diagnostic": f"CRITICAL LEAK (Exposed Secret/Key): {domain_ctx.get('aperture_reason', 'Manual Bypass')}"
                })
                
            risk_vector = star.get("risk_vector", [])
            if len(risk_vector) == len(self.RISK_SCHEMA):
                for r_key, r_idx in risk_indices.items():
                    score = risk_vector[r_idx]
                    mapping = sec_risk_mapping[r_key]
                    if score >= mapping["threshold"]:
                        label = mapping["label"]
                        vuln_exposures[label]["Critical Files"].append({"Path": path, "Score": f"{score:.1f}%"})
                        vuln_exposures[label]["Artifacts Flagged"] += 1
            
            # Aggregate the raw threat hits
            hit_vector = star.get("hit_vector")
            if isinstance(hit_vector, list) and len(hit_vector) == len(self.HIT_SCHEMA):
                for h_key, h_idx in hit_indices.items():
                    hits = hit_vector[h_idx]
                    if hits > 0:
                        label = sec_hit_mapping[h_key]
                        raw_threat_hits[label] += hits

        # --- THE FALSE POSITIVE FIX: Decouple Active Threats from Surface Risks ---
        # 1. Count actual malicious regex hits (ignoring the _description string)
        malicious_hits_total = sum(v for k, v in raw_threat_hits.items() if isinstance(v, int))
        
        # 2. Check for explicit malware
        has_malware = vuln_exposures["Hidden Malware Risk Exposure"]["Artifacts Flagged"] > 0
        has_secrets = vuln_exposures["Secrets Risk Exposure"]["Artifacts Flagged"] > 0

        # ---> NEW: SORT AND FORMAT THE AI HITLIST <---
        ml_threat_files.sort(key=lambda x: x["AI_Confidence"], reverse=True)
        top_ml_threats = [
            {
                "Path": threat["Path"], 
                "Confidence": threat["Formatted_Score"], 
                "Model": "XGBoost Structural DNA"
            }
            for threat in ml_threat_files
        ]

        # 3. Tiered Status Routing (AI IS NOW THE SUPREME AUTHORITY)
        if ml_threat_files:
            audit_status = "AI_CONFIRMED_MALWARE_DETECTED"
        elif quarantined_files or has_malware or has_secrets or malicious_hits_total > 0:
            audit_status = "CRITICAL_THREATS_DETECTED (Rule-Based)"
        elif any(v["Artifacts Flagged"] > 0 for v in vuln_exposures.values()):
            audit_status = "ELEVATED_SURFACE_RISK" 
        else:
            audit_status = "SECURE_NO_MALWARE_DETECTED"

        security_audit = {
            "Audit Status": audit_status,
            "AI Threat Intelligence (XGBoost)": {
                "Infected Files Detected": len(ml_threat_files),
                "Critical Targets": top_ml_threats
            },
            "Scope": {
                "Artifacts Evaluated": len(stars),
                "Threat Signatures Monitored": len(sec_hit_mapping),
                "Vulnerability Vectors Calculated": len(sec_risk_mapping)
            },
            "Exposed Secrets & Credentials (Quarantined Files)": quarantined_files,
            "Vulnerability Exposures (Rule-Based Threshold Breaches)": vuln_exposures,
            "Raw Threat Signature Hits (Total Repository Occurrences)": raw_threat_hits
        }

        # ==========================================================
        # 5. Final Mission Archive Packaging
        # ==========================================================
        
        # --- THE FIX: Format the Global Ecosystem Fingerprint ---
        global_fingerprint = summary.get("ecosystem_fingerprint", {})
        pretty_global_fingerprint = {}
        
        if "ml_clusters" in global_fingerprint or "static_mass" in global_fingerprint:
            # New V6.3 Nested Structure
            if "ml_clusters" in global_fingerprint:
                pretty_global_fingerprint["Active Execution Logic (ML Clusters)"] = {
                    k: f"{v['pct']}% ({v['count']} files)" for k, v in global_fingerprint["ml_clusters"].items()
                }
            if "static_mass" in global_fingerprint:
                pretty_global_fingerprint["Inert Structural Mass (Static Categories)"] = {
                    k: f"{v['pct']}% ({v['count']} files)" for k, v in global_fingerprint["static_mass"].items()
                }
        else:
            # Legacy Fallback
            pretty_global_fingerprint = {
                k: f"{v}%" for k, v in global_fingerprint.items()
            } if global_fingerprint else "No archetypes detected."
            
        summary["Global Architectural Fingerprint"] = pretty_global_fingerprint
        
        # Explicitly format the Repo Macro-Species if present
        macro = summary.get("repo_macro_species", {})
        if macro:
            summary["Repository Macro-Species (Architecture)"] = {
                "Classification": macro.get("name", "Unclassified"),
                "Architectural Drift (Z-Score)": macro.get("z_score", 0.0)
            }

        mission_audit = {
            "Audit Protocol": "GitGalaxy v6.3.2-Audit",
            "1. Forensic Trail (Traceability)": forensic_trail,
            "2. Global Synthesis Summary": summary,
            "3. Forensic Security & Vulnerability Audit": security_audit,
            "4. High-Value Forensic Report": forensic_report,
            "5. Dark Matter (Excluded Artifacts)": pretty_singularity,
            "6. Visible Matter (Scanned Artifacts)": pretty_constellations
        }

        # --- THE FIX ---
        # Convert the output_path handed to us by the orchestrator into a Path object
        target_path = Path(output_path)

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