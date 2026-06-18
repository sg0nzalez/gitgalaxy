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
import logging
from typing import Dict, List, Optional, Tuple, Any, TypedDict
from gitgalaxy.standards.language_standards import LENS_CONFIG, PRISM_CONFIG

# ==============================================================================
# GitGalaxy Phase 2: Structural Refractor (The Prism)
# Strategy v6.2.0 Protocol: Safe Delimiter Extraction & Singularity Bypasses
# ==============================================================================


class RefractionResult(TypedDict):
    """
    The dual-stream output of the Prism engine.

    Attributes:
        code_stream (str): The pure logic stream (Active Matter).
        comment_stream (str): The pure literature stream (Ghost Mass).
        coding_loc (int): Lines of code (non-empty, non-literature).
        doc_loc (int): Lines of literature/documentation.
    """

    code_stream: str
    comment_stream: str
    coding_loc: int
    doc_loc: int


class RefractionError(Exception):
    """Exception raised for structural failures during the Optical Split."""

    pass


class Prism:
    """
    GitGalaxy Phase 2: The Optical Split (Structural Refraction)

    PURPOSE: Performs high-fidelity structural refraction. Separates executable
    logic (Active Matter) from documentation (Ghost Mass) while preserving string literals.

    ARCHITECTURE (v6.2.0):
    1. Singularity Bypass: Respects 'undeterminable' files by leaving them whole.
    2. Dynamic Matrix: Safely compiles regex based on dynamic JSON config lengths.
    3. String Literal Masking: Prevents logic erosion in recursive block comments (Rust/Swift).
    4. Polyglot Delegation: 'lang_mix' tracking is now fully delegated to the Detector.
    """

    def __init__(
        self,
        comment_definitions: Dict[str, Any],
        language_definitions: Dict[str, Any],
        parent_logger: Optional[logging.Logger] = None,
    ):
        """Initializes the Prism hardware and pre-compiles the optical matrix."""

        # --- TELEMETRY SYNC ---
        if parent_logger:
            self.logger = parent_logger.getChild("prism")
            self.logger.setLevel(parent_logger.level)
        else:
            self.logger = logging.getLogger("prism")
            self.logger.setLevel(logging.INFO)

        self.families = comment_definitions.get("mechanical_families", {})
        self.languages = language_definitions

        self.logger.debug(
            "Initializing Prism hardware and warming up optical matrix..."
        )

        # --- TIER 1: THE STRING LITERAL SHIELD ---
        self.SHIELD_PATTERN = PRISM_CONFIG.get("SHIELD_PATTERN", "")

        # --- TIER 2: OPTICAL CALIBRATION (Regex Pre-compilation) ---
        self.PRISM_MATRIX: Dict[str, re.Pattern] = self._calibrate_matrix()

        # Phase 6.1 Handshake Registry (Synchronized securely via Universal Laws)
        self.HANDSHAKES = []
        for hs in LENS_CONFIG.get("HANDSHAKE_REGISTRY", []):
            self.HANDSHAKES.append(
                {
                    "trigger": re.compile(hs["trigger"], re.I),
                    "end": re.compile(hs["end"], re.I),
                    "target": hs["target"],
                    "pair": hs["pair"],
                }
            )

        # Performance Constants
        self.HANDSHAKE_LOOKAHEAD_LIMIT = LENS_CONFIG.get("THRESHOLDS", {}).get(
            "HANDSHAKE_LOOKAHEAD_LIMIT", 50000
        )
        self.NESTED_PEEL_LIMIT = PRISM_CONFIG.get("THRESHOLDS", {}).get(
            "NESTED_PEEL_LIMIT", 500
        )
        self.POSITIONAL_ANCHORS = PRISM_CONFIG.get(
            "POSITIONAL_ANCHORS", {"*", "C", "c", "/", "!"}
        )

        # Hardened Language Specific Extractors
        self.PYTHON_DOC_PATTERN = re.compile(
            PRISM_CONFIG.get("PYTHON_DOC_PATTERN", ""), re.M
        )
        self.PHP_HEREDOC_PATTERN = re.compile(
            PRISM_CONFIG.get("PHP_HEREDOC_PATTERN", ""), re.M
        )
        self.PHP_MULTILINE_STRING = re.compile(
            PRISM_CONFIG.get("PHP_MULTILINE_STRING", ""), re.M
        )

        self.logger.info(
            f"Prism Engine Online | Calibrated {len(self.PRISM_MATRIX)} mechanical lenses."
        )

    def refract(self, content: str, primary_lang: str) -> RefractionResult:
        """Decouples the signal into mutually exclusive streams (Logic vs Literature)."""
        if not content:
            self.logger.debug("Refraction skipped: Empty content buffer.")
            return {
                "code_stream": "",
                "comment_stream": "",
                "coding_loc": 0,
                "doc_loc": 0,
            }

        # --- THE UNPARSABLE BYPASS (Spec 2.3.4.A.1) ---
        if primary_lang in ("undeterminable", "unknown"):
            self.logger.debug(
                f"Unparsable Bypass: '{primary_lang}' signal routed to Active Matter intact."
            )
            coding_loc = len([l for l in content.split("\n") if l.strip()])
            return {
                "code_stream": content,
                "comment_stream": "",
                "coding_loc": coding_loc,
                "doc_loc": 0,
            }

        # --- THE PROSE BYPASS ---
        # Simply add "xml" to the tuple!
        if primary_lang in ("markdown", "plaintext", "xml"):
            self.logger.debug(
                f"Prose Bypass: '{primary_lang}' signal routed to Ghost Mass intact."
            )
            doc_loc = len([l for l in content.split("\n") if l.strip()])
            return {
                "code_stream": "",
                "comment_stream": content,
                "coding_loc": 0,
                "doc_loc": doc_loc,
            }

        # 1. METADATA GUARD
        header, body = self._guard_metadata_signal(content)

        # 2. STATE INITIALIZATION
        code_parts: List[str] = []
        comment_parts: List[str] = []

        try:
            # 3. THE SLIDING LOOP (Phase 6)
            # We partition the file so embedded languages get their native comment lens applied.
            segments = self._partition_segments(body, primary_lang)

            if len(segments) > 1:
                self.logger.info(
                    f"Multi-language file detected in [{primary_lang}]. - Engaging dynamic language lens swap across {len(segments)} distinct file sections."
                )

            for lang_id, segment_text in segments:
                family = self.languages.get(lang_id, {}).get("lexical_family", "std_c")
                self.logger.debug(
                    f"Refracting segment [{lang_id}] using optical family '{family}'..."
                )

                # Refract the segment
                seg_code, seg_comments = self._refract_segment(
                    segment_text, lang_id, family
                )

                code_parts.append(seg_code)
                comment_parts.append(seg_comments)

            # 4. OUTPUT SYNTHESIS
            final_code = header + "".join(code_parts)
            final_comments = "\n".join(comment_parts).strip()

            # --- THE FIX: Prevent the "Inline Comment Double-Dip" ---
            # 1. Count the total non-blank lines in the original un-split file
            total_active_lines = len([l for l in content.split("\n") if l.strip()])

            # 2. Count the pure coding lines
            coding_loc = len([l for l in final_code.split("\n") if l.strip()])

            # 3. Derive the documentation lines by subtracting code from the active total.
            # This forces mutual exclusivity: if a line has code and a comment, it counts as Code.
            doc_loc = max(0, total_active_lines - coding_loc)

            self.logger.debug(
                f"Refraction Complete: {coding_loc} Active LOC | {doc_loc} Ghost LOC."
            )

            return {
                "code_stream": final_code,
                "comment_stream": final_comments,
                "coding_loc": coding_loc,
                "doc_loc": doc_loc,
            }

        except Exception as e:
            self.logger.error(
                f"Catastrophic structural failure during optical split: {e}",
                exc_info=True,
            )
            raise RefractionError(f"Prism failure: {e}")

    def _refract_segment(self, text: str, lang_id: str, family: str) -> Tuple[str, str]:
        """Surgically strips literature from a single segment using pre-compiled lenses."""
        if family == "nested_c":
            code, lits = self._refract_nested(text)
            return code, "\n".join(lits)

        if family == "positional":
            return self._refract_positional(text)

        # Retrieve the pre-compiled pattern (Zero redundant compilation)
        pattern = self.PRISM_MATRIX.get(family)
        if not pattern:
            self.logger.debug(
                f"No pre-compiled lens for family '{family}'. Returning unrefracted."
            )
            return text, ""

        lits = []

        def callback(m: re.Match) -> str:
            if m.group(1):
                # Shielded Literal Hit (e.g. String containing a URL)
                return m.group(1)
            if m.group(2):
                # Literature Hit (Comment)
                lits.append(m.group(2).strip())
            return ""

        code = pattern.sub(callback, text)

        # Hardened Python Post-Processing
        if lang_id in ("python", "micropython", "ruby"):
            code, extra_lits = self._strip_python_docstrings(code)
            if extra_lits:
                self.logger.debug(
                    f"Post-processor extracted {len(extra_lits)} standalone docstrings."
                )
            lits.extend(extra_lits)

        # ---> ADD THIS: Hardened PHP Post-Processing (Heredoc & Multi-line Strings)
        if lang_id == "php":
            code, php_lits = self._strip_php_string_mass(code)
            if php_lits:
                self.logger.debug(
                    f"Post-processor extracted {len(php_lits)} PHP Heredoc/Multi-line strings."
                )
            lits.extend(php_lits)

        return code, "\n".join(lits)

    def _calibrate_matrix(self) -> Dict[str, re.Pattern]:
        """Safely pre-compiles the standard prisms based on dynamic config lengths."""
        matrix = {}

        for fam_key, data in self.families.items():
            if fam_key in ("nested_c", "positional"):
                continue

            delims = data.get("delimiters", [])
            if not delims:
                continue

            # Secure array escape
            d = [re.escape(x) for x in delims]
            p = ""

            # Dynamically build regex based on family type and safe bounds checks
            if fam_key == "std_c" and len(d) >= 3:
                p = rf"({d[0]}[^\n]*|{d[1]}.*?{d[2]})"
            elif fam_key == "pure_hash" and len(d) >= 1:
                p = rf"({d[0]}[^\n]*)"
            elif fam_key == "hybrid_hash" and len(d) >= 3:
                p = rf"({d[1]}.*?{d[2]}|{d[0]}[^\n]*)"
            elif fam_key == "hybrid_dash" and len(d) >= 5:
                p = rf"({d[1]}.*?{d[2]}|{d[3]}.*?{d[4]}|{d[0]}[^\n]*)"
            elif fam_key == "hybrid_dash" and len(d) >= 3:  # Fallback
                p = rf"({d[1]}.*?{d[2]}|{d[0]}[^\n]*)"
            elif fam_key == "polyglot" and len(d) >= 4:
                p = rf"({d[1]}.*?{d[2]}|{d[0]}[^\n]*|{d[3]}[^\n]*)"
            elif fam_key == "polyglot" and len(d) >= 3:  # Fallback
                p = rf"({d[1]}.*?{d[2]}|{d[0]}[^\n]*)"
            elif fam_key == "singular":
                # =====================================================================
                # THE FIX: Neutralized the Zero-Width ReDoS Bomb.
                #
                # HISTORICAL CONTEXT FOR FUTURE MAINTAINERS & LLMS:
                # A previous iteration of this regex started with `(|^[ \t]...`.
                # The leading `|` (OR) without a preceding token created a zero-width
                # assertion. This told Python's `re.sub` engine that matching an "empty
                # string" was a valid success state. Consequently, `re.sub` would
                # evaluate and trigger a callback at EVERY SINGLE CHARACTER BOUNDARY
                # in the file. For a 1MB Assembly file, this caused 1,000,000 redundant
                # Python loop executions, freezing the pipeline.
                #
                # DO NOT ADD A LEADING OR TRAILING `|` TO THIS CAPTURE GROUP.
                #
                # REGEX TOKEN BREAKDOWN:
                # This pattern explicitly maps a grab-bag of legacy/singular comment
                # tokens safely. It evaluates sequentially:
                #
                # 1. `^[ \t]*%\{.*?%\}` : Matlab block comments. Matches start of line,
                #                         optional whitespace, then %{ ... %} natively.
                #                         (Relies on re.M and re.S flags applied later).
                # 2. `;[^\n]*`          : Assembly, Lisp, and INI single-line comments.
                # 3. `//[^\n]*`         : C-style single-line comments.
                # 4. `(?i)\bdnl\b[^\n]*`: M4 macro comments ("Discard to Next Line").
                #                         (?i) sets case-insensitivity, \b ensures exact
                #                         word match.
                # 5. `%[^\n]*`          : TeX and Matlab single-line comments.
                # =====================================================================
                p = r"(//[^\n]*|;[^\n]*|%[^\n]*|^[ \t]*%\{.*?%\}|(?i)\bdnl\b[^\n]*)"

            if p:
                try:
                    # ---> THE FIX: Strip any rogue inline flags injected by the config <---
                    p = p.replace("(?i)", "").replace("(?m)", "").replace("(?s)", "")
                    full_pattern = f"{self.SHIELD_PATTERN}|{p}"

                    flags = re.S | re.M
                    if fam_key == "singular":
                        flags |= re.IGNORECASE

                    matrix[fam_key] = re.compile(full_pattern, flags)
                    self.logger.debug(
                        f"Optical matrix calibrated for family: {fam_key}"
                    )
                except re.error as e:
                    self.logger.error(
                        f"Regex compilation failed for family '{fam_key}': {e}"
                    )

        return matrix

    def _strip_python_docstrings(self, text: str) -> Tuple[str, List[str]]:
        """Hardened extraction for standalone triple-quoted literature blocks (O(N) Single Pass)."""
        docs = []

        def callback(m: re.Match) -> str:
            docs.append(m.group(0).strip())
            return "\n"

        clean = self.PYTHON_DOC_PATTERN.sub(callback, text)
        return clean, docs

    def _strip_php_string_mass(self, text: str) -> Tuple[str, List[str]]:
        """Surgically extracts PHP Heredoc and multi-line strings to prevent structural hallucinations."""
        lits = []

        def capture_lit(m: re.Match) -> str:
            # Save the literal into the Ghost Mass stream
            lits.append(m.group(0).strip())
            # Replace with a safe, empty string literal to preserve PHP array syntax
            return '""'

        # 1. Extract Heredoc/Nowdoc
        text = self.PHP_HEREDOC_PATTERN.sub(capture_lit, text)

        # 2. Extract massive Multi-line Strings
        text = self.PHP_MULTILINE_STRING.sub(capture_lit, text)

        return text, lits

    def _partition_segments(
        self, content: str, primary_id: str
    ) -> List[Tuple[str, str]]:
        """Splits content into language segments based on handshake triggers."""
        segments = []
        last_idx = 0

        triggers = []
        # --- FAST PATH: The Universal Web Tax Shield ---
        # Bypasses expensive case-insensitive regex scans unless the trigger literal is actually present.
        content_lower = None

        for h in self.HANDSHAKES:
            # Extract a reliable literal hint (e.g., 'script', 'style', 'asm')
            hint = (
                h["trigger"]
                .pattern.lower()
                .replace("\\s*", "")
                .replace("\\b", "")
                .replace("__", "")
                .split("<")[-1]
                .split("(")[0]
                .split("!")[0]
                .strip()
            )

            if len(hint) >= 3:
                if content_lower is None:
                    content_lower = content.lower()  # One fast C-level allocation
                if hint not in content_lower:
                    continue  # Skip the expensive regex entirely!

            for m in h["trigger"].finditer(content):
                triggers.append(
                    {
                        "start": m.start(),
                        "end_pattern": h["end"],
                        "target": h["target"],
                        "pair": h["pair"],
                        "trigger_end": m.end(),
                    }
                )

        triggers.sort(key=lambda x: x["start"])

        for t in triggers:
            if t["start"] < last_idx:
                continue

            self.logger.debug(
                f"Handshake Trigger: Alien segment '{t['target']}' discovered at offset {t['start']}."
            )

            if t["start"] > last_idx:
                segments.append((primary_id, content[last_idx : t["start"]]))

            if t["pair"]:
                open_char, close_char = t["pair"]
                end_idx = self._find_balanced_end(
                    content, t["start"], open_char, close_char
                )
            else:
                search_limit = min(
                    t["trigger_end"] + self.HANDSHAKE_LOOKAHEAD_LIMIT, len(content)
                )
                end_match = t["end_pattern"].search(
                    content, pos=t["trigger_end"], endpos=search_limit
                )
                end_idx = end_match.end() if end_match else len(content)
                if not end_match and end_idx == search_limit:
                    self.logger.warning(
                        "Lens Scope Guard: Failed to find closure within limit. Forcing clip."
                    )

            segments.append((t["target"], content[t["start"] : end_idx]))
            last_idx = end_idx

        if last_idx < len(content):
            segments.append((primary_id, content[last_idx:]))

        return segments if segments else [(primary_id, content)]

    def _find_balanced_end(
        self, text: str, start_pos: int, opener: str, closer: str
    ) -> int:
        """Balanced scoping implementation for paired-bracket alien segments."""
        depth = 0
        in_string: Optional[str] = None
        limit = min(start_pos + self.HANDSHAKE_LOOKAHEAD_LIMIT, len(text))

        i = start_pos
        while i < limit:
            char = text[i]

            # 1. EXACT Escape Handling
            if char in ('"', "'", "`"):
                # Count consecutive backslashes preceding the quote
                bs_count = 0
                j = i - 1
                while j >= start_pos and text[j] == "\\":
                    bs_count += 1
                    j -= 1

                # If backslashes are EVEN, the quote is real. If ODD, it is escaped.
                if bs_count % 2 == 0:
                    if not in_string:
                        in_string = char
                    elif in_string == char:
                        in_string = None

            # 2. Scope Tracking (Only active when NOT trapped inside a string)
            elif not in_string:
                if char == opener:
                    depth += 1
                elif char == closer:
                    depth -= 1
                    if depth <= 0:
                        self.logger.debug(
                            f"Balanced scoping closed at offset +{i - start_pos} chars."
                        )
                        return i + 1

            i += 1

        self.logger.warning(
            f"Lens Scope Guard: Failed to find balanced '{opener}{closer}'. Forcing closure."
        )
        return limit

    def _refract_nested(self, text: str) -> Tuple[str, List[str]]:
        """
        While-Peel loop for recursively nested block comments (e.g. Rust/Swift/Scala).
        Hardened with active string-masking to prevent logic erosion.
        """
        delims = self.families.get("nested_c", {}).get("delimiters", ["//", "/*", "*/"])
        if len(delims) < 3:
            return text, []

        s_line, b_start, b_end = delims[0], delims[1], delims[2]
        lits = []

        # 1. Protect Strings via Safe Masking
        # Masking prevents the `.rfind` mathematical loop from tearing apart string literals
        shield = re.compile(self.SHIELD_PATTERN, re.S | re.M)
        string_cache = {}

        def _shield_replacer(m: re.Match) -> str:
            if m.group(1):
                key = f"__GALAXY_STR_MASK_{len(string_cache)}__"
                string_cache[key] = m.group(1)
                return key
            return ""

        protected_code = shield.sub(_shield_replacer, text)

        # --- FAST O(1) UNMASKING ROUTINE ---
        def unmask(chunk: str) -> str:
            if "__GALAXY_STR_MASK_" not in chunk:
                return chunk
            # Instantly find masks via regex and retrieve the original string via O(1) dictionary lookup
            return re.sub(
                r"__GALAXY_STR_MASK_\d+__",
                lambda match: string_cache.get(match.group(0), match.group(0)),
                chunk,
            )

        # 2. Peel single-line comments safely
        s_line_pattern = re.compile(rf"{re.escape(s_line)}[^\n]*")

        def single_callback(m: re.Match) -> str:
            comment = m.group(0)
            lits.append(unmask(comment).strip())
            return ""

        protected_code = s_line_pattern.sub(single_callback, protected_code)

        # 3. Iteratively peel nested blocks from the inside out
        safety = 0
        while b_start in protected_code and safety < self.NESTED_PEEL_LIMIT:
            end_match = re.search(re.escape(b_end), protected_code)
            if not end_match:
                break

            start_idx = protected_code.rfind(b_start, 0, end_match.start())
            if start_idx == -1:
                break

            block_content = protected_code[start_idx : end_match.end()]

            # Unmask any strings safely captured within the comment block using O(1) lookup
            lits.append(unmask(block_content).strip())

            # Remove from logic stream
            protected_code = (
                protected_code[:start_idx] + protected_code[end_match.end() :]
            )
            safety += 1

        if safety >= self.NESTED_PEEL_LIMIT:
            self.logger.warning(
                f"Nested Peel Guard triggered: Reached max iteration limit ({self.NESTED_PEEL_LIMIT})."
            )

        # 4. Final Logic Unmasking
        return unmask(protected_code), lits

    def _refract_positional(self, text: str) -> Tuple[str, str]:
        """Column-anchored and Inline stripping for legacy species (COBOL/Fortran)."""
        code, lits = [], []

        for line in text.split("\n"):
            # 1. Legacy Column-1 or Column-7 anchors (Fixed Form)
            if (len(line) >= 1 and line[0] in self.POSITIONAL_ANCHORS) or (
                len(line) >= 7 and line[6] in self.POSITIONAL_ANCHORS
            ):
                lits.append(line)
                continue

            # 2. Modern Inline Fortran (!) and COBOL (*>) comments
            if "*>" in line:
                parts = line.split("*>", 1)
                code.append(parts[0])
                lits.append("*>" + parts[1])
            elif "!" in line:
                parts = line.split("!", 1)
                code.append(parts[0])
                lits.append("!" + parts[1])
            else:
                code.append(line)

        return "\n".join(code), "\n".join(lits)

    def _guard_metadata_signal(self, content: str) -> Tuple[str, str]:
        """Protects shebangs and preprocessor headers from the stripping engine."""
        lines = content.split("\n", 1)
        if not lines:
            return "", ""

        first = lines[0]
        # Explicit guard for #! and early PHP/XML execution tags
        if first.startswith(("#!", "<?php", "<?xml")):
            return first + "\n", lines[1] if len(lines) > 1 else ""

        return "", content
