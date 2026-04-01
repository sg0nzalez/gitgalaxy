# Claim 5 (K-means clusters on language keyword per file.) 

To truly understand software health, we need to stop judging every file by the same generic standard. A frontend UI router should not be penalized for having high concurrency, just as a low-level memory handler shouldn't be penalized for lacking dependency injection. Context matters.

To map the true physical reality of how software is built, we conducted a massive unsupervised machine learning analysis. We fed **over 120 million lines of code across 104 different enterprise codebases** into a K-Means clustering algorithm. We didn't give the AI any human rules about what constitutes "good" or "bad" code. We simply fed it the raw, structural DNA of roughly 465,000 files—regex hit densities, control flow ratios, active security threat payloads, and syntactic markers—and asked it to group them by physical resemblance.

The result? The algorithm naturally separated the half-million files into **16 distinct file archetypes**. 

By labeling every new file we scan with its exact ML Archetype, we can measure its risk scores *relative to its cluster*. We no longer ask, "Is this file too complex?" We ask, "Is this file too complex *for a Unit Test Suite*?" Furthermore, because our matrix now tracks security signatures, we can see exactly which architectural islands are most susceptible to specific vulnerabilities.

## 🧬 The 16 File Archetypes

Here are the 16 archetypes identified by the clustering algorithm. Each micro-species represents a distinct architectural fingerprint based on structural DNA, independent of human-defined folders or logic tags.


**0. Testing & Verification**
The verification layer, characterized by unit test assertions, closures, and intentional safety bypasses. Because it relies heavily on mock data, this cluster naturally isolates test-bound credential leaks and avoids false alarms in production logic.

* **Cluster Size:** 19,615 files (4.2%)
* **Spatial Dispersion:** 3.89 
* **Dominant Languages:** Java (26.8%), Kotlin (22.8%), Groovy (18.2%), Python (12.1%), Dart (9.8%), Other (10.2%)
* **Top Repositories:** elasticsearch (26.0%), kotlin (23.1%), gradle (17.5%), sdk (8.2%), odoo (3.7%), Other (21.5%)
* **Top Signatures:** Unit Test Assertions (+2.62 IQR), Closures/Anonymous Functions (+0.82 IQR), Generic Type Abstractions (+0.71 IQR), Type Safety Bypasses (+0.66 IQR)

**1. Heavy Pointer Implementations**
The low-level procedural architecture. These files are defined by massive pointer arithmetic and preprocessor macro usage, making them highly susceptible to memory corruption vectors.

* **Cluster Size:** 17,436 files (3.7%)
* **Spatial Dispersion:** 5.61
* **Dominant Languages:** C++ (48.5%), C (42.9%), Go (5.1%), Assembly (0.8%), Zig (0.5%), Other (2.2%)
* **Top Repositories:** freebsd-src (38.3%), root (14.0%), godot (7.3%), tensorflow (6.9%), node (6.3%), Other (27.3%)
* **Top Signatures:** Pointer Arithmetic/Addressing (+104.34 IQR), Structural Tab Indentations (+1.38 IQR), Preprocessor Macros (+1.04 IQR), Log Popularity In (+0.94 IQR)

**2. Documented Procedural Logic**
The documented boundaries of low-level systems. Featuring high pointer density but balanced with structured documentation blocks, these files act as the readable interfaces and structural contracts for C, C++, and Go systems.

* **Cluster Size:** 9,752 files (2.1%)
* **Spatial Dispersion:** 7.00
* **Dominant Languages:** C++ (34.8%), C (22.0%), Go (22.0%), Rust (6.3%), Zig (3.3%), Other (11.6%)
* **Top Repositories:** freebsd-src (20.5%), kubernetes (10.0%), tensorflow (8.6%), go (7.0%), node (7.0%), Other (46.8%)
* **Top Signatures:** Pointer Arithmetic/Addressing (+46.51 IQR), Structural Tab Indentations (+1.73 IQR), Log Popularity In (+1.01 IQR), Structured Documentation (+0.91 IQR)

**3. Extreme Memory Manipulation**
The absolute highest-risk zone for memory leaks and buffer overflows. Displaying extreme pointer arithmetic deviation, these files represent the raw, unshielded "meat grinder" of C codebases.

* **Cluster Size:** 5,217 files (1.1%)
* **Spatial Dispersion:** 7.82
* **Dominant Languages:** C (78.5%), C++ (16.9%), Go (3.9%), Assembly (0.2%), Dart (0.2%), Other (0.3%)
* **Top Repositories:** freebsd-src (37.1%), circuitpython (22.0%), root (11.2%), node (7.4%), godot (6.5%), Other (15.8%)
* **Top Signatures:** Pointer Arithmetic/Addressing (+146.64 IQR), Log Popularity In (+1.74 IQR), Preprocessor Macros (+1.36 IQR), Authorship Metadata (+1.26 IQR)

**4. Stateful C/C++ Components**
The active engines of state transformation in low-level systems. These files blend heavy pointers and macros with dense state mutation, variable reassignment, and explicit type casts.

* **Cluster Size:** 15,190 files (3.3%)
* **Spatial Dispersion:** 6.15
* **Dominant Languages:** C++ (43.6%), C (31.2%), Go (14.0%), Rust (3.4%), Zig (2.3%), Other (5.5%)
* **Top Repositories:** freebsd-src (29.2%), tensorflow (9.9%), root (8.6%), kubernetes (7.8%), node (6.7%), Other (37.7%)
* **Top Signatures:** Pointer Arithmetic/Addressing (+77.91 IQR), Structural Tab Indentations (+1.59 IQR), Log Popularity In (+0.89 IQR), Preprocessor Macros (+0.87 IQR)

**5. Annotated Object-Oriented Structures**
The connective tissue of enterprise applications. Defined by massive decorator and annotation density, generic type abstractions, and strict encapsulation.

* **Cluster Size:** 54,271 files (11.7%)
* **Spatial Dispersion:** 4.21
* **Dominant Languages:** Java (49.6%), Dart (10.6%), Kotlin (9.9%), Python (8.6%), C# (7.3%), Other (14.2%)
* **Top Repositories:** elasticsearch (26.2%), gradle (10.7%), kotlin (9.3%), odoo (8.2%), kafka (5.9%), Other (39.7%)
* **Top Signatures:** Decorators And Annotations (+4.77 IQR), Generic Type Abstractions (+1.17 IQR), Private Encapsulated Scopes (+0.94 IQR), Closures (+0.91 IQR)

**6. Complex C/Go Systems**
High-complexity system files balancing moderate pointer math with strict private encapsulated scopes and explicit type casts. They serve as safe operational boundaries for memory management.

* **Cluster Size:** 6,407 files (1.4%)
* **Spatial Dispersion:** 7.80
* **Dominant Languages:** C++ (30.2%), Go (23.2%), C (19.2%), Rust (6.7%), C# (3.9%), Other (16.8%)
* **Top Repositories:** freebsd-src (17.1%), kubernetes (9.7%), go (9.6%), tensorflow (7.3%), node (7.2%), Other (49.0%)
* **Top Signatures:** Pointer Arithmetic/Addressing (+26.50 IQR), Structural Tab Indentations (+1.72 IQR), Log Popularity In (+1.00 IQR), Log Max Func Complexity (+0.88 IQR)

**7. High-Density Macros & Pointers**
Algorithmic and heavily preprocessed C/C++ files. These are driven by massive macro expansion, pointer arithmetic, and exposed public exports that interact directly with the compiler.

* **Cluster Size:** 13,580 files (2.9%)
* **Spatial Dispersion:** 6.09
* **Dominant Languages:** C (64.4%), C++ (28.5%), Go (6.2%), Assembly (0.2%), Zig (0.1%), Other (0.6%)
* **Top Repositories:** freebsd-src (48.7%), root (13.0%), godot (7.1%), node (6.5%), kubernetes (4.9%), Other (19.8%)
* **Top Signatures:** Pointer Arithmetic/Addressing (+129.72 IQR), Structural Tab Indentations (+1.83 IQR), Log Max Func Complexity (+1.02 IQR), Preprocessor Macros (+1.01 IQR)

**8. High-Dependency Keystones**
The 'God Nodes' of a codebase. These files possess massive inbound popularity and heavy macro usage, acting as the structural pillars that hold the rest of the application together. Changes here have a massive blast radius.

* **Cluster Size:** 23,903 files (5.1%)
* **Spatial Dispersion:** 4.60
* **Dominant Languages:** C++ (46.3%), C (35.1%), Java (5.7%), Python (2.9%), Dart (1.8%), Other (8.3%)
* **Top Repositories:** freebsd-src (25.3%), tensorflow (18.2%), node (7.8%), root (5.8%), circuitpython (4.8%), Other (38.2%)
* **Top Signatures:** Log Popularity In (+2.80 IQR), Preprocessor Macros (+2.53 IQR), Authorship Metadata (+1.45 IQR), Metaprogramming/Reflection (+0.93 IQR)

**9. Formatting Outliers & Configs**
Files with massive structural formatting deviations (e.g., extreme tab indentation). Heavily composed of TypeScript, PHP, and Shell scripts, these files often define I/O boundaries and network configurations.

* **Cluster Size:** 36,139 files (7.8%)
* **Spatial Dispersion:** 4.42
* **Dominant Languages:** TypeScript (15.2%), Go (13.2%), PHP (12.8%), Shell (12.6%), JSON (11.4%), Other (34.8%)
* **Top Repositories:** freebsd-src (27.9%), mediawiki (19.3%), vscode (18.2%), go (7.9%), kubernetes (4.9%), Other (21.9%)
* **Top Signatures:** Structural Tab Indentations (+4.02 IQR), Structured Documentation (+1.00 IQR), Type Safety Bypasses (+0.71 IQR), Private Encapsulated Scopes (+0.64 IQR)

**10. Static Configuration & Data**
Structural dark matter. Highly static, consisting of inert data, YAML, JSON, and PBTXT. However, because it lacks executable logic, this cluster frequently acts as a host for homoglyph evasion and hardcoded secrets.

* **Cluster Size:** 106,635 files (22.9%)
* **Spatial Dispersion:** 2.75
* **Dominant Languages:** Kotlin (16.8%), YAML (15.3%), PBTXT (7.1%), Python (6.9%), JSON (5.5%), Other (48.4%)
* **Top Repositories:** kotlin (19.0%), freebsd-src (12.8%), tensorflow (9.8%), discourse (7.7%), kubernetes (6.7%), Other (44.0%)
* **Top Signatures:** Class Entity Declarations (+0.26 IQR), Structured Documentation (+0.24 IQR), Exposed API Public Exports (+0.21 IQR), Log Popularity In (+0.20 IQR)

**11. Highly Documented Native Code**
The well-defined architectural blueprints of C/C++ systems. These files pair heavy pointer arithmetic with extensive, structured documentation blocks, bridging the gap between raw hardware execution and human intent.

* **Cluster Size:** 17,583 files (3.8%)
* **Spatial Dispersion:** 5.64
* **Dominant Languages:** C (51.9%), C++ (41.7%), Go (4.7%), Assembly (0.4%), Zig (0.2%), Other (1.1%)
* **Top Repositories:** freebsd-src (43.3%), root (14.1%), node (7.5%), godot (7.4%), tensorflow (4.2%), Other (23.4%)
* **Top Signatures:** Pointer Arithmetic/Addressing (+116.83 IQR), Structural Tab Indentations (+1.52 IQR), Preprocessor Macros (+1.05 IQR), Log Max Func Complexity (+0.99 IQR)

**12. Complex Control Flow & Defensive Logic**
The baseline execution layer of modern software. High in defensive programming, generics, and closures, these files gracefully handle state flux and exceptions.

### Thoughts
One of the most profound discoveries of this clustering process is that not a single architectural micro-species is composed of only one programming language.

Before feeding the telemetry into the K-Means algorithm, we deliberately blinded the model to the file extension, the repository name, and the human-assigned language. The AI had no idea if it was looking at a Java file, a Python script, or a C++ header. It was forced to group files based purely on their structural physics—their control flow density, architectural mass, structural logic branches, and usage of abstractions like generics or pointers.

The result is a taxonomical map that proves intent scales across syntax.

The algorithm mathematically recognized that a massive, heavily annotated Java Service class (Cluster 13) has far more in common with a robust C# Dependency Injection file than it does with a simple Java data model. It recognized that a dense, highly defensive Python script (Cluster 12) shares the exact same structural DNA as a defensively written Kotlin file.

By grouping code by its physical behavior rather than its file extension, we have created a truly language-agnostic map of software architecture.

By having a mathematical definition of 16 file architypes not only can we assess entire repos by the ratios of these file types (an OS has a very different profile than a web app in cluster percentages) and assess what a project actually is by composition, but we can also assess how statistically deviant those files are from the cluster centroid and provide quality assessments on the files fit. We also keep track of poorly fitted points and highlight those, this indicates when we have a true need for drift, that some file file is literally half way betweeen two file types, trying to do two jobs at once! 

### Appendix: The 104 Repository Training Set
The archetypes above were derived mathematically by scanning the following enterprise, open-source, and historical repositories:

> abap-cleaner, abap2xlsx, abapGit, AFNetworking, Alamofire, alphafold_2018, angr, ansible, apex-recipes, AppFlowy, Apollo-11, bevy, bitcoin-0.1.0, blast, brew, bugzilla, bun, cics-genapp, circuitpython, cobol-check, cobol-programming-course, cpython, curl, discourse, django, DOOM, eeglab, elasticsearch, exiftool, express, fflib-apex-common, fieldtrip, fineract, flask, flutter, freebsd-src, ghostty, gitgalaxy, gnucobol, gnupg, go, godot, gradle, impacket, iwubi, jellyfin, jenkins, kafka, kotlin, kubernetes, laravel, linux-1.0, livecode, macports-base, mediawiki, micropython, micropython-ulab, moby, node, nvda, odoo, okhttp, opencv, openclaw-typescript, openzeppelin-contracts, pandoc, pandas, platform_dalvik, PowerShell, PowerToys, prometheus, pwntools, pyarmor, racket, rails, react, redis, retrofit, ripgrep, root, roslyn, scapy, sdk, spamassassin, spm12, spock, spring-boot, sqlite, sqlmap, srfi-1, swift, tauri, tcpip_historical, tensorflow, terraform, tigerbeetle, tokio, vapor, voyager, vscode, vue, wordpress, WorldWideWeb, wrf-fortran
