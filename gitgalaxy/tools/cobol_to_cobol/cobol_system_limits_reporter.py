#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: System Limit Reporter (The Honesty Protocol)
# Purpose: Static Analysis sensor to detect structural anomalies, dynamic routing,
#          and legacy "dragons" that compromise deterministic mathematical mapping.
# ==============================================================================
import argparse
import sys
import re
from pathlib import Path

# Define the "Ancient Dragons" (Structural limiters)
SYSTEM_LIMIT_RULES = {
    "ALTER_STATEMENT": {
        "regex": re.compile(
            r"\bALTER\s+[A-Z0-9\-]+\s+TO\s+(?:PROCEED\s+TO\s+)?[A-Z0-9\-]+\b",
            re.IGNORECASE,
        ),
        "severity": "CRITICAL",
        "description": "Control flow mathematically compromised. The target of a GO TO is being dynamically rewritten.",
    },
    "COPY_REPLACING": {
        "regex": re.compile(r'\bCOPY\s+[\'"]?[A-Z0-9\-]+[\'"]?\s+REPLACING\b', re.IGNORECASE),
        "severity": "HIGH",
        "description": "Macro substitution detected. AST math may drift from actual compiled execution.",
    },
    "CICS_ASYNC_JUMP": {
        "regex": re.compile(r"EXEC\s+CICS\s+HANDLE\s+CONDITION", re.IGNORECASE),
        "severity": "CRITICAL",
        "description": "Asynchronous error routing detected. Execution flow can jump outside the static DAG.",
    },
}


def scan_system_limits(filepath: Path) -> list:
    """
    Scans a COBOL file for structural anomalies that break deterministic mapping.
    Returns a list of formatted warning strings.
    """
    anomalies = []
    try:
        # Open file with error handling for legacy encodings
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except Exception as e:
        return [f"[{filepath.name}] ERROR: Failed to read file - {e}"]

    for line_num, line in enumerate(lines, start=1):
        # Skip standard COBOL comments (asterisk in column 7)
        if len(line) > 6 and line[6] == "*":
            continue

        clean_line = line.strip()
        if not clean_line:
            continue

        for rule_name, rule_data in SYSTEM_LIMIT_RULES.items():
            if rule_data["regex"].search(clean_line):
                # Format: [FILE : Line XXXX] SEVERITY LIMIT - Description
                warning = f"[{filepath.name} : Line {line_num:04d}] {rule_data['severity']} LIMIT - {rule_data['description']}"
                anomalies.append(warning)

    return anomalies


def main():
    from gitgalaxy.licensing import enforce_licensing_guard

    enforce_licensing_guard("System Limit Reporter (The Legacy Forge)")

    parser = argparse.ArgumentParser(description="GitGalaxy System Limit Reporter (Honesty Protocol)")
    parser.add_argument("target", help="Path to a .cbl file OR a directory to scan")
    args = parser.parse_args()

    target_path = Path(args.target).resolve()
    if not target_path.exists():
        print(f"Error: Target {target_path} does not exist.")
        sys.exit(1)

    cobol_files = []
    if target_path.is_file():
        cobol_files.append(target_path)
    elif target_path.is_dir():
        print(f"📠 Scanning directory for System Limits: {target_path.name}...")
        cobol_files.extend(target_path.rglob("*.cbl"))
        cobol_files.extend(target_path.rglob("*.cob"))

    if not cobol_files:
        print("⚠️ No .cbl or .cob files found in the target location.")
        sys.exit(0)

    print(f"\n🔎 GitGalaxy Honesty Protocol scanning {len(cobol_files)} files for structural dragons...\n")
    print("=" * 90)

    total_anomalies = 0

    for file_path in cobol_files:
        anomalies = scan_system_limits(file_path)
        if anomalies:
            for anomaly in anomalies:
                print(f" ⚠️ {anomaly}")
                total_anomalies += 1

    print("=" * 90)
    if total_anomalies == 0:
        print(" ✅ No structural limits detected. DAG is 100% mathematically deterministic.")
    else:
        print(f" 🚨 WARNING: Found {total_anomalies} structural anomalies requiring human architectural review.")
    print("==========================================================================================\n")


if __name__ == "__main__":
    main()
