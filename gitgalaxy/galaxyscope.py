# ==============================================================================
# GitGalaxy
# Copyright (c) 2026 Joe Esquibel
#
# This source code is licensed under the PolyForm Noncommercial License 1.0.0.
# You may not use this file except in compliance with the License.
# A copy of the license can be found in the LICENSE file in the root directory
# of this project, or at https://polyformproject.org/licenses/noncommercial/1.0.0/
# ==============================================================================
import logging
import time
import zipfile
import tempfile
import shutil
import sys
import re
import os
import subprocess
import multiprocessing
import concurrent.futures
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Union, Set
from collections import defaultdict

# Hardware Layer (Strategy v6.2 Protocol - Optical Pipeline)
from .aperture import ApertureFilter, ApertureError, InaccessibleArtifactError
from .guidestar_lens import GuideStarLens 
from .language_lens import LanguageDetector, FocusingError
from .prism import Prism, RefractionError
from .detector import LogicSplicer, Cartographer
from .chronometer import Chronometer
from .signal_processor import SignalProcessor
from .spectral_auditor import SpectralAuditor
from .gpu_recorder import GPURecorder
from .audit_recorder import AuditRecorder
from .llm_recorder import LLMRecorder
from .security_lens import SecurityLens
# Load Universal Laws from config
from . import gitgalaxy_standards_v1 as scanning_config

logger = logging.getLogger("GalaxyScope")

# ==============================================================================
# WORKER PROCESS: ISOLATED MEMORY SPACE FOR PASS 1 (CPU BOUND)
# ==============================================================================
# Top-level functions to bypass Python's Multi-Processing pickling limitations

_worker_state = {}

# ------START: Updated _init_worker to accept git_tracked files for intent caching


def _init_worker(root_str: str, config: Dict[str, Any], ext_tally: Dict[str, int], log_level: int, git_tracked: Set[str], census: Set[str]):
    """
    Initializes the CPU-bound optical modules within the worker process's isolated memory.
    
    PERFORMANCE FIX: 
    Force-warms pseudo-languages (plaintext/markdown) to kill the 'Plaintext Stutter'.
    This prevents [AUTO-HEAL] log spam and redundant regex compilation.
    """
    global _worker_state
    
    logging.getLogger().setLevel(log_level)
    worker_logger = logging.getLogger("GalaxyScope.Worker")

    root = Path(root_str)
    lang_defs = config.get("LANGUAGE_DEFINITIONS", {})
    comm_defs = config.get("COMMENT_DEFINITIONS", {})
    aperture_cfg = config.get("APERTURE_CONFIG", {})
    priority_whitelist = config.get("PRIORITY_WHITELIST", [])
    
    # --- PERFORMANCE ANCHOR: SPLICER CACHE WARM-UP ---
    splicer_cache = {}
    from .detector import LogicSplicer
    
    # 1. Force-warm the fallbacks immediately.
    # This silences the [AUTO-HEAL] warnings and compiles the regex engine for these IDs.
    for fallback_id in ["plaintext", "markdown"]:
        splicer_cache[fallback_id] = LogicSplicer(fallback_id, lang_defs, parent_logger=worker_logger)
    
    # 2. Warm up active project languages based on extensions found in Pass 0.
    active_langs = set()
    for ext in ext_tally.keys():
        for l_id, l_cfg in lang_defs.items():
            if ext in l_cfg.get('extensions', []):
                active_langs.add(l_id)
                break
    
    for lang_id in active_langs:
        if lang_id not in splicer_cache:
            splicer_cache[lang_id] = LogicSplicer(lang_id, lang_defs, parent_logger=worker_logger)

    # --- NEW: Decide the Rules of Engagement before booting the engines ---
    if config.get("PARANOID_MODE", False):
        active_policy = scanning_config.ThreatPolicy.get_policy("paranoid")
    else:
        active_policy = scanning_config.ThreatPolicy.get_policy("baseline")

    _worker_state.update({
        'root': root,
        'config': config,
        'ext_tally': ext_tally,
        'lang_defs': lang_defs,
        'worker_logger': worker_logger,
        'git_tracked': git_tracked,
        'census': census,
        'filter': ApertureFilter(root, lang_defs, aperture_cfg, parent_logger=worker_logger),
        'guidestar': GuideStarLens(root, priority_whitelist, parent_logger=worker_logger),
        'detector': LanguageDetector(lang_defs, comm_defs),
        'prism': Prism(comm_defs, lang_defs, parent_logger=worker_logger),
        'splicer_cache': splicer_cache,
        'word_tokenizer': re.compile(r'\b\w+\b'),
        
        # --- NEW: Boot the physics engines into worker memory ---
        'chronometer': Chronometer(root, parent_logger=worker_logger),
        'signal': SignalProcessor(aperture_config=config, parent_logger=worker_logger),
        'security': SecurityLens(policy=active_policy)
        # --------------------------------------------------------
    })
    
    _worker_state['guidestar'].align_telescope()
    
def resolve_mission_control(target_name: str) -> Path:
    """Routes reports to a .env path, or defaults to the current directory."""
    env_path = os.environ.get("GITGALAXY_DATA_DIR")
    
    if env_path:
        # If the environment variable is set, drop the files EXACTLY there
        mission_dir = Path(env_path)
    else:
        # If no variable (like on a user's machine), make a safe subfolder so we don't make a mess
        mission_dir = Path.cwd() / "galaxy_reports" / target_name
        
    mission_dir.mkdir(parents=True, exist_ok=True)
    return mission_dir

def _process_file_worker(rel_path: str) -> Dict[str, Any]:
    """Processes a single file path using the worker's cached hardware modules."""
    global _worker_state
    
    # ---> START THE CLOCK FOR THE MICRO-PROFILER <---
    t_start = time.time()
    
    root = _worker_state['root']
    full_path_str = str(root / rel_path) 
    
    # --- NEW: PARALLEL PHANTOM CHECK ---
    # Silently evaporates files missing on disk to prevent main-thread anomaly logging
    if not Path(full_path_str).is_file():
        return {
            "rel_path": rel_path, 
            "status": "phantom", 
            "reason": "Phantom file (missing on disk)", 
            "data": {},
            "processing_time": time.time() - t_start
        }

    logger = _worker_state['worker_logger']
    aperture = _worker_state['filter']
    guidestar = _worker_state['guidestar']
    detector = _worker_state['detector']
    prism = _worker_state['prism']
    census = _worker_state['census']
    lang_defs = _worker_state['lang_defs']
    splicer_cache = _worker_state['splicer_cache']
    tokenizer = _worker_state['word_tokenizer']
    
    # --- NEW: Extract the physics engines from worker memory ---
    chronometer = _worker_state['chronometer']
    signal = _worker_state['signal']
    security = _worker_state['security']
    # -----------------------------------------------------------
    
    has_prior, intent_vector = guidestar.get_intent_status(full_path_str)
    observation = {"rel_path": rel_path, "status": "filtered", "reason": "Aperture block", "data": {}}

    # --- PHASE PROFILING STATE ---
    is_file_profiling = _worker_state['config'].get("FILE_SPEED", False)
    is_profiling = _worker_state['config'].get("SPLICING_SPEED", False)
    phase_times = {}

    try:
        # Phase 1: Aperture Filter
        t_aperture = time.perf_counter()
        is_valid, size_bytes, reason = aperture.evaluate_path_integrity(full_path_str, has_intent=has_prior)
        if is_file_profiling: phase_times["1_Aperture_Filter"] = time.perf_counter() - t_aperture
        
        if not is_valid:
            observation["status"] = "singularity"
            observation["reason"] = reason
            observation["size_bytes"] = size_bytes 
            observation["processing_time"] = time.time() - t_start
            return observation
            
        # Phase 2: Disk I/O
        t_io = time.perf_counter()
        try:
            with open(full_path_str, 'r', encoding='utf-8', errors='ignore') as f:
                content_buffer = f.read()
        except FileNotFoundError:
            # Replaces the Phantom Check! Fast, zero-overhead disk failure routing.
            observation["status"] = "phantom"
            observation["reason"] = "Phantom file (missing on disk)"
            observation["processing_time"] = time.time() - t_start
            return observation
        except Exception as e:
            observation["reason"] = f"I/O Error: {str(e)}"
            observation["processing_time"] = time.time() - t_start
            return observation
        if is_file_profiling: phase_times["2_Disk_IO"] = time.perf_counter() - t_io

        filter_res = aperture.is_in_scope(full_path_str, content=content_buffer, has_intent=has_prior)
        if not filter_res["is_in_scope"]:
            observation["status"] = "singularity"
            observation["reason"] = filter_res["reason"]
            observation["processing_time"] = time.time() - t_start
            return observation

        # Phase 3: Linguistic Detector
        t_detector = time.perf_counter()
        detection_result = detector.inspect(
            full_path_str, 
            content_sample=content_buffer, 
            has_intent=has_prior, 
            intent_vector=intent_vector, 
            ext_tally=_worker_state.get('ext_tally', {}),
            census=_worker_state['census']
        )
        if is_file_profiling: phase_times["3_Language_Detector"] = time.perf_counter() - t_detector
        
        lang_id = detection_result["lang_id"]
        is_supported = lang_id in lang_defs or lang_id in ("plaintext", "markdown")
        
        if lang_id in ("undeterminable", "unknown") or not is_supported:
            observation["status"] = "singularity"
            observation["reason"] = f"Unsupported Format (.{lang_id})" 
            observation["identity_confidence"] = detection_result.get("intensity", 0.0)
            observation["processing_time"] = time.time() - t_start
            return observation
        
        # Phase 4: Prism Refraction
        t_prism = time.perf_counter()
        refraction = prism.refract(content_buffer, lang_id)
        if is_file_profiling: phase_times["4_Prism_Refraction"] = time.perf_counter() - t_prism
        
        if lang_id not in splicer_cache:
            from .detector import LogicSplicer
            splicer_cache[lang_id] = LogicSplicer(lang_id, lang_defs, parent_logger=logger)
        
        splicer = splicer_cache[lang_id]
        
        # --- INJECTED DEBUG TRACE ---
        logger.debug(f"[WORKER-TRACE] >>> ENTERING SPLICER: {rel_path} (Lang: {lang_id})")
        
        # Phase 5: Logic Splicer
        t_splicer = time.perf_counter()
        logic_data = splicer.splice(
            code_stream=refraction["code_stream"], 
            comment_stream=refraction["comment_stream"],
            confidence=detection_result.get("intensity", 1.0),
            profile_regex=is_profiling
        )
        if is_file_profiling: phase_times["5_Logic_Splicer"] = time.perf_counter() - t_splicer
        
        logger.debug(f"[WORKER-TRACE] <<< EXITING SPLICER: {rel_path}")
        
        # Phase 6: Raw Imports
        t_imports = time.perf_counter()
        import_regex = lang_defs.get(lang_id, {}).get("rules", {}).get("_dependency_capture")
        raw_imports = set()
        if import_regex:
            try:
                for match in import_regex.finditer(content_buffer):
                    # Grab the first non-empty capture group (the actual dependency name)
                    extracted_path = next((g for g in match.groups() if g), None)
                    if extracted_path:
                        raw_imports.add(extracted_path)
            except Exception:
                pass
        if is_file_profiling: phase_times["6_Import_Regex"] = time.perf_counter() - t_imports

        # Phase 7: Tokenization & Census
        t_token = time.perf_counter()
        popularity_hits = set(tokenizer.findall(refraction["code_stream"])) & census
        t_end = time.perf_counter()
        if is_file_profiling: phase_times["7_Token_Intersection"] = t_end - t_token
        
        # Append the new blind-spot telemetry to the regex output
        if is_profiling:
            logic_data["regex_telemetry"] = logic_data.get("regex_telemetry", {})
            logic_data["regex_telemetry"][f"{lang_id}::Worker_Imports"] = t_token - t_imports
            logic_data["regex_telemetry"][f"{lang_id}::Worker_Popularity_Tokens"] = t_end - t_token

        data_payload = {
            "path": rel_path,
            "stem": Path(rel_path).stem.lower(), 
            "lang_id": lang_id, 
            "lock_tier": detection_result.get("lock_tier", 4),
            "intensity": detection_result.get("intensity", 0.0),
            "source_proof": detection_result.get("source_proof", "Discovery"),
            "size_bytes": filter_res.get("size_bytes", 0),
            "total_loc": filter_res.get("total_loc", 0),
            "prior_lock": has_prior,
            "coding_loc": refraction["coding_loc"],
            "doc_loc": refraction["doc_loc"],
            "raw_imports": list(raw_imports),          
            "popularity_hits": popularity_hits,
            "regex_telemetry": logic_data.pop("regex_telemetry", {}) if is_profiling else {}
        }
        
        data_payload.update(logic_data)
        data_payload["control_flow_ratio"] = logic_data.get("total_control_flow_ratio", 0.0)
        data_payload["file_impact"] = logic_data.get("sum_fxn_impact", 0.0)

        observation.update({
            "status": "success", 
            "reason": None, 
            "data": data_payload,
            "phase_times": phase_times if is_file_profiling else {}
        })

    except Exception as e:
        observation["status"] = "anomaly"
        observation["reason"] = f"Hardware failure: {str(e)}"
        
    # ---> RECORD THE FINAL TIME <---
    total_time = time.time() - t_start
    observation["processing_time"] = total_time

    # ---> NEW: REAL-TIME SLOW FILE ALERT <---
    if total_time > 10.0:
        logger.warning(f"🐌 SLOW PARSE DETECTED: '{rel_path}' took {total_time:.2f} seconds.")

    return observation

# ==============================================================================
# GitGalaxy Phase 3: Pipeline Orchestrator (The GalaxyScope)
# Strategy v6.2 Protocol: Bayesian Optics & Singularity Bypasses
# ==============================================================================

class Orchestrator:
    """Mission Control: The GitGalaxy Central Processing Core."""

    def __init__(self, target_input: Union[str, Path], config: Dict[str, Any], version: str = "6.2.0"):
        self.config = config
        self.version = version
        self.temp_dir: Optional[str] = None
        self.root = self._prepare_target(target_input)
        
        lang_defs = config.get("LANGUAGE_DEFINITIONS", {})
        comm_defs = config.get("COMMENT_DEFINITIONS", {})
        aperture_cfg = config.get("APERTURE_CONFIG", {})
        priority_whitelist = config.get("PRIORITY_WHITELIST", [])
        
        # Sensor Submodules
        self.filter = ApertureFilter(self.root, lang_defs, aperture_cfg, parent_logger=logger)        
        self.guidestar = GuideStarLens(self.root, priority_whitelist, parent_logger=logger)
        self.chronometer = Chronometer(self.root, parent_logger=logger)
        self.cartographer = Cartographer(parent_logger=logger)
        self.processor = SignalProcessor(aperture_config=config, parent_logger=logger)
        self.auditor = SpectralAuditor(parent_logger=logger) 
        
        # --- UPDATED: Instantiate New Dual Recorders ---
        self.gpu_recorder = GPURecorder(version=self.version, parent_logger=logger)
        self.audit_recorder = AuditRecorder(parent_logger=logger)
        self.llm_recorder = LLMRecorder(parent_logger=logger)
        
        # --- NEW: THE SMART THREAT SWITCH (MAIN THREAD) ---
        if self.config.get("PARANOID_MODE", False):
            active_policy = scanning_config.ThreatPolicy.get_policy("paranoid")
        else:
            active_policy = scanning_config.ThreatPolicy.get_policy("baseline")

        self.security_analyzer = SecurityLens(policy=active_policy)
        # --------------------------------------------------
        
        # State Arrays
        self.census: Set[str] = set()
        self.stem_map: Dict[str, str] = {}
        self.cryolink: Dict[str, Dict[str, Any]] = {}
        self.stars: List[Dict[str, Any]] = []
        self.singularity_candidates: List[Dict[str, Any]] = [] 
        self.anomalies: List[Dict[str, str]] = []
        self.popularity_scores: Dict[str, int] = {}
        self.ext_tally: Dict[str, int] = {}
        self.git_tracked_files: Set[str] = set()
        
        # ---> NEW: NEIGHBORHOOD MICRO-MASS QUOTA STATE <---
        self.MICRO_MASS_BYTES = 50
        self.MICRO_MASS_GRACE_LIMIT = 15
        self.neighborhood_tracker = defaultdict(int)
        
        self.splicing_telemetry = {
            "top_slowest": [], 
            "regex_totals": defaultdict(float),
            "files_sampled": 0,
            "regex_limit_reached": False
        }
        
        self.file_speed_telemetry = {
            "phase_totals": defaultdict(float),
            "file_count": 0
        }

    def run_mission(self, output_file: str = "galaxy.json"):
        """Executes the synthesis protocol with dual-recorder exit strategy."""
        start_time = time.time()
        logger.info(f"--- MISSION_IGNITION: {self.root.name} (v{self.version}) ---")

        try:
            # PHASE 0: Radar & Pre-Flight
            t_phase = time.time()
            self.guidestar.align_telescope()
            self._ignite_radar()
            logger.info(f"⏱️ MACRO-CLOCK [Phase 0 - Radar]: {time.time() - t_phase:.2f}s")

            # PHASE 1: Workers & IPC Transfer
            t_phase = time.time()
            self._first_pass_extraction()
            logger.info(f"⏱️ MACRO-CLOCK [Phase 1 - Workers & IPC]: {time.time() - t_phase:.2f}s")

            # PHASE 1.5: Dependency Resolution
            t_phase = time.time()
            self._calculate_galactic_popularity()
            logger.info(f"⏱️ MACRO-CLOCK [Phase 1.5 - Imports]: {time.time() - t_phase:.2f}s")

            # PHASE 2: Relational Physics
            t_phase = time.time()
            self._second_pass_relational()
            logger.info(f"⏱️ MACRO-CLOCK [Phase 2 - Relational]: {time.time() - t_phase:.2f}s")

            # PHASE 4: Audit Verification
            t_phase = time.time()
            visible_galaxy, audit_singularity = self.auditor.audit(self.stars)
            total_singularity = self.singularity_candidates + audit_singularity
            logger.info(f"⏱️ MACRO-CLOCK [Phase 4 - Auditor]: {time.time() - t_phase:.2f}s")
            
            # PHASE 5: 3D Cartography
            t_phase = time.time()
            if visible_galaxy:
                visible_galaxy = self.cartographer.map_galaxy(visible_galaxy)
            stars_mapped_count = len(visible_galaxy) if visible_galaxy else 0
            logger.info(f"⏱️ MACRO-CLOCK [Phase 5 - Cartography]: {time.time() - t_phase:.2f}s")
            
            # PHASE 6: Metrics Synthesis
            t_phase = time.time()
            summary = self.processor.summarize_galaxy_metrics(visible_galaxy, total_singularity)
            report = self.processor.generate_forensic_report(visible_galaxy)
            logger.info(f"⏱️ MACRO-CLOCK [Phase 6 - Synthesis]: {time.time() - t_phase:.2f}s")
            
            # --- PHASE 7.5: SHARED METADATA LOCKING ---
            # Calculate physical mass before the GPU Recorder destroys the visible_galaxy list
            total_loc = sum(s.get("total_loc", 0) for s in (visible_galaxy or []))
        
            # Calculate rate using exact precision BEFORE rounding for display
            raw_duration = time.time() - start_time
            loc_per_sec = int(total_loc / raw_duration) if raw_duration > 0 else 0
            duration = round(raw_duration, 2)

            session_meta = {
                "engine": f"GitGalaxy Scope v{self.version}",
                "target": self.root.name,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "duration_seconds": duration,
                "target_directory": str(self.root.resolve()),
                "git_audit": self._get_git_audit()
            }
            
            if "singularity" not in summary: 
                summary["singularity"] = {}
                
            # Pass the array into the function, and merge the results directly
            summary["singularity"].update(self._summarize_anomalies(total_singularity))

            # --- THE NEW ROUTER ---
            mission_dir = resolve_mission_control(self.root.name)
            output_file = str(mission_dir / Path(output_file).name)
            # ----------------------
            
            # --- CHECK EXCLUSIVE MODE FLAGS ---
            exclusive_mode = self.config.get("LLM_ONLY") or self.config.get("GPU_ONLY") or self.config.get("AUDIT_ONLY")
            audit_output = "Skipped"

            # ==========================================================
            # PHASE 8: AUDIT RECORDER (Non-Destructive Forensic Fork)
            # ==========================================================
            if not exclusive_mode or self.config.get("AUDIT_ONLY"):
                try:
                    out_path = Path(output_file)
                    audit_output = str(out_path.with_name(f"{out_path.stem}_audit{out_path.suffix}"))
                    logger.info(f"AUDIT: Generating comprehensive human-readable forensic log -> {audit_output}")
                    
                    self.audit_recorder.generate_report(
                        stars=visible_galaxy,
                        singularity=total_singularity,
                        summary=summary,
                        forensic_report=report,
                        session_meta=session_meta,
                        output_path=audit_output
                    )
                except Exception as e:
                    logger.error(f"AUDIT_FAILURE: Could not generate forensic log. {e}", exc_info=True)

            # ==========================================================
            # PHASE 8.5: LLM RECORDER (The AI Translation Layer)
            # ==========================================================
            if not exclusive_mode or self.config.get("LLM_ONLY"):
                try:
                    output_dir = str(Path(output_file).parent)
                    logger.info(f"LLM: Generating AI translation artifacts -> {output_dir}")
                    
                    self.llm_recorder.generate_artifacts(
                        stars=visible_galaxy,
                        singularity=total_singularity,
                        summary=summary,
                        session_meta=session_meta,
                        output_dir=output_dir,
                        forensic_report=report
                    )
                except Exception as e:
                    logger.error(f"LLM_FAILURE: Could not generate AI artifacts. {e}", exc_info=True)

            # ==========================================================
            # PHASE 9: GPU RECORDER (Destructive Columnar Pivot)
            # ==========================================================
            if not exclusive_mode or self.config.get("GPU_ONLY"):
                logger.info(f"GPU: Generating minified payload -> {output_file}")
                # record_mission destructively clears RAM as it pivots
                payload = self.gpu_recorder.record_mission(
                    stars=visible_galaxy,
                    singularity=total_singularity,
                    summary=summary,
                    forensic_report=report,
                    repo_name=self.root.name
                )
                
                payload["meta"]["session"] = session_meta
                self.gpu_recorder.save_minified(payload, output_file)

            logger.info(f"--- MISSION_SUCCESS: {stars_mapped_count} stars mapped in {duration}s ---")
            logger.info(f"--- ENGINE_TELEMETRY: Processed {total_loc:,} lines of code at {loc_per_sec:,} LOC/s ---")
            logger.info(f"--- ARCHIVES_SEALED: {output_file} & {audit_output} ---")
            
            if self.config.get("FILE_SPEED"):
                self._render_file_speed_chart()

            if self.config.get("SPLICING_SPEED"):
                self._render_splicing_chart()
                
            # --- THE FINAL CALL TO ACTION (CLI BILLBOARD) ---
            print("\n" + "="*75)
            print(" 🌌 READY FOR VISUALIZATION (100% LOCAL / ZERO UPLOAD)")
            print("="*75)
            print(" 1. Open your browser to: \033[94m\033[4mhttps://gitgalaxy.io/\033[0m")
            print(f" 2. Drag and drop '{output_file}'")
            print("\n * PRIVACY SECURED: Your data never leaves your machine.")
            print("   All architectural rendering executes locally in your browser.")
            print("="*75 + "\n")
            
        except Exception as e:
            logger.critical(f"FATAL_SYSTEM_COLLAPSE: {str(e)}", exc_info=True)
            raise
        finally:
            self.cleanup()
            
    def _ignite_radar(self):
        """Phase 0: Building the Census via Git Authority with Fallback."""
        try:
            raw_output = subprocess.check_output(
                ['git', 'ls-files'], cwd=self.root, text=True, stderr=subprocess.DEVNULL
            )
            git_paths = raw_output.splitlines()
            self.git_tracked_files = set(git_paths)
            
            # --- FAST I/O: ThreadPool for os.stat operations ---
            def _inspect_path(rel_path):
                path_obj = Path(rel_path)
                full_path = self.root / path_obj
                has_intent, _ = self.guidestar.get_intent_status(path_obj)
                is_valid, size_bytes, reason = self.filter.evaluate_path_integrity(
                    full_path, has_intent=has_intent
                )
                return rel_path, path_obj, is_valid, size_bytes, reason

            # Use 32 threads to saturate the disk I/O queue
            with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
                inspections = executor.map(_inspect_path, git_paths)
            
            # Process the results synchronously to prevent race conditions on state maps
            for rel_path, path_obj, is_valid, size_bytes, reason in inspections:
                
                # ---> NEW: THE NEIGHBORHOOD MICRO-MASS QUOTA <---
                if is_valid and size_bytes < self.MICRO_MASS_BYTES:
                    dir_path = str(path_obj.parent)
                    self.neighborhood_tracker[dir_path] += 1
                    if self.neighborhood_tracker[dir_path] > self.MICRO_MASS_GRACE_LIMIT:
                        is_valid = False
                        reason = "Excluded: Neighborhood Micro-Mass Limit Exceeded"
                # ------------------------------------------------
                
                if is_valid:
                    stem = path_obj.stem.lower()
                    ext = path_obj.suffix.lower()
                    name = path_obj.name.lower()
                    
                    self.census.add(stem)
                    self.stem_map[rel_path] = rel_path
                    
                    self.ext_tally[ext] = self.ext_tally.get(ext, 0) + 1
                    self.ext_tally[name] = self.ext_tally.get(name, 0) + 1 
                else:
                    # Route directly to Dark Matter, bypassing the Multi-Processing pool
                    self.singularity_candidates.append({
                        "path": rel_path,
                        "reason": reason,
                        "identity_confidence": 0.0,
                        "size_bytes": size_bytes
                    })
                    self._record_anomaly(rel_path, reason)
                
            logger.info(f"CENSUS_COMPLETE: Found {len(git_paths)} tracked artifacts via Git.")

        except (subprocess.CalledProcessError, FileNotFoundError):
            self.git_tracked_files = set()
            logger.warning("GIT_NOT_FOUND: Reverting to standard filesystem walk.")
            self._standard_radar_walk()

    def _standard_radar_walk(self):
        """Standard filesystem walk for non-Git projects or ZIP archives."""
        for root, dirs, files in os.walk(self.root):
            # Add [0] to extract just the boolean 'is_valid'
            dirs[:] = [d for d in dirs if self.filter.evaluate_path_integrity(Path(root) / d)[0]]
            for file in files:
                full_p = Path(root) / file
                is_valid, size_bytes, reason = self.filter.evaluate_path_integrity(full_p)
                
                # ---> NEW: THE NEIGHBORHOOD MICRO-MASS QUOTA <---
                if is_valid and size_bytes < self.MICRO_MASS_BYTES:
                    dir_path = str(full_p.parent.relative_to(self.root))
                    self.neighborhood_tracker[dir_path] += 1
                    if self.neighborhood_tracker[dir_path] > self.MICRO_MASS_GRACE_LIMIT:
                        is_valid = False
                        reason = "Excluded: Neighborhood Micro-Mass Limit Exceeded"
                # ------------------------------------------------

                rel_p = str(full_p.relative_to(self.root))

                if is_valid:
                    stem = full_p.stem.lower()
                    ext = full_p.suffix.lower()
                    name = full_p.name.lower()  # <-- Extract lowercased filename
                    
                    self.census.add(stem)
                    self.stem_map[rel_p] = rel_p
                    
                    # ---> Tally both the extension AND the full filename
                    self.ext_tally[ext] = self.ext_tally.get(ext, 0) + 1
                    self.ext_tally[name] = self.ext_tally.get(name, 0) + 1 
                else:
                    self.singularity_candidates.append({
                        "path": rel_p,
                        "reason": reason,
                        "identity_confidence": 0.0,
                        "size_bytes": size_bytes
                    })
                    self._record_anomaly(rel_p, reason)     

    def _first_pass_extraction(self):
        """Pass 1: Parallel Refraction & Matter Eviction via Multi-Core Map-Reduce."""
        total_files = len(self.stem_map)
        logger.info(f"PASS_1: Optical sequence initiated for {total_files} artifacts via ProcessPoolExecutor.")
        
        if total_files == 0:
            return

        cpu_count = os.cpu_count()
        if cpu_count is None:
            cpu_count = 4
        max_workers = max(1, cpu_count - 1)
        
        current_log_level = logging.getLogger().getEffectiveLevel()
        completed_count = 0

        with concurrent.futures.ProcessPoolExecutor(
            max_workers=max_workers, 
            initializer=_init_worker, 
            initargs=(str(self.root), self.config, self.ext_tally, current_log_level, self.git_tracked_files, self.census)
        ) as executor:
            
            # Map futures to their file paths in a tracking dictionary
            active_futures = {
                executor.submit(_process_file_worker, rel_path): rel_path 
                for rel_path in self.stem_map.values()
            }
            
# THE STARVATION MONITOR (Event-Driven Generator)
            # as_completed yields instantly upon future completion, averting O(N^2) polling wait states.
            try:
                # THE FIX: Removed `timeout=60.0`. Python's timeout is an absolute mission timer, 
                # not an idle worker timer. Massive repositories (80k+ files) take more than 
                # 60 seconds to scan end-to-end. Infinite loops are now prevented 
                # natively by the 1500-char Line Limiter and strict Regex bounds.
                for future in concurrent.futures.as_completed(active_futures):
                    rel_path = active_futures.pop(future)
                    completed_count += 1
                    
                    if completed_count % 50 == 0:
                        logger.info(f"PROGRESS: Surveyed {completed_count}/{total_files} coordinates.")
                        
                    try:
                        res = future.result()
                        status = res["status"]
                        
                        if status == "success":
                            self.cryolink[rel_path] = res["data"]
                            
                            if self.config.get("FILE_SPEED"):
                                p_times = res.get("phase_times", {})
                                for phase, duration in p_times.items():
                                    self.file_speed_telemetry["phase_totals"][phase] += duration
                                self.file_speed_telemetry["file_count"] += 1

                            if self.config.get("SPLICING_SPEED"):
                                process_time = res.get("processing_time", 0)
                                
                                # 1. Always track the globally slowest files (bounded to save RAM)
                                self.splicing_telemetry["top_slowest"].append({
                                    "path": rel_path,
                                    "time": process_time
                                })
                                
                                # Keep the array tiny: Sort and truncate every 50 files
                                if len(self.splicing_telemetry["top_slowest"]) > 50:
                                    self.splicing_telemetry["top_slowest"].sort(key=lambda x: x["time"], reverse=True)
                                    self.splicing_telemetry["top_slowest"] = self.splicing_telemetry["top_slowest"][:10]
                                
                                # 2. Cap Regex Telemetry at 5,000 files to save RAM
                                if not self.splicing_telemetry["regex_limit_reached"]:
                                    regex_stats = res["data"].pop("regex_telemetry", {})
                                    
                                    for regex_name, duration in regex_stats.items():
                                        self.splicing_telemetry["regex_totals"][regex_name] += duration
                                        
                                    self.splicing_telemetry["files_sampled"] += 1
                                    if self.splicing_telemetry["files_sampled"] >= 5000:
                                        self.splicing_telemetry["regex_limit_reached"] = True
                                        logger.warning("SPLICING SPEED: 5,000 file sample reached. Halting regex telemetry (Global file speeds still tracking).")
                                    
                        elif status == "singularity":
                            logger.debug(f"SINGULARITY_BYPASS: '{rel_path}' lacks structural integrity. Relegating to Dark Matter.")
                            self.singularity_candidates.append({
                                "path": rel_path,
                                "reason": res["reason"],
                                "identity_confidence": res.get("identity_confidence", 0.0),
                                "size_bytes": res.get("size_bytes", 0) 
                            })
                            self._record_anomaly(rel_path, res["reason"])

                        elif status in ("filtered", "anomaly"):
                            self._record_anomaly(rel_path, res["reason"])
                            
                    except Exception as e:
                        logger.error(f"WORKER_CRASH on {rel_path}: {e}")
                        self._record_anomaly(rel_path, f"Fatal Worker Crash: {str(e)}")

            except concurrent.futures.TimeoutError:
                logger.error("\n" + "="*75)
                logger.error(" SYSTEM HALT: Worker Thread Starvation")
                logger.error(" All CPU workers have exceeded the 60.0s execution limit.")
                logger.error(" This indicates Catastrophic Backtracking (ReDoS) in the regex engine.")
                logger.error(" The following artifacts paralyzed the thread pool:")
                
                for future in active_futures:
                    stuck_file = active_futures[future]
                    logger.error(f"  -> TIMEOUT: {stuck_file}")
                    
                    self._record_anomaly(stuck_file, "Thread Timeout (Regex ReDoS)")
                    self.singularity_candidates.append({
                        "path": stuck_file,
                        "reason": "Thread Timeout (Regex ReDoS)",
                        "identity_confidence": 0.0,
                        "size_bytes": 0
                    })
                    
                logger.error("="*75 + "\n")
                logger.warning("Aborting synthesis to unfreeze the terminal. Please check the Anti-ReDoS shields.")
                
                executor.shutdown(wait=False, cancel_futures=True)
                raise TimeoutError("Mission aborted due to worker starvation (ReDoS or IPC Deadlock).")
                
    def _calculate_galactic_popularity(self):
        """
        Pass 1.5: Optimized relational token aggregation & Fuzzy Suffix Matching.
        Defused O(N^2) Bomb using O(1) Pre-Sliced Suffix Hash Maps.
        """
        logger.info("PASS_1.5: Resolving import graphs via O(1) Pre-computed Suffix Hash Maps...") 
        
        self.popularity_scores = {rel_path: 0 for rel_path in self.stem_map.values()}
        repo_file_paths = set(self.stem_map.values())
        
        # --- O(1) SUFFIX MAP ---
        suffix_map = {}
        stem_to_paths = {}
        
        # Pre-compute all possible valid suffixes for every file to bypass O(N) searching
        for repo_file in repo_file_paths:
            s = Path(repo_file).stem.lower()
            if s not in stem_to_paths:
                stem_to_paths[s] = []
            stem_to_paths[s].append(repo_file)
            
            norm_repo = repo_file.replace("\\", "/")
            repo_no_ext = norm_repo.rsplit('.', 1)[0] if '.' in Path(norm_repo).name else norm_repo
            
            # 1. Build suffixes for the Exact Extension version (e.g. 'utils.h', 'core/utils.h')
            parts_ext = norm_repo.split('/')
            for i in range(len(parts_ext)):
                suffix = "/".join(parts_ext[i:])
                if suffix not in suffix_map:
                    suffix_map[suffix] = []
                suffix_map[suffix].append(repo_file)
                
            # 2. Build suffixes for the Extension-less version (e.g. 'utils', 'core/utils')
            parts_no_ext = repo_no_ext.split('/')
            for i in range(len(parts_no_ext)):
                suffix = "/".join(parts_no_ext[i:])
                if suffix not in suffix_map:
                    suffix_map[suffix] = []
                # Avoid duplicating the target if it already matched the extension list
                if repo_file not in suffix_map[suffix]:
                    suffix_map[suffix].append(repo_file)
            
        stop_stems = {
            "text", "type", "types", "param", "params", "index", "main", 
            "data", "util", "utils", "config", "common", "core", "base", 
            "app", "model", "models", "schema", "style", "styles", "global",
            "env", "helper", "helpers", "constants", "init", "setup", "view",
            "testing", "compat", "api", "tools", "format",
            "os", "sys", "math", "time", "datetime", "json", "csv", "pickle", 
            "copy", "warnings", "collections", "itertools", "functools", 
            "numpy", "pytest", "cython", "typing", "io"
        }
        
        # --- THE REGEX OPTIMIZATION ---
        # Pre-compile the regex ONCE to save CPU cycles inside the massive inner loop
        import_cleaner = re.compile(r'^(?:#\s*include|%\s*include|import|export import|from|require|use|source)\s*', re.IGNORECASE)

        for rel_path, meta in self.cryolink.items():
            raw_imports = meta.get("raw_imports", set())
            for raw_import in raw_imports:
                
                # Apply the pre-compiled regex
                clean_path = import_cleaner.sub('', raw_import.strip())
                                
                if 'from' in clean_path:
                    clean_path = clean_path.split('from')[-1]
                    
                clean_path = clean_path.strip('<>"\'; ()').replace("\\", "/")
                if not clean_path:
                    continue
                
                # THE FIX: Don't turn file extensions into folders!
                # If the string has a dot but no slash, we only replace '.' with '/' 
                # if it is NOT a recognized file extension.
                if "." in clean_path and "/" not in clean_path:
                    ext_guess = "." + clean_path.rsplit('.', 1)[-1].lower()
                    if ext_guess not in self.ext_tally:
                        clean_path = clean_path.replace(".", "/")
                
                # Strip leading relative markers so it aligns with our suffix map
                clean_path = clean_path.lstrip("./")
                if not clean_path:
                    continue
                
                # --- FAST PATH 1: O(1) Suffix & Exact Match ---
                # This single lookup replaces the entire O(N) for-loop!
                if clean_path in suffix_map:
                    for target_path in suffix_map[clean_path]:
                        self.popularity_scores[target_path] += 1
                    continue
                    
                # --- FAST PATH 2: O(1) Python Package Resolution (__init__.py) ---
                init_path = clean_path + "/__init__"
                if init_path in suffix_map:
                    for target_path in suffix_map[init_path]:
                        self.popularity_scores[target_path] += 1
                    continue

                # --- THE FALLBACK: Stem Matching ---
                guess_stem = Path(clean_path).stem.lower()
                if guess_stem in stem_to_paths and guess_stem not in stop_stems and len(guess_stem) >= 3:
                    for target_path in stem_to_paths[guess_stem]:
                        if clean_path in target_path or guess_stem == clean_path:
                            self.popularity_scores[target_path] += 1 
                        elif "/" not in clean_path:
                            self.popularity_scores[target_path] += 1

            # Evict memory before Pass 2
            if "popularity_hits" in meta: del meta["popularity_hits"]
            
    def _second_pass_relational(self):
        """Pass 2: Universal Exposure Framework & Signal Processing."""
        logger.info("PASS_2: Calculating structural physics and Tiered Normalization.")
        
        # ==============================================================
        # NEW: CALCULATE FOLDER CONTEXTS (For Domain Ontologies)
        # Tally the languages in every folder to find the dominant ecosystem
        # ==============================================================
        folder_tallies = {}
        for rel_path, meta in self.cryolink.items():
            folder = str(Path(rel_path).parent)
            lang = meta.get("lang_id", "unknown")
            
            if folder not in folder_tallies:
                folder_tallies[folder] = {}
            folder_tallies[folder][lang] = folder_tallies[folder].get(lang, 0) + 1
            
        folder_dominant_langs = {}
        for folder, tallies in folder_tallies.items():
            if tallies:
                # The language with the most files wins the neighborhood
                folder_dominant_langs[folder] = max(tallies, key=tallies.get)
                
        # --- NEW: CALCULATE THE GLOBAL TEST UMBRELLA ---
        total_loc = 0
        test_loc = 0
        for rel_path, meta in self.cryolink.items():
            loc = meta.get("coding_loc", 0)
            total_loc += loc
            # Identify if the file lives in a test folder or is a test file
            if re.search(r'/tests?/|/testing/|\.test$', rel_path.lower()) or "test" in Path(rel_path).stem.lower():
                test_loc += loc
                
        # Calculate percentage of repo dedicated to testing
        umbrella_coverage = (test_loc / max(total_loc, 1)) * 100.0
        
        # Scale the bonus. Max out at 50.0 to clear the Sigmoid threshold for the whole project
        umbrella_bonus = min(umbrella_coverage * 2.0, 50.0) 
        logger.info(f"UMBRELLA SHIELD: Repo test coverage is {umbrella_coverage:.1f}%. Applying +{umbrella_bonus:.1f} density bonus.")
        # -----------------------------------------------

        for rel_path, meta in self.cryolink.items():
            
            # ---> NEW: INJECT THE FOLDER CONTEXT FOR THE SIGNAL PROCESSOR <---
            folder = str(Path(rel_path).parent)
            if "metadata" not in meta:
                meta["metadata"] = {}
                
            # Grab the winning language for this folder (defaulting to the file's own language)
            meta["metadata"]["folder_dominant_lang"] = folder_dominant_langs.get(folder, meta.get("lang_id", "unknown"))
            # -----------------------------------------------------------------
            
            meta["temporal_telemetry"] = self.chronometer.get_temporal_signals(rel_path)
            meta["authors"] = meta["temporal_telemetry"].get("authors", {})
            stem = Path(rel_path).stem.lower()
            
            # The Enterprise Bridge: Expanding sibling detection to catch Java/C# standards.
            # Because 'self.census' is global, this naturally bridges 'src/main' and 'src/test'
            # without writing brittle directory-parsing logic.
            sibling_candidates = [
                # Node / Python / Ruby / Go conventions
                f"{stem}_test", f"test_{stem}", f"{stem}.test",
                f"{stem}_spec", f"spec_{stem}", f"{stem}.spec",
                # Java / C# / Enterprise conventions (CamelCase becomes flat strings)
                f"{stem}test", f"test{stem}", f"{stem}tests", f"{stem}testcase", f"{stem}spec"
            ]
            meta["is_protected"] = any(cand in self.census for cand in sibling_candidates)
                    
            # --- THE DOCUMENTATION BYPASS ---
            if meta.get("lang_id") in self.config.get("DOCUMENTATION_LANGUAGES", set()):
                # Inject a perfectly neutral payload for human prose
                # Risk Vector matches the 13 standard indices expected by the SignalProcessor
                forensic_result = {
                    "risk_vector": [0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0, 100.0, 0.0, 100.0, 0.0], 
                    "hit_vector": {},
                    "file_impact": 0.0,
                    "telemetry": {
                        "structural_mass": 0.0,
                        "logic_density": 0.0,
                        "average_fxn_mass": 0.0
                    }
                }
            else:
                # Inject the umbrella_bonus into the risk calculator for actual code
                forensic_result = self.processor.calculate_risk_vector(
                    meta, 
                    meta.get("equations", {}),
                    umbrella_bonus=umbrella_bonus
                )

            # =========================================================
            # THE GRAVITY SHIELD: APPLY STRUCTURAL MASS DAMPENERS
            # SignalProcessor handles % Risks, but Orchestrator handles raw Mass.
            # =========================================================
            mass_modifiers = self.config.get("PATH_MODIFIERS", {}).get("Structural Mass", [])
            mass_multiplier = 1.0
            
            # Normalize path for safe cross-platform regex matching
            search_path = rel_path.replace("\\", "/")
            for mod_regex, mod_val in mass_modifiers:
                if mod_regex.search(search_path):
                    mass_multiplier = mod_val
                    break # First match wins
            
            # Apply the dampener to the physical mass
            forensic_result["file_impact"] = round(forensic_result.get("file_impact", 0.0) * mass_multiplier, 2)
            # =========================================================
            
            # =========================================================
            # REPLACE YOUR EXISTING TELEMETRY BLOCK WITH THIS
            # =========================================================
            telemetry_payload = forensic_result.get("telemetry", {})
            ghost_meta = meta.get("metadata", {})
            
            # Legacy Telemetry
            telemetry_payload["control_flow_ratio"] = meta.get("control_flow_ratio", 0.0) 
            telemetry_payload["popularity"] = self.popularity_scores.get(rel_path, 0)
            
            # THE FIX: Replace the brittle regex ownership with the dominant Git author
            if meta.get("authors"):
                # Get the name of the author with the most commits
                dominant_author = max(meta["authors"], key=meta["authors"].get)
                telemetry_payload["ownership"] = dominant_author
            else:
                # Fallback to the comment regex if Git is dormant or unavailable
                telemetry_payload["ownership"] = ghost_meta.get("ownership", "Unknown Architect")
            
            # THE FIX: Conditionally inject historical metadata into the domain_context
            # ONLY if the PROJECT_OVERRIDES regex successfully extracted it.
            if "purpose" in ghost_meta:
                if "domain_context" not in telemetry_payload:
                    telemetry_payload["domain_context"] = {}
                telemetry_payload["domain_context"]["purpose"] = ghost_meta["purpose"]
            
            # Phase 1 Bayesian Optics Traceability (SBOM compliance)
            telemetry_payload["roadmap_locked"] = meta.get("prior_lock", False)
            telemetry_payload["identity_lock_tier"] = meta.get("lock_tier", 4)
            telemetry_payload["identity_confidence"] = meta.get("intensity", 0.0)
            telemetry_payload["identity_source_proof"] = meta.get("source_proof", "Discovery")

            self.stars.append({
                **meta,
                "name": Path(rel_path).name,
                "risk_vector": forensic_result["risk_vector"],
                "hit_vector": forensic_result["hit_vector"],
                "file_impact": forensic_result["file_impact"],
                "telemetry": telemetry_payload 
            })
            
        # ==================================================================
        # THE SECRETS SUPERNOVA INJECTION (Synthetic Visualization)
        # Pull critical leaks out of Dark Matter and force them onto the map
        # ==================================================================
        leaks = [cand for cand in self.singularity_candidates if "CRITICAL LEAK" in cand.get("reason", "")]
        
        # Remove them from Dark Matter so they aren't double-counted in the summary
        self.singularity_candidates = [cand for cand in self.singularity_candidates if "CRITICAL LEAK" not in cand.get("reason", "")]
        
        from .signal_processor import SignalProcessor
        
        for leak in leaks:
            rel_path = leak["path"]
            logger.critical(f"Supernova Injection: Forcing {rel_path} onto the 3D Map!")
            
            synthetic_star = {
                "name": Path(rel_path).name,
                "path": rel_path,
                "lang_id": "plaintext", # <-- Bypasses the Spectral Auditor as Inert Matter
                "coding_loc": 1,
                "total_loc": 1,
                "band": "critical_secret_leak",
                
                # 18-point risk vector. Index 17 is secrets_risk. Peg it to 100%.
                "risk_vector": [0.0] * 13 + [0.0, 0.0, 0.0, 0.0, 100.0], 
                "hit_vector": [0] * len(SignalProcessor.SIGNAL_SCHEMA),
                
                # ---> CARTOGRAPHER GRAVITY <---
                # This makes the radius massive and pushes all other files away
                "file_impact": 5000.0, 
                
                "telemetry": {
                    "ownership": "Secrets Radar",
                    "domain_context": {"warning": "CRITICAL CREDENTIAL LEAK DETECTED"},
                    "identity_source_proof": "Aperture Security Override",
                    "identity_lock_tier": 0
                }
            }
            
            # Manually flag the private_info hit so UI tooltips show the exact trigger
            if "private_info" in SignalProcessor.SIGNAL_SCHEMA:
                idx = SignalProcessor.SIGNAL_SCHEMA.index("private_info")
                synthetic_star["hit_vector"][idx] = 1
                
            self.stars.append(synthetic_star)
    
    def _prepare_target(self, target_input: Union[str, Path]) -> Path:
        """Prepares the filesystem for analysis."""
        input_path = Path(target_input)
        if not input_path.exists():
            raise InaccessibleArtifactError(f"Target missing: {target_input}")

        if input_path.suffix.lower() == '.zip':
            logger.info(f"ARCHIVE_DETECTED: Unpacking {input_path.name} to temporary lead shielding.")
            try:
                self.temp_dir = tempfile.mkdtemp(prefix="refraction_")
                with zipfile.ZipFile(input_path, 'r') as zip_ref:
                    zip_ref.extractall(self.temp_dir)
                return Path(self.temp_dir).resolve()
            except Exception as e:
                self.cleanup()
                raise InaccessibleArtifactError(f"Extraction failure: {e}")

        return input_path.resolve(strict=True)

    def cleanup(self):
        """Purges temporary extraction site."""
        if self.temp_dir and Path(self.temp_dir).exists():
            try:
                shutil.rmtree(self.temp_dir)
            except Exception as e:
                logger.warning(f"CLEANUP_FAILED: Could not remove {self.temp_dir} ({e})")

    def _record_anomaly(self, path: Union[str, Path], message: str):
        """Records failure telemetry."""
        name = Path(path).name
        logger.debug(f"ANOMALY: {name} | {message}")
        self.anomalies.append({"star": name, "diagnostic": message})

    def _summarize_anomalies(self, total_singularity: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Gathers unparsable artifacts and builds the hierarchical extension breakdown."""
        summary = {"size_limit": 0, "binary": 0, "unparsable": 0, "os_permissions": 0}
        unparsable_artifacts: List[str] = []
        
        # 1. Maintain the physical error tallies (I/O, Binary, OS)
        for a in self.anomalies:
            diag = a["diagnostic"].lower()
            
            if "massive" in diag or "size" in diag: 
                summary["size_limit"] += 1
            elif "binary" in diag: 
                summary["binary"] += 1
            elif "saturated" in diag or "syntax" in diag or "unparsable" in diag: 
                summary["unparsable"] += 1
                # Grab the full file path and save it to our array
                unparsable_artifacts.append(a["star"]) 
            elif "permission" in diag or "os " in diag or "read error" in diag: 
                summary["os_permissions"] += 1

        if unparsable_artifacts:
            summary["unparsable_artifacts"] = unparsable_artifacts
            
        # 2. Build the hierarchical composition_by_extension_and_reason
        composition = {}
        for dark in total_singularity:
            path = dark.get("path", "")
            reason = dark.get("reason", "Unknown Reason")
            
            # Extract and normalize the extension using the engine's REGEX SHIELD
            ext = Path(path).suffix.lower()
            if not ext or len(ext) > 12 or not re.match(r'^\.[a-z0-9_\-+]+$', ext):
                ext = "no_extension"
                
            if ext not in composition:
                composition[ext] = {}
            if reason not in composition[ext]:
                composition[ext][reason] = 0
                
            composition[ext][reason] += 1
            
        # Sort extensions by total count, and reasons within them by count
        summary["composition_by_extension_and_reason"] = {
            ext: dict(sorted(reasons.items(), key=lambda x: x[1], reverse=True))
            for ext, reasons in sorted(composition.items(), key=lambda x: sum(x[1].values()), reverse=True)
        }
            
        return summary

    def _render_file_speed_chart(self):
        """Generates a terminal ASCII chart for macro file phases."""
        count = self.file_speed_telemetry["file_count"]
        if count == 0:
            return

        print("\n" + "="*75)
        print(" ⏱️  FILE SPEED (MACRO PHASE) TELEMETRY REPORT")
        print("="*75)
        print(f"\n [ CUMULATIVE TIME SPENT ACROSS {count} FILES ]")
        
        sorted_phases = sorted(self.file_speed_telemetry["phase_totals"].items(), key=lambda x: x[1], reverse=True)
        max_time = sorted_phases[0][1] if sorted_phases else 1
        
        for phase, duration in sorted_phases:
            bar_len = int((duration / max_time) * 30)
            bar = "█" * bar_len
            avg_ms = (duration / max(count, 1)) * 1000
            print(f" {duration:.2f}s | {bar:<30} | {phase} (Avg: {avg_ms:.2f}ms/file)")
            
        print("="*75 + "\n")

    def _render_splicing_chart(self):
        """Generates a terminal ASCII chart for regex and file performance."""
        if not self.splicing_telemetry["top_slowest"]:
            return

        print("\n" + "="*75)
        print(" ⏱️  SPLICING SPEED TELEMETRY REPORT")
        print("="*75)
        
        print("\n [ TOP 10 SLOWEST FILES (Global Search) ]")
        
        # Ensure it's fully sorted before displaying
        sorted_files = sorted(self.splicing_telemetry["top_slowest"], key=lambda x: x["time"], reverse=True)[:10]
        max_file_time = sorted_files[0]["time"] if sorted_files else 1
        
        for f in sorted_files:
            bar_len = int((f["time"] / max_file_time) * 30)
            bar = "█" * bar_len
            print(f" {f['time']:.3f}s | {bar:<30} | {f['path']}")

        sample_size = min(self.splicing_telemetry["files_sampled"], 5000)
        print(f"\n [ CUMULATIVE REGEX EXECUTION TIME (Sampled {sample_size} Files) ]")
        sorted_regex = sorted(self.splicing_telemetry["regex_totals"].items(), key=lambda x: x[1], reverse=True)[:15]
        
        if sorted_regex:
            max_rx_time = sorted_regex[0][1]
            for name, duration in sorted_regex:
                bar_len = int((duration / max_rx_time) * 30)
                bar = "█" * bar_len
                print(f" {duration:.3f}s | {bar:<30} | {name}")
        else:
            print(" No regex telemetry collected.")
            
        print("="*75 + "\n")
    
    def _get_git_audit(self) -> Dict[str, str]:
        """Extracts forensic Git metadata for audit tracking."""
        audit = {
            "branch": "Unknown",
            "commit_hash": "Unknown",
            "remote_url": "Unknown",
            "latest_commit_date": "Unknown"
        }
        try:
            # 1. Commit Hash
            audit["commit_hash"] = subprocess.check_output(
                ['git', 'rev-parse', 'HEAD'], cwd=self.root, text=True, stderr=subprocess.DEVNULL
            ).strip()
            
            # 2. Branch Name
            audit["branch"] = subprocess.check_output(
                ['git', 'rev-parse', '--abbrev-ref', 'HEAD'], cwd=self.root, text=True, stderr=subprocess.DEVNULL
            ).strip()
            
            # 3. Remote URL (The true identity of the repo)
            try:
                audit["remote_url"] = subprocess.check_output(
                    ['git', 'config', '--get', 'remote.origin.url'], cwd=self.root, text=True, stderr=subprocess.DEVNULL
                ).strip()
            except subprocess.CalledProcessError:
                audit["remote_url"] = "Local Only (No Remote)"
                
            # 4. Last Commit Date (When the repo was last updated/pulled)
            audit["latest_commit_date"] = subprocess.check_output(
                ['git', 'log', '-1', '--format=%cd', '--date=iso-strict'], cwd=self.root, text=True, stderr=subprocess.DEVNULL
            ).strip()
            
        except (subprocess.CalledProcessError, FileNotFoundError):
            return {"status": "Not a Git repository (or Git not installed)"}
            
        return audit

# ==============================================================================
# MISSION CONTROL: THE ENTRY POINT
# ==============================================================================

def main():
    import argparse
    import copy
    import os  # <-- Added for the hard memory eviction
    from pathlib import Path
    
    # Required for safe execution limits with the multiprocessing pool on Windows
    multiprocessing.freeze_support()
    
    parser = argparse.ArgumentParser(description="GitGalaxy GalaxyScope v6.2.0")
    parser.add_argument("target", help="Path to repo or ZIP")
    parser.add_argument("--output", default=None, help="Optional output filename override")
    parser.add_argument("--debug", action="store_true", help="Turn on verbose Analytical logging")
    parser.add_argument("--paranoid", action="store_true", help="Lower security thresholds to flag more potential threats.")
    
    # --- NEW: EXCLUSIVE RECORDER FLAGS ---
    parser.add_argument("--llm-only", action="store_true", help="Run ONLY the LLM recorder")
    parser.add_argument("--gpu-only", action="store_true", help="Run ONLY the GPU recorder")
    parser.add_argument("--audit-only", action="store_true", help="Run ONLY the Audit recorder")
    parser.add_argument("--splicing-speed", action="store_true", help="Profile regex and file processing speeds (capped at 5000 files)")
    parser.add_argument("--file-speed", action="store_true", help="Profile the macro lifecycle phases of file processing")
    
    args = parser.parse_args()

    log_level = logging.DEBUG if args.debug else logging.INFO
    
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s [%(levelname)s] [%(name)s] %(message)s',
        stream=sys.stdout,
        force=True
    )
    
    logging.getLogger().setLevel(log_level)
    
    try:
        # ---------------------------------------------------------
        # 1. Target Identification
        # ---------------------------------------------------------
        target_path = Path(args.target)
        project_name = target_path.name
        final_output = args.output if args.output else f"{project_name}_galaxy.json"

        # ---------------------------------------------------------
        # 2. The Domain Dialect Pre-Flight Patch
        # ---------------------------------------------------------
        base_langs = getattr(scanning_config, "LANGUAGE_DEFINITIONS", {})
        project_overrides = getattr(scanning_config, "PROJECT_OVERRIDES", {})
        base_aperture = getattr(scanning_config, "APERTURE_CONFIG", {})
        
        merged_langs = copy.deepcopy(base_langs) 
        merged_aperture = copy.deepcopy(base_aperture)
        
        if project_name in project_overrides:
            logging.info(f"🌌 DIALECT DETECTED: Injecting Project Overrides for '{project_name}'")
            dialect_dict = project_overrides[project_name]
            
            for lang, overrides in dialect_dict.items():
                if lang == "_shield_":
                    if "exclude_dirs" in overrides:
                        if "BLACK_HOLES" not in merged_aperture:
                            merged_aperture["BLACK_HOLES"] = set()
                        merged_aperture["BLACK_HOLES"].update(overrides["exclude_dirs"])
                        logging.debug(f"   -> Patched Aperture Shield (Added {len(overrides['exclude_dirs'])} Black Holes).")
                    
                    if "exclude_paths" in overrides:
                        if "CONTRABAND_PATTERNS" not in merged_aperture:
                            merged_aperture["CONTRABAND_PATTERNS"] = []
                        merged_aperture["CONTRABAND_PATTERNS"].extend(overrides["exclude_paths"])
                        logging.debug(f"   -> Patched Contraband Shield (Added {len(overrides['exclude_paths'])} exact paths).")
                    continue 
                    
                if lang in merged_langs:
                    if "extensions" in overrides:
                        merged_langs[lang]["extensions"] = overrides["extensions"]
                        logging.debug(f"   -> Patched '{lang}' extensions.")
                        
                    rules_patch = {k: v for k, v in overrides.items() if k != "extensions"}
                    if rules_patch and 'rules' in merged_langs[lang]:
                        merged_langs[lang]['rules'].update(rules_patch)
                        logging.debug(f"   -> Patched '{lang}' geometry rules.")

        # --- THE SMART THREAT SWITCH ---
        if args.paranoid:
            active_policy = scanning_config.ThreatPolicy.get_policy("paranoid")
            logging.getLogger("GalaxyScope").info("🔒 ZERO-TRUST MODE: Security Lens thresholds set to maximum sensitivity.")
        else:
            active_policy = scanning_config.ThreatPolicy.get_policy("baseline")

        # Boot the lens with the chosen policy
        security_lens = SecurityLens(policy=active_policy)
        # -------------------------------
        
        # ---------------------------------------------------------
        # 3. Assemble the Final Configuration
        # ---------------------------------------------------------
        full_config = {
            "LANGUAGE_DEFINITIONS": merged_langs,
            "COMMENT_DEFINITIONS": getattr(scanning_config, "COMMENT_DEFINITIONS", {}),
            "APERTURE_CONFIG": merged_aperture,
            "PATH_MODIFIERS": getattr(scanning_config, "PATH_MODIFIERS", {}),
            "PRIORITY_WHITELIST": getattr(scanning_config, "PRIORITY_WHITELIST", []),
            "DOCUMENTATION_LANGUAGES": getattr(scanning_config, "DOCUMENTATION_LANGUAGES", set()),
            "PARANOID_MODE": args.paranoid,
            # --- NEW: PASS EXCLUSIVE FLAGS TO ORCHESTRATOR ---
            "LLM_ONLY": args.llm_only,
            "GPU_ONLY": args.gpu_only,
            "AUDIT_ONLY": args.audit_only,
            "SPLICING_SPEED": args.splicing_speed,
            "FILE_SPEED": args.file_speed
        }
        # ---------------------------------------------------------
        # 4. Ignite the Engine
        # ---------------------------------------------------------
        scope = Orchestrator(args.target, full_config)
        scope.run_mission(final_output)
        
        # --- THE FIX: INSTANT RAM EVICTION ---
        os._exit(0)
        
    except Exception as e:
        logging.error(f"Critical failure during execution: {e}", exc_info=True)
        # --- THE FIX: INSTANT ERROR EXIT ---
        os._exit(1)

# This tells Python to run main() if you call the file directly, 
# but allows PyPI to map to main() dynamically.
if __name__ == "__main__":
    main()