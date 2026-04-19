# Specification Alignment Exposure
# Specification Alignment Exposure

> **Metric: Architectural Traceability (Specs vs. Entities)**
>
> **Summary:** Visualizes the gap between executable logic and formal documentation. Specification Alignment measures how many of your functional entities (Classes and Functions) are explicitly tied back to architectural specs, RFCs, or formal audits. 
>
> **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.
> * 🟦 **VERY LOW (Score 0-19):** Fully Traceable. Almost every entity maps to a formal spec.
> * 🟨 **MODERATE (Score 40-59):** Partial Traceability. Some logic is formally documented, while the rest is ad-hoc.
> * 🟥 **VERY HIGH (Score 80-100):** Rogue Logic. The module executes heavily without any ties to a formal specification.

## The Equation: Inverse Ratio Mapping

We calculate the direct ratio of specification markers to total logic entities. Because this is an *Exposure* metric, a high ratio of specifications results in a low risk score.

**Step A: Define the Entities**
We sum the total number of structural blocks in the file.
$$Entities = \max(func\_start + class\_start, 1)$$

**Step B: Calculate the Traceability Ratio**
We divide the `spec_exposure` hits by the total entities, clamping at 1.0.
$$Ratio = \min\left(\frac{spec\_exposure}{Entities}, 1.0\right)$$

**Step C: Invert for Risk Exposure**
We subtract the ratio from 1.0, multiply by 100, and apply the Path Modifier ($Mp$). 
$$Exposure = \min((1.0 - Ratio) \times 100.0 \times Mp, 100.0)$$