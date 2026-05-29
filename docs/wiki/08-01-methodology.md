# Overview of Methodology

> **The Core Philosophy: From Raw Text to Relational Knowledge Graph**
>
> GitGalaxy does not measure subjective "Code Quality," which implies judgment. Instead, it measures objective **Risk Exposures**. 
>
> By utilizing deterministic keyword heuristics, the engine parses raw text to build a massive, interconnected knowledge graph of the entire repository. We extract structural markers from the code (the data) and translate them into visible risk heatmaps (the projection). This allows architecture teams to instantly see where their system is drifting into dangerous territory without reading a single line of code.

## The Universal Risk Spectrum (A11y Standard)

To reduce cognitive load on the user, GitGalaxy abandons distinct color palettes for individual metrics. Instead, we project the knowledge graph's telemetry using a single, unified **High-Contrast Spectrum** for all risk and exposure dashboards. 

Regardless of the metric being viewed, the visual translation is always the same:
* 🟦 **Deep Blue:** Very Low Exposure (Safe / Cold / Clean)
* 🩵 **Cyan:** Low Exposure
* 🟨 **Yellow:** Moderate / Intermediate Exposure
* 🟧 **Orange:** High Exposure
* 🟥 **Bright Red:** Critical / Extreme Exposure (Hot / Dangerous)

## The Exposure Metrics (Graph Telemetry)

When a user selects a metric from the HUD, the visualizer queries the underlying knowledge graph and recolors the nodes using the Universal Spectrum. The table below defines what the engine's heuristics are actively hunting for, and what a "Red" (Critical) state represents for each mode.

| Labeling Mode | Heuristic Target | The "Red" (Critical) State Indicates... |
| :--- | :--- | :--- |
| **Cognitive Load** | **How hard is it to read?** Scans for deeply nested logic, sprawling methods, and high control-flow complexity. | The logic is incredibly difficult for a human to follow. A prime target for refactoring. |
| **Deep Churn** | **How often does it change?** Identifies files that are constantly being rewritten, patched, or reverted based on Git history. | The file refuses to settle down. It is highly fluid and likely a source of recurring bugs. |
| **Error & Exception Exposure** | **Is it fragile?** Compares the ratio of defensive code (error handling, guards) against aggressive logic. | The file lacks safety nets. It is performing complex logic without adequate exception handling. |
| **Tech Debt** | **Are there shortcuts?** Scans for `TODO`s, `FIXME`s, known hacks, and temporary architectural band-aids. | The file is heavily burdened by unfinished business and documented technical debt. |
| **Documentation Risk** | **Is it explained?** Measures the ratio and quality of instructional literature against the raw executable code. | The file is essentially undocumented. It operates as a "black box" to new developers. |
| **Verification (Tests)** | **Is it proven?** Checks if the file has a corresponding safety net of tests proving it works. | The code is heavily exposed due to a severe lack of testing and verification coverage. |
| **Stability (Heat)** | **Is it fresh?** Shows where work is happening *right now* vs. code that was written months ago via OS `mtime` or Git logs. | The file is "Hot." It has been actively edited or committed in the very recent past. |
| **Graveyard** | **Is there dead code?** Finds massive blocks of code that were commented out and abandoned. | The file is hoarding historical, dead code that needs to be purged. |
| **API Exposure** | **Is it public?** Highlights the entry points and network routers where the system talks to the outside world. | The file serves as a major public endpoint, demanding strict security scrutiny. |
| **Concurrency** | **Is it multitasking?** Highlights complex timing, threads, or asynchronous execution logic. | Heavy reliance on asynchronous timing, introducing severe risks for race conditions. |
| **State Flux** | **Is the data changing?** Highlights variables that are constantly being modified or mutated in memory. | "Boiling" data. The file mutates state aggressively, making it hard to track standard values. |
| **Ownership Entropy** | **Who wrote this?** Measures the Shannon Entropy of Git blame data to see if a file is owned by one person or many. | A "Community" file. It has been touched by so many different developers that no single person truly owns it. |

## Custom Topological Scales

Certain metrics do not represent a "Safe to Dangerous" pipeline, but rather a difference in structural style or identity within the graph. These bypass the Universal Spectrum and use custom rendering palettes.

* **Civil War (Tabs vs. Spaces):** Checks for indentation consistency across the codebase.
  * 🟩 **Green:** Strictly uses Tabs.
  * 🟨 **Yellow:** Strictly uses Spaces.
  * 🟦 **Blue:** A chaotic, mixed indentation style (The "Warzone").
* **Language Identity:** Colors the file based on its evaluated taxonomy (e.g., JavaScript is Yellow, Python is Blue, Rust is Orange) to create a visual map of the system's tech stack.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
