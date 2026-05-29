# 2.1.D. Satellite Unit

> **Metric: Function Declaration (e.g., `function`, `=>`, `def`, class method)**
>
> **Purpose:** Represents a discrete unit of logic—a "Tool"—contained within the file (the Toolbox). 
>
> **Why:** Files are rarely monolithic blocks of text; they are collections of distinct functions. We visualize these as moons orbiting the planet to show the granularity and inventory of the file at a glance. 
>
> **Effect:** Spawns a small spherical geometry orbiting the central parent.

## 2.1.D.1. The Philosophy: The Toolkit

We treat the file as a container.

* **The Star:** The Box (Class/Module).
* **The Satellites:** The Tools (Functions/Methods). 

A star with no moons is likely a static data configuration. A star with 50 moons is a heavy utility class with many diverse tools.

## 2.1.D.2. The Inputs: Identification

* **Regex Hits:** `function`, `=>`, `def`, `func`, etc.
* **Cap:** ~12 satellites (To prevent rendering swarming clouds of visual noise, we visualize a representative sample of the heaviest functions).

## 2.1.D.3. Basal Values (The Standard Model)

Every satellite begins with these default physical properties before other metrics (like complexity or churn) warp them:

| Property | Default Value | Visual Purpose |
| :--- | :--- | :--- |
| **Geometry** | `SphereGeometry(2, 4, 4)` | Renders as a low-poly "Moon". |
| **Radius** | 2 Units | Keeps the satellite fixed and small. |
| **Color** | Inherits Parent | Maintains visual cohesion with the central star. |
| **Opacity** | 0.8 | Slightly ghosted to indicate subservience to the parent. |
| **Orbit** | Basal Speed | Rotates uniformly around the parent unless modified by "Heat" metrics. |

## 2.1.D.4. The Function Impact Score

Not all moons are equal. A one-line "getter" is a pebble; a 500-line algorithm is a massive moon. To ensure the visualization is honest, we calculate an Impact Score for every function found. This score determines which 12 satellites are actually rendered (we always show the heaviest) and how "large" they appear.

**The Logic:** We combine Complexity (Branches), Connectivity (Arguments), and Volume (Lines of Code) into a single weight metric.

$$\text{Impact Score} = \left( (\text{BranchHits} + 1) \times (\text{Args} + 1) + (0.05 \times \text{LOC}) \right) \times 10$$

**The Variables:**
* **BranchHits:** The density of decision making inside the function.
* **Args:** The weight of inputs and coupling.
* **LOC:** The physical length of the function (scaled down by $0.05$ to prioritize logic over verbosity).
* **Multiplier (10):** Scales the integer up for storage efficiency in vectorized formats.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
