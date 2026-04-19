# DAG Architect (Data Lineage)

> **Architecture: Topological Sorting & Dead Logic Deflection**
>
> **Summary:** The DAG (Directed Acyclic Graph) Architect parses the structural intent of the repository to map Input/Output data flows. By analyzing which programs read and write to specific physical files, it mathematically calculates the perfect execution order for the entire mainframe cluster.

## The Ghost Deflector
Before analyzing data flows, the DAG Architect queries the Intermediate Representation (IR) State Manager for a list of dead paragraphs (unreachable logic). It deliberately masks out these dead zones during its AST scan. This prevents the regex engine from detecting `OPEN` statements that mathematically will never execute, ensuring the generated dependency graph is completely free of hallucinated edges.

## I/O Intent Mapping
The architect maps internal COBOL variables to their external physical boundaries (DD Names). It categorizes the execution intent based on standard legacy operations:
* **Read Operations:** `OPEN INPUT`
* **Write Operations:** `OPEN OUTPUT`
* **Mutation Operations:** `OPEN I-O` and `OPEN EXTEND` (These act as both Read and Write dependencies).

## Topological Execution Pipeline
Once all dependencies are mapped across the repository, the engine applies **Kahn's Algorithm** for topological sorting. 
* It calculates the in-degree (number of prerequisites) for every program.
* It builds a strict, linear execution sequence where no program runs until its data dependencies are fully satisfied.
* **Deadlock Detection:** If the algorithm detects a cyclic dependency (e.g., Program A waits on File 1 from Program B, but Program B waits on File 2 from Program A), it immediately halts the pipeline and isolates the deadlocked nodes for architectural review.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

