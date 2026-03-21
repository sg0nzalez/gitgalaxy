import math
import logging
import re
import statistics
from typing import Dict, Any, List, Optional, Tuple
import gitgalaxy_standards_v011 as config

# ==============================================================================
# GitGalaxy Phase 4: Signal Processor (The Physics Engine)
# Strategy v6.2.0 Protocol: Temporal Normalization & Universal Exposure
# ==============================================================================

class SignalProcessor:
    """
    The GitGalaxy Signal Processor.
    
    PURPOSE: Converts raw logic counts and temporal telemetry into "Exposure Vectors" 
    and generates high-fidelity forensic reports identifying structural risks.
    
    ARCHITECTURE (v6.2.0):
    1. Temporal Consolidation: Math formulas for Churn and Stability now live here.
    2. Two-Pass Normalization: Auto-scales Churn based on the galaxy's global maximum.
    3. Sigmoid Armor: `try/except OverflowError` guarantees survival on extreme file densities.
    4. Flexible Risk Schema: Vector indexing is dynamic, preventing offset bugs.
    """

    # --- THE SPECTRAL SCHEMA ---
# --- THE SPECTRAL SCHEMA (v6.2.0 - 51-Point Sync) ---
    SIGNAL_SCHEMA = [
        "branch", "linear", "args", "func_start", "class_start",
        "safety", "safety_neg", "danger", "io", "api", "flux", "graveyard", "doc", "test",
        "concurrency", "ui_framework", "closures", "globals", "decorators", "generics", 
        "comprehensions", "scientific", "heat_triggers", "import", "ownership",
        "planned_debt", "fragile_debt", "private_info", "spec_exposure", "civil_war", 
        "ssr_boundaries", "events", "dependency_injection", "macros", "pointers", 
        "memory_alloc", "inline_asm", "telemetry", "print_hits", "cast_hits", 
        "bailout_hits", "halt_hits", "bitwise_hits", "sync_locks", "freeze_hits", 
        "cleanup", "encapsulation", "listeners", "test_skip",
        "indent_tabs", "indent_spaces"
    ]
    
    # --- THE 13-POINT RISK EXPOSURE SCHEMA ---
    RISK_SCHEMA = [
        "cognitive_load", "safety_score", "tech_debt",   "verification", 
        "api_exposure",   "concurrency",  "state_flux",  "graveyard", 
        "spec_match",     "stability",    "churn",       "documentation", 
        "civil_war"
    ]

    def __init__(
        self, 
        aperture_config: Optional[Dict[str, Any]] = None,
        parent_logger: Optional[logging.Logger] = None
    ):
        """Initializes the physics engine with forensic constants and telemetry."""
        if parent_logger:
            self.logger = parent_logger.getChild("processing")
            self.logger.setLevel(parent_logger.level)
        else:
            self.logger = logging.getLogger("processing")
            self.logger.setLevel(logging.INFO) 

        self.logger.debug("Initializing Universal Exposure Framework...")
        self.config = aperture_config or {}
    
        # Fetch Physics Constants
        physics = getattr(config, "PHYSICS_CONSTANTS", {})
        self.WEIGHT_RISK = physics.get("WEIGHT_RISK", 2.5)
        self.WEIGHT_DEFENSE = physics.get("WEIGHT_DEFENSE", 1.0)
        self.TIER_VARS = physics.get("TIER_VARS", {
            "tier1": {"fc": 1.0,  "irc": 0}, 
            "tier2": {"fc": 0.85, "irc": 2}, 
            "tier3": {"fc": 0.60, "irc": 5}
        })
        self.MASSIVE_FILE_THRESHOLD = physics.get("MASSIVE_FILE_THRESHOLD", 300)
        self.TESTING_RISK_FLOOR = physics.get("TESTING_RISK_FLOOR", 15.0)

        # Fetch Path Modifiers & Asset Masks
        self.path_modifiers = getattr(config, "PATH_MODIFIERS", {})
        self.asset_masks = getattr(config, "PHYSICS_ASSET_MASKS", {})
        self.risk_tuning = getattr(config, "RISK_EQUATION_TUNING", {})
        
        self.logger.info(f"Signal Processor Online | 13-Point Risk Schema loaded.")

    def _calculate_silo_risk(self, authors: dict) -> float:
        """
        Calculates the 'Bus Factor' risk of a file.
        100% = A single developer wrote the entire file (High Silo Risk).
        0% = Perfectly distributed across multiple developers (Low Silo Risk).
        """
        if not authors:
            return 0.0 
            
        total_commits = sum(authors.values())
        if total_commits == 0:
            return 0.0
            
        dominant_commits = max(authors.values())
        ownership_ratio = dominant_commits / total_commits
        
        return round(ownership_ratio * 100.0, 1)

    def calculate_risk_vector(self, meta: Dict[str, Any], equations: Dict[str, int], umbrella_bonus: float = 0.0) -> Dict[str, Any]:
        """Calculates risk exposure, temporal physics, and per-file physical impact."""
        loc = max(meta.get("coding_loc", 1), 1)
        total_loc = max(meta.get("total_loc", loc), 1)
        doc_lines = meta.get("doc_loc", 0)
        lang_id = meta.get("lang_id", "undeterminable")
        rel_path = meta.get("path", "unknown")
        
        try:
            # ==================================================================
            # THE DOCUMENTATION BYPASS PROTOCOL
            # Treat pure literature as static structural assets, skipping logic math
            # ==================================================================
            doc_languages = self.asset_masks.get("DOCUMENTATION_LANGUAGES", {"markdown", "plaintext", "rst", "text"})
                        
            if lang_id.lower() in doc_languages:
                # We still want temporal history to know if docs are actively maintained
                temporal_data = meta.get("temporal_telemetry", {})
                _, raw_churn_freq = self._calc_raw_temporal_signals(temporal_data)

                # --- NEW: Extract rich Git data for ownership & silo risk ---
                authors_map = meta.get("authors", {})
                silo_exposure = self._calculate_silo_risk(authors_map)
                
                ghost_meta = meta.get("metadata", {})
                if authors_map:
                    dominant_author = max(authors_map, key=authors_map.get)
                else:
                    dominant_author = ghost_meta.get("ownership", "Unknown Architect")

                # 1. Synthetic 13-Point Risk Exposure (The Blanket Scores)
                blanket_risk_vector = [
                    0.0,    # Cognitive Load (None)
                    0.0,  # Safety (Completely safe)
                    0.0,    # Tech Debt (None)
                    0.0,    # Verification/Testing (N/A)
                    0.0,    # API Exposure (N/A)
                    0.0,    # Concurrency (None)
                    0.0,    # State Flux (None)
                    0.0,    # Graveyard (None)
                    0.0,  # Spec Match (Docs ARE specs)
                    0.0,  # Stability (Highly stable)
                    min(raw_churn_freq * 10, 100.0), # Churn (Scales based on commit frequency)
                    100.0,  # Documentation Coverage (Perfect)
                    50.0     # Civil War (N/A)
                ]

                return {
                    "risk_vector": blanket_risk_vector,
                    # 2. Perfect 51-point array of zeroes to prevent hollow UI dictionaries
                    "hit_vector": [0] * len(self.SIGNAL_SCHEMA), 
                    # 3. Apply a generic light mass purely based on line count
                    "file_impact": round(max(total_loc / 50.0, 1.0), 2),
                    "telemetry": {
                        "control_flow_ratio": 0.0, # 0% active control flow
                        "ownership_entropy": self._calc_ownership_entropy(authors_map),
                        "author_distribution": silo_exposure,  # <-- The new metric!
                        "ownership": dominant_author,          # <-- The updated ownership!
                        "domain_context": ghost_meta
                    }
                }

            # ==================================================================
            # 1. ACTIVE PHYSICS ENGINE (For normal executable code)
            # ==================================================================
            tier = self._get_tier(lang_id)
            fc = self.TIER_VARS[tier]["fc"]
            irc = self.TIER_VARS[tier]["irc"]
            
            # Environmental Context
            mp_map = self._get_locational_multipliers(rel_path)

            self.logger.debug(f"[{rel_path}] Physics Calc | Lang: {lang_id} (Fc: {fc:.2f}, Irc: {irc})")

            hit_vector = [equations.get(key, 0) for key in self.SIGNAL_SCHEMA]

            # ------------------------------------------------------------------
            # 1. TEMPORAL PRE-PROCESSING (Raw Extraction)
            # ------------------------------------------------------------------
            temporal_data = meta.get("temporal_telemetry", {})
            stability_score, raw_churn_freq = self._calc_raw_temporal_signals(temporal_data)

            # ------------------------------------------------------------------
            # 2. CORE RISK EXPOSURE CALCULATIONS
            # ------------------------------------------------------------------
            cog_score, cog_raw = self._calc_cog_load(loc, equations, irc, fc, mp_map.get("cog", 1.0))
            saf_score = self._calc_safety(loc, equations, irc, fc, mp_map.get("safety", 1.0))
            debt_score = self._calc_tech_debt(loc, equations, irc, mp_map.get("debt", 1.0))
            
            # --- FIX: Passing umbrella_bonus into the verification calculation ---
            test_score = self._calc_verification(
                loc, 
                rel_path, 
                meta.get("is_protected", False), 
                equations, 
                irc, 
                fc, 
                mp_map.get("test", 1.0),
                umbrella_bonus=umbrella_bonus
            )
            
            doc_score = self._calc_documentation(loc, doc_lines, equations, fc, irc, mp_map.get("doc", 1.0))
            
            exposure_vector = {
                "cognitive_load": cog_score,
                "safety_score":   saf_score,
                "tech_debt":      debt_score,
                "verification":   test_score,
                "api_exposure":   self._calc_api_exposure(equations, mp_map.get("api", 1.0)),
                "concurrency":    self._calc_concurrency(loc, equations, irc, mp_map.get("async", 1.0)),
                "state_flux":     self._calc_state_flux(loc, equations, irc, mp_map.get("flux", 1.0)),
                "graveyard":      self._calc_graveyard(total_loc, equations, mp_map.get("dead", 1.0)),
                "spec_match":     self._calc_spec_alignment(equations, mp_map.get("spec", 1.0)),
                "stability":      stability_score,
                "churn":          0.0, # Placeholder: Auto-Scaled globally in Pass 2
                "documentation":  doc_score,
                "civil_war":      self._calc_civil_war(equations)
            }
            
            # ------------------------------------------------------------------
            # 3. VECTOR ASSEMBLY (Locked to RISK_SCHEMA order)
            # ------------------------------------------------------------------
            risk_vector_ordered = [round(exposure_vector[key], 4) for key in self.RISK_SCHEMA]

            # ------------------------------------------------------------------
            # 4. CALCULATE FILE IMPACT (The Mass)
            # ------------------------------------------------------------------
            satellites = meta.get("satellites", [])
            func_start = equations.get("func_start", 0)
            
            # Use actual satellite impacts if available
            if satellites:
                sum_function_impacts = sum(sat.get("impact", 0) for sat in satellites)
            else:
                # --- THE HEADER & DATA DUMP CONTINGENCY ---
                # If there are no functions, global branches and args represent structural 
                # macros or data, not execution logic. We temporarily treat them as 0 
                # to prevent a geometric explosion in the fallback math.
                if func_start == 0:
                    temp_branches = 0
                    temp_args = 0
                else:
                    # Fallback for procedural scripts
                    temp_branches = equations.get("branch", 0)
                    temp_args = equations.get("args", 0)
                    
                sum_function_impacts = ((temp_branches + 1) * (temp_args + 1) + (0.05 * loc)) * 10
                
            api_exposure = equations.get("api", 0)
            concurrency = equations.get("concurrency", 0)
            flux = equations.get("flux", 0)
            
            file_mass = sum_function_impacts + api_exposure + concurrency + flux + (loc / 50.0)

            # ------------------------------------------------------------------
            # 5. EXECUTE OWNERSHIP ENTROPY MATH & SILO RISK
            # ------------------------------------------------------------------
            authors_map = meta.get("authors", {})
            ownership_score = self._calc_ownership_entropy(authors_map)
            silo_exposure = self._calculate_silo_risk(authors_map)
            
            ghost_meta = meta.get("metadata", {})
            
            if authors_map:
                dominant_author = max(authors_map, key=authors_map.get)
            else:
                dominant_author = ghost_meta.get("ownership", "Unknown Architect")

            telemetry_payload = {
                "densities": {"cog_raw": round(cog_raw, 3)},
                "raw_churn_freq": raw_churn_freq,
                "ownership_entropy": ownership_score,
                "author_distribution": silo_exposure,  # <-- The new metric!
                "ownership": dominant_author,          # <-- The updated ownership!
                "domain_context": ghost_meta 
            }
            
            if mp_map:
                telemetry_payload["multipliers"] = mp_map

            return {
                "risk_vector": risk_vector_ordered,
                "hit_vector": hit_vector,
                "file_impact": round(file_mass, 2),
                "telemetry": telemetry_payload
            }

        except Exception as e:
            self.logger.error(f"Catastrophic physics failure on artifact '{rel_path}': {e}", exc_info=True)
            # Fail-soft: Return a baseline safe vector
            return {
                "risk_vector": [0.0] * len(self.RISK_SCHEMA),
                "hit_vector": [equations.get(k, 0) for k in self.SIGNAL_SCHEMA],
                "file_impact": max(loc / 50.0, 1.0),
                "telemetry": {"error": str(e)}
            }
                    
    # ==========================================================================
    # GLOBAL SYNTHESIS & 2-PASS NORMALIZATION
    # ==========================================================================

    def summarize_galaxy_metrics(self, stars: List[Dict[str, Any]], singularity: List[Dict[str, Any]]) -> Dict[str, Any]:
        """[GLOBAL SYNTHESIS] Executes Pass 2 Normalization and aggregates health metrics."""
        
        # Execute Pass 2: Temporal Normalization across the Universe
        self._normalize_temporal_metrics(stars)
        
        total_files = len(stars) + len(singularity)
        if total_files == 0: 
            return {}

        self.logger.info(f"Synthesizing galaxy metrics across {total_files} artifacts ({len(stars)} visible, {len(singularity)} dark matter)...")
        
        # Safely extract score averages from the risk_vector list via mapping
        def get_avg(metric_name):
            if metric_name not in self.RISK_SCHEMA: return 0.0
            idx = self.RISK_SCHEMA.index(metric_name)
            scores = [s["risk_vector"][idx] for s in stars if "risk_vector" in s and len(s["risk_vector"]) > idx]
            return round(statistics.mean(scores), 3) if scores else 0.0

        lang_comp = {}
        total_loc = 0
        for s in stars:
            lang = s.get("lang_id", "unknown")
            loc = s.get("coding_loc", 0)
            total_loc += loc
            if lang not in lang_comp: lang_comp[lang] = {"files": 0, "loc": 0}
            lang_comp[lang]["files"] += 1
            lang_comp[lang]["loc"] += loc

        churn_idx = self.RISK_SCHEMA.index("churn")
        high_volatility = len([s for s in stars if "risk_vector" in s and len(s["risk_vector"]) > churn_idx and s["risk_vector"][churn_idx] > 80.0])
        volatility_idx = round(high_volatility / max(len(stars), 1), 3)
        darkness_ratio = round(len(singularity) / max(total_files, 1), 3)

        self.logger.info(f"Synthesis Complete | Volatility Index: {volatility_idx:.2f} | Darkness Ratio: {darkness_ratio * 100:.1f}%")

        # --- NEW: Constellation Aggregation Logic ---
        constellations_data = {}
        for s in stars:
            c_name = s.get("constellation", "__monolith__")
            if c_name not in constellations_data: 
                constellations_data[c_name] = {"count": 0, "mass": 0.0, "risks": [0.0] * len(self.RISK_SCHEMA)}
            
            constellations_data[c_name]["count"] += 1
            constellations_data[c_name]["mass"] += s.get("file_impact", 0.0)
            
            for i, val in enumerate(s.get("risk_vector", [])):
                if i < len(self.RISK_SCHEMA): 
                    constellations_data[c_name]["risks"][i] += val
                    
        c_metrics = {
            name: {
                "file_count": data["count"], 
                "total_mass": round(data["mass"], 2), 
                "avg_exposures": {
                    self.RISK_SCHEMA[i]: round(data["risks"][i] / data["count"], 2) 
                    for i in range(len(self.RISK_SCHEMA))
                }
            } 
            for name, data in constellations_data.items()
        }

        return {
            "summary": {
                "total_files": total_files,
                "visible_stars": len(stars),
                "total_loc": total_loc,
                "dominant_language": self._get_dominant_lang(lang_comp),
                "volatility_index": volatility_idx,
                "Percent_Visible": round((1 - darkness_ratio) * 100, 1)
            },
            "singularity": {
                "ambig_file_count": len(singularity),
            },
            "health": {
                "avg_cognitive_load": get_avg("cognitive_load"),
                "avg_safety_score": get_avg("safety_score"),
                "avg_tech_debt": get_avg("tech_debt"),
                "avg_documentation": get_avg("documentation")
            },
            "composition": lang_comp,
            "constellations": c_metrics
        }
        
    def _normalize_temporal_metrics(self, stars: List[Dict[str, Any]]):
        """[PASS 2] Normalizes churn using a Logarithmic Curve for better UI gradients."""
        if not stars: return
        max_freq = 0.0
        
        # Pass 2.A: Find the volcano (Global Max)
        for s in stars:
            freq = s.get("telemetry", {}).get("raw_churn_freq", 0.0)
            if freq > max_freq:
                max_freq = freq
                
        # THE FIX: Apply a logarithmic curve to the maximum ceiling
        # math.log1p safely handles 0 values (log(1 + x))
        safe_max_f = math.log1p(max(max_freq, 1.0))
        idx = self.RISK_SCHEMA.index("churn")
        
        # Pass 2.B: Normalize every star against the logarithmic curve
        for s in stars:
            freq = s.get("telemetry", {}).get("raw_churn_freq", 0.0)
            
            # THE FIX: Apply the same logarithmic curve to the individual file
            base_score = (math.log1p(freq) / safe_max_f) * 100.0
            
            mp = s.get("telemetry", {}).get("multipliers", {}).get("churn", 1.0)
            final_churn = min(base_score * mp, 100.0)
            
            # Inject Churn directly into the correct Risk Vector index
            if "risk_vector" in s and len(s["risk_vector"]) > idx:
                s["risk_vector"][idx] = round(final_churn, 2)

    # ==========================================================================
    # FORENSIC EQUATIONS (The Physics Models)
    # ==========================================================================
   
    def _calc_raw_temporal_signals(self, temp: Dict[str, Any]) -> Tuple[float, float]:
        """Calculates Stability (Age) and Raw Churn (Seismic Frequency)."""
        if not temp or not temp.get("is_git_tracked", False):
            return 50.0, 0.0 

        mtime = temp.get("mtime", 0.0)
        repo_min = temp.get("repo_min_time", mtime)
        repo_max = temp.get("repo_max_time", mtime)
        commits = temp.get("commit_count", 0)

        # ---> THE FIX: Clamp the time difference so it never goes negative <---
        seconds_from_max = max(repo_max - mtime, 0.0)
        time_range = max(repo_max - repo_min, 1.0)
        
        # 1. Stability (0 = Newest/Surface, 100 = Oldest/Bedrock)
        stability_ratio = seconds_from_max / time_range
        stability_score = min(stability_ratio * 100.0, 100.0)

        # 2. Raw Churn Frequency 
        age_weeks = max(seconds_from_max / 604800.0, 1.0) 
        raw_churn_freq = commits / math.sqrt(age_weeks)
        
        return stability_score, raw_churn_freq

    def _calc_ownership_entropy(self, authors: Dict[str, int]) -> float:
        """
        Calculates Ownership Entropy (Shannon Entropy) for the file.
        0 = Single Author (Pure Ownership/Stable), 100 = Highly Distributed (Vibrating/White).
        """
        if not authors:
            return 0.0
            
        total_commits = sum(authors.values())
        if total_commits == 0:
            return 0.0
            
        entropy = 0.0
        for count in authors.values():
            if count > 0:
                p_i = count / total_commits
                entropy -= p_i * math.log2(p_i)
                
        # Scale to 0-100 score as defined in spec: OwnershipScore = min(H * 32, 100)
        ownership_score = min(entropy * 32.0, 100.0)
        
        return round(ownership_score, 2)

    def _calc_civil_war(self, eq: Dict[str, int]) -> float:
        """
        Calculates Layout Unity (Tabs vs Spaces). 
        0 = Pure Tabs (Green), 100 = Pure Spaces (Yellow), 50 = War Zone (Blue).
        """
        tab_lines = eq.get('indent_tabs', 0)
        space_lines = eq.get('indent_spaces', 0)
        
        l_total = tab_lines + space_lines
        
        # 2. Handle Void States (No indentation at all)
        if l_total == 0:
            return 50.0 # Default to Neutral Blue
            
        # 3. Calculate Space-Ratio (R)
        space_ratio = space_lines / l_total
        
        # 4. Final Score Mapping (0-100)
        return space_ratio * 100.0
    
    def _calc_cog_load(self, loc: int, eq: Dict[str, int], irc: int, fc: float, mp: float) -> Tuple[float, float]:
        safe_loc = max(loc, 1)
        t = self.risk_tuning.get("cognitive_load", {})
        
        if safe_loc < 15:
            total_density = sum([eq.get(k, 0) for k in ["branch", "flux", "concurrency", "heat_triggers", "danger"]]) / safe_loc + (irc / safe_loc)
            return 5.0, total_density
            
        branches = eq.get("branch", 0)
        if branches == 0 and safe_loc > 50:
            return 0.0, 0.0
            
        branch_density = branches / safe_loc
        flux_density = eq.get("flux", 0) / safe_loc
        concurrency_density = eq.get("concurrency", 0) / safe_loc
        heat_density = eq.get("heat_triggers", 0) / safe_loc
        danger_density = eq.get("danger", 0) / safe_loc
        
        clamped_branch = min(branch_density * 1.0, t.get("branch_clamp", 0.5))
        clamped_flux = min(flux_density * t.get("flux_mult", 2.0), t.get("flux_clamp", 0.75)) 
        heavy_logic = (concurrency_density * t.get("async_mult", 3.0)) + (heat_density * t.get("heat_mult", 5.0)) + (danger_density * t.get("danger_mult", 5.0))
        
        total_density = clamped_branch + clamped_flux + heavy_logic + (irc / safe_loc)
        
        if safe_loc <= 2 and total_density == 0:
            return 0.0, total_density
            
        try:
            raw_score = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 4.0) * (total_density - t.get("sigmoid_offset", 0.75))))
        except OverflowError:
            raw_score = 100.0 if total_density > t.get("sigmoid_offset", 0.75) else 0.0
            
        doc_coverage = (eq.get("doc", 0) * t.get("doc_mult", 10.0)) / safe_loc
        cooling = max(0.5, 1.0 - (doc_coverage * fc))
        
        return min(raw_score * cooling * mp, 100.0), total_density

    def _calc_safety(self, loc: int, eq: Dict[str, int], irc: int, fc: float, mp: float) -> float:
        safe_loc = max(loc, 1)
        t = self.risk_tuning.get("safety", {})
        
        attack_hits = (eq.get("danger", 0) * t.get("danger_weight", 4.0)) + (eq.get("safety_neg", 0) * t.get("safety_neg_weight", 1.5)) + (eq.get("flux", 0) * t.get("flux_weight", 0.5))
        defense_hits = (eq.get("safety", 0) * self.WEIGHT_DEFENSE) + (eq.get("test", 0) * t.get("test_weight", 0.5)) + (eq.get("doc", 0) * t.get("doc_weight", 0.1))
        
        if attack_hits == 0:
            return 0.0
            
        smoothed_loc = safe_loc + t.get("laplace_smoothing", 20.0)
        attack = ((attack_hits + irc) / smoothed_loc) * mp
        defense = (defense_hits / smoothed_loc) * fc
        
        systems_buffer = t.get("systems_buffer", 0.25) if fc < 1.0 else 0.0
        net_exposure = (attack - defense) - systems_buffer
        
        try:
            score = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 12.0) * net_exposure))
        except OverflowError:
            score = 100.0 if net_exposure > 0 else 0.0

        danger_density = (eq.get("danger", 0) + eq.get("safety_neg", 0)) / safe_loc
        if danger_density > t.get("breach_density_min", 0.03) and attack > defense:
            floor = min(t.get("breach_floor_max", 80.0), 30.0 + (danger_density * t.get("breach_floor_mult", 500.0)))
            score = max(score, floor)
            
        return max(score, 0.0)

    def _calc_tech_debt(self, loc: int, eq: Dict[str, int], irc: int, mp: float) -> float:
        t = self.risk_tuning.get("tech_debt", {})
        good_debt = eq.get("planned_debt", 0)
        bad_debt = eq.get("fragile_debt", eq.get("keyword_debt", 0))
        stubs = eq.get("func_empty", 0)
        
        if good_debt == 0 and bad_debt == 0 and stubs == 0:
            return 0.0
        
        stress = (good_debt * t.get("good_debt_weight", 1.0)) + (bad_debt * t.get("bad_debt_weight", 3.0)) + (stubs * t.get("stub_weight", 0.5)) + (irc * t.get("irc_weight", 0.5))
        density = (stress / max(loc, 1)) * 100.0
        threshold = t.get("threshold", 5.0)
        
        try:
            raw_score = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 0.5) * (density - threshold)))
        except OverflowError:
            raw_score = 100.0 if density > threshold else 0.0
            
        return min(raw_score * mp, 100.0)

    def _calc_documentation(self, loc: int, doc_loc: int, eq: Dict[str, int], fc: float, irc: int, mp: float) -> float:
        t = self.risk_tuning.get("documentation", {})
        weighted_points = (eq.get("doc", 0) * t.get("doc_weight", 1.0)) + (eq.get("ownership", 0) * t.get("ownership_weight", 0.5)) + (doc_loc * t.get("doc_loc_weight", 0.33))
        density = (weighted_points / loc) * 100.0
        
        if loc <= 2 and doc_loc == 0:
            return 0
        
        threshold = (t.get("threshold_base", 10.0) + irc) * mp
        try:
            raw_risk = 100.0 / (1.0 + math.exp(t.get("sigmoid_slope", 0.2) * (density - threshold)))
        except OverflowError:
            raw_risk = 0.0 if density > threshold else 100.0
            
        return min(raw_risk * (2.0 - fc), 100.0)

    def _calc_verification(self, loc: int, file_path: str, is_protected: bool, eq: Dict[str, int], irc: int, fc: float, mp: float, umbrella_bonus: float = 0.0) -> float:
        import os
        filename = os.path.basename(file_path).lower()
        ext = filename.split('.')[-1] if '.' in filename else ""
        
        exempt_exts = self.asset_masks.get("UNTESTABLE_EXTENSIONS", set())
        exempt_names = self.asset_masks.get("UNTESTABLE_NAMES", set())
             
        if ext in exempt_exts or filename in exempt_names or filename.startswith('readme') or 'makefile' in filename or 'cmake' in filename:
            return 0.0

        t = self.risk_tuning.get("verification", {})
        safe_loc = max(loc, 1)
        
        sibling_bonus = t.get("sibling_bonus", 30.0) if is_protected else 0.0
        internal_density = (eq.get("test", 0) * t.get("internal_test_mult", 5.0) / safe_loc) * 100.0
        total_density = internal_density + sibling_bonus 
        
        threshold = (t.get("threshold_base", 15.0) + (irc * t.get("irc_mult", 3.0))) * mp
        
        try:
            raw_exposure = 100.0 / (1.0 + math.exp(t.get("sigmoid_slope", 0.25) * (total_density - threshold)))
        except OverflowError:
            raw_exposure = 0.0 if total_density > threshold else 100.0
            
        final_exposure = raw_exposure * (2.0 - fc)

        # Uses the globally defined threshold rather than hardcoded 300
        if safe_loc > self.MASSIVE_FILE_THRESHOLD:
            mass_penalty = min((safe_loc - self.MASSIVE_FILE_THRESHOLD) / t.get("mass_penalty_div", 20.0), t.get("mass_penalty_max", 40.0)) 
            final_exposure += mass_penalty

        return min(max(final_exposure, t.get("risk_floor", 15.0)), 100.0)
    
    def _calc_graveyard(self, total_loc: float, eq: Dict[str, int], mp: float) -> float:
        hits = eq.get("graveyard", 0)
        if hits == 0:
            return 0.0
            
        t = self.risk_tuning.get("graveyard", {})
        ghost_lines = hits * t.get("hit_mult", 3.0)
        density = (ghost_lines / max(total_loc, t.get("safe_mass_floor", 50.0))) * 100.0
        
        threshold = t.get("threshold_base", 10.0) / max(mp, 0.1) 
        try:
            score = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 0.3) * (density - threshold)))
        except OverflowError:
            score = 100.0 if density > threshold else 0.0
            
        return min(score, 100.0)

    def _calc_api_exposure(self, eq: Dict[str, int], mp: float) -> float:
        api_hits = eq.get("api", 0)
        if api_hits == 0:
            return 0.0
            
        t = self.risk_tuning.get("api_exposure", {})
        entities = max(eq.get("func_start", 0) + eq.get("class_start", 0), 1)
        ratio = min(api_hits / float(entities), 1.0)
        volume_weight = min(math.log10(api_hits + 1) / t.get("log_divisor", 1.5), 1.0)
        raw_score = ((ratio * t.get("ratio_weight", 0.4)) + (volume_weight * t.get("volume_weight", 0.6))) * 100.0
        
        return min(raw_score * mp, 100.0)

    def _calc_concurrency(self, loc: int, eq: Dict[str, int], irc: int, mp: float) -> float:
        hits = eq.get("concurrency", 0)
        if hits == 0:
            return 0.0
            
        t = self.risk_tuning.get("concurrency", {})
        weighted_hits = hits + (irc * t.get("irc_mult", 0.1))
        density = (weighted_hits / max(loc, 1)) * 100.0
        threshold = t.get("threshold_base", 4.0) * mp
        
        try:
            score = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 0.4) * (density - threshold)))
        except OverflowError:
            score = 100.0 if density > threshold else 0.0
            
        return min(score, 100.0)

    def _calc_state_flux(self, loc: int, eq: Dict[str, int], irc: int, mp: float) -> float:
        hits = eq.get("flux", 0)
        if hits == 0: return 0.0
                
        t = self.risk_tuning.get("state_flux", {})
        density = ((hits + (irc * t.get("irc_mult", 0.15))) / max(loc, 1)) * 100.0
        threshold = t.get("threshold_base", 15.0) * mp
        
        try:
            score = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 0.20) * (density - threshold)))
        except OverflowError:
            score = 100.0 if density > threshold else 0.0
            
        return min(score, 100.0)

    def _calc_spec_alignment(self, eq: Dict[str, int], mp: float) -> float:
        entities = max(eq.get("func_start", 0) + eq.get("class_start", 0), 1)
        ratio = min(eq.get("spec_exposure", 0) / entities, 1.0)
        return min((1.0 - ratio) * 100.0 * mp, 100.0)
    
    # --------------------------------------------------------------------------
    # REPORTING UTILITIES
    # --------------------------------------------------------------------------

    def generate_forensic_report(self, stars: List[Dict[str, Any]]) -> Dict[str, Any]:
        """[FORENSIC RANKING] Generates Top/Bottom 3 for dynamically indexed exposures."""
        if not stars: return {}
        self.logger.info("Generating forensic exposure rankings...")

        # ====================================================================
        # THE ACTIVE LOGIC MASK
        # 1. Define the structural assets that should be invisible to risk rankings
        # ====================================================================
        STRUCTURAL_ASSETS = self.asset_masks.get("STRUCTURAL_ASSETS", set())

        # 2. Filter the stars to ONLY include active executable logic
        active_stars = [
            star for star in stars 
            if star.get("lang_id", "unknown").lower() not in STRUCTURAL_ASSETS
        ]

        # 3. Fallback: If a repo is *only* markdown/data files, don't crash
        if not active_stars:
            active_stars = stars

        # 4. Generate rankings using ONLY the masked `active_stars` list
        report = {
            "exposures": {},
            "file_impact": self._rank_list(active_stars, key_path=["file_impact"]),
            "function_impact": self._generate_function_rankings(active_stars)
        }

        for idx, rk in enumerate(self.RISK_SCHEMA):
            report["exposures"][rk] = self._rank_list(active_stars, key_path=["risk_vector", idx])
            
        return report

    def _get_locational_multipliers(self, path: str) -> Dict[str, float]:
        """Matches path against regex configurations and extracts applicable Modifiers."""
        active_multipliers = {}
        bridge = {
            'Cognitive Load Exposure': 'cog', 'Safety Exposure': 'safety',
            'Tech Debt Exposure': 'debt', 'Documentation Exposure': 'doc',
            'Testing Exposure': 'test', 'Dead Code Exposure': 'dead',
            'API Exposure': 'api', 'Concurrency Exposure': 'async',
            'State Flux Exposure': 'flux', 'Specification Exposure': 'spec',
            'Churn Exposure': 'churn'
        }

        for category, modifiers in self.path_modifiers.items():
            signal_key = bridge.get(category)
            if not signal_key: continue
            
            for pattern, multiplier in modifiers:
                if hasattr(pattern, 'search') and pattern.search(path):
                    active_multipliers[signal_key] = multiplier
                    break
                elif isinstance(pattern, str) and re.search(pattern, path):
                    active_multipliers[signal_key] = multiplier
                    break
                    
        return active_multipliers

    def _rank_list(self, stars: List[Dict[str, Any]], key_path: List[Any]) -> Dict[str, List[Dict[str, Any]]]:
        """Extracts top and bottom ranks safely navigating dictionaries and lists."""
        def get_val(s):
            curr = s
            for k in key_path: 
                if isinstance(curr, dict):
                    curr = curr.get(k, 0.0)
                elif isinstance(curr, list) and isinstance(k, int) and k < len(curr):
                    curr = curr[k]
                else:
                    return 0.0
            return float(curr) if isinstance(curr, (int, float)) else 0.0
        
        sorted_stars = sorted(stars, key=get_val, reverse=True)
        return {
            "highest": [{"name": s.get("name", "unknown"), "path": s.get("path", ""), "value": get_val(s)} for s in sorted_stars[:3]],
            "lowest": [{"name": s.get("name", "unknown"), "path": s.get("path", ""), "value": get_val(s)} for s in reversed(sorted_stars[-3:])]
        }

    def _generate_function_rankings(self, stars: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        all_funcs = []
        for s in stars:
            for sat in s.get("satellites", []):
                if isinstance(sat, dict):
                    all_funcs.append({
                        "name": sat.get("name", "anon"), 
                        "file": s.get("name", "unknown"), 
                        "impact": sat.get("impact", 0), 
                        "loc": sat.get("loc", 0)
                    })
        all_funcs.sort(key=lambda x: x["impact"], reverse=True)
        return {"highest": all_funcs[:3], "lowest": all_funcs[-3:] if len(all_funcs) >= 3 else all_funcs}

    def _get_tier(self, lang_id: str) -> str:
        explicit = {'rust', 'go', 'swift', 'java', 'typescript', 'csharp', 'dart'}
        structured = {'python', 'javascript', 'cpp', 'c', 'ruby', 'kotlin', 'php'}
        if lang_id in explicit: return "tier1"
        if lang_id in structured: return "tier2"
        return "tier3"

    def _get_dominant_lang(self, composition: Dict[str, Dict[str, int]]) -> str:
        if not composition: return "mixed"
        return max(composition.items(), key=lambda x: x[1]['loc'])[0]