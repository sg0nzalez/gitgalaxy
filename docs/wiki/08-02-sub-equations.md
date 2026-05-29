# 2.2.B. Sub-Equations (The Scanner Variables)

> **Purpose: Defining the Raw Inputs of the Knowledge Graph**
>
> To ensure the risk and complexity equations are actionable, the engine relies on a standardized array of regex variables extracted from the source text. The GitGalaxy Analysis Engine operates in a strict 5-Phase sequence to map these heuristics. 
> 
> *(Note: The scanner appends a `_hits` suffix to all output variables. For example, the `branch` regex rule outputs its final count as `branch_hits`)*.

## Phase 1: Architectural Geometry (Structure)
These variables define the raw structural shape and volume of the file within the knowledge graph.

| Variable | Structural Definition |
| :--- | :--- |
| `branch_hits` | Logic forcing execution to split or jump (conditionals, loops, short-circuits). Excludes unrecoverable exceptions. |
| `args_hits` | Functional signatures defining the parameter mass and data inputs. Used to calculate coupling weight. |
| `linear_hits` | Declarative pathing defining the file's architectural skeleton (imports, returns, package declarations). |
| `func_start_hits` | The primary syntactic anchor identifying the beginning of executable intent (named functions, methods, subroutines). |
| `class_start_hits` | Defines the boundaries of Object-Oriented entities or structural data definitions (classes, interfaces, structs). |

## Phase 2: Risk & Exposure Heuristics (Integrity)
These variables track defensive programming versus reckless execution to identify risk exposures.

| Variable | Structural Definition |
| :--- | :--- |
| `safety_hits` | Explicit signals of safe boundary management, error handling, and strict equality (e.g., `try/catch`). |
| `safety_neg_hits` | Active bypasses of type systems, error suppression, or unsafe pointer usage (e.g., `any`, `unsafe`). |
| `danger_hits` | Catastrophic execution risks, un-sanitized process triggers, or dynamic execution (e.g., `eval`, `process.exit`). |
| `io_hits` | Interaction with external systems (Disk, Network, Database). |
| `api_hits` | Identification of code surface area exposed to external scopes (public interfaces, exported members). |
| `flux_hits` | Direct mutation of state, memory reassignments, and side-effect triggers. |
| `graveyard_hits` | Commented-out execution logic indicating dead features or abandoned code. |
| `doc_hits` | Signals of structured metadata/docs intended for humans and parsers (e.g., JSDoc). |
| `test_hits` | Triggers indicating internal verification or testing framework proximity (e.g., `describe`, `assert`). |

## Phase 3: Specialized Sensors (Architecture & Domain)
These variables detect the specific paradigm and domain behavior of the code.

| Variable | Structural Definition |
| :--- | :--- |
| `concurrency_hits` | Asynchronous primitives, coroutines, and thread orchestration. |
| `ui_framework_hits` | Density of visual layout primitives or framework-specific UI bindings (e.g., JSX components). |
| `closures_hits` | Anonymous scopes, lambda callbacks, and inline delegates. |
| `globals_hits` | Access to global registries, environment variables, or singleton states. |
| `decorators_hits` | Architectural annotations modifying block behavior or tagging metadata. |
| `generics_hits` | Signals of generic contracts, templates, and type parameterization. |
| `comprehensions_hits` | High-density logic patterns (mapping, filtering, list-comps) acting as inline data pipelines. |
| `scientific_hits` | Math libraries, tensor operations, and linear algebra primitives. |
| `heat_triggers_hits` | Metaprogramming, reflection, or dynamic property binding that increases cognitive load. |
| `import_hits` | Dependency resolution, module loading, and file inclusion. |
| `ownership_hits` | Identifying the architect within comments (e.g., `@author`, `Maintainer:`). |

## Phase 4: Extracted Sub-Equations (Specialized Systems)
These variables capture highly specific execution contexts and known technical debt.

| Variable | Structural Definition |
| :--- | :--- |
| `planned_debt_hits` | Future engineering work that doesn't break execution (e.g., `TODO`, `WIP`). |
| `fragile_debt_hits` | Explicit admissions of hacks or 'ugly' code (e.g., `FIXME`, `HACK`). |
| `private_info_hits` | Hardcoded credentials or secrets tied directly to assignment operators. |
| `spec_exposure_hits` | Documentation tracking code back to architecture specs, RFCs, or formal audits. |
| `ssr_boundaries_hits` | Server-side rendering hydration or template boundaries. |
| `events_hits` | Event dispatching, message emission, and signal publishers. |
| `dependency_injection_hits` | Wiring, container resolution signatures, and inversion of control. |
| `macros_hits` | Compile-time logic generation hooks. |
| `pointers_hits` | Raw memory addressing and explicit pointer manipulation. |
| `memory_alloc_hits` | Explicit heap control and manual memory allocation (e.g., `malloc`, `new`). |
| `inline_asm_hits` | Direct hardware instruction injection. |

## Phase 5: Contextual Mitigations (Counter-Weights)
These variables provide the mathematical counter-weights to Phase 2 and Phase 3 risks, ensuring standard language paradigms aren't unfairly penalized.

| Variable | Structural Definition |
| :--- | :--- |
| `telemetry_hits` | Structured logging, observability, and tracing frameworks. |
| `print_hits` | Ad-hoc terminal dumps for transient debugging (e.g., `console.log`). |
| `cast_hits` | Forceful type coercion bypassing the safety engine (Standard friction, not a structural fracture). |
| `bailout_hits` | Hard execution destruction and unrecoverable exceptions (e.g., `panic!`, `abort`). |
| `halt_hits` | Forcing threads to sleep (often a symptom of hidden race conditions). |
| `bitwise_hits` | Low-level byte and binary manipulation. |
| `sync_locks_hits` | Explicit coordination to prevent race conditions (The counter-weight to Concurrency). |
| `freeze_hits` | Explicit locking of data to prevent mutation (The counter-weight to Flux). |
| `cleanup_hits` | Explicit destruction of state or closing of streams (The counter-weight to Memory Alloc/IO). |
| `encapsulation_hits` | Logic deliberately hidden from view (The counter-weight to API Exposure). |
| `listeners_hits` | Waiting to receive state from an external broadcast (The counter-weight to Events). |
| `test_skip_hits` | Framework code that explicitly bypasses verification (e.g., `it.skip`). |

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
