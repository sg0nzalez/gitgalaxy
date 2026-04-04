# Claim 5 (K-means clusters on language keyword per file.) 

To truly understand software health, we need to stop judging every file by the same generic standard. A frontend UI router should not be penalized for having high concurrency, just as a low-level memory handler shouldn't be penalized for lacking dependency injection. Context matters.

To map the true physical reality of how software is built, we conducted a massive unsupervised machine learning analysis. We fed **over 174 million lines of code across 255 different enterprise codebases** into a K-Means clustering algorithm. We didn't give the AI any human rules about what constitutes "good" or "bad" code. We simply fed it the pure, structural DNA of **1.25 million files**—regex hit densities, control flow ratios, active security threat payloads, and syntactic markers—and asked it to group them by physical resemblance. 

*Crucially, we stripped out all formatting lint (Tabs vs. Spaces).* The AI was forced to look past the "paint" and strictly evaluate the architectural "plumbing."

The result? The algorithm naturally separated the 1.25 million files into **16 distinct architectural micro-species**. 

By labeling every new file we scan with its exact ML Archetype, we can measure its risk scores *relative to its cluster*. We no longer ask, "Is this file too complex?" We ask, "Is this file too complex *for a UI Framework component*?" Furthermore, because our matrix tracks security signatures, we can see exactly which architectural islands are most susceptible to specific vulnerabilities.

---

## 🧬 The 16 File Archetypes

Here are the 16 archetypes identified by the clustering algorithm. Each micro-species represents a distinct architectural fingerprint based on structural DNA, independent of human-defined folders or logic tags.

### **Cluster 0: Annotated Service Layer**
The backend connective tissue. This cluster is defined by its massive reliance on decorators to wire up services, define REST mappings, and inject dependencies, forming the backbone of enterprise Spring Boot and Kotlin architectures.
* **Size:** 82,449 files (6.6%) | **Dispersion:** 3.97
* **Dominant Languages:** Java (36.1%), Kotlin (19.9%), JavaScript (10.8%), TypeScript (6.7%), C# (6.0%)
* **Top Origins:** `kotlin` (24.1%), `gradle` (9.9%), `elasticsearch` (7.4%), `spring-boot` (7.1%)
* **Defining DNA:**
    * **Decorators & Annotations:** +6.38 IQR
    * **Class Entity Declarations:** +1.15 IQR
    * **Structured Documentation:** +1.03 IQR
    * **Private Encapsulated Scopes:** +0.78 IQR
    * **Exposed API / Public Exports:** +0.65 IQR

### **Cluster 1: Universal Dependencies (The God Nodes)**
The architectural anchors of the modern web stack. These are highly imported utility modules, core type definitions, and central configuration hubs that possess a massive "blast radius" across the repository.
* **Size:** 49,853 files (4.0%) | **Dispersion:** 4.57
* **Dominant Languages:** TypeScript (24.6%), Java (12.8%), JavaScript (12.7%), Python (9.9%), C (9.7%)
* **Top Origins:** `swc` (8.1%), `elasticsearch` (7.2%), `gutenberg` (6.8%), `freebsd-src` (5.8%)
* **Defining DNA:**
    * **Inbound Popularity (Imported By):** +5.51 IQR
    * **Structured Documentation:** +0.93 IQR
    * **Decorators & Annotations:** +0.71 IQR
    * **Generic Type Abstractions:** +0.59 IQR
    * **Defensive Constructs:** +0.57 IQR

### **Cluster 2: Inert Configuration & Data (The Dark Matter)**
The largest single cluster in the galaxy. Highly static and dense, consisting of inert data structures, JSON configs, YAML pipelines, and Makefiles. It completely lacks executable control flow but is essential for orchestrating environments.
* **Size:** 275,516 files (21.9%) | **Dispersion:** 2.01 *(Extremely tight grouping)*
* **Dominant Languages:** JSON (18.2%), JavaScript (13.7%), YAML (12.8%), TypeScript (7.7%), Makefile (6.2%)
* **Top Origins:** `freebsd-src` (14.1%), `swc` (10.8%), `tensorflow` (7.3%), `TypeScript` (6.8%)
* **Defining DNA:**
    * **Inbound Popularity:** +0.23 IQR
    * **State Mutations / Reassignments:** +0.21 IQR
    * **I/O & Network Boundaries:** +0.20 IQR

### **Cluster 3: High-Density Dependency Injection**
Complex object-oriented blueprints. Characterized by incredibly high generic abstractions and decorator density, this cluster defines the heavily typed, encapsulated interfaces of robust backend systems.
* **Size:** 86,997 files (6.9%) | **Dispersion:** 3.94
* **Dominant Languages:** Java (51.0%), Python (10.3%), Rust (8.7%), Dart (7.4%), Kotlin (7.0%)
* **Top Origins:** `elasticsearch` (25.0%), `gradle` (10.5%), `kotlin` (7.3%), `sdk` (4.4%)
* **Defining DNA:**
    * **Decorators & Annotations:** +3.78 IQR
    * **Generic Type Abstractions:** +1.54 IQR
    * **Private Encapsulated Scopes:** +1.51 IQR
    * **Structured Documentation:** +1.28 IQR
    * **Max Function Complexity:** +1.06 IQR

### **Cluster 4: Software Verification & Testing**
The QA layer. Because it relies heavily on mock data, closures, and intentional constraint bypasses, this cluster naturally isolates test-bound logic and avoids polluting the primary execution architecture.
* **Size:** 45,404 files (3.6%) | **Dispersion:** 3.73
* **Dominant Languages:** Java (21.2%), Python (15.1%), Groovy (13.7%), TypeScript (13.6%), Kotlin (12.2%)
* **Top Origins:** `elasticsearch` (20.8%), `gradle` (13.1%), `kotlin` (12.7%)
* **Defining DNA:**
    * **Unit Test Assertions:** +2.78 IQR
    * **Closures & Anonymous Functions:** +1.05 IQR
    * **Max Function Complexity:** +0.80 IQR
    * **Defensive Constructs:** +0.69 IQR
    * **Type Safety Bypasses:** +0.61 IQR

### **Cluster 5: Build, Infra & I/O Automation**
The DevOps and scripting "Wild West." These files throw safety to the wind to automate builds, execute shell commands, and read/write to disks and networks. They form the automated scaffolding of the software lifecycle.
* **Size:** 28,618 files (2.3%) | **Dispersion:** 4.46
* **Dominant Languages:** Shell (50.2%), JavaScript (17.9%), Python (10.2%), TypeScript (6.0%)
* **Top Origins:** `freebsd-src` (39.3%), `TypeScript` (7.7%), `swc` (7.5%), `kotlin` (5.7%)
* **Defining DNA:**
    * **Type Safety Bypasses:** +3.12 IQR
    * **I/O & Network Boundaries:** +1.46 IQR
    * **Metaprogramming & Reflection:** +1.19 IQR
    * **Defensive Constructs:** +1.00 IQR
    * **Ad Hoc Print / Debugs:** +0.98 IQR

### **Cluster 6: High-Dependency C Headers**
The foundational core of operating systems and native runtimes. These files act as the central neurological pathways for C/C++ repositories, driven by high inbound popularity, preprocessor macros, and pointer math.
* **Size:** 37,620 files (3.0%) | **Dispersion:** 3.88
* **Dominant Languages:** C (60.1%), C++ (39.5%)
* **Top Origins:** `freebsd-src` (39.1%), `node` (9.8%), `circuitpython` (7.4%), `root` (6.7%)
* **Defining DNA:**
    * **Pointer Arithmetic / Addressing:** +3.04 IQR
    * **Inbound Popularity:** +3.01 IQR
    * **Preprocessor Macros:** +2.47 IQR
    * **Authorship Metadata:** +1.22 IQR
    * **Class Entity Declarations:** +0.99 IQR

### **Cluster 7: Raw Pointer & Memory Manipulation**
The "Meat Grinder." This is the raw, unshielded execution layer of native codebases. It is defined by extreme pointer arithmetic, complex branching, and dense state mutation, making it the highest-risk zone for memory leaks.
* **Size:** 122,369 files (9.7%) | **Dispersion:** 3.27
* **Dominant Languages:** C (51.3%), C++ (41.8%), Go (3.4%)
* **Top Origins:** `freebsd-src` (39.9%), `tensorflow` (9.6%), `root` (7.6%), `node` (7.5%)
* **Defining DNA:**
    * **Pointer Arithmetic / Addressing:** +3.05 IQR
    * **Max Function Complexity:** +1.44 IQR
    * **State Mutations / Reassignments:** +1.18 IQR
    * **Explicit Type Casts:** +0.88 IQR
    * **Control Flow Ratio:** +0.79 IQR

### **Cluster 8: Test-Driven Annotated Services**
Enterprise-grade integration testing. These files pair massive dependency injection footprints (decorators) with extensive unit test assertions, ensuring that complex Java/C# backend flows behave predictably.
* **Size:** 44,224 files (3.5%) | **Dispersion:** 3.57
* **Dominant Languages:** Java (40.1%), Python (15.7%), Kotlin (10.0%), C# (9.8%), Groovy (8.5%)
* **Top Origins:** `elasticsearch` (14.2%), `spring-boot` (9.9%), `gradle` (9.0%), `roslyn` (8.4%)
* **Defining DNA:**
    * **Decorators & Annotations:** +4.13 IQR
    * **Unit Test Assertions:** +2.54 IQR
    * **Generic Type Abstractions:** +0.81 IQR
    * **Closures & Anonymous Functions:** +0.81 IQR

### **Cluster 9: Functional OOP & Async Logic**
Modern, non-blocking execution logic. Primarily composed of JavaScript and Dart, these files are defined by asynchronous callbacks, closures, and highly fluid object-oriented structures executing concurrent flows.
* **Size:** 54,103 files (4.3%) | **Dispersion:** 3.95
* **Dominant Languages:** JavaScript (28.9%), Dart (22.3%), TypeScript (21.9%), C# (7.8%)
* **Top Origins:** `sdk` (18.9%), `swc` (11.6%), `TypeScript` (9.9%)
* **Defining DNA:**
    * **Closures & Anonymous Functions:** +2.56 IQR
    * **Asynchronous/Concurrent Execution:** +0.65 IQR
    * **Generic Type Abstractions:** +0.61 IQR
    * **Defensive Constructs:** +0.58 IQR

### **Cluster 10: Object-Oriented Structures**
The pure class entity layer. Focused strictly on declaring structural objects and types with very little internal logic. Kotlin and TypeScript use these as foundational data models and rigid interfaces.
* **Size:** 84,085 files (6.7%) | **Dispersion:** 3.41
* **Dominant Languages:** Kotlin (39.5%), TypeScript (11.8%), Java (9.1%), Ruby (7.5%)
* **Top Origins:** `kotlin` (41.3%), `TypeScript` (8.4%), `discourse` (6.3%)
* **Defining DNA:**
    * **Class Entity Declarations:** +1.86 IQR
    * **Generic Type Abstractions:** +1.10 IQR
    * **Immutable Data Declarations:** +0.47 IQR
    * **Private Encapsulated Scopes:** +0.44 IQR

### **Cluster 11: Algorithmic & Defensive Logic**
The complex brains of the application. These files feature massive branching and maximum function complexities, tightly wrapped in heavy defensive try/catch blocks and null-safety nets to prevent the algorithms from exploding.
* **Size:** 126,797 files (10.1%) | **Dispersion:** 3.94
* **Dominant Languages:** TypeScript (16.6%), Kotlin (14.4%), Python (11.4%), JavaScript (8.6%), Go (7.9%)
* **Top Origins:** `kotlin` (13.8%), `roslyn` (4.3%), `spm12` (4.1%)
* **Defining DNA:**
    * **Max Function Complexity:** +1.47 IQR
    * **Defensive Constructs:** +1.41 IQR
    * **Private Encapsulated Scopes:** +0.96 IQR
    * **Control Flow Ratio:** +0.96 IQR
    * **Logic LOC:** +0.70 IQR

### **Cluster 12: Documented Core Interfaces**
The well-explained borders of the system. These files are characterized by an extreme density of structured documentation blocks (GoDocs, JSDocs, PyDocs) sitting directly above private scopes and entity boundaries.
* **Size:** 91,710 files (7.3%) | **Dispersion:** 3.99
* **Dominant Languages:** Go (21.9%), Python (14.2%), Java (13.4%), PHP (12.1%), C# (10.8%)
* **Top Origins:** `kubernetes` (10.1%), `mediawiki` (8.7%), `go` (7.4%)
* **Defining DNA:**
    * **Structured Documentation Blocks:** +3.52 IQR
    * **Private Encapsulated Scopes:** +1.38 IQR
    * **Class Entity Declarations:** +0.81 IQR
    * **Exposed API / Public Exports:** +0.69 IQR

### **Cluster 13: Documented Native Headers**
The highly-readable C/C++ architecture definitions. These files pair raw hardware execution paths (pointers and casts) with deep structural explanations and metadata, outlining how native systems should interact.
* **Size:** 31,318 files (2.5%) | **Dispersion:** 4.05
* **Dominant Languages:** C++ (81.5%), C (15.6%)
* **Top Origins:** `root` (36.2%), `freebsd-src` (20.6%), `godot` (15.0%)
* **Defining DNA:**
    * **Structured Documentation Blocks:** +3.76 IQR
    * **Pointer Arithmetic / Addressing:** +2.69 IQR
    * **Inbound Popularity:** +2.17 IQR
    * **Preprocessor Macros:** +1.58 IQR
    * **Explicit Type Casts:** +1.21 IQR

### **Cluster 14: UI Frameworks & View Layers**
The visual rendering engine. Isolated flawlessly by the algorithm, this cluster represents the frontend DOM manipulation of React, Angular, and Flutter, driven by extreme decorator usage mapping to UI View Layer components.
* **Size:** 49,238 files (3.9%) | **Dispersion:** 3.92
* **Dominant Languages:** JavaScript (39.1%), TypeScript (36.9%), Dart (8.8%), HTML (4.3%)
* **Top Origins:** `material-ui` (21.1%), `odoo` (7.9%), `Rocket.Chat` (7.4%)
* **Defining DNA:**
    * **Decorators & Annotations:** +3.87 IQR
    * **UI / View Layer Components:** +1.68 IQR
    * **Closures & Anonymous Functions:** +0.97 IQR
    * **Inbound Popularity:** +0.87 IQR
    * **Generic Type Abstractions:** +0.82 IQR

### **Cluster 15: Preprocessor Macros & Metaprogramming**
The native reflection layer. This cluster represents the deeply embedded C/C++ files that generate code at compile-time via massive macro sets and explicit type casts to bend the compiler to their will.
* **Size:** 45,594 files (3.6%) | **Dispersion:** 3.68
* **Dominant Languages:** C (55.4%), C++ (42.4%)
* **Top Origins:** `freebsd-src` (29.6%), `tensorflow` (17.8%), `zig` (14.1%)
* **Defining DNA:**
    * **Preprocessor Macros:** +3.34 IQR
    * **Inbound Popularity:** +1.58 IQR
    * **Authorship Metadata:** +1.54 IQR
    * **Metaprogramming & Reflection:** +1.00 IQR
    * **Explicit Type Casts:** +0.51 IQR

---

### Thoughts
One of the most profound discoveries of this clustering process is that **not a single architectural micro-species is composed of only one programming language.**

Before feeding the telemetry into the K-Means algorithm, we deliberately blinded the model to the file extension, the repository name, and the human-assigned language. The AI had no idea if it was looking at a Java file, a Python script, or a C++ header. It was forced to group files based purely on their structural physics—their control flow density, architectural mass, structural logic branches, and usage of abstractions like generics or pointers.

The result is a taxonomical map that proves **intent scales across syntax.**

The algorithm mathematically recognized that a massive, heavily annotated Java Service class (Cluster 0) has far more in common with a robust TypeScript Dependency Injection file than it does with a simple Java data model. It recognized that a dense, highly defensive Python script (Cluster 11) shares the exact same structural DNA as a defensively written Kotlin file.

By grouping code by its physical behavior rather than its file extension, we have created a truly language-agnostic map of software architecture.

By having a mathematical definition of 16 file archetypes, not only can we assess entire repos by the ratios of these file types (an OS would have a very different ratio profile than a web app) and assess what a project actually is by composition, but we can also assess how statistically deviant those files are from the cluster centroid and provide quality assessments on the file's fit. We also keep track of poorly fitted points and highlight those. This indicates when we have a true need for refactoring, we measure cluster drift — that some file is literally halfway between two file archetypes, trying to do two jobs at once!

### Appendix: The 255 Repository Training Set
The archetypes above were derived mathematically by scanning 174,068,615 lines of code across the following enterprise, open-source, and historical repositories:

> pytudes, Apollo-11, wtfpython, DOOM, gnupg, substrate, linux-1.0, sqlite, twisted, actix-web, solana, cargo, tokio, hyperion, rust-analyzer, zellij, node, scikit-learn, freeCodeCamp, pandas, redis, wgpu, scapy, spm12, wasmtime, scipy, bugzilla, root, esbuild, numpy, okhttp, syn, abapGit, libxev, networkx, content, nushell, freebsd-src, PowerShell, gitgalaxy, excalidraw, ripgrep, eeglab, mach, pypy, vscode, rdkit, tensorflow, abap-cleaner, pip, react, serde, deno, three.js, fieldtrip, microzig, Alamofire, kivy, mypy, swift, nvda, impacket, prometheus, hyper, pygments, pyarmor, cpython, ghostty, zls, cesium, mediawiki, ngl, Python, terraform, arktype, sqlmap, core, tigerbeetle, flutter, zod, nx, openclaw-typescript, sentry, pixijs, angular, angr, gutenberg, pandoc, kubernetes, apex-recipes, workers-sdk, tauri, exiftool, gnucobol, roslyn, airflow, desktop, reveal.js, pwntools, river, setuptools, spamassassin, spock, django, assemblyscript, cics-banking-sample-appli..., micropython, Zig, pyqtgraph, godot, vscode_cobol, lazygit, Excalibur, kafka, rails, cyber, bitcoin-0.1.0, bevy, igv.js, javascript-algorithms, bog, sdk, vue, esphome, AppFlowy, canvas-lms, GitPython, rich, mikro-orm, typeorm, cython, openzeppelin-contracts, type-fest, retrofit, bun, selenium, docker-py, zap, textual, http.zig, react-router, micropython-ulab, storybook, puppeteer, jedi, vapor, playwright, zig-okredis, jellyfin, opencv, cobrix, black, gradle, ncdu, elasticsearch, react-flow, odoo, platform_dalvik, prisma, cypress, AFNetworking, swc, circuitpython, spring-boot, cics-genapp, fineract, flask, jenkins, racket, kotlin, che-che4z-lsp-for-cobol, fastapi, ionic-framework, Rocket.Chat, Cobol-Projects, trpc, ansible, PowerToys, discourse, bootloader, WorldWideWeb, ant-design, fp-ts, zig, blast, cobol-check, tailwindcss, cytoscape.js, pylint, grafana, tornado, prettier, python-patterns, cobol-programming-course, bootstrap, fd, next.js, cics-java-jcics-samples, brew, jquery, Chart.js, TypeScript, curve25519-dalek, Mainframe, nest, curl, express, cli, otterkit, wordpress, biopython, alphafold_2018, zopeneditor-sample, COBOL_Tutorial, sokol-zig, quote, cobol-samples, CICS-Cobol, typescript-eslint, moment, pywat, wrf-fortran, cobol-dialect-template, moby, voyager, material-ui, jcl-assess, srfi-1, go, DOOM-fire-zig, berry, redox, zigup, laravel, capy, livecode, macports-base, tcpip_historical, language-cobol, poop (NOTE: I asked the LLM for edge case repos and it literally brought me ****, but what is a good data set without real world ****, so it stays.), html5-boilerplate, iwubi, learning-cobol, Adafruit_CircuitPython_Bu..., awesome-cobol, code4z, d3, cash-account-cobol, Babylon.js, type-challenges, zig-book, alacritty, COBOL-Guide, ziglings, zig-gamedev
