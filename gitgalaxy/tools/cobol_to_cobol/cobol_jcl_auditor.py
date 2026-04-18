#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: Zero-Trust Meta Auditor (v4 - API Module)
# Purpose: Compares forged JCLs against original IBM legacy JCLs to calculate
#          exact code bloat reduction and over-permissioned I/O shedding.
# ==============================================================================
import re
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
    """API endpoint for the Refractor Controller to fetch bloat metrics."""
    legacy_jcls = list(original_dir.rglob("*.[jJ][cC][lL]")) + list(original_dir.rglob("*.txt"))
    legacy_map = {}
    
    # 1. Map Legacy JCLs by Intent (Handling multi-step monoliths)
    for lj in legacy_jcls:
        if forged_dir in lj.parents: continue
        metrics = parse_jcl_intent(lj)
        for pgm in metrics["exec_pgms"]:
            # If multiple legacy JCLs call the same program, keep the biggest one (worst offender)
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