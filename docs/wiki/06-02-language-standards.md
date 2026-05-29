# Language Standards (The Linguistic Registry)

> **The Universal Translator**
>
> The `language_standards.py` file is the master linguistic registry of GitGalaxy. It does not execute any logic itself; rather, it provides the precise mathematical constants, structural blueprints, and regular expression schemas that the optical lenses use to parse the universe.
>
> **Extensibility:** If GitGalaxy encounters an unknown syntax, this is the exact file where developers can add support for entirely new programming languages, proprietary legacy scripts, or custom domain-specific languages (DSLs).

## The 51-Element Universal Schema

To ensure that downstream engines (like the XGBoost ML model and the 3D WebGL UI) never crash due to misaligned data, the standards enforce a strict `UNIVERSAL_METRICS_SCHEMA`. 

Every language, regardless of how it is structured, must map its **syntax heuristics** into this exact 51-element array. This guarantees that a loop in C++, a list comprehension in Python, and a recursive function in Lisp can all be compared mathematically on the exact same risk scale. If a new language definition attempts to inject an unregistered rule, the engine will actively ignore it.

## The Language Definitions Registry

The core of the file is the `LANGUAGE_DEFINITIONS` dictionary. Every supported language possesses a strict blueprint defining its physical properties. 

If you are **adding a new language** to GitGalaxy, you simply add a new block to this registry. A complete language block requires four core components:

### 1. Identity & Ecosystem (The Metadata)
* **`extensions`:** The list of file extensions associated with the language (e.g., `['.js', '.jsx']`). Used by the Language Lens to establish initial Ecosystem Gravity.
* **`disqualifiers`:** A blacklist of regex strings. If the engine finds `<?php` inside a file claiming to be Python, the definition actively rejects the file to prevent hallucinations.
* **`handicap`:** A multiplier (typically `1.0`). Legacy languages with incredibly broad keywords (like ABAP or Fortran) receive a severe handicap (e.g., `0.4`) so their greedy regex rules don't artificially swallow other languages during Discovery Mode.

### 2. The Optical Mode (The Splicer Routing)
Tells the Detector which extraction algorithm to use when slicing the file into functions:
* **Mode A (Label-Based):** For procedural legacy languages (Assembly, COBOL).
* **Mode B (Recursive Scope):** For languages using braces `{}` or parentheses `()` (C++, Java, Lisp).
* **Mode C (Density Stratification):** For whitespace-sensitive languages (Python, YAML).
* **Mode D (Semantic Handshake):** For keyword-bounded scripts (Ruby, Elixir, Bash).
* **Mode E (Terminator Cleaving):** For declarative architectures (SQL, Erlang).

### 3. The Prism Family (Comment Routing)
Tells the Prism exactly how to strip the literature out of the file without destroying string literals. You map the language to one of the 9 pre-compiled **language families** (e.g., `std_c` for `//`, `pure_hash` for `#`, or `hybrid_dash` for `--`).

### 4. The Structural Geometry (Regex Triggers)
The bulk of the definition. This maps the language's specific syntax to the Universal Schema.
* **Example:** To satisfy the `branch` metric, the Python definition might supply the regex `r'\b(if|elif|else)\b'`, while the SQL definition supplies `r'\b(WHEN|ELSE|IF)\b'`.
* **Security Triggers:** This is also where language-specific danger zones are defined, such as mapping `eval()` or `child_process.exec` to the `sec_danger` key for the AI AppSec Sensor to catch.

## Extending the Galaxy (Adding New Languages)

Because GitGalaxy dynamically compiles its parsing engines at runtime based on this exact file, adding a new language requires **zero changes to the core parsing logic**. 

To add a proprietary or novel language:
1. Open `language_standards.py`.
2. Create a new dictionary key (e.g., `my_custom_dsl`).
3. Define its extensions, routing modes, and regex triggers.
4. The next time the Orchestrator boots, the `LanguageDetector` and `LogicSplicer` will automatically ingest the new blueprint, instantly allowing the 3D Cartographer to map your custom code.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
