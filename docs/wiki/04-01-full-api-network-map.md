# Full API Network Map (The Boundary Cartographer)

> **Mapping the Attack Surface**
>
> While the core GitGalaxy engine maps the internal structural dependencies of the codebase (file-to-file), the Full API Network Map (`full_api_network_map.py`) is a standalone spoke designed to map the **external boundaries** of the repository. 
>
> It acts as the Boundary Cartographer, comparing the actual physical router code against official OpenAPI/Swagger documentation to hunt down undocumented "Shadow APIs" and exposed entry points.

## The Router Physics (Framework Traps)

Rather than simply reading configuration files, the tool utilizes specialized Regex Traps to parse the raw logic streams of multiple backend frameworks:

* **Python:** Scans `.py` files for FastAPI and Flask decorators (e.g., `@app.get` or `@router.post`).
* **Node.js:** Scans `.js` and `.ts` files for Express routes (e.g., `app.get` or `router.delete`).
* **Java:** Scans `.java` files for Spring Boot annotations (e.g., `@GetMapping` or `@PostMapping`).
* **Golang:** Scans `.go` files for Gorilla Mux and Gin router configurations.

The parser normalizes every discovered route into a standard `METHOD /path` string (e.g., `GET /api/users`).

## The Math (Set Theory Validation)

To determine the true security posture of the API boundary, the tool performs a Set Theory analysis comparing the "Physical Reality" (the code) against the "Approved Truth" (the documentation):

1. **The Baseline:** It parses the official `swagger.json` or `swagger.yaml` file to build a Set of Approved APIs.
2. **Shadow APIs (Critical Risk):** The tool subtracts the Approved Set from the Physical Set (`physical_endpoints - approved_apis`). This isolates APIs that are actively compiled and listening in the code but are hidden from the official documentation, creating a massive blind spot for security teams and penetration testers.
3. **Ghost APIs (Documentation Bloat):** It subtracts the Physical Set from the Approved Set (`approved_apis - physical_endpoints`). This isolates endpoints that are explicitly documented in Swagger but no longer physically exist in the source code, helping engineering teams clean up rotting documentation.

## The Presentation Dashboard

Because this tool is built for security and compliance teams, it prints a clean terminal dashboard. It explicitly lists the total counts for documented vs. physical endpoints, and clearly prints out the exact paths and files where any Shadow or Ghost APIs were discovered.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

