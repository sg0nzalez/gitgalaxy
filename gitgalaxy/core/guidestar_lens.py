# ==============================================================================
# GitGalaxy
# Copyright (c) 2026 Joe Esquibel
#
# This source code is licensed under the PolyForm Noncommercial License 1.0.0.
# You may not use this file except in compliance with the License.
# A copy of the license can be found in the LICENSE file in the root directory
# of this project, or at https://polyformproject.org/licenses/noncommercial/1.0.0/
# ==============================================================================
import re
import os
import json
import logging
import fnmatch
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple, Union
from gitgalaxy.standards.gitgalaxy_config import GUIDESTAR_CONFIG

# ==============================================================================
# GitGalaxy Phase 0.5: Sector Intelligence (The GuideStar Lens)
# Strategy: v6.3.0 (Deep Manifest Inspection & Evidence Hierarchy)
# ==============================================================================


class GuideStarLens:
    """
    The GuideStar Lens provides 'Social Proof' for files by parsing repository
    instructions and structural metadata.

    This module uses a tiered skepticism matrix to generate a Prior Probability Vector.
    In v6.3.0, it performs 'Deep Inspection' of manifests to identify entry points,
    build targets mentioned in configurations, and explicit linguistic overrides
    via .gitattributes.
    """

    # Fetch intelligence dictionaries directly from the Universal Laws
    _gs_config = GUIDESTAR_CONFIG

    MANIFEST_MAP = _gs_config.get("MANIFEST_MAP", {})
    INTENT_BIASED_SECTORS = set(_gs_config.get("INTENT_BIASED_SECTORS", []))
    EXEC_PREFIX_MAP = _gs_config.get("EXEC_PREFIX_MAP", {})

    # We keep the compiled regex here since it is an operational mechanic, not a tunable list
    README_TARGET_HEADERS = re.compile(
        r"^#+\s+(Usage|Structure|File|Layout|Getting\s+Started|Installation|Architecture|Scripts|CLI)",
        re.I | re.MULTILINE,
    )

    def __init__(
        self,
        root_path: Union[str, Path],
        priority_whitelist: Optional[List[str]] = None,
        parent_logger: Optional[logging.Logger] = None,
    ):
        """Initializes the Intelligence Engine and calibrates the prior maps."""
        if parent_logger:
            self.logger = parent_logger.getChild("guidestar")
            self.logger.setLevel(parent_logger.level)
        else:
            self.logger = logging.getLogger("guidestar")
            self.logger.setLevel(logging.INFO)

        self.root = Path(root_path).resolve()
        self.whitelist = set(priority_whitelist or [])

        # Internal Prior Map: Dict[filename, {lang, confidence, proof}]
        self.priors: Dict[str, Dict[str, Any]] = {}

        # Pattern Prior Map for .gitattributes (e.g., *.h)
        self.pattern_priors: Dict[str, Dict[str, Any]] = {}

        # Spatial Documentation Map: Dict[directory_path, shield_strength_float]
        self.doc_umbrellas: Dict[str, float] = {}

        self.logger.debug(f"GuideStar Lens Online | Sector: {self.root.name}")

    def align_telescope(self):
        """Phase 0.5: Dispatches scouts to scan manifests and explicit directives."""
        self.logger.info("GuideStar: Scanning sectors for Social & Roadmap Proof...")

        # 1. The Roadmap Scout (Manifests)
        self._survey_manifests()

        # 2. The Authority Scout (.gitattributes)
        self._survey_gitattributes()

        # 3. The Evasion Scout (.gitignore)
        self._survey_gitignore()

        # 4. The Knowledge Scout (Documentation Umbrellas)
        self._survey_knowledge_anchors()

        self.logger.info(
            f"GuideStar: Alignment complete. Cached {len(self.priors)} intent priors, {len(self.pattern_priors)} pattern rules, and {len(self.doc_umbrellas)} documentation shields."
        )

    def get_intent_status(self, path: Union[str, Path]) -> Tuple[bool, Dict[str, Any]]:
        """Returns the Bayesian Prior for a given file path based on strict, pattern, or sector match."""
        path_obj = Path(path)
        filename = path_obj.name
        rel_path = str(path_obj.relative_to(self.root) if path_obj.is_absolute() else path_obj).replace("\\", "/")

        # 1. Check direct filename match (e.g., 'main.py')
        prior = self.priors.get(filename)

        # 2. Check path-based match (e.g., 'src/index.js')
        if not prior:
            prior = self.priors.get(rel_path)

        # 3. Check Pattern-based match from .gitattributes (e.g., '*.h')
        if not prior:
            for pattern, pat_prior in self.pattern_priors.items():
                # Test against both the raw filename and the relative path
                if fnmatch.fnmatch(filename, pattern) or fnmatch.fnmatch(rel_path, pattern):
                    prior = pat_prior
                    break

        # 4. Sector Bias: If the file lives in an intentional folder, it gets a base prior
        if not prior:
            parts = set(p.lower() for p in path_obj.parts)
            if parts.intersection(self.INTENT_BIASED_SECTORS):
                return True, {
                    "lang_id": "unknown",
                    "intensity": 0.75,
                    "source_proof": "Sector Bias",
                }

        if prior:
            return True, prior

        return False, {}

    def _inject_prior(self, filename: str, lang: str, confidence: float, proof: str):
        """Safely updates the prior map with evidence-based intelligence."""
        if not filename:
            return

        # Clean the filename (remove leading dots or path separators)
        filename = filename.strip("./").strip()

        # If we already have a prior, we only update if the new proof is more authoritative
        existing = self.priors.get(filename)
        if existing and existing["intensity"] >= confidence:
            return

        # Whitelist Trust Bonus
        if filename in self.whitelist:
            confidence = min(confidence + 0.1, 0.99)
            proof = f"{proof} + Whitelist Bonus"

        self.priors[filename] = {
            "lang_id": lang,
            "intensity": round(confidence, 2),
            "source_proof": proof,
        }

    def _inject_pattern_prior(self, pattern: str, lang: str, confidence: float, proof: str):
        """Safely updates the pattern prior map with wildcard evidence."""
        if not pattern:
            return

        existing = self.pattern_priors.get(pattern)
        if existing and existing["intensity"] >= confidence:
            return

        self.pattern_priors[pattern] = {
            "lang_id": lang,
            "intensity": round(confidence, 2),
            "source_proof": proof,
        }

    # ==============================================================================
    # DEEP MANIFEST INSPECTION (Roadmap Scout)
    # ==============================================================================

    def _survey_manifests(self):
        """Identifies authoritative project anchors and parses their internal logic."""
        # Dynamically inject requirements.txt if it wasn't in the global config
        active_manifests = dict(self.MANIFEST_MAP)
        if "requirements.txt" not in active_manifests:
            active_manifests["requirements.txt"] = "python"

        for manifest, lang in active_manifests.items():
            path = self.root / manifest
            if path.exists():
                # 1. Prioritize the manifest itself
                self._inject_prior(manifest, lang, 0.90, "Roadmap Lock (Manifest)")

                # 2. Deep Inspection: Parse the manifest to find referenced files
                self._deep_inspect_manifest(path, manifest, lang)

    def _deep_inspect_manifest(self, path: Path, filename: str, lang: str):
        """Dispatches files to specific parsers based on their format."""
        try:
            # 1. Scan for AI/LLM footprints in the raw text first
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                self._detect_ai_ecosystem(f.read(), filename)

            # 2. Route to specific parsers for structural roadmaps
            if filename == "package.json":
                self._parse_package_json(path)
            elif filename == "Makefile" or filename.endswith(".mk"):
                self._parse_makefile(path)
            elif filename in ("pyproject.toml", "Cargo.toml", "requirements.txt"):
                self._parse_toml_style_manifest(path, lang)
        except Exception as e:
            self.logger.debug(f"GuideStar: Deep inspection failed for '{filename}': {e}")

    def _detect_ai_ecosystem(self, content: str, filename: str):
        """Scans manifest files for explicit AI/LLM orchestrators or tensor frameworks."""
        ai_keywords = {
            "langchain",
            "llama_index",
            "openai",
            "anthropic",
            "torch",
            "tensorflow",
            "transformers",
            "huggingface_hub",
            "vllm",
            "ollama",
            "chromadb",
            "pinecone",
        }

        found = [kw for kw in ai_keywords if kw in content.lower()]
        if found:
            self.logger.info(f"🧠 AI ECOSYSTEM DETECTED: Found {found} in {filename}. Flagging repository archetype.")
            # We inject a synthetic prior so the downstream pipeline knows this is an AI repo
            self._inject_prior("__galaxy_brain__.ai", "json", 1.0, f"AI Ecosystem Lock ({found[0]})")

    def _parse_package_json(self, path: Path):
        """Extracts 'main', 'bin', and 'scripts' from Node/JS manifests."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

                # Main Entry Point
                if "main" in data:
                    self._inject_prior(
                        data["main"],
                        "javascript",
                        0.95,
                        "Manifest Entry (package.json:main)",
                    )

                # Binary targets
                bins = data.get("bin", {})
                if isinstance(bins, str):
                    self._inject_prior(bins, "javascript", 0.95, "Manifest Binary (package.json:bin)")
                elif isinstance(bins, dict):
                    for b_path in bins.values():
                        self._inject_prior(
                            b_path,
                            "javascript",
                            0.95,
                            "Manifest Binary (package.json:bin)",
                        )

                # Scripts (Finding secondary logic)
                scripts = data.get("scripts", {})
                for name, cmd in scripts.items():
                    # Find potential filenames in command strings using regex
                    # e.g. "node src/server.js" -> "src/server.js"
                    files = re.findall(r"([a-zA-Z0-9_\-\./]+\.(?:js|ts|mjs|cjs))", cmd)
                    for f in files:
                        self._inject_prior(
                            f,
                            "javascript",
                            0.85,
                            f"Manifest Script (package.json:scripts:{name})",
                        )
        except Exception:
            pass

    def _parse_makefile(self, path: Path):
        """Parses Makefiles to find source variables and targets."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

                # Strategy 1: Find variable assignments like SRCS = main.c ...
                matches = re.findall(r"(?:SRCS|SOURCES|FILES|TARGET)\s*[+:]?=\s*(.*)", content, re.I)
                for m in matches:
                    files = m.split()
                    for f in files:
                        if "." in f:  # Heuristic for a filename
                            self._inject_prior(f, "unknown", 0.85, "Manifest Source (Makefile)")

                # Strategy 2: Find target lines like 'build: main.o'
                targets = re.findall(r"^([a-zA-Z0-9_\-]+)\s*:", content, re.M)
                for t in targets:
                    if t not in ("all", "clean", "test", "install"):
                        self._inject_prior(t, "unknown", 0.70, "Makefile Target")
        except Exception:
            pass

    def _parse_toml_style_manifest(self, path: Path, lang: str):
        """Simple regex-based TOML parser for script/entry points."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

                # Find quoted paths in script or bin sections
                # e.g. in pyproject.toml: [project.scripts] my-app = "app.main:main"
                # e.g. in Cargo.toml: path = "src/main.rs"
                matches = re.findall(r'path\s*=\s*"(.*)"', content)
                matches += re.findall(r'=\s*"(.*):', content)  # Python entry points

                for m in matches:
                    if "/" in m or "." in m:
                        self._inject_prior(m, lang, 0.95, f"Manifest Roadmap ({path.name})")
        except Exception:
            pass

    def _extract_execution_triggers(self, text: str):
        """Finds extensionless files used in command-line examples and infers exact language."""
        # Match patterns like './setup' or 'python3 main'
        exec_matches = re.findall(
            r"(\.\/|python3?\s+|node\s+|sh\s+|bash\s+|cargo\s+run\s+|go\s+run\s+)([a-zA-Z0-9_\-\./]+)",
            text,
        )
        for prefix, filename in exec_matches:
            prefix_clean = prefix.strip().split()[0]  # Get 'python' from 'python3'
            predicted_lang = self.EXEC_PREFIX_MAP.get(prefix_clean, "unknown")

            # --- THE FIX: Remove the shell dead-end for generic execution prefixes ---
            if prefix.strip() == "./":
                predicted_lang = "unknown"

            self.logger.debug(f"GuideStar: Contextual hint found via execution trigger: '{filename}'")
            self._inject_prior(filename, predicted_lang, 0.85, f"Execution Trigger ({prefix_clean})")

    # ==============================================================================
    # EXPLICIT AUTHORITY (The .gitattributes Scout)
    # ==============================================================================

    def _survey_gitattributes(self):
        """Parses .gitattributes for explicit linguist-language overrides."""
        gitattr_path = self.root / ".gitattributes"
        if not gitattr_path.exists():
            return

        # Map common human-readable GitHub linguist names to our engine's internal IDs
        lang_map = {
            "c++": "cpp",
            "c#": "csharp",
            "objective-c": "objective-c",
            "objective-c++": "objective-c",
            "javascript": "javascript",
            "typescript": "typescript",
        }

        try:
            with open(gitattr_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    # Ignore empty lines and comments
                    if not line or line.startswith("#"):
                        continue

                    parts = line.split()
                    if len(parts) < 2:
                        continue

                    pattern = parts[0]
                    for attr in parts[1:]:
                        if attr.startswith("linguist-language="):
                            raw_lang = attr.split("=", 1)[1].lower().strip("'\"")

                            # Translate the name, or fallback to the raw string
                            engine_lang = lang_map.get(raw_lang, raw_lang)

                            # 0.99 Confidence: This is explicit human instruction
                            self._inject_pattern_prior(
                                pattern,
                                engine_lang,
                                0.99,
                                f"Authoritative Override (.gitattributes: {attr})",
                            )
                            self.logger.debug(
                                f"GuideStar: Locked pattern '{pattern}' to '{engine_lang}' via .gitattributes"
                            )

        except Exception as e:
            self.logger.debug(f"GuideStar: Deep inspection failed for .gitattributes: {e}")

    # ==============================================================================
    # EVASION TACTICS (The .gitignore Scout)
    # ==============================================================================

    def _survey_gitignore(self):
        """
        Scans .gitignore for hostile force-includes (e.g., !payload.so).
        Attackers use this to bypass standard directory exclusions (like node_modules/)
        and force malicious compiled binaries into the repository.
        """
        gitignore_path = self.root / ".gitignore"
        if not gitignore_path.exists():
            return

        # The list of compiled/binary formats attackers typically try to smuggle
        hostile_bins = {".so", ".dll", ".exe", ".dylib", ".bin", ".xz", ".gz", ".zip"}

        try:
            with open(gitignore_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()

                    # We are only looking for Force-Includes
                    if line.startswith("!"):
                        # Extract the extension, ignoring path structures
                        ext = Path(line).suffix.lower()

                        if ext in hostile_bins:
                            # Strip the '!' and any leading slashes to get the clean path
                            clean_path = line[1:].strip("/")

                            self.logger.critical(
                                f"🚨 EVASION DETECTED: .gitignore is force-including a binary -> '{line}'"
                            )

                            # Apply an absolute Intent Lock (1.0).
                            # This forces Aperture.py to bypass its Dark Matter filters and
                            # sends the file directly into the X-Ray Binary Sensor!
                            self._inject_prior(
                                clean_path,
                                "unknown",
                                1.0,
                                "Hostile Gitignore Force-Include",
                            )

        except Exception as e:
            self.logger.debug(f"GuideStar: Evasion inspection failed for .gitignore: {e}")

    # ==============================================================================
    # KNOWLEDGE ANCHORS (The Documentation Scout)
    # ==============================================================================

    def _survey_knowledge_anchors(self):
        """
        Scans the repository for high-value architectural literature.
        Calculates the physical mass of the documentation to project a
        defensive umbrella shield over the surrounding directory.
        """
        anchor_patterns = {
            "README.md",
            "README.txt",
            "README.rst",
            "ARCHITECTURE.md",
            "DESIGN.md",
            "SPEC.md",
            "swagger.json",
            "openapi.yaml",
            "openapi.json",
            "CONTRIBUTING.md",
            "USAGE.md",
        }

        for root_dir, dirs, files in os.walk(self.root):
            dir_path = Path(root_dir)

            # Skip known black holes to avoid wasting I/O
            if any(part in self._gs_config.get("BLACK_HOLES", set()) for part in dir_path.parts):
                continue

            local_shield_mass = 0

            for file in files:
                if file in anchor_patterns or file.lower().endswith(".md"):
                    file_path = dir_path / file
                    try:
                        # Fetch the physical byte size of the documentation
                        size_bytes = file_path.stat().st_size

                        # Ignore stubs (e.g., "# Project Title" and nothing else)
                        if size_bytes > 150:
                            local_shield_mass += size_bytes
                    except OSError:
                        pass

            if local_shield_mass > 0:
                # Calculate Shield Strength:
                # 3000+ bytes of documentation provides a 100% (1.0) shield for this folder.
                shield_strength = min(local_shield_mass / 3000.0, 1.0)

                rel_dir = str(dir_path.relative_to(self.root)).replace("\\", "/")
                if rel_dir == ".":
                    rel_dir = "__root__"

                self.doc_umbrellas[rel_dir] = round(shield_strength, 3)
                self.logger.debug(
                    f"GuideStar: Projected {shield_strength*100:.1f}% Documentation Shield over '{rel_dir}'"
                )
