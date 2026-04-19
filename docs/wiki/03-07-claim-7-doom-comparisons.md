# Tracking the Genetic Drift of DOOM: A GitGalaxy Stress Test

Building a multi-language static analysis engine is notoriously difficult. Every programming language operates on its own unique physical laws. C relies on raw memory and macro expansion, C# forces strict object-oriented hierarchies, and JavaScript lives and dies by event-driven closures. 

So, how do you prove that a multi-language scanner actually understands *architecture*? How do you prove it can compare apples to oranges, rather than just counting syntax tokens? 

You need a Rosetta Stone. A singular, highly complex system that has been translated into almost every programming paradigm imaginable. You need a baseline to see what structural DNA emerges, what similarities survive the translation, and what gets completely lost in the void. This is exactly the kind of cross-language comparative intelligence that tools like **GitGalaxy** were built for.

And when it comes to a universal benchmark, every engineer knows the answer: **DOOM**. 

To run the ultimate stress test on GitGalaxy’s architectural mapping, we ingested the original 1997 id Software C repository. Then, we immediately threw a gauntlet of architectural whiplash at the scanner: ESP32 microcontroller ports, C# object-oriented rewrites, ASCII terminal renderers, and even a completely cursed CSS/DOM mutation. 

The goal was simple: **Can an engine trace the "architectural genetics" of John Carmack’s masterpiece across decades of mutation and entirely different programming languages?**

The telemetry we extracted was mind-blowing. Here is what happens to the DNA of DOOM when it gets dragged across the multiverse.

---

## The Architecture of a Legend

### 🧬 The Indestructible "God Nodes" (C & C++)
Modern software engineering preaches decoupled microservices and strict dependency injection. Early 90s game development did not care. 

When GitGalaxy mapped the original 1997 source, it revealed an architecture completely dominated by what our ML archetypes classify as **Cluster 8: Universal Dependencies (The God Nodes)** and **Cluster 13: Documented Native Headers**. 

The entire engine revolved around a few massive, centralized files like `doomdef.h` and `i_system.h` that acted as the gravitational center of the repository. 

Amazingly, this structural fingerprint is practically bulletproof. When we scanned the `doomgeneric`, `esp32-doom`, and `rp2040-doom` ports, the exact same planetary bodies formed the center of the galaxy. Even when developers shoved the game into memory-constrained microcontrollers, the "God Node" paradigm survived the hardware constraints completely intact.

### 🏛️ The Load-Bearing Pillars Survive the Jump (C#)
What happens when you translate 1997 C code into a modern, garbage-collected, strictly-typed language like C#? 

We fed `ManagedDoom` into GitGalaxy to find out. Despite the language shift, the scanner’s "Satellite Hitlist" caught the exact same monolithic functions doing the heavy lifting. 

In the original C code, functions like `P_UseSpecialLine` (handling doors, switches, and elevators) and `G_Ticker` (the main game loop) registered as the most massive, highly-coupled logic blocks in the system. In the C# rewrite, `UseSpecialLine` and `CrossSpecialLine` still registered as the heaviest, most complex functions in the entire 44,000-line repository. They dropped the `P_` prefix, but the structural mass of the logic remained completely identical. 

GitGalaxy proved that across languages, the C# port is a direct, faithful descendant of the original brain. 

### 👽 The Alien Mutants: The CSS Dimension
This is where the structural whiplash occurs. We wanted to see what happens when you render DOOM entirely through HTML `<div>` tags and CSS 3D transforms (`cssDOOM`). 

When the scanner chewed through the TypeScript/CSS ports, the original DOOM DNA completely vaporized. 
* **The Paradigm Shift:** The codebase abandoned the "God Node" clusters entirely, shifting heavily into **Cluster 1: I/O, UI & Scripting Automation**. 
* **The Missing Pillars:** The legendary game loop and spatial logic were gone. Instead, GitGalaxy identified UI-centric functions like `initKeyboardInput` and `getCharClassName` as the heaviest structural pillars. 

The CSS ports are DOOM in visual spirit only. Structurally, they are modern frontend web applications operating on completely different physical laws than the original C codebase.

---

## The Telemetry: Cross-Dimensional Breakdown

To keep the data readable, we split the repositories into two distinct families: **The C-Lineage** (direct descendants and microcontroller ports) and **The Language Mutants** (C#, Rust, and web framework ports).

### Part 1: The C-Lineage (The Direct Descendants)
These are the repositories that stayed relatively true to the original 1997 C architecture, simply adapting the IO and rendering layers for specific hardware.

| Metric | Original DOOM | DoomGeneric | ESP32 DOOM | RP2040 DOOM | ASCII DOOM |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Dominant Language** | C (93.3%) | C (98.9%) | C (90.8%) | C (86.0%) | C (97.2%) |
| **Total Artifacts** | 165 | 211 | 203 | 779 | 193 |
| **Total LOC** | 29,778 | 37,171 | 45,583 | 198,081 | 37,116 |
| **Top Archetype 1** | Cluster 13 (Native Headers): 42.7% | Cluster 13 (Native Headers): 43.2% | Cluster 13 (Native Headers): 38.9% | Cluster 8 (God Nodes): 33.4% | Cluster 13 (Native Headers): 43.6% |
| **Top Archetype 2** | Cluster 8 (God Nodes): 38.7% | Cluster 8 (God Nodes): 40.0% | Cluster 8 (God Nodes): 34.1% | Cluster 13 (Native Headers): 32.1% | Cluster 8 (God Nodes): 37.0% |
| **Heaviest Function 1** | `P_UseSpecialLine` (Impact: 194.9) | `convertToDoomKey` (Impact: 229.7) | `P_UseSpecialLine` (Impact: 457.8) | `P_ExecuteLineSpecial` (Impact: 477.1) | `P_UseSpecialLine` (Impact: 194.9) |
| **Heaviest Function 2** | `D_DoomMain` (Impact: 172.2) | `DG_GetKey` (Impact: 224.4) | `M_Responder` (Impact: 352.0) | `convert_textures` (Impact: 436.4) | `P_CrossSpecialLine` (Impact: 192.0) |
| **Mean Cog Load** | 24.9 | 24.1 | 26.9 | 24.8 | 22.8 |
| **Mean API Exposure** | 76.7 | 82.8 | 78.2 | 75.0 | 81.9 |
| **Mean State Flux** | 4.6 | 4.8 | 5.3 | 4.6 | 4.8 |

**The C-Lineage Verdict:** The engine successfully proved these are the exact same game. The structural mass, the "God Node" dependencies, and the average cognitive loads are nearly identical across the board. The only massive outlier is the RP2040 port, which ballooned to nearly 200k LOC because the developers crammed the source code for several games (*Hexen*, *Strife*, and *Heretic*) into a single repo, skewing the overall volume.

### Part 2: The Language Mutants (C#, Rust, and CSS/Web)
These are the systems that attempted to port the logic to entirely different programming paradigms, resulting in massive architectural drift.

| Metric | C# Managed | Rust LiDoom | Rust Generic | CSS Pure | CSS TypeScript |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Dominant Language** | C# (99.2%) | RUST (80.0%) | RUST (75.0%) | JS (57.4%) | TS (76.1%) |
| **Total Artifacts** | 350 | 18 | 9 | 1047 | 273 |
| **Total LOC** | 44,874 | 640 | 136 | 6,750 | 3,633 |
| **Top Archetype 1** | Cluster 8 (God Nodes): 46.6% | Cluster 8 (God Nodes): 30.0% | Cluster 9 (OOP/Async): 50.0% | Cluster 10 (OO Structures): 29.8% | Cluster 8 (God Nodes): 44.9% |
| **Top Archetype 2** | Cluster 2 (Data Configs): 38.5% | Cluster 10 (OO Structures): 20.0% | Cluster 16 (Docs): 25.0% | Cluster 2 (Data Configs): 24.5% | Cluster 2 (Data Configs): 31.9% |
| **Heaviest Function 1** | `UseSpecialLine` (Impact: 370.9) | `run` (Impact: 58.1) | `DG_GetKey` (Impact: 12.9) | `initKeyboardInput` (Impact: 131.0) | `getCharClassName` (Impact: 39.9) |
| **Heaviest Function 2** | `CrossSpecialLine` (Impact: 358.6) | `run` (Impact: 50.1) | `from_char` (Impact: 6.3) | `updateCulling` (Impact: 125.3) | `render` (Impact: 16.6) |
| **Mean Cog Load** | 6.5 | 24.0 | 8.1 | 11.2 | 11.6 |
| **Mean API Exposure** | 53.1 | 18.9 | 33.9 | 42.8 | 24.8 |
| **Mean State Flux** | 4.7 | 4.3 | 3.6 | 4.1 | 4.9 |

**The Mutants Verdict:** 1. **The C# Mirror:** The C# port (`ManagedDoom`) is the only port here that actually retained the true DNA of the game. Despite the language change, the core functions (`UseSpecialLine`) carried the exact same structural mass as the original C code. However, because C# enforces strong Object-Oriented patterns, the average Cognitive Load plummeted from the 20s down to 6.5.
2. **The Rust Phantoms:** GitGalaxy immediately exposed the Rust repos. They aren't full ports; at under 700 lines of code, they are just tiny UI wrappers hooking into external binaries. 
3. **The CSS Void:** The DOM/CSS ports completely lost the architectural thread. The core physical pillars of the game vanished, replaced by UI rendering logic and generic frontend archetypes.

---

## 🔭 Why This Matters

Codebases evolve, mutate, and rot. A standard linter will tell you if you missed a semicolon, but it won't tell you when your architecture has fundamentally shifted beneath your feet. 

By mapping the syntactic physics of a repository—measuring the density of state mutations, the blast radius of dependencies, and the sheer structural mass of individual functions—GitGalaxy doesn't just show you lines of code. It reveals the load-bearing pillars holding your system together, the dangerous blind spots lurking in the dark matter, and the exact moment a codebase loses its original DNA. 

If a scanner can track the genetic drift of DOOM across 30 years and a half-dozen languages, imagine what it can map in your production repositories.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

