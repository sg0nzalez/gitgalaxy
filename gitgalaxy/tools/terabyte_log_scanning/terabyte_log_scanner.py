#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: Mega Log Parser
# Purpose: High-speed, single-pass log analyzer with ASCII time-series histograms.
# ==============================================================================
import argparse
import sys
import os
import re
import time
import json # <-- ADD THIS
from collections import defaultdict
from pathlib import Path

def draw_ascii_histogram(time_buckets: dict, keyword: str):
    """Draws a dynamically scaled ASCII histogram, showing only top spikes if massive."""
    if not time_buckets:
        return

    print(f"\n === TIME-SERIES: {keyword.upper()} ===")
    
    max_hits = max(time_buckets.values())
    max_bar_width = 40
    avg_hits = sum(time_buckets.values()) / len(time_buckets)
    anomaly_threshold = avg_hits * 3  
    
    # THE UX FIX: If there are too many buckets, only show the Top 15 worst ones
    if len(time_buckets) > 15:
        print(" (Filtering to Top 15 Highest Volume Spikes)")
        # Sort by highest hits, grab top 15, then resort chronologically for the graph
        top_offenders = sorted(time_buckets.items(), key=lambda x: x[1], reverse=True)[:15]
        display_buckets = dict(sorted(top_offenders))
    else:
        display_buckets = dict(sorted(time_buckets.items()))

    for time_bucket, hits in display_buckets.items():
        bar_len = int((hits / max_hits) * max_bar_width) if max_hits > 0 else 0
        bar = "█" * max(1, bar_len)
        
        alert = "  <-- ANOMALY SPIKE" if hits >= anomaly_threshold and hits > 10 else ""
        print(f" [{time_bucket}] {bar} ({hits:,} hits){alert}")

def main():
    parser = argparse.ArgumentParser(description="GitGalaxy Mega Log Parser")
    parser.add_argument("target", help="Path to the log file (Translated ASCII SMF)")
    # Make keywords optional, and add an input file argument
    parser.add_argument("-k", "--keywords", nargs="+", help="Keywords to search for")
    parser.add_argument("--input_state", type=str, help="Path to GitGalaxy ir_state.json to auto-extract targets")
    parser.add_argument("--out", type=str, help="Optional: Custom directory to save the results log")
    args = parser.parse_args()

    target_path = Path(args.target).resolve()
    if not target_path.exists():
        print(f"Error: Target {target_path} does not exist.")
        sys.exit(1)

    # =====================================================================
    # ADAPTATION 1: The Input Handshake
    # =====================================================================
    search_targets = []
    dynamic_call_hunts = {}

    if args.input_state:
        state_path = Path(args.input_state)
        if state_path.exists():
            with open(state_path, 'r') as f:
                ir_state = json.load(f)
                # Extract all known programs to check for the 0-Hit dead code rule
                search_targets = ir_state.get('analysis', {}).get('known_programs', [])
                print(f"📡 Loaded {len(search_targets)} targets from {state_path.name}")
    elif args.keywords:
        search_targets = args.keywords
    else:
        print("Error: Must provide either -k keywords or --input_state json.")
        sys.exit(1)

    # =====================================================================
    # ADAPTATION 2: Mainframe Execution Regex
    # We prefix targets with common SMF/JCL execution markers to avoid noise
    # =====================================================================
    keyword_patterns = {}
    for kw in search_targets:
        # Example: looking for "PGM=NAME" or "STARTED NAME"
        pattern_str = fr"(?:PGM=|STARTED\s+){kw}"
        keyword_patterns[kw] = re.compile(pattern_str.encode('utf-8'), re.IGNORECASE)

    ts_pattern = re.compile(br'(\d{4}-\d{2}-\d{2}[T\s]\d{2}|\b[A-Z][a-z]{2}\s+\d{1,2}\s\d{2})')
    histograms = {kw: defaultdict(int) for kw in search_targets}

    # ... [Keep your existing file path setup and start_time logic here] ...
    
    # 2. The Memory Shield
    with open(target_path, 'rb') as f_in, open(results_path, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            for kw, pattern in keyword_patterns.items():
                if pattern.search(line):
                    decoded_line = line.decode('utf-8', errors='ignore').strip()
                    ts_match = ts_pattern.search(line)
                    bucket = ts_match.group(1).decode('utf-8', errors='ignore') + ":00" if ts_match else "Unknown Time"
                    histograms[kw][bucket] += 1
                    f_out.write(f"{decoded_line}\n")
                    break 

    time_elapsed = time.time() - start_time
    
    # ... [Keep your existing ASCII Histogram and Executive Summary printing here] ...

    total_counts = {kw: sum(buckets.values()) for kw, buckets in histograms.items()}

    # =====================================================================
    # ADAPTATION 3: The Output Handshake (JSON Sidecar)
    # =====================================================================
    sidecar_path = target_path.parent / "dynamic_telemetry.json"
    
    telemetry_payload = {
        "execution_counts": total_counts,
        "resolved_dynamic_calls": {} # Placeholder for advanced chronological resolution
    }

    with open(sidecar_path, 'w') as f_json:
        json.dump(telemetry_payload, f_json, indent=4)
        
    print(f" 💾 JSON State Sidecar written to: {sidecar_path.resolve()}")
    print("="*75 + "\n")

if __name__ == "__main__":
    main()