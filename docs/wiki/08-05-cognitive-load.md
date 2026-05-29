# Cognitive Load Exposure

> **Metric: Density of Decision-Making & Logic Tangledness**
>
> **Summary:** Visualizes the "Mental RAM" required to understand a file. Unlike Lines of Code (which measures physical volume), Cognitive Load measures the density of decision-making heuristics within the knowledge graph. A healthy engineering culture admits that human working memory is a finite resource. We recognize that complex problems often require complex solutions. We don't measure "Tangled Logic" to critique the necessity of the code, but to deterministically surface it so the team can be honest about which files require the most mental overhead. Surfacing these high-friction zones protects the team from burnout.
>
> **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum, scaling from 🟦 **Deep Blue** (linear, easy-to-read data) to 🟥 **Intense Red** (high-friction, multi-state async logic).

## The Philosophy: The Density of Understanding

Human working memory is a biological bottleneck. Every time a developer encounters a nested `if`, a complex ternary, or a manual memory management keyword, they must "cache" the current state in their brain. This represents the total Cognitive Load of a module.

In GitGalaxy, we treat code as a system where logic generates friction and documentation provides mitigation. By being honest about where the Cognitive Load is "hot," we move away from performance judgment and toward resource management. 

* **Low Cognitive Load:** Linear code that reads clearly; low impact on the developer's working memory.
* **High Cognitive Load:** Necessary but complex logic that requires the developer to simulate multiple realities simultaneously; identifies areas that require peak focus.

## The Inputs: Heuristic Stressors & Mitigations

We utilize the pre-calculated hits from the deterministic engine and weight them based on the "Mental Tax" they impose on the reader.

| Variable | Metric Focus | Multiplier | Clamp Limit | Human Translation |
| :--- | :--- | :--- | :--- | :--- |
| `branch_hits` | Decision Density | 1.0x | 0.5/line | The baseline of decision making (`if`/`else`). Clamped to prevent massive, flat switch-statements from breaking the math. |
| `flux_hits` | State Mutation | 2.0x | 0.75/line | Tracking variables changing values taxes short-term memory significantly more than static logic. |
| `concurrency_hits` | Temporal Complexity | 3.0x | None | Logic that jumps in time forces the reader to track non-linear execution. |
| `heat_triggers_hits`| Abstraction Penalty | 5.0x | None | Macros, reflection, and dynamic dispatch hide the true logic, forcing "mental compilation." |
| `danger_hits` | Anxiety | 5.0x | None | `eval` or unsafe code forces the brain into a slow, high-alert verification mode. |
| `doc_hits` | The Antidote | 10.0x | None | Structured documentation provides mental shortcuts, reducing the effective load (acts as a mitigating agent). |

## Universal Framework Integration

We apply the standard physics variables to ensure fairness across language families and environments:

* **$Irc$ (Implicit Risk Correction):** Added to the total density. Opaque languages (Shell, Perl) get a baseline complexity penalty because the syntax itself implies hidden logic.
* **$Fc$ (Fidelity Coefficient):** Applied to the mitigation factor. We trust documentation in explicit languages (Java) more than in implicit ones (Ruby) where comments might drift from reality.
* **$Mp$ (Path Modifier):** Utilized to allow contextual overrides. For example, highly complex mocking logic in a `tests/` directory may receive a reduction, as the cognitive expectations there differ from a production runtime core.

## The Equation: The Sigmoid Clamp

We use a Logistic Function (Sigmoid) tuned to be forgiving of moderate complexity but demanding of high complexity.

**Step A: Calculate Clamped Densities**
We calculate the per-line density of each stressor. Branch and Flux densities are clamped. A file with 5,000 lines of simple `case` statements shouldn't be flagged as high-friction just because of high raw branch counts.

**Step B: The Synergistic Sum**
We sum the clamped densities and heavy logic multipliers, then add the baseline opacity tax ($Irc$).

$$TotalDensity = ClampedBranch + ClampedFlux + HeavyLogic + \left(\frac{Irc}{LOC}\right)$$

**Step C: The Sigmoid Curve (The Base Score)**
We map the total density to a $0-100$ scale using a Sigmoid curve. 
* **Offset ($0.75$):** Pushes the "center" of the curve to the right. Code must have a high density ($0.75$ weighted points per line) just to reach a score of $50$.
* **Slope ($4.0$):** A moderate slope ensures a smooth transition rather than a sudden wall, allowing for nuance in the $50-80$ range.

$$RawScore = \frac{100}{1 + e^{-4.0 \times (TotalDensity - 0.75)}}$$

**Step D: The Mitigation Factor (The Antidote)**
Documentation reduces load, but never to zero. Complex logic is still complex, even if explained well. We cap the cooling effect at a maximum reduction of 50%, then apply the Path Modifier ($Mp$).

$$DocCoverage = \frac{doc\_hits \times 10.0}{LOC}$$
$$MitigationFactor = \max(0.5,\ 1.0 - (DocCoverage \times Fc))$$
$$FinalScore = \min(RawScore \times MitigationFactor \times Mp,\ 100)$$

## Visual Interpretation: The Cognitive Topology

| Score Range | Universal Color | Risk Label | Structural Reality |
| :--- | :--- | :--- | :--- |
| **0 - 19** | 🟦 **Deep Blue** | **VERY LOW** | Big JSON Configs. Zero branching. Minimal baseline density. |
| **20 - 39** | 🩵 **Cyan** | **LOW** | Standard UI Component. Normal complexity, easily held in working memory. |
| **40 - 59** | 🟨 **Yellow** | **INTERMEDIATE** | Complex Algorithm. Noticeable, but not alarming. The code is "doing work." |
| **60 - 89** | 🟧 **Orange** | **HIGH** | Heavy Logic Core. The Tipping Point. Heavy branching mixed with state flux. |
| **90 - 100** | 🟥 **Bright Red** | **VERY HIGH** | Extreme Meta-Programming. Dense clusters of async, reflection, and danger per line. |

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
