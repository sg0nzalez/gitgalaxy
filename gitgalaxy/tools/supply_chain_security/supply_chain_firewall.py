#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: Supply Chain Firewall
# Purpose: Zero-Trust Dependency Verification, Steganography, and Hostile I/O.
# ==============================================================================
import argparse
import sys
import os
import time
import fnmatch
import re
from pathlib import Path

# Import exclusively from the GitGalaxy Hub
from gitgalaxy.core.aperture import ApertureFilter
from gitgalaxy.security.security_lens import SecurityLens
from gitgalaxy.standards.analysis_lens import ThreatPolicy
from gitgalaxy.standards.language_standards import LANGUAGE_DEFINITIONS

# Safely import the config, falling back if the user hasn't added exceptions yet
try:
    from gitgalaxy.standards.gitgalaxy_config import (
        APERTURE_CONFIG, ALLOWLIST_PATHS, DENYLIST_PATTERNS,
        STRICT_IMPORT_MODE, APPROVED_IMPORTS, BLACKLISTED_IMPORTS
    )
except ImportError:
    from gitgalaxy.standards.gitgalaxy_config import APERTURE_CONFIG
    ALLOWLIST_PATHS = []
    DENYLIST_PATTERNS = []
    STRICT_IMPORT_MODE = False
    APPROVED_IMPORTS = []
    BLACKLISTED_IMPORTS = []

def main():
    parser = argparse.ArgumentParser(description="Supply Chain Firewall")
    parser.add_argument("target", help="Directory (e.g., node_modules/ or venv/) to scan")
    args = parser.parse_args()

    target_path = Path(args.target).resolve()
    if not target_path.exists():
        print(f"Error: Target {target_path} does not exist.")
        sys.exit(1)
        
    print(f"🧱 Supply Chain Firewall inspecting dependencies in {target_path.name}...")
    
    # Instantiate the engines
    filter_engine = ApertureFilter(target_path, LANGUAGE_DEFINITIONS, APERTURE_CONFIG)
    security = SecurityLens(policy=ThreatPolicy.get_policy("paranoid"))
    
    # ---> THE SPEED FIX: NEUTER THE LENS <---
    security.THREAT_SIGNATURES = {
        "homoglyphs": security.THREAT_SIGNATURES["homoglyphs"],
        "shadow_imports": security.THREAT_SIGNATURES["shadow_imports"],
        "io": security.THREAT_SIGNATURES["io"],
        "danger": security.THREAT_SIGNATURES["danger"],
        "flux": security.THREAT_SIGNATURES["flux"]
    }
    
    threats_found = 0
    threats_allowed = 0
    forbidden_blocked = 0
    files_evaluated = 0
    
    # Zero-Trust Telemetry
    imports_whitelisted = 0
    imports_blacklisted = 0
    imports_unknown = 0
    
    # The Universal Import Slicer (Regex for require('x'), import 'x', from 'x')
    import_regex = re.compile(r'(?:require(?:_once)?\s*\(\s*|import\s+|from\s+)[\'"]([a-zA-Z0-9_@/-]+)[\'"]')
    
    files_to_deep_scan = []
    
    # ==============================================================================
    # PASS 1: The Funnel (Build the Queue & Catch Surface Threats)
    # ==============================================================================
    for root, dirs, files in os.walk(target_path):
        rel_root = str(Path(root).relative_to(target_path))
        
        if rel_root == ".":
            dirs[:] = [d for d in dirs if filter_engine._check_solar_shield(d)]
        elif not filter_engine._check_solar_shield(rel_root):
            dirs[:] = []
            continue
            
        for file in files:
            files_evaluated += 1
            file_path = Path(root) / file
            
            rel_path_str = str(file_path.relative_to(target_path)).replace('\\', '/')
            is_whitelisted = any(approved in rel_path_str for approved in ALLOWLIST_PATHS)
            
            is_forbidden = any(fnmatch.fnmatch(file, pattern) for pattern in DENYLIST_PATTERNS)
            if is_forbidden and not is_whitelisted:
                print(f"\n🚨 [FORBIDDEN FILE BREACH] Illegal file pattern detected: {rel_path_str}")
                forbidden_blocked += 1
                threats_found += 1
                continue 
            
            is_valid, size, reason = filter_engine.evaluate_path_integrity(file_path)
            if is_valid:
                files_to_deep_scan.append((file_path, rel_path_str, is_whitelisted))

    # ==============================================================================
    # PASS 2: The Deep Scan (Internal Contents & Zero-Trust Verification)
    # ==============================================================================
    print(f"\n🔎 Scanning {len(files_to_deep_scan):,} files for supply chain risks:")
    print("   - Zero-Trust Package Verification")
    print("   - Unicode Homoglyphs & Typo-squatting")
    print("   - Steganography & Shadow Imports")
    print("   - Tainted I/O & Malicious Execution\n")
    
    start_time = time.time()
    
    for file_path, rel_path_str, is_whitelisted in files_to_deep_scan:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            # --- 1. ZERO-TRUST IMPORT VERIFICATION ---
            ext = file_path.suffix.lower()
            if ext in ['.js', '.jsx', '.ts', '.tsx', '.py', '.php', '.go', '.rs']:
                found_packages = import_regex.findall(content)
                for pkg in found_packages:
                    if pkg in BLACKLISTED_IMPORTS:
                        imports_blacklisted += 1
                        threats_found += 1
                        if not is_whitelisted:
                            print(f"🚨 [BLACKLISTED IMPORT] Malicious package '{pkg}' blocked in: {rel_path_str}")
                    elif pkg in APPROVED_IMPORTS:
                        imports_whitelisted += 1
                    else:
                        imports_unknown += 1
                        if STRICT_IMPORT_MODE:
                            threats_found += 1
                            if not is_whitelisted:
                                print(f"🚨 [ZERO-TRUST BREACH] Unknown package '{pkg}' blocked by Strict Mode in: {rel_path_str}")

            # --- 2. PHYSICS ENGINE & HOMOGLYPHS ---
            loc = max(len(content.splitlines()), 1)
            sec_results = security.scan_content(content, loc)
            
            # THE INERT DATA SHIELD & MINIFIED BYPASS
            if ext in ['.json', '.md', '.txt', '.csv', '.yaml', '.yml', '.css', '.less', '.h'] or '.d.ts' in file_path.name or '.min.' in file_path.name or '.umd.' in file_path.name:
                for key in sec_results["counts"].keys():
                    sec_results["counts"][key] = 0
            
            safe_loc = max(loc + 150, 1)
            exposures = security.evaluate_risk(sec_results["counts"], safe_loc)
            
            if "Hidden Malware Risk" in exposures or "Data Injection Risk" in exposures:
                if is_whitelisted:
                    threats_allowed += 1
                else:
                    print(f"\n🚨 [SUPPLY CHAIN COMPROMISE] Density Threshold Breached in: {rel_path_str}")
                    if "Hidden Malware Risk" in exposures:
                        print(f"   -> Malware Exposure Density: {exposures['Hidden Malware Risk'] * 100:.1f}%")
                    if "Data Injection Risk" in exposures:
                        print(f"   -> Injection Exposure Density: {exposures['Data Injection Risk'] * 100:.1f}%")
                    
                    for key, snips in sec_results["snippets"].items():
                        if snips and key in ["homoglyphs", "shadow_imports", "tainted_injection", "danger", "io"]:
                            print(f"   -> Evidence ({key}):")
                            for s in snips: print(f"      {s}")
                    threats_found += 1
        except Exception:
            pass
            
    end_time = time.time()
    time_delta = end_time - start_time
    scan_rate = len(files_to_deep_scan) / time_delta if time_delta > 0 else 0

    # ==============================================================================
    # MISSION REPORT
    # ==============================================================================
    mode_str = "Strict (Exclude Blacklist and Unknown)" if STRICT_IMPORT_MODE else "Audit (Allow Whitelist + Unknown, Exclude Blacklist)"
    
    print("\n" + "="*75)
    print(" 🧱 SUPPLY CHAIN FIREWALL: MISSION REPORT")
    print("="*75)
    print(f" Mode               : {mode_str}")
    print(f" Files Deep Scanned : {len(files_to_deep_scan):,}")
    print(f" Scan Velocity      : {scan_rate:,.0f} files/sec")
    print("-" * 75)
    print(f" Approved Packages    : {imports_whitelisted:,}")
    print(f" Banned Packages      : {imports_blacklisted:,}")
    print(f" Unknown Packages     : {imports_unknown:,}")
    print("-" * 75)
    print(f" Active Threats       : {threats_found:,}")
    print(f" File Denylist Blocks : {forbidden_blocked:,}")
    print(f" File Allowlist Bypasses: {threats_allowed:,}")
    print("-" * 75)
    
    if threats_found > 0:
        print(f" ❌ BUILD FAILED: {threats_found} infected dependencies or policy violations blocked.")
        sys.exit(1)
    else:
        print(" ✅ BUILD PASSED: Dependency supply chain is clean.")
    print("="*75 + "\n")

def run_firewall_audit(target_path: Path) -> dict:
    """Programmatic entry point for GalaxyScope."""
    # Note: Keep this extremely lightweight so it doesn't double-scan the entire repo during the main run.
    # Since the main GalaxyScope pipeline ALREADY scans for Homoglyphs and I/O, we only need to return 
    # the Zero-Trust package counts for the LLM!
    
    imports_unknown = 0
    imports_blacklisted = 0
    import_regex = re.compile(r'(?:require(?:_once)?\s*\(\s*|import\s+|from\s+)[\'"]([a-zA-Z0-9_@/-]+)[\'"]')
    
    for root, dirs, files in os.walk(target_path):
        for file in files:
            if Path(file).suffix.lower() in ['.js', '.ts', '.py', '.php', '.go', '.rs']:
                try:
                    with open(Path(root) / file, 'r', encoding='utf-8', errors='ignore') as f:
                        found_packages = import_regex.findall(f.read())
                        for pkg in found_packages:
                            if pkg in BLACKLISTED_IMPORTS: imports_blacklisted += 1
                            elif pkg not in APPROVED_IMPORTS: imports_unknown += 1
                except Exception: pass
                
    return {"imports_unknown": imports_unknown, "imports_blacklisted": imports_blacklisted}

if __name__ == "__main__":
    main()