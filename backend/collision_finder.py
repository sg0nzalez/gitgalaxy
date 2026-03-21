import collections
import json
from gitgalaxy_standards_v011 import LANGUAGE_DEFINITIONS

def scan_for_collisions(registry):
    """
    Scans the GitGalaxy language registry to identify all overlapping
    extensions and exact_matches across the ecosystem, while also 
    calculating total unique coverage.
    """
    extension_map = collections.defaultdict(list)
    exact_match_map = collections.defaultdict(list)

    # 1. Build the inverted index for all languages
    for lang, config in registry.items():
        # Track Extensions
        for ext in config.get('extensions', []):
            # Normalize to lowercase just in case there's casing weirdness (like .C vs .c)
            extension_map[ext.lower()].append(lang)
            
        # Track Exact Matches
        for exact in config.get('exact_matches', []):
            exact_match_map[exact].append(lang)

    # 2. Capture the total unique counts before filtering
    total_unique_extensions = len(extension_map)
    total_unique_exact_matches = len(exact_match_map)

    # 3. Filter down to ONLY the collisions (items claimed by > 1 language)
    extension_collisions = {
        ext: list(set(langs)) 
        for ext, langs in extension_map.items() 
        if len(set(langs)) > 1
    }
    
    exact_match_collisions = {
        exact: list(set(langs)) 
        for exact, langs in exact_match_map.items() 
        if len(set(langs)) > 1
    }

    # Sort the results by the number of colliding languages (highest first)
    extension_collisions = dict(sorted(extension_collisions.items(), key=lambda item: len(item[1]), reverse=True))
    exact_match_collisions = dict(sorted(exact_match_collisions.items(), key=lambda item: len(item[1]), reverse=True))

    return extension_collisions, exact_match_collisions, total_unique_extensions, total_unique_exact_matches


def print_collision_report(ext_cols, exact_cols, total_exts, total_exact):
    """Prints a highly readable terminal report of the collisions and total coverage."""
    print("=" * 60)
    print(" 🚨 GITGALAXY REGISTRY STATS & COLLISION MATRIX 🚨")
    print("=" * 60)
    
    # NEW: Display total coverage
    print(f"\n[+] REGISTRY COVERAGE:")
    print(f"    Total Unique Extensions Mapped:   {total_exts}")
    print(f"    Total Unique Exact Matches Mapped: {total_exact}")
    print("-" * 60)

    print(f"\n[+] EXTENSION COLLISIONS ({len(ext_cols)} found):")
    for ext, langs in ext_cols.items():
        print(f"    {ext.ljust(15)} -> {', '.join(langs)}")

    print(f"\n[+] EXACT MATCH COLLISIONS ({len(exact_cols)} found):")
    for exact, langs in exact_cols.items():
        print(f"    {exact.ljust(15)} -> {', '.join(langs)}")
    print("\n" + "=" * 60)


# ==========================================
# Example Usage
# ==========================================
if __name__ == "__main__":
    print("Scanning GitGalaxy Phase 0 Registry for collisions...")
    
    # 1. Run the scan and unpack all 4 returned variables
    ext_collisions, exact_collisions, total_exts, total_exact = scan_for_collisions(LANGUAGE_DEFINITIONS)
    
    # 2. Print the report to your terminal, including the new totals
    print_collision_report(ext_collisions, exact_collisions, total_exts, total_exact)
    
    # 3. Automatically dump it to a JSON file for your engine to ingest
    with open('collision_matrix.json', 'w') as f:
        json.dump({'extensions': ext_collisions, 'exact_matches': exact_collisions}, f, indent=4)
        
    print("[+] Saved complete collision data to collision_matrix.json")