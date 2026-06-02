# Overview of Methodology & Risk Exposure Index

> **The Core Philosophy: From Raw Text to Relational Knowledge Graph**
>
> GitGalaxy does not measure subjective "Code Quality," which implies judgment. Instead, it measures objective **Risk Exposures**. 
>
> By utilizing deterministic keyword heuristics, the engine parses raw text to build a massive, interconnected knowledge graph of the entire repository. We extract structural markers from the code (the data) and translate them into visible risk heatmaps (the projection). This allows architecture teams to instantly see where their system is drifting into dangerous territory without reading a single line of code.
>
> **The Structural Taxonomy of GitGalaxy**
>
> GitGalaxy assesses functions against 50+ metrics. We then roll these measurements up to the class, file, folder and repo level. 

## The Universal Risk Spectrum

Regardless of the risk metric being viewed, the visual translation is always the same color palette:
* 🟦 **Blue:** Very Low Exposure 
* 🩵 **Cyan:** Low Exposure
* 🟨 **Yellow:** Moderate / Intermediate Exposure
* 🟧 **Orange:** High Exposure
* 🟥 **Bright Red:** Critical / Extreme Exposure (Hot / Dangerous)

## Primary Risk Exposures

**Definition:** The mathematical output of parsing regex heuristics, file boundaries, version control counts, and ecosystem multipliers. These metrics represent the unified risk calculations applied across the repository.

| Metric | Level 1: Function<br>([count based](08-02-sub-equations.md))<br>(0-infinity) | Level 2: Class<br>([count based](08-02-sub-equations.md))<br>(0-infinity) | Level 3: File<br>([Sigmoid normalized](08-03-transforming-regex-counts.md))<br>(0-100) | Level 4: Folder<br>(Weighted Avg)<br>(0-100) | Level 5: Repo<br>(Weighted Avg)<br>(0-100) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[Cognitive Load](08-05-cognitive-load.md)** | # of branches, mutations, and danger triggers, adjusted | Sum of function counts + Gini | Normalized via sigmoid function + GuideStar Shield | Mass-Weighted Avg | Mass-Weighted Avg |
| **[State Flux](08-16-state-flux-exposure.md)** | # of variable mutations, adjusted | Sum of function counts + LCOM | Normalized via sigmoid function | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Concurrency](08-15-concurrency-exposure.md)** | # of async/thread operations minus locks, adjusted | Sum of function counts | Normalized via sigmoid function | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Technical Debt](08-08-technical-debt.md)** | # of engineer comments (ex: HACK, TODO), adjusted | Sum of function counts | Normalized via sigmoid function | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Structural Fortification](08-07-structural-fortification.md)**| # of attacker vs. defender keywords, adjusted | Sum of function counts | Normalized via sigmoid function w/ Breach Floor | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Graveyard](08-13-graveyard-detector.md)** | N/A | N/A | Commented out code lines, normalized via sigmoid function | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Specification Alignment](08-18-specification-alignment.md)**| # of functions with Spec tags, adjusted | Sum of function counts w/ Spec mapping | Percentage of entities lacking spec tags, adjusted | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Civil War (Tabs/Spaces)](08-12-civil-war.md)** | N/A | N/A | Ratio of tab vs space indented lines, percentage | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Ownership Entropy](08-04-ownership-entropy.md)** | N/A | N/A | Distribution of git authors, normalized via Shannon entropy | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Deep Churn](08-06-deep-churn.md)** | N/A | N/A | Total git commits over time, normalized via log curve | Mass-Weighted Avg | Mass-Weighted Avg |
| **[File Stability (Heat)](08-10-file-stability.md)**| N/A | N/A | Time since last commit, normalized via time distance | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Verification Risk (Test Coverage)](08-11-test-coverage.md)**| # of unverified execution paths, adjusted | Sum of function counts | Normalized via sigmoid function * Cross-File Test Tethers | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Documentation Risk Exposure](08-09-documentation-risk.md)**| # of missing docstrings, comments, and readmes, adjusted | Sum of function counts | Normalized via sigmoid function * Bus Factor | Mass-Weighted Avg | Mass-Weighted Avg |
| **[API Exposure](08-14-api-exposure.md)** | # of export/public modifiers, adjusted | Sum of function counts + Public interfaces | Normalized via ratio and volume * Network Blast Radius | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Algorithmic DoS Exposure](08-24-Big-O-Detection.md)** | # of deep loops interacting with data/network, adjusted | Sum of function counts | Normalized via sigmoid function * Network Blast Radius | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Logic Bomb Exposure](08-20-logic-bomb-exposure.md)** | # of conditions leading to payloads, adjusted | Sum of function counts | Normalized via sigmoid function * Taint Flow Tracking | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Injection Surface Exposure](08-21-injection-surface-exposure.md)**| # of inputs flowing to execution, adjusted | Sum of function counts | Normalized via sigmoid function * Taint Flow Tracking | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Memory Corruption Exposure](08-22-memory-corruption-exposure.md)**| # of pointers/allocations minus cleanups, adjusted | Sum of function counts | Normalized via sigmoid function * ML Archetype Map | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Obscured Payload Exposure](08-19-obscured-payload-exposure.md)**| # of obfuscation and intent triggers, adjusted | Sum of function counts | Normalized via sigmoid function * Biaxial Drift | Mass-Weighted Avg | Mass-Weighted Avg |
| **[Hardcoded Secrets Exposure](08-23-hardcoded-secrets-exposure.md)**| N/A | N/A | Detected credential strings, normalized via sigmoid function | Mass-Weighted Avg | Mass-Weighted Avg |

## Custom Topological Scales

Certain metrics do not represent a "Safe to Dangerous" pipeline, but rather a difference in structural style within the graph. These bypass the Universal Spectrum and use custom rendering palettes.

* **Civil War (Tabs vs. Spaces):** Checks for indentation consistency across the codebase.
  * 🟩 **Green:** Strictly uses Tabs.
  * 🟨 **Yellow:** Strictly uses Spaces.
  * 🟦 **Blue:** A chaotic, mixed indentation style (The "Warzone").


---

## Expanding the Physics Framework

These documents outline the specific variables and mathematical normalization strategies that power the equations detailed in the matrix above.

* [08-02: Sub-Equations (Scanner Variables)](08-02-sub-equations.md)
* [08-03: Transforming Regex Counts (The UEF)](08-03-transforming-regex-counts.md)

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**