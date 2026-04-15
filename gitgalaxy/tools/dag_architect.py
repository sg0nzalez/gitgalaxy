#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: Data Lineage DAG Architect
# Purpose: Parses COBOL structural intent to map INPUT/OUTPUT data flows
#          and calculates the mathematically perfect topological execution order.
# ==============================================================================
import argparse
import sys
import re
from pathlib import Path
from collections import defaultdict, deque

def extract_lineage(filepath: Path) -> dict:
    """X-Rays a COBOL program to map its internal variables to external physical files."""
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore').upper()
    except Exception:
        return None

    # 1. Extract the permanent PROGRAM-ID
    prog_match = re.search(r'PROGRAM-ID\.\s+([A-Z0-9@#$]+)', content)
    if not prog_match:
        return None
    program_id = prog_match.group(1)

    # 2. Map internal file variables to physical external boundaries (DD Names)
    # E.g., SELECT RPT-FILE ASSIGN TO REPORTS
    file_map = {}
    for match in re.finditer(r'SELECT\s+([A-Z0-9-]+)\s+ASSIGN\s+(?:TO\s+)?([A-Z0-9@#$]+)', content):
        file_map[match.group(1)] = match.group(2)

    inputs = set()
    outputs = set()

    # 3. Extract exact Functional Intent (OPEN INPUT vs OPEN OUTPUT)
    for match in re.finditer(r'OPEN\s+(INPUT|OUTPUT|I-O|EXTEND)\s+([^.]+)\.', content):
        mode = match.group(1)
        # Handle multiple files opened on the same line (e.g., OPEN INPUT FILE-A FILE-B.)
        files_raw = re.sub(r'\s+', ' ', match.group(2)).replace(',', ' ').split()
        
        for internal_file in files_raw:
            if internal_file in file_map:
                physical_file = file_map[internal_file]
                if mode in ('INPUT', 'I-O', 'EXTEND'):
                    inputs.add(physical_file)
                if mode in ('OUTPUT', 'I-O', 'EXTEND'):
                    outputs.add(physical_file)

    return {
        "program_id": program_id,
        "inputs": inputs,
        "outputs": outputs
    }

def main():
    parser = argparse.ArgumentParser(description="GitGalaxy DAG Architect")
    parser.add_argument("target", help="Directory containing legacy COBOL payloads")
    args = parser.parse_args()

    target_path = Path(args.target).resolve()
    if not target_path.exists():
        print(f"Error: Target {target_path} does not exist.")
        sys.exit(1)

    print(f"🕸️ GitGalaxy DAG Architect mapping data lineage in: {target_path.name}...\n")

    cobol_files = list(target_path.rglob("*.cbl")) + list(target_path.rglob("*.cob"))
    
    programs = []
    for f in cobol_files:
        lineage = extract_lineage(f)
        if lineage and (lineage['inputs'] or lineage['outputs']):
            programs.append(lineage)

    # Map which programs create which physical files
    file_creators = defaultdict(set)
    for p in programs:
        for out_file in p['outputs']:
            file_creators[out_file].add(p['program_id'])

    # Build the Dependency Graph
    dependencies = defaultdict(set)
    dependents = defaultdict(set)
    in_degree = {p['program_id']: 0 for p in programs}

    for p in programs:
        pid = p['program_id']
        for in_file in p['inputs']:
            # If a file this program needs is created by another program in this cluster...
            if in_file in file_creators:
                for creator in file_creators[in_file]:
                    if creator != pid:  # Program doesn't depend on itself
                        dependencies[pid].add(creator)
                        dependents[creator].add(pid)

    # Calculate in-degrees (how many programs must run before this one)
    for pid in dependencies:
        in_degree[pid] = len(dependencies[pid])

    # --- Kahn's Algorithm for Topological Sort ---
    # Start with programs that have 0 dependencies (The Origin Nodes)
    queue = deque([pid for pid, deg in in_degree.items() if deg == 0])
    execution_order = []

    while queue:
        current = queue.popleft()
        execution_order.append(current)

        for dependent in dependents[current]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    # --- Presentation ---
    print("==========================================================")
    print(" ⚡ ZERO-TRUST EXECUTION PIPELINE (TOPOLOGICAL SORT)")
    print("==========================================================\n")
    
    if len(execution_order) != len(programs):
        print(" ⚠️ WARNING: Cyclic Dependency Detected! Pipeline locked.")
        sys.exit(1)

    for step, pid in enumerate(execution_order, 1):
        # Find the original data
        prog_data = next((p for p in programs if p['program_id'] == pid), None)
        in_files = ", ".join(prog_data['inputs']) if prog_data['inputs'] else "None"
        out_files = ", ".join(prog_data['outputs']) if prog_data['outputs'] else "None"
        
        print(f" STEP {step:02d}: Run [{pid}]")
        print(f"          ↳ Reads : {in_files}")
        print(f"          ↳ Writes: {out_files}")
        print("-" * 58)

if __name__ == "__main__":
    main()