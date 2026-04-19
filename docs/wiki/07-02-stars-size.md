# 2.1.A. Star's Size

> **Purpose: Visualize the sheer "Gravitational Weight" of a file within the system.**
>
> In a galaxy, size is the first thing you notice. But in software, "length" does not always equal "weight." A 200-line configuration file is light, while a 50-line recursive algorithm is heavy. By calculating mass based on complexity, risk, and volume, we ensure that the most impactful files—the ones that are hard to read, dangerous to touch, or heavily connected—physically dominate the screen as super-massive suns. Size instantly communicates structural importance.

## 2.1.A.1. The Philosophy: Physical Presence

We treat code as physical matter, but we recognize that matter has different densities:

* **Low Density:** Simple data, linear lists, and standard config files. These are large but light, and easy to move.
* **High Density:** Complex branching logic, heavy arguments, and high-risk exposure. These are small but incredibly heavy, exerting high gravity.

By scaling the star's size based on this Composite Mass, we create a visual hierarchy where the true "Main Characters"—the complex logic engines—naturally anchor the sector, while simple helper files drift in the background.

## 2.1.A.2. The Inputs: Measuring Mass

The mass calculation ingests five distinct dimensions of code structure:

1. **Function Impact:** The complexity of every function inside the file.
2. **API Exposure:** How publicly visible the file is.
3. **Concurrency Exposure:** The density of asynchronous/threading logic.
4. **State Flux Exposure:** The density of variable mutation.
5. **Lines of Code (LOC):** The raw physical volume (scaled down to act as a base substrate).

## 2.1.A.3. The Equation: Structural Mass & Visual Radius

We utilize a multi-stage summation to determine the raw mass. Complexity multiplies; volume merely adds. We then apply a logarithmic clamp to determine the final visual radius, ensuring that massive "God Objects" are distinct but do not consume the entire viewport.

**Step 1: Calculate Function Impact**
For every function in the file, we calculate an impact score based on its decision density (Branches), connectivity (Args), and length.

$$\text{Function Impact} = \left( (\text{BranchHits} + 1) \times (\text{Args} + 1) + (0.05 \times \text{LOC}) \right) \times 10$$

**Step 2: Calculate Total Mass (The Raw Metric)**
The file's final mass is the sum of its functions plus its system-wide risk exposures.

$$\text{Total Mass} = \sum(\text{Function Impacts}) + \text{API} + \text{Concurrency} + \text{Flux} + \left( \frac{\text{LOC}}{50} \right)$$

**Step 3: Calculate Visual Radius (The Render Size)**
We apply a base-2 logarithm to compress the massive range of weights (10 to 1,000,000) into a renderable scale (10 to 50 units).

$$\text{Radius} = 10 + \left( \log_2(\max(\text{Total Mass}, 1)) \times 2 \right)$$

## 2.1.A.4. The Visual Thresholds (The Scale)

| Classification | Mass Range | Visual Radius | Description |
| :--- | :--- | :--- | :--- |
| **The Asteroid** | < 100 | ~16 units | Simple DTOs, interfaces, or small configs. Nimble, low-gravity rocks that drift in the periphery. |
| **The Planet** | 100 - 1,000 | ~20 to 26 units | Standard business logic. Visible, stable, but not overwhelming. The "Middle Class" of the galaxy. |
| **The Star** | 1,000 - 20,000 | ~27 to 38 units | Core utilities, major controllers, or complex engines. These anchor local clusters and exert visible gravity. |
| **The Super-Giant** | 20,000+ | ~40+ units | "God Objects," massive reducers, or legacy core files. These dominate the screen, signaling extreme structural density. |

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

