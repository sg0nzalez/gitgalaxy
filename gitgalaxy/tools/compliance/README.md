# GitGalaxy: Compliance & Zero-Trust SBOM Generation

[![Standard](https://img.shields.io/badge/Standard-CycloneDX_1.4-00C957.svg)](#)
[![Security](https://img.shields.io/badge/Security-Zero__Trust-FF4500.svg)](#)
[![Pipeline](https://img.shields.io/badge/Pipeline-Bayesian_Optics-8A2BE2.svg)](#)

Welcome to the **GitGalaxy Compliance & SBOM Suite**.

The industry standard for generating a Software Bill of Materials (SBOM) is fundamentally flawed. Standard tools open your `package.json`, `composer.json`, or `requirements.txt`, read the list of dependencies, and blindly export them to a PDF. **They trust the manifest.**

But manifests lie. A supply chain attack doesn't announce itself. A package might claim to be a simple text-formatting utility, but its physical files contain high-entropy encrypted payloads, obfuscated malware, or mismatched languages. 

GitGalaxy takes a **Zero-Trust** approach. We don't just read the manifest; we physically hunt down the package on your disk and scan its internal contents to mathematically verify its identity and safety before signing off on the compliance report.

### 🧠 The Zero-Trust Strategy: Trust Nothing, Verify Everything

When you run our Universal SBOM Generator, it leverages the full weight of the GitGalaxy physics engine to audit your dependencies:

#### 1. The Universal Manifest Slicer
It automatically detects your ecosystem (NPM, PyPI, Composer, Cargo), slices the manifest, and cross-references the declared dependencies against what actually exists on your hard drive. If a dependency is claimed but missing, it is flagged as `UNVERIFIED_MISSING_ON_DISK`.

#### 2. Deep File Inspection & The Language Lens
For every package found on disk, we open the core source files and run them through our **Language Lens**. We use Bayesian Optics to confirm the file's true identity. 
* **Identity Spoofing:** If an attacker hides a malicious bash script by naming it `index.js`, the Language Lens cross-references the extension against the internal file shebangs and structural markers. It triggers an **Identity Crisis** and flags the package as `SPOOF_DETECTED`.
* **Entropy Math:** We calculate the Shannon Entropy of the raw code. If the structural density exceeds standard human programming bounds (e.g., an entropy score > 4.8), we flag it for containing encrypted or packed payloads.

### 🛡️ The Full GitGalaxy Defense Pipeline

Our compliance auditing isn't just a simple script; it is backed by a multi-tiered, battle-tested astronomical pipeline:

* **Aperture (The Solar Shield):** Acts as the frontline perimeter. It detects embedded hex arrays, opaque binary debris, and machine-generated monoliths before they can overwhelm the system.
* **GuideStar Lens (Intent & Evasion):** Scans your metadata (`.gitattributes`, `Makefile`). Crucially, it hunts for evasion tactics—like an attacker using `.gitignore` to secretly force-include a malicious `.so` binary while hiding it from standard directory scans.
* **Language Lens (The Trust Matrix):** Bypasses LLM hallucinations by using 60+ strict keyword regex profiles to definitively lock in a file's language family based on structural evidence, not just its extension.
* **Spectral Auditor (Quality Control):** Applies the "50/0 Law" and Z-Score math. If a file claims to be a specific language but its structural logic density is a mathematical outlier compared to the rest of the ecosystem, it drops into the **Quarantine Guard**. We catch malware trying to disguise itself as inert data dumps.

---

### 🚀 Quickstart: Generate a Zero-Trust SBOM

Run the Universal SBOM Generator against the root of your project. It will automatically find your manifests, locate the physical dependencies, scan their internals, and output an industry-standard CycloneDX JSON file.

```bash
python3 sbom_generator.py /path/to/your/project
```

---
### 🌌 Powered by the blAST Engine
This tool is a spoke in the larger GitGalaxy ecosystem. It is powered by the **blAST Engine**, an AST-free, mathematical heuristics engine capable of mapping repositories at 100,000 LOC/sec.

* 📖 **[Read the Official Wiki](https://squid-protocol.github.io/gitgalaxy/)** for deep dives into the engine's physics, architecture blueprints, and the Taxonomical Equivalence Map.
* 🪐 **[Return to the Main GitGalaxy Hub](https://github.com/squid-protocol/gitgalaxy)** to explore other enterprise tools like Supply Chain Firewalls and Terabyte Log Scanners.
