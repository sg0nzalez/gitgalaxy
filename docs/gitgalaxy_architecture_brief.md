# ARCHITECTURAL_BRIEF: gitgalaxy
> INSTRUCTION: Deterministic Syntactic Physics. Base architectural insights on Mass, DNA, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope v6.2.0 (Delta Mode)` |
| **Target Path** | `/home/runner/work/gitgalaxy/gitgalaxy` |
| **Timestamp** | `2026-05-31T16:17:49.805409+00:00` |
| **Scan Duration** | `5.91s` |
| **Git Branch** | `main` |
| **Git Commit** | `b1fd5958f888395964e57b194cf1aba6d231b03d` |
| **Git Remote** | `https://github.com/squid-protocol/gitgalaxy` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_MALWARE_DETECTED**
> XGBoost Structural DNA model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> Code is art. Logic is art. Systems engineering is art.
> You are analyzing software architecture through the lens of GitGalaxy. GitGalaxy acts as a Rosetta Stone for code complexity, translating the non-visual architecture of repositories into measurable metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We do not assess 'Bad Code'; we measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into dangerous territory, not incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural DNA (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
> 
> **THE STRUCTURAL DNA LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (catastrophic triggers), `flux` (state mutation), `graveyard` (dead code), `safety_neg` (bypassing types).
> * **Architecture & Domain:** `io` (external latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `Error & Exception handling, `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE PHYSICS (EQUATIONS & CONTEXT)
> **How the Physics Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`. High scores indicate a high density of decision-making, conditional branching, and complex state management packed into a small area.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`. High scores mean risky operations (dynamic execution, type bypasses, unhandled mutations) exceed defensive guardrails (try/catch blocks, type checks, assertions). **Breach Cap:** If danger density is too high, the score is mathematically floored to a high-risk state regardless of defense. A value of near 30 is near minimum floor as gitgalaxy tests for testing file pairs, testing folders but not actually their contents.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`. High scores indicate a high volume of temporary workarounds, fragile logic, and incomplete implementations relative to the file size.
> 4. **Verification (Testing) Risk Exposure:** Measures the density of unit testing and programmatic assertions. Evaluates `Test Density` + `Sibling Bonus` (if a dedicated test file exists). High scores (100% risk) mean the logic lacks internal test coverage and has no dedicated sibling test file, increasing the risk of silent failures during refactoring. **Mass Penalty:** Files over 300 LOC get an automatic risk penalty because massive files are inherently harder to test completely.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`. Weighted by logarithmic volume. High scores indicate that a large percentage of the file's functions and classes are explicitly exported or publicly accessible by external systems.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic. `Density(Async/Thread Hits)`. High scores indicate a high risk of race conditions, deadlocks, and complex execution timing issues.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment. `Density(State Mutations / LOC)`. High scores indicate unstable data states with constant side-effects, making state tracking difficult and unpredictable.
> 8. **Graveyard (commented out code):** Measures the presence of abandoned, commented-out logic blocks. `Density(Commented-out Code / LOC)`. High scores indicate messy refactoring trails that create visual clutter and confusion for maintainers.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements. `Inverse Ratio(Spec Hits / Total Functions)`. 100% Risk means no functions are tagged to a specification (undocumented exploratory logic); 0% means all logic is explicitly anchored to documented requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan. `Ratio(Seconds from Last Edit / Total Repo Lifespan)`. 100% Risk = Edited very recently; 0% Risk = Untouched for a long period.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification. `(Commits / sqrt(Age in Weeks))`. Normalized globally so the file with the most commits relative to its age is always 100%, indicating a constant hotspot for changes.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata. `Inverse Density(Doc Hits + Ownership / LOC)`. High risk means the file contains complex logic but lacks explanatory comments or structured metadata tags (like JSDoc) for developers.
> 13. **Civil War - DONT MENTION:** Measures formatting consistency regarding indentation. 0% = File is in pure Tabs, 100% = File is in Pure Spaces, 50% = Mixed indentation. (Provided for human context, not a functional risk) DO NOT MENTION THIS ONE .
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk (obscured_payload):** Measures the density of obfuscated logic, packed strings, and non-standard encoding. High scores indicate code that is structurally evading human readability or static analysis.
> 15. **Destructive Execution Surface (logic_bomb):** Measures condition-heavy execution leading to destructive OS, memory, or process commands. High scores indicate a weaponizable surface where logic could easily be hijacked for sabotage.
> 16. **Injection Surface Risk Exposure (injection_surface):** Measures external network/I/O input flowing directly into dynamic execution contexts without safety nets (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure (memory_corruption):** Measures the density of raw pointer math, manual memory allocations, and forceful casts without mitigations (Buffer Overflows, UAF). Primarily affects C/C++/Rust.
> 18. **Secrets Risk Exposure (secrets_risk):** Measures the presence of hardcoded credentials (RHS assignments) exposed to logs, globals, or graveyard code. Any score > 0 is a critical alert.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. **This is NOT a risk score.** It measures the volume of decision-making, parameter coupling, and length. High impact means the function is a load-bearing 'Main Character' in the logic.
> **20. File Magnitude (Total Mass):** Measures the total gravitational pull of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. **This is NOT a risk score.** A massive file simply means it is a heavily connected, structurally dense hub, whereas a lightweight file is a simple utility or config.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 604 |
| Visible Matter (Scanned) | 150 |
| Dark Matter (Non-scanned - binaries, images, extensions without definitions) | 454 |
| Total LOC | 40927 |
| Volatility Index | 0.02 |
| % Scanned of codebase = | 24.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 106 | 35293 | 70.7% |
| MARKDOWN | 25 | 0 | 16.7% |
| JAVASCRIPT | 10 | 2988 | 6.7% |
| PLAINTEXT | 3 | 0 | 2.0% |
| HTML | 3 | 2141 | 2.0% |
| CSS | 2 | 449 | 1.3% |
| YAML | 1 | 56 | 0.7% |

## 4.5 REPOSITORY MACRO-SPECIES (GLOBAL ARCHITECTURE)
> **Assigned Macro-Species:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.602`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 MICRO-SPECIES (FILE ARCHETYPES & STATIC MASS)
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 100 | 66.7% |
| file_cluster_13 | 12 | 8.0% |
| file_cluster_17 | 4 | 2.7% |
| file_cluster_0 | 3 | 2.0% |
| file_cluster_4 | 2 | 1.3% |
| file_cluster_2 | 1 | 0.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 28 | 18.7% |

## 4.7 AI & MACHINE LEARNING TOPOLOGY
> **Classification:** `Non-AI / Traditional`

## 5. DARK MATTER (Non-scanned items ARTIFACTS)
*Total Excluded Artifacts: 454*

**Composition by Extension & Reason:**
- `.md`: 329x Excluded (System Exclusion, Hidden Directory, or Dynamic Black Hole), 1x Excluded (Machine-Generated Source Code Signature: 38 LOC), 1x Excluded (Machine-Generated Source Code Signature: 34 LOC)
- `.png`: 60x Excluded (Explicitly Blacklisted Extension: '.png')
- `.gif`: 18x Excluded (Explicitly Blacklisted Extension: '.gif')
- `no_extension`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Black Hole)
- `.yml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Black Hole)
- `.py`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Black Hole), 1x Excluded (Machine-Generated Source Code Signature: 318 LOC), 1x Excluded (Machine-Generated Source Code Signature: 516 LOC)
- `.go`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Black Hole)
- `.html`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Black Hole)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Black Hole)
- `.f`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Black Hole)
- `.cpp`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Black Hole)
- `.hpp`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Black Hole)
- `.svg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Black Hole)
- `.xml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Black Hole)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Black Hole)

## 6. RISK EXPOSURE PHYSICS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 94.3 | 10.8 | 4.0 | 0.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 16.0 | 0.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 90.2 | 4.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 100.0 | 54.3 | 67.7 | 67.7 |
| API Exposure | 0.0 | 11.0 | 3.0 | 2.6 | 0.0 |
| Concurrency Exposure | 0.0 | 22.2 | 1.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 29.3 | 8.3 | 0.0 | 0.0 |
| Graveyard Exposure | 0.0 | 8.4 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 75.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.8 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 7.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 17.2 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 5.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `gitgalaxy/standards/language_standards.py` (Hits: 32)
- `gitgalaxy/licensing.py` (Hits: 20)
- `gitgalaxy/tools/compliance/sbom_generator.py` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These files act as core load-bearing infrastructure. Changes here carry a high risk of cascading breaks.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
2. **README.md** (`README.md`) — 0 inbound connections
3. **README.md** (`gitgalaxy/README.md`) — 0 inbound connections
4. **README.md** (`gitgalaxy/core/README.md`) — 0 inbound connections
5. **README.md** (`gitgalaxy/physics/README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **galaxyscope.py** (`gitgalaxy/galaxyscope.py`) — 44 outbound dependencies
2. **cobol_refractor_controller.py** (`gitgalaxy/cobol_refractor_controller.py`) — 16 outbound dependencies
3. **sbom_generator.py** (`gitgalaxy/tools/compliance/sbom_generator.py`) — 15 outbound dependencies
4. **supply_chain_firewall.py** (`gitgalaxy/tools/supply_chain_security/supply_chain_firewall.py`) — 13 outbound dependencies
5. **cobol_to_java_test_forge.py** (`gitgalaxy/tools/cobol_to_java/cobol_to_java_test_forge.py`) — 12 outbound dependencies

## 8. FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `renderSearchResults` (@ `site/index.html`) -> Impact: **1691.3** | LOC: 968
- `calculateFrequency` (@ `site/js/core/metavisualizer.html`) -> Impact: **1286.2** | LOC: 262
- `audit` (@ `gitgalaxy/physics/spectral_auditor.py`) -> Impact: **1026.2** | LOC: 364
- `extract_lineage` (@ `gitgalaxy/tools/cobol_to_cobol/cobol_dag_architect.py`) -> Impact: **687.6** | LOC: 173
  * *Intent:* """ X-Rays a COBOL program to map internal variables to external physical files. Utilizes shared IR context to mask out dead code and prevent hallucin...
- `_renderTiledPrintCanvas` (@ `site/tools/poster.js`) -> Impact: **530.5** | LOC: 390
- `_process_file_worker` (@ `gitgalaxy/galaxyscope.py`) -> Impact: **501.9** | LOC: 378
- `loadSector` (@ `site/js/core/galaxy-engine.js`) -> Impact: **473.3** | LOC: 259
- `map_ecosystem` (@ `gitgalaxy/core/network_risk_sensor.py`) -> Impact: **466.0** | LOC: 220
- `_calculate_galactic_popularity` (@ `gitgalaxy/galaxyscope.py`) -> Impact: **401.1** | LOC: 263
- `run_mission` (@ `gitgalaxy/galaxyscope.py`) -> Impact: **353.7** | LOC: 285

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `audit` (@ `gitgalaxy/physics/spectral_auditor.py`) -> **O(2^N) [Recursive]**
- `flatten_copybooks` (@ `gitgalaxy/tools/cobol_to_cobol/cobol_compiler_forge.py`) -> **O(2^N) [Recursive]**
- `extract_lineage` (@ `gitgalaxy/tools/cobol_to_cobol/cobol_dag_architect.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ X-Rays a COBOL program to map internal variables to external physical files. Utilizes shared IR context to mask out dead code and prevent hallucin...
- `animate` (@ `site/js/core/galaxy-engine.js`) -> **O(2^N) [Recursive]**
- `renderTree` (@ `site/tools/ally.js`) -> **O(2^N) [Recursive]**
  * *Intent:* // Navigate and create folders
- `generatePreview` (@ `site/tools/poster.js`) -> **O(2^N) [Recursive]**
- `calculateFrequency` (@ `site/js/core/metavisualizer.html`) -> **O(2^N) [Recursive]**
- `fmt` (@ `site/js/core/metavisualizer.html`) -> **O(2^N) [Recursive]**
- `fmt` (@ `site/js/core/metavisualizer.html`) -> **O(2^N) [Recursive]**
- `toggleSystemProfile` (@ `site/index.html`) -> **O(2^N) [Recursive]**
  * *Intent:* // --- NATIVE METAVISUALIZER HANDOFF ---

### Highest Data Gravity (Database Complexity)
- `enforce_licensing_guard` (@ `gitgalaxy/licensing.py`) -> DB Complexity: **60**
- `renderSearchResults` (@ `site/index.html`) -> DB Complexity: **60**
- `setupEvents` (@ `site/js/core/galaxy-engine.js`) -> DB Complexity: **56**
- `init` (@ `site/js/main.js`) -> DB Complexity: **48**
- `animate` (@ `site/js/core/galaxy-engine.js`) -> DB Complexity: **44**
- `loadSector` (@ `site/js/core/galaxy-engine.js`) -> DB Complexity: **40**
- `main` (@ `gitgalaxy/tools/terabyte_log_scanning/terabyte_log_scanner.py`) -> DB Complexity: **39**
- `handleThemeChange` (@ `site/js/main.js`) -> DB Complexity: **38**
- `generate_build_jcl` (@ `gitgalaxy/tools/cobol_to_cobol/cobol_compiler_forge.py`) -> DB Complexity: **34**
- `generate_rest_controller` (@ `gitgalaxy/tools/cobol_to_java/cobol_to_java_api_contract_forge.py`) -> DB Complexity: **34**
  * *Intent:* """Forges the API endpoints and auto-wires the Service layer."""

## 9. DIRECTORY GROUPS (Top 10 Heaviest Folders)
| Folder Path | Files | Total Mass | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `site/js/core` | 5 | 3721.42 | 42.1% | 12.17% |
| `gitgalaxy/physics` | 6 | 2672.42 | 9.31% | 0.0% |
| `gitgalaxy/core` | 7 | 2665.56 | 9.48% | 1.14% |
| `gitgalaxy` | 6 | 2654.58 | 5.19% | 1.38% |
| `site` | 3 | 2378.22 | 32.44% | 30.59% |
| `site/js` | 2 | 1010.78 | 38.83% | 5.02% |
| `tests/security_auditing` | 16 | 883.12 | 3.43% | 0.0% |
| `tests/core_engine` | 12 | 847.22 | 1.75% | 0.0% |
| `gitgalaxy/standards` | 7 | 839.64 | 6.0% | 7.05% |
| `tests/extraction` | 5 | 709.42 | 3.07% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `gitgalaxy/tools/cobol_to_java/cobol_to_java_service_forge.py` -> **90.1764%** Exposure
- `gitgalaxy/tools/cobol_to_java/cobol_to_java_agent_forge.py` -> **85.6401%** Exposure
- `site/app.py` -> **82.9436%** Exposure
- `site/js/core/materials.js` -> **60.8539%** Exposure
- `gitgalaxy/tools/cobol_to_java/cobol_to_java_build_forge.py` -> **52.7147%** Exposure
### Highest State Flux (Mutation/Volatility)
- `site/tools/search.js` -> **29.2726%** Exposure
- `site/tools/perf_monitor.js` -> **28.8132%** Exposure
- `gitgalaxy/tools/cobol_to_java/cobol_to_java_api_contract_forge.py` -> **28.1434%** Exposure
- `gitgalaxy/tools/cobol_to_java/cobol_to_java_service_forge.py` -> **27.857%** Exposure
- `site/js/core/galaxy-engine.js` -> **27.7646%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/core_engine/test_signal_processor.py` -> **47** Orphaned Functions | **0** Duplicates
- `tests/core_engine/test_detector.py` -> **26** Orphaned Functions | **0** Duplicates
- `tests/security_auditing/test_api_network_map.py` -> **12** Orphaned Functions | **0** Duplicates
- `tests/core_engine/test_aperture.py` -> **11** Orphaned Functions | **0** Duplicates
- `tests/security_auditing/test_binary_anomaly_detector.py` -> **9** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural DNA.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED LENS)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `tests/cobol_mainframe/test_cobol_etl_unpacker.py` -> **0.0073%** Exposure
- `tests/security_auditing/test_neural_auditor.py` -> **0.0001%** Exposure
- `tests/security_auditing/test_security_lens.py` -> **0.0001%** Exposure
### Exploit Generation Surface
- `gitgalaxy/physics/signal_processor.py` -> **100.0%** Exposure
- `tests/cobol_mainframe/test_cobol_agent_task_forge.py` -> **100.0%** Exposure
- `tests/core_engine/test_language_lens.py` -> **100.0%** Exposure
- `tests/core_engine/test_signal_processor.py` -> **100.0%** Exposure
- `tests/security_auditing/test_security_lens.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `gitgalaxy/tools/cobol_to_cobol/cobol_system_limits_reporter.py` -> **100.0%** Exposure
- `tests/cobol_mainframe/test_cobol_agent_task_forge.py` -> **100.0%** Exposure
- `tests/security_auditing/test_security_lens.py` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `tests/security_auditing/test_pii_leak_hunter.py` -> **100.0%** Exposure
- `tests/security_auditing/test_vault_sentinel.py` -> **99.9999%** Exposure
- `tests/core_engine/test_aperture.py` -> **99.7922%** Exposure
- `tests/security_auditing/test_security_lens.py` -> **95.8312%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `23` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures (excluding Civil War). These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `gitgalaxy/tools/cobol_to_cobol/cobol_system_limits_reporter.py` (PYTHON) -> Cumulative Risk: **522.91**
- **Archetype:** `file_cluster_8` (Distance: 8.495 IQR)
- **Mass:** 0.11 | **LOC:** 113 | **CtrlFlow:** 56.8% | **Silo Risk:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Logic Bomb (99.9999%), Verification (67.7318%)
- **Heaviest Functions:** `main` (Impact: 58.5), `scan_system_limits` (Impact: 46.4)

### 2. `gitgalaxy/physics/signal_processor.py` (PYTHON) -> Cumulative Risk: **488.36**
- **Archetype:** `file_cluster_8` (Distance: 8.756 IQR)
- **Mass:** 1107.24 | **LOC:** 2415 | **CtrlFlow:** 77.1% | **Silo Risk:** 100.0%
- **Primary Risk Drivers:** Verification (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Churn (86.14%)
- **Heaviest Functions:** `generate_forensic_report` (Impact: 286.1), `_calc_injection_surface` (Impact: 82.1), `_rank_list` (Impact: 75.4)

### 3. `gitgalaxy/galaxyscope.py` (PYTHON) -> Cumulative Risk: **476.35**
- **Archetype:** `file_cluster_8` (Distance: 9.758 IQR)
- **Mass:** 2364.5 | **LOC:** 2217 | **CtrlFlow:** 67.0% | **Silo Risk:** 100.0%
- **Primary Risk Drivers:** Verification (100.0%), Spec Match (100.0%), Churn (100.0%), Documentation (66.7313%)
- **Heaviest Functions:** `_process_file_worker` (Impact: 501.9), `_calculate_galactic_popularity` (Impact: 401.1), `run_mission` (Impact: 353.7)

### 4. `tests/security_auditing/test_security_lens.py` (PYTHON) -> Cumulative Risk: **471.68**
- **Archetype:** `file_cluster_8` (Distance: 11.095 IQR)
- **Mass:** 40.96 | **LOC:** 210 | **CtrlFlow:** 4.3% | **Silo Risk:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), Secrets Risk (95.8312%)
- **Heaviest Functions:** `test_security_lens_god_mode_coverage_swe` (Impact: 6.8), `test_security_lens_taint_slicer` (Impact: 6.5), `test_security_lens_threat_signatures` (Impact: 3.9)

### 5. `site/js/core/galaxy-engine.js` (JAVASCRIPT) -> Cumulative Risk: **471.36**
- **Archetype:** `file_cluster_17` (Distance: 12.339 IQR)
- **Mass:** 1622.18 | **LOC:** 1255 | **CtrlFlow:** 73.6% | **Silo Risk:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (95.4318%), Cognitive Load (94.3244%), Documentation (87.9753%)
- **Heaviest Functions:** `loadSector` (Impact: 473.3), `animate` (Impact: 223.3), `toggleGlobalWeb` (Impact: 101.1)

### 6. `site/js/core/materials.js` (JAVASCRIPT) -> Cumulative Risk: **462.02**
- **Archetype:** `file_cluster_2` (Distance: 11.948 IQR)
- **Mass:** 185.9 | **LOC:** 158 | **CtrlFlow:** 65.0% | **Silo Risk:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.8669%), Safety Score (71.1765%), Verification (67.7318%)
- **Heaviest Functions:** `resolveMaterialProperties` (Impact: 75.9), `resolveBasalColor` (Impact: 36.9), `refresh` (Impact: 21.8)

### 7. `site/js/main.js` (JAVASCRIPT) -> Cumulative Risk: **457.83**
- **Archetype:** `file_cluster_4` (Distance: 12.113 IQR)
- **Mass:** 1009.78 | **LOC:** 696 | **CtrlFlow:** 69.1% | **Silo Risk:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (95.8503%), Cognitive Load (77.6505%), Verification (77.1818%)
- **Heaviest Functions:** `init` (Impact: 258.3), `loadGalaxyFromRAM` (Impact: 124.4), `handleThemeChange` (Impact: 106.5)

### 8. `site/tools/search.js` (JAVASCRIPT) -> Cumulative Risk: **449.8**
- **Archetype:** `file_cluster_17` (Distance: 11.92 IQR)
- **Mass:** 0.21 | **LOC:** 204 | **CtrlFlow:** 56.4% | **Silo Risk:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (97.0909%), Verification (67.7318%), Safety Score (65.9712%)
- **Heaviest Functions:** `bindEvents` (Impact: 36.7), `onInput` (Impact: 22.4), `render` (Impact: 18.8)

### 9. `site/tools/ally.js` (JAVASCRIPT) -> Cumulative Risk: **420.37**
- **Archetype:** `file_cluster_8` (Distance: 10.821 IQR)
- **Mass:** 0.31 | **LOC:** 262 | **CtrlFlow:** 73.2% | **Silo Risk:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (96.2469%), Verification (67.7318%), Safety Score (54.1935%)
- **Heaviest Functions:** `handleNavigation` (Impact: 74.4), `generateDescription` (Impact: 72.6), `renderTree` (Impact: 50.9)

### 10. `site/tools/perf_monitor.js` (JAVASCRIPT) -> Cumulative Risk: **411.93**
- **Archetype:** `file_cluster_17` (Distance: 11.538 IQR)
- **Mass:** 0.23 | **LOC:** 273 | **CtrlFlow:** 73.5% | **Silo Risk:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (91.1528%), Verification (67.7318%), Safety Score (45.4321%)
- **Heaviest Functions:** `renderStats` (Impact: 40.8), `assessQuality` (Impact: 29.2), `setTheme` (Impact: 26.4)

## 12. VISIBLE MATTER HITLIST (Top 25 Heaviest Files)
> *Note: 'Mass' represents the file's total Structural Magnitude and gravitational pull within the system. It is independent of its Risk Profile. High mass implies high structural importance and centralization.*

### `gitgalaxy/galaxyscope.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.758 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.663 IQR)
- **Top Global Matches:** file_cluster_8: 9.758, file_cluster_13: 10.093, file_cluster_7: 10.294
- **Mass:** 2364.5 | **LOC:** 2217 | **CtrlFlow:** 67.0% | **Silo Risk:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (12.4292%), Tech Debt (8.2833%)
**Top Internal Functions/Classes:**
  * `_process_file_worker` (Impact: 501.9 | O(N^6) | DB: 12)
  * `_calculate_galactic_popularity` (Impact: 401.1 | O(N^6) | DB: 10)
  * `run_mission` (Impact: 353.7 | O(N^6) | DB: 10)
  * `_second_pass_relational` (Impact: 300.7 | O(N^6) | DB: 7)
    * *Intent:* # Evict memory before Pass 2 if "popularity_hits" in meta: del meta["popularity_hits"] def _second_p...
  * `main` (Impact: 184.5 | O(N^6) | DB: 15)
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 361`, `linear: 178`, `args: 28`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_neg: 66`, `flux: 69`, `design_slop_orphans: 1`
* *Architecture:* `io: 11`, `api: 6`, `concurrency: 3`, `import: 53`
* *Defense:* `safety: 45`, `doc: 36`, `test: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` shutil, gitgalaxy.tools.supply_chain_security.supply_chain_firewall, multiprocessing, copy, gitgalaxy.standards.analysis_lens, gitgalaxy.tools.ai_guardrails.dev_agent_firewall, gitgalaxy.security.security_lens, gitgalaxy.recorders.audit_recorder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `site/index.html` (HTML | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.001 IQR)
- **Top Global Matches:** file_cluster_0: 11.001, file_cluster_17: 11.117, file_cluster_8: 11.333
- **Mass:** 2099.94 | **LOC:** 1710 | **CtrlFlow:** 52.3% | **Silo Risk:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (88.0635%), Tech Debt (8.8137%)
**Top Internal Functions/Classes:**
  * `renderSearchResults` (Impact: 1691.3 | O(N^6) | DB: 60)
  * `toggleGlobalNetwork` (Impact: 43.7 | O(N^6) | DB: 1)
  * `toggleLabels` (Impact: 37.6 | O(N^5) | DB: 1)
  * `interceptLog` (Impact: 36.9 | O(N^6) | DB: 2)
  * `hideHUDUI` (Impact: 22.6 | O(N^4))
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 319`, `linear: 291`, `args: 103`, `func_start: 41`
* *Risk/State:* `safety_neg: 42`, `danger: 14`, `flux: 108`, `design_slop_orphans: 1`
* *Architecture:* `io: 15`, `api: 63`, `concurrency: 12`, `import: 1`
* *Defense:* `safety: 61`, `doc: 1`, `test: 1`, `freeze_hits: 133`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` 7f9d03714fb4d30ac0cc541eabd2b415.min.js, tween.umd.js, colors.js, poster.js, styles.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `site/js/core/galaxy-engine.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.339 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.166 IQR)
- **Top Global Matches:** file_cluster_17: 12.339, file_cluster_8: 12.352, file_cluster_4: 12.36
- **Mass:** 1622.18 | **LOC:** 1255 | **CtrlFlow:** 73.6% | **Silo Risk:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (94.3244%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loadSector` (Impact: 473.3 | O(N^6) | DB: 40)
  * `animate` (Impact: 223.3 | O(2^N) | DB: 44)
  * `toggleGlobalWeb` (Impact: 101.1 | O(N^5) | DB: 20)
  * `setupEvents` (Impact: 96.7 | O(N^4) | DB: 56)
  * `showHUD` (Impact: 65.9 | O(N^6) | DB: 5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 12 instances
* *Amplified Race Conditions:* 5 instances
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `linear: 75`, `args: 52`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_neg: 29`, `flux: 354`
* *Architecture:* `io: 1`, `api: 6`, `concurrency: 30`, `import: 6`
* *Defense:* `safety: 48`, `doc: 1`, `freeze_hits: 208`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` three, tsl, webgpu, phase-6-shaders.js, BloomNode.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `site/js/core/metavisualizer.html` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 10.011 IQR)
- **Top Global Matches:** file_cluster_17: 10.011, file_cluster_0: 10.31, file_cluster_8: 10.419
- **Mass:** 1473.34 | **LOC:** 585 | **CtrlFlow:** 46.0% | **Silo Risk:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (26.4958%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `calculateFrequency` (Impact: 1286.2 | O(2^N) | DB: 17)
  * `findIdx` (Impact: 35.1 | O(N^4) | DB: 1)
  * `calculateHistogram` (Impact: 31.1 | O(N^4) | DB: 2)
    * *Intent:* /** * Histogram Engine with Galactic (Log) Support (Rule 3.A) */
  * `fmt` (Impact: 24.5 | O(2^N))
  * `fmt` (Impact: 24.5 | O(2^N))
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `linear: 155`, `args: 54`, `func_start: 14`, `class_start: 11`
* *Risk/State:* `safety_neg: 23`, `flux: 26`
* *Architecture:* `io: 1`, `api: 14`
* *Defense:* `safety: 28`, `doc: 5`, `freeze_hits: 72`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` output.css
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/physics/spectral_auditor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.327 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.254 IQR)
- **Top Global Matches:** file_cluster_8: 9.327, file_cluster_16: 9.656, file_cluster_13: 9.826
- **Mass:** 1135.36 | **LOC:** 532 | **CtrlFlow:** 69.7% | **Silo Risk:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (18.7869%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `audit` (Impact: 1026.2 | O(2^N) | DB: 22)
  * `_is_necrotic` (Impact: 26.1 | O(N^4))
    * *Intent:* """Determines if a file is a Polyglot where the primary language is < 80% of the mass."""
  * `_is_threat` (Impact: 25.9 | O(N^4))
    * *Intent:* """ telemetry = star.get("telemetry", {}) return { "path": star.get("path", "unknown"), "reason": re...
  * `_is_highly_blended` (Impact: 20.7 | O(N^4))
    * *Intent:* # Format it as Inert Dark Matter to save memory and ensure schema consistency relegated_count += 1 e...
  * `_format_for_singularity` (Impact: 5.2 | O(N^3))
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `linear: 37`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_neg: 26`, `flux: 20`
* *Architecture:* `io: 2`, `api: 3`, `import: 5`
* *Defense:* `safety: 9`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` statistics, typing, os, math, logging
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/physics/signal_processor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.756 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.679 IQR)
- **Top Global Matches:** file_cluster_8: 8.756, file_cluster_16: 9.312, file_cluster_7: 9.352
- **Mass:** 1107.24 | **LOC:** 2415 | **CtrlFlow:** 77.1% | **Silo Risk:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (14.3775%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generate_forensic_report` (Impact: 286.1 | O(N^6) | DB: 3)
    * *Intent:* # 2. The Amplifiers (Network & Data Gravity) if db_complex > 0: func_threat *= 1.0 + (db_complex * 0...
  * `_calc_injection_surface` (Impact: 82.1 | O(N^3))
    * *Intent:* # If the LHS Slicer confirmed data crossed from I/O to Danger, risk is absolute. taint_confirmed = e...
  * `_rank_list` (Impact: 75.4 | O(N^5))
  * `_calc_safety` (Impact: 65.6 | O(N^4))
    * *Intent:* # ---> THE GOD FUNCTION PENALTY <--- # If complexity is heavily skewed into a single massive functio...
  * `_calc_tech_debt` (Impact: 65.3 | O(N^3))
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 451`, `linear: 134`, `args: 44`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_neg: 38`, `flux: 45`
* *Architecture:* `io: 1`, `api: 11`, `concurrency: 2`, `import: 8`
* *Defense:* `safety: 70`, `doc: 50`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` statistics, typing, re, os, gitgalaxy.standards, math, logging
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `site/js/main.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.113 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.687 IQR)
- **Top Global Matches:** file_cluster_4: 12.113, file_cluster_17: 12.14, file_cluster_8: 12.48
- **Mass:** 1009.78 | **LOC:** 696 | **CtrlFlow:** 69.1% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (77.6505%), Tech Debt (10.0358%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 258.3 | O(N^6) | DB: 48)
  * `loadGalaxyFromRAM` (Impact: 124.4 | O(N^6) | DB: 12)
  * `handleThemeChange` (Impact: 106.5 | O(N^4) | DB: 38)
  * `fetchGalaxyData` (Impact: 67.6 | O(N^4) | DB: 9)
  * `syncHUDWithSelection` (Impact: 51.4 | O(N^4) | DB: 10)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 9 instances
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `linear: 67`, `args: 49`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_neg: 20`, `danger: 3`, `flux: 147`, `design_slop_orphans: 1`
* *Architecture:* `io: 2`, `concurrency: 59`, `import: 3`
* *Defense:* `safety: 45`, `doc: 8`, `freeze_hits: 58`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` phase-6-shaders.js, galaxy-engine.js, data-parser.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/core/prism.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.785 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.018 IQR)
- **Top Global Matches:** file_cluster_8: 9.785, file_cluster_16: 9.839, file_cluster_7: 10.156
- **Mass:** 811.02 | **LOC:** 574 | **CtrlFlow:** 61.3% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (13.2748%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_find_balanced_end` (Impact: 307.7 | O(N^6) | DB: 8)
  * `_calibrate_matrix` (Impact: 155.5 | O(N^6))
    * *Intent:* # Hardened Python Post-Processing if lang_id in ("python", "micropython", "ruby"): code, extra_lits ...
  * `_partition_segments` (Impact: 129.5 | O(N^6) | DB: 4)
  * `refract` (Impact: 94.6 | O(N^5) | DB: 2)
  * `_refract_segment` (Impact: 63.7 | O(N^4) | DB: 3)
    * *Intent:* # 3. Derive the documentation lines by subtracting code from the active total. doc_loc = max(0, tota...
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `linear: 65`, `args: 19`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_neg: 17`, `flux: 32`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* `safety: 4`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` gitgalaxy.standards.language_standards, logging, typing, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/core/network_risk_sensor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.209 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.799 IQR)
- **Top Global Matches:** file_cluster_8: 9.209, file_cluster_13: 9.665, file_cluster_16: 9.812
- **Mass:** 643.2 | **LOC:** 328 | **CtrlFlow:** 75.9% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (17.3864%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `map_ecosystem` (Impact: 466.0 | O(N^6) | DB: 1)
  * `_fallback_map_ecosystem` (Impact: 157.6 | O(N^6))
  * `__init__` (Impact: 7.9 | O(N^2) | DB: 2)
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `linear: 28`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_neg: 25`, `flux: 3`
* *Architecture:* `io: 1`, `api: 4`, `import: 7`
* *Defense:* `safety: 20`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` networkx, typing, pathlib, networkx.algorithms, math, logging, gitgalaxy.standards.analysis_lens
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/core/guidestar_lens.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.944 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.749 IQR)
- **Top Global Matches:** file_cluster_8: 8.944, file_cluster_13: 9.375, file_cluster_7: 9.384
- **Mass:** 586.68 | **LOC:** 494 | **CtrlFlow:** 61.6% | **Silo Risk:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (7.4024%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_parse_toml_style_manifest` (Impact: 130.6 | O(N^6) | DB: 6)
    * *Intent:* """Simple regex-based TOML parser for script/entry points."""
  * `get_intent_status` (Impact: 73.8 | O(N^5))
  * `_survey_knowledge_anchors` (Impact: 69.3 | O(N^6) | DB: 3)
    * *Intent:* # ============================================================================== # KNOWLEDGE ANCHORS...
  * `_parse_package_json` (Impact: 56.8 | O(N^6) | DB: 3)
    * *Intent:* # We inject a synthetic prior so the downstream pipeline knows this is an AI repo def _parse_package...
  * `_survey_gitignore` (Impact: 50.5 | O(N^6) | DB: 3)
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `linear: 53`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_neg: 17`, `flux: 4`
* *Architecture:* `io: 8`, `api: 6`, `import: 8`
* *Defense:* `safety: 16`, `doc: 32`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` json, typing, fnmatch, re, pathlib, os, logging, gitgalaxy.standards.gitgalaxy_config
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/core/detector.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.428 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.159 IQR)
- **Top Global Matches:** file_cluster_8: 8.428, file_cluster_16: 8.921, file_cluster_7: 8.992
- **Mass:** 586.36 | **LOC:** 2443 | **CtrlFlow:** 73.8% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (19.3325%), Tech Debt (7.9908%)
**Top Internal Functions/Classes:**
  * `map_repository` (Impact: 189.7 | O(N^6) | DB: 7)
    * *Intent:* # Removed the p_scalar multiplier. # Micro-placement will now be tight, and macro WebGPU scaling is ...
  * `_classify_function` (Impact: 124.5 | O(N^4))
    * *Intent:* # ---> THE C++ SCOPE SHIELD <--- # Hide the double-colon so the single-colon guillotine doesn't see ...
  * `_extract_name` (Impact: 96.3 | O(N^5))
  * `__init__` (Impact: 11.5 | O(N^3) | DB: 9)
    * *Intent:* # ------------------------------------------------------------------------------ # THE CARTOGRAPHER ...
  * `_hash_jitter` (Impact: 8.4 | O(N^3))
    * *Intent:* # Base expansion multipliers self.MACRO_STEP_FACTOR = 1.5 # Inter-galaxy step multiplier (Center-to-...
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 532`, `linear: 189`, `args: 37`, `func_start: 32`, `class_start: 5`
* *Risk/State:* `safety_neg: 59`, `flux: 61`, `graveyard: 2`, `planned_debt: 1`
* *Architecture:* `api: 18`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 46`, `doc: 68`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` time, hashlib, typing, re, bisect, math, gitgalaxy.standards.language_standards, logging...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/security/security_auditor.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.015 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.938 IQR)
- **Top Global Matches:** file_cluster_8: 9.015, file_cluster_13: 9.479, file_cluster_7: 9.619
- **Mass:** 492.8 | **LOC:** 377 | **CtrlFlow:** 66.0% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (12.4191%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_resolve_dependency_graph` (Impact: 162.7 | O(N^6) | DB: 3)
  * `audit_galaxy` (Impact: 116.0 | O(N^6))
  * `__init__` (Impact: 100.3 | O(N^6) | DB: 8)
  * `_construct_feature_matrix` (Impact: 90.2 | O(N^6) | DB: 2)
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `linear: 35`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_neg: 9`, `flux: 13`
* *Architecture:* `io: 1`, `api: 5`, `import: 8`
* *Defense:* `safety: 12`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` numpy, networkx, pathlib, xgboost, pandas, logging, collections, gitgalaxy.standards.analysis_lens
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/recorders/llm_recorder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.865 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.871 IQR)
- **Top Global Matches:** file_cluster_8: 9.865, file_cluster_16: 10.373, file_cluster_7: 10.377
- **Mass:** 376.22 | **LOC:** 1543 | **CtrlFlow:** 87.7% | **Silo Risk:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (48.7905%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 11.0 | O(N^3) | DB: 4)
  * `_parse_threat_score` (Impact: 7.3 | O(N^3))
  * `generate_artifacts` (Impact: 1.9 | O(N^2))
    * *Intent:* """Safely extracts and converts the AI threat score string to a float."""
  * `_build_markdown` (Impact: 1.9 | O(N^2))
  * `_generate_sqlite_graph` (Impact: 1.9 | O(N^2))
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 355`, `linear: 50`, `args: 32`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_neg: 30`, `flux: 312`
* *Architecture:* `io: 2`, `api: 4`, `concurrency: 12`, `import: 9`
* *Defense:* `safety: 15`, `doc: 26`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` statistics, json, typing, pathlib, gitgalaxy.standards, heapq, logging, collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `site/js/core/data-parser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.962 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.815 IQR)
- **Top Global Matches:** file_cluster_8: 9.962, file_cluster_7: 10.484, file_cluster_17: 10.522
- **Mass:** 376.04 | **LOC:** 264 | **CtrlFlow:** 77.8% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (42.9731%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `transformEntity` (Impact: 123.0 | O(N^6) | DB: 4)
  * `parse` (Impact: 83.7 | O(N^5) | DB: 16)
  * `addToGroup` (Impact: 79.8 | O(N^4) | DB: 19)
  * `transformSatellite` (Impact: 20.2 | O(N^4) | DB: 8)
  * `createEmptyGroups` (Impact: 4.2 | O(N^4) | DB: 1)
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `linear: 16`, `args: 12`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_neg: 2`, `flux: 48`
* *Architecture:* `io: 1`, `api: 3`
* *Defense:* `safety: 2`, `doc: 5`, `freeze_hits: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/standards/language_standards.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.515 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.244 IQR)
- **Top Global Matches:** file_cluster_8: 6.515, file_cluster_1: 7.362, file_cluster_7: 7.402
- **Mass:** 322.06 | **LOC:** 10239 | **CtrlFlow:** 76.9% | **Silo Risk:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.1626%), Tech Debt (41.3419%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *Amplified Race Conditions:* 3 instances
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 1907`, `linear: 574`
* *Risk/State:* `safety_neg: 34`, `danger: 19`, `flux: 47`, `graveyard: 9`, `planned_debt: 64`, `fragile_debt: 78`
* *Architecture:* `io: 32`, `api: 19`, `concurrency: 102`, `import: 1`
* *Defense:* `safety: 154`, `doc: 33`, `test: 60`, `sync_locks: 82`, `freeze_hits: 43`, `cleanup: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/standards/language_lens.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.326 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.071 IQR)
- **Top Global Matches:** file_cluster_8: 7.326, file_cluster_16: 7.901, file_cluster_7: 8.097
- **Mass:** 311.76 | **LOC:** 1107 | **CtrlFlow:** 73.2% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (16.0865%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_detect_hybrids` (Impact: 93.7 | O(N^6) | DB: 2)
  * `_tier_2_fingerprint_check` (Impact: 78.3 | O(N^6))
    * *Intent:* # This forces the pipeline to fall back to Tier 1.5 Ecosystem Gravity # or Tier 3 Spectral Verificat...
  * `_calibrate_lookup_maps` (Impact: 73.7 | O(N^6))
  * `_tier_1_metadata_lock` (Impact: 16.6 | O(N^3))
  * `inspect` (Impact: 1.9 | O(N^2))
    * *Intent:* """Legacy Support Gateway."""
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `linear: 98`, `args: 17`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_neg: 30`, `flux: 17`
* *Architecture:* `io: 2`, `api: 6`, `import: 9`
* *Defense:* `safety: 13`, `doc: 14`, `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` time, typing, re, pathlib, math, gitgalaxy.standards.language_standards, logging, gitgalaxy.standards.gitgalaxy_config
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `site/app.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.283 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.254 IQR)
- **Top Global Matches:** file_cluster_8: 8.283, file_cluster_13: 8.808, file_cluster_0: 8.93
- **Mass:** 277.28 | **LOC:** 409 | **CtrlFlow:** 42.7% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (9.2512%), Tech Debt (82.9436%)
**Top Internal Functions/Classes:**
  * `stripe_webhook` (Impact: 134.3 | O(N^6) | DB: 3)
  * `create_checkout_session` (Impact: 76.5 | O(N^6) | DB: 3)
    * *Intent:* # --- 6. COMMERCE ENDPOINTS --- @app.route("/api/create-checkout-session", methods=["POST"]) def cre...
  * `capture_enterprise_lead` (Impact: 28.1 | O(N^5))
  * `list_galaxies` (Impact: 11.0 | O(N^3) | DB: 6)
  * `get_printify_session` (Impact: 4.3 | O(N^3) | DB: 4)
    * *Intent:* # --- 4. ROBUST API SESSION HELPER --- """ Creates an HTTP session that automatically retries failed...
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `linear: 51`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_neg: 3`, `flux: 1`, `planned_debt: 1`, `design_slop_orphans: 7`
* *Architecture:* `io: 14`, `api: 9`, `import: 11`
* *Defense:* `safety: 13`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dotenv, base64, urllib3.util.retry, json, requests.adapters, requests, os, stripe...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/physics/chronometer.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.89 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.811 IQR)
- **Top Global Matches:** file_cluster_8: 9.89, file_cluster_13: 10.071, file_cluster_16: 10.265
- **Mass:** 275.36 | **LOC:** 394 | **CtrlFlow:** 60.8% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (9.7411%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_survey_boundaries` (Impact: 112.5 | O(N^6) | DB: 12)
    * *Intent:* # Step C: Populate Churn and MTime Maps if self.is_resilient: self._ignite_hybrid_log_scan() else: s...
  * `_load_ignored_revs` (Impact: 43.3 | O(N^6) | DB: 3)
  * `_calibrate_temporal_field` (Impact: 23.1 | O(N^4) | DB: 1)
    * *Intent:* # --- INTERNAL STATE (The Sensor Cache) --- self.entropy_map: Dict[str, int] = {} self.mtime_map: Di...
  * `_survey_filesystem_mtimes` (Impact: 21.3 | O(N^5) | DB: 6)
  * `_ignite_hybrid_log_scan` (Impact: 20.5 | O(N^4))
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `linear: 38`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_neg: 13`, `danger: 1`, `flux: 12`
* *Architecture:* `io: 8`, `api: 4`, `import: 7`
* *Defense:* `safety: 19`, `doc: 18`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` time, typing, pathlib, os, subprocess, gitgalaxy.standards, logging
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/core_engine/test_signal_processor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.783 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.137 IQR)
- **Top Global Matches:** file_cluster_8: 10.783, file_cluster_7: 11.099, file_cluster_1: 11.304
- **Mass:** 262.44 | **LOC:** 1144 | **CtrlFlow:** 7.9% | **Silo Risk:** 50.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (1.4862%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create_synthetic_star` (Impact: 23.9 | O(N^3) | DB: 1)
  * `test_signal_processor_report_fallback` (Impact: 8.6 | O(N^2))
    * *Intent:* # Should execute smoothly without raising a KeyError, TypeError, or IndexError report = physics_engi...
  * `test_signal_processor_zero_division_shie` (Impact: 8.4 | O(N^2))
  * `test_signal_processor_math_overflow_shie` (Impact: 8.3 | O(N^2))
    * *Intent:* # ============================================================================== # TEST 10: GALAXY A...
  * `test_signal_processor_structural_metrics` (Impact: 6.2 | O(N^2))
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `linear: 152`, `args: 49`, `func_start: 49`
* *Risk/State:* `safety_neg: 2`, `flux: 5`, `planned_debt: 1`, `fragile_debt: 1`, `design_slop_orphans: 47`
* *Architecture:* `api: 49`, `import: 3`
* *Defense:* `safety: 99`, `doc: 98`, `test: 142`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, gitgalaxy.physics.signal_processor
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/core_engine/test_detector.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.241 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.561 IQR)
- **Top Global Matches:** file_cluster_8: 11.241, file_cluster_7: 11.558, file_cluster_13: 11.589
- **Mass:** 219.3 | **LOC:** 705 | **CtrlFlow:** 21.0% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (1.9618%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_cartographer_sectorization_and_mono` (Impact: 27.2 | O(N^2))
    * *Intent:* # CARTOGRAPHER: 3D SPATIAL GEOMETRY & MAPPING # ====================================================...
  * `test_detector_catastrophic_fallbacks` (Impact: 15.2 | O(N^3))
    * *Intent:* # ============================================================================== # TEST 11: ADVANCED...
  * `test_detector_terminator_cleaving` (Impact: 13.7 | O(N^2))
  * `test_detector_orphan_and_duplicate_logic` (Impact: 11.5 | O(N^2))
  * `test_detector_mode_d_ruby_inline_modifie` (Impact: 11.5 | O(N^2))
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `linear: 177`, `args: 48`, `func_start: 27`
* *Risk/State:* `safety_neg: 2`, `flux: 2`, `graveyard: 1`, `design_slop_orphans: 26`
* *Architecture:* `io: 2`, `api: 27`, `import: 6`
* *Defense:* `safety: 82`, `doc: 56`, `test: 121`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, unittest.mock, spawning, gitgalaxy.core.detector, artificially, math, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/extraction/test_function_extraction_strict.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.753 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.058 IQR)
- **Top Global Matches:** file_cluster_8: 6.753, file_cluster_7: 7.708, file_cluster_1: 7.845
- **Mass:** 212.96 | **LOC:** 540 | **CtrlFlow:** 48.4% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.0762%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_positive_function_extraction` (Impact: 79.4 | O(N^5))
    * *Intent:* """ Proves that valid function signatures are caught, and the regex isolates EXACTLY the function na...
  * `test_pathological_function_extraction` (Impact: 74.0 | O(N^5))
  * `test_negative_function_extraction` (Impact: 35.4 | O(N^4))
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `linear: 49`, `args: 8`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `design_slop_orphans: 3`
* *Architecture:* `io: 1`, `api: 4`, `concurrency: 11`, `import: 3`
* *Defense:* `safety: 13`, `doc: 6`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, gitgalaxy.standards.language_standards, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/cobol_refractor_controller.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.764 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.151 IQR)
- **Top Global Matches:** file_cluster_8: 8.764, file_cluster_13: 8.98, file_cluster_7: 9.329
- **Mass:** 210.96 | **LOC:** 410 | **CtrlFlow:** 50.6% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (7.6668%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_init_sql_schema` (Impact: 165.8 | O(N^4) | DB: 12)
  * `calibrate_ir_medium` (Impact: 18.9 | O(N^2))
    * *Intent:* # ============================================================================== # THE SCALE SENSOR ...
  * `__init__` (Impact: 8.4 | O(N^3) | DB: 6)
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `linear: 39`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_neg: 3`, `flux: 9`
* *Architecture:* `io: 4`, `api: 4`, `import: 16`
* *Defense:* `safety: 4`, `doc: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` gitgalaxy.tools.cobol_to_cobol.cobol_system_limits_reporter, json, argparse, gitgalaxy.tools.cobol_to_cobol.cobol_lexical_patcher, gitgalaxy.tools.cobol_to_cobol.cobol_graveyard_finder, gitgalaxy.tools.cobol_to_cobol.cobol_jcl_auditor, gitgalaxy.tools.cobol_to_cobol.cobol_agent_task_forge, datetime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/extraction/test_class_extraction_strict.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.134 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.567 IQR)
- **Top Global Matches:** file_cluster_8: 7.134, file_cluster_7: 8.02, file_cluster_1: 8.193
- **Mass:** 199.8 | **LOC:** 364 | **CtrlFlow:** 33.3% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.2939%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_positive_class_extraction` (Impact: 79.2 | O(N^5))
    * *Intent:* """ Proves that valid class/entity signatures are caught, and the regex isolates EXACTLY the entity ...
  * `test_pathological_class_extraction` (Impact: 74.0 | O(N^5))
  * `test_negative_class_extraction` (Impact: 35.4 | O(N^4))
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `linear: 76`, `args: 5`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `flux: 1`, `design_slop_orphans: 3`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 11`, `doc: 6`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, gitgalaxy.standards.language_standards, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/extraction/test_dependency_extraction_strict.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.332 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.841 IQR)
- **Top Global Matches:** file_cluster_8: 7.332, file_cluster_7: 8.105, file_cluster_13: 8.3
- **Mass:** 193.02 | **LOC:** 438 | **CtrlFlow:** 25.4% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.0231%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_positive_dependency_extraction` (Impact: 74.0 | O(N^5))
    * *Intent:* """ Proves that valid import signatures are caught, and the regex isolates EXACTLY the module/file p...
  * `test_pathological_dependency_extraction` (Impact: 68.7 | O(N^5))
  * `test_negative_dependency_extraction` (Impact: 35.4 | O(N^4))
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `linear: 94`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_neg: 1`, `flux: 3`, `graveyard: 3`, `design_slop_orphans: 3`
* *Architecture:* `io: 2`, `api: 4`, `import: 3`
* *Defense:* `safety: 7`, `doc: 6`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, gitgalaxy.standards.language_standards, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `site/js/core/materials.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.948 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.355 IQR)
- **Top Global Matches:** file_cluster_2: 11.948, file_cluster_8: 12.11, file_cluster_17: 12.11
- **Mass:** 185.9 | **LOC:** 158 | **CtrlFlow:** 65.0% | **Silo Risk:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (36.0853%), Tech Debt (60.8539%)
**Top Internal Functions/Classes:**
  * `resolveMaterialProperties` (Impact: 75.9 | O(N^5) | DB: 8)
  * `resolveBasalColor` (Impact: 36.9 | O(N^3) | DB: 3)
    * *Intent:* /** * GitGalaxy * Copyright (c) 2026 Joe Esquibel * * This source code is licensed under the PolyFor...
  * `refresh` (Impact: 21.8 | O(N^3) | DB: 7)
  * `get` (Impact: 19.2 | O(N^3) | DB: 7)
  * `constructor` (Impact: 2.4 | O(N^2) | DB: 3)
    * *Intent:* /** * GitGalaxy * Copyright (c) 2026 Joe Esquibel *
**Structural DNA (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `linear: 14`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_neg: 7`, `flux: 28`, `design_slop_orphans: 2`
* *Architecture:* None
* *Defense:* `safety: 8`, `doc: 6`, `freeze_hits: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Blast Radius (PageRank):` 6.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. BIAXIAL ANOMALY & ARCHITECTURAL DRIFT
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Refactoring Targets for: file_cluster_0
- `tests/core_engine/test_chronometer.py` (PYTHON) | Mass: 76.82 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top DNA Signatures: indent_spaces: 78, test: 39, linear: 38, safety: 19
- `tests/security_auditing/test_binary_anomaly_detector.py` (PYTHON) | Mass: 122.92 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top DNA Signatures: indent_spaces: 127, test: 48, linear: 43, branch: 16
- `site/index.html` (HTML) | Mass: 2099.94 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_17`
  * Top DNA Signatures: indent_spaces: 1364, branch: 319, linear: 291, globals: 276

### Refactoring Targets for: file_cluster_13
- `tests/cobol_mainframe/test_cobol_lexical_patcher.py` (PYTHON) | Mass: 14.38 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top DNA Signatures: indent_spaces: 27, linear: 24, test: 21, safety: 15
- `gitgalaxy/tools/cobol_to_java/cobol_to_java_api_contract_forge.py` (PYTHON) | Mass: 0.14 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top DNA Signatures: indent_spaces: 95, flux: 34, branch: 23, linear: 22
- `tests/tools_recorders/test_golden_forge.py` (PYTHON) | Mass: 9.58 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top DNA Signatures: indent_spaces: 41, linear: 27, decorators: 15, import: 12
- `tests/core_engine/test_language_standards_strict.py` (PYTHON) | Mass: 49.18 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top DNA Signatures: indent_spaces: 52, linear: 29, doc: 22, sec_danger: 20
- `tests/security_auditing/test_redos_poison.py` (PYTHON) | Mass: 115.54 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_8`
  * Top DNA Signatures: indent_spaces: 59, branch: 20, linear: 18, import: 8

### Refactoring Targets for: file_cluster_17
- `site/tools/perf_monitor.js` (JAVASCRIPT) | Mass: 0.23 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top DNA Signatures: indent_spaces: 159, flux: 69, branch: 36, globals: 23
- `site/js/core/galaxy-engine.js` (JAVASCRIPT) | Mass: 1622.18 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top DNA Signatures: indent_spaces: 844, flux: 354, branch: 209, freeze_hits: 208
- `site/js/core/metavisualizer.html` (HTML) | Mass: 1473.34 | Delta: **0.299 IQR** | Secondary Pull: `file_cluster_0`
  * Top DNA Signatures: indent_spaces: 492, linear: 155, branch: 132, freeze_hits: 72
- `site/tools/search.js` (JAVASCRIPT) | Mass: 0.21 | Delta: **0.337 IQR** | Secondary Pull: `file_cluster_8`
  * Top DNA Signatures: indent_spaces: 136, flux: 67, branch: 31, linear: 24

### Refactoring Targets for: file_cluster_2
- `site/js/core/materials.js` (JAVASCRIPT) | Mass: 185.9 | Delta: **0.162 IQR** | Secondary Pull: `file_cluster_8`
  * Top DNA Signatures: indent_spaces: 82, flux: 28, branch: 26, linear: 14

### Refactoring Targets for: file_cluster_4
- `site/js/main.js` (JAVASCRIPT) | Mass: 1009.78 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_17`
  * Top DNA Signatures: indent_spaces: 483, branch: 150, flux: 147, linear: 67
- `site/tools/poster.js` (JAVASCRIPT) | Mass: 1.2 | Delta: **0.201 IQR** | Secondary Pull: `file_cluster_17`
  * Top DNA Signatures: indent_spaces: 546, branch: 133, freeze_hits: 117, concurrency: 107

### Refactoring Targets for: file_cluster_8
- `gitgalaxy/tools/ai_guardrails/ai_appsec_sensor.py` (PYTHON) | Mass: 0.13 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top DNA Signatures: indent_spaces: 39, branch: 19, linear: 7, api: 4
- `tests/security_auditing/test_network_risk_sensor.py` (PYTHON) | Mass: 59.44 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top DNA Signatures: indent_spaces: 73, test: 33, linear: 31, branch: 17
- `tests/cobol_mainframe/test_cobol_compiler_forge.py` (PYTHON) | Mass: 21.7 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top DNA Signatures: indent_spaces: 42, linear: 25, test: 20, safety: 15
- `gitgalaxy/tools/cobol_to_cobol/cobol_compiler_forge.py` (PYTHON) | Mass: 0.3 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top DNA Signatures: indent_spaces: 122, flux: 39, branch: 27, linear: 20
- `gitgalaxy/core/prism.py` (PYTHON) | Mass: 811.02 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_16`
  * Top DNA Signatures: indent_spaces: 334, branch: 103, linear: 65, flux: 32

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Silos)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high silo risk (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `gitgalaxy/galaxyscope.py` -> **squid-protocol** (100.0% isolated ownership) | Mass: 2364.5
- `gitgalaxy/physics/signal_processor.py` -> **squid-protocol** (100.0% isolated ownership) | Mass: 1107.24
- `gitgalaxy/core/guidestar_lens.py` -> **squid-protocol** (100.0% isolated ownership) | Mass: 586.68
- `gitgalaxy/recorders/llm_recorder.py` -> **squid-protocol** (100.0% isolated ownership) | Mass: 376.22
- `gitgalaxy/standards/language_standards.py` -> **squid-protocol** (100.0% isolated ownership) | Mass: 322.06

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Physics)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Blind Bottlenecks (Blast Radius * Doc Risk)
These are 'God Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `gitgalaxy/core/guidestar_lens.py` -> **Severity: 666.7** (Blast Radius: 6.667 * Doc Risk: 100.0%)
- `gitgalaxy/tools/cobol_to_cobol/cobol_compiler_forge.py` -> **Severity: 666.7** (Blast Radius: 6.667 * Doc Risk: 100.0%)
- `gitgalaxy/tools/network_auditing/full_api_network_map.py` -> **Severity: 666.7** (Blast Radius: 6.667 * Doc Risk: 100.0%)
- `site/js/core/data-parser.js` -> **Severity: 665.913** (Blast Radius: 6.667 * Doc Risk: 99.882%)
- `gitgalaxy/physics/neural_auditor.py` -> **Severity: 661.229** (Blast Radius: 6.667 * Doc Risk: 99.1794%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or constellations with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive 'God Nodes', or mitigate extreme risk exposures to stabilize the system's architecture.
