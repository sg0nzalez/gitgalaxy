# GitGalaxy: Network Auditing & Cartography

[![Frameworks](https://img.shields.io/badge/Supported-Python_|_Node_|_Java_|_Go-00C957.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-AST--Free_Regex-00BFFF.svg)](#)
[![Security](https://img.shields.io/badge/Security-Shadow_API_Hunter-FF4500.svg)](#)

Welcome to the **GitGalaxy Network Auditing Suite**.

Security documentation is theoretical. Compiled source code is physical reality. As monolithic codebases scale and microservices fracture, OpenAPI/Swagger specifications inevitably drift from the actual routing logic deployed in production. 

Attackers don't exploit the APIs you documented; they exploit the legacy test endpoints you forgot to remove. 

The **Full API Network Map** acts as a deterministic source of truth. It bypasses compilation and LLM hallucinations, utilizing raw structural regex to hunt down framework-specific web routers. It then applies strict set theory against your official Swagger documentation to isolate critical security gaps.

### 🧠 How It Works: Router Physics & Set Theory

1. **Extract the Theoretical Truth:** The engine parses your official security documentation (`swagger.json` or `swagger.yaml`) to build a baseline set of "Approved" APIs.
2. **Map the Physical Reality:** Utilizing "Router Physics" (highly optimized regex traps), the engine scans the raw text of the target codebase, identifying physical execution routes mapped by the underlying web frameworks.
3. **Mathematical Resolution:** The tool applies basic set theory to calculate exact risk exposure:
    * **Shadow APIs (Critical Risk):** `Physical - Approved`. Endpoints that exist in the codebase and can be executed by attackers, but are completely missing from security documentation.
    * **Ghost APIs (Documentation Bloat):** `Approved - Physical`. Endpoints that are officially documented and tested by security teams, but no longer exist in the physical source code.

### 🛠️ Core Capabilities

The AST-free routing heuristics natively support the industry's most common backend frameworks without requiring a build environment:
* **Python:** FastAPI & Flask (`@app.get`, `@router.post`)
* **Node.js / TypeScript:** Express (`app.get`, `router.post`)
* **Java:** Spring Boot (`@GetMapping`, `@PostMapping`)
* **Golang:** Gorilla Mux & Gin (`.GET`, `.HandleFunc`)

---

### 🚀 Quickstart: Running the Network Mapper

Execute the spoke tool directly, pointing it at both your physical source code and your theoretical documentation:

```bash
python3 full_api_network_map.py /path/to/source/code --swagger /path/to/swagger.json