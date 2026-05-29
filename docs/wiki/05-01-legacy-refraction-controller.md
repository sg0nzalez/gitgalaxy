# Legacy Refraction Controller

> **Architecture: Hybrid Intermediate Representation (IR) State Manager**
>
> **Summary:** The COBOL Refractor Controller is the core orchestration engine for the legacy modernization suite. It scans procedural COBOL repositories, extracts the deterministic business logic, and translates it into a standardized JSON Intermediate Representation (IR). 
>
> **OOM Prevention:** To handle planetary-scale legacy monoliths without crashing, the controller utilizes an auto-scaling Hybrid State Manager. It scouts the repository mass upon execution; if the mass exceeds safe limits (e.g., >2,000 files or >200 MB), it seamlessly shifts the IR state from High-Speed RAM into a localized SQLite3 database to prevent Out-Of-Memory (OOM) failures.

## The Three-Phase Extraction Pipeline

The pipeline processes each legacy payload through a strict, shared-state architecture to ensure no execution logic is lost during translation.

### Phase 0: Lexical Sanitization
The engine executes the Lexical Patcher to neutralize known architectural traps (e.g., legacy `NEXT SENTENCE` directives) before the main analysis begins, ensuring a clean, deterministic Abstract Syntax Tree.

### Phase 1: Reconnaissance & Analysis
* **The Graveyard Reaper:** Scans the code to identify "Dead Memory" (orphaned variables) and "Phantom Logic" (unreachable paragraphs). This structural necrosis is mapped and saved to the State Manager so downstream forges know what to ignore.
* **The DAG Architect:** Maps the Input/Output intent of the file, deliberately querying the Graveyard state to deflect and ignore ghost dependencies.
* **Honesty Protocol:** Scans for structural anomalies, system limit overrides, and unresolved dynamic `CALL` statements, logging them into a master audit report for manual architectural review.

### Phase 2: Context-Aware Generation
* **Schema Forge:** Translates the active memory map into Cloud Schemas (JSON/SQL), explicitly bypassing the orphaned variables identified in Phase 1 to prevent schema bloat.
* **Zero-Trust JCL Forge:** Utilizes the DAG lineage to generate highly restricted, zero-trust Job Control Language (JCL) emulators.
* **Microservice Slicer:** Slices the business logic based on target variables, skipping dead execution blocks to output a perfectly isolated JSON rule set ready for LLM translation.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
