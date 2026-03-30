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
import math
import hashlib
import logging
import time
from typing import Dict, List, Any, TypedDict, Optional, Tuple
from . import gitgalaxy_standards_v1 as config


# ==============================================================================
# GitGalaxy Phase 2.5 & 7.5: Logic Splicer & Cartographer
# Strategy v6.3.0 Protocol: Fluid-State Counters, Language Sliding & Semantic Modes
# ==============================================================================

class Satellite(TypedDict, total=False):
    """Metadata for a surgically extracted logic block."""
    name: str
    
    # Dual-Key mapping to ensure compatibility with all pipeline versions
    texture: str
    type_id: str
    
    loc: int
    
    branch_count: int
    branch: int
    
    args: int
    args_count: int
    
    logic_angle: float
    angle: float
    
    control_flow_ratio: float
    cf_ratio: float
    
    magnitude: float
    mag: float
    impact: float
    
    start_line: int
    end_line: int


class LogicData(TypedDict, total=False):
    """The standardized output schema for Strategy v6.2.0+ compliance."""
    equations: Dict[str, int]
    satellites: List[Satellite]
    logic_density: float
    sum_fxn_impact: float
    total_control_flow_ratio: float
    raw_imports: list  
    metadata: Dict[str, str]


# ==============================================================================
# THE OPTICAL CONFIGURATION MATRIX
# ==============================================================================

class SemanticScopeRegistry:
    """
    The Optical Calibration Matrix for GalaxyScope's Primary Detector.
    Defines the structural physics required to slice non-brace languages.
    
    - MODE D: Semantic Handshake (Depth tracking via text keywords)
    - MODE E: Terminator Cleaving (Hard slicing via line-ending tokens)
    """

    # Internal aliases to route variations to their base optical physics
    _ALIASES = {
        "bash": "shell", 
        "sh": "shell", 
        "zsh": "shell",
        "t-sql": "sql", 
        "plpgsql": "sql", 
        "mysql": "sql", 
        "psql": "sql",
        "sqlite": "sql",
        "visualbasic": "vb", 
        "vba": "vb"
    }

    DEFINITIONS = {
        # ==========================================
        # 🔴 INTEGRATION MODE D: The Handshake Stack
        # ==========================================
        "shell": {
            "mode": "mode_d",
            "openers": [
                r"\bif\b",
                r"\bwhile\b",
                r"\buntil\b",
                r"\bfor\b",
                r"\bcase\b",
                r"\{",  # Shell functions use braces for scope
            ],
            "closers": [r"\bfi\b", r"\bdone\b", r"\besac\b", r"\}"],
        },
        "ruby": {
            "mode": "mode_d",
            "openers": [
                r"(?<![:.])\bdef\b(?!:)",
                r"(?<![:.])\bclass\b(?!:)",
                r"(?<![:.])\bmodule\b(?!:)",
                r"(?<![:.])\bif\b(?!:)",
                r"(?<![:.])\bunless\b(?!:)",
                r"(?<![:.])\bwhile\b(?!:)",
                r"(?<![:.])\buntil\b(?!:)",
                r"(?<![:.])\bfor\b(?!:)",
                r"(?<![:.])\bcase\b(?!:)",
                r"(?<![:.])\bdo\b(?!:)",
                r"(?<![:.])\bbegin\b(?!:)",
            ],
            "closers": [r"(?<![:.])\bend\b(?!:)"],
        },
        "lua": {
            "mode": "mode_d",
            "openers": [
                r"\bfunction\b",
                r"\bif\b",
                r"\bwhile\b",
                r"\bfor\b",
                r"\brepeat\b",
            ],
            "closers": [r"\bend\b", r"\buntil\b"],
        },
        "elixir": {
            "mode": "mode_d",
            "openers": [
                r"\bdef\b",
                r"\bdefmodule\b",
                r"\bdefmacro\b",
                r"\bdefp\b",
                r"\bif\b",
                r"\bunless\b",
                r"\bcase\b",
                r"\bcond\b",
                r"\breceive\b",
                r"\bfn\b",
                r"\bdo\b",
            ],
            "closers": [r"\bend\b"],
        },
        "vb": {
            "mode": "mode_d",
            "openers": [
                r"\bsub\b",
                r"\bfunction\b",
                r"\bif\b",
                r"\bwhile\b",
                r"\bselect\b",
                r"\bfor\b",
                r"\bwith\b",
                r"\bproperty\b",
                r"\bclass\b",
            ],
            "closers": [r"\bend\b", r"\bnext\b", r"\bloop\b", r"\bwend\b"],
            "ignore_case": True,
        },
        # ==========================================
        # 🪓 INTEGRATION MODE E: Terminator Cleaving
        # ==========================================
        "sql": {
            "mode": "mode_e",
            "terminator": r";",
            "igniter": r"\b(SELECT|CREATE|UPDATE|DELETE|INSERT|ALTER|DROP|GRANT|REVOKE|WITH|DECLARE|TRUNCATE)\b",
        },
        "erlang": {
            "mode": "mode_e",
            "terminator": r"\.",
            "igniter": r"^[a-z_][a-zA-Z0-9_]*\s*(?:\(|->)",
        },
        "prolog": {
            "mode": "mode_e",
            "terminator": r"\.",
            "igniter": r"^[a-z_][a-zA-Z0-9_]*\s*(?:\(|:-)",
        },
    }

    @classmethod
    def get_config(cls, lang_id: str) -> Optional[dict]:
        """Resolves aliases and returns the optical physics config for the language."""
        if not lang_id:
            return None
        normalized_id = lang_id.lower()
        base_id = cls._ALIASES.get(normalized_id, normalized_id)
        return cls.DEFINITIONS.get(base_id)

    @classmethod
    def get_mode(cls, lang_id: str) -> Optional[str]:
        """Returns the specific integration mode required for the language."""
        config = cls.get_config(lang_id)
        return config["mode"] if config else None


# ------------------------------------------------------------------------------
# THE DETECTOR (Logic Splicer)
# ------------------------------------------------------------------------------

class LogicSplicer:
    """
    The GitGalaxy Logic Splicer (The Primary Detector & Function Splicer).
    
    ARCHITECTURE:
    1. Fluid State Counter: Dynamically swaps regex registries mid-file for polyglot accuracy.
    2. Bucket Continuation: Accumulates secondary language hits into the primary vector.
    3. Integration Modes: Labels (A), Braces (B), Indentation (C), Keywords (D), Terminators (E).
    """

    # --- DYNAMIC SCHEMA FETCH ---
    # Directly mirrors the central registry to prevent schema drift
    UNIVERSAL_METRICS_SCHEMA = config.RECORDING_SCHEMAS.get("SIGNAL_SCHEMA", [])
    
    HANDSHAKE_REGISTRY = [
        {"trigger": re.compile(r'<script', re.I), "end": re.compile(r'</script>', re.I), "target": "javascript", "pair": None},
        {"trigger": re.compile(r'<style', re.I), "end": re.compile(r'</style>', re.I), "target": "css", "pair": None},
        {"trigger": re.compile(r'asm!\s*\(|__asm__', re.I), "end": re.compile(r'\)'), "target": "assembly", "pair": ("(", ")")},
        ]

    def __init__(
        self, 
        lang_id: str, 
        language_definitions: Dict[str, Any],
        parent_logger: Optional[logging.Logger] = None
    ):
        if parent_logger:
            self.logger = parent_logger.getChild("splicer")
            self.logger.setLevel(parent_logger.level)
        else:
            self.logger = logging.getLogger("splicer")
            self.logger.setLevel(logging.INFO)

        self.primary_lang_id = lang_id.lower() if lang_id else "unknown"
        self.languages = language_definitions
        
        lang_config = self.languages.get(self.primary_lang_id, {})
        self.primary_rules = lang_config.get('rules', {})
        self.primary_family = lang_config.get('lexical_family', 'std_c')

        self.assembly_returns = re.compile(
            r'\b(?:TC\s+Q|TCF\s+Q|RETURN|RESUME|RELINT|RET|RTS|JMP\s+LR|BLR|END-PERFORM|END-IF|GOBACK|EXIT)\b', 
            re.IGNORECASE
        )

        self.CORE_MAPPING = {
            "branching": "branch",
            "io_ops": "io",
            "safety": "safety",
            "danger": "danger",
            "concurrency": "concurrency",
            "logic_flux": "flux"
        }
        
        self.MAX_SATELLITES = 250  
        self.MAX_DEPTH = 50 
        self.HANDSHAKE_LOOKAHEAD_LIMIT = 50000
        
        if self.primary_lang_id not in self.languages or 'rules' not in self.languages.get(self.primary_lang_id, {}):
            try:
                from .gitgalaxy_standards_v1 import LANGUAGE_DEFINITIONS
                self.languages = LANGUAGE_DEFINITIONS
                self.logger.warning(f"[AUTO-HEAL] Re-injected LANGUAGE_DEFINITIONS for '{self.primary_lang_id}'")
            except ImportError:
                pass

    def splice(self, code_stream: str, comment_stream: str, confidence: float = 1.0, profile_regex: bool = False) -> Dict[str, Any]:
        """Executes the structural regex pass over refracted code streams."""
        regex_telemetry = {}
        t_start = time.time()
        
        # We always extract the metadata first, even for Dark Matter files
        ghost_meta = self._decode_comment_stream(comment_stream)

        # ---> THE ECOSYSTEM GRAVITY OVERRIDE <---
        # If the broader ecosystem safely locked a contested file (like a .h header) 
        # into a C-family language, we trust the gravity and artificially boost the confidence.
        # This prevents pure-macro headers from falling below the 0.42 floor and vanishing into Dark Matter.
        if self.primary_lang_id in ["c", "cpp", "objective-c"]:
            confidence = 1.0
        
        # 1. The Custom Singularity Bypass & Prose Deflection
        # Rejects unverified artifacts AND English text files before wasting compute
        if confidence < 0.42 or self.primary_lang_id in ("plaintext", "markdown"):
            self.logger.debug(f"[DIAGNOSTIC] Bypass triggered (Conf: {confidence:.2f} | Lang: {self.primary_lang_id}). Relegating to Dark Matter/Ghost Mass.")
            return {
                "equations": {}, 
                "satellites": [], 
                "logic_density": 0.0, 
                "sum_fxn_impact": 0.0, 
                "total_control_flow_ratio": 0.0, 
                "raw_imports": [],
                "metadata": ghost_meta
            }
        
        if not code_stream:
            return {
                "equations": {}, 
                "satellites": [], 
                "logic_density": 0.0, 
                "sum_fxn_impact": 0.0, 
                "total_control_flow_ratio": 0.0, 
                "raw_imports": [],
                "metadata": ghost_meta
            } 

        # --- THE ANTI-REDOS SHIELD (Line Length Limiter) ---
        # Identifies absurdly long continuous lines (Make .depend files, C hex arrays)
        # and blanks them out before they reach the regex engine. Neutralizes Catastrophic
        # Backtracking while perfectly preserving the file's geometry (mass and LOC).
        safe_lines = []
        for line in code_stream.split('\n'):
            if len(line) > 1500:
                safe_lines.append(' ' * len(line))
            else:
                safe_lines.append(line)
        code_stream = '\n'.join(safe_lines)

        try:
            line_count = sum(1 for l in code_stream.splitlines() if l.strip())

            # --- EXISTING OPTICAL PIPELINE ---
            t_part = time.time()
            segments = self._partition_segments(code_stream, self.primary_lang_id)
            
            t_eq = time.time()
            equations = self.coding_analysis(segments, regex_telemetry if profile_regex else None)
           
            equations = self.comment_analysis(comment_stream, self.primary_lang_id, equations)
            
            t_slice = time.time()
            satellites, sum_fxn_impact = self._function_slice(segments, regex_telemetry if profile_regex else None)

            branch_hits = equations.get("branch", 0)
            linear_hits = equations.get("linear", 0)
            total_control_flow_ratio = round(branch_hits / max(branch_hits + linear_hits, 1), 3)
                        
            # Use the newly standardized keys from the updated coding_analysis
            total_signals = sum(equations.values())
            logic_density = round(total_signals / line_count, 3) if line_count > 0 else 0.0

            result_payload = {
                "equations": equations,
                "satellites": satellites,
                "logic_density": logic_density,
                "sum_fxn_impact": sum_fxn_impact,
                "total_control_flow_ratio": total_control_flow_ratio,
                # THE FIX: Removed 'raw_imports' so it doesn't overwrite the worker's Phase 6 capture
                "metadata": ghost_meta
            }
            if profile_regex:
                result_payload["regex_telemetry"] = regex_telemetry
            return result_payload

        except Exception as e:
            self.logger.error(f"Catastrophic failure during structural splicing: {e}", exc_info=True)
            return {
                "equations": {}, 
                "satellites": [], 
                "logic_density": 0.0, 
                "sum_fxn_impact": 0.0, 
                "total_control_flow_ratio": 0.0, 
                "raw_imports": [],
                "metadata": ghost_meta
            }
            
    def _decode_comment_stream(self, comment_stream: str) -> Dict[str, str]:
        meta = {"ownership": "Unknown Architect"}
        if not comment_stream:
            return meta

        re_ownership = self.primary_rules.get('ownership')
        ownership_val = None
        if re_ownership:
            try:
                m_owner = re_ownership.search(comment_stream)
                if m_owner:
                    ownership_val = m_owner.group(m_owner.lastindex).strip() if m_owner.lastindex else m_owner.group(0).strip()
            except Exception: pass

        if ownership_val:
            raw_ownership = re.sub(r'<[^>]+>', '', ownership_val).strip()
            raw_ownership = raw_ownership.rstrip('.,;-')
            if raw_ownership:
                meta["ownership"] = raw_ownership

        # Look for the underscore-prefixed metadata rules
        re_purpose_line = self.primary_rules.get('_meta_purpose_line')
        re_purpose_block = self.primary_rules.get('_meta_purpose_block')
        re_boundary = self.primary_rules.get('_meta_boundary')

        if not (re_purpose_line or re_purpose_block):
            return meta

        # ---> MEMORY CAP <---
        # We only scan the top 500 lines anyway, so hard-cap the string at ~15,000 characters
        # to prevent massive license blocks or generated data from thrashing the regex engine.
        capped_stream = comment_stream[:15000]

        clean_text = re.sub(r'^[ \t]*([#/*!\-]+|[Cc][ \t]+)[ \t]*', '', capped_stream, flags=re.MULTILINE)
        lines = clean_text.splitlines()

        active_capture = None
        purpose_buffer = []
        fallback_buffer = []
        has_block_text = False

        for line in lines[:500]: 
            line_str = line.strip()

            if active_capture == "block":
                if not line_str:
                    if has_block_text:
                        break 
                    else:
                        continue 
                if re_boundary and hasattr(re_boundary, 'match') and re_boundary.match(line_str):
                    break
                purpose_buffer.append(line_str)
                has_block_text = True
                continue

            if active_capture == "line":
                if not line_str or (re_boundary and hasattr(re_boundary, 'match') and re_boundary.match(line_str)) or (re_purpose_block and hasattr(re_purpose_block, 'match') and re_purpose_block.match(line_str)):
                    active_capture = None
                else:
                    fallback_buffer.append(line_str)
                    continue

            if re_purpose_block and hasattr(re_purpose_block, 'match') and re_purpose_block.match(line_str):
                active_capture = "block"
                purpose_buffer = [] 
                has_block_text = False
                continue

            if re_purpose_line and hasattr(re_purpose_line, 'match') and not purpose_buffer:
                try:
                    m_purpose = re_purpose_line.match(line_str)
                    if m_purpose:
                        active_capture = "line"
                        purpose_text = m_purpose.group(m_purpose.lastindex).strip() if m_purpose.lastindex else m_purpose.group(0).strip()
                        if purpose_text:
                            fallback_buffer.append(purpose_text)
                except Exception: pass
                continue

        final_purpose = purpose_buffer if purpose_buffer else fallback_buffer
        if final_purpose:
            p_text = " ".join(final_purpose)
            p_text = re.sub(r'\s+', ' ', p_text).strip()
            if p_text:
                meta["purpose"] = p_text[:800] + ("..." if len(p_text) > 800 else "")

        return meta

    def _partition_segments(self, content: str, primary_id: str) -> List[Tuple[str, str, int]]:
        segments = []
        last_idx = 0
        current_line_offset = 0
        
        triggers = []
        for h in self.HANDSHAKE_REGISTRY:
            for m in h["trigger"].finditer(content):
                triggers.append({
                    "start": m.start(), 
                    "end_pattern": h["end"], 
                    "target": h["target"], 
                    "pair": h["pair"],
                    "trigger_end": m.end()
                })
        
        triggers.sort(key=lambda x: x["start"])
        
        for t in triggers:
            if t["start"] < last_idx: continue 
            
            if t["start"] > last_idx:
                chunk = content[last_idx:t["start"]]
                segments.append((primary_id, chunk, current_line_offset))
                current_line_offset += chunk.count('\n')
            
            if t["pair"]:
                open_char, close_char = t["pair"]
                end_idx = self._find_balanced_end(content, t["start"], open_char, close_char)
            else:
                search_limit = min(t["trigger_end"] + self.HANDSHAKE_LOOKAHEAD_LIMIT, len(content))
                end_match = t["end_pattern"].search(content, pos=t["trigger_end"], endpos=search_limit)
                end_idx = end_match.end() if end_match else len(content)
            
            chunk = content[t["start"]:end_idx]
            segments.append((t["target"], chunk, current_line_offset))
            current_line_offset += chunk.count('\n')
            last_idx = end_idx
            
        if last_idx < len(content):
            chunk = content[last_idx:]
            segments.append((primary_id, chunk, current_line_offset))
            
        return segments if segments else [(primary_id, content, 0)]

    def _find_balanced_end(self, safe_text: str, start_pos: int, opener: str, closer: str) -> int:
        """
        C-Optimized jump-tracking algorithm. 
        Expects 'safe_text' where string literals and comments have already been shielded.
        """
        depth = 0
        limit = min(start_pos + self.HANDSHAKE_LOOKAHEAD_LIMIT, len(safe_text))
        pos = start_pos

        while pos < limit:
            # Ask the C-engine to instantly find the next brace, bypassing Python loops
            next_open = safe_text.find(opener, pos, limit)
            next_close = safe_text.find(closer, pos, limit)

            # If there are no more closing braces, the scope is truncated/malformed. Bail out.
            if next_close == -1:
                break

            # If the opener comes next, dive one level deeper
            if next_open != -1 and next_open < next_close:
                depth += 1
                pos = next_open + 1
                
                if depth > self.MAX_DEPTH:
                    depth = self.MAX_DEPTH
            
            # If the closer comes next, surface one level
            else:
                depth -= 1
                pos = next_close + 1
                
                # We have cleanly exited the original scope
                if depth <= 0:
                    return pos
                    
        return limit

    def coding_analysis(self, segments: List[Tuple[str, str, int]], regex_telemetry: dict = None) -> Dict[str, int]: 
        # 1. THE FIX: Initialize the dictionary using the strict, ordered schema.
        # This guarantees the dictionary is exactly 51 elements long, in the exact same order every time.
        counts: Dict[str, int] = {key: 0 for key in self.UNIVERSAL_METRICS_SCHEMA}
        
        for seg_lang, seg_code, _ in segments:
            rules = self.languages.get(seg_lang, {}).get('rules', {})
            seg_len = len(seg_code)
            
            for rule_name, pattern in rules.items():
                if rule_name.startswith('_'):
                    continue
                    
                mapped_key = self.CORE_MAPPING.get(rule_name, rule_name)
                
                # 2. Prevent Hallucinations: If a rule isn't in our schema, ignore it so it doesn't break the array.
                if mapped_key not in counts:
                    self.logger.warning(f"[DIAGNOSTIC] Unregistered rule '{mapped_key}' found in '{seg_lang}'. Ignoring to preserve schema.")
                    continue
                    
                if not pattern:
                    continue
                    
                # Fast-fail for empty or useless patterns to save compute
                raw_pat = getattr(pattern, 'pattern', str(pattern))
                clean_pat = raw_pat.replace("(?i)", "").replace("(?m)", "").replace("(?s)", "").strip()
                if clean_pat in ("", "()", "(?:)", "^", "$"):
                    continue

                try:
                    # --- INJECTED DEBUG TRACE ---
                    self.logger.debug(f"[REGEX-TRACE] Evaluating rule: '{rule_name}' for language '{seg_lang}'...")
                    t_rule_start = time.perf_counter()

                    if hasattr(pattern, 'findall'): 
                        c = len(pattern.findall(seg_code))
                    else: 
                        c = len(re.findall(str(pattern), seg_code))
                    
                    # Log if a rule is dangerously slow, but didn't permanently hang
                    t_elapsed = time.perf_counter() - t_rule_start
                    
                    if regex_telemetry is not None:
                        key = f"{seg_lang}::{rule_name}"
                        # Accumulate time in case the same rule is evaluated across multiple segments
                        regex_telemetry[key] = regex_telemetry.get(key, 0.0) + t_elapsed
                    if t_elapsed > 0.5:
                        self.logger.debug(f"[REGEX-TRACE] ^-- SLOW RULE: '{rule_name}' took {t_elapsed:.4f}s")

                    # Sanity check against zero-width match blowouts
                    if c > seg_len and seg_len > 0: 
                        c = 0
                        
                    counts[mapped_key] += c
                    
                except Exception as e:
                    self.logger.error(f"[DIAGNOSTIC] Regex failure in rule '{rule_name}' for language '{seg_lang}': {e}")

            # Capture indentation signatures (only counting lines with actual content after the indent)
            counts['indent_tabs'] += len(re.findall(r'^\t+(?=\S)', seg_code, flags=re.MULTILINE))
            counts['indent_spaces'] += len(re.findall(r'^[ ]{2,}(?=\S)', seg_code, flags=re.MULTILINE))

        return counts

    def comment_analysis(self, comment_stream: str, lang_id: str, counts: Dict[str, int]) -> Dict[str, int]:
        """
        Analyzes the comment stream for developer intent, technical debt, and traceability.
        Kept strictly separated from active coding analysis to maintain Separation of Concerns.
        """
        if not comment_stream:
            return counts

        rules = self.languages.get(lang_id, {}).get('rules', {})
        
        # The specific rules designed to extract telemetry from human-readable text
        comment_rules = ["graveyard", "doc", "ownership", "planned_debt", "fragile_debt", "spec_exposure"]

        for rule_name in comment_rules:
            pattern = rules.get(rule_name)
            mapped_key = self.CORE_MAPPING.get(rule_name, rule_name)
            
            # Ensure the pattern exists and the key is safely in our 51-element schema
            if pattern and mapped_key in counts:
                try:
                    if hasattr(pattern, 'findall'):
                        c = len(pattern.findall(comment_stream))
                    else:
                        c = len(re.findall(str(pattern), comment_stream))
                    
                    counts[mapped_key] += c
                    
                except Exception as e:
                    self.logger.error(f"[DIAGNOSTIC] Comment stream regex failure in '{rule_name}': {e}")
                    
        return counts
    
    # ==============================================================================
    # PRE-PROCESSING HELPERS
    # ==============================================================================

    def _apply_literal_shield(self, text: str, lang_id: str = None) -> str:
        """
        The Smarter Atomic Literal Shield: Handles C++ Raw Strings, Python Triple Quotes,
        and safely isolates Heredocs to prevent Quote Desynchronization.
        """
        if len(text) > 500000:
            self.logger.warning(f"[DIAGNOSTIC-SHIELD] Extremely long block ({len(text)} chars). Shielding may be slow.")

        t_start = time.time()
        
        def preserve_newlines(m):
            return '""' + '\n' * m.group(0).count('\n')

        # 1. Advanced Atomic Quotes 
        # Order is critical: Check multi-char string markers before single quotes.
        # Handles Python ("""), C++ (R"(...)"), and standard strings.
        atomic_string_pattern = (
            r'""".*?"""|'                       # Python Triple Double
            r"'''.*?'''|"                       # Python Triple Single
            r'R"([a-zA-Z0-9_]*)\(.*?\)\1"|'     # C++ Raw String Literal (e.g. R"EOF(...)EOF")
            r'"(?:\\.|[^"\\])*"|'               # Standard Double
            r"'(?:\\.|[^'\\])*'|"               # Standard Single
            r'`(?:\\.|[^`\\])*`'                # Standard Backtick
        )
        text = re.sub(atomic_string_pattern, preserve_newlines, text, flags=re.DOTALL)
        t_quotes = time.time()

        t_heredoc = t_quotes
        t_pct = t_quotes

        # 2. Isolate Heredoc Logic to supported scripting languages
        if lang_id in ['ruby', 'perl', 'elixir', 'shell', 'bash']:
            
            # State-Machine for Heredocs
            lines = text.split('\n')
            shielded_lines = []
            active_heredoc_delimiter = None
            
            # In detector.py -> _apply_literal_shield
            heredoc_opener_pattern = re.compile(r'<<[-~]?\s*[\'"]?\\?([a-zA-Z_][a-zA-Z0-9_]*)[\'"]?')
                        
            for line in lines:
                if active_heredoc_delimiter:
                    if line.strip() == active_heredoc_delimiter:
                        shielded_lines.append(line)
                        active_heredoc_delimiter = None
                    else:
                        shielded_lines.append("")
                    continue

                match = heredoc_opener_pattern.search(line)
                if match:
                    delimiter = match.group(1)
                    is_standard_heredoc = (
                        '-' in match.group(0) or 
                        '~' in match.group(0) or 
                        "'" in match.group(0) or 
                        '"' in match.group(0) or 
                        delimiter.isupper()
                    )
                    if is_standard_heredoc:
                        active_heredoc_delimiter = delimiter
                
                shielded_lines.append(line)

            text = '\n'.join(shielded_lines)
            t_heredoc = time.time()

            # 3. Shield Ruby % Literals (Strictly gated to Ruby)
            if lang_id == 'ruby':
                text = re.sub(r'%[qQwWiIrxs]?\{.*?\}', preserve_newlines, text, flags=re.DOTALL)
                text = re.sub(r'%[qQwWiIrxs]?\[.*?\]', preserve_newlines, text, flags=re.DOTALL)
                text = re.sub(r'%[qQwWiIrxs]?\(.*?\)', preserve_newlines, text, flags=re.DOTALL)
                text = re.sub(r'%[qQwWiIrxs]?\|.*?\|', preserve_newlines, text, flags=re.DOTALL)
                t_pct = time.time()

        if (time.time() - t_start) > 0.5:
            self.logger.warning(
                f"[DIAGNOSTIC-SHIELD] Slow Shield Regex: {time.time() - t_start:.2f}s total "
                f"(Quotes: {t_quotes-t_start:.2f}s | Heredoc: {t_heredoc-t_quotes:.2f}s | "
                f"PCT: {t_pct-t_heredoc:.2f}s)"
            )
            
        return text

    def _extract_semantic_name(self, line: str, lang_id: str) -> str:
        """Safely extracts function/block names for Mode D logic."""
        lang_key = SemanticScopeRegistry._ALIASES.get(lang_id.lower(), lang_id.lower())
        if lang_key == 'shell':
            m = re.search(r'\bfunction\s+([a-zA-Z0-9_.-]+)', line)
            if m: return m.group(1)
            m = re.search(r'([a-zA-Z0-9_.-]+)\s*\(\)', line)
            if m: return m.group(1)
        elif lang_key in ['ruby', 'elixir']:
            m = re.search(r'\b(?:def|class|module|defmacro|defmodule|defp)\s+([a-zA-Z0-9_.:?!]+)', line)
            if m: return m.group(1)
        elif lang_key == 'lua':
            m = re.search(r'\bfunction\s+([a-zA-Z0-9_.:]+)', line)
            if m: return m.group(1)
        elif lang_key == 'vb':
            m = re.search(r'\b(?:sub|function|class|property)\s+([a-zA-Z0-9_]+)', line, re.IGNORECASE)
            if m: return m.group(1)
        return "Anonymous_Block"

    # ==============================================================================
    # THE MASTER DISPATCHER
    # ==============================================================================

    def _function_slice(self, segments: List[Tuple[str, str, int]], regex_telemetry: dict = None) -> Tuple[List[Satellite], float]:
        """The Master Routing Dispatcher: Directs the optical signal into the correct integration mode."""
        all_satellites = []
        global_impact = 0.0

        for lang_id, code, offset in segments:
            lang_config = self.languages.get(lang_id, {})
            rules = lang_config.get('rules', {})
            family = lang_config.get('lexical_family', 'std_c')
            
            optical_mode = SemanticScopeRegistry.get_mode(lang_id)
            
            t_mode_start = time.perf_counter()
            mode_name = "Unknown"
            
            if optical_mode == "mode_d":
                mode_name = "Mode_D_Keywords"
                sats, impact = self._slice_by_keywords(code, lang_id, rules, offset)
            elif optical_mode == "mode_e":
                mode_name = "Mode_E_Terminator"
                sats, impact = self._slice_by_terminator(code, lang_id, rules, offset)
            else:
                # Fallback to standard optical heuristics (Modes A, B, C)
                func_start = rules.get('func_start')
                if not func_start:
                    continue
                    
                if lang_id in ('assembly', 'agc_assembly', 'cobol', 'fortran') or family in ('singular', 'positional'):
                    mode_name = "Mode_A_Labels"
                    sats, impact = self._slice_by_labels(code, rules, offset)
                elif family in ('pure_hash', 'hybrid_hash') or lang_id in ('python', 'yaml'):
                    mode_name = "Mode_C_Indentation"
                    sats, impact = self._slice_by_indentation(code, rules, offset)
                else:
                    mode_name = "Mode_B_Braces"
                    # FIX: Pass the lexical family down so we can swap {} for ()
                    sats, impact = self._slice_by_braces(code, lang_id, rules, offset, family=family)

            # Record the telemetry if profiling is active
            if regex_telemetry is not None and mode_name != "Unknown":
                key = f"{lang_id}::Cartography_{mode_name}"
                regex_telemetry[key] = regex_telemetry.get(key, 0.0) + (time.perf_counter() - t_mode_start)

            all_satellites.extend(sats)
            global_impact += impact

            if len(all_satellites) >= self.MAX_SATELLITES:
                all_satellites = all_satellites[:self.MAX_SATELLITES]
                break

        all_satellites.sort(key=lambda x: x.get("mag", 0), reverse=True)
        return all_satellites, global_impact
    
    # ==============================================================================
    # INTEGRATION MODES (Slicers)
    # ==============================================================================

    def _slice_by_labels(self, code: str, rules: Dict[str, Any], offset: int) -> Tuple[List[Satellite], float]:
        """[INTEGRATION MODE A] - Greedy Label-Based Scan (Assembly, COBOL)."""
        satellites = []
        sum_fxn_impact = 0.0
        func_start = rules.get('func_start')

        try: matches = list(func_start.finditer(code))
        except Exception: return [], 0.0

        # --- FAST O(N) LINE TRACKER ---
        current_line_count = offset + 1
        last_counted_idx = 0

        for i, match in enumerate(matches):
            if len(satellites) >= self.MAX_SATELLITES: break

            start_idx = match.start()
            greedy_end_idx = matches[i+1].start() if i + 1 < len(matches) else len(code)
            
            sandbox = code[start_idx:greedy_end_idx]
            end_offset = len(sandbox)
            
            if self.assembly_returns:
                ret_matches = list(self.assembly_returns.finditer(sandbox))
                if ret_matches: end_offset = ret_matches[-1].end()
            
            block = code[start_idx:start_idx+end_offset].strip()
            if not block or len(block.splitlines()) < 2: continue

            raw_name = match.group(match.lastindex) if match.lastindex else match.group(0)
            if raw_name is None:
                raw_name = match.group(0)

            if any(m in raw_name for m in ["BOOST_", "TEST", "TEST_F", "TEST_CASE"]):
                raw_name = match.group(0)
                
            name = self._extract_name(raw_name)
            
            # --- FAST O(N) LINE TRACKER ---
            current_line_count += code.count('\n', last_counted_idx, start_idx)
            last_counted_idx = start_idx
            start_line = current_line_count
            
            loc = block.count('\n') + 1
            end_line = start_line + loc - 1

            sat, mag = self._process_satellite_physics(name, block, loc, start_line, end_line, rules)
            
            satellites.append(sat)
            sum_fxn_impact += mag

        return satellites, sum_fxn_impact

    def _slice_by_braces(self, code: str, lang_id: str, rules: Dict[str, Any], offset: int, family: str = 'std_c') -> Tuple[List[Satellite], float]:
        """[INTEGRATION MODE B] - Global Recursive Scope Analysis (C-Family & Lisp)."""
        satellites = []
        sum_fxn_impact = 0.0
        func_start = rules.get('func_start')
        
        if not func_start: return [], 0.0

        try: 
            matches = list(func_start.finditer(code))
        except Exception: 
            return [], 0.0

        # Dynamically set scope bounds based on lexical family
        opener = '(' if family == 'lisp_semi' else '{'
        closer = ')' if family == 'lisp_semi' else '}'

        # 1. High-Performance C-Backed Shield Function
        def fast_shield(m):
            text = m.group(0)
            if '\n' not in text: 
                return ' ' * len(text)
                
            # --- THE FIX: C-Optimized String Manipulation ---
            # Replaces the character-by-character regex grind with native split/join.
            # Instantly blanks massive Doxygen blocks without destroying line-counts.
            return '\n'.join(' ' * len(line) for line in text.split('\n'))

        # 2. The Single-Pass Lexer (Massive I/O Reduction)
        # Combines strings and comments into ONE scan to prevent memory-copy thrashing.
        if family == 'lisp_semi':
            combined_pattern = r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|`(?:\\.|[^`\\])*`|;.*|#\|.*?\|#'
        else:
            combined_pattern = r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|`(?:\\.|[^`\\])*`|//.*|/\*.*?\*/'

        safe_code = re.sub(combined_pattern, fast_shield, code, flags=re.DOTALL)

        # 3. Macro Shields (Strictly Gated to C-Family)
        if lang_id in ('c', 'cpp', 'objective-c', 'cs', 'swift'):
            # --- FAST O(N) PREPROCESSOR STATE MACHINE ---
            # Replaces the ReDoS-vulnerable regexes with a single-pass linear scanner.
            # Properly handles nested #if blocks and multi-line \ macros in OS-level codebases.
            lines = safe_code.splitlines(keepends=True)
            in_dead_branch = False
            dead_nesting_depth = 0
            in_multiline_macro = False
            
            for i in range(len(lines)):
                line = lines[i]
                stripped = line.lstrip()
                
                # A) Handle Multi-line Macro Continuation
                if in_multiline_macro:
                    lines[i] = ' ' * (len(line) - 1) + '\n' if line.endswith('\n') else ' ' * len(line)
                    if not stripped.rstrip(' \t\r\n').endswith('\\'):
                        in_multiline_macro = False
                    continue
                    
                # B) Handle Preprocessor Directives
                if stripped.startswith('#'):
                    if stripped.startswith('#if'):
                        if in_dead_branch:
                            dead_nesting_depth += 1
                    elif stripped.startswith(('#else', '#elif')):
                        if not in_dead_branch and dead_nesting_depth == 0:
                            in_dead_branch = True
                    elif stripped.startswith('#endif'):
                        if in_dead_branch:
                            if dead_nesting_depth > 0:
                                dead_nesting_depth -= 1
                            else:
                                in_dead_branch = False
                                
                    if stripped.startswith('#define'):
                        if stripped.rstrip(' \t\r\n').endswith('\\'):
                            in_multiline_macro = True
                            
                    # Always blank the directive itself to prevent floating syntax
                    lines[i] = ' ' * (len(line) - 1) + '\n' if line.endswith('\n') else ' ' * len(line)
                    continue
                    
                # C) Blank Dead Branch Content
                if in_dead_branch:
                    lines[i] = ' ' * (len(line) - 1) + '\n' if line.endswith('\n') else ' ' * len(line)

            safe_code = "".join(lines)

        last_end_idx = 0
        
        # --- FAST O(N) LINE TRACKER ---
        current_line_count = offset + 1
        last_counted_idx = 0

        for match_idx, match in enumerate(matches):
            if len(satellites) >= self.MAX_SATELLITES: break

            start_idx = match.start()
            if start_idx < last_end_idx: continue

            next_match_start = matches[match_idx + 1].start() if match_idx + 1 < len(matches) else len(code)
            search_limit = min(next_match_start, start_idx + 2000)

            # Find the opening brace/paren instantly using the shielded code
            brace_idx = safe_code.find(opener, start_idx, search_limit)
            if brace_idx == -1: continue 

            # Find the balanced end using the fast string
            end_idx = self._find_balanced_end(safe_code, brace_idx, opener, closer)
            
            # Extract the raw payload using the original code, preserving all strings/comments
            block = code[start_idx:end_idx].strip()
            if not block: continue

            raw_name = match.group(match.lastindex) if match.lastindex else match.group(0)
            if raw_name is None:
                raw_name = match.group(0)
            
            # ---> ADD THIS STEP A INTERCEPT! <---
            # If it's a test macro, pass the FULL match string (which includes the parentheses)
            if any(m in raw_name for m in ["BOOST_", "TEST", "TEST_F", "TEST_CASE"]):
                raw_name = match.group(0)

            name = self._extract_name(raw_name)

            # --- FAST O(N) LINE TRACKER ---
            # Only count the newlines since the last match, preventing O(N^2) quadratic scanning
            current_line_count += code.count('\n', last_counted_idx, start_idx)
            last_counted_idx = start_idx
            start_line = current_line_count
            
            loc = block.count('\n') + 1
            end_line = start_line + loc - 1

            sat, mag = self._process_satellite_physics(name, block, loc, start_line, end_line, rules)
            
            satellites.append(sat)
            sum_fxn_impact += mag
            
            last_end_idx = end_idx

        return satellites, sum_fxn_impact

    def _slice_by_indentation(self, code: str, rules: Dict[str, Any], offset: int) -> Tuple[List[Satellite], float]:
        """[INTEGRATION MODE C] - Density Stratification (Python, YAML)."""
        satellites = []
        sum_fxn_impact = 0.0
        func_start = rules.get('func_start')
        
        if not func_start: return [], 0.0

        # 1. Apply the Index-Aligned Shield
        # Preserves exact character indices and newline counts so safe_code maps 1:1 with code.
        def index_aligned_shield(m):
            text = m.group(0)
            return ''.join('\n' if c == '\n' else ' ' for c in text)

        # Shield Python triple-quotes first to prevent inner-quote collisions
        safe_code = re.sub(r'\"\"\"(.*?)\"\"\"', index_aligned_shield, code, flags=re.DOTALL)
        safe_code = re.sub(r"\'\'\'(.*?)\'\'\'", index_aligned_shield, safe_code, flags=re.DOTALL)
        
        # Shield standard strings
        safe_code = re.sub(r'"(?:\\.|[^"\\])*"', index_aligned_shield, safe_code, flags=re.DOTALL)
        safe_code = re.sub(r"'(?:\\.|[^'\\])*'", index_aligned_shield, safe_code, flags=re.DOTALL)
        
        # Shield comments (Python and YAML use #)
        safe_code = re.sub(r'#.*', lambda m: ' ' * len(m.group(0)), safe_code)
            
        # Match against safe_code to prevent triggering on words inside docstrings!
        try: matches = list(func_start.finditer(safe_code))
        except Exception: return [], 0.0

        last_end_idx = 0
        
        # --- FAST O(N) LINE TRACKER ---
        current_line_count = offset + 1
        last_counted_idx = 0

        for match in matches:
            if len(satellites) >= self.MAX_SATELLITES: break
            
            start_idx = match.start()
            if start_idx < last_end_idx: continue
            
            raw_name = match.group(match.lastindex) if match.lastindex else match.group(0)
            if raw_name is None:
                raw_name = match.group(0)
            name = self._extract_name(raw_name)
            
            # Find base indent level using the safe_code
            line_start_idx = safe_code.rfind('\n', 0, start_idx) + 1
            first_line = safe_code[line_start_idx:match.end()]
            base_indent = len(first_line) - len(first_line.lstrip())
            
            end_idx = len(safe_code)
            scan_pos = safe_code.find('\n', match.end())
            if scan_pos == -1:
                scan_pos = len(safe_code)
            else:
                scan_pos += 1
                
            # --- FAST O(N) INDENT TRACKER ---
            # Replaced O(N^2) array allocations with zero-copy index jumping
            while scan_pos < len(safe_code):
                next_nl = safe_code.find('\n', scan_pos)
                if next_nl == -1:
                    line_end = len(safe_code)
                else:
                    line_end = next_nl + 1
                
                f_line = safe_code[scan_pos:line_end]
                stripped = f_line.lstrip()
                
                if stripped:
                    current_indent = len(f_line) - len(stripped)
                    if current_indent <= base_indent:
                        end_idx = scan_pos
                        break
                        
                scan_pos = line_end
                
            last_end_idx = end_idx
            
            # Extract the raw payload using the ORIGINAL code to retain the exact physics payload
            block = code[start_idx:end_idx].strip()
            if not block or len(block.splitlines()) < 2: continue
            
            # --- FAST O(N) LINE TRACKER ---
            current_line_count += code.count('\n', last_counted_idx, start_idx)
            last_counted_idx = start_idx
            start_line = current_line_count
            
            loc = block.count('\n') + 1
            end_line = start_line + loc - 1
            
            sat, mag = self._process_satellite_physics(name, block, loc, start_line, end_line, rules)
            
            satellites.append(sat)
            sum_fxn_impact += mag

        return satellites, sum_fxn_impact

    def _slice_by_keywords(self, code: str, lang_id: str, rules: Dict[str, Any], offset: int) -> Tuple[List[Satellite], float]:
        """[INTEGRATION MODE D] - Semantic Handshake Stack (Shell, Ruby, Lua)."""
        self.logger.debug(f"[DIAGNOSTIC] Mode D: Initiating _slice_by_keywords for {lang_id}")
        config = SemanticScopeRegistry.get_config(lang_id)
        if not config:
            return self._slice_by_braces(code, rules, offset)

        flags = re.IGNORECASE if config.get("ignore_case") else 0
        open_pattern = re.compile('|'.join(config["openers"]), flags)
        close_pattern = re.compile('|'.join(config["closers"]), flags)

        satellites = []
        sum_fxn_impact = 0.0
        
        global_dust = []
        current_satellite = []
        
        stack_depth = 0
        satellite_name = "Main"
        
        # 1. Apply the comprehensive Atomic Literal Shield
        safe_code = self._apply_literal_shield(code)
        
        # ---> FAST SINGLE-PASS COMMENT STRIP <---
        # Ensures #var or #foo are not erroneously treated as comments if they are not at the start of a word.
        safe_code = re.sub(r'(^|[ \t])(?:#|--|//).*$', r'\1', safe_code, flags=re.MULTILINE)

        # 2. Split both into parallel arrays
        original_lines = code.splitlines(keepends=True)
        safe_lines = safe_code.splitlines(keepends=True)
        
        total_lines = len(original_lines)
        self.logger.debug(f"[DIAGNOSTIC] Mode D: Traversing {total_lines} lines...")

        current_line_offset = offset
        sat_start_line = offset + 1

        lang_key = SemanticScopeRegistry._ALIASES.get(lang_id.lower(), lang_id.lower())

        # 3. Zip them together. We scan the safe_line for triggers, but save the orig_line into the satellite.
        for idx, (orig_line, safe_line) in enumerate(zip(original_lines, safe_lines)):
            
            opens = len(open_pattern.findall(safe_line))
            closes = len(close_pattern.findall(safe_line))

            # The Ruby/Elixir Inline Modifier Guard
            if lang_key in ["ruby", "elixir"] and opens > 0:
                # Find all valid condition keywords on the line
                inline_mods = len(re.findall(r'(?<![:.])\b(if|unless|while|until)\b(?!:)', safe_line))
                
                if inline_mods > 0:
                    # Check if one of them is the actual start of the statement
                    if re.search(r'^\s*(?:[a-zA-Z0-9_@.\[\]]+\s*=\s*)?(?:if|unless|while|until)\b', safe_line):
                        # Subtract all EXCEPT the one that started the line
                        opens -= (inline_mods - 1)
                    else:
                        # ALL of them are trailing modifiers (e.g., `return true if x unless y`)
                        opens -= inline_mods

            net_change = opens - closes

            if stack_depth == 0:
                if net_change > 0:
                    satellite_name = self._extract_semantic_name(safe_line, lang_key)
                    current_satellite = [orig_line]
                    stack_depth += net_change
                    sat_start_line = current_line_offset + 1
                else:
                    global_dust.append(orig_line)
                    stack_depth = max(0, stack_depth + net_change) 
            else:
                current_satellite.append(orig_line)
                stack_depth += net_change
                
                # Check against MAX_DEPTH to prevent infinite saturation overflow
                if stack_depth > self.MAX_DEPTH:
                    self.logger.warning(f"[DIAGNOSTIC] Mode D: Max depth ({self.MAX_DEPTH}) exceeded in {satellite_name}. Clamping.")
                    stack_depth = self.MAX_DEPTH
                
                if stack_depth <= 0:
                    block = '\n'.join(current_satellite).strip()
                    if block:
                        loc = max(len(current_satellite), 1)
                        sat_end_line = current_line_offset + 1
                        sat, mag = self._process_satellite_physics(satellite_name, block, loc, sat_start_line, sat_end_line, rules)
                        satellites.append(sat)
                        sum_fxn_impact += mag
                        
                    current_satellite = []
                    satellite_name = "Main"
                    stack_depth = 0
            
            current_line_offset += 1

        self.logger.debug(f"[DIAGNOSTIC] Mode D: Finished traversing. Processing remnants...")

        if stack_depth > 0 and current_satellite:
            block = '\n'.join(current_satellite).strip()
            if block:
                loc = max(len(current_satellite), 1)
                sat, mag = self._process_satellite_physics(satellite_name + "_[Truncated]", block, loc, sat_start_line, current_line_offset, rules)
                satellites.append(sat)
                sum_fxn_impact += mag

        if global_dust and ''.join(global_dust).strip():
            block = '\n'.join(global_dust).strip()
            if block:
                loc = max(len(global_dust), 1)
                sat, mag = self._process_satellite_physics("__global_context__", block, loc, offset + 1, current_line_offset, rules)
                satellites.append(sat)
                sum_fxn_impact += mag

        self.logger.debug(f"[DIAGNOSTIC] Mode D: Extracted {len(satellites)} satellites.")
        return satellites, sum_fxn_impact
    
    def _slice_by_terminator(self, code: str, lang_id: str, rules: Dict[str, Any], offset: int) -> Tuple[List[Satellite], float]:
        """[INTEGRATION MODE E] - Terminator Cleaving (SQL, Erlang, Prolog)."""
        config = SemanticScopeRegistry.get_config(lang_id)
        if not config:
            return self._slice_by_braces(code, rules, offset)

        terminator_pattern = re.compile(config["terminator"])
        igniter_pattern = re.compile(config["igniter"], re.IGNORECASE)

        satellites = []
        sum_fxn_impact = 0.0
        current_satellite = []
        satellite_name = "Declarative_Block"
        
        is_orbiting = False
        sat_start_line = offset + 1
        current_line_offset = offset

        # 1. Apply the shield to the ENTIRE string, preserving newline counts.
        # This prevents multi-line strings from collapsing the parallel line iteration.
        def preserve_newlines(m):
            return '""' + '\n' * m.group(0).count('\n')

        safe_code = re.sub(r'"(?:\\.|[^"\\])*"', preserve_newlines, code, flags=re.DOTALL)
        safe_code = re.sub(r"'(?:\\.|[^'\\])*'", preserve_newlines, safe_code, flags=re.DOTALL)
        safe_code = re.sub(r"`(?:\\.|[^`\\])*`", preserve_newlines, safe_code, flags=re.DOTALL)

        # ---> FAST SINGLE-PASS COMMENT STRIP <---
        # Execute the regex once globally. Prevents 500,000+ regex calls on massive SQL dumps.
        safe_code = re.sub(r'(--|%).*$', '', safe_code, flags=re.MULTILINE)

        # 2. Split both into parallel arrays
        original_lines = code.splitlines(keepends=True)
        safe_lines = safe_code.splitlines(keepends=True)

        # 3. Zip them together. We scan the safe_line for igniters/terminators, 
        # but save the orig_line into the satellite block.
        for orig_line, safe_line in zip(original_lines, safe_lines):
            current_line_offset += 1

            if not safe_line.strip() and not is_orbiting:
                sat_start_line = current_line_offset + 1
                continue

            # Check for block ignition
            if not is_orbiting:
                is_orbiting = True
                match = igniter_pattern.search(safe_line)
                if match:
                    lang_key = SemanticScopeRegistry._ALIASES.get(lang_id.lower(), lang_id.lower())
                    satellite_name = f"{match.group(1).upper()}_Statement" if 'sql' in lang_key else match.group(0).strip()
                    satellite_name = re.sub(r'[^a-zA-Z0-9_]', '', satellite_name)

            # Build the block using the unaltered original line
            current_satellite.append(orig_line)

            # The Guillotine Drop (Evaluate the safe_line for the terminator)
            if terminator_pattern.search(safe_line):
                block = '\n'.join(current_satellite).strip()
                if block:
                    loc = max(len(current_satellite), 1)
                    sat_end_line = current_line_offset
                    sat, mag = self._process_satellite_physics(satellite_name, block, loc, sat_start_line, sat_end_line, rules)
                    satellites.append(sat)
                    sum_fxn_impact += mag
                
                # Reset for the next orbit
                current_satellite = []
                satellite_name = "Declarative_Block"
                is_orbiting = False
                sat_start_line = current_line_offset + 1

        # Process Remnants (Unterminated blocks at the end of the file)
        if current_satellite and ''.join(current_satellite).strip():
            block = '\n'.join(current_satellite).strip()
            if block:
                loc = max(len(current_satellite), 1)
                sat, mag = self._process_satellite_physics(satellite_name + "_[Unterminated]", block, loc, sat_start_line, current_line_offset, rules)
                satellites.append(sat)
                sum_fxn_impact += mag

        return satellites, sum_fxn_impact


    # ==============================================================================
    # SHARED SATELLITE PHYSICS ENGINE
    # ==============================================================================

    def _process_satellite_physics(self, name: str, block: str, loc: int, start_line: int, end_line: int, rules: Dict[str, Any]) -> Tuple[Satellite, float]:
        branch_pattern = rules.get('branch')
        linear_pattern = rules.get('linear')
        args_pattern = rules.get('args')
        
        branch_hits = 0
        if branch_pattern:
            if hasattr(branch_pattern, 'findall'): branch_hits = len(branch_pattern.findall(block))
            else: branch_hits = len(re.findall(str(branch_pattern), block))
            
        linear_hits = 0
        if linear_pattern:
            if hasattr(linear_pattern, 'findall'): linear_hits = len(linear_pattern.findall(block))
            else: linear_hits = len(re.findall(str(linear_pattern), block))

        total_hits = branch_hits + linear_hits
        
        # --- Updated Math Variables ---
        control_flow_ratio = branch_hits / max(total_hits, 1)
        control_flow_ratio = max(0.0, min(control_flow_ratio, 1.0))
        angle = 22.5 + (1.0 - control_flow_ratio) * 67.5

        args_count = 0
        if args_pattern and hasattr(args_pattern, 'search'):
            try:
                arg_match = args_pattern.search(block)
                if arg_match:
                    args_str = arg_match.group(arg_match.lastindex) if arg_match.lastindex else arg_match.group(0)
                    if args_str and args_str.strip() != '()':
                        if ',' in args_str:
                            args_count = args_str.count(',') + 1
                        else:
                            # Handle space-separated arguments (Lisp/Scheme/Shell)
                            args_count = len(args_str.strip().split())
            except Exception: pass

        texture_str = self._classify_function(name, block, rules)

        # ---> THE FIX 1: SIGNAL-ANCHORED LOC <---
        # Cap the 'weight-bearing' lines to 10x the number of actual logic signals.
        # A massive dictionary with 0 signals shrinks to an effective_loc of 10.
        total_signals = branch_hits + linear_hits + args_count
        effective_loc = min(loc, (total_signals + 1) * 10)

        # ---> THE FIX 2: SUB-LINEAR ARGUMENT DAMPENER <---
        # Apply a square root to the arguments to prevent combinatorial mass explosions
        # on edge-case mega-functions, while preserving the core physics philosophy.
        arg_multiplier = math.sqrt(args_count + 1)

        # Calculate magnitude using the dampened arguments and logic-bounded length
        magnitude = float((branch_hits + 1) * arg_multiplier + (0.05 * effective_loc))

        sat: Satellite = {
            "name": name[:40], 
            "texture": texture_str, 
            "type_id": texture_str,
            "loc": loc,
            "branch_count": branch_hits,
            "branch": branch_hits,
            "args": args_count,
            "args_count": args_count,
            "logic_angle": round(angle, 2),
            "angle": round(angle, 2),
            "control_flow_ratio": round(control_flow_ratio, 3),
            "cf_ratio": round(control_flow_ratio, 3),
            "magnitude": round(magnitude, 1),
            "mag": round(magnitude, 1),
            "impact": round(magnitude, 1), 
            "start_line": start_line,
            "end_line": end_line
        }
        return sat, magnitude

    def _extract_name(self, raw_match: str) -> str:
        """Safely extracts the function name by isolating the last valid alphanumeric word before parameters."""
        match_strip = raw_match.strip()
        
        # 1. Objective-C Method Extraction
        if match_strip.startswith('-') or match_strip.startswith('+'):
            clean_objc = re.sub(r'^[-+]\s*(?:\([^)]+\))?\s*', '', match_strip)
            clean_objc = clean_objc.split(':')[0].split('(')[0].split('{')[0].strip()
            words = [w for w in re.findall(r'[a-zA-Z0-9_.-]+', clean_objc) if w.strip('_-')]
            return words[0] if words else "Unknown_Sat"

        # --- 1.5 C++ OPERATOR SHIELD ---
        # Safely extract overloaded C++ operators before standard extraction destroys the symbols.
        if "operator" in match_strip:
            # Matches operator symbols, (), [], or type casts like 'operator bool'
            op_match = re.search(r'\b(operator\s*(?:\[\s*\]|\(\s*\)|[^a-zA-Z0-9_\s({]+|[a-zA-Z_]\w*(?:\s*\*+)?))', match_strip)
            if op_match:
                op_str = op_match.group(1).strip()
                # If it's a symbolic operator (<<, ==, ++, ()), remove all spaces: 'operator <<' -> 'operator<<'
                if not re.search(r'[a-zA-Z]', op_str[8:]): 
                    return re.sub(r'\s+', '', op_str)
                else: # It's a cast like 'operator int', ensure single spacing
                    return re.sub(r'\s+', ' ', op_str)

        # 2. C-Style ARGS Macro Shield
        clean = re.sub(r'\b(?:ARGS\d+|NOARGS)\b', '', raw_match)      
        
        # ---> 2.5 C++ TEST MACRO SHIELD <---
        # Extracts the actual test name from BOOST_AUTO_TEST_CASE(MyTest) or GTest's TEST(Suite, MyTest)
        macro_match = re.search(r'(?:BOOST_[A-Z_]+|TEST|TEST_F|TEST_CASE)\s*\(\s*([a-zA-Z0-9_]+)', match_strip)
        if macro_match:
            return macro_match.group(1) 
         
        # 3. Standard Extraction
        if "$(" in clean: 
            # Makefile Shield: Do not split variables by parenthesis
            clean = clean.split(':')[0].strip()
        else:
            # ---> THE C++ SCOPE SHIELD <---
            # Hide the double-colon so the single-colon guillotine doesn't see it
            clean = clean.replace('::', '__SCOPE__')
            clean = clean.split('(')[0].split('{')[0].split(':')[0].strip()
            # Restore the double-colon
            clean = clean.replace('__SCOPE__', '::')
        
        # Allow standard characters, plus Makefiles ($/%), and C++ Scopes (:)
        words = [w for w in re.findall(r'[a-zA-Z0-9_./%$()-:]+', clean) if w.strip('_-:')]
        
        return words[-1] if words else "Unknown_Sat"


 
    def _classify_function(self, name: str, block: str, rules: Dict[str, Any]) -> str:
        tag_match = re.search(r'[\@](?:type|gal_type)[:\s]+(\w+)', block, re.IGNORECASE)
        if tag_match: return tag_match.group(1).lower()

        name_lower = name.lower()
        if any(v in name_lower for v in ['get', 'fetch', 'load', 'read', 'query', 'select']): return 'io'
        if any(v in name_lower for v in ['set', 'write', 'save', 'update', 'delete', 'post', 'send', 'put']): return 'mutation'
        if any(v in name_lower for v in ['on', 'handle', 'click', 'submit', 'route', 'rupt', 'task']): return 'event'
        if any(v in name_lower for v in ['calc', 'compute', 'parse', 'transform', 'map', 'filter', 'reduce', 'tcf', 'ccs']): return 'logic'
        if any(v in name_lower for v in ['is', 'has', 'validate', 'check', 'ensure']): return 'check'
        if any(v in name_lower for v in ['test', 'assert', 'mock', 'stub']): return 'verification'

        danger_pattern = rules.get('danger')
        io_pattern = rules.get('io')

        if danger_pattern and hasattr(danger_pattern, 'search') and danger_pattern.search(block): return 'danger'
        if io_pattern and hasattr(io_pattern, 'search') and io_pattern.search(block): return 'io'
        
        return 'standard'

# ------------------------------------------------------------------------------
# THE CARTOGRAPHER (Phase 7.5: Spatial Positioning Engine)
# ------------------------------------------------------------------------------

class Cartographer:
    """
    Transforms a flat list of files into a deterministic 3D star map 
    following a "Fractal Fibonacci" pattern. 
    
    Groups files into Constellations (folders) and orbits them around the 
    heavy "Sun" (God Object) of each sector while maintaining satellite clearance.
    """
    
    def __init__(self, parent_logger: Optional[logging.Logger] = None):
        # --- TELEMETRY SYNC ---
        if parent_logger:
            self.logger = parent_logger.getChild("cartographer")
            self.logger.setLevel(parent_logger.level)
        else:
            self.logger = logging.getLogger("cartographer")
            self.logger.setLevel(logging.INFO)

        # --- SPATIAL CONSTANTS ---
        # Micro Angle: Stars within folders follow the classic Golden Angle
        self.MICRO_GOLDEN_ANGLE = math.pi * (3.0 - math.sqrt(5.0))  # ~2.39996 rad (~137.5 deg)
        
        # Macro Angle: Constellations follow the user-tuned 92.4 degree step
        self.MACRO_GOLDEN_ANGLE = math.radians(92.4) 
        
        # Base expansion multipliers
        self.MICRO_SPACING = 250.0   # Internal planet-to-planet density baseline
        self.MACRO_STEP_FACTOR = 1.5 # Inter-galaxy step multiplier (Center-to-Center)
        self.MAX_TILT_DEG = 15.0     # Max degrees a constellation can tilt from horizontal plane
        self.CORE_EXCLUSION_RADIUS = 600.0 # Clear center zone
        self.JITTER_MAGNITUDE = 100


    def _calculate_orbit_footprint(self, mass: float) -> float:
        """Determines the required tight clearance radius for a star based on mass."""
        visual_radius = 10 + (math.pow(max(mass, 1), 1/3) * 2) 
        clearance = 40 + (math.log2(max(mass, 2)) * 5)
        
        # Removed the p_scalar multiplier. 
        # Micro-placement will now be tight, and macro WebGPU scaling is handled safely in map_galaxy.
        return visual_radius + clearance

    def _hash_jitter(self, seed: str, amplitude: float) -> float:
        """
        Applies a deterministic pseudo-random jitter based on a filename hash.
        Ensures the same codebase generates the exact same geometry every time.
        """
        if not seed:
            return 0.0
        h = int(hashlib.md5(seed.encode('utf-8')).hexdigest()[:8], 16)
        # Map 0-0xffffffff to a normalized range of -1.0 to 1.0
        normalized = (h / 0xffffffff) * 2.0 - 1.0
        return normalized * amplitude



    def map_galaxy(self, stars: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Injects 3D coordinates using a Ray-Casting Dynamic Mask.
        Ensures galaxies wrap around previous turns of the spiral by measuring
        all previously placed obstruction circles.
        """
        if not stars:
            return []

        self.logger.info(f"Cartographer: Executing Ray-Casting Dynamic Mask packing for {len(stars)} bodies...")

        # 1. Sectorization
        sectors: Dict[str, List[Dict[str, Any]]] = {}
        for star in stars:
            path_str = star.get("path", star.get("filename", ""))
            parts = [p for p in path_str.replace("\\", "/").split("/") if p]
            sector_name = "/".join(parts[:-1]) if len(parts) > 1 else "__monolith__"
            star["constellation"] = sector_name # Saves to RAM for other reports
            if sector_name not in sectors: sectors[sector_name] = []
            sectors[sector_name].append(star)

        # 2. Hull Calculation
        sector_stats = []
        for name, items in sectors.items():
            items.sort(key=lambda x: self._get_mass(x), reverse=True)
            sun_mass = self._get_mass(items[0])
            sun_foot = self._calculate_orbit_footprint(sun_mass)
            hull_radius = sun_foot + (math.sqrt(len(items)) * self.MICRO_SPACING)
            sector_stats.append({"name": name, "stars": items, "radius": hull_radius})
            
        sector_stats.sort(key=lambda x: x["radius"], reverse=True)

# 3. DYNAMIC MASK PLACEMENT (Spatial Hashed)
        placed_circles = [[0.0, 0.0, self.CORE_EXCLUSION_RADIUS]] 
        
        # --- THE FIX: ANGULAR SPATIAL HASHING ---
        # Neutralizes the O(N^2) death-spiral. Instead of checking every folder, we divide 
        # the 360-degree map into 360 buckets. A ray only checks the exact degree it is pointing at.
        NUM_BINS = 360
        spatial_grid = [[] for _ in range(NUM_BINS)]
        
        # Put the origin exclusion zone into all buckets
        for b in range(NUM_BINS):
            spatial_grid[b].append(0)
        
        current_angle = 0.0
        prev_radius = 0.0
        prev_dist_from_center = self.CORE_EXCLUSION_RADIUS

        for i, sec in enumerate(sector_stats):
            s_name = sec["name"]
            s_stars = sec["stars"]
            sec_radius = sec["radius"]

            if i == 0:
                dist = self.CORE_EXCLUSION_RADIUS + sec_radius
                sec_x, sec_z = dist, 0.0
                current_angle = 0.0
                prev_dist_from_center = dist
            else:
                arc_step = (prev_radius + sec_radius) * self.MACRO_STEP_FACTOR
                delta_theta = arc_step / max(prev_dist_from_center, 1.0)
                current_angle += delta_theta
                
                cos_th = math.cos(current_angle)
                sin_th = math.sin(current_angle)
                max_r_intersect = self.CORE_EXCLUSION_RADIUS
                
                # --- FAST O(1) LOOKUP ---
                # Retrieve only the circles that overlap with our ray's exact degree trajectory
                ray_deg = int(math.degrees(current_angle)) % 360
                bins_to_check = [(ray_deg - 1) % 360, ray_deg, (ray_deg + 1) % 360]
                
                candidates = set()
                for b in bins_to_check:
                    candidates.update(spatial_grid[b])
                
                for idx in candidates:
                    px, pz, pr = placed_circles[idx]
                    
                    b = -2 * (px * cos_th + pz * sin_th)
                    c = (px**2 + pz**2) - (pr * self.MACRO_STEP_FACTOR)**2
                    disc = b**2 - 4*c
                    
                    if disc >= 0:
                        r2 = (-b + math.sqrt(disc)) / 2.0
                        if r2 > max_r_intersect:
                            max_r_intersect = r2
                            
                dist = max_r_intersect + sec_radius
                sec_x = dist * cos_th
                sec_z = dist * sin_th
                prev_dist_from_center = dist

            # Add to memory array
            new_idx = len(placed_circles)
            placed_circles.append([sec_x, sec_z, sec_radius])
            
            # --- REGISTER IN SPATIAL GRID ---
            # Calculate which angular slices this new constellation occupies and stash its index
            eff_pr = sec_radius * self.MACRO_STEP_FACTOR
            dist_to_center = math.hypot(sec_x, sec_z)
            center_a = math.atan2(sec_z, sec_x)
            
            if eff_pr >= dist_to_center:
                # It's huge, it overlaps the center, it goes in all bins
                for b in range(NUM_BINS): spatial_grid[b].append(new_idx)
            else:
                # Stash it only in the degrees its radius touches
                half_a = math.asin(eff_pr / dist_to_center)
                start_deg = int(math.degrees(center_a - half_a))
                end_deg = int(math.degrees(center_a + half_a))
                
                for deg in range(start_deg, end_deg + 1):
                    spatial_grid[deg % 360].append(new_idx)

            # Jitter and Tilt logic
            sec_y = self._hash_jitter(s_name, 250.0)
            tilt_mag = math.radians(self._hash_jitter(s_name + "_tilt_mag", self.MAX_TILT_DEG))
            tilt_dir = math.radians((self._hash_jitter(s_name + "_tilt_dir", 0.5) + 0.5) * 360.0)

            sun_mass = self._get_mass(s_stars[0])
            sun_foot = self._calculate_orbit_footprint(sun_mass)

            for j, star in enumerate(s_stars):
                f_name = star.get("name", star.get("filename", f"star_{j}"))
                if j == 0:
                    lx, ly, lz = 0.0, 0.0, 0.0
                else:
                    p_foot = self._calculate_orbit_footprint(self._get_mass(star))
                    local_r = sun_foot + p_foot + (math.sqrt(j) * self.MICRO_SPACING)
                    local_th = j * self.MICRO_GOLDEN_ANGLE
                    
                    bx, bz = local_r * math.cos(local_th), local_r * math.sin(local_th)
                    rot_x = bx * math.cos(tilt_dir) + bz * math.sin(tilt_dir)
                    rot_z = -bx * math.sin(tilt_dir) + bz * math.cos(tilt_dir)
                    tx, ty, tz = rot_x * math.cos(tilt_mag), rot_x * math.sin(tilt_mag), rot_z
                    lx = tx * math.cos(tilt_dir) - tz * math.sin(tilt_dir)
                    lz = tx * math.sin(tilt_dir) + tz * math.cos(tilt_dir)
                    ly = ty

                jit_x = self._hash_jitter(f_name + "_x", self.JITTER_MAGNITUDE )
                jit_y = self._hash_jitter(f_name + "_y", self.JITTER_MAGNITUDE )
                jit_z = self._hash_jitter(f_name + "_z", self.JITTER_MAGNITUDE * 4)

                star["pos_x"] = round(sec_x + lx + jit_x, 2)
                star["pos_y"] = round(sec_y + ly + jit_y, 2)
                star["pos_z"] = round(sec_z + lz + jit_z, 2)

                if "layout" not in star: star["layout"] = {}
                star["layout"]["x"], star["layout"]["y"], star["layout"]["z"] = star["pos_x"], star["pos_y"], star["pos_z"]

            prev_radius = sec_radius

        return stars



    
    def _get_mass(self, star: Dict[str, Any]) -> float:
        """Safely extracts mass regardless of which JSON version the pipeline is using."""
        if "forensics" in star:
            return float(star["forensics"].get("structural_mass", 0.0))
        return float(star.get("file_impact", star.get("sum_fxn_impact", 0.0)))
