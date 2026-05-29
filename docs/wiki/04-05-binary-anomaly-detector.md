# Binary Anomaly Detector (The X-Ray Inspector)

> **Seeing Through the Disguise**
>
> Advanced adversaries rarely drop plain-text malware into a repository. They use steganography, packing techniques, and high-entropy encryption to hide their payloads inside seemingly harmless files (like `.png` images, `.zip` archives, or compiled binaries). 
>
> The Binary Anomaly Detector (`binary_anomaly_detector.py`), known internally as the X-Ray Inspector, is designed for the fast triage of these concealed threats. It scans the raw bytes and mathematical entropy of files to detect malicious execution headers and obfuscated payloads.

## The Funnel & The Binary Exception

Most GitGalaxy tools (like the Optical Lenses) rely on the `ApertureFilter` to explicitly drop binary files from the scan queue to save memory. The X-Ray Inspector fundamentally reverses this logic.

* **The Binary Exception:** During the initial Pass 1 Funnel, the X-Ray Inspector intentionally *bypasses* the standard path integrity checks. It actively wants to scan the binaries (`.png`, `.zip`) to verify that their internal structures actually match their file extensions.
* **The Test Data Shield:** Because unit tests often generate highly randomized or encrypted mock data, the Inspector automatically whitelists any paths containing `/test/`, `/tests/`, or `phpunit` to prevent false positives.
* **X-Ray Bypasses:** It utilizes dedicated `XRAY_BYPASS_EXTENSIONS` and `XRAY_BYPASS_PATHS` from the global config, allowing architects to explicitly whitelist known, safe dense data formats (like `.gz` or `.json` fixtures).

## The Deep Scan (8KB Heuristics)

To maintain hyper-scale velocity, the Inspector does not read massive binaries into memory. It reads only the first 8KB of every file as raw bytes, looking for structural anomalies:

### 1. Magic Byte Mismatches
The Inspector checks the file's Magic Bytes (the invisible signature at the very beginning of a file) against its claimed extension. If a file claims to be a `.jpg` but has the Magic Bytes of a compiled `.elf` Linux executable, the Inspector immediately flags it as a hidden threat.

### 2. Shannon Entropy Math (Packed Payloads)
The Inspector decodes the raw bytes into UTF-8 and evaluates the mathematical randomness of the strings. If the file contains mathematically dense or encrypted strings resulting in a Shannon Entropy score greater than 4.8, it flags the file as a potential packed payload or encrypted malware.

### 3. Sub-Atomic Decryption Loops
The Inspector hunts for specific Bitwise operations (`bitwise_hits`). High concentrations of custom XOR math are a primary indicator of a sub-atomic decryption routine, often used by malware to unpack itself dynamically in memory.

## Speed Optimization & The Header Shield

* **Neutered Lens:** To maximize speed, the Orchestrator instantiates a `SecurityLens` but heavily neuters it. It strips out all complex regex and AST parsing, restricting the engine to look *only* at `heat_triggers` and `bitwise_hits`.
* **The Expected Header Shield:** Linux and macOS scripts (`.sh`, `.bash`, `.command`) legally contain execution strings like `#!/bin/bash`. If the binary scanner flags a threat but detects this exact pattern in a shell extension, it safely clears the threat to prevent false positives.

## CI/CD Triage Alert

When the scan is complete, the X-Ray Inspector prints a Mission Report detailing the scan velocity and the exact files containing structural anomalies. 

If any encrypted payloads, Magic Byte mismatches, or parasitic execution headers are detected, it issues a `TRIAGE ALERT`, exiting with a status code of `1` to violently block the malicious commit or Pull Request.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
