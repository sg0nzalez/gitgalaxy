# Lexical Patcher

> **Architecture: Pre-Processing Trap Neutralization**
>
> **Summary:** Legacy COBOL frequently relies on outdated control flow structures that break modern Abstract Syntax Tree (AST) parsers. The Lexical Patcher acts as a pre-processor, safely restructuring these traps into deterministic modern equivalents before the main analysis engine engages.

## The Dialect Sensor
Because altering mainframe source code carries extreme risk, the patcher first executes a Dialect Sensor to determine the compiler era of the file. It scans for post-1985 structural keywords (e.g., `EVALUATE`, explicit scope terminators like `END-IF`). 
* If the code targets a modern compiler (COBOL-85+), the patcher is cleared to inject modern equivalents.
* If the code is constrained to COBOL-74, the patcher engages "ultra-conservative punch-card mode," bypassing modern injections to prevent `0C1` compiler crashes.

## Neutralizing NEXT SENTENCE
The `NEXT SENTENCE` directive is a notoriously dangerous legacy construct that acts as an implicit, invisible `GO TO` jumping past the next period. This breaks deterministic control flow.
* **COBOL-85 Mode:** The patcher safely rewrites the trap into a localized, block-scoped `CONTINUE` statement, appending a traceable `*>` inline comment to document the automated remediation.
* **COBOL-74 Mode:** The patcher leaves the `NEXT SENTENCE` command intact but cleans the surrounding whitespace to ensure the downstream AST slicer can accurately track the statement without crashing.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
