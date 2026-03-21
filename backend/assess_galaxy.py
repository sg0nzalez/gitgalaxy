import json
import os
import sys
from collections import defaultdict

def load_galaxy_map(filename='apollo_galaxy.json'):
    """Loads the JSON map relative to the script location."""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)
        
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: Could not find '{filename}' in {script_dir}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"❌ Error: '{filename}' is not valid JSON.")
        sys.exit(1)

def analyze_system(data):
    """Aggregates stats from the columnar data."""
    
    # 1. Unpack Columns
    galaxy = data.get('galaxy', {})
    meta = data.get('meta', {})
    
    names = galaxy.get('names', [])
    lang_ids = galaxy.get('lang_ids', [])
    satellites_list = galaxy.get('satellites', []) # List of lists of satellites
    
    # 2. Unpack Lookups
    lang_lookup = meta.get('lookups', {}).get('langs', [])
    
    # 3. Aggregators
    stats = defaultdict(lambda: {'files': 0, 'functions': 0, 'empty_files': 0})
    total_files = len(names)
    total_functions = 0
    
    # --- INTEGRITY CHECK ---
    # Ensure columns match. If satellites list is short, pad it to avoid IndexError.
    if len(satellites_list) < total_files:
        print(f"⚠️  WARNING: Data Corruption Detected.")
        print(f"    'names' column has {total_files} entries.")
        print(f"    'satellites' column has {len(satellites_list)} entries.")
        print(f"    > Padding 'satellites' with empty lists to continue assessment...\n")
        # Pad with empty lists so the loop doesn't crash
        satellites_list.extend([[] for _ in range(total_files - len(satellites_list))])

    # 4. Iterate & Count
    for i in range(total_files):
        # Resolve Language
        l_id = lang_ids[i]
        lang_name = lang_lookup[l_id] if l_id < len(lang_lookup) else "unknown"
        
        # Count Satellites (Functions)
        # satellites_list[i] is a list of satellites for file i
        satellites = satellites_list[i]
        sat_count = len(satellites)
        
        # Update Stats
        stats[lang_name]['files'] += 1
        stats[lang_name]['functions'] += sat_count
        total_functions += sat_count
        
        if sat_count == 0:
            stats[lang_name]['empty_files'] += 1

    return {
        'total_files': total_files,
        'total_functions': total_functions,
        'scanner_version': meta.get('session', {}).get('scanner_version', 'Unknown'),
        'timestamp': meta.get('session', {}).get('timestamp', 'Unknown'),
        'breakdown': stats
    }

def print_report(results):
    """Prints a formatted CLI report."""
    print(f"\n========================================================")
    print(f"   GitGalaxy System Assessment | v{results['scanner_version']}")
    print(f"   Timestamp: {results['timestamp']}")
    print(f"========================================================")
    
    print(f"\n🌍 UNIVERSE OVERVIEW")
    print(f"   • Total Files Scanned:      {results['total_files']:,}")
    print(f"   • Total Functions Detected: {results['total_functions']:,}")
    
    avg_func = results['total_functions'] / max(results['total_files'], 1)
    print(f"   • Avg Functions/File:       {avg_func:.2f}")

    print(f"\n📊 LANGUAGE BREAKDOWN")
    print(f"   {'LANGUAGE':<15} | {'FILES':<8} | {'FUNCS':<8} | {'FUNC/FILE':<10} | {'ZERO-FUNC FILES':<15}")
    print(f"   {'-'*15} | {'-'*8} | {'-'*8} | {'-'*10} | {'-'*15}")
    
    sorted_langs = sorted(results['breakdown'].items(), key=lambda x: x[1]['files'], reverse=True)
    
    anomalies = []

    for lang, data in sorted_langs:
        files = data['files']
        funcs = data['functions']
        empty = data['empty_files']
        ratio = funcs / max(files, 1)
        
        # Check for anomalies
        # Anomaly = Language known for functions has 0 functions across many files
        if funcs == 0 and files > 0:
            anomalies.append(f"⚠️  {lang}: Detected {files} files but 0 functions. Regex might be failing.")
        elif (empty / files) > 0.9 and files > 10:
             anomalies.append(f"⚠️  {lang}: 90%+ of files have no detected functions. Check 'func_start' regex.")

        print(f"   {lang:<15} | {files:<8,} | {funcs:<8,} | {ratio:<10.2f} | {empty:<15} ({int((empty/files)*100)}%)")

    print(f"\n🔍 ANOMALY DETECTION")
    if anomalies:
        for alert in anomalies:
            print(f"   {alert}")
    else:
        print(f"   ✅ No major anomalies detected. System looks nominal.")
    
    print(f"\n========================================================\n")

if __name__ == "__main__":
    data = load_galaxy_map()
    results = analyze_system(data)
    print_report(results)