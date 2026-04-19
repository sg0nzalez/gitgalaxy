# The Detector (The Logic Splicer & Cartographer)

> **The EMCCD Sensor & Galactic Cartography**
>
> Before the Splicer spends computational energy carving a logic stream, it performs a strict physical viability check. If a file enters the Splicer with a structural confidence score below `0.42`, or belongs to a known inert data format (`json`, `yaml`, `csv`), it triggers a **Bypass**, safely relegating the file to "Dark Matter" or treating it as pure static mass. Similarly, files explicitly verified as `markdown` or `plaintext` trigger a Prose Deflection.
>
> **The Ecosystem Gravity Override:** A critical exception exists for highly contested, declarative files—most notably C/C++ header files (`.h`). Pure-macro headers often lack the standard functional logic required to pass the confidence floor naturally. If the upstream Language Lens utilized ecosystem mass to safely lock a file into a C-family orbit, the Splicer trusts that macro-level gravity and artificially boosts the file's parsing confidence to `1.0`, ensuring these critical structural components are fully mapped.

## The Atomic Literal Shield

Strings and text literals are the natural enemies of structural parsers. A stray opening brace `{` or an unmatched quote `"` trapped inside a developer's string can permanently desynchronize the scope stack, shattering the parsed logic.

To prevent this "Quote Desynchronization," the Splicer utilizes the **Atomic Literal Shield**, an advanced pre-processing engine that securely masks disruptive text *without* altering the physical line counts or character indexing of the original file. This ensures the parsed logic perfectly maps 1:1 with the original source code.

* **Advanced Atomic Quotes:** The shield processes multi-character sequence markers strictly *before* single quotes. This surgical ordering correctly masks C++ Raw String Literals (e.g., `R"EOF(...)EOF"`) and Python Triple Quotes without prematurely triggering on standard double quotes contained within them.
* **Heredoc Isolation:** For scripting languages, standard regex is insufficient. The Splicer deploys a line-by-line state machine to isolate complex Heredoc logic, safely blanking out massive text blocks that frequently contain rogue bash characters.
* **Ruby `%` Literals:** Strictly gated to the Ruby ecosystem, a dedicated shield evaluates and masks the complex, bracketed `%` string syntax, preventing internal brackets from falsely triggering the scope stack.
* **Diagnostic Telemetry:** To protect pipeline performance against Catastrophic Backtracking (ReDoS), the shield actively times its own regex operations. If shielding an obfuscated file takes longer than 0.5 seconds, the engine logs a targeted diagnostic warning to trace the latency bottleneck.

## Coding vs. Comment Analysis (Separation of Concerns)

To maintain absolute mathematical integrity, the GitGalaxy Splicer strictly enforces a Separation of Concerns between executable logic (Active Matter) and developer literature (Ghost Mass). Mixing these two streams is the primary cause of "Logic Erosion" in legacy scanners. 

### Spatial Mapping & Signal Correlation (Active Matter)
The `coding_analysis` engine measures the raw physical properties of the Active Matter. Rather than just counting hits, the engine generates a **Spatial Map**, recording the exact index coordinate of every regex strike. This allows the engine to perform $O(N)$ Spatial Correlation to uncover complex, multi-line vulnerabilities:
* **Taint Tracking (RCE Weaponization):** Correlates dangerous execution functions (eval/exec) that sit within the blast radius of external I/O or LLM hooks.
* **The Silencer Region:** Correlates error-suppression/bypasses with nearby safety blocks to determine if danger is truly mitigated or actively weaponized.
* **Race Condition Radar:** Correlates high state-flux mutation with asynchronous thread spawns that lack nearby synchronization locks.
* **Memory Leak Tracker:** Correlates manual memory allocations against cleanup functions to find unmitigated leaks or Use-After-Free (UAF) vulnerabilities.

### Intra-File Orphan & Duplicate Detector
The engine executes a high-speed $O(1)$ word-frequency tally across the entire file. It cross-references this tally against the names of the parsed functions to instantly flag **Design Slop**—functions that are duplicated, or functions that are declared but entirely orphaned (unused) within their local scope.

### Token Physics & ML Inference
The Splicer doesn't just measure lines of code; it calculates the file's LLM context footprint.
* **Token Mass:** Utilizing `tiktoken` (cl100k_base), it calculates the exact token mass and subsequent financial read-cost of feeding the file to an LLM.
* **Function ML Classification:** The Splicer calculates the Big-O Depth, Recursion presence, and Structural Inequality (Gini index) of every isolated function. It then scales these vectors and uses Euclidean distance against pre-loaded K-Means centroids to instantly classify the function's archetype (e.g., "God Function", "State Mutator", "I/O Bridge").

### Comment Analysis (Ghost Mass Telemetry)
The `comment_analysis` engine scans the isolated literature of the file. It uses a specialized subset of rules to measure developer intent and technical debt without polluting core logic metrics. It actively tracks `planned_debt` (TODOs), `fragile_debt` (HACKS), and `graveyard` hits (dead code trapped inside comments).

## Metric Vectorization: Multi-Dimensional Physics

Because programming languages adhere to vastly different structural physics, a one-size-fits-all regex approach is mathematically impossible. The Master Dispatcher analyzes the language's lexical family and dynamically routes the Active Matter into one of five highly specialized extraction algorithms (Integration Modes).

* **The Anti-ReDoS Line Limiter:** Before routing, the engine scans for absurdly long continuous lines (like `Make` `.depend` files or C hex arrays). Any line exceeding 1500 characters is blanked out to neutralize Catastrophic Backtracking while perfectly preserving the file's geometry.
* **Mode A: Label-Based Scan (Legacy Species)** Used for legacy procedural languages like Assembly, AGC, and COBOL. It searches for functional start tags and captures the entire block until it encounters a definitive return instruction.
* **Mode B: Recursive Scope Analysis (C-Family & Lisp)** The standard algorithm for languages relying on braces `{}` or parentheses `()`. It utilizes an Atomic Alternation Shield to prevent complex string manipulation from confusing the scanner, and a C++ Preprocessor Shield to safely step over raw floating braces (e.g., `#else {`).
* **Mode C: Density Stratification (Python & YAML)** Languages that rely on whitespace require a topographical approach. The engine identifies a structural igniter, calculates its base indentation level, and scans forward line-by-line until the code drops back to or below the base indentation.
* **Mode D: Semantic Handshake Stack (Keyword Scoping)** Designed for non-brace scripting languages like Shell, Ruby, Lua, and Elixir. It tracks structural depth via text keywords (`if`/`fi`, `def`/`end`) rather than symbols, using specialized heuristics like the Ruby Inline Modifier Guard to prevent false depth increments.
* **Mode E: Terminator Cleaving (Declarative Architectures)** Designed for query languages like SQL, Erlang, and Prolog. It monitors the stream for an Igniter keyword (`SELECT`, `CREATE`) to start orbiting a new block, leaving it open until it detects a Terminator token (`;` or `.`), where the "guillotine drops."

## Satellite Physics & Naming Shields

Once the Master Dispatcher cleaves a block of logic from the file, it becomes a "Satellite."

### Satellite Physics (The Mathematical Engine)
The engine analyzes the raw string of the isolated block to calculate its weight and trajectory:
* **Control Flow Ratio:** Measures the density of branching logic vs. linear execution.
* **Logic Angle:** Determines the trajectory of the satellite's branches in the 3D viewer. (Highly linear functions branch at steep 90° angles; complex functions branch at wide 22.5° angles).
* **Magnitude (Mass):** A composite equation weighting exponential complexity (Branches) and input density (Args).
* **Level 3 Wiring (Call Chains):** Scans the block for any word followed by a parenthesis (excluding keywords) to map exact function-to-function call chains for downstream relational mapping.

### The Naming Shields
Extracting a function name from raw text is notoriously difficult. GitGalaxy utilizes a gauntlet of Naming Shields to ensure pristine labels:
* **C++ Operator Shield:** Safely intercepts and extracts overloaded symbolic operators (e.g., `operator<<`) before standard extraction destroys the symbols.
* **C++ Test Macro Shield:** Extracts the true test name from complex macro wrappers (e.g., `BOOST_AUTO_TEST_CASE(MyTest)` -> `MyTest`).
* **C++ Scope Shield:** Temporarily replaces the double-colon (`::`) with a safe token so the standard single-colon guillotine doesn't truncate names.
* **Objective-C Extraction:** Surgically parses Apple's unique bracketed message syntax.

## The Cartographer: Fractal Fibonacci Positioning

The Cartographer transforms flat file lists into a deterministic 3D star map utilizing a collision-aware packing algorithm to create organic, repeatable, and dense volumetric galaxies.

### Sectorization & Hull Calculation
Files are grouped by their root directory (Constellations). Within each constellation, the file with the highest Structural Mass is designated as the central "Sun." The engine calculates the required bounding box (Hull Radius) for the folder based on the Sun's footprint and the total number of orbiting stars.

### The Ray-Casting Dynamic Mask (Angular Spatial Hashing)
To map the galaxy on a 2D plane without constellations colliding, the engine uses a Ray-Casting Mask.
* **The Optimization:** To prevent an $O(N^2)$ death spiral when mapping 10,000+ folders, the Cartographer implements **Angular Spatial Hashing**. It divides the 360-degree galactic map into 360 distinct memory bins.
* **The Ray-Cast:** When placing a new constellation, the engine shoots a mathematical ray down the current angle. Instead of checking every folder for a collision, it only queries the exact 3-degree arc the ray is passing through.
* **Dense Packing:** It solves a quadratic intersection equation against those specific colliding boundaries, pushing the new constellation outward only to the furthest intersecting positive root. This guarantees zero collisions while ensuring the galaxy remains as tightly packed as mathematically possible.

### Local Star Systems & Constellation Tilt
* **The Golden Angle:** Planets orbit their central Sun using the classic Fibonacci angle ($\approx$ 137.5°). The radius expands based on the square root of the star's mass-rank, gracefully decreasing the density of the star system as it moves outward.
* **Volumetric Tilting:** To break the artificial flatness of a 2D plane, each constellation is rotated on its local axis. Using hash-derived math, entire folders are tilted in unique directions, creating a true 3D volumetric cloud.

### Organic Entropy (Hash Jitter)
To break the mechanical perfection of the mathematical spirals, the engine injects "Organic Noise."
* **MD5 Seed Logic:** It hashes the filename to a hex string, mapping it to a normalized coordinate modifier.
* **Reproducible Chaos:** A perfectly mathematical spiral feels artificial. Jitter provides the "texture" of a real galaxy. Because the seed is based on the filename, the chaos is strictly deterministic—a file will always "vibrate" to the exact same relative sub-coordinate every time the map is rendered.