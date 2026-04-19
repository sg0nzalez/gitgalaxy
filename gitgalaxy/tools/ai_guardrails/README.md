# GitGalaxy: Dual-Sided AI Guardrails & AppSec Sensors

[![Defense](https://img.shields.io/badge/Defense-Dual--Sided_AI_Guardrails-00BFFF.svg)](#)
[![Velocity](https://img.shields.io/badge/Velocity-No_Compilation_Required-00C957.svg)](#)
[![Reporting](https://img.shields.io/badge/Reporting-Contextual_Telemetry-8A2BE2.svg)](#)

Welcome to the **GitGalaxy AI Guardrails Suite**.

The AI revolution created two massive blind spots. First, developers are building AI features that give LLMs too much power (The AppSec Threat). Second, developers are unleashing autonomous coding agents that silently break complex codebases (The DevSec Threat).

Legacy security scanners cannot fix this. They look for SQL injection, not Prompt Injection. They rely on slow compilation cycles. 

GitGalaxy maps the architectural reality of your code in seconds. We use AST-free mathematical heuristics to generate deep, contextual reports. We block dangerous AI behavior before it hits production.

---

### 🛡️ Side 1: The AI AppSec Sensor (`ai_appsec_sensor.py`)
*Protects your application from the AI features you build.*

Standard scanners miss "Weaponized AI Architectures." This sensor maps the physical distance between an LLM API call and your critical system functions. 

* **The RCE Funnel:** LLMs wired directly to OS commands. Prevents Prompt-Injection-to-RCE attacks.
* **The "God-Mode" Agent:** Autonomous tools with raw database access. Blocks autonomous data corruption.
* **The Exfiltration Vector:** LLMs accessing network sockets and secrets. Stops SSRF and key exfiltration.

---

### 🤖 Side 2: The Dev Agent Firewall (`dev_agent_firewall.py`)
*Protects your codebase from the autonomous AI tools you use.*

Not all code is safe for an AI (like Cursor or Claude) to modify. This firewall evaluates the physics of a file to determine if an AI agent will succeed, hallucinate, or silently destroy your system.

* **Context Window Shredders:** Massive files with extreme algorithmic complexity. Prevents AI context collapse.
* **The Hallucination Zone:** Heavy metaprogramming with zero documentation. Prevents AI method hallucination.
* **Silent Mutation Risk:** High blast radius with zero test coverage. Blocks unverifiable AI modifications.
* **HITL Mandate:** Severe technical debt detected. Forces human-in-the-loop code review.

---

### 🚀 The GitGalaxy Advantage

This is a fundamentally novel approach to AI security, built for extreme velocity.

* **Zero Compilation:** Scans raw text instantly. No build environment required.
* **Contextual Reporting:** Explains the exact architectural danger. No useless "Yes/No" alerts.
* **CI/CD Ready:** Scans at 100k+ LOC/sec. Blocks dangerous PRs synchronously.