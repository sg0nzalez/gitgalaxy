# File Stability (Commit Heat)

> **Metric: Relative Temporal Distance (Geological Layers)**
>
> **Summary:** Visualizes the "Geological Layers" of the knowledge graph. Instead of measuring "Freshness" (which implies old code is bad/stale), we measure **Stability**. We use Auto-Scaling Normalization to scan the entire repository and find the absolute oldest and newest timestamps, creating a relative timeframe specific to that exact topology.
>
> **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.
> * 🟦 **HOT/NEW (Score 0-19):** The "Active Front." Code written or heavily modified very recently.
> * 🟨 **ACTIVE (Score 40-59):** Settled. Halfway down the repository's timeline.
> * 🟥 **ENDURING (Score 80-100):** The "Foundation." The oldest, most untouched files in the repository.

## The Inputs (File System)

We use **Auto-Scaling Normalization**. We scan the entire repository to find the absolute oldest and newest timestamps, creating a relative time-frame strictly for this specific project.

| Variable | Source | Unit | Structural Definition |
| :--- | :--- | :--- | :--- |
| `FileMTime` | `os.path.getmtime` | Epoch | The last modified timestamp of the specific file. |
| `RepoMinTime` | Calculated (Phase 1) | Epoch | The timestamp of the *oldest* file in the entire repo. |
| `RepoMaxTime` | Calculated (Phase 1) | Epoch | The timestamp of the *newest* file in the entire repo. |

## Universal Framework Integration

Stability is a pure temporal measurement. It is not a risk factor that requires structural dampening or context amplification.

* **$Fc$ (Fidelity Coefficient):** Not Applied. Time is absolute.
* **$Irc$ (Implicit Risk Correction):** Not Applied.
* **$Mp$ (Path Modifier):** Not Applied. The age of a file is a physical constant.

## The Equation: Relative Time Normalization

We define Stability as the "Distance from the Newest moment."

**Step A: Calculate Temporal Distance**
We subtract the file's last modified time (`mtime`) from the newest moment in the repository (`repo_max`). We clamp this difference to $0.0$ at a minimum to prevent negative time errors if a file's timestamp somehow drifts ahead of the global max during processing.

$$SecondsFromMax=\max(RepoMaxTime-FileMTime, 0.0)$$

**Step B: Calculate Relative Ratio**
We divide the file's temporal distance by the total time range of the repository. We enforce a minimum range of $1.0$ second to prevent division-by-zero crashes in brand-new or single-file repositories.

$$TimeRange=\max(RepoMaxTime-RepoMinTime, 1.0)$$
$$StabilityScore=\min\left( \left( \frac{SecondsFromMax}{TimeRange} \right) \times 100.0, 100.0 \right)$$

* If $FileTime == RepoMaxTime$ (Newest), the distance is $0$, so $StabilityScore = 0.0$.
* If $FileTime == RepoMinTime$ (Oldest), the distance equals the full range, so $StabilityScore = 100.0$.

## Implementation (Python Reference)

```python
import math
from typing import Dict, Any, Tuple

def _calc_raw_temporal_signals(self, temp: Dict[str, Any]) -> Tuple[float, float]:
    """Calculates Stability (Age) and Raw Churn (Seismic Frequency)."""
    if not temp or not temp.get("is_git_tracked", False):
        return 50.0, 0.0 

    mtime = temp.get("mtime", 0.0)
    repo_min = temp.get("repo_min_time", mtime)
    repo_max = temp.get("repo_max_time", mtime)
    commits = temp.get("commit_count", 0)

    # ---> THE FIX: Clamp the time difference so it never goes negative <---
    seconds_from_max = max(repo_max - mtime, 0.0)
    time_range = max(repo_max - repo_min, 1.0)

    # 1. Stability (0 = Newest/Surface, 100 = Oldest/Bedrock)
    stability_ratio = seconds_from_max / time_range
    stability_score = min(stability_ratio * 100.0, 100.0)

    # 2. Raw Churn Frequency (Calculated alongside stability)
    age_weeks = max(seconds_from_max / 604800.0, 1.0) 
    raw_churn_freq = commits / math.sqrt(age_weeks)

    return stability_score, raw_churn_freq

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

