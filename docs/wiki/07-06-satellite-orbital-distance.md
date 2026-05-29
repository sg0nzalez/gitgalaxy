# 2.1.E. Satellite Orbital Distance

> **Metric: Lines of Code (LOC) in a specific function.**
>
> **Purpose:** Visually separate functions by their physical volume to identify bloated methods at a glance.
>
> **Effect:** The bigger the function, the further the satellite orbits from the central star. 
> 
> **Visual Output:** Modulates the 3D distance of the orbiting satellite from the core (Orbital Radius).

## 2.1.E.1. The Logic: Logarithmic Scaling

We need to visually differentiate between small helper functions (10 lines), large algorithms (1,000 lines), and massive legacy functions (100,000 lines). 

If we mapped distance linearly, massive functions would push their satellites infinitely off the screen, breaking the camera viewport. By applying a Logarithmic Scale, we compress the vast difference in line counts into a manageable physical space. A 100,000-line function is visually distant and imposing, but it remains anchored within the local star system.

## 2.1.E.2. The Equation

We establish a base distance (60 units) so satellites don't clip into the parent star's mesh, and then add the log-scaled line count multiplied by a spread factor (30).

$$\text{Orbital Radius} = 60 + \left( \log_2(\max(\text{LOC}, 1)) \times 30 \right)$$

## 2.1.E.3. The Scaling Examples

This equation produces a clean, readable spread of satellites based on their exact length:

| Lines of Code (LOC) | Orbital Radius | Visual Representation |
| :--- | :--- | :--- |
| **10 LOC** | ~160 units | **Visible Stub:** Hugs the parent star closely. |
| **100 LOC** | ~260 units | **Standard Branch:** A normal, healthy distance. |
| **1,000 LOC** | ~360 units | **Major Limb:** A noticeably distant, heavy function. |
| **100,000 LOC** | ~560 units | **Megastructure Reach:** Pushed to the far edges of the local system. |

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
