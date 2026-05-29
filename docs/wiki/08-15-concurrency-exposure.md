# Concurrency Exposure

> **Metric: Temporal Static and Signal-to-Noise Ratio**
>
> **Summary:** Visualizes "Temporal Static" and the Signal-to-Noise Ratio within the knowledge graph. Concurrency is treated as "Information Static" because it fractures the linear execution timeline, increasing the cognitive load required to understand the file. The "Tiger in the Cage" rule applies here: We do not discount concurrency just because it lives in a "Worker" or "API" folder. A tiger in a cage is still dangerous. High concurrency is always high cognitive load and high risk, regardless of where it lives.
>
> **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.
> * 🟦 **LOW (Score 0-19):** Linear. The code executes sequentially (1, then 2, then 3). The signal is clear and stable.
> * 🟨 **MODERATE (Score 40-59):** Standard async operations. Minor temporal branching.
> * 🟥 **VERY HIGH (Score 80-100):** Noisy. The code manages multiple parallel timelines (Promises, threads, channels). The signal is highly fractured, warning that execution timing is non-deterministic.

## The Inputs (Temporal Markers)

We count the heuristics that "Fork" time.

| Variable | Regex Key | Weight | Structural Definition |
| :--- | :--- | :--- | :--- |
| `AsyncHits` | `concurrency` | **1.0x** | **The Fork.** Keywords that spawn or manage parallel execution: `async`, `await`, `Promise`, `thread`, `spawn`, `go`, `chan`, `synchronized`. |
| `LOC` | `meaningful_loc` | **Denominator** | We measure density. A 1,000-line file with 1 `await` is linear. A 10-line file with 5 `await`s is a temporal knot. |

## Universal Framework Integration

* **$Fc$ (Fidelity Coefficient):** **Not Applied.** Time is absolute.
* **$Irc$ (Implicit Risk Correction):** **Applied to Numerator (Dampened).** Implicit languages (JS, Python) hide race conditions better than explicit ones (Rust, Go). We add a small "Ghost Load" to density, but we scale it down ($Irc \times 0.1$) so it acts as a "Tie Breaker" rather than a false positive generator.
* **$Mp$ (Path Modifier):** **Applied to Threshold.**
  * *UI/Views ($Mp = 0.5$):* **Low Tolerance (High Scream).** Async logic in UI code is a primary source of bugs (race conditions, jank). We lower the bar so even minor concurrency glows here.
  * *Standard/Workers ($Mp = 1.0$):* **Standard Tolerance.** We do NOT discount workers. If a worker is complex, it should look complex.

## The Equation: The Tipping Point Sigmoid

Concurrency complexity is non-linear. A single `await` is standard. Ten `await` calls in a small function is a "Logic Tangle." We use a Sigmoid to create a visual "Tipping Point."

**Step A: Pre-Filter (The Zero Check)**
If the file contains **Zero** async hits, the score is $0.0$. No amount of implicit risk can turn synchronous code into concurrent code.

**Step B: Calculate Temporal Density**
We determine what percentage of the code is dedicated to managing time. We add a fraction of $Irc$ ($0.1\times$) to penalize implicit safety gaps without creating noise.

$$WeightedHits = AsyncHits + (Irc \times 0.1)$$
$$Density = \left( \frac{WeightedHits}{\max(LOC, 1)} \right) \times 100.0$$

**Step C: Determine The Threshold (The Breakdown)**
This is the density required to "Fracture" the signal. We start with a Base of $4.0$ (4% density), which provides a safe buffer for standard async patterns before triggering warnings.

$$Threshold = 4.0 \times Mp$$

**Step D: The Sigmoid Map**
We map density against the threshold using a moderately steep slope ($0.4$). Concurrency risk escalates quickly once it crosses the threshold.

$$RawScore = \frac{100.0}{1 + e^{-0.4 \times (Density - Threshold)}}$$
$$FinalScore = \min(RawScore, 100.0)$$

## Implementation (Python Reference)

```python
import math

def calculate_concurrency_exposure(self, hits_async, loc, irc, mp):
    """
    Calculates Concurrency Exposure (Temporal Static).
    Returns int 0-100.
    """
    # 1. Step A: Pre-Filter (Zero Check)
    if hits_async == 0:
        return 0

    # 2. Step B: Temporal Density
    # Scaled Irc (0.1x) prevents false positives in small files
    weighted_hits = hits_async + (irc * 0.1)
    density = (weighted_hits / max(loc, 1)) * 100

    # 3. Step C: Dynamic Threshold
    # Base = 4% density.
    # UI (Mp 0.5) -> Threshold 2.0%.
    # Workers/Standard (Mp 1.0) -> Threshold 4.0%.
    path_mod = mp.get('Concurrency Exposure', 1.0)
    threshold = 4.0 * path_mod

    # 4. Step D: Sigmoid Map
    try:
        raw_score = 100 / (1 + math.exp(-0.4 * (density - threshold)))
    except OverflowError:
        raw_score = 100 if density > threshold else 0

    return int(min(raw_score, 100))

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
