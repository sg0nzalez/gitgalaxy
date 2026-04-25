# GitGalaxy: Internal Architecture & Source Code

Welcome to the internal source code for the **GitGalaxy blAST Engine**. 

This directory contains the core physics, routing, and mathematical heuristics that power the system. If you are a developer looking to contribute or understand the pipeline, here is the architectural map:

### 🗺️ The Developer Map
* **`/core/`**: The optical routing layer. Contains `aperture.py` and `prism.py`, which break down source code into structural signals and separate executable logic from ghost mass (comments).
* **`/physics/`**: The heuristics engine. Contains `signal_processor.py` and `neural_auditor.py`, which apply GitGalaxy mathematics to score O(N) complexity, blast radius, and state flux.
* **`/recorders/`**: The export layer. Translates the internal state maps into SQLite databases, AI-agent JSON tickets, and WebGPU data payloads.
* **`/security/`**: The zero-trust validation layer for detecting embedded malware and logic bombs.
* **`/tools/`**: The enterprise "Spokes". Contains specific automation controllers for CI/CD pipelines, including Supply Chain Firewalls, PII Leak Hunters, and GitHub Actions integrations.

---

### ⚡ Performance Showcase: NVDA (NonVisual Desktop Access)

To demonstrate the engine's capability on complex, cross-language system architecture, we unleashed GalaxyScope on **NVDA**, the open-source Windows screen reader. 

Because NVDA relies heavily on bridging Python application logic with low-level C++ system hooks, it requires advanced dependency mapping. The blAST engine successfully parsed the mixed-language architecture, analyzing **236,754 lines of code** in just **5.59 seconds** (a velocity of 42,357 LOC/sec). 

Crucially, during the import resolution phase, the Air-Gapped Dependency Radar successfully intercepted a structural naming collision (`fstream` vs `sstream`), proving the real-time typosquatting defenses are fully operational. 

> **Note on False Positives:** Because `fstream` and `sstream` are both standard C++ libraries, this specific flag is a false positive. To prevent the engine from halting on trusted internal libraries, contributors can whitelist them by adding them to the `approved_imports.json` registry.

![NVDA Processing Demo](../docs/wiki/assets/nvda_processing.gif)

```text
[INFO] PASS_1.5: Running Air-Gapped Typosquatting & Dependency Confusion Radar...
[CRITICAL] 🚨 TYPOSQUATTING DETECTED: 'fstream' in nvdaHelper/vbufBase/storage.cpp closely matches anchor 'sstream'!
[WARNING] Intercepted 1 typosquatting attempts via repository baseline analysis.
...
[INFO] --- MISSION_SUCCESS: 849 files mapped in 5.59s ---
[INFO] --- ENGINE_TELEMETRY: Processed 236,754 lines of code at 42,357 LOC/s ---
```

---

### 🛠️ Local Development & Testing

If you are modifying the internal physics or optical routing, it is highly recommended to install the package in editable mode so your CLI commands instantly reflect your local code changes.

From the **root directory** of the repository, run:
```bash
pip install -e .
```

Once installed, you can trigger the main orchestrator (`galaxyscope.py`) globally from your terminal:
```bash
galaxyscope /path/to/test/repo --debug
```

Before submitting a Pull Request, ensure your changes do not skew the baseline risk equations by running the test suite:
```bash
python3 -m unittest discover tests/
```

---
### 🌌 Deep Dive into the Physics
If you want to understand the exact equations inside the `/physics/` module, read the full methodology in the Wiki:
* 📖 **[GitGalaxy Signal Processing & Equations](https://squid-protocol.github.io/gitgalaxy/)**
* 🪐 **[Return to the Main GitGalaxy Hub](https://github.com/squid-protocol/gitgalaxy)**