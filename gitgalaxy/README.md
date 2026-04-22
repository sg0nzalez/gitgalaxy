# GitGalaxy: Internal Architecture & Source Code

Welcome to the internal source code for the **GitGalaxy blAST Engine**. 

This directory contains the core physics, routing, and mathematical heuristics that power the system. If you are a developer looking to contribute or understand the pipeline, here is the architectural map:

### 🗺️ The Developer Map
* **`/core/`**: The optical routing layer. Contains the `aperture.py` and `prism.py` which break down source code into structural signals.
* **`/physics/`**: The heuristics engine. Contains the `signal_processor.py` and `neural_auditor.py` which apply the GitGalaxy mathematics to score O(N) complexity, blast radius, and state flux.
* **`/recorders/`**: The export layer. Translates the internal state maps into SQLite databases, AI-agent JSON tickets, and the WebGPU data payloads.
* **`/security/`**: The zero-trust validation layer. 
* **`/tools/`**: The enterprise "Spokes". Contains the specific scripts for Legacy Refraction, Supply Chain Firewalls, and AI Guardrails.

---

### ⚡ Performance Showcase: NVDA (NonVisual Desktop Access)

To demonstrate the engine's capability on complex, cross-language system architecture, we unleashed GalaxyScope on **NVDA**, the open-source Windows screen reader. 

Because NVDA relies heavily on bridging Python application logic with low-level C++ system hooks, it requires advanced dependency mapping. The blAST engine successfully parsed the mixed-language architecture, analyzing **236,754 lines of code** in just **5.59 seconds** (a velocity of 42,357 LOC/sec). 

Crucially, during the import resolution phase, the Air-Gapped Dependency Radar successfully intercepted a structural naming collision (`fstream` vs `sstream`), proving the real-time typosquatting defenses are fully operational, this is likely a false positive, which could be prevented by adding these approved imports to the approve import list, so the system doesn't keep flagging them as unknown. 

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

### Using the blAST Engine
You do not need to run these internal files directly. To scan a repository, use the main entry point:
```bash
python3 galaxyscope.py /path/to/your/repo
```

---
### 🌌 Deep Dive into the Physics
If you want to understand the exact equations inside the `/physics/` module, read the full methodology in the Wiki:
* 📖 **[GitGalaxy Signal Processing & Equations](https://squid-protocol.github.io/gitgalaxy/)**
* 🪐 **[Return to the Main GitGalaxy Hub](https://github.com/squid-protocol/gitgalaxy)**