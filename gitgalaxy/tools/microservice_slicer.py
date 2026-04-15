#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: The Microservice Slicer (v2)
# Purpose: Recursive taint-tracking and business rule extraction for legacy COBOL.
# ==============================================================================
import argparse
import sys
import re
from pathlib import Path

def slice_business_logic(filepath: Path, initial_var: str):
    """Recursively tracks a variable and its aliases through the AST."""
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore').upper()
    except Exception:
        return None

    if "PROCEDURE DIVISION" not in content:
        return None

    proc_div = content.split("PROCEDURE DIVISION")[1]
    lines = proc_div.split('\n')
    
    tainted_vars = {initial_var}
    
    # PASS 1: Recursive Taint Mapping (The Alias Engine)
    # We loop 3 times to catch chained aliases (e.g., A -> B -> C)
    for _ in range(3):
        for line in lines:
            clean_line = line.strip()
            if not clean_line or clean_line.startswith('*'): 
                continue
            
            # Match assignments: MOVE A TO B, ADD A TO B, SUBTRACT A FROM B
            match = re.search(r'(?:MOVE|ADD|SUBTRACT)\s+([A-Z0-9\-]+)\s+(?:TO|FROM)\s+([A-Z0-9\-]+)', clean_line)
            if match:
                var1, var2 = match.group(1), match.group(2)
                # If either variable is tainted, taint the other
                if var1 in tainted_vars or var2 in tainted_vars:
                    tainted_vars.add(var1)
                    tainted_vars.add(var2)
                    
            # Match math formulas: COMPUTE X = Y * Z
            comp_match = re.search(r'COMPUTE\s+([A-Z0-9\-]+)\s*=', clean_line)
            if comp_match:
                var1 = comp_match.group(1)
                if var1 in tainted_vars:
                    # Taint every variable inside the math equation
                    vars_in_eq = re.findall(r'([A-Z][A-Z0-9\-]+)', clean_line.split('=')[1])
                    tainted_vars.update(vars_in_eq)

    # PASS 2: Extraction
    para_pattern = re.compile(r'^[ \t]{0,7}([A-Z0-9\-]+)\.[ \t]*$', re.MULTILINE)
    extracted_logic = []
    current_paragraph = "MAIN-ENTRY"
    
    for i, line in enumerate(lines):
        clean_line = line.strip()
        if not clean_line or clean_line.startswith('*'): 
            continue
        
        para_match = para_pattern.match(line)
        if para_match:
            current_paragraph = para_match.group(1)
            continue
            
        # TAINT CHECK: If ANY tainted variable is on this line, extract it
        if any(var in clean_line for var in tainted_vars):
            extracted_logic.append({
                "line_num": i + 1,
                "paragraph": current_paragraph,
                "statement": clean_line
            })
            
    return extracted_logic, tainted_vars

def main():
    parser = argparse.ArgumentParser(description="GitGalaxy Microservice Slicer v2")
    parser.add_argument("target", help="Path to a .cbl file to slice")
    parser.add_argument("--var", required=True, help="The target variable to track")
    args = parser.parse_args()

    target_path = Path(args.target).resolve()
    if not target_path.exists():
        print(f"Error: Target {target_path} does not exist.")
        sys.exit(1)

    print(f"🔪 GitGalaxy Slicer hunting aliases for [{args.var.upper()}] in {target_path.name}...\n")

    result = slice_business_logic(target_path, args.var.upper())
    
    if not result:
        print(f"⚠️ Variable {args.var.upper()} is never mutated in the PROCEDURE DIVISION.")
        sys.exit(0)

    logic_slice, aliases = result

    print("==========================================================")
    print(f" 🧬 TAINTS FOUND: {', '.join(aliases)}")
    print("==========================================================")
    
    current_p = ""
    for item in logic_slice:
        if item['paragraph'] != current_p:
            print(f"\n[{item['paragraph']}]")
            current_p = item['paragraph']
        
        print(f"  Line {item['line_num']:04d} | {item['statement']}")
        
    print("\n==========================================================")
    print(f" 🎯 Sliced {len(logic_slice)} distinct business rules.")
    print("==========================================================\n")

if __name__ == "__main__":
    main()