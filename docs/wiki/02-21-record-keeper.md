# The SQLite Record Keeper (Relational Graphing)

> **The Portable Source of Truth**
>
> The Record Keeper (`record_keeper.py`) is the serialization engine responsible for translating GitGalaxy's multi-dimensional RAM state into a highly portable, relational SQLite database (`_galaxy_graph.sqlite`). 
>
> While the GPU Recorder creates compressed payloads for visual rendering, the Record Keeper builds a structured, queryable knowledge graph designed specifically to empower Autonomous AI Agents and custom CI/CD analytics pipelines.

## The Architectural Pivot: SQLite vs. Neo4j / Cypher

In earlier iterations of code-graphing tools, the industry standard was to export dependency maps into dedicated Graph Databases (like Neo4j) and query them using Graph Query Languages (like Cypher), often requiring heavy Node.js backend drivers. 

GitGalaxy fundamentally rejects this approach in favor of native SQLite for three critical reasons:

### 1. Superior LLM Synergy (Text-to-SQL vs. Text-to-Cypher)
Large Language Models (like GPT-4o or Claude 3.5) are trained on billions of lines of standard SQL. They understand relational joins, aggregations, and subqueries with near-perfect accuracy. In contrast, LLM training data for Cypher is vastly smaller. When autonomous agents attempt to write complex graph traversals in Cypher, they frequently hallucinate syntax or misinterpret node/edge property mappings. By providing a clean SQLite schema, GitGalaxy guarantees that RAG (Retrieval-Augmented Generation) agents can natively write flawless queries against the codebase.

### 2. Zero-Infrastructure Portability
A Neo4j or Node.js-backed architecture requires standing up Docker containers, managing network ports, and maintaining persistent storage volumes. GitGalaxy's SQLite output is a single, isolated `.sqlite` file. It can be attached to an email, dropped into an S3 bucket, or instantly queried by lightweight Python agents (via `sqlite3`) and WASM-based browser environments without spinning up a single server.

### 3. Schema Simplicity
Code architecture is inherently relational. By mapping files to functions, and files to dependencies using strict Foreign Keys, we eliminate the ambiguous property-graph bloat. The relational structure forces strict typing and mathematical integrity.

## The Relational Schema

The Record Keeper extracts the live object state and constructs a highly normalized database schema optimized for fast analytical queries:

* **`stars` (The Core Ledger):** The master table containing the primary telemetry for every file. It includes pre-calculated columns for the 18-point Risk Vector, Structural Mass, Volatility, AI Threat Confidence, and Network Centrality (PageRank).
* **`constellations` (Neighborhoods):** Folder-level aggregate metrics, allowing agents to query the health of entire architectural domains rather than just isolated files.
* **`satellites` (Internal Logic):** Maps every extracted function, class, or method back to its parent `star_id`. It includes specific function-level metrics like Big-O complexity, argument counts, and Control Flow Ratios.
* **`dna_hits` (The Regex Ledger):** A flattened, highly indexed table containing every single regex pattern triggered by a file. This allows security agents to instantly query, for example, "Show me all files that contain `sec_danger` hits."
* **`inbound_dependencies` & `outbound_dependencies` (The Edge Tables):** The bi-directional graph represented as relational join tables. This dual-table approach allows an agent to easily query "Blast Radius" (who imports me?) and "Fragility" (who do I import?) using standard `INNER JOIN` logic.

## Empowering Autonomous Workflows

By bridging the gap between raw file parsing and standard SQL, the Record Keeper turns a repository into a queryable dataset. 

Instead of writing brittle Python scripts to traverse abstract syntax trees, an LLM agent can now simply execute a SQL query to answer complex architectural questions, such as: *"Find all files with a PageRank greater than 1.0, that have high State Flux, and are imported by the authentication module."*

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

