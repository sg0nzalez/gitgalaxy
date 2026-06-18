#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: Supply Chain Firewall
# Purpose: Zero-Trust Dependency Verification and Behavioral Policy Enforcement.
# Architecture: RAM-Exclusive Logic Gate (Consumes Phase 1 Topological Graph)
# ==============================================================================
import argparse
import sys
import json
from pathlib import Path

# Import exclusively from the GitGalaxy Hub
from gitgalaxy.security.security_lens import SecurityLens
from gitgalaxy.standards.analysis_lens import ThreatPolicy

# Safely import the config, falling back if the user hasn't added exceptions yet
try:
    from gitgalaxy.standards.gitgalaxy_config import (
        ALLOWLIST_PATHS,
        STRICT_IMPORT_MODE,
        APPROVED_IMPORTS,
        BLACKLISTED_IMPORTS,
    )
except ImportError:
    ALLOWLIST_PATHS = []
    STRICT_IMPORT_MODE = False
    APPROVED_IMPORTS = []
    BLACKLISTED_IMPORTS = []


def run_firewall_audit(parsed_files: list, alias_map: dict = None) -> dict:
    """
    Programmatic entry point for GalaxyScope (Zero-Disk I/O).
    Operates exclusively on the pre-tokenized, anomaly-checked RAM graph from Phase 1.
    """
    security = SecurityLens(policy=ThreatPolicy.get_policy("paranoid"))
    safe_alias_map = alias_map or {}

    imports_whitelisted = 0
    imports_blacklisted = 0
    imports_unknown = 0
    threats_found = 0
    threats_allowed = 0

    if not parsed_files:
        return {
            "imports_unknown": imports_unknown,
            "imports_blacklisted": imports_blacklisted,
            "threats_found": threats_found,
        }

    for star in parsed_files:
        rel_path_str = star.get("path", "unknown")
        is_whitelisted = any(approved in rel_path_str for approved in ALLOWLIST_PATHS)

        # =====================================================================
        # 1. ZERO-TRUST IMPORT VERIFICATION
        # =====================================================================
        for raw_pkg in star.get("raw_imports", []):
            # The Relative Path Shield: Ignore native internal routing
            if raw_pkg.startswith("."):
                continue

            # The Deep-Path Truncator: Normalize sub-module paths to their base package name
            if raw_pkg.startswith("@"):
                parts = raw_pkg.split("/")
                pkg = f"{parts[0]}/{parts[1]}" if len(parts) >= 2 else raw_pkg
            else:
                pkg = raw_pkg.split("/")[0]

            # The Identity Translation Shield: Dereference manifest aliases
            true_pkg = safe_alias_map.get(pkg, pkg)

            if true_pkg in BLACKLISTED_IMPORTS:
                imports_blacklisted += 1
                threats_found += 1
                # The Whitelist Loophole Fix: A blacklisted import is ALWAYS a threat. Never suppress it.
                if true_pkg != pkg:
                    print(
                        f"🚨 [BLACKLISTED IMPORT] Spoofed alias blocked: '{pkg}' -> '{true_pkg}' in: {rel_path_str}"
                    )
                else:
                    print(
                        f"🚨 [BLACKLISTED IMPORT] Malicious package '{pkg}' blocked in: {rel_path_str}"
                    )
            elif true_pkg in APPROVED_IMPORTS:
                imports_whitelisted += 1
            else:
                imports_unknown += 1
                if STRICT_IMPORT_MODE:
                    threats_found += 1
                    if not is_whitelisted:
                        if true_pkg != pkg:
                            print(
                                f"🚨 [ZERO-TRUST BREACH] Spoofed alias '{pkg}' -> '{true_pkg}' blocked by Strict Mode in: {rel_path_str}"
                            )
                        else:
                            print(
                                f"🚨 [ZERO-TRUST BREACH] Unknown package '{pkg}' blocked by Strict Mode in: {rel_path_str}"
                            )

        # =====================================================================
        # 2. BEHAVIORAL POLICY ENFORCEMENT (Leveraging Phase 1 Measurements)
        # =====================================================================
        # Extract the raw threat equations calculated natively by Prism/Detector in Phase 1
        equations = star.get("equations", {})
        loc = star.get("coding_loc", 1)

        # Clone the dictionary to safely apply the sandbox multiplier without corrupting global RAM
        local_counts = dict(equations)

        # THE BUILD-TIME EXECUTION MULTIPLIER (STATIC SANDBOX)
        # Apply a massive artificial density multiplier to manifest triggers so any
        # I/O or Danger hits instantly detonate the firewall.
        build_time_multiplier = 1.0
        filename = Path(rel_path_str).name
        if filename in [
            "setup.py",
            "build.rs",
            "preinstall.js",
            "postinstall.js",
            "package.json",
        ]:
            build_time_multiplier = 10.0

        safe_loc = max(loc + 150, 1)

        if build_time_multiplier > 1.0:
            for k in local_counts:
                if isinstance(local_counts[k], (int, float)):
                    local_counts[k] = int(local_counts[k] * build_time_multiplier)

        # Evaluate risk using Phase 1 network topography context (e.g., Blast Radius)
        network_metrics = star.get("dependency_network", {})
        exposures = security.evaluate_risk(local_counts, safe_loc, network_metrics)

        if (
            "Hidden Malware Risk" in exposures
            or "Data Injection Risk" in exposures
            or "Secrets Leak Risk" in exposures
            or "Logic Bomb Risk" in exposures
        ):
            if is_whitelisted:
                threats_allowed += 1
            else:
                print(
                    f"\n🚨 [SUPPLY CHAIN COMPROMISE] Density Threshold Breached in: {rel_path_str}"
                )
                for risk, density in exposures.items():
                    print(f"   -> {risk}: {density * 100:.1f}%")
                threats_found += 1

    return {
        "imports_whitelisted": imports_whitelisted,
        "imports_unknown": imports_unknown,
        "imports_blacklisted": imports_blacklisted,
        "threats_found": threats_found,
        "threats_allowed": threats_allowed,
    }


def main():
    """
    Standalone Execution Mode.
    Because the firewall is now completely divested of redundant O(N) disk parsing,
    it must be fed the compiled JSON RAM-graph generated by the GalaxyScope orchestrator.
    """
    from gitgalaxy.licensing import enforce_licensing_guard

    enforce_licensing_guard("Supply Chain Firewall")

    parser = argparse.ArgumentParser(
        description="Supply Chain Firewall (RAM-Exclusive Mode)"
    )
    parser.add_argument(
        "target", help="Path to the compiled GalaxyScope RAM graph (e.g., results.json)"
    )
    args = parser.parse_args()

    target_path = Path(args.target).resolve()
    if not target_path.exists():
        print(f"Error: RAM graph '{target_path}' does not exist.")
        sys.exit(1)

    print(
        f"🧱 Supply Chain Firewall ingesting orchestrator RAM graph from {target_path.name}..."
    )

    try:
        with open(target_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            parsed_files = data.get("stars", [])
    except Exception as e:
        print(f"❌ Failed to parse RAM graph JSON: {e}")
        sys.exit(1)

    # In standalone CLI mode, we bypass the dynamic manifest parsing for speed,
    # relying purely on strict exact-match dependencies and behavioral math.
    results = run_firewall_audit(parsed_files, alias_map={})

    mode_str = (
        "Strict (Exclude Blacklist and Unknown)"
        if STRICT_IMPORT_MODE
        else "Audit (Allow Whitelist + Unknown)"
    )

    print("\n" + "=" * 75)
    print(" 🧱 SUPPLY CHAIN FIREWALL: MISSION REPORT (RAM-EXCLUSIVE)")
    print("=" * 75)
    print(f" Mode                 : {mode_str}")
    print(f" Files Evaluated      : {len(parsed_files):,}")
    print("-" * 75)
    print(f" Approved Packages    : {results['imports_whitelisted']:,}")
    print(f" Banned Packages      : {results['imports_blacklisted']:,}")
    print(f" Unknown Packages     : {results['imports_unknown']:,}")
    print("-" * 75)
    print(f" Active Threats       : {results['threats_found']:,}")
    print(f" Allowlist Bypasses   : {results['threats_allowed']:,}")
    print("-" * 75)

    if results["threats_found"] > 0:
        print(
            f" ❌ BUILD FAILED: {results['threats_found']} infected dependencies or policy violations blocked."
        )
        sys.exit(1)
    else:
        print(" ✅ BUILD PASSED: Dependency supply chain is clean.")
    print("=" * 75 + "\n")


if __name__ == "__main__":
    main()
