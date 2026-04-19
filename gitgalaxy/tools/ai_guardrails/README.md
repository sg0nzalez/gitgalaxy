# GitGalaxy: Dual-Sided AI Guardrails & AppSec Sensors

[![Defense](https://img.shields.io/badge/Defense-Dual--Sided_AI_Guardrails-00BFFF.svg)](#)
[![Velocity](https://img.shields.io/badge/Velocity-No_Compilation_Required-00C957.svg)](#)
[![Reporting](https://img.shields.io/badge/Reporting-Contextual_Telemetry-8A2BE2.svg)](#)

Welcome to the **GitGalaxy AI Guardrails Suite**.

The AI revolution introduces two entirely new threat models to software engineering:
1. **The AppSec Threat:** Your developers are building AI features that give LLMs too much power, turning standard prompt injection into catastrophic RCE or data exfiltration.
2. **The DevSec Threat:** You are unleashing autonomous AI coding agents (like Cursor or Claude) onto your codebase, but they get confused by complex metaprogramming or lack of tests, silently breaking the architecture.

Legacy security scanners were built for SQL injection, not Prompt Injection. They rely on slow ASTs and compilation cycles. **GitGalaxy’s Dual-Sided AI Guardrails** solve this. Because our engine operates via high-speed, AST-free mathematical heuristics, we map the entire architectural intent of your repository in seconds, generating deep, contextual reports instead of useless binary "yes/no" flags.

---

### 🛡️ Side 1: The AI AppSec Sensor (`ai_appsec_sensor.py`)
*Protects your application from the AI features you build.*

This sensor hunts for "Weaponized AI Architectures." It maps the topological distance between an LLM API call and critical system functions. 

* **The RCE Funnel:** Detects when an LLM orchestrator is adjacent to OS-level execution (`eval`, `subprocess`) and exposed via a public API router. This is the exact anatomy of a catastrophic Prompt Injection to RCE vulnerability.
* **The "God-Mode" Agent:** Flags autonomous AI tools bound to raw database writes with a low defensive programming density (lack of try/catches or regex validators). 
* **The Exfiltration Vector:** Identifies LLM logic that has access to both unsandboxed network sockets and environment secrets, highlighting immediate SSRF and key-exfiltration risks.

---

### 🤖 Side 2: The Dev Agent Firewall (`dev_agent_firewall.py`)
*Protects your codebase from the autonomous AI tools you use.*

Not all code is safe for an AI to modify. This firewall evaluates the physical physics of a file to determine if an autonomous agent will succeed, hallucinate, or silently destroy your system.

* **The Context Window Shredder (Black Holes):** If a file burns > 8,000 tokens and has terrible algorithmic complexity (O(N^3)), the AI's context window will collapse. The firewall blocks the agent from engaging.
* **The Hallucination Zone:** Detects heavy dynamic metaprogramming combined with a documentation density of < 20%. The AI *will* hallucinate missing methods here. 
* **Silent Mutation Risk:** Flags files with high State Flux, massive "Blast Radius" (in-degree dependencies), and ZERO tests. If the AI breaks this file, it cannot verify its own fixes, and the blast will take down the system.
* **HITL Mandate (Human-In-The-Loop):** Automatically flags files with severe technical debt and high architectural gravity as requiring manual human review before any AI-generated PR can be merged.

---

### 🚀 The GitGalaxy Advantage

* **Zero Compilation Required:** We scan the raw text. We don't need your code to build, compile, or install dependencies to map the AI threat surface. 
* **Contextual, Thorough Reporting:** We don't just output `Is_Vulnerable: True`. We correlate topological blast radius, token mass, semantic complexity, and test coverage to give you the exact *architectural reason* why a file is dangerous.
* **CI/CD Ready:** Because the entire repository is scanned at 100k+ LOC/sec, these guardrails can run on every single pull request, instantly blocking an AI agent from modifying a "Black Hole" file, or blocking a developer from pushing a "God-Mode" LLM feature.