# 2.1.I. Planetary Rings 

> **Metric: External Library Import Count**
>
> **Purpose:** See which files import external libraries.
>
> **Why:** Determine which files have dependencies that you don't fully control.
>
> **Effect:** Spawns rings around the file to visually represent its external dependency weight.

## 2.1.I.1. The Philosophy: The Gravity Well

A clean file is a sphere. It floats freely. A file with dependencies is tethered. The more it imports, the heavier it gets. We set a **High Threshold** for rings. We don't want visual noise for a single utility import. Rings are reserved strictly for "Heavy Lifters" and "Glue Code."

## 2.1.I.2. The Inputs: Measuring Dependencies

* **ImportHits:** The count of `import`, `require`, or `include` statements found by the scanner.
* **Threshold:** **> 5 Imports**. Anything less is considered "Standard Weight" and renders with **No Rings**.

## 2.1.I.3. The Equation: Growth and Density

Instead of complex accretion disks, we use a single, evolving ring system that grows in **Density (Opacity)** and **Mass (Width)** as the gravity increases.

**1. Opacity (Visibility)**
Ranges from $0.0$ to $0.6$ over the first 26 imports. Rare imports create a barely visible "Ghost Ring." As dependencies hit the critical mass (26), the ring becomes a distinct, semi-solid band.

$$\text{Opacity} = \min\left( \left(\frac{\text{ImportHits}}{26}\right) \times 0.6,\ 0.6 \right)$$

**2. Width (Tube Thickness)**
Grows continuously as imports increase. The ring gets physically thicker and wider, consuming more visual space around the planet as the gravity well deepens.

$$\text{TubeRadius} = \text{BaseWidth} + (\text{ImportHits} \times 0.1)$$

## 2.1.I.4. The Visual Output

* **Geometry:** `TorusGeometry`.
* **Tube Radius:** Scaled linearly by `ImportHits`.
* **Material:** Transparent with `opacity` capped at $0.6$.
* **Tilt:** Rings are tilted at randomized axes (Euler angles) to ensure they don't look like flat plates, but dynamic, gyroscope-like orbital paths.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
