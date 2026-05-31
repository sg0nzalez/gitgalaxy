# GitGalaxy: Zero-Trust DevSecOps Action

[![Marketplace](https://img.shields.io/badge/GitHub-Marketplace-blue.svg)](#)
[![Architecture](https://img.shields.io/badge/Architecture-AST--Free_Physics-00BFFF.svg)](#)
[![Security](https://img.shields.io/badge/Security-Zero--Trust_Enforcement-FF4500.svg)](#)

GitGalaxy is an AST-free, high-velocity heuristic physics engine for codebase architecture and DevSecOps. 

Instead of relying on slow static parsers, GitGalaxy translates structural codebase DNA into N-dimensional risk physics. This GitHub Action allows you to drop our entire suite of security sentinels, autonomous AI guardrails, and architectural cartography tools directly into your CI/CD pipeline. It physically blocks threats and automatically generates living architectural documentation.

For a deep dive into the methodology, see [The blAST Paradigm](docs/wiki/01-03-the-blast-paradigm.md) and our [Security Landscape Overview](docs/wiki/04-00-security_landscape.md).

---

## 🚀 The "Golden Path" (Recommended Pipeline)

For the highest level of automated enterprise security and documentation, we recommend the **Parallel Enforcement & Autonomous Reporting** pipeline. 

This workflow runs our core Zero-Trust Sentinels simultaneously for lightning-fast pipeline execution. If (and only if) the code passes all security gates, the Orchestrator (`galaxyscope`) generates an updated LLM Architectural Brief and automatically commits it back to your `main` branch under the `docs/` folder.

Create a file at `.github/workflows/gitgalaxy-pipeline.yml`:

```yaml
name: GitGalaxy Zero-Trust Pipeline

on:
  push:
    branches:
      - main

jobs:
  vault-sentinel:
    name: Vault Sentinel
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: squid-protocol/gitgalaxy@v2.2.1
        with:
          tool: 'vault-sentinel'
          target: '.'

  xray-inspector:
    name: X-Ray Inspector
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: squid-protocol/gitgalaxy@v2.2.1
        with:
          tool: 'xray-inspector'
          target: '.'

  supply-chain-firewall:
    name: Supply Chain Firewall
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: squid-protocol/gitgalaxy@v2.2.1
        with:
          tool: 'supply-chain-firewall'
          target: '.'

  architectural-report:
    name: Autonomous LLM Brief
    needs: [vault-sentinel, xray-inspector, supply-chain-firewall]
    runs-on: ubuntu-latest
    permissions:
      contents: write # Grants the Action permission to push the report to main
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Required to calculate historical Volatility/Churn

      - name: Generate GalaxyScope LLM Brief
        uses: squid-protocol/gitgalaxy@v2.2.1
        with:
          tool: 'galaxyscope'
          target: '.'
          args: '--llm-only'
          full_precision: 'true'

      - name: Commit and Push LLM Brief to Main
        run: |
          mkdir -p docs
          mv *_galaxy_llm.md docs/gitgalaxy_architecture_brief.md || true
          
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add docs/gitgalaxy_architecture_brief.md
          
          # Only commit and push if the architecture actually changed
          git diff --quiet && git diff --staged --quiet || (git commit -m "docs: auto-update LLM architectural brief" && git push)
```

---

## 🧰 The Arsenal: Tool Directory

The `tool` input determines which GitGalaxy program executes. Choose the right tool for your specific pipeline stage:

### 1. The Orchestrator (Reporting & Observability)
* **[`galaxyscope`](docs/wiki/01-02-galaxyscope-cli-reference.md)**: The core mapping engine. It calculates 18-point risk physics (Cognitive Load, State Flux, Instructional Density), runs ML threat inference, and generates outputs (LLM Markdown Briefs, GPU Payloads, SQLite DBs). *Does not fail the pipeline; strictly for reporting and cartography.*

### 2. The Sentinels (Zero-Trust Enforcement)
*These tools are designed to `sys.exit(1)` and break the build instantly if a threat is detected.*
* **[`vault-sentinel`](docs/wiki/04-04-vault-sentinel.md)**: High-speed secrets scanner. Drops the hammer on hardcoded API keys, exposed `.env` variables, and cryptographic vault leaks.
* **[`xray-inspector`](docs/wiki/04-05-binary-anomaly-detector.md)**: Binary and Obfuscation scanner. Hunts for high-entropy encrypted payloads, sub-atomic XOR loops, and hidden executables disguised via magic byte mismatches (e.g., malware hidden in a `.png`).
* **[`supply-chain-firewall`](docs/wiki/04-03-supply-chain-firewall.md)**: Dependency execution verifyer. Blocks blacklisted imports, identifies shadowed/steganographic imports, and flags tainted I/O access.

### 3. AI Agent Guardrails (Safe Autonomous Development)
*If your team uses autonomous AI agents (Cursor, Claude, Devin) to write code, these sentinels ensure they do not create catastrophic security loops or collapse under cognitive load.*
* **[`ai-appsec-sensor`](docs/wiki/02-17-ai-appsec-sensor.md)**: Hunts for weaponized AI architectures. Flags dangerous intersections where LLMs are given access to OS commands, database writes, or unfiltered network sockets (Prompt Injection -> RCE).
* **[`dev-agent-firewall`](docs/wiki/02-18-dev-agent-firewall.md)**: Evaluates algorithmic complexity and blast radius to determine if an AI has the context to safely modify the code. Flags "Context Window Black Holes" and enforces Human-in-the-Loop (HITL) mandates for highly volatile infrastructure.

### 4. Specialized Hunters & Artifacts (Targeted Audits)
* **[`zero-trust-sbom`](docs/wiki/04-02-sbom-generator.md)**: Generates a universally compliant CycloneDX 1.4 JSON SBOM. Unlike standard tools that blindly trust manifests, this engine physically verifies packages on disk, flagging high-entropy code and spoofed files.
* **[`api-network-map`](docs/wiki/04-01-full-api-network-map.md)**: Compares physical source-code routing against official OpenAPI/Swagger specs to hunt down undocumented **Shadow APIs** (Security Risks) and **Ghost APIs** (Audit Bloat).
* **[`pii-leak-hunter`](docs/wiki/04-06-pii-leak-hunter.md)**: A high-velocity streaming binary scanner for massive, single files. Scrubs database dumps or raw production logs for exposed VISA, Mastercard, SSN, and AWS keys, generating a safely masked evidence log.

---

## ⚙️ Inputs & Configuration

Configure the GitGalaxy action via the `with` block in your workflow step.

| Input | Required | Default | Description |
| :--- | :--- | :--- | :--- |
| `tool` | Yes | `galaxyscope` | The specific executable to run (see Tool Directory above). |
| `target` | Yes | `.` | The directory or specific file path to scan. |
| `args` | No | `""` | Additional CLI arguments passed directly to the tool. |
| `version` | No | `latest` | Target a specific PyPI version of GitGalaxy (e.g., `2.2.1`). |
| `full_precision` | No | `false` | Set to `'true'` to install heavy physics engines (`networkx`, `tiktoken`, `xgboost`) for Blast Radius math and ML Threat Inference. |

### 🛡️ Understanding the `--paranoid` Flag

When passing arguments via `args`, the `--paranoid` flag allows you to control the sensitivity of the [Security Lens](docs/wiki/02-06-security-lens.md).

* **Standard Mode (Omitted):** Built for typical enterprise environments. Evaluates codebase architecture using high-confidence security thresholds to prevent CI/CD fatigue. Focuses on undeniable architectural flaws and confirmed vulnerabilities. This is the recommended setting for standard blocking pipelines.
* **Paranoid Mode (`--paranoid`):** Lowers all safety thresholds to their minimums, turning the engine into a hyper-sensitive threat hunter. It provides a full list of all *possible* issues, structural anomalies, and theoretical attack vectors. **Warning:** This mode is highly false-positive rich by design. It is intended for rigorous security audits, zero-trust sandbox evaluations, and aggressive red-teaming where you want to manually review every potential structural weakness.

---

## 🛠️ Advanced Integration Examples

### Universal Zero-Trust SBOM Generation
Generate a physical-verified CycloneDX SBOM to attach to a release.

```yaml
      - name: Generate Physical SBOM
        uses: squid-protocol/gitgalaxy@v2.2.1
        with:
          tool: 'zero-trust-sbom'
          target: '.'
          
      - name: Upload SBOM Artifact
        uses: actions/upload-artifact@v4
        with:
          name: project-sbom
          path: '*_bom.json'
```

### Autonomous AI Guardrail Audit
Automatically halt the CI/CD pipeline if an AI agent commits code that exposes an RCE funnel or creates a cognitive black hole.

```yaml
      - name: AI AppSec Validation
        uses: squid-protocol/gitgalaxy@v2.2.1
        with:
          tool: 'ai-appsec-sensor'
          target: '.'

      - name: Agent Context Firewall
        uses: squid-protocol/gitgalaxy@v2.2.1
        with:
          tool: 'dev-agent-firewall'
          target: '.'
```

### Shadow API Hunter
Automatically audit Pull Requests to ensure developers aren't silently exposing new endpoints without updating the Swagger documentation.

```yaml
      - name: Shadow API Audit
        uses: squid-protocol/gitgalaxy@v2.2.1
        with:
          tool: 'api-network-map'
          target: '.'
          # Optional: Point directly to a swagger file, or use --merge-all for monorepos
          args: '--swagger ./docs/openapi.yaml'
```