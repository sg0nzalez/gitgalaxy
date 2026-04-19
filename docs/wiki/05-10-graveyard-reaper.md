# Graveyard Reaper (Dead Code Analysis)

> **Architecture: AST Resolution & Dead Logic Isolation**
>
> **Summary:** The Graveyard Reaper performs static analysis on the COBOL Abstract Syntax Tree (AST) to isolate orphaned data and mathematically unreachable code. By identifying this structural necrosis early, it prevents downstream forges from generating bloated cloud schemas or hallucinated microservices.

## The Inline Copybook Expander
Legacy COBOL frequently hides its variable declarations inside external `.cpy` files. Before the Reaper can accurately map memory usage, it must assemble the full execution context. 
* It recursively hunts for `COPY` statements and injects the target file's contents directly into the local memory string.
* **Dynamic Variable Swapping:** It actively parses `REPLACING ==OLD== BY ==NEW==` clauses during the injection phase, executing word-boundary regex substitutions to ensure the resulting AST perfectly matches what the mainframe compiler would see.

## Phase 1: Hunting Orphaned Data
The Reaper splits the code into the `DATA DIVISION` and `PROCEDURE DIVISION`. 
1. It scans the Data Division to build a master set of all declared variables (ignoring structural noise like `FILLER` or boolean `88` levels).
2. It executes a strict word-boundary scan against the Procedure Division.
3. Any variable that is declared in memory but never explicitly referenced in the execution logic is flagged as **Orphaned Memory**. This list is passed to the Schema Forge to prevent useless columns from being created in the PostgreSQL database.

## Phase 2: Hunting Phantom Paragraphs
To identify dead execution logic, the Reaper maps the control flow of the program:
1. It catalogs every paragraph (code block) defined in the file.
2. It assumes the very first paragraph is the "Main Entry Point" and is always executed.
3. It scans the entire file for explicit jump commands (`PERFORM` and `GO TO`) to build a set of all "Reached" targets.
4. Any paragraph that is declared but never reached by a jump command from the main execution tree is flagged as a **Phantom Paragraph**. This list is passed to the DAG Architect and Microservice Slicer so they know to completely ignore those lines of code.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

