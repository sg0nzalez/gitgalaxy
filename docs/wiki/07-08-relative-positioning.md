# 2.1.G. Satellite's Relative Positioning in a Unit

> **Metric: Control Flow Ratio ($R_L$)**
>
> **Purpose:** Give every function (satellite cluster) a distinctive spatial arrangement based on its ratio of logical statements to declarative statements.
>
> **Why:** A uniform galaxy is not only boring and repetitive to look at, but it also wastes a dimension of data communication. By altering the layout, we allow the user to instantly recognize the behavioral pattern of a function based purely on the geometric shape of its satellite cluster.
>
> **Effect:** Alters the angular arrangement of satellites in 3D space.

## 2.1.G.1. The Philosophy: Thinking vs. Speaking

Code does two things: it either **computes** (makes decisions) or it **declares** (defines structures). We visualize this tension physically in how the satellites arrange themselves around the parent.

* **Computing (Logic):** "If X happens, do Y." This represents the thinking brain. Functions that "think" a lot (heavy algorithms) arrange their satellites in jagged, non-linear, and energetic patterns.
* **Defining (Structure):** "Let X equal 5." This represents the memory of the system. Functions that "remember" a lot (configs, interfaces) arrange their satellites in flat, linear, and stable patterns.

## 2.1.G.2. The Visual Translation (The Lerp)

We map the abstract Control Flow Ratio ($R_L$) to physical 3D angles using **Linear Interpolation (Lerp)**. 

To calculate the divergence angle between satellites, we interpolate between a minimum sharp angle ($22.5^\circ$) and a maximum right angle ($90^\circ$), driven by the inverse of the logic ratio.

$$\text{Angle} = 22.5^\circ + \left( (1.0 - R_L) \times (90^\circ - 22.5^\circ) \right)$$

## 2.1.G.3. The Structural Archetypes

These calculated angles are then used to build the final 3D position of the satellites, resulting in two distinct visual extremes:

| Control Flow ($R_L$) | Divergence Angle | Visual Style | Spatial Arrangement |
| :--- | :--- | :--- | :--- |
| **High Logic** ($R_L \approx 1.0$) | $\approx 22.5^\circ$ | **"The Lightning Bolt"** | Branches diverge sharply. The satellites cluster in aggressive, jagged, tight formations indicating heavy algorithmic routing. |
| **High Structure** ($R_L \approx 0.0$) | $\approx 90.0^\circ$ | **"The Circuit Board"** | Branches diverge at perfect right angles. The satellites form a clean, highly organized grid indicating stable, declarative data. |
