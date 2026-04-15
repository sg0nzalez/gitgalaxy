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
    parser.add_argument("target", help="Path to the log file")
    parser.add_argument("-k", "--keywords", nargs="+", required=True, help="Keywords to search for")
    parser.add_argument("--out", type=str, help="Optional: Custom directory to save the results log")
    args = parser.parse_args()

    target_path = Path(args.target).resolve()
    if not target_path.exists():
        print(f"Error: Target {target_path} does not exist.")
        sys.exit(1)

    # Determine Output Path
    if args.out:
        out_dir = Path(args.out).resolve()
        out_dir.mkdir(parents=True, exist_ok=True)
        results_path = out_dir / f"{target_path.stem}_audit_hits.log"
    else:
        results_path = target_path.parent / f"{target_path.stem}_audit_hits.log"

    file_size_gb = target_path.stat().st_size / (1024**3)
    print(f"🌊 Tapping into log stream: {target_path.name} ({file_size_gb:.2f} GB)")
    print(f"📁 Streaming evidence to: {results_path.resolve()}")
    
    keyword_patterns = {kw: re.compile(kw.encode('utf-8'), re.IGNORECASE) for kw in args.keywords}
    ts_pattern = re.compile(br'(\d{4}-\d{2}-\d{2}[T\s]\d{2}|\b[A-Z][a-z]{2}\s+\d{1,2}\s\d{2})')

    histograms = {kw: defaultdict(int) for kw in args.keywords}
    
    start_time = time.time()
    
    # 2. The Memory Shield: Read binary in, stream text out immediately
    with open(target_path, 'rb') as f_in, open(results_path, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            for kw, pattern in keyword_patterns.items():
                if pattern.search(line):
                    decoded_line = line.decode('utf-8', errors='ignore').strip()
                    
                    # Extract timestamp for the UI graph
                    ts_match = ts_pattern.search(line)
                    bucket = ts_match.group(1).decode('utf-8', errors='ignore') + ":00" if ts_match else "Unknown Time"
                        
                    histograms[kw][bucket] += 1
                    
                    # Write immediately to disk, bypassing RAM bloat
                    f_out.write(f"{decoded_line}\n")
                    break 

    time_elapsed = time.time() - start_time
    
    # 3. Print the Visual Dashboards
    for kw in args.keywords:
        draw_ascii_histogram(histograms[kw], kw)
        
    # 4. Calculate totals for the Executive Summary
    total_counts = {kw: sum(buckets.values()) for kw, buckets in histograms.items()}
    max_total = max(total_counts.values()) if total_counts.values() else 0

    print("\n" + "="*75)
    print(" 📊 EXECUTIVE SUMMARY (TOTAL VOLUME)")
    print("="*75)
    
    if max_total > 0:
        for kw, count in total_counts.items():
            bar_len = int((count / max_total) * 30) if max_total > 0 else 0
            bar = "█" * max(1, bar_len) if count > 0 else ""
            print(f" {kw.ljust(15)} | {bar} ({count:,} hits)")
    else:
        print(" No keyword hits detected in this scan.")
        
    print("-" * 75)
    processing_speed = file_size_gb / time_elapsed if time_elapsed > 0 else 0
    print(f" ✅ Scan complete. Sliced through {target_path.name} in {time_elapsed:.2f} seconds.")
    print(f" ⚡ Processing Velocity: {processing_speed:.3f} GB/s")
    print(f" 📁 Evidence Log: {results_path.resolve()}")
    print("="*75 + "\n")

if __name__ == "__main__":
    main()