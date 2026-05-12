# 🌌 GitGalaxy Documentation

**Code is art. Logic is art. Systems engineering is art.**

GitGalaxy is a high-velocity, deterministic function-level knowledge graph engine designed for planetary-scale codebases. 

While the project is widely recognized for its interactive 3D WebGL visualizer—which renders repositories as explorable galaxies—this visualizer is ultimately just a presentation layer. The true core of the project is the **blAST Engine** (Bypassing LLMs and ASTs): a polyglot structural physics engine that extracts the architectural heuristics of 50+ languages simultaneously without requiring compilation.

---

## 🧭 Where should I start?

GitGalaxy is a massive ecosystem. Choose your entry point based on your operational domain:

### 🛡️ For Enterprise Architects & DevSecOps
If you are looking to secure supply chains, audit AI agents, and generate compliance artifacts, start here:
* 📜 [The SHBOM Standard (Structural Health Bill of Materials)](01-07-the-shbom-standard.md)
* 🤖 [Autonomous AI Guardrails (Dev Agent Firewall)](01-08-autonomous-ai-guardrails.md)
* ⏱️ [The Continuous Delta Paradigm (CI/CD Integration)](01-09-the-continuous-delta-paradigm.md)
* 🗄️ [Cookbook: Enforce a Zero-Trust Supply Chain Firewall](cookbook/enforce-supply-chain-firewall.md)

### 🏦 For Legacy Modernization Teams
If you are tasked with breaking apart 40-year-old IBM monoliths without using an emulator:
* 🌉 [The Legacy Bridge (Mainframe Modernization Philosophy)](01-04-the-legacy-bridge.md)
* 🕸️ [The DAG Architect (Topological Execution Mapping)](05-08-dag-architect.md)
* ☕ [Cookbook: Refactoring COBOL into Spring Boot](cookbook/map-cobol-monoliths.md)

### ⚙️ For Systems Engineers (The Physics & Proofs)
If you want to understand the mathematics driving the engine and the empirical proofs that validate our AST-free approach:
* 🔬 [The blAST Paradigm (Heuristics vs. ASTs vs. LLMs)](01-03-the-blast-paradigm.md)
* ⚖️ [Claim 10: The Heuristic vs. AST Paradigm](03-10-claim-10-ast-vs-heuristic-parsing.md)
* 🛡️ [Claim 8: Empirical Validation of AST-Free Parsing (The Gauntlets)](03-08-claim-8-empirical-validation-of-ast-free-parsing.md)
* 📐 [The 13-Point Risk Exposure Equations](08-01-methodology.md)

---

## ⚙️ The Hub and Spoke Ecosystem

### 1. The Hub: The blAST Engine (GalaxyScope)
A hyper-scale, language-agnostic static analysis CLI. Bypassing traditional ASTs, it parses code at ~100,000 LOC/second using deterministic regular expressions and a multi-phase Physics Engine. It outputs rich JSON telemetry, SQLite databases, and low-token Markdown briefs optimized for AI-agent workflows.

### 2. The Spokes: Enterprise Operations
The core engine powers a massive ecosystem of specialized tools:
* **Legacy Modernization:** Automated pipelines to map, slice, and refactor legacy COBOL into modern Java microservices.
* **Security & Auditing:** Zero-trust firewalls that verify physical dependencies, hunt Shadow APIs, and perform Binary X-Rays.
* **AI Governance:** Threat sensors designed to hunt RCE Funnels, God-Mode Agents, and Context Window Shredders.

### 3. The Presentation: The Observatory
Drop your `_galaxy.json` into the free viewer at [GitGalaxy.io](https://gitgalaxy.io) or use the repo's `airgap_observatory`, a standalone WebGPU visualizer. Both visualizers read the JSON contract and render the entire codebase as a procedural 3D galaxy where files are stars, allowing humans to visually map scale and risk exposure instantly.

---

## 🚀 Quickstart

**1. Install**
```bash
pip install gitgalaxy
```

**2. Scan a Repository**
Point the GalaxyScope at any local repository or ZIP archive. The engine runs entirely on your local machine—zero data is transmitted.
```bash
galaxyscope /path/to/your/local/repo
```

**3. View the Galaxy**
GitGalaxy offers two ways to visualize your 3D architecture, both built on a strict Zero-Trust Privacy Model where your code never leaves your machine.
* **The Web Viewer (Frictionless):** Drag and drop your generated `_galaxy.json` file directly into [GitGalaxy.io](https://gitgalaxy.io). All rendering and scanning happens entirely in your browser's local memory.
* **The Local Server (Enterprise & Offline):** For teams operating under strict compliance rules, GitGalaxy includes a 100% static, zero-telemetry local viewer called the Airgap Observatory.

---

## 🔒 Zero-Trust Architecture

Whether you are running the command-line engine or the WebGL visualizer, GitGalaxy operates on a strict Zero-Trust Privacy Model: **Your code never leaves your computer.**

* **No Data Transmission:** Source code is never transmitted to any API, cloud database, or third-party LLM service.
* **Air-Gap Ready:** The entire suite of tools is designed to run in highly secure, internet-disconnected environments.
* **Ephemeral Memory Processing:** Repositories are unpacked into a volatile memory buffer and are automatically purged when the operation completes.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.