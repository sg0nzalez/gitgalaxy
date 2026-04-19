# Mainframe Compiler Forge

> **Architecture: Era-Aware JCL Generation & AST Flattening**
>
> **Summary:** The MVS 3.8j COBOL Compiler Forge dynamically generates the exact Job Control Language (JCL) required to compile legacy payloads on IBM mainframes. It features a Dialect Sensor to prevent catastrophic compiler strokes by routing code to the correct compiler era (OS/VS vs. Enterprise).

## The Dialect Sensor
Mainframe compilers are notoriously fragile. Feeding post-1985 syntax into a 1974 compiler results in immediate ABENDs (Abnormal Ends). The forge scans the Abstract Syntax Tree (AST) for modern structural signatures (e.g., `EVALUATE`, `INITIALIZE`, inline `*>` comments, and explicit scope terminators like `END-IF`). 
* If detected, it routes the build step to the modern Enterprise Compiler (`IGYWCL`). 
* If absent, it conservatively routes to the legacy OS/VS Compiler (`COBUCL`).

## The Copybook Flattener
Legacy code frequently relies on external `COPY` statements, fragmenting the business logic across multiple files. To create a self-contained compilation payload, the forge recursively resolves and inlines all copybooks.
* **Infinite Loop Protection:** Because legacy systems often contain cyclic copybook references (A calls B, B calls A), the flattener enforces a strict recursion depth limit (maximum 10 layers). If the limit is exceeded, it forcefully aborts the cyclic branch to prevent memory exhaustion.

## Execution Intent Extraction
The forge parses the structural boundaries of the file to extract the `PROGRAM-ID` and all physical file allocations (`SELECT ... ASSIGN TO`). It uses this data to automatically scaffold the Phase 1 infrastructure provisioning steps (`IEFBR14`) in the generated JCL, ensuring all required datasets are allocated before the compiler runs.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

