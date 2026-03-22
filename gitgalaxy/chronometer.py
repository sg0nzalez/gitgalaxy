# ==============================================================================
# GitGalaxy
# Copyright (c) 2026 Joe Esquibel
#
# This source code is licensed under the PolyForm Noncommercial License 1.0.0.
# You may not use this file except in compliance with the License.
# A copy of the license can be found in the LICENSE file in the root directory
# of this project, or at https://polyformproject.org/licenses/noncommercial/1.0.0/
# ==============================================================================
import os
import subprocess
import logging
import time
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple
from . import gitgalaxy_standards_v011 as config

# ==============================================================================
# GitGalaxy Phase 3: Chronometer (Temporal Sensor)
# Strategy v6.3.0 Melded Protocol: Bulk Survey, Dynamic Windowing & Thread-Safety
# ==============================================================================

class Chronometer:
    """
    The GitGalaxy Chronometer.
    
    PURPOSE: Acts as a high-fidelity Temporal Sensor. It measures Git churn 
    and physical file-system stability, providing raw telemetry to the 
    Signal Processor for exposure calculations.
    
    ARCHITECTURE (v6.3.0 Melded):
    1. Survey-First Logic: Performs a bulk metadata sweep during initialization 
       to ensure Pass 2 threading is a zero-I/O memory lookup.
    2. Dynamic Windowing: Calculates a rolling window based on 10% of the project's
       total lifespan; falls back to volume-based if the sector is dormant.
    3. Boundary Lock: Restores absolute project Min/Max time detection via 
       Git rev-list and log-head analysis.
    4. Resource Guard: Uses buffered Popen streaming with explicit pipe 
       finalization to prevent zombie processes and FD leaks.
    """

    def __init__(self, root_path: Path, parent_logger: Optional[logging.Logger] = None):
        """Initializes the Temporal Sensor and ignites the Bulk Survey Pass."""
        if parent_logger:
            self.logger = parent_logger.getChild("chronometer")
            self.logger.setLevel(parent_logger.level)
        else:
            self.logger = logging.getLogger("chronometer")
            self.logger.setLevel(logging.INFO)

        self.root = Path(root_path).resolve()
        self.is_resilient = False
        
        # Pull configurations safely
        self.chrono_config = getattr(config, "CHRONOMETER_CONFIG", {})
        self.aperture_config = getattr(config, "APERTURE_CONFIG", {})
        
        # --- INTERNAL STATE (The Sensor Cache) ---
        self.entropy_map: Dict[str, int] = {}
        self.mtime_map: Dict[str, float] = {}
        self.author_map: Dict[str, Dict[str, int]] = {} 
        
        # Signal 1: Global Temporal Boundaries
        self.repo_min_time = time.time()
        self.repo_max_time = time.time()
        
        self.logger.debug(f"Initializing Melded Temporal Sensor for: '{self.root.name}'...")

        # 1. Hardware Verification & Boundary Survey
        self._calibrate_temporal_field()

    def _calibrate_temporal_field(self):
        """Dispatches the survey engines to establish boundaries and churn cache."""
        t_start = time.time()
        
        # Step A: Check for Git Hardware
        if (self.root / ".git").exists():
            try:
                subprocess.run(['git', '--version'], capture_output=True, check=True)
                self.is_resilient = True
                self.logger.debug("Git hardware verified. Commencing Deep Boundary Survey.")
            except (subprocess.CalledProcessError, FileNotFoundError):
                self.logger.warning("Git binary not found. Falling back to OS Walk.")

        # Step B: Establish Absolute Project Boundaries (Min/Max Time)
        self._survey_boundaries()

        # Step C: Populate Churn and MTime Maps
        if self.is_resilient:
            self._ignite_hybrid_log_scan()
        else:
            self._survey_filesystem_mtimes()

        duration = time.time() - t_start
        self.logger.info(
            f"Chronometer Calibration Complete ({duration:.2f}s) | "
            f"Visible Timeline: {self.repo_max_time - self.repo_min_time:.0f}s | "
            f"Cached Artifacts: {len(self.mtime_map)}"
        )

    def _survey_boundaries(self):
        """
        [SIGNAL 1: ABSOLUTE BOUNDARIES]
        Determines the project's start and end dates for temporal normalization.
        """
        if self.is_resilient:
            try:
                # Get Most Recent Commit (Max Time)
                res_max = subprocess.run(['git', 'log', '-1', '--format=%ct'], cwd=self.root, capture_output=True, text=True, check=True)
                if res_max.stdout.strip():
                    self.repo_max_time = float(res_max.stdout.strip())
                
                # Get First Commit (Min Time)
                res_min = subprocess.run(['git', 'rev-list', '--max-parents=0', 'HEAD'], cwd=self.root, capture_output=True, text=True, check=True)
                first_commits = res_min.stdout.strip().split('\n')
                if first_commits and first_commits[0]:
                    res_min_time = subprocess.run(['git', 'log', '-1', '--format=%ct', first_commits[0]], cwd=self.root, capture_output=True, text=True, check=True)
                    if res_min_time.stdout.strip():
                        self.repo_min_time = float(res_min_time.stdout.strip())
                
                self.logger.debug(f"Boundaries Locked (Git): {self.repo_min_time} to {self.repo_max_time}")
                return
            except Exception as e:
                self.logger.warning(f"Git boundary survey failed, falling back to FS scan: {e}")

        # Fallback: OS Walk for boundaries utilizing global Aperture configs
        black_holes = self.aperture_config.get("BLACK_HOLES", set())
        scan_limit = self.chrono_config.get("FALLBACK_SCAN_LIMIT", 25000)
        
        min_t, max_t = float('inf'), 0.0
        count = 0
        for root, dirs, files in os.walk(self.root):
            # Skip noise sectors dynamically
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in black_holes]
            for f in files:
                try:
                    m = os.path.getmtime(os.path.join(root, f))
                    if m < min_t: min_t = m
                    if m > max_t: max_t = m
                    count += 1
                except OSError: pass
                if count > scan_limit: break 
            if count > scan_limit: break
            
        if count > 0:
            self.repo_min_time, self.repo_max_time = min_t, max_t

    def _load_ignored_revs(self) -> set:
        """Loads non-functional cosmetic commits to filter out of the churn math."""
        ignored = set()
        ignore_file = self.root / ".git-blame-ignore-revs"
        
        if ignore_file.exists():
            try:
                with open(ignore_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        # Skip comments and empty lines
                        if line and not line.startswith('#'):
                            ignored.add(line)
            except Exception as e:
                self.logger.warning(f"Could not load .git-blame-ignore-revs: {e}")
                
        return ignored

    def _ignite_hybrid_log_scan(self):
        """
        [MUSEUM DEMO PROTOCOL]
        Streams history backwards for exactly 1 year to guarantee deep churn data,
        bypassing the coverage early-exit trap while respecting the strict time budget.
        """
        start_time = time.time()
        
        # 1. Establish the Denominator (Total Tracked Files)
        try:
            res = subprocess.run(['git', 'ls-files'], cwd=self.root, capture_output=True, text=True, check=True)
            tracked_files = set(res.stdout.splitlines())
            total_files = len(tracked_files)
        except Exception:
            tracked_files = set()
            total_files = 1000 # Fallback safety
            
        # 2. Configure the Kiosk Thresholds
        # Set an impossible required_files target to disable the coverage early-exit (Kill Switch 2).
        # This forces the engine to chew through the full 1-year history or hit the time limit.
        required_files = 9999999 
        
        # The Kiosk Safety Net: Ensure this pulls from your config (e.g., 15.0 or 60.0)
        timeout_limit = self.chrono_config.get("STREAM_TIMEOUT_SECONDS", 15.0)
        
        self.logger.info(
            f"Chronometer: Engaging 1-Year Historical Sweep (Kiosk Mode). "
            f"Budget: {timeout_limit}s"
        )
        
        ignored_hashes = self._load_ignored_revs()
        
        # 3. The Command: Limit Git to the last year of commits.
        # This generates massive churn spikes without getting bogged down in decade-old bedrock.
        cmd = [
            'git', 'log', 
            '--since=1.year', 
            '--name-only', '--pretty=format:%H|%at|%an', '--no-merges'
        ]
        
        # Execute the stream
        processed_events, _ = self._run_git_stream_escalator(
            cmd, ignored_hashes, tracked_files, required_files, timeout_limit, start_time
        )
        
        duration = time.time() - start_time
        
        # Filter our entropy map to only count currently tracked files for the final pct
        coverage_achieved = len([k for k in self.entropy_map.keys() if k in tracked_files])
        pct = (coverage_achieved / max(total_files, 1) * 100)
        
        self.logger.info(
            f"Temporal Sync Complete | Sweep finished in {duration:.2f}s. "
            f"Achieved {pct:.1f}% active coverage ({coverage_achieved}/{total_files} files via {processed_events} events)."
        )
        
    def _run_git_stream_escalator(self, cmd: List[str], ignored_hashes: set, tracked_files: set, required_files: int, timeout_limit: float, start_time: float) -> Tuple[int, bool]:
        """Executes Git log via Popen stream, halting dynamically based on coverage or time."""
        processed_lines = 0
        process = None
        current_ts = self.repo_max_time
        current_author = "Unknown"
        skip_current_commit = False
        reached_target = False
        
        # Local tracker to ensure we only count files that currently exist
        valid_files_seen = set()

        try:
            process = subprocess.Popen(
                cmd, cwd=self.root, 
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                text=True, bufsize=1
            )

            for line in process.stdout:
                # [THE KILL SWITCH 1] Enforce the hard compute timeout
                if time.time() - start_time > timeout_limit:
                    break
                    
                # [THE KILL SWITCH 2] Enforce the dynamic file coverage target
                if len(valid_files_seen) >= required_files:
                    reached_target = True
                    break
                    
                clean_line = line.strip()
                if not clean_line: continue
                
                # Check if this is the commit header (Hash|Timestamp|Author)
                if '|' in clean_line:
                    parts = clean_line.split('|', 2)
                    if len(parts) >= 2 and parts[1].isdigit(): 
                        commit_hash = parts[0]
                        
                        if commit_hash in ignored_hashes:
                            skip_current_commit = True
                            continue
                            
                        skip_current_commit = False
                        current_ts = float(parts[1])
                        current_author = parts[2].strip() if len(parts) > 2 else "Unknown"
                        continue
                
                if skip_current_commit:
                    continue
                
                if clean_line.startswith('"') and clean_line.endswith('"'):
                    clean_line = clean_line[1:-1]
                
                path_key = Path(clean_line).as_posix()
                
                # Only count towards our goal if it's an active file (avoids being tricked by renamed/deleted files)
                if path_key in tracked_files:
                    valid_files_seen.add(path_key)
                
                # Track Churn
                self.entropy_map[path_key] = self.entropy_map.get(path_key, 0) + 1
                
                # Track Ownership Entropy
                if path_key not in self.author_map:
                    self.author_map[path_key] = {}
                self.author_map[path_key][current_author] = self.author_map[path_key].get(current_author, 0) + 1
                
                # Track Stability (MTime)
                if current_ts > self.mtime_map.get(path_key, 0.0):
                    self.mtime_map[path_key] = current_ts
                
                processed_lines += 1

        except Exception as e:
            self.logger.error(f"Git log streaming failure: {e}")
        finally:
            # THE CRITICAL CLEANUP: Because we are breaking the stream early, we MUST 
            # violently kill the Popen process, otherwise it creates zombie processes 
            # and broken pipes in the OS.
            if process:
                process.kill() 
                process.communicate()
                if process.stdout: process.stdout.close()
                if process.stderr: process.stderr.close()
                
        return processed_lines, reached_target
    
    def _survey_filesystem_mtimes(self):
        """OS-level fallback to populate mtime_map in non-Git environments."""
        for root, _, files in os.walk(self.root):
            for name in files:
                try:
                    full_path = Path(root) / name
                    rel_path = full_path.relative_to(self.root).as_posix()
                    self.mtime_map[rel_path] = os.path.getmtime(full_path)
                except (OSError, ValueError): continue

    def get_temporal_signals(self, rel_path: str) -> Dict[str, Any]:
            """
            [THE HANDOVER]
            Returns raw temporal telemetry. Optimized for Thread-Safe O(1) lookups.
            """
            lookup_key = Path(rel_path).as_posix()
            
            # Stability (MTime) lookup
            mtime = self.mtime_map.get(lookup_key)
            if mtime is None:
                try:
                    mtime = os.path.getmtime(self.root / rel_path)
                except OSError:
                    mtime = self.repo_max_time

            # Churn lookup
            commit_count = self.entropy_map.get(lookup_key, 0)
            
            return {
                "commit_count": commit_count,
                "mtime": mtime,
                "repo_min_time": self.repo_min_time,
                "repo_max_time": self.repo_max_time,
                "is_git_tracked": self.is_resilient,
                "authors": self.author_map.get(lookup_key, {}) 
            }