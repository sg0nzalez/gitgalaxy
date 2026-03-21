import statistics
import logging
from typing import List, Dict, Any, Tuple, Optional
import math

# ==============================================================================
# GitGalaxy Phase 7: Spectral Auditor (Quality Control)
# Strategy v6.2.0 Protocol: Bayesian Accountability & Inert Dark Matter
# ==============================================================================

class SpectralAuditor:
    """
    The GitGalaxy Spectral Auditor.
    
    PURPOSE: Performs the 3rd-gate sanity check to catch Linguistic Drift and 
    Data Dumps using species-specific statistical outliers and the 50/0 Law.
    
    PHILOSOPHY: Holds Bayesian predictions to account. If a file acts as a 
    statistical outlier compared to its peers, the focus is lost and it is 
    banished to the Singularity, regardless of its initial metadata claims.
    
    ARCHITECTURE (v6.2.0):
    1. Bayesian Accountability: Logs when high-confidence priors are refuted.
    2. Polyglot Baseline Defense: Bypasses strict MAD checks for highly blended files.
    3. Inert Dark Matter: Relegated files are stripped to a lightweight schema.
    4. Vestigial Cleanup: Spatial geometry is deferred entirely to the Cartographer.
    """

    def __init__(self, parent_logger: Optional[logging.Logger] = None, lang_defs: Optional[Dict[str, Any]] = None):
        """Initializes the statistical auditor and synchronizes telemetry."""
        
        # --- TELEMETRY SYNC ---
        if parent_logger:
            self.logger = parent_logger.getChild("auditor")
            self.logger.setLevel(parent_logger.level)
        else:
            self.logger = logging.getLogger("auditor")
            self.logger.setLevel(logging.INFO)

        self.logger.debug("Initializing Spectral Auditor (Statistical Gating)...")

        # Save the language definitions so we can check for execution geometry later
        self.lang_defs = lang_defs or {}

        # SCHEMA CONSTANTS (32 Signal Keys representing pure active logic)
        self.SIGNAL_KEYS = [
            "branch", "args", "linear", "func_start", "class_start", "import", "api", "decorators",
            "safety", "safety_neg", "danger", "flux", "heat_triggers", "keyword_debt", "private_info",
            "io", "concurrency", "ui_framework", "events", "ssr_boundaries", "dependency_injection",
            "scientific", "generics", "comprehensions", "closures", "globals", "telemetry", "test",
            "macros", "pointers", "memory_alloc", "inline_asm"
        ]

    def audit(self, stars: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """Executes statistical gating to identify 'Hollow Stars' (outliers/data-dumps)."""
        import os # Required for extension splitting in Consensus Engine
        
        if not stars: 
            self.logger.debug("Spectral Audit skipped: Empty star roster provided.")
            return [], []

        self.logger.info(f"Initiating Spectral Audit across {len(stars)} celestial bodies...")
        
        total_stars = max(len(stars), 1)
        orphan_threshold = max(3, int(math.log10(total_stars) * 2))
        self.logger.debug(f"Dynamic Ecosystem Orphan Threshold set to: <= {orphan_threshold} files.")
        
        visible, singularity = [], []
        
        # =================================================================
        # GATE 0: EMPIRICAL BAYES LOOP-BACK (The Consensus Engine)
        # =================================================================
        confident_core = []
        ambiguous_pen = []
        
        # 1. The Triage
        for s in stars:
            telemetry = s.get("telemetry", {})
            tier = telemetry.get("identity_lock_tier", s.get("lock_tier", 4))
            proof = telemetry.get("identity_source_proof", s.get("source_proof", ""))
            
            # If the engine had to guess, or confidence was terrible, hold it back.
            if tier >= 4 or "Collision" in proof:
                ambiguous_pen.append(s)
            else:
                confident_core.append(s)
                
        # 2. Build the Ecosystem Consensus Map
        # Structure: { ".ext": { "lang1": count, "lang2": count } }
        consensus_map: Dict[str, Dict[str, int]] = {}
        for s in confident_core:
            ext = os.path.splitext(s.get("path", ""))[1].lower()
            lang = s.get("lang_id")
            if ext and lang:
                if ext not in consensus_map:
                    consensus_map[ext] = {}
                consensus_map[ext][lang] = consensus_map[ext].get(lang, 0) + 1
                
        # 3. The Heuristic Loop-Back
        resolved_count = 0
        for s in ambiguous_pen:
            ext = os.path.splitext(s.get("path", ""))[1].lower()
            current_lang = s.get("lang_id", "unknown")
            
            if ext in consensus_map:
                lang_counts = consensus_map[ext]
                total_for_ext = sum(lang_counts.values())
                
                if total_for_ext > 0:
                    # Find the dominant language for this extension in THIS repository
                    winner_lang = max(lang_counts, key=lang_counts.get)
                    winner_count = lang_counts[winner_lang]
                    
                    # If the winner claims >= 80% of the confident files, it is the Ecosystem Truth.
                    if (winner_count / total_for_ext) >= 0.80:
                        s["lang_id"] = winner_lang
                        if "telemetry" not in s:
                            s["telemetry"] = {}
                        s["telemetry"]["identity_source_proof"] = f"Heuristic Loop-Back (Consensus: {winner_lang})"
                        s["telemetry"]["identity_lock_tier"] = 2 # Elevate it to a strong Ecosystem Lock
                        
                        self.logger.debug(f"[Consensus] Resolved ambiguous '{s.get('name')}': {current_lang} -> {winner_lang}")
                        confident_core.append(s)
                        resolved_count += 1
                        continue
            
            # If we reach here, the file was ambiguous and the ecosystem couldn't save it.
            # Banish it to the Singularity immediately to prevent hallucinations.
            reason = f"Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)"
            singularity.append(self._format_for_singularity(s, reason))
            
        if resolved_count > 0:
            self.logger.info(f"Heuristic Loop-Back complete: {resolved_count} ambiguous artifacts rescued via Ecosystem Consensus.")
        # =================================================================

        by_lang: Dict[str, List[Dict[str, Any]]] = {}
        
        # 4. Group artifacts by linguistic species for localized statistics
        # Note: We now iterate over 'confident_core' instead of raw 'stars'
        for s in confident_core:
            lid = s.get("lang_id", "undeterminable")
            if lid not in by_lang: 
                by_lang[lid] = []
            by_lang[lid].append(s)
            
        # 5. Process each species independently
        for lid, group in by_lang.items():
            if lid in ("undeterminable", "unknown"):
                for s in group:
                    singularity.append(self._format_for_singularity(s, "Already Dark Matter (Pre-Audit)"))
                self.logger.debug(f"[{lid}] Bypassed {len(group)} artifacts (already Dark Matter).")
                continue
            
            # =================================================================
            # THE DYNAMIC AUDITABILITY CHECK (Code vs. Structure vs. Data)
            # =================================================================
            is_inert = False
            is_structural = False
            
            if hasattr(self, 'lang_defs') and lid in self.lang_defs:
                rules = self.lang_defs[lid].get("rules", {})
                
                # POSITIVE COUNT: How many actual, active logic sensors exist?
                # .get(key) safely handles "space-efficient" dictionaries by returning None
                active_signals = sum(1 for key in self.SIGNAL_KEYS if rules.get(key) is not None)
                total_signals = len(self.SIGNAL_KEYS) 
                
                # 1. THE INERT MATTER GATE (0 active signals)
                # e.g., MLIR, Proto, Plaintext, YAML, CSV.
                if active_signals == 0:
                    is_inert = True
                    
                # 2. THE STRUCTURAL GATE (Lacks the "Full" Regex Scan)
                # e.g., HTML, CSS, Makefile, Dockerfile. 
                # If a language is missing ~25% or more of its sensors (like pointers, 
                # memory allocation, or closures), it is Structural, not Turing-complete.
                elif active_signals <= (total_signals * 0.75):
                    is_structural = True
            else:
                is_inert = True # Unknown/Undefined languages are inert by default
                
            # Immediately bypass inert matter from all statistical checks
            if is_inert:
                visible.extend(group)
                self.logger.debug(f"[{lid}] Bypassed {len(group)} artifact(s) (Dynamic Inert Matter: 0 Signals).")
                continue

            # =================================================================
            # GATE C: THE ECOSYSTEM ORPHAN GUARD
            # =================================================================
            # If a language only has a tiny presence (<= orphan_threshold) in the galaxy...
            if len(group) <= orphan_threshold:
                # FIX: Require an absolute Tier 0 Convergent Lock for orphans to survive.
                # If ALL files in this tiny group are Tier 1 or worse (> 0), banish them.
                all_weak_claims = all(
                    s.get("telemetry", {}).get("identity_lock_tier", s.get("lock_tier", 4)) > 0 
                    for s in group
                )
                
                if all_weak_claims:
                    relegation_reason = f"Ecosystem Orphan (Population {len(group)}). Reverting to plaintext."
                    self.logger.warning(f"[{lid}] {relegation_reason}")
                    
                    for s in group:
                        # Strip the hallucination, keep the mass visible in the 3D map
                        s["lang_id"] = "plaintext"
                        s["telemetry"]["identity_source_proof"] = "Orphan Guard Fallback"
                        s["equations"] = {} # Inert matter has no logic equations
                        visible.append(s)
                    continue
                
            # =================================================================

            # --- GATE D: STATISTICAL OUTLIER DETECTION (The 50/0 Law) ---
            
            rhos = []
            
            # Calculate logic density (rho) for all stars in this language
            for s in group:
                try:
                    equations = s.get("equations", {})
                    signal_hits = sum(equations.get(k, 0) for k in self.SIGNAL_KEYS)
                    # Denominator MUST be total physical lines to detect 'hollowness'
                    total_physical_loc = max(s.get("total_loc", s.get("coding_loc", 1)), 1)
                    s["_rho"] = signal_hits / total_physical_loc
                    
                    # Polyglot Defense: Only add pure files to the statistical baseline
                    if not self._is_highly_blended(s):
                        rhos.append(s["_rho"])
                except Exception as e:
                    self.logger.warning(f"Failed to calculate signal density for '{s.get('name', 'unknown')}': {e}")
                    s["_rho"] = 0.0
                    rhos.append(0.0)

            # --- GATE D.1: STATISTICAL READINESS CHECK ---
            # 1. Population Density (N >= 50)
            has_mass = len(rhos) >= 50
            
            # 2. Confidence Anchor (At least one file with C > 0.85)
            has_anchor = any(
                s.get("telemetry", {}).get("identity_confidence", s.get("intensity", 0.0)) > 0.85 
                for s in group
            )
            
            use_stats = has_mass and has_anchor
            median_rho = 0.0
            mad = 0.00001

            if use_stats:
                try:
                    median_rho = statistics.median(rhos)
                    mad = statistics.median([abs(r - median_rho) for r in rhos])
                    mad = max(mad, 0.00001) # Prevent division by zero
                    
                    # 3. Cohesion Metric (R-MAD < 1.0)
                    r_mad = mad / max(median_rho, 0.00001)
                    if r_mad >= 1.0:
                        self.logger.debug(f"[{lid}] Baseline skipped: Heterogeneous Population (R-MAD {r_mad:.2f} >= 1.0).")
                        use_stats = False
                    else:
                        self.logger.debug(f"[{lid}] Statistical Baseline -> Median Rho: {median_rho:.4f} | MAD: {mad:.4f} | R-MAD: {r_mad:.2f}")
                except statistics.StatisticsError as e:
                    self.logger.warning(f"[{lid}] Statistical failure during MAD calculation: {e}. Falling back to 50/0 Law only.")
                    use_stats = False
            else:
                self.logger.debug(f"[{lid}] Baseline skipped (N={len(rhos)}, Anchor={has_anchor}). Defaulting to 50/0 Law.")

            relegated_count = 0
            necrotic_count = 0

            # 3. Evaluate each star against the baseline
            for s in group:
                rho = s.pop("_rho", 0.0)
                is_outlier = False
                relegation_reason = ""
                
                loc = s.get("coding_loc", 0)
                name = s.get("name", "unknown")
                path = s.get("path", "unknown")
                is_blended = self._is_highly_blended(s)
                
                # Extract Bayesian telemetry from Phase 1 OR fallback to root meta keys
                telemetry = s.get("telemetry", {})
                lock_tier = telemetry.get("identity_lock_tier", s.get("lock_tier", 4))
                source_proof = telemetry.get("identity_source_proof", s.get("source_proof", "Discovery"))
                confidence = telemetry.get("identity_confidence", s.get("intensity", 0.0))
                
                # THE 50/0 LAW: Hard Floor check for data dumps disguised as code
                if loc > 50 and rho == 0:
                    is_outlier = True
                    relegation_reason = f"50/0 Law (LOC: {loc}, Signals: 0)"
                # THE ROBUST Z-SCORE (MAD)
                # Bypassed if the file is a heavy polyglot (its density is blended)
                elif use_stats and not is_blended:
                    mi = (0.6745 * (rho - median_rho)) / mad
                    
                    # 4. Bayesian Threshold Gating (T_adj = -3.5 * Ci)
                    t_adj = -5 * max(confidence, 0.1) # Floor confidence to prevent 0 threshold
                    
                    if mi < t_adj: 
                        is_outlier = True
                        relegation_reason = f"Statistical Anomaly (Z-Score: {mi:.2f} < {t_adj:.2f})"

                # 4. Routing logic for Outliers
                if is_outlier:
                    if self._is_necrotic(s):
                        # SPEC ALIGNMENT: Grant Reprieve from Relegation without mutating lang_id
                        # We keep a flag for internal tracking, but preserve the original lang_id
                        s["is_necrotic"] = True 
                        self.logger.debug(f"[{lid}] Necrosis Guard: '{name}' failed audit ({relegation_reason}) but granted a Reprieve from Relegation.")
                        visible.append(s)
                        necrotic_count += 1
                    else:
                        # --- BAYESIAN ACCOUNTABILITY ---
                        # If the file had a strong prior (Tier 0 or 1), hold the prediction to account.
                        if lock_tier <= 1:
                            self.logger.warning(
                                f"BAYESIAN REFUTATION: '{path}' was claimed as '{lid}' via {source_proof} (Tier {lock_tier}), "
                                f"but its Intent Density is an outlier ({relegation_reason}). Focus lost."
                            )
                        elif loc > 1000:
                            # SIZE-AWARE WARNING: If a massive file is dropped, alert the engineer.
                            self.logger.warning(f"Massive Data Dump Relegated: '{path}' (LOC: {loc}) stripped to Singularity. Reason: {relegation_reason}")
                        else:
                            self.logger.debug(f"[{lid}] Relegated: '{name}' stripped to Singularity. Reason: {relegation_reason}")

                        # Format it as Inert Dark Matter to save memory and ensure schema consistency
                        singularity.append(self._format_for_singularity(s, relegation_reason))
                        relegated_count += 1
                else:
                    visible.append(s)

            if relegated_count > 0 or necrotic_count > 0:
                self.logger.info(f"[{lid}] Audit complete: {relegated_count} relegated to Singularity, {necrotic_count} flagged as Necrosis.")

        self.logger.info(f"Spectral Audit Complete | Visible Matter: {len(visible)} | Relegated to Singularity: {len(singularity)}")
        return visible, singularity

    def _is_highly_blended(self, star: Dict[str, Any]) -> bool:
        """Determines if a file is a Polyglot where the primary language is < 80% of the mass."""
        lang_mix = star.get("lang_mix", [])
        if not lang_mix:
            return False
            
        primary_lang = star.get("lang_id")
        for mix in lang_mix:
            if mix.get("id") == primary_lang:
                # If the primary language makes up less than 80% of the file, it's blended.
                return mix.get("pct", 100.0) < 80.0
                
        return True # Primary language wasn't even in the mix (Extreme anomaly)

    def _is_necrotic(self, star: Dict[str, Any]) -> bool:
        """Determines if a star is dead matter using literature ratios."""
        try:
            doc_loc = star.get("doc_loc", 0)
            coding_loc = max(star.get("coding_loc", 1), 1)
            
            # Condition 1: Massive comment-to-code ratio (5-to-1)
            if doc_loc > (coding_loc * 5): 
                return True
                
            eq = star.get("equations", {})
            total_signals = sum(eq.values())
            
            # Condition 2: Over 50% of the active signals are commented-out structural logic
            if total_signals > 0 and eq.get("graveyard", 0) > (total_signals * 0.5): 
                return True
                
        except Exception as e:
            self.logger.debug(f"Necrosis evaluation failed safely: {e}")
            
        return False

    def _format_for_singularity(self, star: Dict[str, Any], reason: str) -> Dict[str, Any]:
        """
        Formats an audited star to match the Orchestrator's Pre-Refraction Dark Matter schema.
        This ensures mathematical inertia and prevents the JSON archive from bloating.
        """
        telemetry = star.get("telemetry", {})
        
        return {
            "path": star.get("path", "unknown"),
            "reason": reason,
            "size_bytes": star.get("size_bytes", 0),
            
            # Preserve Bayesian Optics for Phase 8 SBOM Traceability
            "failed_claim": star.get("lang_id", "unknown"),
            "identity_confidence": telemetry.get("identity_confidence", star.get("intensity", 0.0)),
            "identity_lock_tier": telemetry.get("identity_lock_tier", star.get("lock_tier", 4)),
            "identity_source_proof": telemetry.get("identity_source_proof", star.get("source_proof", "Discovery"))
        }