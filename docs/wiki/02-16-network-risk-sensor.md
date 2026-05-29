# The Network Risk Sensor (Graph Topology)

> **Wiring the Universe**
>
> The Network Risk Sensor (`network_risk_sensor.py`) is responsible for transforming a flat list of isolated files into an interconnected, $N$-dimensional Directed Graph. 
>
> By mapping how files import and depend on each other, the sensor elevates GitGalaxy from a simple file scanner into a systemic risk engine. It calculates the absolute "Blast Radius" of every file, defines its architectural role, and aggregates repo-wide macro-physics to determine the structural resilience of the entire codebase.

## The Directed Graph

The sensor ingests the raw import strings extracted by the Language Lens and wires them into a NetworkX Directed Graph (`nx.DiGraph`). 

* **Fast Path Lookup:** It utilizes a pre-computed resolution map to instantly link `raw_imports` (like `import utils`) to their exact physical node counterparts (like `src/core/utils.py`).
* **Weighted Edges:** The graph is not uniformly weighted. If the upstream scanner detected an import tied to a specific entity (like a class or a specific function, rather than a generic file import), the sensor increases the edge weight by 1.5x to represent tighter logical coupling.

## Node Centrality & Blast Radius

Once the graph is wired, the sensor executes advanced network mathematics to determine the true gravity of every file:

* **PageRank (Load-Bearing Gravity):** Calculates the absolute importance of a file based on how many other important files depend on it. This is normalized (multiplied by 1000) to create the **Normalized Blast Radius**. Modifying a file with a high Blast Radius carries extreme regression risk.
* **Betweenness (Choke Points):** Measures how often a file acts as a bridge along the shortest path between two other domains. *Note: To maintain hyper-scale velocity on massive repositories (>5,000 nodes), Betweenness calculation is capped to a randomized sample size ($k=50$) to guarantee $O(N)$ execution speed*.
* **Closeness (Ripple Effect):** Measures how "close" a file is to every other file in the repository, dictating how fast a runtime error here will cascade across the application.

## Ecosystem Roles

A file's risk profile changes based on its role. The sensor calculates the ratio of incoming dependencies (`in_degree`) to total dependencies, strictly classifying every node:

* **Pure Producer (Foundation):** $>80\%$ of its edges are inbound. These are core libraries, utilities, or database schemas that the rest of the app relies upon.
* **Pure Consumer (Orchestrator):** $<20\%$ of its edges are inbound. These are controllers, UI views, or main entry points that pull in massive amounts of dependencies to execute logic.
* **Transceiver (Middle-Tier):** Sits between 20% and 80%, acting as a bridge passing data between producers and consumers.
* **Isolated/Orphan:** Has zero connections. It is either an unused file, a dynamic injection target, or a top-level script.

## Systemic Threats & Algorithmic Bottlenecks

Local risk is only half the story. A file with 90% Tech Debt is harmless if it's an isolated orphan; it is catastrophic if it is a foundational Producer.

* **Multi-Dimensional Systemic Threat:** The sensor cross-multiplies the Normalized Blast Radius against the 18-point local risk vector. This generates a new `systemic_threat_vector`, highlighting files that are both highly dangerous *and* highly depended upon.
* **Algorithmic Bottlenecks:** The sensor checks the file's Big-O depth and recursion markers. If a file has a Normalized Blast Radius $> 1.0$ AND it possesses an algorithmic complexity of $O(N^3)$ or higher (or is actively recursive), it is immediately flagged as an `is_algorithmic_bottleneck`. These are the primary targets for performance refactoring.

## Macro-Ecosystem Physics

After mapping individual stars, the sensor calculates the health and resilience of the entire galaxy using undirected subgraphs:

* **Modularity:** Are components cleanly separated (Microservice-like) or deeply tangled (Spaghetti code)?
* **Assortativity:** Do heavy files connect to other heavy files (Resilient core), or do heavy files connect to fragile files (Negative assortativity / Single points of failure)?
* **Cyclic Density:** What percentage of the repository is trapped in dependency loops (Static Friction)?
* **Average Path Length:** The average number of "hops" required to get from one file to any other file, indicating the tightness of system coupling.
* **Articulation Points:** The exact number of single files that, if removed or broken, would completely shatter the network graph into disconnected pieces.

### Zero-Dependency Fallback
If the host environment cannot run `networkx`, the sensor gracefully degrades into a Zero-Dependency Mode. It manually calculates direct in/out degrees to determine basic Ecosystem Roles and a heuristic Blast Radius, ensuring the pipeline never fails due to missing external math libraries.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
