# GitGalaxy

[![PyPI version](https://badge.fury.io/py/gitgalaxy.svg)](https://badge.fury.io/py/gitgalaxy)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: PolyForm Noncommercial](https://img.shields.io/badge/License-PolyForm%20Noncommercial-blue.svg)](https://polyformproject.org/licenses/noncommercial/1.0.0/)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0-brightgreen.svg)](https://pypi.org/project/gitgalaxy/)
[![Airgap Ready](https://img.shields.io/badge/Security-Airgap_Ready-teal.svg)](#)
[![Local Processing](https://img.shields.io/badge/Telemetry-100%25_Local-blueviolet.svg)](#)
[![Hardware Accelerated](https://img.shields.io/badge/Render-WebGPU_|_WebGL2-ff69b4.svg)](#)

Code is art. Logic is art. Systems engineering is art.

GitGalaxy reveals the complexity of codebases as explorable 3D galaxies by using source code as a seed for procedural generative art. It acts as a Rosetta Stone for code complexity, allowing you to visually compare the scale and risk exposure of different projects—from Apollo 11 to the Linux Kernel—under the same set of rules. 

> **Live Demo:** View 3D galaxy examples of Apollo-11, Linux, and more at [GitGalaxy.io](https://gitgalaxy.io/)

> **Note:** This is a condensed version of the full documentation. For the 200-page Architectural Master Blueprint, please visit: [https://github.com/squid-protocol/gitgalaxy](https://github.com/squid-protocol/gitgalaxy)

---

## Quickstart

### 1. Install

```bash
pip install gitgalaxy
```

### 2. Scan a Repository

Point the GalaxyScope at any local repository or ZIP archive. The engine runs entirely on your local machine—zero data is transmitted.

```bash
gitgalaxy /path/to/your/repo
```

### 3. View the Galaxy

GitGalaxy offers two ways to visualize your 3D architecture, both built on a strict Zero-Trust Privacy Model where your code never leaves your machine.

**Option A: The Web Viewer (Frictionless)**
Simply drag and drop your generated "your_repo_galaxy.json" file (or a .zip of your raw repository) directly into GitGalaxy.io. All rendering and scanning happens entirely in your browser's local memory.

**Option B: The Local Server (Enterprise & Offline)**
For teams working behind strict corporate firewalls, you can host the 3D viewer locally. Clone the repository and spin up the included Flask server:

```bash
git clone https://github.com/squid-protocol/gitgalaxy.git
cd gitgalaxy
python app.py
```

Then open http://localhost:5000 in your browser and drop your JSON file in securely.

## What Does it Measure?

GitGalaxy maps the hidden architecture of massive software repositories, translating codebases into non-numeric star-based dashboards (for humans), low-token markdown summaries (for AI agents), and full internal scanned audit results (for lawyers). 

Accomplished by scanning codebases with the same tech used to scan strings of DNA when I was a scientist. By employing a BLAST-like algorithm, a taxonomic language feature map, and DNA fingerprinting algorithms, GitGalaxy brings 50-ish years of bioinformatics to code analysis. We parse our resulting DNA/code fingerprint into a series of risk exposure metrics (genotype to phenotype assocations).

GitGalaxy does not measure "Code Quality", which feels like a judgment, but instead measures Risk Exposure. Our measurements do not judge; they highlight. We do not assess "Bad Code"; we measure Cognitive Load Exposure—how hard it is for a human to work through the logic—because teams should be aware which files are the hardest to work on. 

Risk Exposures identify general trends (this file has high API exposure) instead of providing an absolute ranking over tiny differences (this file is better than that one because it scored 6% higher in the tech debt equation). These are general guides to give engineers, managers and CTOs a visual estimate on code status. It allows a team to agree on standards and instantly see—without reading a single line of text—where their architecture might be drifting into dangerous territory.

## Zero-Trust Architecture

Your code never leaves your machine. GitGalaxy performs 100% of its scanning and vectorization locally.

* **No Data Transmission:** Source code is never transmitted to any API, cloud database, or third-party service.
* **Ephemeral Memory Processing:** Repositories are unpacked into a volatile memory buffer (RAM) and are automatically purged when the browser tab is closed.
* **Privacy-by-Design:** Even when using the web-based viewer, the data remains behind the user's firewall at all times.

## License & Copyright

Copyright (c) 2026 Joe Esquibel

GitGalaxy is released under the PolyForm Noncommercial License 1.0.0. It is completely free for personal use, research, experiment, testing, and hobby projects. Use by educational or charitable organizations is also permitted.

Any commercial use or integration into commercial SaaS products or corporate CI/CD pipelines requires a separate commercial license. Please reach out via gitgalaxy.io to discuss commercial integration.