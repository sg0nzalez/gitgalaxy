#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Tool: Binary Anomaly Detector
# Purpose: Fast triage of binary anomalies, magic byte mismatches, and obfuscated payloads.
# ==============================================================================
import argparse
import sys
import os
import time
import fnmatch
from pathlib import Path

# Import exclusively from the GitGalaxy Hub
from gitgalaxy.core.aperture import ApertureFilter
from gitgalaxy.security.security_lens import SecurityLens
from gitgalaxy.standards.language_standards import LANGUAGE_DEFINITIONS

# Safely import the config, falling back if the user hasn't added exceptions yet
try:
    from gitgalaxy.standards.gitgalaxy_config import (
        APERTURE_CONFIG,
        ALLOWLIST_PATHS,
        DENYLIST_PATTERNS,
        XRAY_BYPASS_EXTENSIONS,
        XRAY_BYPASS_PATHS,
    )
except ImportError:
    from gitgalaxy.standards.gitgalaxy_config import APERTURE_CONFIG

    ALLOWLIST_PATHS = []
    DENYLIST_PATTERNS = []
    XRAY_BYPASS_EXTENSIONS = []
    XRAY_BYPASS_PATHS = []


def main():
    from gitgalaxy.licensing import enforce_licensing_guard

    enforce_licensing_guard("Binary Anomaly Detector")

    parser = argparse.ArgumentParser(description="Binary Anomaly Detector: Entropy & Magic Byte Scanner")
    parser.add_argument("target", help="Directory to scan")
    args = parser.parse_args()

    target_path = Path(args.target).resolve()
    if not target_path.exists():
        print(f"Error: Target {target_path} does not exist.")
        sys.exit(1)

    print(f"🔍 Initializing Binary Anomaly Detector on {target_path.name}...")

    # Initialize lightweight filters
    filter_engine = ApertureFilter(target_path, LANGUAGE_DEFINITIONS, APERTURE_CONFIG)
    security = SecurityLens()

    # DEFENSIVE DESIGN (SENSOR OPTIMIZATION): Restrict the Security Lens to entropy and bitwise operations to minimize CPU overhead during binary evaluation.
    security.THREAT_SIGNATURES = {
        "heat_triggers": security.THREAT_SIGNATURES["heat_triggers"],
        "bitwise_hits": security.THREAT_SIGNATURES["bitwise_hits"],
    }

    anomalies_found = 0
    anomalies_allowed = 0
    forbidden_blocked = 0
    files_evaluated = 0

    files_to_deep_scan = []

    # ==============================================================================
    # PHASE 1: Path Filtering and Queue Generation
    # ==============================================================================
    for root, dirs, files in os.walk(target_path):
        rel_root = str(Path(root).relative_to(target_path))

        # Root Traversal Optimization: Evaluate top-level directories against ignore rules.
        if rel_root == ".":
            dirs[:] = [d for d in dirs if filter_engine._check_ignore_rules(d)]
        elif not filter_engine._check_ignore_rules(rel_root):
            dirs[:] = []
            continue

        for file in files:
            files_evaluated += 1
            file_path = Path(root) / file
            ext = file_path.suffix.lower()

            # Create a normalized string for checking against lists
            rel_path_str = str(file_path.relative_to(target_path)).replace("\\", "/")

            # Evaluate Global vs. Tool-Specific Bypasses
            is_global_allow = any(approved in rel_path_str for approved in ALLOWLIST_PATHS)
            is_xray_bypass = ext in XRAY_BYPASS_EXTENSIONS or any(b in rel_path_str for b in XRAY_BYPASS_PATHS)

            is_whitelisted = is_global_allow or is_xray_bypass

            # FALSE POSITIVE MITIGATION: Test directories frequently generate high-entropy mock data (e.g., cryptographic keys). Bypass deep scanning for these paths.
            if (
                "/test/" in rel_path_str.lower()
                or "/tests/" in rel_path_str.lower()
                or "phpunit" in rel_path_str.lower()
            ):
                is_whitelisted = True

            # 1. DENYLIST ENFORCEMENT
            is_forbidden = any(fnmatch.fnmatch(file, pattern) for pattern in DENYLIST_PATTERNS)
            if is_forbidden and not is_whitelisted:
                print(f"[DENYLIST MATCH] Unauthorized file pattern detected: {rel_path_str}")
                forbidden_blocked += 1
                anomalies_found += 1
                continue

            # NOTE: We intentionally DO NOT call evaluate_path_integrity here!
            # X-Ray needs to scan binaries (.png, .zip), which the other tools drop.
            files_to_deep_scan.append((file_path, rel_path_str, ext, is_whitelisted))

    # ==============================================================================
    # PHASE 2: Deep Content and Binary Header Inspection
    # ==============================================================================
    print(f"\n🔎 Scanning {len(files_to_deep_scan):,} files for structural anomalies:")
    print("   - Magic Byte Mismatches (e.g., hidden executables disguised as images)")
    print("   - Embedded Execution Headers (e.g., executable signatures within static data)")
    print("   - High-Entropy Payloads (e.g., packed executables or obfuscated bitwise loops)")

    start_time = time.time()

    for file_path, rel_path_str, ext, is_whitelisted in files_to_deep_scan:
        try:
            # Read the first 8KB of the file as raw bytes
            with open(file_path, "rb") as f:
                head_bytes = f.read(8192)

            has_anomaly = False
            anomaly_msgs = []

            # 1. Binary X-Ray (Magic Bytes & Headers)
            binary_threats = security.scan_binary(head_bytes, ext)

            # EXPECTED HEADER EXCEPTION
            if binary_threats:
                threat_msg = binary_threats.get("threat_snippet", "")
                if ext in [".sh", ".bash", ".zsh", ".command"] and "#!/bin/" in threat_msg:
                    binary_threats = {}  # Clear the threat, it is expected

            if binary_threats:
                has_anomaly = True
                anomaly_msgs.append(binary_threats.get("threat_snippet", "Unknown Binary Threat"))

            # 2. String Entropy X-Ray (Encrypted/Packed Payloads)
            content = head_bytes.decode("utf-8", errors="ignore")
            sec_results = security.scan_content(content, 100)

            if sec_results["counts"].get("entropy", 0) > 0:
                has_anomaly = True
                anomaly_msgs.append("Mathematically dense/encrypted strings detected (Shannon Entropy > 4.8)")

            if sec_results["counts"].get("bitwise_hits", 0) > 0:
                has_anomaly = True
                anomaly_msgs.append("Obfuscated bitwise operations (XOR loops) detected")

            # 3. Report the Anomaly
            if has_anomaly:
                if is_whitelisted:
                    anomalies_allowed += 1
                else:
                    print(f"[ANOMALY DETECTED] {rel_path_str}")
                    for msg in anomaly_msgs:
                        print(f"   -> {msg}")
                    anomalies_found += 1

        except Exception:
            pass

    end_time = time.time()
    time_delta = end_time - start_time
    scan_rate = len(files_to_deep_scan) / time_delta if time_delta > 0 else 0

    # ==============================================================================
    # SCAN SUMMARY
    # ==============================================================================
    print("\n" + "=" * 75)
    print(" BINARY ANOMALY DETECTOR: SCAN SUMMARY")
    print("=" * 75)
    print(f" Files Evaluated    : {files_evaluated:,}")
    print(f" Files Deep Scanned : {len(files_to_deep_scan):,}")
    print(f" Time Elapsed       : {time_delta:.2f} seconds")
    print(f" Scan Velocity      : {scan_rate:,.0f} files/sec")
    print("-" * 75)
    print(f" Anomalies Detected : {anomalies_found:,}")
    print(f" File Denylist Blocks : {forbidden_blocked:,}")
    print(f" File Allowlist Bypasses: {anomalies_allowed:,}")
    print("-" * 75)

    if anomalies_found > 0:
        print(f" [BLOCKING ACTION] {anomalies_found} structural anomalies detected. Failing pipeline.")
        print(" TIP: Entropy-based detection naturally flags compressed or dense data.")
        print("         - If safe extension (e.g., .gz, .json): Add to XRAY_BYPASS_EXTENSIONS")
        print("         - If safe specific file: Add to XRAY_BYPASS_PATHS")
        print("         - Edit these inside: gitgalaxy/standards/gitgalaxy_config.py")
        sys.exit(1)
    else:
        print(" [SUCCESS] No obfuscated payloads or binary anomalies detected.")
        if anomalies_allowed > 0:
            print(f" NOTE: {anomalies_allowed} known mock/safe files were bypassed via configuration.")
    print("=" * 75 + "\n")


def run_xray_audit(target_path: Path) -> dict:
    """Programmatic entry point for GalaxyScope."""
    filter_engine = ApertureFilter(target_path, LANGUAGE_DEFINITIONS, APERTURE_CONFIG)
    security = SecurityLens()
    security.THREAT_SIGNATURES = {
        "heat_triggers": security.THREAT_SIGNATURES["heat_triggers"],
        "bitwise_hits": security.THREAT_SIGNATURES["bitwise_hits"],
    }

    anomalies_found = 0
    # Minimal silent scan
    for root, dirs, files in os.walk(target_path):
        rel_root = str(Path(root).relative_to(target_path))
        if rel_root == ".":
            dirs[:] = [d for d in dirs if filter_engine._check_ignore_rules(d)]
        elif not filter_engine._check_ignore_rules(rel_root):
            dirs[:] = []
            continue

        for file in files:
            file_path = Path(root) / file
            rel_path_str = str(file_path.relative_to(target_path)).replace("\\", "/")
            is_whitelisted = (
                any(a in rel_path_str for a in ALLOWLIST_PATHS)
                or file_path.suffix.lower() in XRAY_BYPASS_EXTENSIONS
                or any(b in rel_path_str for b in XRAY_BYPASS_PATHS)
            )
            if "/test/" in rel_path_str.lower() or "/tests/" in rel_path_str.lower():
                is_whitelisted = True

            if any(fnmatch.fnmatch(file, p) for p in DENYLIST_PATTERNS) and not is_whitelisted:
                anomalies_found += 1
                continue

            try:
                with open(file_path, "rb") as f:
                    head_bytes = f.read(8192)
                ext = file_path.suffix.lower()
                bt = security.scan_binary(head_bytes, ext)
                if bt and not (ext in [".sh", ".bash", ".zsh"] and "#!/bin/" in bt.get("threat_snippet", "")):
                    if not is_whitelisted:
                        anomalies_found += 1

                content = head_bytes.decode("utf-8", errors="ignore")
                sr = security.scan_content(content, 100)
                if (
                    sr["counts"].get("entropy", 0) > 0 or sr["counts"].get("bitwise_hits", 0) > 0
                ) and not is_whitelisted:
                    anomalies_found += 1
            except Exception:
                pass

    return {"anomalies_found": anomalies_found}


if __name__ == "__main__":
    main()
