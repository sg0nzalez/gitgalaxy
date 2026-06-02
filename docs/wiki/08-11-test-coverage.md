# Verification Risk Exposure (Test Coverage)

GitGalaxy measures test coverage not by counting lines, but by assessing the complexity and magnitude of the logic against the amount and size of the tests defending it. We calculate an initial raw structural impact for every function which can be reduced by testing, either with internal assertions or external testing files that reference that function. This reveals the remaining **Untested Impact** for each function and these scores are rolled up into classes. At the file level, we have enough data to normalize the raw values. The raw untested impact values are normalized for coding loc, network importance and by the presence of golden image tests and subjected to a sigmoidal threshold scoring system that ranges from 0-100. 

 **Effect:** Maps directly to the GitGalaxy Universal Risk Spectrum.
 * 🟦 **VERY LOW (Score 0-19):** Heavy Shielding. The largest, small and large functions are heavily dampened by proportional, targeted unit tests or component-level golden images.
 * 🟨 **INTERMEDIATE (Score 40-59):** Moderate Exposure. Standard logic has basic coverage, but some functions lack sufficient defensive mass, leaving noticeable residual risk.
 * 🟥 **VERY HIGH (Score 80-100+):** Blind Execution. Many functions and files with very low testing verification. 

### Level 1: Function 

Range: 0 - Max

This level starts with the initial the raw structural impact value of the function and reduces that impact if it has tests targeting it, and uses that relative ratio to mathematically crush the risk into a residual **Untested Impact**.

**Step A: The Base Impact**
We take the raw `Function Impact` score and subtract the explicitly defined internal defenses located physically inside the function boundaries. To ensure accuracy across all languages, the engine calculates this defense by combining exactly **three specific metrics** from the 51-Element Universal Schema:
* **Verification (`test`):** Inline assertions and test macros (e.g., `assert()`, `expect()`).
* **Safety (`safety`):** Guard clauses, type-guards, and strict boundary management (e.g., `require()`).
* **Bypassed Tests (`test_skip`):** A negative modifier that aggressively *subtracts* defensive mass if an assertion is explicitly disabled (e.g., `it.skip`).

$$BaseImpact = \max(FunctionImpact - ((Verification + Safety - (Bypassed \times 2.0)) \times Fc), 0.0)$$

**Step B: The Defensive Ratio (Effective Mass)**
We calculate the `EffectiveTestImpact` of every external test targeting the function. To prevent "safety theater" and structural blind spots, a test's raw impact is modified by three strict rules before summation:
* **Assertion Density:** If the external test lacks internal assertions (zero `test` schema hits), its mass is zeroed out—a massive test without assertions verifies nothing.
* **External Bypass (Sabotage):** If the external test contains a skip/bypass trigger (`test_skip`), its defensive tether is severed and its mass is completely nullified.
* **Parameterization Multiplier:** If the test utilizes data-driven parameterization macros (e.g., `@pytest.mark.parametrize`), a multiplier is applied to its mass to accurately reflect its dynamic execution weight.

Each test's effective impact is then divided by the total number of production functions it targets ($TargetCount$) to dilute sprawling integration tests.

$$DefensiveRatio = \frac{\sum (EffectiveTestImpact / TargetCount)}{FunctionImpact}$$

**Step C: The Asymptotic Dampener**
We feed that `DefensiveRatio` into the inverse decay equation. If the tests are physically tiny compared to the function, the ratio is low, and the dampener barely reduces the risk. If the tests are massive compared to the function, the ratio is high, and the risk is violently crushed toward zero.

$$UntestedImpact = BaseImpact \times \left( \frac{1}{1 + (C_t \times DefensiveRatio)} \right)$$

### Level 2: Class 

Range: 0 - Max

Classes act strictly as containment boundaries to roll up the math. 

* **The Mechanics:** We sum the residual **Untested Impact** scores from all the functions contained within the class architecture.
* **The Math:**
$$ClassUntestedImpact = \sum (FunctionUntestedImpact)$$

### Level 3: File 

Range: 0-100

This level translates the raw, accumulated unverified impact scores into a true risk percentage. Following the Universal Exposure Framework, we normalize the risk against the file's coding loc, apply environmental multipliers, and finally push the adjusted density through our sigmoidal model.

* **Step A: Executable Density Normalization**
We take the sum of all `Untested Impact` from the file's functions and divide this total by the `coding_loc` (Total LOC minus comments and whitespace) to establish the base density. By stripping out comments and whitespace, we prevent bloated formatting from artificially diluting the risk. 

To account for the "Opacity Tax" of highly dynamic or implicit languages, we multiply this base density by the language's **Opacity Tax Multiplier**. This ensures that the penalty for the language's implicit ambiguity scales proportionally with the amount of unverified logic.
$$RawDensity = \left( \frac{\sum ClassUntestedImpact}{\max(CodingLOC, 1)} \right) \times Ot$$

* **Step B: Ecosystem Modifiers (Pre-Curve Normalization)**
Before plugging this into our sigmoidal equation, we adjust the density based on the file's physical surroundings and network gravity:
  * **The GuideStar Umbrella (Dampener):** If the file is protected by directory-level golden image tests or visual regression snapshots, we apply a dampening fraction to shrink the density.
  * **Network Blast Radius (Amplifier):** We multiply the density by the file's PageRank centrality. If the file is a highly imported global router, its lack of verification is exponentially more dangerous, artificially swelling its density.
$$AdjustedDensity = (RawDensity \times GuideStarDampener) \times BlastRadius$$

* **Step C: Sigmoidal Normalization**
The `AdjustedDensity` is pushed through the logistic sigmoid function. This acts as a strict noise gate: files with trace amounts of unverified mass stay near 0 (Safe/Blue). Once the unverified density crosses the critical threshold, the sigmoidal model normalizes the value, spiking rapidly toward 100 (Critical/Red).
$$BaseScore = \min\left( \frac{100.0}{1 + e^{-Slope \times (AdjustedDensity - Threshold)}}, 100.0 \right)$$

* **Step D: The Path Modifier & Breach Cap**
Finally, we apply the Path Modifier ($Mp$). If the file itself is a test suite (e.g., `router.spec.js` or located in `/tests/`), $Mp$ is set to $0.0$, immediately neutralizing the risk. For production files ($Mp = 1.0$), we evaluate the **Breach Cap**: if the total unverified mass is overwhelmingly larger than the verified mass, the file is hard-capped to a minimum "Fragile" rating, ensuring no amount of mathematical noise-gating can hide a fundamentally untested file.
$$FinalFileScore = BaseScore \times Mp$$

### Level 4: Folder 

Range: 0-100

This level determines the testing risk exposure of different folders.

*  The Testing Risk Exposure scores for each file, ranging from 0-100, within a directory are rolled up using a Mass-Weighted Average coding LOC of each file.
* **The Result:** A massive, complex God Object that scores a 95 (Critical Risk) will exert immense averaging pull on the parent folder's overall health score. A tiny, 15-line helper script with zero tests that also scores a 95 will barely move the needle, preventing small utility files from skewing the local aggregate metrics.

### Level 5: Repo 

Range: 0-100

This level determines the ultimate testing risk exposure of the entire codebase.

*  The Testing Risk Exposure scores for each directory under root, ranging from 0-100, are rolled up using a Mass-Weighted Average coding LOC of each folder.
* **The Physics:** A massive, highly complex core directory saturated with risk will drag down the gravitational health of the entire project. Conversely, a highly risky but lightweight experimental folder will be safely absorbed by the stabilizing mass of a well-tested, fortified core.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🧠 **[Deep Dive into the Physics Source Code](https://github.com/squid-protocol/gitgalaxy/tree/main/gitgalaxy/physics)** to see the math in action.
* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

---

**[⬅️ Back to Master Index](index.md)**