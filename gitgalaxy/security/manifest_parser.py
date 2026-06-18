# ==============================================================================
# GitGalaxy - Manifest Parser
# Purpose: Parses ecosystem manifests and lockfiles to extract cryptographic
#          realities, neutralizing dependency confusion and alias spoofing.
# ==============================================================================
import json
import logging
import re
from pathlib import Path


class ManifestParser:
    def __init__(self, parent_logger=None):
        self.logger = (
            parent_logger.getChild("manifest_parser")
            if parent_logger
            else logging.getLogger("manifest_parser")
        )

        # Matches standard Python packages, dropping version constraints (==, >=, ~)
        self.py_req_regex = re.compile(r"^([a-zA-Z0-9_\-]+)(?:[=><~].*)?$")

        # Matches external Python injections (git+, file://, http)
        self.py_injection_regex = re.compile(
            r"^(?:git\+|file:|https?:|hg\+|svn\+|bzr\+)(.*)$"
        )

    def build_translation_map(self, manifest_paths: list) -> dict:
        """
        Accepts a list of exact file paths and builds a global O(1) translation
        dictionary by parsing package.json, package-lock.json, and requirements.txt.
        """
        translation_map = {}

        for path_str in manifest_paths:
            manifest_path = Path(path_str)
            if not manifest_path.exists():
                continue

            filename = manifest_path.name.lower()

            try:
                if filename == "package.json":
                    self._parse_package_json(manifest_path, translation_map)
                elif filename == "package-lock.json":
                    self._parse_package_lock(manifest_path, translation_map)
                elif filename == "requirements.txt":
                    self._parse_requirements_txt(manifest_path, translation_map)
                elif filename in ["pip.conf", ".pypirc", "pip.ini"]:
                    self._parse_pip_conf(manifest_path, translation_map)
            except Exception as e:
                self.logger.warning(
                    f"Manifest Parser: Failed to parse {filename} - {e}"
                )

        return translation_map

    def _parse_package_json(self, filepath: Path, translation_map: dict):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        deps = data.get("dependencies", {})
        dev_deps = data.get("devDependencies", {})
        all_deps = {**deps, **dev_deps}

        for alias, version_string in all_deps.items():
            if not isinstance(version_string, str):
                continue

            # 1. NPM Aliasing (npm:real-package@1.0)
            if version_string.startswith("npm:"):
                raw_pkg = version_string[4:]
                if raw_pkg.startswith("@"):
                    real_pkg = (
                        raw_pkg.rsplit("@", 1)[0] if "@" in raw_pkg[1:] else raw_pkg
                    )
                else:
                    real_pkg = raw_pkg.split("@")[0]
                translation_map[alias] = real_pkg

            # 2. Local File / Git Spoofing (file:./malware.js, github:hacker/repo)
            elif version_string.startswith(("file:", "github:", "git+", "http")):
                translation_map[alias] = version_string
                self.logger.warning(
                    f"Manifest Parser: Flagged external/local override for '{alias}' -> {version_string}"
                )

    def _parse_package_lock(self, filepath: Path, translation_map: dict):
        """
        Extracts the true resolution URLs from package-lock.json v2/v3.
        Neutralizes Namespace Hijacking by verifying internal registries.
        """
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        packages = data.get("packages", {})
        for node_path, info in packages.items():
            if not node_path or "node_modules/" not in node_path:
                continue

            pkg_name = node_path.split("node_modules/")[-1]
            resolved_url = info.get("resolved", "")

            # If the resolved URL points to a strange domain or a direct Git link, flag it.
            if resolved_url and not resolved_url.startswith(
                "[https://registry.npmjs.org/](https://registry.npmjs.org/)"
            ):
                translation_map[pkg_name] = resolved_url
                self.logger.info(
                    f"Manifest Parser: Flagged non-standard resolution for '{pkg_name}' -> {resolved_url}"
                )

    def _parse_requirements_txt(self, filepath: Path, translation_map: dict):
        """
        Extracts direct packages and flags external source injections in Python.
        """
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                # Check for direct external injections (git+https://, file://)
                injection_match = self.py_injection_regex.match(line)
                if injection_match:
                    # Map the raw string directly so the firewall flags it as an unknown/external source
                    translation_map[line] = line
                    self.logger.warning(
                        f"Manifest Parser: Flagged Python external injection -> {line}"
                    )
                    continue

                # Standard package capture
                match = self.py_req_regex.match(line)
                if match:
                    pkg_name = match.group(1)
                    # We just ensure the package exists in the map as itself to verify it against the firewall
                    if pkg_name not in translation_map:
                        translation_map[pkg_name] = pkg_name

    def _parse_pip_conf(self, filepath: Path, translation_map: dict):
        """
        Hunts for Dependency Confusion vulnerabilities in Python by auditing
        index-url and extra-index-url routing in pip.conf or .pypirc.
        """
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith(("#", ";")):
                    continue

                # Look for custom registry routing
                if (
                    "index-url" in line
                    or "extra-index-url" in line
                    or "repository" in line
                ):
                    parts = line.split("=")
                    if len(parts) == 2:
                        url = parts[1].strip()

                        # Flag unencrypted HTTP or suspicious ngrok/local proxies immediately
                        if (
                            url.startswith("http://")
                            or "ngrok" in url
                            or "localtunnel" in url
                        ):
                            self.logger.warning(
                                f"🚨 Manifest Parser: INSECURE REGISTRY DETECTED -> {url}"
                            )
                            translation_map[f"INSECURE_REGISTRY_{filepath.name}"] = url
