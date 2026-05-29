# API & Service Contracts

> **Architecture: Dual-Paradigm Execution & Dependency Injection**
>
> **Summary:** The API and Service Forges translate the legacy Directed Acyclic Graph (DAG) intent into modern Spring Boot REST Controllers and `@Service` layers. It automatically detects the execution paradigm (Batch vs. Transactional) and auto-wires cross-service dependencies.

## Dual-Paradigm Execution Detection

Legacy COBOL operates in two primary modes: CICS (Transactional) and JCL (Batch). The API Contract Forge analyzes the DAG lineage to detect the original intent and scaffolds the corresponding REST interface.

* **The Transactional Paradigm:** If the module relies on structured data inputs/outputs without physical file requests, the forge generates a standard JSON POST endpoint (`/api/v1/{module}/execute`). It automatically injects the required Data Transfer Objects (`@RequestBody DTO`) based on the input schemas.
* **The Batch Paradigm:** If the DAG indicates the module expects physical file bindings (`DD` names), the forge switches to a Batch paradigm. It generates a specialized multipart endpoint (`/api/v1/{module}/execute-batch`) mapped to `@RequestParam MultipartFile` inputs, securely piping the data streams directly into the Service layer.

## Auto-Wiring the Service Layer

The Service Forge generates the `@Service` skeleton where the actual business logic will reside. It utilizes the DAG to map the architectural lineage and inject cross-service dependencies:
* **Known Dependencies:** Fully resolved module calls are injected into the class constructor for standard Spring Dependency Injection (`@RequiredArgsConstructor`).
* **Unresolved Dependencies:** If the legacy code dynamically calls a module that was not found in the repository scan, the forge injects a `TODO: AI AGENT` comment with the required interface signature. It intentionally comments out the dependency to ensure the generated Spring Boot application remains fully compilable out of the box.

## The Mock Service Shield

To prevent missing external subroutines from crashing the Spring Application Context upon booting, the orchestrator generates Mock Services for any unresolved calls. These mock services intercept the legacy call, log a standard warning (`"Mock Service invoked. Implementation missing."`), and safely return execution to the main thread.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
