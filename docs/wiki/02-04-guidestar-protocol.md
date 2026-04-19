# The GuideStar Protocol: Contextual Intelligence

> **The Intelligence Officer**
>
> The GuideStar Protocol acts as the "Intelligence Officer" of the GitGalaxy observatory. While the Aperture Filter serves as a shield—a wavelength filter designed to block out binaries and noise by removing files from analysis—we use user-defined whitelists to ensure we don't lose what is important. The GuideStar Protocol is an adaptive intelligence engine that tunes the observatory to the unique atmospheric conditions of a repository by analyzing the structural metadata created by the user.
>
> By reading a project's own roadmap (manifests, folder biases, and explicit `.gitattributes`), GuideStar tells the telescope which signals are intentional logic and which are mere debris. This transforms a rigid exclusion filter into a dynamic system that understands the "Social Proof" of a file before the Language Lens begins its atomic scan.

## The Prior Probability Vector

In the GitGalaxy pipeline, every file in the CensusArray begins as an uninitialized artifact with a base probability of "Deep Space Mystery." Because the observatory operates on a Bayesian logic of "Proof over Assumption," the GuideStar Protocol is responsible for the first major update to this Prior Vector.

By searching for multiple lines of evidence—ranging from explicit `.gitattributes` directives to hardcoded build manifests—the protocol categorizes files into distinct Quality Tiers. These tiers allow the telescope to prioritize its instrumentation: high-tier evidence (like an Authoritative Override) allows for an immediate focus lock, while low-tier or absent evidence flags an artifact for a more intensive spectral audit later in the pipeline.

* **Selective Injection:** GuideStar only updates priors for files or patterns it explicitly "touches" during its environmental scan. It does not perform a blanket sweep; instead, it generates specific evidence of intent via manifests, `.gitattributes` pattern rules, and sector biases.
* **Contextual Tagging:** When GuideStar identifies a file, it attaches a **Data Vector** to the file's metadata. This vector contains the predicted `lang_id`, the `prior_confidence` (intensity), and the `source_proof` (e.g., "Roadmap Lock").
* **Whitelist Trust Bonus:** If an artifact's filename appears in a user-provided **Priority Whitelist**, the GuideStar applies a **Confidence Boost**. The prior intensity is increased by **+0.10** (capped at 0.99), signaling to the pipeline that this specific file has explicit human-validated importance.

## The Handover: Intent vs. Identity

This separation of concerns allows the pipeline to maintain a "Scan Once" efficiency by distinguishing between two different types of intelligence:

1. **GuideStar (The Scout):** Identifies **Intent** (Why this file exists). It says: *"I found this file referenced in a Makefile and it has a known C-extension; I predict it is a C-target with 0.90 confidence."*
2. **Language Lens (The Scientist):** Identifies **Identity** (What this file is). It updates the prior for the "Standard Galaxy" (files with known extensions) and performs the atomic scan to verify all claims.

## The Evidence Hierarchy: Identifying Social Proof

GuideStar prioritizes evidence based on its "Proximity to Human Intent." This principle assumes that explicit configuration files override automated guessing. This hierarchy creates three distinct Quality Tiers that guide the telescope's sensors.

### Tier 1: Machine Roadmap (Authoritative Proof)
This is the "God Tier" of evidence. If a developer explicitly dictates the language of a file or pattern using GitHub's standard `.gitattributes` file (e.g., `*.h linguist-language=C++`), the engine trusts it absolutely.
* **Detection:** Parses `.gitattributes` for `linguist-language=` flags, normalizes the names, and locks the pattern with a **0.99 Prior**, overriding all other heuristics.

### Tier 2: Functional Motion (Dynamic Triggers)
These are machine-readable build manifests where a developer has explicitly declared an artifact's role in the system. Because these files are essential for successful execution, they provide high proximity to logic.
* **Manifest Entries / Binaries:** Files explicitly declared as `main` or `bin` in `package.json`, or as `path =` in `Cargo.toml` receive a **0.95 Prior**.
* **Manifest Scripts / Sources:** Files extracted from command strings (like `npm run`) or Makefile variables (like `SRCS =`) receive a **0.85 Prior**.

### Tier 3: Informational Context (Heuristic Labels)
This tier captures evidence of a file "in motion" or residing in a designated execution neighborhood.
* **Intent-Biased Sectors:** If a file resides in a known execution-heavy directory (e.g., `/bin`, `/scripts`, `/hooks`, `/tools`, `/src`), it is granted an automatic **0.75 Prior** simply for existing in that sector.
* **Makefile Targets:** Non-reserved custom targets identified in build files (e.g., `build-assets:`) are granted a **0.70 Prior**.

## Rules for Deep Manifest & README Analysis

### Deep Manifest Inspection
GuideStar dispatches specific scouts to extract internal references:
* **Node.js:** Scans `main`, `bin`, and the values within `scripts` blocks for potential filenames, using regex to extract `.js`/`.ts` targets from command strings.
* **Makefiles:** Extracts variable assignments (e.g., `SRCS`, `SOURCES`, `FILES`, `TARGET`).
* **Makefile Target Heuristics:** Identifies custom targets. If a target name is not a generic reserved word (like `all` or `clean`), it is injected as a valid artifact.
* **TOML (Python/Rust):** Parses `path =` assignments in `Cargo.toml` and colon-delimited entry points in `pyproject.toml`.

### Tactful README Scanning
Instead of fuzzy README scraping, GuideStar establishes absolute truth by parsing `.gitattributes`. It isolates lines containing `linguist-language=`, translates human-readable tags (like `c++` or `objective-c++`) into the engine's internal nomenclature (`cpp`, `objective-c`), and registers a global pattern matcher. When a file is evaluated, its relative path and filename are tested against these patterns, allowing entire directories or file extensions to be instantly focus-locked.

## Determinism and Inventory Integrity

* **Traceability:** Every file in the final inventory indicates whether its prior was provided by Context (GuideStar) or Signature (Language Lens).
* **Dynamic Resolution:** When asked for a file's status, GuideStar checks in this exact order: `Exact Filename Match` $\rightarrow$ `Relative Path Match` $\rightarrow$ `Pattern Match (.gitattributes)` $\rightarrow$ `Sector Bias`. This ensures hyper-specific locks override generic folder biases.
* **Clean Room Normalization:** Before injection, GuideStar cleans and normalizes all filenames (stripping `./` and leading whitespace) to ensure manifest references align perfectly with physical file paths.