# Documentation Risk Exposure

> **Metric: Density of Intent (Sigmoid Debt)**
>
> **Summary:** Visualizes the "Duty of Care" a developer owes to their future self and the collective within the knowledge graph. This metric does not reward the raw volume of text; it measures the **Density of Intent**. We distinguish between "Library-Grade" engineering—where a component is supported by structured metadata—and "Silent Logic," which requires the reader to perform manual mental compilation to understand the *why* behind the *what*.
>
> **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.
> * 🟦 **VERY LOW (Score 0-19):** Thorough. Saturated map. Perfect coverage with high intent density.
> * 🟨 **INTERMEDIATE (Score 40-59):** Moderate. Functional baseline. Meets standard safety thresholds.
> * 🟥 **VERY HIGH (Score 80-100):** Undocumented. Total Opacity. Zero intent density, representing high maintenance risk.

## The Inputs (Tiered Efficiency)

The heuristic scanning has been decoupled from the core deterministic engine. The analysis engine pre-calculates documentation lines and structured hits, passing them into the Signal Processor.

| Variable | Weight | Value | Structural Definition |
| :--- | :--- | :--- | :--- |
| `doc_hits` | 1.0x | **High** | **Tier 1 (The Interface).** Gold standard tags (`@param`, `///`). One hit provides a full point of intent density. |
| `ownership_hits` | 0.5x | **Medium** | **Tier 2 (The Metadata).** Attribution and file-level summaries. Valuable context, but less critical for line-by-line logic comprehension. |
| `doc_loc` | 0.33x | **Low** | **Tier 3 (The Narrative).** General inline comments. Requires 3 lines of text to equal 1 structured tag, honoring effort but demanding volume. |

## Universal Framework Integration

* **$Fc$ (Fidelity Coefficient):** Applied to the final risk reduction. We trust documentation in Explicit languages (e.g., Rust) more than in Implicit languages (e.g., Shell), where comments are prone to "drifting" from the actual logic.
* **$Irc$ (Implicit Risk Correction):** Applied to the Threshold. Implicit languages require a higher "Opacity Tax." They need more documentation density just to reach a baseline safety level.
* **$Mp$ (Path Modifier):** * *Public/API ($Mp = 1.5$):* High Bar. This is the face of the system. Lack of docs here is punished more severely.
  * *Tests/Experiments ($Mp = 0.5$):* Low Bar. Internal logic is more "forgiven" for being silent.

## The Equation: The Dynamic Risk Sigmoid

We calculate the density of intent and map it to a "Debt Curve" where the score represents the Exposure caused by missing documentation.

**Step A: The Micro-Bypass**
Tiny scripts ($\le 2$ lines of code) with $0$ documentation are automatically granted a $0.0$ risk score. A one-line utility function does not require a map.

**Step B: Calculate Intent Density**
We sum the weighted points and normalize them against the file size ($LOC$). A 1,000-line file requires significantly more intent-signaling than a 10-line utility.

$$WeightedPoints = (doc\_hits \times 1.0) + (ownership\_hits \times 0.5) + (doc\_loc \times 0.33)$$
$$Density = \left( \frac{WeightedPoints}{LOC} \right) \times 100.0$$

**Step C: Determine The Risk Threshold (The Bar)**
We calculate the "Tipping Point" where a file transitions from "Well-Documented" to "High Risk." We add the Implicit Risk Correction ($Irc$) and multiply by the Path Modifier ($Mp$).

$$Threshold = (BaseThreshold + Irc) \times Mp$$

**Step D: The Risk Sigmoid Map**
We use a sigmoid with a positive exponent. As Documentation Density increases, the denominator grows, causing the Risk Score to mathematically decrease.

$$RawRisk = \frac{100.0}{1 + e^{0.2 \times (Density - Threshold)}}$$

**Step E: Fidelity Trust Multiplier**
Finally, we apply the Fidelity Coefficient ($Fc$). Low-fidelity languages suffer an inverted trust multiplier, acknowledging that comments in those languages are more prone to drifting from reality.

$$FinalRisk = \min(RawRisk \times (2.0 - Fc), 100.0)$$

## Implementation (Python Reference)

```python
import math
from typing import Dict

def _calc_documentation(self, loc: int, doc_loc: int, eq: Dict[str, int], fc: float, irc: int, mp: float) -> float:
    t = self.risk_tuning.get("documentation", {})
    
    # Step B: Calculate Intent Density
    weighted_points = (eq.get("doc", 0) * t.get("doc_weight", 1.0)) + \
                      (eq.get("ownership", 0) * t.get("ownership_weight", 0.5)) + \
                      (doc_loc * t.get("doc_loc_weight", 0.33))
    density = (weighted_points / loc) * 100.0
    
    # Step A: Micro-bypass for tiny utilities
    if loc <= 2 and doc_loc == 0:
        return 0.0
        
    # Step C: Dynamic Threshold
    threshold = (t.get("threshold_base", 10.0) + irc) * mp
    
    # Step D: Sigmoid Map
    try:
        raw_risk = 100.0 / (1.0 + math.exp(t.get("sigmoid_slope", 0.2) * (density - threshold)))
    except OverflowError:
        raw_risk = 0.0 if density > threshold else 100.0
        
    # Step E: Fidelity Trust Multiplier
    return min(raw_risk * (2.0 - fc), 100.0)

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
