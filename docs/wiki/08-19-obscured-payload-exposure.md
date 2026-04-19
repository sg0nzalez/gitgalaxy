# Obscured Payload Exposure

> **Metric: Malicious Intent Density (Steganography & Evasion)**
>
> **Summary:** A core Security Lens metric. It detects code that actively attempts to hide its execution path or intent. It looks for the combination of "Obfuscation" (hiding) and "Intent" (destructive or exfiltration capabilities). 
>
> **Effect:** Maps to the Universal Risk Spectrum. Any high score here is an immediate red flag for potential malware, trojans, or highly evasive technical debt.

## The Inputs (Threat Vectors)

The deterministic engine categorizes threats into two distinct masses: Obfuscation and Intent.

| Vector | Heuristics Included | Weight | Role |
| :--- | :--- | :--- | :--- |
| **Glassworm** | Metaprogramming, Bitwise math | High | **Obfuscation.** Hides logic flow. |
| **Steganography** | Shadow imports, Extension mismatch | Extreme | **Obfuscation.** Active evasion tactics. |
| **Shadow Logic** | Dead code / Graveyards | Low | **Obfuscation.** Hiding in the noise. |
| **Executioner** | `eval`, `exec`, unsafe execution | Extreme | **Intent.** Destructive capabilities. |
| **Exfiltration** | Network IO, file system access | High | **Intent.** Moving data across boundaries. |

## The Equation: Biaxial Threat Synthesis

**Step A: Group and Dampen Obfuscation**
We calculate the raw Obfuscation mass. Because scientific libraries use heavy math and strange symbols naturally, we apply an "Agentic / Science Shield" dampener to prevent false positives in math-heavy repos.

**Step B: Calculate Total Threat Mass**
$$TotalMass = (ObfuscationMass + IntentMass) \times ArchetypeMultiplier$$

**Step C: The Biaxial Trojan Spike**
If the file blends in perfectly with the *global* repository but violates the *local* language physics (high local drift, low global drift), it is acting as a Trojan.
* If $\frac{LocalDrift}{GlobalDrift} > 1.5$, the $TotalMass$ is multiplied by that ratio.

**Step D: The Professionalism Quotient**
Malware authors rarely write 500 lines of meticulous JSDoc and `try/catch` blocks. We calculate a "Professionalism Dampener" based on safety and documentation hits to reduce the threat mass of highly engineered code.

**Step E: Sigmoid Mapping**
The final mass is divided by the file's LOC (with a heavy +150 Laplace padding) and mapped through the Sigmoid curve to output a 0-100 risk score.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

