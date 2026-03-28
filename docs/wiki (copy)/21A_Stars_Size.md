#### 2.1.A. Star's Size

#####

****Purpose: Visualize the sheer \"Gravitational Weight\" of a file
within the system. Why: In a galaxy, size is the first thing you notice.
But in software, \"length\" does not always equal \"weight.\" A 200-line
configuration file is light, while a 50-line recursive algorithm is
heavy. By calculating mass based on complexity, risk, and volume, we
ensure that the most impactful files---the ones that are hard to read,
dangerous to touch, or heavily connected---physically dominate the
screen as super-massive suns. We use size to instantly communicate
structural importance.****

##### 2.1.A.1. The Philosophy: Physical Presence

We treat code as physical matter, but we recognize that matter has
different densities.

Low Density: Simple data, linear lists, and standard config files. These
are large but light, easy to move.

High Density: Complex branching logic, heavy arguments, and high risk
exposure. These are small but incredibly heavy, exerting high gravity.

By scaling the star\'s size based on this Composite Mass, we create a
visual hierarchy where the true \"Main Characters\"---the complex logic
engines---naturally anchor the sector, while simple helper files drift
in the background.

##### 2.1.A.2. The Inputs: Measuring Mass

The mass calculation ingests five distinct dimensions of code structure:

1.  Function Impact: The complexity of every function inside the file.
2.  API Exposure: How publicly visible the file is.
3.  Concurrency Exposure: The density of asynchronous/threading logic.
4.  State Flux Exposure: The density of variable mutation.
5.  LOC (Lines of Code): The raw physical volume (scaled down to act as
a base substrate).

##### 2.1.A.3. The Equation: Structural Mass & Visual Radius

We utilize a multi-stage summation to determine the raw mass. Complexity
multiplies; volume merely adds. We then apply a logarithmic clamp to
determine the final visual radius, ensuring that massive \"God Objects\"
are distinct but do not consume the entire viewport.

Step 1: Calculate Function Impact For every function in the file, we
calculate an impact score based on its decision density (Branches),
connectivity (Args), and length.

Function Impact = ((BranchHits + 1) \* (Args + 1) + (0.05 \* LOC)) \* 10

Step 2: Calculate Total Mass (The Raw Metric) The file\'s final mass is
the sum of its functions plus its system-wide risk exposures.

Total Mass = Sum(Function Impacts) + API + Concurrency + Flux + (LOC /
50)

Step 3: Calculate Visual Radius (The Render Size) We apply a base-2
logarithm to compress the massive range of weights (10 to 1,000,000)
into a renderable scale (10 to 50 units).

Radius = 10 + (Math.log2(Math.max(Total Mass, 1)) \* 2)

##### 2.1.A.4. The Visual Thresholds (The Scale)

The Asteroid (Mass \< 100): Radius \~16 units. Simple DTOs, interfaces,
or small configs. Nimble, low-gravity rocks that drift in the periphery.

The Planet (Mass 100 - 1,000): Radius \~20 to 26 units. Standard
business logic. Visible, stable, but not overwhelming. The \"Middle
Class\" of the galaxy.

The Star (Mass 1,000 - 20,000): Radius \~27 to 38 units. Core utilities,
major controllers, or complex engines. These anchor local clusters and
exert visible gravity.

The Super-Giant (Mass 20,000+): Radius \~40+ units. \"God Objects,\"
massive reducers, or legacy core files. These dominate the screen,
signaling extreme structural density.

****
