# GitGalaxy

[![PyPI version](https://badge.fury.io/py/gitgalaxy.svg)](https://badge.fury.io/py/gitgalaxy)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: PolyForm Noncommercial](https://img.shields.io/badge/License-PolyForm%20Noncommercial-blue.svg)](https://polyformproject.org/licenses/noncommercial/1.0.0/)

[![Engine](https://img.shields.io/badge/Engine-blAST-8A2BE2.svg)](#)
[![Velocity](https://img.shields.io/badge/Velocity-100k+_LOC%2Fs-00C957.svg)](#)
[![Analysis](https://img.shields.io/badge/Analysis-Code_Bioinformatics-00BFFF.svg)](#)
[![Threat Hunting](https://img.shields.io/badge/Threat_Hunting-Behavioral-FF4500.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-Zero__Trust-teal.svg)](#)

[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0-brightgreen.svg)](https://pypi.org/project/gitgalaxy/)
[![Airgap Ready](https://img.shields.io/badge/Security-Airgap_Ready-teal.svg)](#)


Code is art. Logic is art. Systems engineering is art.

GitGalaxy is a two-part ecosystem connected by a universal JSON contract. It is designed to extract the structural DNA of massive software repositories and render their non-visual architecture into measurable, explorable 3D galaxies.

**1. The blAST Engine - The galaxyscope (Backend):** A hyper-scale, language-agnostic static analysis CLI. Based on 50 years of bioinformatics and genetic sequencing algorithms, it parses code at ~100,000 LOC/second. It outputs rich JSON telemetry, SQLite databases, and low-token Markdown briefs optimized for AI-agent workflows.

**2. The Observatory (Frontend):** Drop your galaxy.json into the free viewer at [GitGalaxy.io](https://gitgalaxy.io/) or use the repo's airgap_observatory, a standalone, zero-telemetry WebGPU visualizer. Both visualizers read the JSON contract and renders the entire code base as a procedural 3D galaxy where files are stars, allowing humans to visually map scale and risk exposure instantly.

**Live Demo:** View 3D galaxy examples of Apollo-11, Linux, Tensorflow and more at [GitGalaxy.io](https://gitgalaxy.io/)

> **📖 Official Documentation:** Read the full technical specifications, architecture blueprints, and the Taxonomical Equivalence Map at **[squid-protocol.github.io/gitgalaxy](https://squid-protocol.github.io/gitgalaxy/)**.

---

## Quickstart

### 1. Install

```bash
pip install gitgalaxy
```

### 2. Scan a Repository

Point the GalaxyScope at any local repository or ZIP archive. The engine runs entirely on your local machine—zero data is transmitted.

```bash
galaxyscope /path/to/your/local/repo
```

### 3. View the Galaxy

GitGalaxy offers two ways to visualize your 3D architecture, both built on a strict Zero-Trust Privacy Model where your code never leaves your machine.

**Option A: The Web Viewer (Frictionless)**
Simply drag and drop your generated "your_repo_galaxy.json" file (or a .zip of your raw repository) directly into GitGalaxy.io. All rendering and scanning happens entirely in your browser's local memory.

**Option B: The Local Server (Enterprise & Offline)**
For teams operating under strict compliance rules or behind corporate firewalls, GitGalaxy includes a 100% static, zero-telemetry local viewer called the Airgap Observatory.

There is no backend, no database, and no external API calls. It is a completely closed-box system built on static HTML and JavaScript, you just need to spin up a basic local server to view it.

Navigate into the visualizer folder and start Python's built-in static web server:

```bash
git clone https://github.com/squid-protocol/gitgalaxy.git
cd gitgalaxy/airgap_observatory
python3 -m http.server 8000
```
Open your web browser and go to http://localhost:8000.

Drag and drop your newly generated _galaxy.json file to instantly render your architecture.

## 🧬 The blAST Paradigm: Sequencing the DNA of Software

Traditional computer science treats software like a rigid blueprint, using slow, language-specific Abstract Syntax Trees (ASTs) to analyze code. GitGalaxy treats code as a living, mutating organism using **blAST (Broad Lexical Abstract Syntax Tracker)**.

By applying the principles of biological sequence alignment to software, blAST hunts for the universal structural markers of logic across ~40 languages and ~250 file extensions. We translate this genetic code into "phenotypes"—measurable risk exposures.

### Sequencing at Hyper-Scale
By abandoning the compiler bottleneck, blAST achieves processing velocities that traditional ASTs simply cannot comprehend. In live telemetry tracking across the largest open-source ecosystems, blAST demonstrated its absolute scale:
* **Peak Velocity:** Sequenced the 141,445 lines of the original **Apollo-11** Guidance Computer assembly code in **0.28 seconds** (an alignment rate of **513,298 LOC/s**).
* **Massive Monoliths:** Chewed through the **3.2 million lines of OpenCV in just 11.11 seconds** (288,594 LOC/s). 
* **Planetary Scale:** Effortlessly mapped the architectural DNA of planetary-scale repositories like **TensorFlow (7.8M LOC)**, **Kubernetes (5.5M LOC)**, and **FreeBSD (24.4M LOC)** in a fraction of the time required to compile them.

## Zero-Trust Architecture

Your code never leaves your machine. GitGalaxy performs 100% of its scanning and vectorization locally.

* **No Data Transmission:** Source code is never transmitted to any API, cloud database, or third-party service.
* **Ephemeral Memory Processing:** Repositories are unpacked into a volatile memory buffer (RAM) and are automatically purged when the browser tab is closed.
* **Privacy-by-Design:** Even when using the web-based viewer, the data remains behind the user's firewall at all times.

### The Viral Security Lens: Behavioral Threat Hunting
Traditional security scanners rely on rigid, outdated virus signatures. blAST acts like an immune system, hunting for the *behavioral genetic markers* of a threat. By analyzing the structural density of I/O hits, execution triggers, and security bypasses, blAST is perfectly engineered to stop modern attack vectors:

* **Supply-Chain Poisoning:** Instantly flags seemingly innocent setup scripts that possess an anomalous density of network I/O and dynamic execution (`eval`/`exec`).
* **Logic Bombs & Sabotage:** Identifies code designed to destroy infrastructure by catching dense concentrations of catastrophic OS commands and raw hardware aborts.
* **Steganography & Obfuscated Malware:** Mathematically exposes evasion techniques, flagging Unicode Smuggling (homoglyph imports) and sub-atomic custom XOR decryption loops.
* **Credential Hemorrhaging:** Acts as a ruthless data vault scanner, isolating hardcoded cryptographic assets (`.pem`, `.pfx`, `.jks` files) buried deep within massive repositories.

## License & Copyright

Copyright (c) 2026 Joe Esquibel

GitGalaxy is released under the PolyForm Noncommercial License 1.0.0. It is completely free for personal use, research, experiment, testing, and hobby projects. Use by educational or charitable organizations is also permitted.

Any commercial use or integration into commercial SaaS products or corporate CI/CD pipelines requires a separate commercial license. Please reach out via gitgalaxy.io to discuss commercial integration.
