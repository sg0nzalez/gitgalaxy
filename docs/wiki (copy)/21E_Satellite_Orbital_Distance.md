#### 2.1.E Satellite Orbital Distance

**Metric**: Lines of Code in a function.

**Effect**: Bigger the function, the further the satellite.

**Input**: LOC (Lines of Code for the specific function/block).

**Logic**: Logarithmic Scaling. This ensures that we can visually
differentiate between small (10 lines), large (1,000 lines), and massive
(100,000 lines) files without the graphic growing infinitely off the
screen.

****Equation:****

-   *Length_pixels = 60 + (Math.log2(Math.max(LOC, 1)) \* 30)*

****Scaling Examples: ****

-   -   ****10 LOC:**** \~160px (Visible Stub)
-   ****100 LOC:**** \~260px (Standard Branch)
-   ****1,000 LOC:**** \~360px (Major Limb)
-   ****100,000 LOC:**** \~560px (Megastructure Reach)

****Visual Output:****

-   -   ****3D:**** Distance of the orbiting satellite from the core
(Orbital Radius).
