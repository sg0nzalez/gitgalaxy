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
import time
import logging
from pathlib import Path
from typing import Tuple, Optional, Dict, List, Any, TypedDict, Union
from .gitgalaxy_standards_v011 import EXACT_FILE_MATCH, LANGUAGE_DEFINITIONS, LENS_CONFIG

# ==============================================================================
# GitGalaxy Phase 1: The Entity Census (The Linguistic Detector Chip)
# Strategy v6.2.0 Protocol: Bayesian Optics & The Trust Matrix
# ==============================================================================


class DetectorResult(TypedDict):
    """Structured Bayesian metadata for the Pipeline Orchestrator."""
    lang_id: str
    intensity: float
    family: Optional[str]
    lock_tier: Union[int, float]
    source_proof: str
    candidates: List[str]
    path: str
    lang_mix: List[Dict[str, Any]]
    loc: int
    size_bytes: int


class FocusingError(Exception):
    """Exception raised for hardware-level failures during linguistic focusing."""
    pass


class LanguageDetector:
    """
    PURPOSE: 
    Converts raw text signals and Bayesian Priors into a high-fidelity 'Identity Lock'. 
    
    ARCHITECTURE (The Trust Matrix):
    - Tier 0: Convergent Lock (Dual Evidence: Ext+Shebang, or Ext+Manifest)
    - Tier 1: Roadmap Lock (GuideStar Manifest Alignment)
    - Tier 1.5: Ecosystem Gravity Lock (Resolves Collisions via Macro-Environment)
    - Tier 2: Single Signature (Extension or Shebang alone)
    - Tier 3: Contextual Proof (GuideStar README / Folder Bias)
    - Tier 4: Discovery (Deep Space Mystery - requires high spectral density)
    """

    def __init__(
        self, 
        language_definitions: Dict[str, Any], 
        comment_definitions: Dict[str, Any], 
        parent_logger: Optional[logging.Logger] = None
    ):
        self.languages = language_definitions
        self.comment_defs = comment_definitions
        
        if parent_logger:
            self.logger = parent_logger.getChild("lens")
            self.logger.setLevel(parent_logger.level)
        else:
            self.logger = logging.getLogger("lens")
            self.logger.setLevel(logging.INFO)

        self.extension_map: Dict[str, str] = {}
        self.anchor_map: Dict[str, str] = {}
        
        # --- BAYESIAN TUNING CONSTANTS (Dynamic Fetch) ---
        self.thresholds = LENS_CONFIG.get("THRESHOLDS", {})
        self.COLLISION_FREQUENCIES = set(LENS_CONFIG.get("COLLISION_FREQUENCIES", set()))
        self.PROSE_ANCHORS = set(LENS_CONFIG.get("PROSE_ANCHORS", set()))
        
        # Compile disqualifiers on boot
        self.DISQUALIFIERS = {}
        for key, regex_str in LENS_CONFIG.get("DISQUALIFIERS", {}).items():
            self.DISQUALIFIERS[key] = re.compile(regex_str, re.M | re.I)
            
        # Compile handshake triggers on boot
        self.HANDSHAKE_REGISTRY = []
        for hs in LENS_CONFIG.get("HANDSHAKE_REGISTRY", []):
            self.HANDSHAKE_REGISTRY.append({
                "trigger": re.compile(hs["trigger"], re.I),
                "end": re.compile(hs["end"], re.I),
                "target": hs["target"],
                "pair": hs["pair"]
            })
        
        self.logger.debug("Initializing O(1) lookup maps for Linguistic Detector...")
        self._calibrate_lookup_maps()
        self.logger.debug(f"Detector Chip Online | {len(self.extension_map)} Extensions | {len(self.anchor_map)} Anchors")

    def _calibrate_lookup_maps(self):
        for lang_id, data in self.languages.items():
            for ext in data.get('extensions', []):
                self.extension_map[ext.lower()] = lang_id
            for anchor in data.get('exact_matches', []):
                self.anchor_map[anchor] = lang_id
                
            # ---> THE REGEX PRE-COMPILER <---
            if 'rules' in data:
                for rule_name, regex in data['rules'].items():
                    if isinstance(regex, str):
                        try:
                            data['rules'][rule_name] = re.compile(regex)
                        except re.error:
                            pass # Safely bypass malformed strings in external definitions
        
        for anchor in self.PROSE_ANCHORS:
            if anchor not in self.anchor_map:
                self.anchor_map[anchor] = "markdown" if anchor == "README" else "plaintext"

    def focus(self, file_path: Union[str, Path], content_sample: str = "", **kwargs) -> Tuple[str, float, Optional[str]]:
        """Legacy Support Gateway."""
        result = self.inspect(file_path, content_sample, **kwargs)
        if result['intensity'] < 0.25:
            self.logger.debug(f"Focus Loss on '{Path(file_path).name}': Intensity {result['intensity']:.2f} is purely ambiguous.")
            return "undeterminable", 0.0, None
        return result['lang_id'], result['intensity'], result['family']

    def inspect(
        self, 
        file_path: Union[str, Path], 
        content_sample: str = "",
        has_intent: bool = False,
        intent_lang: str = "",
        intent_vector: Optional[Dict[str, Any]] = None,
        ext_tally: Optional[Dict[str, int]] = None
    ) -> DetectorResult:
        
        path_obj = Path(file_path)
        name = path_obj.name
        ext = path_obj.suffix.lower()

        # =====================================================================
        # FIX: MULTI-DOT & DOTFILE RESOLUTION
        # =====================================================================
        # 1. Dotfiles (like .bashrc) shouldn't be treated as having an extension
        if name.startswith('.') and name.count('.') == 1:
            ext = ""
            
        # 2. Extract hidden true extensions (e.g. script.sh.template -> .sh)
        # ONLY extract if the final extension is a known, safe wrapper.
        else:
            SAFE_WRAPPERS = {'.template', '.tmpl', '.bak', '.old', '.orig', '.dist', '.gen', '.in'}
            if (ext not in self.extension_map or ext in SAFE_WRAPPERS) and len(path_obj.suffixes) > 1:
                 if ext in SAFE_WRAPPERS:
                        for middle_ext in reversed(path_obj.suffixes[:-1]):
                            if middle_ext.lower() in self.extension_map:
                                ext = middle_ext.lower()
                                self.logger.debug(f"[{name}] Extracted hidden extension '{ext}' from wrapper")
                                break

        if not intent_vector and has_intent:
            intent_vector = {"lang_id": intent_lang, "prior_confidence": 0.75, "source_proof": "Legacy Context Pass"}
            
        prior_lang = intent_vector.get("lang_id", "unknown") if intent_vector else "unknown"
        prior_conf = intent_vector.get("prior_confidence", 0.10) if intent_vector else 0.10
        prior_proof = intent_vector.get("source_proof", "Discovery") if intent_vector else "Discovery"

        result: DetectorResult = {
            "lang_id": "undeterminable",
            "intensity": 0.0,
            "family": None,
            "lock_tier": 4,
            "source_proof": "Singularity Default",
            "candidates": [],
            "path": str(file_path),
            "lang_mix": [],
            "loc": 0,
            "size_bytes": 0
        }

        if not content_sample:
            content_sample = self._capture_raw_signal(file_path)
            
        if name in EXACT_FILE_MATCH:
            return self._forge_result(
                lang_id=EXACT_FILE_MATCH[name], 
                intensity=0.95, 
                tier=2, 
                proof="Single Signature (Exact Match)", 
                base=result, 
                content_sample=content_sample
            )

        # =====================================================================
        # PRE-FLIGHT: PROSE & METADATA ANCHORS 
        # =====================================================================
        upper_stem = path_obj.stem.upper()
        
        # We explicitly add .txt and .log to the prose override list
        if ext in {'.md', '.mdx', '.rst', '.rtf', '.txt', '.log'}:
            target_id = "markdown" if ext in {'.md', '.mdx'} else "plaintext"
            return self._forge_result(target_id, self.thresholds.get("PROSE_CONFIDENCE", 0.95), 1, f"Prose Extension ({ext})", result, content_sample)
        
        # ---> THE FIX: The Code Shield <---
        # Do not allow prose hijacking if the file has a known executable extension!
        is_known_code_ext = ext in self.extension_map and ext not in {'.txt', '.md', '.log'}
        
        is_prose = False
        if not is_known_code_ext:
            # 1. Check exact match first
            is_prose = upper_stem in self.PROSE_ANCHORS    
            
            # 2. Check for prefixed/suffixed anchors (e.g., PSF_LICENSE, README-EN)
            if not is_prose:
                is_prose = any(
                    upper_stem.endswith(f"_{anchor}") or 
                    upper_stem.endswith(f"-{anchor}") or
                    upper_stem.endswith(f".{anchor}") or     
                    upper_stem.startswith(f"{anchor}_") or 
                    upper_stem.startswith(f"{anchor}-") or
                    upper_stem.startswith(f"{anchor}.")      
                    for anchor in self.PROSE_ANCHORS
                )

        target_id = None
        anchor_proof = f"Metadata Anchor ({name})"
            
        if name in self.anchor_map:
            target_id = self.anchor_map.get(name)
        elif name.split('.')[0] in self.anchor_map:
            base_anchor = name.split('.')[0]
            target_id = self.anchor_map.get(base_anchor)
            anchor_proof = f"Prefix Anchor ({base_anchor})"
        elif is_prose:
            target_id = "markdown" if "README" in upper_stem else "plaintext"
            anchor_proof = f"Prose Anchor ({path_obj.stem})"

        if target_id:
            if target_id == "undeterminable":
                target_id = "plaintext"
            return self._forge_result(target_id, self.thresholds.get("PROSE_CONFIDENCE", 0.95), 1, anchor_proof, result, content_sample)

        # 1. Gather Physical Signals
        ext_lang = self._tier_1_metadata_lock(ext, name)
        shebang_lang = self._tier_2_fingerprint_check(content_sample)

        # =========================================================================
        # THE TRUST MATRIX (Bayesian Evidence Hierarchy)
        # =========================================================================
        best_lang = "undeterminable"
        best_conf = 0.10
        lock_tier = 4
        source_proof = "Discovery"

        # TIER 0: CONVERGENT LOCK
        if ext_lang and ext_lang != "undeterminable" and shebang_lang and shebang_lang != "undeterminable" and shebang_lang == ext_lang:
            best_lang, best_conf, lock_tier, source_proof = ext_lang, 0.999, 0, "Convergent Lock (Ext + Shebang)"
        elif ext_lang and ext_lang != "undeterminable" and prior_lang == ext_lang and prior_conf >= 0.75:
            best_lang, best_conf, lock_tier, source_proof = ext_lang, 0.999, 0, f"Convergent Lock (Ext + {prior_proof})"
        elif shebang_lang and shebang_lang != "undeterminable" and prior_lang == shebang_lang and prior_conf >= 0.75:
            best_lang, best_conf, lock_tier, source_proof = shebang_lang, 0.999, 0, f"Convergent Lock (Shebang + {prior_proof})"

        # TIER 1: ROADMAP LOCK
        elif prior_conf >= 0.95 and prior_lang != "unknown":
            best_lang, best_conf, lock_tier, source_proof = prior_lang, prior_conf, 1, prior_proof
            
        # TIER 2: SINGLE SIGNATURE
        elif shebang_lang and shebang_lang != "undeterminable":
            best_lang, best_conf, lock_tier, source_proof = shebang_lang, 0.91, 2, "Single Signature (Shebang)"
        elif ext_lang and ext_lang != "undeterminable":
            best_lang, best_conf, lock_tier, source_proof = ext_lang, 0.91, 2, f"Single Signature (Ext: {ext})"
            
        # TIER 3: CONTEXTUAL PROOF
        elif prior_conf >= 0.90 and prior_lang != "unknown":
            best_lang, best_conf, lock_tier, source_proof = prior_lang, prior_conf, 3, prior_proof

        # =========================================================================
        # TIER 1.5: THE ECOSYSTEM GRAVITY LOCK (Collision Resolution)
        # =========================================================================
        gravity_lang = None
        if ext in self.COLLISION_FREQUENCIES and ext_tally and lock_tier > 0:
            gravity_lang, dominance = self._evaluate_ecosystem_gravity(ext, ext_tally)
            
            if gravity_lang:
                loc_estimate = content_sample.count('\n')
                
                # Small File Bypass OR Overwhelming Ecosystem Dominance
                if dominance >= self.thresholds.get("ECOSYSTEM_DOMINANCE_MIN", 0.70):
                    best_lang = gravity_lang
                    best_conf = 0.95  
                    lock_tier = 1.5
                    source_proof = f"Ecosystem Gravity Lock ({dominance*100:.0f}% Anchor Share)"
                    self.logger.debug(f"[{name}] Fast-tracked via Ecosystem Gravity -> {gravity_lang}")
                    
        # =========================================================================
        # TIER 1.7: THE EXO-SPECIES FALLBACK (Unknown Extension Trust)
        # =========================================================================
        is_known_ext = ext in self.extension_map
        if ext and not is_known_ext and lock_tier == 4:
            clean_ext = ext.lstrip('.').lower()
            if 0 < len(clean_ext) <= 12 and clean_ext.isalnum():
                best_lang = clean_ext
                best_conf = 0.95
                lock_tier = 1.7
                source_proof = f"Exo-Species Fallback (Ext: {ext})"
                self.logger.debug(f"[{name}] Exo-Species Fallback -> '{best_lang}'")

        # =========================================================================
        # MANDATORY SPECTRAL VERIFICATION
        # =========================================================================
        
        needs_spectral = (best_conf < self.thresholds.get("INTENSITY_FLOOR", 0.78)) or (ext in self.COLLISION_FREQUENCIES and lock_tier > 2)
        
        if needs_spectral:
            self.logger.debug(f"[{name}] Claim Unverified ({best_lang} at Tier {lock_tier}). Engaging Spectral Verification.")
            
            if lock_tier == 4 and best_lang in ("undeterminable", "unknown"):
                coding_loc = max(content_sample.count('\n') + (1 if content_sample else 0), 1)                
                spectral_id, spec_intensity = self._tier_4_deep_space_discovery(content_sample, coding_loc)
            else:
                spectral_id, spec_intensity = self._tier_3_spectral_scan(content_sample, ext, claimed_lang=best_lang, gravity_lang=gravity_lang)
            
            if spectral_id != "undeterminable":
                if spectral_id == best_lang:
                    best_conf = max(best_conf, 0.95)
                    lock_tier = 0
                    source_proof = f"Convergent Lock (Spectral Verified: {source_proof})"
                    self.logger.debug(f"[{name}] Verification Success -> {source_proof}")
                else:
                    if ext in self.COLLISION_FREQUENCIES:
                        best_lang = spectral_id
                        best_conf = max(spec_intensity + 0.10, 0.92) 
                        lock_tier = 4
                        source_proof = f"Collision Resolved ({ext} -> {spectral_id})"
                    elif lock_tier == 4:
                        if spec_intensity >= self.thresholds.get("FLOOR_TIER_4", 0.92):
                            best_lang, best_conf = spectral_id, spec_intensity
                            source_proof = f"Spectral Discovery (Passed {self.thresholds.get("FLOOR_TIER_4", 0.92)} Floor)"
                        else:
                            best_lang, best_conf = "undeterminable", spec_intensity
                            source_proof = f"Failed Discovery Floor ({spec_intensity:.2f})"
                    elif lock_tier >= 2:
                        if spec_intensity > best_conf:
                            best_lang = spectral_id
                            best_conf = spec_intensity
                            lock_tier = 4
                            source_proof = f"Spectral Override (Evidence {spec_intensity:.2f} > {source_proof})"
                        else:
                            best_conf = min(best_conf, spec_intensity)
                            source_proof += " (Unverified / Conflicted)"
            else:
                if lock_tier == 4:
                    if not ext:
                        best_lang, best_conf, lock_tier, source_proof = "plaintext", 0.70, 4, "Prose Fallback (Low Signal)"
                else:
                    source_proof += " (Unverified)"

        self.logger.debug(f"[{name}] Focus Lock -> '{best_lang}' (Tier: {lock_tier} | Conf: {best_conf:.2f})")

        if best_lang not in ("undeterminable", "plaintext", "unknown") and content_sample:
            result["lang_mix"] = self._detect_hybrids(content_sample, best_lang)

        return self._forge_result(best_lang, best_conf, lock_tier, source_proof, result, content_sample)

    def _evaluate_ecosystem_gravity(self, ext: str, ext_tally: Dict[str, int]) -> Tuple[Optional[str], float]:
        # 1. GATHER CANDIDATES
        candidates = [lid for lid, data in self.languages.items() if ext in data.get('extensions', [])]
        
        # C++ MUST be allowed to compete for .h files
        if ext == '.h' and 'cpp' not in candidates and 'cpp' in self.languages:
            candidates.append('cpp')
            
        if not candidates:
            return None, 0.0
            
        scores = {}
        debug_scoreboard = {} 
        
        for lid in candidates:
            data = self.languages.get(lid, {})
            
            # 2. BASE ECOSYSTEM MASS
            support_exts = [e for e in data.get('extensions', []) if e != ext]
            base_contributors = {e: ext_tally.get(e.lower(), 0) for e in support_exts if ext_tally.get(e.lower(), 0) > 0}
            base_mass = sum(base_contributors.values())
            
            # 3. DISCRIMINATOR MASS
            discriminators = data.get('discriminators', [])
            discrim_contributors = {d: ext_tally.get(d.lower(), 0) for d in discriminators if ext_tally.get(d.lower(), 0) > 0}
            discrim_mass = sum(discrim_contributors.values())
            
            # 4. TOXIC MASS
            disqualifiers = data.get('disqualifiers', [])
            toxic_contributors = {dq: ext_tally.get(dq.lower(), 0) for dq in disqualifiers if ext_tally.get(dq.lower(), 0) > 0}
            toxic_mass = sum(toxic_contributors.values())
            
            # ==========================================
            # THE PHYSICS ENGINE
            # ==========================================
            final_score = 0.0
            status = "Evaluated"
            
            if toxic_mass > 0:
                final_score = 0.0  # Thermodynamic collapse
                status = f"Collapsed (Toxic: {toxic_contributors})"
            elif base_mass == 0:
                final_score = discrim_mass * 0.1  # Ghost Ecosystem
                status = "Ghost (Discrim only)"
            else:
                final_score = base_mass + (discrim_mass * 2.0) # Healthy Ecosystem
                status = "Healthy"
                
            scores[lid] = final_score
            
            # Only build the debug data if the user is actively debugging to save CPU cycles
            if self.logger.isEnabledFor(logging.DEBUG):
                debug_scoreboard[lid] = {
                    "base": f"{base_mass} {base_contributors}",
                    "discrim": f"{discrim_mass} {discrim_contributors}",
                    "toxic": f"{toxic_mass} {toxic_contributors}",
                    "score": final_score,
                    "status": status
                }
                
        total_gravity = sum(scores.values())
        if total_gravity == 0:
            return None, 0.0 
        
        # Calculate final dominance ratio
        top_lid = max(scores, key=scores.get)
        dominance = scores[top_lid] / total_gravity
        
        # Output the professional debug receipt
        if self.logger.isEnabledFor(logging.DEBUG):
            log_lines = [f"Ecosystem Gravity Calculation for '{ext}':"]
            for lid, stats in debug_scoreboard.items():
                log_lines.append(f"  -> [{lid}] Score: {stats['score']:.1f} ({stats['status']})")
                log_lines.append(f"       Base: {stats['base']} | Discrim: {stats['discrim']} | Toxic: {stats['toxic']}")
            log_lines.append(f"  => Winner: {top_lid} ({dominance*100:.1f}% dominance)")
            self.logger.debug("\n" + "\n".join(log_lines) + "\n")
        
        return top_lid, dominance
    
    
    def _tier_1_metadata_lock(self, ext: str, file_name: str) -> Optional[str]:
        if file_name in self.anchor_map: 
            return self.anchor_map[file_name]
            
        # THE FIX: If the extension is highly contested, refuse to lock it at Tier 1.
        # This forces the pipeline to fall back to Tier 1.5 Ecosystem Gravity 
        # or Tier 3 Spectral Verification to prove its true identity.
        if ext in self.COLLISION_FREQUENCIES:
            return None
            
        if ext in self.extension_map: 
            return self.extension_map[ext]
        return None

    def _tier_2_fingerprint_check(self, content: str) -> Optional[str]:
        if not content.startswith('#!'): 
            return None
            
        first_line = content.split('\n', 1)[0].lower()
        self.logger.debug(f"Fingerprint Scan: Analyzing shebang line: '{first_line.strip()}'")
        
        for lang_id, data in self.languages.items():
            for trigger in data.get('shebangs', []):
                if trigger in first_line: 
                    return lang_id
        return None

    def _tier_3_spectral_scan(self, content: str, ext: str, claimed_lang: str = "undeterminable", gravity_lang: Optional[str] = None) -> Tuple[str, float]:
        """
        The Iron Wall Scanner. 
        If a file has an extension, it MUST be claimed by a known language. 
        Falling back to 'all languages' is forbidden if an extension is present.
        """
        candidates = []
        if ext:
            candidates = [l for l, d in self.languages.items() if ext in d.get('extensions', [])]
            
            # --- THE IRON WALL ---
            if not candidates:
                self.logger.debug(f"Iron Wall: Extension '{ext}' is unknown. Aborting spectral scan to prevent hallucination.")
                return "undeterminable", 0.0

        # Only allow 'Scan All' fallback for truly extensionless files
        if not candidates and not ext:
            candidates = list(self.languages.keys())

        if not candidates:
            return "undeterminable", 0.0

        loc = max(content.count('\n') + 1, 1)
        content_len = len(content)
        scores = {}

        for lid in candidates:
            data = self.languages.get(lid, {})
            family = data.get('lexical_family')
            
            # Phase 2 Pruning
            if family in self.DISQUALIFIERS and self.DISQUALIFIERS[family].search(content):
                continue
                
            raw_score = 0.0
            rules = data.get('rules', {})
            
            for _, regex in rules.items():
                if not regex: continue
                try:
                    c = len(regex.findall(content))
                    if c > content_len: c = 0 # Hallucination shield
                    raw_score += (c * 10.0)
                except Exception: pass
            
            # Delimiter Bonus
            family_key = data.get('lexical_family', 'std_c')
            delims = self.comment_defs.get("mechanical_families", {}).get(family_key, {}).get("delimiters", [])
            for d in delims:
                if d in content: raw_score += 15.0
            
            # Language Handicaps
            if lid in ('abap', 'fortran', 'cobol'): raw_score *= 0.4

            scores[lid] = raw_score / math.log1p(loc)

        if not scores: return "undeterminable", 0.0

        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        top_id, top_signal = sorted_scores[0]
        
        if top_signal < self.thresholds.get("PROSE_BASELINE_SIGNAL", 3.0): return "plaintext", 0.5

        # Margin and Confidence logic
        confidence = min(top_signal / 50.0, 1.0)
        return top_id, confidence


    # =========================================================================
    # THE TIER 4 DEEP SPACE DISCOVERY FUNNEL
    # =========================================================================
        # =========================================================================
    # THE TIER 4 DEEP SPACE DISCOVERY FUNNEL
    # =========================================================================
    def _tier_4_deep_space_discovery(self, content: str, coding_loc: int) -> Tuple[str, float]:
        """
        The redesigned Tier 4 Deep Space Discovery Funnel.
        Prioritizes graceful failure over guessing by enforcing a strict 1.5x margin logic.
        """
        if coding_loc < self.thresholds.get("TIER_4_MIN_LINES", 20):
            self.logger.debug(f"Tier 4 Discovery aborted: Insufficient physical mass ({coding_loc} < 20 lines).")
            return "plaintext", 0.40
        
        min_outlier_margin = self.thresholds.get("TIER_4_OUTLIER_MARGIN", 1.5)
        loc = max(coding_loc, 1)
        content_len = len(content)
        
        # =========================================================================
        # PHASE 1: Comment Family Isolation
        # =========================================================================
        family_scores = {}
        mechanical_families = self.comment_defs.get("mechanical_families", {})
        
        if mechanical_families:
            for fam_key, fam_data in mechanical_families.items():
                delims = fam_data.get("delimiters", [])
                family_scores[fam_key] = sum(content.count(d) for d in delims)
        else:
            # Fallback for the 8 standardized mechanical delimiters if not defined
            # Safely breaking apart the XML delimiter to prevent markdown render crashes
            xml_delim = "<" + "!--" 
            family_scores = {
                "std_c": content.count("//") + content.count("/*"),
                "pure_hash": content.count("#"),
                "hybrid_dash": content.count("--"),
                "xml_angle": content.count(xml_delim),
                "lisp_semi": content.count(";"),
                "tex_percent": content.count("%"),
                "bat_rem": len(re.findall(r'(?im)^REM\b', content)),
                "quote_string": content.count('"""') + content.count("'''")
            }
            
        winning_family = max(family_scores, key=family_scores.get, default=None)
        
        # Fail gracefully if no comments/structure exist to even establish a family
        if not winning_family or family_scores.get(winning_family, 0) == 0:
            self.logger.debug("Tier 4 [Phase 1]: Failed to establish a comment family (No delimiters found).")
            return "undeterminable", 0.0

        self.logger.debug(f"Tier 4 [Phase 1]: Comment Family Isolated -> '{winning_family}' (Score: {family_scores[winning_family]})")

        candidates = [
            lid for lid, data in self.languages.items() 
            if data.get('lexical_family') == winning_family
        ]

        if not candidates:
            self.logger.debug(f"Tier 4 [Phase 1]: No candidate languages found for family '{winning_family}'.")
            return "undeterminable", 0.0

        # =========================================================================
        # PHASE 2: Heuristic Disqualification (The Blacklist)
        # =========================================================================
        surviving_candidates = []
        for lid in candidates:
            family_key = self.languages.get(lid, {}).get('lexical_family')
            if family_key in self.DISQUALIFIERS and self.DISQUALIFIERS[family_key].search(content):
                self.logger.debug(f"Tier 4 [Phase 2]: Pruning '{lid}' via Heuristic Blacklist.")
                continue # Pruned by blacklist
            surviving_candidates.append(lid)

        if not surviving_candidates:
            self.logger.debug("Tier 4 [Phase 2]: All candidates pruned by heuristic blacklist.")
            return "undeterminable", 0.0
            
        self.logger.debug(f"Tier 4 [Phase 2]: Surviving candidates -> {surviving_candidates}")

        # =========================================================================
        # PHASE 3: Structural Density Scan
        # =========================================================================
        density_scores = {}
        friction_scores = {}  # <-- ADDED: Initialize the missing dictionary
        
        for lid in surviving_candidates:
            regex_hits = 0
            rules = self.languages.get(lid, {}).get('rules', {})
            t_start = time.time() # <-- ADDED: Start the friction timer
            
            for _, regex in rules.items():
                if not regex: continue
                
                # ---> THE RUNAWAY REGEX SHIELD <---
                raw_pat = getattr(regex, 'pattern', str(regex))
                clean_pat = raw_pat.replace("(?i)", "").replace("(?m)", "").replace("(?s)", "").strip()
                if clean_pat in ("", "()", "(?:)", "^", "$"):
                    continue

                try:
                    if hasattr(regex, 'findall'):
                        hits = len(regex.findall(content))
                    else:
                        hits = len(re.findall(str(regex), content))
                        
                    # Anti-Hallucination: Clamp if logic hits > total characters
                    if hits > content_len and content_len > 0:
                        hits = 0
                        
                    regex_hits += hits
                except Exception:
                    pass
            
            # ---> PART 3: THE MACRO BLINDSPOT FIX (Density Boost) <---
            family_key = self.languages.get(lid, {}).get('lexical_family')
            if family_key == 'std_c':
                macro_hits = len(re.findall(r'^\s*#(?:define|ifdef|ifndef|endif|include|pragma|if)\b', content, re.M))
                # Anti-Hallucination clamp
                if macro_hits > content_len and content_len > 0:
                    macro_hits = 0
                regex_hits += macro_hits
                
            # ---> NEW: THE ABAP HANDICAP <---
            if lid == 'abap':
                regex_hits *= 0.7
            
            # =====================================================================
            # PHASE 4: The Density Equation (Hits / loc)
            # =====================================================================
            density_scores[lid] = regex_hits / loc
            friction_scores[lid] = time.time() - t_start # <-- ADDED: Record the friction time
            
            # =====================================================================
            # PHASE 4: The Density Equation (Hits / loc)
            # =====================================================================
            density_scores[lid] = regex_hits / loc

        if not density_scores:
            self.logger.debug("Tier 4 [Phase 3]: No structural signals detected for any candidate.")
            return "undeterminable", 0.0

        # Sort to find the winner and the runner-up
        sorted_scores = sorted(density_scores.items(), key=lambda x: x[1], reverse=True)
        top_id, top_density = sorted_scores[0]
        
        self.logger.debug(f"Tier 4 [Phase 3]: Top signals -> {[(k, round(v, 4)) for k, v in sorted_scores[:3]]}")
        
        # No structural signals at all
        if top_density == 0.0:
            self.logger.debug("Tier 4 [Phase 3]: Top density is 0.0. Failing gracefully.")
            return "undeterminable", 0.0

        # =========================================================================
        # PHASE 4: The Ensemble Reconciliation Engine
        # =========================================================================
        if len(sorted_scores) > 1:
            runner_up_id = sorted_scores[1][0]
            runner_up_density = sorted_scores[1][1]
            
            density_margin = top_density / max(runner_up_density, 0.0001) 
            
            top_friction = friction_scores[top_id]
            runner_up_friction = friction_scores[runner_up_id]
            friction_ratio = top_friction / max(runner_up_friction, 0.000001)
            
            # --- THE SLIDING SCALE OF TRUST ---
            
            # 1. The Strong Structural Lock
            if density_margin >= 1.5:
                if friction_ratio > 5.0:
                    self.logger.warning(f"Tier 4 [Reconciliation]: TEMPORAL ANOMALY on {top_id}...")
                    return "undeterminable", 0.0
            
            # 2. The Friction Tie-Breaker
            elif density_margin >= self.thresholds.get("TIER_4_OUTLIER_MARGIN", 1.10):
                # The density win was weak, so we demand a strong temporal friction win (e.g., 2x faster)
                if friction_ratio > 0.5:
                    self.logger.debug(f"Tier 4 [Reconciliation]: Collision. {top_id} density margin ({density_margin:.2f}x) was too weak, and friction ratio ({friction_ratio:.2f}x) failed to break the tie.")
                    return "undeterminable", 0.0
                self.logger.debug(f"Tier 4 [Reconciliation]: Friction Tie-Breaker utilized for {top_id}.")
                
            # 3. Absolute Ambiguity
            else:
                return "undeterminable", 0.0

    def _forge_result(self, lang_id: str, intensity: float, tier: int, proof: str, base: DetectorResult, content_sample: str = "") -> DetectorResult:
        family = self.languages.get(lang_id, {}).get('lexical_family')
        
        # Calculate our metrics from the ghost parameter!
        file_loc = content_sample.count('\n') + 1 if content_sample else 0
        file_size = len(content_sample.encode('utf-8')) if content_sample else 0

        base.update({
            "lang_id": lang_id, 
            "intensity": intensity, 
            "family": family, 
            "lock_tier": tier,
            "source_proof": proof,
            "candidates": [lang_id] if lang_id != "undeterminable" else [],
            "loc": file_loc,
            "size_bytes": file_size
        })
        return base

    def _capture_raw_signal(self, file_path: Union[str, Path]) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read(1024 * 50)
        except (PermissionError, FileNotFoundError, IOError, OSError) as e:
            self.logger.error(f"Hardware failure reading '{file_path}': {str(e)}")
            # Wire up the dead exception:
            raise FocusingError(f"Failed to focus lens on {file_path}") from e


    def _find_balanced_end(self, text: str, start_pos: int, opener: str, closer: str) -> int:
        depth = 0
        in_string: Optional[str] = None
        limit = min(start_pos + self.thresholds.get("HANDSHAKE_LOOKAHEAD_LIMIT", 50000), len(text))
        
        for i in range(start_pos, limit):
            char = text[i]
            
            if char in ('"', "'", "`") and (i == 0 or text[i-1] != '\\'):
                if not in_string: 
                    in_string = char
                elif in_string == char: 
                    in_string = None
                continue
                
            if in_string: 
                continue

            if char == opener: 
                depth += 1
            elif char == closer:
                depth -= 1
                if depth <= 0: 
                    return i + 1
                    
        return limit

    def _detect_hybrids(self, content: str, primary_id: str) -> List[Dict[str, Any]]:
        total_len = len(content)
        if total_len == 0: 
            return []
        
        distribution = {primary_id: total_len}
        last_processed_idx = 0
        triggers = []
        
        for hs in self.HANDSHAKE_REGISTRY:
            for m in hs["trigger"].finditer(content):
                triggers.append({
                    "start": m.start(),
                    "trigger_end": m.end(),
                    "target": hs["target"],
                    "end_pattern": hs["end"],
                    "pair": hs.get("pair")
                })
        
        triggers.sort(key=lambda x: x["start"])
        
        for t in triggers:
            if t["start"] < last_processed_idx:
                continue 
            
            if t["pair"]:
                open_char, close_char = t["pair"]
                end_idx = self._find_balanced_end(content, t["start"], open_char, close_char)
            else:
                search_limit = min(t["trigger_end"] + self.thresholds.get("HANDSHAKE_LOOKAHEAD_LIMIT", 50000), total_len)
                end_match = t["end_pattern"].search(content, pos=t["trigger_end"], endpos=search_limit)
                end_idx = end_match.end() if end_match else total_len
            
            segment_len = end_idx - t["start"]
            target = t["target"]
            
            distribution[target] = distribution.get(target, 0) + segment_len
            distribution[primary_id] -= segment_len
            last_processed_idx = end_idx

        mix = []
        for lid, m_len in distribution.items():
            if m_len > 0:
                pct = round((m_len / total_len) * 100, 1)
                if pct >= 1.0: 
                    mix.append({"id": lid, "pct": pct})
        
        return sorted(mix, key=lambda x: x['pct'], reverse=True)