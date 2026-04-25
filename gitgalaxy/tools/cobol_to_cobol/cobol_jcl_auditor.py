#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: Zero-Trust Meta Auditor (v5 - CLI Enabled)
# Purpose: Compares forged JCLs against original IBM legacy JCLs to calculate
#          exact code bloat reduction and over-permissioned I/O shedding.
# ==============================================================================
import argparse
import json
import re
import sys
from pathlib import Path

SYSTEM_DDS = {"STEPLIB", "SYSOUT", "SYSPRINT", "SYSUDUMP", "SYSIN", "CEEDUMP", "DFHCSD", "IGZDDOP"}
SYSTEM_PGMS = {"IEFBR14", "IEWL", "ASMA90", "IGYCRCTL", "IGYWC", "HEWL", "IDCAMS", "IEBGENER"}

def parse_jcl_intent(filepath: Path) -> dict:
    """Parses a JCL file to extract its raw execution intent."""
    metrics = {"lines_of_code": 0, "exec_pgms": set(), "data_definitions": set()}
    pgm_pattern = re.compile(r'EXEC\s+(?:PGM=)?([A-Z0-9@#$\-]+)', re.IGNORECASE)
    dd_pattern = re.compile(r'^//([A-Z0-9@#$\-]+)\s+DD\s+', re.IGNORECASE)

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('//*'):
                    continue
                metrics["lines_of_code"] += 1
                
                pgm_match = pgm_pattern.search(line)
                if pgm_match:
                    pgm = pgm_match.group(1).upper()
                    if pgm not in SYSTEM_PGMS:
                        metrics["exec_pgms"].add(pgm)
                    
                dd_match = dd_pattern.search(line)
                if dd_match:
                    dd_name = dd_match.group(1).upper()
                    if dd_name not in SYSTEM_DDS:
                        metrics["data_definitions"].add(dd_name)
    except Exception: pass
    return metrics

def audit_zero_trust_jcls(forged_dir: Path, original_dir: Path) -> dict:
    """Core logic to fetch bloat metrics."""
    legacy_jcls = list(original_dir.rglob("*.[jJ][cC][lL]")) + list(original_dir.rglob("*.txt"))
    legacy_map = {}
    
    # 1. Map Legacy JCLs by Intent (Handling multi-step monoliths)
    for lj in legacy_jcls:
        if forged_dir in lj.parents: continue
        metrics = parse_jcl_intent(lj)
        for pgm in metrics["exec_pgms"]:
            # If multiple legacy JCLs call the same program, keep the biggest one
            if pgm not in legacy_map or metrics.get("lines_of_code", 0) > legacy_map[pgm].get("lines_of_code", 0):
                legacy_map[pgm] = {"file": lj, "metrics": metrics}

    # 2. Compare against Forged JCLs
    forged_files = list(forged_dir.glob("*.jcl"))
    report = {
        "audited": 0, 
        "original_loc": 0, 
        "forged_loc": 0, 
        "excess_dds_blocked": 0,
        "program_breakdown": {}
    }

    for forged_file in forged_files:
        forged_metrics = parse_jcl_intent(forged_file)
        if not forged_metrics["exec_pgms"]: continue
            
        pgm_name = list(forged_metrics["exec_pgms"])[0]

        if pgm_name in legacy_map:
            twin_metrics = legacy_map[pgm_name]["metrics"]
            
            loc_saved = max(0, twin_metrics["lines_of_code"] - forged_metrics["lines_of_code"])
            excess_dds = max(0, len(twin_metrics["data_definitions"] - forged_metrics["data_definitions"]))
            
            report["audited"] += 1
            report["original_loc"] += twin_metrics["lines_of_code"]
            report["forged_loc"] += forged_metrics["lines_of_code"]
            report["excess_dds_blocked"] += excess_dds
            
            report["program_breakdown"][pgm_name] = {
                "loc_saved": loc_saved,
                "io_blocked": excess_dds,
                "legacy_file": legacy_map[pgm_name]["file"].name
            }

    if report["original_loc"] > 0:
        report["bloat_reduction_pct"] = round(((report["original_loc"] - report["forged_loc"]) / report["original_loc"]) * 100, 1)
    else:
        report["bloat_reduction_pct"] = 0.0

    return report

def main():
    parser = argparse.ArgumentParser(description="GitGalaxy Zero-Trust Meta Auditor (v5)")
    parser.add_argument("forged", help="Directory containing the forged GitGalaxy JCLs")
    parser.add_argument("legacy", help="Directory containing the original legacy IBM JCLs")
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of a formatted terminal report")
    
    args = parser.parse_args()
    forged_path = Path(args.forged).resolve()
    legacy_path = Path(args.legacy).resolve()

    if not forged_path.exists() or not legacy_path.exists():
        print("\n[!] ERROR: One or both directories do not exist.")
        sys.exit(1)

    # Run the audit
    report = audit_zero_trust_jcls(forged_path, legacy_path)

    # Output routing
    if args.json:
        print(json.dumps(report, indent=2))
        sys.exit(0)

    # CLI Terminal Vibe
    print("\n==============================================================")
    print(" 🛡️  GitGalaxy Spoke: Zero-Trust Meta Auditor (v5)")
    print("==============================================================")
    print(f" [*] Forged Dir  : {forged_path.name}")
    print(f" [*] Legacy Root : {legacy_path.name}")
    print("--------------------------------------------------------------")
    
    if report["audited"] == 0:
        print(" [!] No matching execution intents found between the directories.")
        print("     Ensure your forged JCLs share PROGRAM-IDs with the legacy corpus.")
    else:
        print(" PROGRAM BREAKDOWN:")
        for pgm, data in report["program_breakdown"].items():
            loc = str(data['loc_saved']).rjust(4)
            io = str(data['io_blocked']).rjust(2)
            print(f"  [+] {pgm.ljust(10)} | LOC Saved: {loc} | I/O Blocked: {io} | Ref: {data['legacy_file']}")

        print("--------------------------------------------------------------")
        print(" 📊 FINAL AUDIT METRICS:")
        print(f"  > Programs Audited       : {report['audited']}")
        print(f"  > Original Legacy LOC    : {report['original_loc']}")
        print(f"  > GitGalaxy Forged LOC   : {report['forged_loc']}")
        print(f"  > Bloat Reduction        : {report['bloat_reduction_pct']}%")
        print(f"  > Over-Permissioned I/O  : {report['excess_dds_blocked']} Boundaries Shed")

    print("==============================================================\n")

if __name__ == "__main__":
    main()