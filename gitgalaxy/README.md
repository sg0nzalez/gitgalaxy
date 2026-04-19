# GitGalaxy: Internal Architecture & Source Code

Welcome to the internal source code for the **GitGalaxy blAST Engine**. 

This directory contains the core physics, routing, and mathematical heuristics that power the system. If you are a developer looking to contribute or understand the pipeline, here is the architectural map:

### 🗺️ The Developer Map
* **`/core/`**: The optical routing layer. Contains the `aperture.py` and `prism.py` which break down source code into structural signals.
* **`/physics/`**: The heuristics engine. Contains the `signal_processor.py` and `neural_auditor.py` which apply the GitGalaxy mathematics to score O(N) complexity, blast radius, and state flux.
* **`/recorders/`**: The export layer. Translates the internal state maps into SQLite databases, AI-agent JSON tickets, and the WebGPU data payloads.
* **`/security/`**: The zero-trust validation layer. 
* **`/tools/`**: The enterprise "Spokes". Contains the specific scripts for Legacy Refraction, Supply Chain Firewalls, and AI Guardrails.

### Using the blAST Engine
You do not need to run these internal files directly. To scan a repository, use the main entry point:
~~~bash
python3 galaxyscope.py /path/to/your/repo
~~~

---
### 🌌 Deep Dive into the Physics
If you want to understand the exact equations inside the `/physics/` module, read the full methodology in the Wiki:
* 📖 **[GitGalaxy Signal Processing & Equations](https://squid-protocol.github.io/gitgalaxy/)**
* 🪐 **[Return to the Main GitGalaxy Hub](https://github.com/squid-protocol/gitgalaxy)**