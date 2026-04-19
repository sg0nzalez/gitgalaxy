# 2.1.H. Node Size

> **Metric: Argument Count (Args)**
>
> **Purpose:** Visualizes the "State Heaviness" or I/O weight of a function.
>
> **Why:** Functions with many arguments often carry significant state or context. A clean utility usually takes 1-2 arguments, while a legacy handler might take 10. We visualize this physically to differentiate sleek tools from heavy machinery.
>
> **Effect:** Modulates the physical size (Scale) of the orbiting satellite.

## 2.1.H.1. The Philosophy: Heavy vs. Light

We view arguments as "Inputs" or "Cables" plugged into the function.

* **Lightweight (0-2 arguments):** Sharp, encapsulated, easy to move and test.
* **Heavyweight (5+ arguments):** Bloated, carrying too much context, and harder to maintain.

## 2.1.H.2. The Inputs: Measuring Args

* **Args:** The count of arguments in the function signature, as found by the scanner.
* **Range:** Typically $0$ to $20+$.

## 2.1.H.3. The Equation: Logarithmic Scaling

We use logarithmic scaling to prevent functions with many arguments (e.g., 20+) from spawning massive, screen-obscuring orbs. A linear scale would make them visually overwhelming. A logarithmic scale highlights the crucial difference between 0 and 5 arguments, but gently compresses the difference between 10 and 20.

$$\text{Scale} = 1.0 + \left( \log_2(\max(\text{Args}, 1)) \times 0.2 \right)$$

* **Base Scale:** $1.0$ (Standard Unit).
* **Factor:** $0.2$ (Gentle growth multiplier).

## 2.1.H.4. The Visual Output

This calculated scale directly modulates the 3D radius of the orbiting moon particles. 

| Argument Count | Calculated Scale | Visual Representation |
| :--- | :--- | :--- |
| **0 - 1 Args** | $1.00$ | **Standard Moon:** Sleek, highly encapsulated utility. |
| **2 - 4 Args** | $\sim 1.20 - 1.40$ | **Swollen Moon:** Normal business logic, carrying standard state. |
| **5 - 10 Args** | $\sim 1.46 - 1.66$ | **Heavy Moon:** Bloated function, heavy I/O weight. |
| **15+ Args** | $\sim 1.78+$ | **Gas Giant:** Visually burdensome, signaling a prime target for refactoring. |
