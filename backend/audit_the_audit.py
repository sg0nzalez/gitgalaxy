import json
import sys
import argparse
from pathlib import Path
from collections import Counter, defaultdict

def audit_the_audit(filepath):
    print(f"\n🔍 [GitGalaxy] Initiating Deep Telemetry Audit on: {filepath}...\n")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"🚨 CRITICAL FAILURE: JSON Truncation or Corruption Detected!\nError: {e}")
        sys.exit(1)

    # Standardize data structure
    stars = data.get("stars", [])
    
    # If the standard format isn't there, dig into the "5. Visible Star Manifest"
    if not stars and isinstance(data, dict):
        manifest = data.get("5. Visible Star Manifest", {})
        for filepath_key, val in manifest.items():
            if isinstance(val, dict) and "1. Identity" in val:
                star = {
                    "name": val["1. Identity"].get("Filename", "UNKNOWN"),
                    "path": val["1. Identity"].get("Path", "UNKNOWN"),
                    "lang_id": val["1. Identity"].get("Language", "unknown").lower(),
                    "coding_loc": val["3. Galactic Profile"].get("coding LOC", 1),
                    "file_impact": val["3. Galactic Profile"].get("Structural Mass", 0.0),
                    "hit_vector": val.get("6. Structural DNA (Raw Hits)", {}),
                    "satellites": val.get("5. Function Analysis (Satellites)", [])
                }
                stars.append(star)

    total_stars = len(stars)
    if total_stars == 0:
        print("🚨 CRITICAL FAILURE: Unrecognized JSON structure or 0 stars found.")
        sys.exit(1)

    print(f"✅ JSON Intact. Parsed {total_stars} stars.\n")

    # --- Tracking Variables ---
    lang_counts = Counter()
    zero_loc_files = 0
    undeterminable_count = 0
    
    ext_func_names = defaultdict(list)
    runaway_regexes = defaultdict(list)

    for star in stars:
        name = star.get("name", "UNKNOWN")
        path = star.get("path", "UNKNOWN")
        lang_id = star.get("lang_id", "unknown")
        
        # Safely extract LOC (fallback to 1 to prevent division by zero)
        loc = max(star.get("coding_loc", star.get("loc", 1)), 1) 
        
        # Safely extract hits and satellites
        hits = star.get("hit_vector", star.get("equations", {}))
        satellites = star.get("satellites", star.get("functions", []))

        # 1. Global Tally
        lang_counts[lang_id] += 1
        if lang_id in ["undeterminable", "unknown"]:
            undeterminable_count += 1
        
        if loc <= 1 and star.get("size_bytes", 0) > 0:
            zero_loc_files += 1

        # 2. Function Name Extraction (TLC for func_start)
        ext = Path(path).suffix.lower() or "no_extension"
        for sat in satellites:
            func_name = sat.get("name", sat.get("Name", ""))
            if func_name:
                ext_func_names[ext].append(func_name)

        # 3. Hits / LOC Density Assessment (Catching wild regexes)
        for metric, count in hits.items():
            if not isinstance(count, (int, float)) or count == 0:
                continue
                
            density = count / loc
            
            # Map human-readable keys that naturally exceed 1.0 (like function arguments)
            high_density_metrics = [
                "args", "Function Parameters", "function input parameter mass", 
                "Collection Iterators / Comprehensions", "comprehensions", 
                "high density collection logic",
                "Structural Space Indentations", "indentation structural unity conflict",
                "Pointer Arithmetic & Addressing"
            ]
            
            # Use a slightly higher threshold for naturally dense metrics
            threshold = 2.5 if metric in high_density_metrics else 1.0
            
            if density > threshold:
                runaway_regexes[ext].append({
                    "file": name,
                    "path": path,
                    "metric": metric,
                    "hits": count,
                    "loc": loc,
                    "density": round(density, 2)
                })

    # --- REPORTING (TERMINAL) ---
    print("--- 🌌 ECOSYSTEM CENSUS ---")
    for lang, count in lang_counts.most_common(5):
        print(f"  - {lang.ljust(15)}: {count} files")
        
    print("\n--- ⚠️ PHYSICS INTEGRITY REPORT ---")
    fail_rate = (undeterminable_count / total_stars) * 100
    print(f"  {'🚨' if fail_rate > 10 else '✅'} Singularity Rate: {fail_rate:.1f}%")
    print(f"  {'🚨' if zero_loc_files > 0 else '✅'} Zero-LOC Ghost Files: {zero_loc_files}")

    print("\n--- 🧬 REGEX DIAGNOSTICS (Terminal Summary) ---")
    
    total_runaways = sum(len(issues) for issues in runaway_regexes.values())
    if total_runaways > 0:
        print(f"  🚨 Detected {total_runaways} instance(s) of runaway regexes (Hits > LOC).")
        flat_runaways = [item for sublist in runaway_regexes.values() for item in sublist]
        flat_runaways.sort(key=lambda x: x['density'], reverse=True)
        for r in flat_runaways[:3]:
            print(f"     -> {r['metric']} in {r['file']} (Hits: {r['hits']} | LOC: {r['loc']} | Density: {r['density']}x)")
    else:
        print("  ✅ No runaway regexes detected (Density < 1.0x).")

    print(f"\n  🔍 Scanning {len(ext_func_names)} extensions for function duplication...")
    found_duplicates = False
    for ext, names in ext_func_names.items():
        name_counts = Counter(names)
        suspicious_dupes = {k: v for k, v in name_counts.items() if v > 50}
        if suspicious_dupes:
            found_duplicates = True
            print(f"     [{ext}] Suspicious high-frequency captures:")
            for k, v in sorted(suspicious_dupes.items(), key=lambda item: item[1], reverse=True)[:3]:
                print(f"        - '{k}': caught {v} times")
    
    if not found_duplicates:
         print("  ✅ No highly suspicious function duplications detected.")

    # --- REPORTING (JSON EXPORT) ---
    
    # NEW: Sort the runaway regexes by density (highest first) for the JSON report
    sorted_runaway_regexes = {}
    for ext, issues in runaway_regexes.items():
        sorted_runaway_regexes[ext] = sorted(issues, key=lambda x: x['density'], reverse=True)

    report_data = {
        "1. Summary": {
            "total_files_parsed": total_stars,
            "total_runaway_regex_events": total_runaways
        },
        "2. Runaway Regexes (Hits > LOC)": sorted_runaway_regexes,
        "3. Function Duplication Analysis": {}
    }

    for ext, names in ext_func_names.items():
        counts = Counter(names)
        dupes = {k: v for k, v in counts.items() if v > 1}
        if dupes:
            report_data["3. Function Duplication Analysis"][ext] = dict(sorted(dupes.items(), key=lambda item: item[1], reverse=True))

    out_path = Path(filepath).stem + "_deep_diagnostics.json"
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=4)
        
    print(f"\n💾 Deep Diagnostics Report successfully exported to: {out_path}")
    print("   Open this file to review all function duplicates and regex density anomalies.\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GitGalaxy Telemetry Auditor")
    parser.add_argument("filepath", help="Path to the galaxy.json or audit.json file")
    args = parser.parse_args()
    
    audit_the_audit(args.filepath)