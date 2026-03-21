import json
import argparse
import sys
import os
import re
from datetime import datetime
from pathlib import Path

# ==============================================================================
# GitGalaxy Phase 9: Astrograph Decoder (The Pretty Printer)
# Strategy v6.2.0 Protocol: Fully Dynamic Schema Extraction & Auto-Scaling
# ==============================================================================

def format_label(key: str) -> str:
    """Provides human-readable formatting for schema keys dynamically for auditing."""
    clean_key = re.sub(r'_x\d+$', '', key)
    
    friendly_names = {
        "m_locs": "Meaningful LOC",
        "locs": "Total LOC",
        "loc": "LOC",
        "pos_x": "Position X",
        "pos_y": "Position Y",
        "pos_z": "Position Z",
        "lang_ids": "Language",
        "mass": "Structural Mass",
        "entropy": "Entropy Signal",
        "cog_raw": "Raw Cognitive Density",
        "raw_churn_freq": "Raw Churn Frequency",
        "type_id": "Satellite Archetype",
        "func_start": "Total Functions",
        "class_start": "Total Classes",
        "api": "API",
        "io": "I/O",
        "ui": "UI",
        "ssr": "SSR",
        # --- NEW: Spec-Compliant Key Aliasing ---
        "verification": "Testing Exposure",
        "cognitive_load": "Cognitive Load Exposure",
        "safety_score": "Safety Exposure",
        "tech_debt": "Tech Debt Exposure",
        "graveyard": "Dead Code Exposure",
        "spec_match": "Specification Exposure",
        "civil_war": "Layout Unity (Civil War)"
    }
    
    if clean_key in friendly_names:
        return friendly_names[clean_key]
        
    return " ".join(word.capitalize() for word in clean_key.split('_'))

def descale(key, value, default_scalar=1.0):
    """
    Dynamically scales integers back to floats based on schema suffixes.
    e.g., 'angle_x10' -> divides value by 10 automatically.
    """
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return value
        
    match = re.search(r'_x(\d+)$', key)
    if match:
        scalar = float(match.group(1))
        return round(value / scalar, 3)
    
    if default_scalar != 1.0:
        return round(value / default_scalar, 3)
        
    return value

def decode_galaxy(input_path, output_path=None):
    print(f"Astrograph Decoder Online: Parsing {input_path}...")

    input_file = Path(input_path)
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Fatal Error: Could not read target artifact: {e}")
        sys.exit(1)

    # 1. METADATA & SCHEMA EXTRACTION
    meta = data.get('meta', {})
    schemas = meta.get('schemas', {})
    lookups = schemas.get('lookups', meta.get('lookups', {}))
    scalars = schemas.get('scalars', {"exposure": 1000, "physics": 10})
    
    exp_scalar = float(scalars.get("exposure", 1000.0))
    phys_scalar = float(scalars.get("physics", 10.0))
    
    # Lookup Tables
    lang_table = lookups.get('languages', [])
    texture_table = lookups.get('textures', [])
    author_table = lookups.get('authors', [])
    proof_table = lookups.get('proofs', [])
    reason_table = lookups.get('reasons', [])
    
    # Dynamic Schema Identification
    galaxy_columns = schemas.get('galaxy_columns', schemas.get('galaxy', []))
    hit_schema = schemas.get('hit_vector', [])
    satellite_schema = schemas.get('satellites', [])
    
    # Automatically locate the risk schema regardless of its scaling suffix
    risk_schema_key = next((k for k in schemas.keys() if k.startswith("risk_vector")), "risk_vector")
    risk_schema = schemas.get(risk_schema_key, [])
    
    risk_scalar = 1.0
    match = re.search(r'_x(\d+)$', risk_schema_key)
    if match:
        risk_scalar = float(match.group(1))

    # 3. COLUMNAR ARRAYS
    galaxy_data = data.get('galaxy', {})
    paths = galaxy_data.get('paths', [])
    count = len(paths)
    
    if count == 0:
        print("Empty Galaxy detected. Checking Singularity only.")

    # Helper to safely fetch from columnar arrays without IndexError
    def get_val(dataset, col_name, idx, default=None):
        arr = dataset.get(col_name, [])
        return arr[idx] if idx < len(arr) else default

    pretty_files = {}

    # ==========================================================================
    # 4. ROW RECONSTRUCTION LOOP (Visible Stars)
    # ==========================================================================
    for i in range(count):
        file_path = paths[i]
        telemetry = get_val(galaxy_data, "telemetry", i, {})
        
        # Identity Lookups
        lang_idx = get_val(galaxy_data, "lang_ids", i, -1)
        lang_str = lang_table[lang_idx] if 0 <= lang_idx < len(lang_table) else "Unknown"
        
        a_id = telemetry.pop("author_id", -1)
        author = author_table[a_id] if 0 <= a_id < len(author_table) else telemetry.pop("ownership", "Unknown Architect")
        
        p_id = telemetry.pop("proof_id", -1)
        proof = proof_table[p_id] if 0 <= p_id < len(proof_table) else telemetry.pop("source_proof", "Discovery")
        
        identity_obj = {
            "Filename": get_val(galaxy_data, "names", i, "Unknown"),
            "Path": file_path,
            "Language": lang_str.title() if lang_str else "Unknown",
            "Architect": author,
            "Purpose": telemetry.pop("purpose", "Standard Logic Matrix"),
            "Identification Evidence": proof
        }
        
        if "lock_tier" in telemetry:
            identity_obj["Lock Tier"] = telemetry.pop("lock_tier")

        # Spatial Coordinates
        spatial_obj = {
            "X": get_val(galaxy_data, "pos_x", i, 0.0),
            "Y": get_val(galaxy_data, "pos_y", i, 0.0),
            "Z": get_val(galaxy_data, "pos_z", i, 0.0)
        }

        # Dynamic Galactic Profile
        profile_obj = {}
        processed_keys = {"names", "paths", "lang_ids", "pos_x", "pos_y", "pos_z", "risks", "hits", "satellites", "telemetry"}
        
        # Loop dynamically through ANY new columns added to the core galaxy object
        for col_key in galaxy_columns:
            if col_key in processed_keys:
                continue
                
            val = get_val(galaxy_data, col_key, i)
            if val is None: continue
            
            # Apply default scalars for universal keys if they lack a suffix
            if col_key == "mass":
                val = descale(col_key, val, phys_scalar)
            elif col_key == "entropy":
                # FIX: Entropy was scaled by 10 (phys_scalar) in record_keeper, not 1000 (exp_scalar)!
                val = descale(col_key, val, phys_scalar) 
            else:
                val = descale(col_key, val)
                
            profile_obj[format_label(col_key)] = val

        # Flatten any remaining "Ghost Metadata" stuffed inside the telemetry object
        for tk, tv in telemetry.items():
            if isinstance(tv, dict):
                for sub_k, sub_v in tv.items():
                    profile_obj[f"{format_label(tk)} - {format_label(sub_k)}"] = descale(sub_k, sub_v)
            else:
                profile_obj[format_label(tk)] = descale(tk, tv)

        # Risk Exposures (Dynamically scales down and converts to human readable percentages)
        risk_obj = {}
        raw_risks = get_val(galaxy_data, "risks", i, [])
        for r_idx, r_key in enumerate(risk_schema):
            if r_idx < len(raw_risks):
                val = raw_risks[r_idx]
                if risk_scalar > 1.0:
                    val = round((val / risk_scalar) * 100, 2)
                elif isinstance(val, (int, float)) and val <= 1.0:
                    val = round(val * 100, 2)
                risk_obj[format_label(r_key)] = f"{val}%"
            else:
                risk_obj[format_label(r_key)] = "0%"

        # Hardware Counters (Hits)
        hit_obj = {}
        raw_hits = get_val(galaxy_data, "hits", i, [])
        for h_idx, h_key in enumerate(hit_schema):
            if h_idx < len(raw_hits):
                hit_obj[format_label(h_key)] = raw_hits[h_idx]
            else:
                hit_obj[format_label(h_key)] = 0
                
        # --- NEW: On-The-Fly Calculations ---
        profile_obj["Total Entities Detected"] = hit_obj.get("Total Functions", hit_obj.get("Func Start", 0)) + hit_obj.get("Total Classes", hit_obj.get("Class Start", 0))
        
        branch = hit_obj.get("Branch", 0)
        linear = hit_obj.get("Linear", 0)
        total_flow = branch + linear
        profile_obj["Logic Ratio"] = f"{round((branch / total_flow) * 100, 1)}%" if total_flow > 0 else "0.0%"

        # Function Analysis / Satellites
        sat_array = []
        raw_sats = get_val(galaxy_data, "satellites", i, [])
        for s_data in raw_sats:
            sat_obj = {}
            for s_idx, s_key in enumerate(satellite_schema):
                if s_idx < len(s_data):
                    val = s_data[s_idx]
                    
                    # --- NEW: Registry Recovery (Checks both texture and type_id) ---
                    if s_key in ("type_id", "texture"):
                        val = texture_table[val].title() if isinstance(val, int) and 0 <= val < len(texture_table) else "Unknown"
                        sat_obj[format_label(s_key)] = val
                    else:
                        clean_key = re.sub(r'_x\d+$', '', s_key)
                        sat_obj[format_label(clean_key)] = descale(s_key, val)
            sat_array.append(sat_obj)


        pretty_files[file_path] = {
            "1. Identity": identity_obj,
            "2. Spatial Coordinates": spatial_obj,
            "3. Galactic Profile": profile_obj,
            "4. Risk Exposures": risk_obj,
            "5. Function Analysis (Satellites)": sat_array,
            "6. Structural DNA (Raw Counters)": hit_obj
        }

    # ==========================================================================
    # 5. SINGULARITY / DARK MATTER PIVOT
    # ==========================================================================
    pretty_singularity = []
    sing_cols = schemas.get("singularity_columns", [])
    sing_data = data.get("singularity", {})
    
    if sing_cols and sing_data:
        s_paths = sing_data.get("paths", [])
        print(f"Astrograph: Decoding {len(s_paths)} Dark Matter anomalies...")
        
        for s_idx in range(len(s_paths)):
            sing_obj = {}
            for col_key in sing_cols:
                raw_val = get_val(sing_data, col_key, s_idx)
                
                # Descale tables based on known lookup integer pointers
                if col_key == "reasons" and isinstance(raw_val, int):
                    val = reason_table[raw_val] if 0 <= raw_val < len(reason_table) else "Unknown"
                elif col_key == "proofs" and isinstance(raw_val, int):
                    val = proof_table[raw_val] if 0 <= raw_val < len(proof_table) else "Discovery"
                elif col_key == "failed_claims" and isinstance(raw_val, int):
                    val = lang_table[raw_val].title() if 0 <= raw_val < len(lang_table) else "Unknown"
                elif col_key == "confidences":
                    val = f"{round((raw_val / exp_scalar) * 100, 1)}%" if isinstance(raw_val, (int, float)) else raw_val
                elif col_key == "lock_tiers":
                    val = f"Tier {raw_val}" if isinstance(raw_val, int) else raw_val
                else:
                    val = descale(col_key, raw_val)
                    
                sing_obj[format_label(col_key)] = val
            pretty_singularity.append(sing_obj)

    # ==========================================================================
    # 6. ENVELOPE SEAL
    # ==========================================================================
    mission_envelope = {
        "Decoding Timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "Engine Metadata": meta.get("session", {}),
        "Global Summary": data.get("global_summary", {}),
        "Forensics Report": data.get("forensic_report", {}),
        "Dark Matter (Singularity)": pretty_singularity,
        "Visible Star Manifest": pretty_files
    }

    if output_path:
        final_out = Path(output_path)
    else:
        final_out = input_file.parent / f"pretty_{input_file.name}"

    try:
        with open(final_out, 'w', encoding='utf-8') as f:
            json.dump(mission_envelope, f, indent=4, ensure_ascii=False)
        
        kb_size = os.path.getsize(final_out) / 1024.0
        print(f"Mission Success! Galaxy pivoted into human-readable manifest -> {final_out} ({kb_size:.1f} KB)")
    except Exception as e:
        print(f"Fatal Write Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GitGalaxy v6.2.0 Dynamic Astrograph Decoder")
    parser.add_argument("input", help="Path to columnar galaxy.json")
    parser.add_argument("--out", help="Optional output path")
    
    args = parser.parse_args()
    decode_galaxy(args.input, args.out)