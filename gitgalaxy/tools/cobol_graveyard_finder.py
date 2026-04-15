#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: The Graveyard Reaper
# Purpose: Static Analysis of COBOL AST to isolate orphaned data and dead code.
# ==============================================================================
import argparse
import sys
import re
from pathlib import Path

def x_ray_dead_code(filepath: Path) -> dict:
    """Parses a COBOL file to find variables and paragraphs that are mathematically unreachable."""
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore').upper()
    except Exception:
        return None

    # COBOL is strictly divided. We need to split the data from the execution.
    if "PROCEDURE DIVISION" not in content:
        return None

    parts = content.split("PROCEDURE DIVISION", 1)
    data_div = parts[0]
    proc_div = parts[1]

    # ==========================================
    # 1. HUNTING ORPHANED DATA
    # ==========================================
    # Look for COBOL variable declarations (Levels 01-49, 77, 88)
    # Example: 05 WS-CUSTOMER-NAME PIC X(50).
    var_pattern = re.compile(r'^[ \t]*(?:0[1-9]|[1-4][0-9]|77|88)[ \t]+([A-Z0-9\-]+)', re.MULTILINE)
    declared_vars = set(var_pattern.findall(data_div))

    used_vars = set()
    for var in declared_vars:
        # A variable is "used" if it appears as a whole word anywhere in the Procedure Division
        if re.search(r'\b' + re.escape(var) + r'\b', proc_div):
            used_vars.add(var)

    orphaned_vars = declared_vars - used_vars

    # ==========================================
    # 2. HUNTING PHANTOM PARAGRAPHS (Dead Code)
    # ==========================================
    # Paragraphs usually start near the beginning of the line and end with a period.
    para_pattern = re.compile(r'^[ \t]{0,11}([A-Z0-9\-]+)\.[ \t]*$', re.MULTILINE)
    paragraphs = para_pattern.findall(proc_div)

    # Find every explicitly called target in the code
    call_pattern = re.compile(r'\b(?:PERFORM|GO\s+TO)\s+([A-Z0-9\-]+)\b')
    called_targets = set(call_pattern.findall(proc_div))

    dead_paragraphs = set()
    if paragraphs:
        # The first paragraph is the Main Entry Point. It is always reached by default.
        entry_point = paragraphs[0]
        reached_paragraphs = {entry_point}.union(called_targets)
        declared_paragraphs = set(paragraphs)

        # The Math: Dead code is anything declared but never explicitly reached
        dead_paragraphs = declared_paragraphs - reached_paragraphs

    # Ignore system paragraphs and generic loop ends (like *-EXIT)
    dead_paragraphs = {p for p in dead_paragraphs if not p.endswith('-EXIT')}

    # Calculate a rough estimate of Lines of Code (LOC) saved
    # (Assuming average 10 lines per paragraph and 1 line per variable)
    loc_saved = (len(dead_paragraphs) * 10) + len(orphaned_vars)

    return {
        "program_id": filepath.name,
        "total_vars": len(declared_vars),
        "orphaned_vars": orphaned_vars,
        "total_paras": len(paragraphs) if paragraphs else 0,
        "dead_paras": dead_paragraphs,
        "loc_saved": loc_saved
    }

def main():
    parser = argparse.ArgumentParser(description="GitGalaxy Graveyard Reaper")
    parser.add_argument("target", help="Directory containing legacy COBOL payloads")
    args = parser.parse_args()

    target_path = Path(args.target).resolve()
    if not target_path.exists():
        print(f"Error: Target {target_path} does not exist.")
        sys.exit(1)

    print(f"🪦 GitGalaxy Reaper scanning {target_path.name} for dead code...\n")

    cobol_files = list(target_path.rglob("*.cbl")) + list(target_path.rglob("*.cob"))
    
    totals = {"loc_saved": 0, "orphaned_vars": 0, "dead_paras": 0, "files_with_dead_code": 0}

    for file_path in cobol_files:
        metrics = x_ray_dead_code(file_path)
        if metrics and (metrics['orphaned_vars'] or metrics['dead_paras']):
            totals["files_with_dead_code"] += 1
            totals["loc_saved"] += metrics['loc_saved']
            totals["orphaned_vars"] += len(metrics['orphaned_vars'])
            totals["dead_paras"] += len(metrics['dead_paras'])

            print(f" 🎯 TARGET: {metrics['program_id']}")
            if metrics['orphaned_vars']:
                print(f"    ↳ Orphaned Variables ({len(metrics['orphaned_vars'])}): {', '.join(list(metrics['orphaned_vars'])[:5])}" + ("..." if len(metrics['orphaned_vars']) > 5 else ""))
            if metrics['dead_paras']:
                print(f"    ↳ Phantom Paragraphs ({len(metrics['dead_paras'])}): {', '.join(list(metrics['dead_paras'])[:5])}" + ("..." if len(metrics['dead_paras']) > 5 else ""))
            print("-" * 60)

    # Presentation
    print("\n==========================================================")
    print(" 📉 DEAD CODE ELIMINATION REPORT")
    print("==========================================================")
    print(f" Files Flagged for Cleanup : {totals['files_with_dead_code']}")
    print(f" Unused Memory Addresses   : {totals['orphaned_vars']} orphaned variables")
    print(f" Unreachable Logic Blocks  : {totals['dead_paras']} phantom paragraphs")
    print(f" ✂️ Estimated Bloat Removed : ~{totals['loc_saved']} Lines of Code")
    print("==========================================================\n")

if __name__ == "__main__":
    main()