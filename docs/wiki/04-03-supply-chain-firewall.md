# The Supply Chain Firewall (Zero-Trust Verification)

> **Guarding the Gates**
>
> Third-party dependencies are the most vulnerable entry point in any modern application. An attacker doesn't need to hack your servers; they just need to compromise a single NPM or PyPI package you rely on.
>
> The Supply Chain Firewall (`supply_chain_firewall.py`) acts as a strict, high-speed quarantine zone. It scans the massive `node_modules` or `venv` directories, enforcing a Zero-Trust architecture to catch malicious packages, Unicode homoglyph attacks, steganography, and hostile I/O execution before the code is ever built or deployed.

## Zero-Trust Import Verification

The firewall utilizes a Universal Import Slicer (regex) to rip through source files (`.js`, `.py`, `.ts`, `.php`, `.go`, `.rs`) and extract exactly what external packages the dependencies are trying to load. 

It evaluates every single `import` or `require` statement against a strict policy matrix:

* **Banned Packages:** Checks against a `BLACKLISTED_IMPORTS` list. If a known malicious package is found, it immediately triggers a `[BLACKLISTED IMPORT]` alert and fails the build.
* **Strict Import Mode:** The firewall can operate in a true Zero-Trust state. If `STRICT_IMPORT_MODE` is enabled, any package that is not explicitly defined in the `APPROVED_IMPORTS` registry is flagged as an "Unknown Package" and blocked.

## High-Speed Security Physics

Scanning tens of thousands of dependency files requires massive computational velocity. To achieve this, the Orchestrator instantiates a `SecurityLens` using the "paranoid" `ThreatPolicy`, but applies a critical **Speed Fix**. 

The firewall explicitly neuters the Security Lens, restricting its regular expression sensors to hunt *only* for supply-chain-specific indicators of compromise:
* `homoglyphs` (Typo-squatting or visual spoofing in the code)
* `shadow_imports` (Attempting to import modules dynamically to bypass static analysis)
* `io` (Unexpected filesystem or network access inside a utility library)
* `danger` (Direct `eval` or remote code execution triggers)
* `flux` (State mutation)

### The Inert Data Shield
To prevent false positives and save CPU cycles, the firewall employs an Inert Data Shield. If a file is a static data format (e.g., `.json`, `.md`, `.csv`, `.yaml`), the engine forcefully zeroes out its threat counts, ensuring the physics engine only evaluates active, executable logic.

## Density Thresholds & Steganography

Sophisticated malware often hides its payload deep within legitimate utility functions (steganography). A single suspicious string might just be a false positive, but a dense cluster of them is a threat.

The firewall calculates the structural density of the threats against the physical lines of code. If the exposure density breaches the "paranoid" policy thresholds, it explicitly flags:
* **Hidden Malware Risk:** Too many obfuscation techniques or shadow imports detected in a small physical area.
* **Data Injection Risk:** High concentrations of dangerous `eval` or untainted I/O operations.

When these thresholds are breached, the firewall dumps the exact code snippets (evidence) to the console so security engineers can see exactly what triggered the alarm.

## The CI/CD Build Breaker

The Supply Chain Firewall is designed to run as a blocking step in a CI/CD pipeline. 

Upon completion, it prints a highly readable Mission Report detailing its scan velocity, the number of approved/banned packages, and the total number of Active Threats. If even a single threat or policy violation is found, the script exits with a status code of `1`, violently failing the build and preventing the infected dependency from reaching production.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

