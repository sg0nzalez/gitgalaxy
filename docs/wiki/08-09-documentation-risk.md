# Documentation Risk Exposure

> **Metric: N-Dimensional Knowledge Debt**
>
> **TL;DR:** Counting lines of comments is an archaic metric. A 20-line utility function converting Celsius to Fahrenheit doesn’t need a sprawling docstring. But an $O(N^3)$ orchestrator function that mutates the global database state and has 45 inbound network dependencies? If that lacks documentation, it is a catastrophic vulnerability. 
> 
> GitGalaxy abandons flat volumetric counting in favor of an **N-Dimensional Physics Equation**. We weigh the *gravitational mass of undocumented logic* against *architectural knowledge shields*, amplifying the risk based on the file's network blast radius and developer silo risk.
>
> **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.
> * 🟦 **VERY LOW (Score 0-19):** Fully shielded. The file is highly documented or lives under a strong architectural markdown umbrella.
> * 🟨 **INTERMEDIATE (Score 40-59):** Moderate. Standard logic with acceptable inline intent.
> * 🟥 **VERY HIGH (Score 80-100+):** Critical Blindness. Massive, highly-coupled, or siloed logic operating with zero human context.

## The 4 Pillars of Context-Aware Documentation Risk

GitGalaxy evaluates documentation through four interconnected dimensions, treating it as a true structural shield rather than a formatting requirement.

### 1. Kinetic Blindness (The Risk)
Instead of a flat penalty for missing docstrings, the engine measures the **exact physical mass** of undocumented logic. We sweep the file's structural satellites (functions/classes). If a function lacks a docstring, the engine evaluates its `impact` score and `big_o_depth`. An undocumented $O(N^3)$ monolithic state machine generates massive "Kinetic Blindness" risk, while an undocumented 5-line utility barely moves the needle. We penalize the *absence of intent on load-bearing structures*.

### 2. The GuideStar Umbrella (Contextual Defense)
Documentation doesn't just live inside source files. The `GuideStarLens` acts as an early-warning radar, sweeping directories for "Knowledge Anchors" (like `README.md` or `ARCHITECTURE.md`). If found, it projects a `doc_umbrella` defense shield over the entire directory. This mathematically forgives complex code for lacking inline comments if a massive architectural document sits right next to it.

### 3. Instructional Density (Markdown Optics)
Markdown is no longer treated as "Dark Matter." Markdown files flow through the optical regex engine to measure their **Instructional Density**. We actively count:
* `lit_code_blocks` (Instructional Proof)
* `lit_diagrams` (Architectural Proof like Mermaid/PlantUML)
* `lit_headers` (Structural Proof)
* `lit_links` (Navigational Proof)

A markdown file full of code examples and diagrams projects an exponentially stronger shield than a massive wall of auto-generated text.

### 4. Blast Radius & Bus Factor (The Multipliers)
We wire the `NetworkRiskSensor` and `Chronometer` directly into the documentation math.
* **Network Blast Radius:** If an undocumented file is an orphaned utility, the risk stays low. If it is a "God Node" imported by 50 other files, the documentation risk is exponentially amplified.
* **Silo Risk (Bus Factor):** If a volatile, undocumented file is written 95% by a single author, the risk multiplies again. The engine mathematically flags: *"If this one developer quits, the company loses the entire context of this load-bearing architecture."*

---

## Universal Framework Integration

As with all GitGalaxy physics, documentation risk is governed by the Universal Trust Matrix:
* **$Fc$ (Fidelity Coefficient):** We trust documentation in Explicit languages (e.g., Rust, Java) more than in Implicit languages (e.g., Shell, Groovy), where comments are prone to "drifting" from the actual execution logic.
* **$Irc$ (Implicit Risk Correction):** Applied to the risk baseline. Implicit languages require a higher "Opacity Tax." They need more documentation density just to reach a baseline safety level.

---

## The Mathematics: The Density of Intent

**Step A: The Defense (The Knowledge Shield)**
We calculate the defensive mass by combining inline documentation, ownership tags, and the external `GuideStar` umbrella shield. The entire defense is then dampened by the language's Fidelity Coefficient ($Fc$).

$$UmbrellaDefense = doc\_umbrella \times 50.0$$
$$DefenseHits = (InlineDocs \times 1.0 + Ownership \times 0.5 + DocLOC \times 0.33 + UmbrellaDefense) \times Fc$$

**Step B: The Risk (Kinetic Blindness)**
We calculate the raw risk by identifying exposed public APIs and summing the mass of all undocumented, heavy logic blocks. The language's Opacity Tax ($Irc$) is appended as a baseline penalty.

$$KineticBlindness = \sum_{undocumented} \left( 5.0 + (\ln(Impact) \times (BigO \times 0.5)) \right)$$
$$RiskHits = KineticBlindness + (API\_Exposure \times 2.0) + Irc$$

**Step C: Net Exposure & Density**
We balance the Risk against the Defense and normalize it against the physical lines of code to find the overall density of vulnerability.

$$NetExposure = \max\left(0, RiskHits - \frac{DefenseHits}{2.0}\right)$$
$$Density = \left( \frac{NetExposure}{\max(LOC, 1)} \right) \times 100.0$$

**Step D: Systemic Multipliers**
We calculate the multipliers for the file's Network Popularity (Blast Radius) and Author Silo Risk (Bus Factor).

$$NetworkMultiplier = 1.0 + \left(\frac{Popularity}{10.0}\right)$$
$$SiloMultiplier = 1.0 + \left(\frac{SiloExposure}{200.0}\right)$$
$$FinalMultiplier = NetworkMultiplier \times SiloMultiplier \times Mp$$

**Step E: The Risk Sigmoid Map**
Because high density equals high risk, we use a sigmoid with a *negative* slope. Finally, we multiply the output by the Systemic Multipliers.

$$RawRisk = \frac{100.0}{1 + e^{-0.2 \times (Density - 10.0)}}$$
$$FinalRisk = \min(RawRisk \times FinalMultiplier, 100.0)$$

---

## Implementation (Python Reference)

```python
import math
from typing import Dict, List, Any

def _calc_documentation(
    self,
    loc: int,
    doc_loc: int,
    eq: Dict[str, int],
    fc: float,
    irc: int,
    mp: float,
    functions: List[Dict[str, Any]] = None,
    doc_umbrella: float = 0.0,
    popularity: int = 0,
    silo_exposure: float = 0.0
) -> float:
    t = self.risk_tuning.get("documentation", {})
    
    # 1. THE DEFENSE (The Knowledge Shield)
    umbrella_defense = doc_umbrella * 50.0 
    
    defense_hits = (
        (eq.get("doc", 0) * t.get("doc_weight", 1.0))
        + (eq.get("ownership", 0) * t.get("ownership_weight", 0.5))
        + (doc_loc * t.get("doc_loc_weight", 0.33))
        + umbrella_defense
    ) * fc
    
    # 2. THE RISK (Kinetic Blindness)
    kinetic_blindness = 0.0
    api_exposure = eq.get("api", 0) * 2.0
    
    if functions:
        for func in functions:
            impact = func.get("impact", 0.0)
            big_o = func.get("big_o_depth", 1)
            
            # If a load-bearing or deeply nested block lacks a semantic tether
            if (impact > 50.0 or big_o >= 3) and not func.get("docstring"):
                kinetic_blindness += 5.0 + (math.log1p(impact) * (big_o * 0.5))

    risk_hits = kinetic_blindness + api_exposure + irc

    # 3. UNIVERSAL DENSITY EQUATION
    net_exposure = max(0.0, risk_hits - (defense_hits / 2.0))
    density = (net_exposure / max(loc, 1)) * 100.0

    # 4. THE MULTIPLIERS (Blast Radius & Bus Factor)
    network_multiplier = 1.0 + (popularity / 10.0)
    silo_multiplier = 1.0 + (silo_exposure / 200.0)
    
    final_multiplier = network_multiplier * silo_multiplier * mp

    threshold = t.get("threshold_base", 10.0)
    
    # 5. SIGMOID CURVE
    try:
        raw_risk = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 0.2) * (density - threshold)))
    except OverflowError:
        raw_risk = 100.0 if density > threshold else 0.0

    return min(raw_risk * final_multiplier, 100.0)
```

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

---

**[⬅️ Back to Master Index](index.md)**