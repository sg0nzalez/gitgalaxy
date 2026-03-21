import json
from pathlib import Path
from collections import defaultdict

def audit_function_extraction(base_directory):
    """
    Scans for *_galaxy_audit.json files and aggregates function extraction
    success rates by programming language.
    """
    # Dictionary to hold the stats: { "Language": {"with": 0, "without": 0} }
    stats = defaultdict(lambda: {"with_functions": 0, "without_functions": 0})
    
    # Define the path and search pattern
    search_path = Path(base_directory)
    file_pattern = '*_galaxy_audit.json'
    
    # Find all matching JSON files recursively
    audit_files = list(search_path.rglob(file_pattern))
    print(f"Found {len(audit_files)} audit files. Beginning scan...\n")
    
    for file_path in audit_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Navigate to the Visible Star Manifest
            manifest = data.get("5. Visible Star Manifest", {})
            
            for filename, file_metrics in manifest.items():
                # Safely extract the language
                identity = file_metrics.get("1. Identity", {})
                language = identity.get("Language", "Unknown")
                
                # Check for satellites (functions)
                satellites = file_metrics.get("5. Function Analysis (Satellites)", [])
                
                if len(satellites) > 0:
                    stats[language]["with_functions"] += 1
                else:
                    stats[language]["without_functions"] += 1
                    
        except json.JSONDecodeError:
            print(f"Warning: Could not decode JSON in file {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    # Print the final diagnostic report
    print("=" * 50)
    print(" SATELLITE EXTRACTION REPORT BY LANGUAGE")
    print("=" * 50)
    
    if not stats:
        print("No language data could be aggregated.")
        return

    # Sort alphabetically by language for readability
    for lang, counts in sorted(stats.items()):
        total_files = counts["with_functions"] + counts["without_functions"]
        success_rate = (counts["with_functions"] / total_files) * 100 if total_files > 0 else 0
        
        print(f"Language: **{lang}**")
        print(f"  Total Files Analyzed : {total_files}")
        print(f"  Files WITH Functions : {counts['with_functions']} ({success_rate:.1f}%)")
        print(f"  Files WITHOUT        : {counts['without_functions']}")
        print("-" * 50)

if __name__ == "__main__":
    target_directory = "/srv/storage_16tb/projects/gitgalaxy/data"
    audit_function_extraction(target_directory)