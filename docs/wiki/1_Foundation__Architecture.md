## 1. Foundation & Architecture

### 1.1 Project Overview

1\. Code can be art. Logic can be art. Systems engineering can be art.
GitGalaxy reveals the **complexity of codebases** **as explorable 3D
galaxies **by using source code as a seed for procedural generative art.
The human brain is not optimized for processing rows of digits; it is
optimized for detecting patterns in nature or physics. By procedurally
mapping complexity to things like spatial position, movement, pulses and
colors, **GitGalaxy taps into our evolutionary strengths to help us
understand** **complex systems intuitively**.

2\. While there are many ways to write code, organizations rely on
agreed-upon standards for coding practices. **GitGalaxy assesses
deviations from organizational standards and displays that info as color
overlays onto the 3D generated world. **GitGalaxy does not measure
\"Code Quality\", which feels like a judgment, but instead measures
**Risk** Exposure. Our measurements do not judge; they
highlight. They function as sensors, not critics.

-   We do not assess \"Bad Code\"; we measure
Cognitive Load Exposure, how hard it is for a human
to work through the logic, because teams should be aware which files
are the hardest to work on.
-   We do not assess \"Missing Docs\"; we assess
**Documentation** Exposure, the risk to the team if a key person
leaves.
-   We do not assess \"Missing Testing\"; we
assess **Testing** Exposure, the risk of unshielded logic
causing a meltdown in production.
-   We do not measure \"System Security\"; we measure
Safety Exposure, the structural brittleness caused by a lack
of *try/except* blocks and robust error handling.

```{=html}
<!-- -->
```
-   We do not measure **API Exposure** because its always bad,
we just want teams to understand **how sensitive a file
might be to changes**.
-   We do not measure **Concurrency Exposure** because it's
always bad but because teams should be able to easily assess
the **risk of race conditions and deadlocks** in multi-threaded
logic.
-   We do not measure State Flux Exposure because it's
always bad but we because teams can easily assess
the **risk of state conflicts**.
-   We do not measure** Specification **Exposure to catch \"Cowboy
Code that's out of spec,\" but to act as an organizational
compass; it ensures that as a feature settles into the codebase,
the documentation follows, fostering a culture where every line of
logic has a traceable and understood home.

By visualizing these exposures as toggle-able color overlays onto the
generated galaxy, GitGalaxy provides an intuitive **non-numeric
dashboard**. It allows a team to agree on standards and instantly
see---without reading a single line of text---where their architecture
might be drifting into dangerous territory.

3\. Many projects are multi-lingual. Traditional code analysis tools
(ASTs) act like strict linguists---they understand the grammar of one
language perfectly but not of any others. GitGalaxy acts as **a Rosetta
Stone for code complexity, project scale and risk exposure**. By
prioritizing consistent regex-based approximation over rigid syntax
parsing, we can meaningfully compare different code bases of different
languages. This consistent standard allows us to visually compare the
scale and complexity of different coding projects, from Apollo 11
(Assembly) to the Linux Kernel (C) to TensorFlow (Python) under the same
set of rules.

**Why This Matters:**

-   **Identify Hotspots: **Instantly spot files with high exposure, as
they are literally glowing planets in space.
-   **See Risk:** See exactly where \"dangerous\" patterns cluster
before they become issues.
-   **Audit Legacy Systems: **Map the topology of ancient codebases
(like COBOL) to plan modernization strategies without reading a
million lines of code.
-   Analysis happens on your machine, takes seconds and makes a file
smaller than a photo and with a data presentation so easy kids could
get it.

To accomplish this, GitGalaxy uses general Regex-based semantic
signatures that have been adapted to each language, as either 1. the
input to various Risk Exposure Equations or 2. as seeds for a
procedurally generated algorithm to create a novel visual representation
of codebase complexity. This project prioritizes ease of use, zero-setup
scanning, comparative analyses and visual impact over the academic rigor
of a single language Abstract Syntax Tree. **This project does not
visualize syntax or if it will compile**; it visualizes aspects of
functional intent.

GitGalaxy comes pre-loaded with functional Risk Exposure Equations but
customization may be needed to adapt for your team's standards. These
equations define the intensity of the color overlay effect. All
equations attempt to target a 0-100 scale. Although the developer has
worked hard to make the equations as nuanced as they can be, the
equations should be viewed as rough approximations only. They should be
used to identify general trends (**Good - this file has high API
exposure**) versus absolute ranking over tiny differences (**Bad - this
file is better than that one because it scored 1% higher in the tech
debt equation**). We took pains to hide the specific numbers, and
instead only report out general tiers (very high, high, medium, low,
very low).

GitGalaxy calculates exposure metrics in a non-linear fashion with
equations and sub-equations. This is because there are multiple ways to
achieve the same goal, like how to adhere to safety standards, and this
allows for the evaluation of different practices and to weigh them
differently. Sometimes our sub-equations pop up in multiple equations;
for example both the safety equation and the tech debt equation use the
sub-equation of SafetyHits, which is a measure of counts of \'try\',
\'catch\', \'finally\', \'assert\', \'sanitize\', etc.

### 1.2 The blAST Paradigm: Sequencing Software as DNA

Standard static analysis tools rely on language-specific Abstract Syntax
Trees (ASTs). These are computationally expensive, fragile, and
bottlenecked by compiler constraints. GitGalaxy abandons the AST
entirely in favor of a novel **blAST (Broad Lexical Abstract Syntax
Tracker)** algorithm.

By applying the principles of biological sequence alignment and
bioinformatics to software (namely the BLAST algorithm), blAST hunts for
the universal structural markers of logic across over 40 languages and
250 file extensions. It translates this genetic code into
\"phenotypes\"---measurable risk exposures and architectural traits.

** Hyper-Scale Velocity** By bypassing the compiler bottleneck, blAST
achieves processing velocities that traditional scanners cannot match,
allowing it to map planetary-scale repositories in seconds rather than
hours:

-   **Peak Velocity:** Sequenced the 141,445 lines of the original
Apollo-11 Guidance Computer assembly code in **0.28 seconds** (an
alignment rate of 513,298 LOC/s).
-   **Massive Monoliths:** Processed the 3.2 million lines of OpenCV in
just **11.11 seconds**.
-   **Planetary Scale:** Effortlessly maps the architectural DNA of
hyper-scale repositories like TensorFlow (7.8M LOC), Kubernetes
(5.5M LOC), and FreeBSD (24.4M LOC).

**The Viral Security Lens (Behavioral Threat Hunting)** Traditional
security scanners rely on rigid, outdated virus signatures. The blAST
algorithm acts as an architectural immune system, hunting for the
*behavioral genetic markers* of a threat rather than specific strings of
text.

By analyzing the structural density of I/O hits, execution triggers, and
security bypasses, blAST proactively flags novel attack vectors:

-   **Supply-Chain Poisoning:** Instantly flags setup scripts possessing
an anomalous density of network I/O and dynamic execution.
-   **Logic Bombs & Sabotage:** Identifies code designed to destroy
infrastructure by catching dense concentrations of catastrophic OS
commands and hardware aborts.
-   **Steganography & Obfuscated Malware:** Mathematically exposes
evasion techniques, flagging Unicode Smuggling (homoglyphs) and
sub-atomic custom XOR decryption loops.
-   **Credential Hemorrhaging:** Acts as a ruthless data vault scanner,
isolating hardcoded cryptographic assets buried deep within massive
repositories.

### 1.3 Visualizing Complexity

GitGalaxy operates on the principle that source code can be used as a
procedural generation seed. Just as a random string of text in Minecraft
dictates the rise of mountains or the depth of oceans, your codebase\'s
logic dictates the topology of the galaxy that emerges. We treat code
not as a set of instructions to be compiled, but as a seed for a
generative galaxy.

GitGalaxy renders code bases with the following visual metaphors:

-   -   **Files** = Stars orbiting around an unseen black hole
-   **External libraries = **Rings around planets
-   **File Relationships = **Relative locations of stars in
the galaxy
-   **Inbound imports = **A star's pulse rate
-   Functions = Satellites orbit
stars
-   **Function complexity **=** **Arrangement, number and size of
satellites in a unit
-   **Function length = **Satellite orbital distance
-   **Function Arguments** = satellite size
-   File Complexity = Star shape
-   **Tech debt** **exposure **= color overlay
-   **Documentation exposure** = color overlay
-   **Cognitive Load exposure**= color overlay
-   **Safety exposure** = color overlay
-   **Testing exposure** = color overlay
-   **API exposure** = color overlay
-   **Concurrency exposure** = color overlay
-   **State Flux exposure **= color overlay
-   **Private Info exposure** = color overlay
-   **Churn** = color overlay
-   **Commit Heat** = color overlay
-   Languages used = color overlay
-   Authorship = color overlay
-   **Audit exposure **= color overlay

### 1.4 System Architecture: High-Level Stack

The application utilizes a concern-separated architecture designed to
bridge raw forensic data with cinematic visualization. The primary
deployment model is a Client-Side \"Zero-Trust\" Application
(Open Source), with an optional Enterprise Backend.

The Open-Source Core (Browser-Based Engine):

-   **scanner.worker.js** (The Primary Engine): The heart of the
free version. It runs in a background Web Worker to perform 100%
local analysis. It digests regex hits and calculates risk exposures
without transmitting code to a server.
-   **scanner_config.js** (The Rulebook): A ported,
JavaScript-native registry of heuristic patterns. It includes the
standard Regex library for 18+ languages.
-   **zip_loader.js** (The Ingestion Layer): Handles the
\"Zero-Trust\" unpacking of repositories directly in browser memory.

The Bridge (Data Schema):

-   **result.json** (The Interface Contract): While the user
never sees this file in the web version, it acts as the strict data
schema that decouples the logic from the rendering.

-   In Web Mode: It exists as an ephemeral in-memory object
passed from the Worker to the Main Thread via **postMessage**.
-   In Enterprise Mode: It is serialized to disk for CI/CD
reporting or trends over time analyses.
-   Role: It carries the unified payload for physics
coordinates and risk exposure, ensuring the 3D Viewer
behaves identically regardless of the source.

The Viewer (Frontend):

-   **engine-3d.js** (The Visualizer): A Three.js WebGL engine
that displays the spatial and color information of a codebase into
an interactive non-numeric dashboard.

### 1.5 System File Map: Backend (Scanner) vs. Frontend (Viewer)

**ROOT/**

**├── pyproject.toml \# Package manifest for the GitGalaxy CLI**

**├── README.md \# Documentation & Quickstart**

**├── data/ \# Output directory for generated artifacts**

**├── gitgalaxy/ \# \[THE BACKEND\] The blAST Analysis Engine**

**│ ├── gitgalaxy_standards_v1.py \# The Universal Laws: Taxonomy,
Threat Policies, & Config**

**│ ├── language_lens.py \# Entity Census & Identity Locks**

**│ ├── prism.py \# The Optical Splitter (Logic vs. Literature)**

**│ ├── detector.py \# Logic Splicer & 3D Cartographer**

**│ ├── security_lens.py \# Threat Detection & Vulnerability Scanning**

**│ ├── signal_processor.py \# The Physics Engine & Exposure Math**

**│ ├── spectral_auditor.py \# Statistical Outlier Detection (Quality
Control)**

**│ ├── audit_recorder.py \# Human-Readable Forensic Manifest
Generator**

**│ ├── llm_recorder.py #: **AI-agent & **RAG SQLite & Markdown Brief
Generator**

**│ └─── gpu_recorder.py \# Hypercompressed Columnar JSON Generator**

**│**

**├── airgap_observatory/ \# \[THE FRONTEND\] Zero-Telemetry Local
Visualizer (Static)**

**│ ├── index.html \# Main Entry Point (UI Shell & Canvas Container)**

**│ ├── main.js \# Main Controller (UI \<-\> Engine Pipeline)**

**│ ├── config/**

**│ │ └── colors.js \# Palette Registry (Exposure, Texture, and Language
colors)**

**│ ├── css/**

**│ │ └── styles.css \# Post-processed Tailwind UI styling**

**│ ├── core/ \# The \"Brain & Eyes\" (Data Processing & Rendering)**

**│ │ ├── data-parser.js \# Decodes the hypercompressed
galaxy_gpu.json**

**│ │ ├── galaxy-engine.js \# The Physics Core (Three.js WebGL scene
orchestrator)**

**│ │ ├── phase-6-shaders.js \# Custom WebGPU/WebGL Shader logic for
particles**

**│ │ └── materials.js \# The Visual Cortex (Data Focus Protocol & Node
Textures)**

**│ ├── tools/ \# The \"Hands\" (Interaction & Utilities)**

**│ │ ├── search.js \# Neural Nav - Fuzzy Indexing & Hacker HUD UI**

**│ │ ├── perf_monitor.js \# The GalaxyScope (Tilde \`\~\` Telemetry
HUD)**

**│ │ ├── ally.js \# The Parallel DOM (Accessibility Engine)**

**│ │ └── poster.js \# The Gift Shop (High-Res Artifact Generator)**

**│ └── lib/ \# Third-Party Dependencies (Three.js, Tween - Collapsed)**

**│**

**└── site/ \# \[THE FRONTEND\] Live Web Application (GitGalaxy.io)**

** ├── app.py \# Server routing for the live web application**

** ├── index.html \# Web Entry Point**

** ├── js/**

** │ ├── main.js \# Web App Controller**

** │ └── core/ \# Web App Rendering Engine (Mirrors
airgap_observatory/core)**

** ├── css/ \# Web App Styling**

** ├── config/ \# Web App Palette Registry**

** ├── tools/ \# Web App Interaction Utilities**

** └── museum/ \# Pre-baked JSON galaxies (Apollo-11, Linux, etc.)**

### 1.6 The Security & Privacy Protocol: Zero-Trust Local Analysis

# 1.7.1 Overview: \"Your Code Never Leaves Your Computer\"

GitGalaxy is built on a Zero-Trust Privacy Model. GitGalaxy
performs 100% of its scanning, vectorization, and rendering within the
local browser environment.

-   No Data Transmission: Source code is never transmitted to
any API, cloud database, or third-party service.
-   Ephemeral Memory Processing: Repositories are unpacked into
a volatile memory buffer (RAM) and are automatically purged when the
browser tab is closed.
-   Privacy-by-Design: Even when \"uploading\" a repository, the
browser merely reads the local file into a Web Worker; the data
remains behind the user\'s firewall at all times.

# 1.6.2 The \"Privacy Engine\": ZipLoader.js

The technical cornerstone of this protocol is the client-side
ZipLoader, which utilizes the JSZip library to handle repository
ingestion safely:

-   Heuristic Unpacking: The loader identifies source files
while strictly excluding binary blobs, junk folders
(**node_modules**, **\_\_pycache\_\_**, **.git**), and build
artifacts (**dist**, **vendor**).
-   Binary Shield: The loader implements a mandatory null-byte
detection check (**indexOf(\'\\0\')**). If a file contains
non-textual characters, it is immediately discarded to prevent
memory corruption or the unintentional analysis of compiled
binaries.
-   Exclusion Heuristics: To ensure performance and privacy, the
loader prunes any path containing hidden files (starting with **.**)
or common media/font extensions.

# 1.6.3 Implementation Detail: Security Safeguards

-   In-Memory Sanitization: Code is read as string buffers. No
persistent files are ever created on the local file system by the
application.
-   Concurrency Protection: The **isProcessing** guard prevents
memory overflow by ensuring only one unpacking operation occurs at a
time, protecting the user\'s browser stability during large-scale
Tier 4 (Megastructure) scans.
