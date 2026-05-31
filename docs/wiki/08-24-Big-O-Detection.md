# Algorithmic DoS & Big-O Detection

> **Metric: Algorithmic DoS & Data Gravity**
>
> **TL;DR:** Performance is no longer just a latency issue; it is a critical security perimeter. A standalone $O(N^3)$ loop calculating math offline is harmless. But that exact same $O(N^3)$ loop attached to a public API endpoint and a database query? That is a ticking Algorithmic Denial of Service (DoS) bomb. 
> 
> GitGalaxy abandons flat volumetric counting in favor of an **N-Dimensional Physics Equation**. We evaluate the mathematical depth of your logic and multiply it by its "Data Gravity" and network exposure.
>
> **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.
> * 🟦 **VERY LOW (Score 0-19):** Linear $O(N)$ execution or safely shielded streams.
> * 🟨 **INTERMEDIATE (Score 40-59):** Moderate. $O(N^2)$ logic that is mostly isolated or well-guarded by safety bailouts.
> * 🟥 **VERY HIGH (Score 80-100+):** Asymmetrical Threat. Recursive $O(2^N)$ or $O(N^3)$ loops directly wired into unauthenticated APIs or state-mutating database calls.

## The Philosophy: The Asymmetrical Attack Surface (CTO Pitch)

Traditional SAST tools fail to catch algorithmic vulnerabilities because they are designed to grep for known CVEs or hardcoded secrets. But an Algorithmic DoS isn't a CVE—it is a structural reality of your architecture. 

A healthy engineering culture admits that human working memory is a finite resource. Similarly, we must acknowledge that CPU threads and RAM are finite biological-equivalent bottlenecks for your infrastructure. If an attacker discovers an unprotected $O(N^4)$ function, they don't need a botnet to take down your servers. A single, well-crafted malicious payload can trap your core processing threads in infinite loops, starving your system of resources and resulting in a catastrophic outage. 

GitGalaxy maps the "syntactic physics" of your codebase to identify where exponential complexity collides with public exposure. By surfacing these asymmetrical attack surfaces deterministically, we empower teams to secure their architecture *before* it reaches production.

## The Inputs: Variables of the Algorithmic Engine

We calculate the physical threat of a function by measuring its depth, its environment, and its structural defenses.

| Variable | Metric Focus | Multiplier | Human Translation |
| :--- | :--- | :--- | :--- |
| `big_o_depth` | Algorithmic Depth | Exponential | Evaluates nesting. $O(N)$ is ignored. $O(N^2)$, $O(N^3)$, and recursive $O(2^N)$ trigger exponential threat scaling. |
| `api` / `io` | Choke Points | Additive | Functions exposed to network requests or I/O act as weaponizable triggers. |
| `db_complexity` | Data Gravity | Additive | Heavy iteration paired with ORM/SQL queries generates severe database locking risks. |
| `flux` | State Mutation | Additive | Mutating variables inside heavy loops quickly leads to Out of Memory (OOM) bombs. |
| `safety` / `bailout` | The Guardrails | 0.5x (Dampener) | Break statements, return limits, and try/catch blocks act as structural circuit breakers, slicing the risk in half. |
| `lazy_evaluation` | OOM Shield | 0.5x (Dampener) | Generators and streams process data in $O(1)$ memory, neutralizing state flux threats. |

## Universal Framework Integration

As with all core physics calculations, the DoS engine is deeply integrated with the ecosystem context:
* **Network Popularity (Blast Radius):** An $O(N^3)$ loop in a globally imported "God Node" multiplies the threat across the entire repository. If the function is an orphaned utility with no inbound network edges, the risk is heavily dampened.
* **Agentic / Hardware Shields:** Physics engine mitigations are dynamically applied. If the complex execution is occurring within a closed-loop native hardware bridge or a deterministic ML pipeline, standard Web-DoS math is scaled back.

## The Mathematics: The Density of Complexity

We use a Logistic Function (Sigmoid) tuned to be forgiving of moderate complexity but demanding of high complexity.

**Step A: The Base Threat**
We evaluate the structural depth. Anything below $O(N^2)$ is safely ignored.
$$BaseThreat=BigODepth^2$$

**Step B: The Asymmetrical Amplifiers (Data Gravity & Choke Points)**
We calculate the environmental multipliers. A deep loop is only dangerous if it interacts with external state or heavy data limits.
$$ChokeMultiplier=1.0+APIHits+IOHits+FluxHits$$
$$GravityMultiplier=1.0+(DBComplexity\times0.5)$$
$$ThreatMass=BaseThreat\times ChokeMultiplier\times GravityMultiplier$$

**Step C: Structural Dampeners (The Circuit Breakers)**
If the engine detects safety bailouts (`break`, `return`, `limit`) or lazy evaluation (generators), the mass is structurally mitigated.
$$MitigatedMass=ThreatMass\times0.5$$

**Step D: The Sigmoid Clamp**
We normalize the final mass against the physical lines of code to find the structural density, then map it to the GitGalaxy 0-100 spectrum.
$$Density=\left(\frac{MitigatedMass}{\max(LOC+150,\ 1)}\right)\times100.0$$
$$FinalRisk=\frac{100.0}{1+e^{-0.3\times(Density-15.0)}}$$

---

## Implementation (Python Reference)

```python
import math
from typing import Dict, List, Any

def _calc_algorithmic_dos(
    self,
    loc: int,
    eq: Dict[str, int],
    mp: float,
    functions: List[Dict[str, Any]],
    popularity: int,
) -> float:
    if not functions:
        return 0.0

    dos_mass = 0.0

    for func in functions:
        depth = func.get("big_o_depth", 1)
        # 1. Ignore O(N) linear loops
        if depth < 2:
            continue

        # 2. Base Threat (Exponential decay of performance)
        func_threat = float(depth**2)

        # 3. Data Gravity & Network Choke Points
        db_complex = func.get("db_complexity", 0)
        if db_complex > 0:
            func_threat *= 1.0 + (db_complex * 0.5)

        hv = func.get("hit_vector", {})
        choke_multiplier = 1.0 + hv.get("api", 0) + hv.get("io", 0) + hv.get("flux", 0)
        func_threat *= choke_multiplier

        # 4. Structural Dampeners (Guardrails)
        safety_hits = hv.get("safety", 0) + hv.get("bailout_hits", 0)
        if safety_hits > 0:
            func_threat *= 0.5  # 50% reduction for bounded iteration

        dos_mass += func_threat

    if dos_mass == 0.0:
        return 0.0

    # 5. Network Posture (Blast Radius)
    network_multiplier = 1.0
    if popularity == 0 and eq.get("api", 0) == 0:
        network_multiplier = 0.10  # Safely isolated orphan
    elif popularity > 0:
        network_multiplier = min(1.0 + (math.log1p(popularity) / 5.0), 3.0)

    total_threat_mass = dos_mass * network_multiplier

    # 6. The Sigmoid Curve
    t = self.risk_tuning.get("algorithmic_dos", {})
    density = (total_threat_mass / max(loc + t.get("loc_padding", 150), 1)) * 100.0
    
    threshold = t.get("threshold_base", 15.0)
    
    try:
        score = 100.0 / (1.0 + math.exp(-t.get("sigmoid_slope", 0.3) * (density - threshold)))
    except OverflowError:
        score = 100.0 if density > threshold else 0.0

    return min(score * mp, 100.0)
```

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🧠 **[Deep Dive into the Physics Source Code](https://github.com/squid-protocol/gitgalaxy/tree/main/gitgalaxy/physics)** to see the math in action.
* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

---

**[⬅️ Back to Master Index](index.md)**