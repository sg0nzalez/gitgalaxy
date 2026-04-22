# GitGalaxy: API Security & Shadow API Detection

[![Frameworks](https://img.shields.io/badge/Supported-Python_|_Node_|_Java_|_Go-00C957.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-AST--Free_Regex-00BFFF.svg)](#)
[![Security](https://img.shields.io/badge/Security-Shadow_API_Hunter-FF4500.svg)](#)

Welcome to the **GitGalaxy API Security & Attack Surface Mapping Suite**.

Security documentation is often strictly theoretical, whereas compiled source code represents physical reality. Attackers do not exploit the APIs you have documented; they hunt for the forgotten, undocumented endpoints left exposed in your codebase.

Standard DevSecOps scanners rely on approved Swagger or OpenAPI files to dictate what should be tested. GitGalaxy provides a deterministic source of truth. By scanning the raw codebase at high velocity, we reveal the exact routing logic that is actively exposed to the network, regardless of what the documentation claims.

### 🔍 Core Methodology: OpenAPI Drift Detection

We utilize AST-free structural heuristics to bypass theoretical documentation and map physical routing logic.

* **Map Physical Reality:** Scans raw text for actual execution routes.
* **Extract Theoretical Truth:** Parses official Swagger or OpenAPI specifications.
* **Mathematical Resolution:** Applies strict set theory to expose critical security gaps and API drift.
* **Identify Shadow APIs (Critical Risk):** Exposes undocumented, active endpoints that evade standard WAFs and security audits.
* **Identify Ghost/Zombie APIs (Audit Bloat):** Highlights documented but non-existent or deprecated endpoints.

### ⚙️ Supported Frameworks

Our AST-free heuristics deterministically map open APIs without requiring a build environment or compiling code.

* **Python Routers:** FastAPI and Flask endpoints (`@app.get`).
* **Node.js Routers:** Express framework routes (`app.post`).
* **Java Routers:** Spring Boot mapping annotations (`@GetMapping`).
* **Golang Routers:** Gorilla Mux and Gin handlers (`.HandleFunc`).

---

### 🚀 Quickstart: Continuous Compliance Auditing

Execute the tool directly against your physical source code and your theoretical documentation to generate an immediate gap analysis:

```bash
python3 full_api_network_map.py /path/to/source/code --swagger /path/to/swagger.json
```

---

### 📊 The Audit Dashboard
Outputs a deterministic terminal dashboard optimized for CI/CD pipeline integration and security team review.

* **Shadow APIs Detected:** Lists physical files containing hidden, undocumented routers.
* **Ghost APIs Detected:** Lists missing routes to eliminate security team audit bloat.

---
### 🌌 Powered by the blAST Engine (Bypassing LLMs and ASTs)
This tool is a modular enterprise integration within the broader GitGalaxy architecture. It is driven by our custom mathematical heuristics engine, capable of mapping multi-dimensional relationships at extreme velocity. Read the official documentation to see how we deterministically map API routes:

* 📖 **[Full API Network Map Architecture](../../../docs/wiki/04-01-full-api-network-map.md)**
* 📖 **[The Network Risk Sensor Mechanics](../../../docs/wiki/02-16-network-risk-sensor.md)**
* 📖 **[API Exposure Risk Equations](../../../docs/wiki/08-14-api-exposure.md)**
* 🪐 **[Return to the Main GitGalaxy Hub](https://github.com/squid-protocol/gitgalaxy)**