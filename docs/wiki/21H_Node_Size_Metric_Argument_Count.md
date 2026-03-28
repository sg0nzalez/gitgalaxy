#### 2.1.H Node Size (Metric: Argument Count)

****Metric:****** Argument Count (Args). **

****Purpose:****** Visualizes the \"State Heaviness\" or I/O weight of a
function. **

****Why:****** Functions with many arguments often carry significant
state or context (\"I/O Weight\"). A clean utility usually takes 1-2
arguments, while a legacy handler might take 10. We visualize this
physically to differentiate sleek tools from heavy machinery. **

****Effect:****** Modulates the physical size (Scale) of the orbiting
satellite.**

##### 2.1.H.1. The Philosophy: Heavy vs. Light

We view arguments as \"Inputs\" or \"Cables\" plugged into the function.

-   **Lightweight:** 0-2 arguments. Sharp, encapsulated, easy to move.
-   **Heavyweight:** 5+ arguments. Bloated, carrying too much context,
harder to maintain.

##### 2.1.H.2. The Inputs: Measuring Args

-   **Args:** The count of arguments in the function signature found by
the scanner.
-   **Range:** Typically 0 to 20+.

##### 2.1.H.3. The Equation: Logarithmic Scaling

We use logarithmic scaling to prevent massive orbs for functions with
many arguments (e.g., 20+). A linear scale would make them visually
overwhelming; a log scale highlights the difference between 0 and 5, but
compresses the difference between 10 and 20.

**Equation:** *Scale = 1.0 + (Math.log2(Math.max(Args, 1)) \* 0.2)*

-   **Base Scale:** 1.0 (Standard Unit).
-   **Factor:** \* 0.2 (Gentle growth multiplier).

##### 2.1.H.4. The Visual Output

-   **3D:** Radius of the orbiting Moon particles.
