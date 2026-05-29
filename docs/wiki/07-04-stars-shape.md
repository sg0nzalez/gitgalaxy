# 2.1.C. Star's Shape

> **Metric: Control Flow Ratio ($R_L$)**
>
> **Purpose:** Give every star a distinctive silhouette that communicates the "State of Matter" of the code.
>
> **Why:** A file isn't just a size; it has a temperament. Declarative code (like a list of variables) is stable and solid. Algorithmic code (like a sorting method) is energetic and sharp. Without this variance, the galaxy looks like a generic ball field. By morphing the shape, we allow developers to "feel" the difference between a config file and a logic core without reading a single character.
>
> **Effect:** Transitions the central mesh through five distinct geometric tiers.

## 2.1.C.1. The Philosophy: Smooth vs. Sharp

Code does two things: it either **computes** (makes decisions) or it **declares** (defines structures). We categorize this into "Phases of Matter" based on its decision-making density, and we visualize this tension physically. 

* **Organic / Defining (The Structure):** *"Let X equal 5."* This is flat, linear, and stable. It represents the memory of the system. Passive code that defines things feels safe and "round."
* **Crystalline / Computing (The Logic):** *"If X happens, do Y."* This is jagged, non-linear, and energetic. It represents the thinking brain. Active code that decides things feels sharp and "dangerous."

A file that "thinks" a lot (algorithms) looks sharp and aggressive. A file that "remembers" a lot (configs, interfaces) has softer angles.

## 2.1.C.2. The Inputs: The Buckets

The scanner separates every regex hit into one of two buckets:

**A. Branch Hits (The Logic)**
* **Concept:** Points where execution splits. High counts mean the code is constantly changing direction.
* **Variables Used:** `BranchHits` (from scanner).
* **Triggers:** `if`, `else`, `switch`, `case`, `for`, `while`, `catch`, `&&`, `||`, ternary `?`.

**B. Linear Hits (The Structure)**
* **Concept:** Points where execution flows straight or data is defined. High counts mean the code is describing *what* things are, not *doing* things.
* **Variables Used:** `LinearHits` (from scanner).
* **Triggers:** `const`, `let`, `return`, `import`, `export`, `class`, `interface`, `type`.

## 2.1.C.3. The Equation: Calculating the Ratio

We calculate the **Control Flow Ratio ($R_L$)** as the percentage of relevant code that is dedicated to branching.

**Step 1: Summation** We find the total "Semantic Mass" of the file.

$$\text{TotalFlow} = \text{BranchHits} + \text{LinearHits}$$

**Step 2: Ratio Calculation** We divide the branching logic by the total mass to find the ratio.

$$R_L = \frac{\text{BranchHits}}{\text{TotalFlow}}$$

* **Result 0.0:** Pure Structure (e.g., a JSON file or TS Interface).
* **Result 0.5:** Balanced code (Standard business logic).
* **Result 1.0:** Pure Logic (e.g., a complex regex parser or math utility).

## 2.1.C.4. The 5-Tier Morphing Thresholds

The engine selects a `BufferGeometry` based on the following thresholds:

| Control Flow Ratio ($R_L$) | Geometry Type | Visual Style | Human Translation |
| :--- | :--- | :--- | :--- |
| **0.0 - 0.59** | **Sphere** | Glowing Orb | "The Seed": Pure data or metadata. |
| **0.60 - 0.69** | **Icosahedron** | 20-sided Glowing Wireframe | Mostly declarative/classes. |
| **0.70 - 0.79** | **Dodecahedron** | 12-sided Glowing Wireframe | Balanced business logic. |
| **0.80 - 0.89** | **Octahedron** | 8-sided Glowing Wireframe | Highly algorithmic/complex. |
| **0.90 - 1.0** | **Tetrahedron** | 4-sided Glowing Wireframe | Pure logic/Recursion. |

> **Note on Matrix Optimization:** For wireframe-only modes (like "The Matrix" theme), the Sphere primitive in the 0.0-0.59 range should be replaced with an Icosidodecahedron (32 faces — a Buckyball!).

## 2.1.C.5. The Visual Enhancements (Wireframe Logic)

To emphasize the "Digital" nature of high-logic code, the rendering style shifts as the shape sharpens:

* **The Low Tier (Sphere):** Rendered with a solid, emissive material. It feels like a glowing planet with soft, volumetric light.
* **The High Tiers (Icosahedron $\rightarrow$ Tetrahedron):** Rendered as Glow Wireframes. We expose the edges and facets, making the star look like a flickering vector projection. As the control flow ratio increases, the wireframe density thins out, making the final Tetrahedron look like **a lethal, minimalist pyramid of pure calculation**.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
