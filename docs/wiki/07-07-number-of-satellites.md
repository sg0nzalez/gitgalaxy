# 2.1.F. Number of Satellites in a Unit

> **Metric: Extended Cyclomatic Complexity**
>
> **Purpose:** Visualizes the "Knotty" nature of logic. High cognitive load manifests as dense, recursive fractals or clusters of satellites.
> 
> **Input:** $C$ (Composite Complexity Score).
> 
> **Effect:** Modulates the number of satellites (moons) within a specific function unit in 3D space.

## 2.1.F.1. The Philosophy: Cognitive Friction

Computers don't care about `try/catch` blocks or nested `if` statements; they execute them in nanoseconds. Humans, however, have limited working memory. Every time a developer reads an `if`, a loop, or an error handler, they have to "fork" their mental model of what the code is doing. We call this Cognitive Friction.

In GitGalaxy, we visualize this friction physically. A simple, linear script grows like a straight bamboo shoot. A complex, defensive, branching function grows like a dense, thorny thicket.

## 2.1.F.2. The Inputs: Anatomy of Complexity

To calculate this, we look at two distinct types of code patterns found by the scanner:

**A. Structural Complexity (The Skeleton)**
* **What it is:** The actual decision points in the logic. Each of these represents a split in reality ("If X is true, go left; otherwise, go right."). Too many splits make the path impossible to follow.
* **Variables Used:** `BranchHits` (from scanner).
* **Triggers:** `if`, `else`, `for`, `while`, `switch`, logical operators (`&&`, `||`), and ternaries (`?`).

**B. Defensive Overhead (The Armor)**
* **What it is:** Code written to protect against failure, not to perform the primary task. While safety is good, it creates visual noise. A function wrapped in three layers of error handling is structurally denser than one that just does the math.
* **Variables Used:** `SafetyHits`.
* **Triggers:** `try`, `catch`, `finally`, `assert`, `guard`, `validate`.

## 2.1.F.3. The Equation: Calculating the Composite Score (C)

We calculate the **Composite Complexity Score ($C$)** using a weighted sum. We weight defensive overhead at 50% because two safety checks consume about as much "mental space" as one actual logic branch. This prevents well-protected code from looking unfairly spaghetti-like while acknowledging it is still denser than unsafe code.

**Step 1: Count the Branches (The Skeleton)**
$$\text{Structural} = \text{BranchHits}$$

**Step 2: Weigh the Armor (The Defense)**
$$\text{Defensive} = \text{SafetyHits} \times 0.5$$

**Step 3: Summation**
$$C = \text{Structural} + \text{Defensive}$$

## 2.1.F.4. The Visual Thresholds (Fractal Depth)

We map the abstract number $C$ to a physical **Fractal Depth**. This determines how many times the geometry splits or how many moons orbit the planet.

| Complexity ($C$) | Fractal Depth | Classification | Visual Mapping | Code Characteristic |
| :--- | :--- | :--- | :--- | :--- |
| **$\le 2$** | **0** | **The Bamboo** | A single planet with 0-1 moons (A line). | A simple list of instructions. Do A, then B, then C. |
| **> 2** | **1** | **The Fork** | The unit splits once. | A basic function with one or two checks. |
| **> 8** | **2** | **The Tree** | Distinct branching structure (3-4 moons). | Standard business logic. Loops inside conditions. |
| **> 15** | **3** | **The Thicket** | Dense, aggressive branching (A swarm of moons). | Complex algorithms, state machines, or legacy parsers. |
| **> 25** | **4** | **The Jungle** | Chaotic fractal explosion (Solid with branches). | "God Objects," massive switch statements, or deep recursion. |

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

