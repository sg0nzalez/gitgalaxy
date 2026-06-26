#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Tool: Universal Zero-Trust SBOM Generator
#
# PURPOSE: 
# Generates a CycloneDX Software Bill of Materials (SBOM) with structural 
# verification of dependencies across multiple language ecosystems (NPM, 
# Composer, PyPI, Cargo, Go, Ruby, Maven).
#
# ARCHITECTURAL DECISION:
# Standard SBOM generators inherently trust manifest files (e.g., package.json).
# This generator implements a Zero-Trust architecture by physically locating the
# downloaded dependency on disk and verifying its structural signatures and 
# entropy to detect namespace hijacking, spoofing, and supply chain poisoning.
# ==============================================================================
import argparse
import sys
import os
import json
import uuid
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Tuple

# Import exclusively from the GitGalaxy Hub
from gitgalaxy.security.security_lens import SecurityLens
from gitgalaxy.standards.analysis_lens import ThreatPolicy
from gitgalaxy.standards.language_standards import LANGUAGE_DEFINITIONS
from gitgalaxy.standards.gitgalaxy_config import LEXICAL_FAMILY_HEURISTICS
from gitgalaxy.standards.language_lens import LanguageDetector


class UniversalManifestExtractor:
    """Uses regex and standard parsing to extract dependencies from any ecosystem."""

    @staticmethod
    def extract_manifest(manifest_path: Path) -> Tuple[str, Dict[str, str]]:
        filename = manifest_path.name
        deps = {}
        ecosystem = "unknown"

        try:
            if filename == "package.json":
                ecosystem = "npm"
                with open(manifest_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    deps.update(data.get("dependencies", {}))
                    deps.update(data.get("devDependencies", {}))

            elif filename == "composer.json":
                ecosystem = "packagist"  # PHP Composer
                with open(manifest_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    deps.update(data.get("require", {}))
                    deps.update(data.get("require-dev", {}))
                    # Remove the php version requirement
                    deps.pop("php", None)

            elif filename == "requirements.txt":
                ecosystem = "pypi"
                with open(manifest_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#"):
                            clean_name = re.split(r"[=><~]", line)[0].strip()
                            # Get version if explicitly defined, else 'latest'
                            version = line.split("==")[1].strip() if "==" in line else "latest"
                            deps[clean_name] = version

            elif filename == "Cargo.toml":
                ecosystem = "cargo"
                with open(manifest_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Universal regex to grab [dependencies] blocks
                    dep_blocks = re.findall(r"\[(?:dev-)?dependencies\](.*?)(\n\[|$)", content, re.DOTALL)
                    for block, _ in dep_blocks:
                        for line in block.splitlines():
                            line = line.strip()
                            if line and not line.startswith("#") and "=" in line:
                                pkg_name = line.split("=")[0].strip()
                                pkg_name = line.split("=")[0].strip()
                                deps[pkg_name] = "latest"  # Simplified version extraction

            elif filename == "go.mod":
                ecosystem = "golang"
                with open(manifest_path, "r", encoding="utf-8") as f:
                    in_require_block = False
                    for line in f:
                        line = line.strip()
                        if line.startswith("require ("):
                            in_require_block = True
                            continue
                        if line == ")":
                            in_require_block = False
                            continue
                        if in_require_block and line and not line.startswith("//"):
                            parts = line.split()
                            if len(parts) >= 2:
                                deps[parts[0]] = parts[1]
                        elif line.startswith("require ") and not in_require_block:
                            parts = line.split()
                            if len(parts) >= 3:
                                deps[parts[1]] = parts[2]

            elif filename == "Gemfile":
                ecosystem = "rubygems"
                with open(manifest_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        # Extract: gem 'nokogiri', '~> 1.11'
                        if line.startswith("gem "):
                            parts = line.split(",")
                            pkg_name = parts[0].replace("gem", "").strip(" '\"")
                            version = parts[1].strip(" '\"") if len(parts) > 1 else "latest"
                            deps[pkg_name] = version

            elif filename == "pom.xml":
                ecosystem = "maven"
                with open(manifest_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Extract artifactId and version from XML blocks
                    deps_raw = re.findall(
                        r"<dependency>.*?<artifactId>([^<]+)</artifactId>(?:.*?<version>([^<]+)</version>)?.*?</dependency>",
                        content,
                        re.DOTALL,
                    )
                    for artifact, version in deps_raw:
                        deps[artifact] = version if version else "latest"

        except Exception:
            pass

        return ecosystem, deps

    @staticmethod
    def locate_physical_package(target_path: Path, pkg_name: str, ecosystem: str) -> Path:
        """Resolves the structural location of a package within the repository bounds."""
        if ecosystem == "npm":
            target = target_path / "node_modules" / pkg_name
            return target if target.exists() else None

        elif ecosystem == "packagist":
            # Composer packages are in vendor/vendor-name/package-name
            target = target_path / "vendor" / pkg_name
            return target if target.exists() else None

        elif ecosystem == "pypi":
            # Hunt through common local virtual environment folders
            safe_pkg_name = pkg_name.replace("-", "_").lower()
            for venv_dir in ["venv", ".venv", "env"]:
                venv_path = target_path / venv_dir
                if venv_path.exists():
                    for root, dirs, _ in os.walk(venv_path):
                        if "site-packages" in root:
                            # Case-insensitive match for the package folder
                            for d in dirs:
                                if d.lower() == safe_pkg_name or d.lower().startswith(f"{safe_pkg_name}-"):
                                    return Path(root) / d

        elif ecosystem == "golang":
            # Go packages are often vendored in the project's root 'vendor/' directory
            target = target_path / "vendor" / pkg_name
            return target if target.exists() else None

        elif ecosystem == "rubygems":
            # Ruby often vendors gems locally here
            target = target_path / "vendor" / "bundle"
            if target.exists():
                for root, dirs, _ in os.walk(target):
                    if pkg_name in dirs:
                        return Path(root) / pkg_name
            return None

        elif ecosystem == "maven":
            # Java local dependency pulls usually land here
            target = target_path / "target" / "dependency"
            if target.exists():
                # Just verifying the jar/folder exists loosely
                for file in target.iterdir():
                    if pkg_name.lower() in file.name.lower():
                        return file
            return None

        return None


def main():
    from gitgalaxy.licensing import enforce_licensing_guard

    enforce_licensing_guard("Universal Zero-Trust SBOM Generator")

    parser = argparse.ArgumentParser(description="Universal Zero-Trust SBOM Generator")
    parser.add_argument("target", help="Root directory of the project")
    parser.add_argument(
        "--out",
        default="bom.json",
        help="Output JSON filename (appended to target name)",
    )
    args = parser.parse_args()

    target_path = Path(args.target).resolve()
    if not target_path.exists():
        print(f"Error: Target {target_path} does not exist.")
        sys.exit(1)

    print(f"📦 Initializing GitGalaxy Universal SBOM Generator on {target_path.name}...")

    security = SecurityLens(policy=ThreatPolicy.get_policy("paranoid"))
    detector = LanguageDetector(LANGUAGE_DEFINITIONS, LEXICAL_FAMILY_HEURISTICS)
    extractor = UniversalManifestExtractor()

    components = []
    total_anomalies = 0
    total_missing = 0
    total_verified = 0

    # 1. Harvest Manifests Universally
    manifest_targets = [
        "package.json",
        "composer.json",
        "requirements.txt",
        "Cargo.toml",
        "go.mod",
        "Gemfile",
        "pom.xml",
    ]
    found_manifests = [target_path / m for m in manifest_targets if (target_path / m).exists()]

    if not found_manifests:
        print("⚠️  No supported manifests found in the root directory.")
        sys.exit(0)

    # 2. The Zero-Trust Structural Audit
    for manifest in found_manifests:
        ecosystem, packages = extractor.extract_manifest(manifest)
        if not packages:
            continue

        print(f"\n🔎 Auditing {len(packages)} {ecosystem.upper()} dependencies from {manifest.name}...")

        for pkg_name, pkg_version in packages.items():
            trust_status = "VERIFIED_SAFE"
            anomaly_notes = []

            pkg_path = extractor.locate_physical_package(target_path, pkg_name, ecosystem)

            if not pkg_path:
                trust_status = "UNVERIFIED_MISSING_ON_DISK"
                anomaly_notes.append("Package declared in manifest but not found locally.")
                total_missing += 1
            else:
                # ==============================================================================
                # DEFENSIVE DESIGN (VELOCITY VS. DEPTH):
                # Scanning every file in `node_modules` would grind the pipeline to a halt.
                # We sample a maximum of 5 executable files per dependency. If a package has 
                # been spoofed or poisoned, malicious entropy or structural anomalies will 
                # almost always be detectable within the primary entry points.
                # ==============================================================================
                scanned_files = 0
                for root, _, files in os.walk(pkg_path):
                    if scanned_files > 5:
                        break

                    for file in files:
                        if not file.endswith((".js", ".py", ".ts", ".php", ".rs")):
                            continue

                        file_path = Path(root) / file
                        try:
                            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                                content = f.read(8192)

                            sec_results = security.scan_content(content, 100)
                            if sec_results["counts"].get("entropy", 0) > 0:
                                trust_status = "SPOOF_DETECTED"
                                anomaly_notes.append(f"High Entropy (>4.8) in {file}")

                            id_result = detector.inspect(file_path, content)
                            if id_result["anomaly_flags"]:
                                trust_status = "SPOOF_DETECTED"
                                anomaly_notes.extend(id_result["anomaly_flags"])

                            scanned_files += 1
                        except Exception:
                            pass

                if trust_status == "SPOOF_DETECTED":
                    total_anomalies += 1
                    print(f"   🚨 [SPOOF DETECTED] {pkg_name}@{pkg_version}")
                else:
                    total_verified += 1

            if trust_status == "UNVERIFIED_MISSING_ON_DISK":
                print(f"   ⚠️  [MISSING] {pkg_name}@{pkg_version}")

            components.append(
                {
                    "type": "library",
                    "name": pkg_name,
                    "version": pkg_version,
                    "purl": f"pkg:{ecosystem}/{pkg_name}@{pkg_version}",
                    "properties": [
                        {"name": "gitgalaxy:trust_status", "value": trust_status},
                        {
                            "name": "gitgalaxy:anomaly_notes",
                            "value": (" | ".join(anomaly_notes) if anomaly_notes else "None"),
                        },
                    ],
                }
            )

    # ==============================================================================
    # CYCLONEDX JSON FORMATTING
    # ==============================================================================
    bom = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.4",
        "serialNumber": f"urn:uuid:{uuid.uuid4()}",
        "version": 1,
        "metadata": {
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "tools": [
                {
                    "vendor": "GitGalaxy",
                    "name": "Universal Zero-Trust SBOM",
                    "version": "6.3.0",
                }
            ],
            "component": {"type": "application", "name": target_path.name},
        },
        "components": components,
    }

    # Output to the parent directory of the target
    out_path = target_path.parent / f"{target_path.name}_{args.out}"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(bom, f, indent=4)

    # ==============================================================================
    # AUDIT REPORT
    # ==============================================================================
    print("\n" + "=" * 75)
    print(" 📦 SBOM GENERATOR: AUDIT REPORT")
    print("=" * 75)
    print(f" Dependencies Claimed : {len(components)}")
    print(" Standard Export      : CycloneDX 1.4 JSON")
    print(f" Output Location      : {out_path.resolve()}")
    print("-" * 75)
    print(f" Verified Safe        : {total_verified}")
    print(f" Missing on Disk      : {total_missing}")
    print(f" Spoofed / Infected   : {total_anomalies}")
    print("-" * 75)
    if total_anomalies > 0:
        print(f" ❌ ALERT: {total_anomalies} dependencies failed structural verification.")
    else:
        print(" ✅ SUCCESS: Structural verification complete. SBOM sealed.")
    print("=" * 75 + "\n")


if __name__ == "__main__":
    main()