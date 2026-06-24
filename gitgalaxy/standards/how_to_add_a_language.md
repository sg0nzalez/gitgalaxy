# 🌌 Architecting a New Language (Extending the blAST Engine)

GitGalaxy does not use brittle Abstract Syntax Trees (ASTs) or traditional compiler toolchains. Instead, we map planetary-scale codebases using the **blAST Engine** (Bypassing LLMs and ASTs): a polyglot structural physics engine. 

Instead of writing a custom parser that breaks the moment a repository fails to compile, we teach the engine the "physics" of a new language using high-speed, mathematically bounded, ReDoS-proof regular expressions. This allows GitGalaxy to build a universal, comparative lexical taxonomy across entirely different computing eras (from 1980s COBOL to modern Rust).

For the mathematical proofs backing this architecture, review:
* 🔬 [The blAST Paradigm](../../docs/wiki/01-03-the-blast-paradigm.md)
* ⚖️ [Claim 10: The Heuristic vs. AST Paradigm](../../docs/wiki/03-10-claim-10-ast-vs-heuristic-parsing.md)
* 🛡️ [Claim 8: Empirical Validation of AST-Free Parsing](../../docs/wiki/03-08-claim-8-empirical-validation-of-ast-free-parsing.md)

To add a new language to the [Language Lens](../../docs/wiki/02-05-language-lens.md), you will use an advanced LLM (like Claude 3.5 Sonnet, GPT-4o, or Gemini 1.5 Pro) to generate the structural dictionary.

---

### Step 1: Initialize the LLM Context
Before asking the LLM to generate the new language, upload the `gitgalaxy/standards/language_standards.py` file to the chat window. Issue this exact command:
> *"Read this file to understand how the GitGalaxy physics engine uses bounded regex to guarantee ReDoS immunity. Pay close attention to how C++ and Python are mapped to prevent Catastrophic Backtracking."*

### Step 2: Inject the Master Calibration Prompt
Copy the **Master Prompt** below and paste it into the LLM. Replace `[TARGET LANGUAGE]` with the exact language you want to map.

### Step 3: Calibrate the Engine
1. Open `gitgalaxy/standards/language_standards.py`.
2. Locate the `LANGUAGE_DEFINITIONS` matrix.
3. Paste the generated Python dictionary directly into the registry to instantly grant the engine native support for the new architecture.

<br><br>

---

## ⚙️ The Master Calibration Prompt
*Copy everything below this line and feed it directly to the LLM.*

**Prompt:**
You are an expert compiler engineer and static analysis specialist. Please generate a GitGalaxy REGISTRY regex dictionary for **[TARGET LANGUAGE]** using the strict Zero-Trust framework defined below. 

This dictionary will be used by an AST-free physics engine to create a system of consistent 1:1 cross-language comparisons (a comparative lexical taxonomical map), calculating risk exposures across implicit and explicit language behaviors. The engine uses `re.M` (Multiline) to scan 50,000+ line enterprise files at extreme velocity.

### 🚨 CRITICAL ENGINE RULES
1. **The Physical Reality Rule (Implicit vs. Explicit):** Do not just hunt for explicit keywords; capture the physical reality. If defining API Exposure (Key 10), determine if the language is implicitly public (e.g., Python, Fortran). If so, the regex must capture standard function/subroutine definitions, not just the rare use of an explicit public or export tag.
2. **The Paradigm Forgiveness Rule:** Do not punish a language for operating within its standard paradigm. Example: Standard C-style pointer casting is standard operating procedure, not a structural fracture. It must be routed to Phase 5 (Resource Management & Stability) as friction, NOT placed in Phase 2 `safety_neg` where it will trigger the Breach Cap.
3. **The "Commented-out Code" Rule (Contextual Debt):** When assessing Tech Debt or Danger, isolate human commentary from execution flow. Example: `TODO` and `FIXME` are planned debt. They must NEVER be placed in execution-blocking keys like `danger`, otherwise a file with high developer documentation will be falsely penalized as a volatile execution risk.
4. **The Comparative Map Rule (Use `None`):** If a dimension does not exist natively in the target language (e.g., pointers in JavaScript, decorators in C), you MUST explicitly set its key to `None`. Do not force a fit.
5. **Absolute ReDoS Immunity (No Catastrophic Backtracking):** Bound all wildcards. Never use `.*` inside brackets. Always use negation (e.g., `<[^>]*>`). In `re.M` mode, `\s` matches newlines (`\n`). 
    * ❌ NEVER use `^\s*`. ✅ ALWAYS use `^[ \t]*`.
    * ❌ NEVER use `\s*$`. ✅ ALWAYS use `[ \t]*$`.
    * ❌ NEVER use `\s*=`. ✅ ALWAYS use `[ \t]*=`.
    * ❌ NEVER nest unbounded quantifiers like `(?:[ \t]*\*+)*` or `(?:(?:public|private)\s+)*`. ✅ ALWAYS use strict numeric clamps like `(?:[ \t*&]+){0,10}` or `(?:(?:public|static)[ \t]+){0,3}`.
6. **The Geometry Inflator Bug:** Do NOT put access modifiers (e.g., public, private, static) in the `linear` array. This artificially inflates the math and turns all files into smooth spheres, destroying visual 3D complexity.
7. **Object/Entity Spurious Matches:** `func_start` must ONLY match executable logic blocks (methods/functions/constructors). Do NOT match interfaces, types, or classes here.
8. **Resource Management & Stability:** Pay special attention to Phase 5. Ensure that chaos (e.g., concurrency, events, flux) and order (e.g., sync_locks, listeners, freeze_hits) are cleanly separated into their specific regex keys so the physics engine can balance them.

### THE LEXICAL FAMILIES
You must assign the language to one of these 5 optical parsing families based on how it handles comments / non-executable text:
* `standard_block`: The language uses both line and block delimiters, but blocks CANNOT be nested. Examples: C, C++, Java, JavaScript, PHP, SQL, Go, Ruby, Lua.
* `recursive_block`: The language allows block comments to be safely nested inside one another. Examples: Rust, Swift, Dart, Scala.
* `line_exclusive`: The language possesses no native multi-line block syntax. The engine ignores closing tags. Examples: Python, Shell, Makefile, Assembly, Scheme.
* `block_exclusive`: The language possesses no native single-line comment syntax. All text must be enclosed. Examples: HTML, XML.
* `positional_anchored`: The engine must verify the token's physical column placement. Examples: Legacy COBOL, Legacy Fortran, ABAP.

### OUTPUT SCHEMA & DEFINITIONS
Generate a valid Python dictionary matching this exact structure. 

```python
"[TARGET LANGUAGE]": {
    "_meta": {
        "target_version": "Include the modern compiler/standard version",
        "last_updated": "YYYY-MM-DD",
        "blueprint_version": "v6.3",
        "status": "production"
    },
    "extensions": [], # e.g. [".js", ".jsx"]
    "exact_matches": [], # e.g. ["Makefile"]
    "discriminators": [], # Ecosystem anchors (e.g. "package.json")
    "shebangs": [], 
    "lexical_family": "", # See Lexical Families list above
    "rules": {
        # --- OPTICAL SPLITS ---
        "_line_anchor": re.compile(r""), 
        "_inline_comment": re.compile(r""),
        "_block_start": re.compile(r""),
        "_block_end": re.compile(r""),

        # --- PHASE 1: GEOMETRY & STRUCTURE ---
        # branch (Control Flow / Branching): Control flow that forces the CPU to make a decision or jump. High density creates jagged shapes. Includes: if, else, switch, for, while, catch, try, &&, ||, ternary. EXCLUDES: Exceptions (throw, raise) — these belong in panics_and_aborts.
        "branch": re.compile(r""), 
        # args (Parameters / Coupling): Signatures defining input parameters. Drives the physical size/mass of the function. Includes: parameter blocks of functions, methods, and lambdas. Must safely step over type hints.
        "args": re.compile(r""), 
        # structural_boundaries (Sequential Boundaries): Keywords defining structural boundaries and straight-line execution. Smooths the geometry into spheres. Includes: var, return, class, import. EXCLUDES: Access modifiers (public, private) and Immutability keywords (const, final — these belong in immutability_locks).
        "structural_boundaries": re.compile(r""), 
        # func_start (Executable Logic Anchors): Exact syntax anchoring the start of an executable block of logic. Includes: Method signatures, constructors. EXCLUDES: Interfaces, types, and classes.
        "func_start": re.compile(r""), 
        # class_start (Object / Entity Declarations): The syntax that defines an object-oriented class, struct, or record. Drives API Surface Area math.
        "class_start": re.compile(r""), 

        # --- PHASE 2: RISK & STRUCTURAL INTEGRITY ---
        # safety (Defensive Programming / Validation): Defensive programming constructs that prevent crashes at runtime. Includes: try/catch, explicit null checks, guard. EXCLUDES: Immutability.
        "safety": re.compile(r""), 
        # safety_bypasses (Safety Bypasses / Unchecked Types): Syntax that actively bypasses type safety, swallows errors, or relies on unpredictable state. Includes: Force unwrapping (!), any, raw memory casting, linter bypasses (@ts-ignore).
        "safety_bypasses": re.compile(r""), 
        # high_risk_execution (High-Risk Execution / System Calls): Extreme tech debt, process-killing commands, and catastrophic runtime vulnerabilities. Includes: eval, exec, process.exit. EXCLUDES: TODO/HACK (debt) and print (debug_prints).
        "high_risk_execution": re.compile(r""), 
        # io (I/O & Network Boundaries): Interaction with the disk, network, or external systems. Includes: File writing/reading, HTTP clients, sockets. EXCLUDES: Logging/printing.
        "io": re.compile(r""), 
        # api (Public Surface Area): Code exposed to the outside world. Measures physical surface area (Mitigated by encapsulation). Captures explicit visibility markers (export, public) AND implicit architectural defaults. If the linker can touch it, it possesses surface area.
        "api": re.compile(r""), 
        # state_mutation (State Mutation): Mutation of state. Reassignment of variables or modifying collections. (Mitigated by immutability_locks). Includes: let, mut, volatile, .push(), .set().
        "state_mutation": re.compile(r""), 
        # dead_code (Dead / Commented-out Code): Commented-out structural code and unused logic trails. Includes: // if (x), /* var y */.
        "dead_code": re.compile(r""), 
        # doc (Structured Documentation): Structured documentation meant to be parsed by IDEs or generators. Includes: JSDoc, Docstrings.
        "doc": re.compile(r""), 
        # test (Testing & Assertions): Assertions and unit testing framework keywords. (Mitigates test_skip). Includes: describe, it, assert, expect.
        "test": re.compile(r""), 

        # --- PHASE 3: ARCHITECTURE & DOMAIN SENSORS ---
        # concurrency (Asynchronous Execution): Time-bending logic and parallel execution. (Mitigated by sync_locks). Includes: async, await, Promise, Thread.
        "concurrency": re.compile(r""), 
        # ui_framework (UI / View Components): DOM manipulation, UI components. Includes: HTML tags, React hooks.
        "ui_framework": re.compile(r""), 
        # closures (Closures / Anonymous Functions): Anonymous functions, lambdas, inline callbacks. Includes: Fat arrows (=>).
        "closures": re.compile(r""), 
        # globals (Global / Shared State): Accessing global state, environment variables, or system registries. Includes: window., process.env.
        "globals": re.compile(r""), 
        # decorators (Decorators / Annotations): Annotations applied to classes/methods. Includes: @Injectable, [Obsolete].
        "decorators": re.compile(r""), 
        # generics (Generics / Type Parameters): Type parameters that make logic reusable but harder to read. Includes: <T>, List<T>.
        "generics": re.compile(r""), 
        # comprehensions (Iterators / Comprehensions): Functional array transformations or inline looping. Includes: .map(, .filter(.
        "comprehensions": re.compile(r""), 
        # scientific (Numerical / Compute Libraries): Math, data science, and complex rendering libraries. Includes: Math., numpy.
        "scientific": re.compile(r""), 
        # reflection_metaprogramming (Metaprogramming & Reflection): Highly complex, "clever" code that causes cognitive meltdown. Includes: Reflection, Proxy, .bind().
        "reflection_metaprogramming": re.compile(r""), 
        # import (Dependency Inclusions): Dependency resolution and module loading. Includes: import, require, using.
        "import": re.compile(r""), 
        # _dependency_capture: Regex strictly capturing group 1 as the exact dependency path string.
        "_dependency_capture": re.compile(r""), 
        # ownership (Authorship Metadata): Authorship metadata. Includes: @author, Created by:.
        "ownership": re.compile(r""), 

        # --- PHASE 4: SPECIALIZED SUB-SYSTEMS ---
        # planned_debt (Annotated Debt / TODOs): Future work that doesn't necessarily imply brokenness. Includes: TODO, WIP, STUB.
        "planned_debt": re.compile(r""), 
        # fragile_debt (Acknowledged Hacks / FIXMEs): Explicit admissions of fragile, dangerous, or ugly logic. Includes: HACK, FIXME, XXX, WTF.
        "fragile_debt": re.compile(r""), 
        # hardcoded_secrets (Hardcoded Secrets / Credentials): Hardcoded secrets, static credentials, or API keys baked into code. Includes: password, secret, token, api_key.
        "hardcoded_secrets": re.compile(r""), 
        # spec_exposure (Spec / Audit Traceability): Audit tags establishing traceability of intent. Includes: [SPEC-123], [audit].
        "spec_exposure": re.compile(r""), 
        # tabs_vs_spaces (Formatting Inconsistencies): Structural formatting markers used to calculate Tabs vs. Spaces ratio. Often None.
        "tabs_vs_spaces": None, 
        # ssr_boundaries (Server-Side Rendering): Server-Side Rendering computation boundaries where backend meets frontend. Includes: getServerSideProps.
        "ssr_boundaries": re.compile(r""), 
        # events (Event Emitters / Pub-Sub): Event-driven architecture signatures and message brokers. (Mitigated by listeners). Includes: emit, EventEmitter, Kafka, Publisher.
        "events": re.compile(r""), 
        # dependency_injection (Dependency Injection / IoC): Inversion of Control (IoC) injection markers. Includes: @Autowired, @Inject.
        "dependency_injection": re.compile(r""), 
        # macros (Preprocessor Directives / Macros): Compiler pragmas or macro definitions that generate code at compile-time. Includes: #define, macro_rules!.
        "macros": re.compile(r""), 
        # pointers (Pointer Arithmetic / Memory Addressing): Explicit tracking of raw memory addressing and pointer dereferencing. Includes: *const, &mut, IntPtr.
        "pointers": re.compile(r""), 
        # memory_alloc (Manual Memory Management): Explicit unmanaged memory allocations and raw heap manipulations. (Mitigated by cleanup). Includes: malloc, new.
        "memory_alloc": re.compile(r""), 
        # inline_asm (Inline Assembly): Direct CPU architecture bridging. Includes: __asm__, asm!.
        "inline_asm": re.compile(r""), 

        # --- PHASE 5: RESOURCE MANAGEMENT & STABILITY ---
        # telemetry (Structured Logging / Telemetry): Structured logging and observability frameworks used safely in production. Acts as executable documentation.
        "telemetry": re.compile(r""), 
        # debug_prints (Standard Output / Debug Prints): Ad-hoc, temporary debug statements pushed to production. Includes: print(, console.log(.
        "debug_prints": re.compile(r""), 
        # explicit_casts (Explicit Type Casting): Explicitly bypassing the compiler's type-checker. Indicates misaligned data structures. Includes: as String, (int), static_cast.
        "explicit_casts": re.compile(r""), 
        # panics_and_aborts (Execution Halts / Panics): Forcefully destroying the current execution context. Includes: throw, raise, panic!, abort().
        "panics_and_aborts": re.compile(r""), 
        # thread_sleeps (Thread Blocking / Sleeps): Forcing a thread to sleep (often an admission of a race condition). Includes: sleep(, delay(.
        "thread_sleeps": re.compile(r""), 
        # bitwise_ops (Bitwise Operations): Manipulating raw bytes and memory registers. Extremely dense, low-level logic. EXCLUDES logical &&/||.
        "bitwise_ops": re.compile(r""), 
        # sync_locks (Thread Synchronization / Locks): Explicitly coordinating threaded logic to prevent race conditions. (Mitigates concurrency).
        "sync_locks": re.compile(r""), 
        # immutability_locks (Immutability Constraints): Explicitly locking data so it cannot be mutated. (Mitigates state_mutation). Includes: const, final, readonly.
        "immutability_locks": re.compile(r""), 
        # cleanup (Resource Cleanup / Teardown): Explicitly destroying state or releasing resources to prevent leaks. (Mitigates memory_alloc and io). Includes: free(, dispose(), .close().
        "cleanup": re.compile(r""), 
        # encapsulation (Access Modifiers / Encapsulation): Explicitly hiding logic from the rest of the application. (Mitigates api). Includes: private, protected, internal.
        "encapsulation": re.compile(r""), 
        # listeners (Event Listeners / Observers): Waiting to receive state from an external broadcast. (Mitigates events). Includes: on(, addEventListener, subscribe(.
        "listeners": re.compile(r""), 
        # test_skip (Bypassed Tests / Ignored Specs): Code that uses the testing framework but explicitly bypasses verification. (Anti-pattern to test). Includes: @Ignore, test.skip(.
        "test_skip": re.compile(r""), 

        # --- HYBRID DOMAIN SENSORS ---
        # serialization_parsing: JSON, XML, YAML parsing libraries.
        "serialization_parsing": re.compile(r""), 
        # regex_execution: Native regex evaluation commands.
        "regex_execution": re.compile(r""), 
        # time_date_logic: Time/date instantiation and math.
        "time_date_logic": re.compile(r""), 
        # ipc_rpc_bridges: Inter-process or RPC bridging commands.
        "ipc_rpc_bridges": re.compile(r"") 
    }
}
```
