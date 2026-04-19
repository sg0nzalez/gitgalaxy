# Batch Test Harness

> **Architecture: Automated Compilation & CI/CD Validation**
>
> **Summary:** The Batch Test Harness is an automated stress-testing tool designed to validate the output of the entire V4 GitGalaxy pipeline across an arbitrary number of legacy repositories. It proves that the generated JSON Intermediate Representation (IR) successfully translates into a 100% compilable Spring Boot architecture.

## The Three-Phase Validation Loop

The harness iterates through the corpus directory, running each repository through a strict validation sequence:
1. **Refraction Phase:** Executes the COBOL Refractor Controller. Converts the legacy monolith into the JSON IR using the auto-scaling State Manager.
2. **Java Forge Phase:** Executes the Java Translation Controller. Scaffolds the Spring Boot architecture, PostgreSQL schemas, and Mock Services.
3. **Compilation Phase:** Spawns a localized Maven subprocess (`mvn clean compile`) to attempt a full build of the generated architecture.

## Execution Isolation & Stability

To ensure consistent testing across varying local environments, the harness applies strict execution controls:
* **Environment Sandboxing:** The harness clones the host environment and explicitly overrides the `JAVA_HOME` path to enforce Java 17 OpenJDK standards.
* **Infinite Hang Protection:** Legacy code can occasionally trigger catastrophic regex recursion. The harness wraps every subprocess command in a strict 5-minute timeout (`timeout=300`). If a phase stalls, the harness safely kills the thread, logs a timeout failure, and proceeds to the next repository.

## Granular Telemetry

All Standard Output (STDOUT) and Standard Error (STDERR) from the Refractor, Java Forge, and Maven compiler are captured and piped into a `batch_test_reports/` directory. If a repository fails to compile, the harness dumps the exact Maven dependency or syntax error into an isolated log file, allowing the engineering team to rapidly debug translation bottlenecks.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

