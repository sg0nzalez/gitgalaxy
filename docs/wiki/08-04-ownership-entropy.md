# Authorship (Ownership Entropy)

> **Metric: Shannon Entropy of Git Blame Data**
>
> **Purpose:** Visualizes the distribution of authorship within a file to identify where knowledge is siloed versus where it is shared. 
>
> **Why:** Ownership isn't about blaming a single author; it's about visualizing the Collective Mind. Rather than a linear author count, this system utilizes Shannon Entropy to determine the concentration or dispersion of contributions. This entropy score is mapped directly to the Universal Risk Spectrum, allowing you to instantly spot heavily siloed knowledge ("Bus Factor" risks) versus highly distributed community code.

## The Philosophy: Knowledge Concentration

Authorship is analyzed as a variable of structural clarity versus architectural diffusion:

* **Low Entropy (Individual Ownership):** Contributions are highly concentrated within a single primary author. This represents a unified mental model, but also a potential "Silo Risk" if that developer is unavailable.
* **High Entropy (Community Diffusion):** Contributions are distributed across multiple authors. As more developers influence the file, the architectural intent becomes shared, indicating a high-traffic module maintained by the collective.

## The Inputs: Contribution Share

* **Authors:** A data map of author identifiers to their specific commit frequencies for the file.
* **TotalCommits:** The aggregate sum of all commits recorded for the file.
* **GlobalAuthorCount:** The total number of unique contributors across the entire repository.

## The Equation: Shannon Entropy

First, we calculate the proportion of total commits ($p_i$) made by author $i$. (e.g., if Author A made 20 out of 100 commits, $p_i=0.2$).

We then apply the Shannon Entropy formula to calculate the total diffusion ($H$):

$$H=-\sum \left( p_i \times \log_2(p_i) \right)$$

Finally, we scale the entropy into a normalized $0$ to $100$ score for the rendering engine:

$$\text{OwnershipScore}=\min(H \times 32, 100)$$

## Why This Model is Superior

It solves the "Long Tail" problem. 
* A file with 1 Major Author (90%) and 1 Minor Author (10%) is relatively stable. 
* A file with 1 Major Author (90%) and 10 Minor Authors (1% each) is chaotic. 

A linear model scores these identically by just counting heads. The Entropy model correctly identifies the second file as significantly more "active" or "noisy" because it accounts for the sheer number of distinct voices in the mix. While the linear model asks, *"Who is the biggest author?"*, the entropy model asks, *"How much **uncertainty** exists in the authorship?"*

## Visual Interpretation: Ownership vs. Collective Diffusion

GitGalaxy utilizes the standard 5-stop Universal Risk Spectrum to visualize the entropy score, scaling from cool, isolated development to hot, multi-author environments.

| Score Range | Classification | Visual Target | Definition |
| :--- | :--- | :--- | :--- |
| **0 - 20** | **Individual** | 🟦 **Deep Blue** | Pure Ownership. The logic represents a single individual's architectural intent. |
| **21 - 60** | **Small Team / Squad** | 🩵 **Cyan** $\rightarrow$ 🟨 **Yellow** | Core Collaboration. Responsibility is shared among a tight-knit group of contributors. |
| **61 - 100** | **Dept / Community** | 🟧 **Orange** $\rightarrow$ 🟥 **Red** | Collective Maintenance. The module experiences constant, multi-author input and has reached complete architectural diffusion. |

## Architectural Stability: Scaling Logic & Visual Overload

By unifying Ownership under the Universal Risk Spectrum, GitGalaxy eliminates the need for expensive, multi-pass chromatic aberration shaders and per-author deterministic hashing.

Because the Shannon Entropy calculation condenses infinite author complexity into a clean $0.0 - 100.0$ exposure vector in the backend (`signal_processor.py`), the frontend renderer inherently scales. Whether a file has 2 authors or 2,000, the WebGPU engine simply translates the float into the static linear gradient. This guarantees smooth 60 FPS performance even when mapping planetary-scale megastructures like Linux or Kubernetes, without requiring visual fallbacks or macroscopic LOD (Level of Detail) toggles.