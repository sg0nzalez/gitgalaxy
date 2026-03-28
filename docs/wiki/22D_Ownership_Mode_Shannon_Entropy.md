# 2.2.D. Ownership Mode: Shannon Entropy

Ownership displays the distribution of authorship within a file.
Ownership isn't about blaming a single author; it's about visualizing
the Collective Mind. A healthy culture is transparent about where
knowledge is shared and where it is siloed.

Rather than a linear author count, this system utilizes Shannon Entropy
to determine the concentration or dispersion of contributions. This
entropy score is then mapped directly to the GitGalaxy Universal Risk
Spectrum, allowing you to instantly spot heavily siloed knowledge (\"Bus
Factor\" risks) versus highly distributed community code.

## 2.2.D.1. The Philosophy: Knowledge Concentration

Authorship is analyzed as a variable of structural clarity versus
architectural diffusion.

-   **Low Entropy (Individual Ownership):** Contributions are highly
concentrated within a single primary author. This represents a
unified mental model, but also a potential \"Silo Risk\" if that
developer is unavailable.
-   **High Entropy (Community Diffusion):** Contributions are
distributed across multiple authors. As more developers influence
the file, the architectural intent becomes shared, indicating a
high-traffic module maintained by the collective.

## 2.2.D.2. The Inputs: Contribution Share

-   **Authors:** A data map of author identifiers to their specific
commit frequencies for the file.
-   **TotalCommits:** The aggregate sum of all commits recorded for the
file.
-   **GlobalAuthorCount:** The total number of unique contributors
across the entire repository.

## 2.2.D.3. Equation

**p_i:** The proportion of total commits made by author \"i\" (e.g., if
Author A made 20/100 commits, p = 0.2).

Entropy = H = -sum(p_i \* log2(p_i))

OwnershipScore = min(H \* 32, 100)

## 2.2.D.4. Why This Model is Superior

1.  **It Solves the \"Long Tail\" Problem:** A file with 1 Major Author
(90%) and 1 Minor Author (10%) is relatively stable. A file with 1
Major Author (90%) and 10 Minor Authors (1% each) is chaotic. The
Linear model scores these identical (Score: 10). The Entropy model
correctly identifies the second file as significantly more
\"active\" or \"noisy\" because it accounts for the sheer number of
distinct voices in the mix while still marking it mostly with the
color of the main author. While the Linear model only asks \"Who is
the biggest author, regardless of commit size?\", the entropy model
displays \"How much **uncertainty** exists in the authorship?\". In
GitGalaxy, high entropy means diffusion of authorship.

-   #####

## 2.2.D.5. Visual Interpretation: Ownership vs. Collective Diffusion

-

**GitGalaxy utilizes the standard 5-stop Universal Risk Spectrum to
visualize the entropy score, scaling from cool, isolated development to
hot, multi-author environments.**

-   INDIVIDUAL (Score 0 - 20):

-   **Visual:** Deep Blue (*#0055ff*).
-   **Definition:** Pure Ownership. The logic represents a single
individual\'s architectural intent.

-   SMALL TEAM / SQUAD (Score 21 - 60):

-   **Visual:** Cyan (*#00ffff*) transitioning to Yellow
(*#ffff00*).
-   **Definition:** Core Collaboration. Responsibility is shared
among a tight-knit group of contributors.

-   DEPT / COMMUNITY (Score 61 - 100):

-   **Visual:** Orange (*#ff8800*) transitioning to intense Red
(*#ff0000*).
-   **Definition:** Collective Maintenance. The module experiences
constant, multi-author input and has reached a state of complete
architectural diffusion.

## 2.2.D.6. RQM: Scaling Logic & Visual Overload

By unifying Ownership under the v6.0 Universal Risk Spectrum, GitGalaxy
eliminates the need for expensive, multi-pass chromatic aberration
shaders and per-author deterministic hashing.

Because the Shannon Entropy calculation condenses infinite author
complexity into a clean *0.0 - 100.0* exposure vector in the backend
*signal_processor.py*, the frontend renderer instantly inherently
scales. Whether a file has 2 authors or 2,000, the WebGPU engine simply
translates the float into the static linear gradient. This guarantees
smooth 60 FPS performance even when mapping planetary-scale
megastructures like Linux or Kubernetes, without requiring visual
fallbacks or macroscopic LOD (Level of Detail) toggles.
