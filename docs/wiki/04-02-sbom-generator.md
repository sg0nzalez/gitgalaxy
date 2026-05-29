# SBOM Generator (Zero-Trust Supply Chain)

> **Physical Verification of Dependencies**
>
> Standard Software Bill of Materials (SBOM) generators blindly trust configuration files. If `package.json` claims to install "React", a standard generator logs it as safe. 
>
> The GitGalaxy SBOM Generator (`sbom_generator.py`) operates on a **Zero-Trust** model. It does not just read the manifest; it physically hunts down the installed dependency on disk, scans its structural DNA for anomalies, and verifies that the code hasn't been spoofed or infected.

## The Universal Manifest Slicer

Modern repositories are often polyglots, utilizing multiple package managers simultaneously. The `UniversalManifestSlicer` handles this by natively parsing the standard manifests of four major ecosystems:

* **NPM (JavaScript/TypeScript):** Parses `package.json` for `dependencies` and `devDependencies`.
* **Packagist (PHP Composer):** Parses `composer.json` for `require` and `require-dev`.
* **PyPI (Python):** Uses regex to parse `requirements.txt`, safely extracting version bounds.
* **Cargo (Rust):** Uses universal regex to extract dependency blocks from `Cargo.toml`.

## The Zero-Trust Physical Audit

Once the dependencies are claimed by the manifests, the engine executes a physical audit to verify their integrity.

### 1. Locating the Payload
The engine hunts for the physical package within the local project bounds (e.g., `node_modules`, `vendor`, or a Python `venv`/`.venv` directory). 
* If the package is declared but cannot be found locally, it is flagged as `UNVERIFIED_MISSING_ON_DISK`.

### 2. The Micro-Scan (Max 5 Files)
To maintain velocity, the generator does not scan every single file in massive dependencies. It extracts a sample of up to 5 core files (`.js`, `.py`, `.ts`, `.php`, `.rs`) from the package directory.
* **Entropy Check:** It runs the file through the `SecurityLens`. If the dependency contains mathematically dense/encrypted strings (Shannon Entropy > 4.8), it is flagged as a potential hidden payload.
* **Spoof Detection:** It runs the file through the `LanguageDetector`. If the file claims to be JavaScript but triggers structural anomalies, it flags the package as spoofed.

### 3. Trust Assignment
Dependencies that fail the micro-scan are flagged as `SPOOF_DETECTED` and their specific anomaly notes are recorded. Packages that pass are marked `VERIFIED_SAFE`.

## CycloneDX 1.4 Serialization

The final output is not a proprietary JSON structure, but a fully compliant **CycloneDX 1.4 JSON** file, ensuring it can be ingested by standard enterprise compliance tools.

However, GitGalaxy enriches this standard by injecting its physical audit data as custom properties on every component:
* `"name": "gitgalaxy:trust_status"`
* `"name": "gitgalaxy:anomaly_notes"`

This creates a hyper-accurate SBOM that tells compliance teams not only what open-source libraries are installed, but exactly which ones have been physically compromised.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
