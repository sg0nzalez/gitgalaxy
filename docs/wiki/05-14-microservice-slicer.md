# Microservice Slicer

> **Architecture: Recursive Taint-Tracking & Logic Extraction**
>
> **Summary:** The Microservice Slicer isolates specific business rules from massive monolithic files. By tracking a target variable through the AST, it extracts only the mathematically relevant lines of code, creating a perfectly isolated logic slice ready for autonomous LLM translation.

## The Alias Engine (Taint Tracking)
Variables in COBOL constantly change names as they move through different paragraphs. The slicer executes a multi-pass taint-tracking algorithm to map these aliases:
* It scans for assignment operators (`MOVE`, `ADD`, `SUBTRACT`). If a tainted variable touches a clean variable, the clean variable becomes tainted.
* It parses complex math formulas (`COMPUTE X = Y * Z`). If the target variable is part of the equation, all interacting variables are added to the alias map.
* It loops through the execution tree multiple times to ensure deeply chained aliases (e.g., Variable A mutates B, which later mutates C) are fully captured.

## Shared IR State Synergies
The Slicer heavily utilizes the global Intermediate Representation (IR) State Manager to enforce strict deterministic boundaries and prevent hallucinated dependencies:
* **Orphaned Memory Abort:** Before scanning, the slicer checks the target variable against the Graveyard Reaper's state. If the target is known to be dead memory, the slicer aborts immediately, saving heavy compute cycles.
* **The Ghost Deflector:** While mapping aliases, the slicer actively checks its current paragraph against the IR state. If the paragraph is flagged as mathematically unreachable, the slicer skips it. This prevents dead code from creating false-positive variable taints.
* **Extraction Shield:** During the final code extraction phase, the slicer physically refuses to extract lines of code that reside inside dead paragraphs, guaranteeing the resulting microservice payload contains 100% active, executable logic.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
