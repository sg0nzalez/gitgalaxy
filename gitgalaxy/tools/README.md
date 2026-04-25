# 🛠️ GitGalaxy Tools (The Spokes)

Welcome to the GitGalaxy Tools directory. 

If `galaxyscope.py` is the core physics engine (the Hub), the tools in this directory are the "Spokes." These are specialized, standalone execution controllers that leverage GitGalaxy's AST-free, high-speed parsing capabilities to solve specific engineering and security challenges.

Each sub-module is designed to be executed directly from the CLI or wired into CI/CD pipelines.

## 📂 Tool Suites Directory

### 🛡️ [Supply Chain Security](./supply_chain_security/README.md)
Zero-trust DevSecOps tools designed for pre-commit hooks and CI/CD pipeline blocking.
* **Supply Chain Firewall:** Scans `node_modules` and vendor directories for malicious typosquatting and unauthorized network I/O.
* **Vault Sentinel:** Hyper-speed secrets and credential detection.
* **Binary Anomaly Detector:** Triage engine for finding encrypted payloads and parasitic logic hidden in binary artifacts.

### 📜 [Compliance & Auditing](./compliance/README.md)
Tools for generating forensic and legal records of software architecture.
* **Zero-Trust SBOM Generator:** Builds CycloneDX/SPDX manifests verified by structural code analysis, not just package manifests.

### 🕵️ [Terabyte Log Scanning](./terabyte_log_scanning/README.md)
High-throughput engines for processing massive data outputs.
* **PII Leak Hunter:** Scans terabytes of raw logs for accidentally exposed PII without choking system memory.
* **Terabyte Log Scanner:** Maps static architecture to dynamic runtime execution logs.

### 🕸️ [Network Auditing](./network_auditing/README.md)
* **API Network Mapper:** Automatically maps the physical outbound and inbound API surface area and compares it against Swagger/OpenAPI docs to find Shadow APIs.

### 🦕 [Legacy Modernization: COBOL to Java](./cobol_to_java/README.md) & [COBOL to COBOL](./cobol_to_cobol/README.md)
A complete suite of architectural controllers for modernizing legacy mainframe systems.
* **COBOL Refractor:** Slices massive monolithic COBOL programs into isolated microservices.
* **Java Spring Forge:** Translates legacy business logic into compiling Java Spring architectures.

### 🤖 [AI Guardrails](./ai_guardrails/README.md)
* **AppSec Sensor & Dev Agent Firewall:** Middleware sensors that prevent LLMs from being wired to RCE vulnerabilities, and block autonomous AI coding agents from mutating highly complex legacy code.

---

## 🚀 Execution & CI/CD Integration

The GitGalaxy Spoke architecture allows you to run these specialized tools using three distinct methods:

### 1. GitHub Actions (The Universal Pipeline)
You can trigger any of the standalone CLI tools in your CI/CD pipeline using our universal composite action. Simply change the `tool` parameter to the spoke you want to execute:

```yaml
      - name: Run GitGalaxy Tool
        uses: squid-protocol/gitgalaxy@main
        with:
          tool: 'supply-chain-firewall' # Options: xray-inspector, zero-trust-sbom, api-network-map, etc.
          target: '.'
```

### 2. Global CLI Execution
If you have GitGalaxy installed via PyPI (`pip install gitgalaxy`), all the standalone tools are registered as global console scripts. You can run them instantly from your terminal:
```bash
vault-sentinel .
api-network-map ./src
pii-leak-hunter ./logs/dump.sql
```

### 3. Engine Middleware (AI Guardrails)
Note that the **AI Guardrails** do not operate as standalone CLI tools. They act as deep-inspection middleware. To utilize them, run the primary `galaxyscope` engine, and the sensors will automatically inject their AppSec findings into the final project telemetry.