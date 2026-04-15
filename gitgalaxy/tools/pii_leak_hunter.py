#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: PII Data Leak Hunter
# Purpose: High-speed, single-pass log analyzer that hunts and masks 
#          exposed Credit Cards, SSNs, and AWS API Keys.
# ==============================================================================
import argparse
import sys
import re
import time
from collections import defaultdict
from pathlib import Path

# ==============================================================================
# 1. THE REGEX PHYSICS (MATHEMATICAL TRAPS)
# ==============================================================================
# We compile these as binary (bytes) to maintain the insane speed of the original log parser
PII_PATTERNS = {
    "VISA": re.compile(br'\b4[0-9]{12}(?:[0-9]{3})?\b'),
    "MASTERCARD": re.compile(br'\b(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}\b'),
    "SSN": re.compile(br'\b\d{3}-\d{2}-\d{4}\b'),
    "AWS_KEY": re.compile(br'\b(?:AKIA|ASIA|AGPA|AIDA|AROA|AIPA)[A-Z0-9]{16}\b')
}

def mask_pii(text: str) -> str:
    """Masks out the middle of sensitive data so the evidence log is safe."""
    # Mask Visa & Mastercard (Leave last 4)
    text = re.sub(r'\b(4[0-9]{12}(?:[0-9]{3})?)\b', lambda m: f"VISA-MASKED-{m.group(1)[-4:]}", text)
    text = re.sub(r'\b((?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12})\b', lambda m: f"MC-MASKED-{m.group(1)[-4:]}", text)
    
    # Mask SSN (Leave last 4)
    text = re.sub(r'\b\d{3}-\d{2}-(\d{4})\b', r'XXX-XX-\1', text)
    
    # Mask AWS Keys (Leave first 4 and last 4)
    text = re.sub(r'\b((?:AKIA|ASIA|AGPA|AIDA|AROA|AIPA))[A-Z0-9]{12}([A-Z0-9]{4})\b', r'\1-XXXX-\2', text)
    
    return text

def draw_ascii_histogram(time_buckets: dict, keyword: str):
    """Draws a dynamically scaled ASCII histogram, showing only top spikes if massive."""
    if not time_buckets:
        return

    print(f"\n === TIME-SERIES: {keyword.upper()} EXPOSURE ===")
    
    max_hits = max(time_buckets.values())
    max_bar_width = 40
    avg_hits = sum(time_buckets.values()) / len(time_buckets)
    anomaly_threshold = avg_hits * 3  
    
    if len(time_buckets) > 15:
        print(" (Filtering to Top 15 Highest Volume Spikes)")
        top_offenders = sorted(time_buckets.items(), key=lambda x: x[1], reverse=True)[:15]
        display_buckets = dict(sorted(top_offenders))
    else:
        display_buckets = dict(sorted(time_buckets.items()))

    for time_bucket, hits in display_buckets.items():
        bar_len = int((hits / max_hits) * max_bar_width) if max_hits > 0 else 0
        bar = "█" * max(1, bar_len)
        
        alert = "  <-- MASSIVE EXFILTRATION SPIKE" if hits >= anomaly_threshold and hits > 10 else ""
        print(f" [{time_bucket}] {bar} ({hits:,} hits){alert}")

def main():
    parser = argparse.ArgumentParser(description="GitGalaxy PII Data Leak Hunter")
    parser.add_argument("target", help="Path to the log file or database dump to scan")
    parser.add_argument("--out", type=str, help="Optional: Custom directory to save the safe evidence log")
    args = parser.parse_args()

    target_path = Path(args.target).resolve()
    if not target_path.exists():
        print(f"Error: Target {target_path} does not exist.")
        sys.exit(1)

    if args.out:
        out_dir = Path(args.out).resolve()
        out_dir.mkdir(parents=True, exist_ok=True)
        results_path = out_dir / f"{target_path.stem}_pii_leak_evidence.log"
    else:
        results_path = target_path.parent / f"{target_path.stem}_pii_leak_evidence.log"

    file_size_gb = target_path.stat().st_size / (1024**3)
    print(f"🚨 Tapping into data stream: {target_path.name} ({file_size_gb:.2f} GB)")
    print(f"🛡️  Masking enabled. Streaming safe evidence to: {results_path.name}")
    
    ts_pattern = re.compile(br'(\d{4}-\d{2}-\d{2}[T\s]\d{2}|\b[A-Z][a-z]{2}\s+\d{1,2}\s\d{2})')
    histograms = {kw: defaultdict(int) for kw in PII_PATTERNS.keys()}
    
    start_time = time.time()
    
    # 2. The Memory Shield: Read binary in, check regex, stream masked text out
    with open(target_path, 'rb') as f_in, open(results_path, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            hit_found = False
            for pii_type, pattern in PII_PATTERNS.items():
                if pattern.search(line):
                    # Only decode the line if a physical hit is detected to save CPU cycles
                    if not hit_found:
                        decoded_line = line.decode('utf-8', errors='ignore').strip()
                        safe_line = mask_pii(decoded_line)
                        f_out.write(f"[{pii_type}] {safe_line}\n")
                        hit_found = True # Prevent duplicate writes if a line has multiple PII types
                    
                    ts_match = ts_pattern.search(line)
                    bucket = ts_match.group(1).decode('utf-8', errors='ignore') + ":00" if ts_match else "Unknown Time"
                    histograms[pii_type][bucket] += 1

    time_elapsed = time.time() - start_time
    
    # 3. Print the Visual Dashboards
    for kw in PII_PATTERNS.keys():
        draw_ascii_histogram(histograms[kw], kw)
        
    # 4. Calculate totals for the Executive Summary
    total_counts = {kw: sum(buckets.values()) for kw, buckets in histograms.items()}
    max_total = max(total_counts.values()) if total_counts.values() else 0

    print("\n" + "="*75)
    print(" 🚨 PRIVACY INCIDENT SUMMARY (TOTAL EXPOSURE)")
    print("="*75)
    
    if max_total > 0:
        for kw, count in total_counts.items():
            bar_len = int((count / max_total) * 30) if max_total > 0 else 0
            bar = "█" * max(1, bar_len) if count > 0 else ""
            print(f" {kw.ljust(15)} | {bar} ({count:,} hits)")
    else:
        print(" ✅ Clean scan. No Social Security, Credit Card, or AWS Keys detected.")
        
    print("-" * 75)
    processing_speed = file_size_gb / time_elapsed if time_elapsed > 0 else 0
    print(f" ✅ Scan complete. Sliced through {target_path.name} in {time_elapsed:.2f} seconds.")
    print(f" ⚡ Processing Velocity: {processing_speed:.3f} GB/s")
    print(f" 📁 Safe Evidence Log: {results_path.resolve()}")
    print("="*75 + "\n")

if __name__ == "__main__":
    main()