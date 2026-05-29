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
2. **The Paradigm Forgiveness Rule (No "Trust Me" Taxes):** Do not punish a language for operating within its standard paradigm. Example: Standard C-style pointer casting is standard operating procedure, not a structural fracture. It must be routed to Phase 5 (Thermodynamic Balance) as friction, NOT placed in Phase 2 `safety_neg` where it will trigger the Breach Cap.
3. **The "Ghost Logic" Rule (Contextual Debt):** When assessing Tech Debt or Danger, isolate human commentary from execution flow. Example: `TODO` and `FIXME` are planned debt. They must NEVER be placed in execution-blocking keys like `danger`, otherwise a file with high developer documentation will be falsely penalized as a volatile execution risk.
4. **The Comparative Map Rule (Use `None`):** If a dimension does not exist natively in the target language (e.g., pointers in JavaScript, decorators in C), you MUST explicitly set its key to `None`. Do not force a fit.
5. **Absolute ReDoS Immunity (No Catastrophic Backtracking):** Bound all wildcards. Never use `.*` inside brackets. Always use negation (e.g., `<[^>]*>`). In `re.M` mode, `\s` matches newlines (`\n`). 
    * ❌ NEVER use `^\s*`. ✅ ALWAYS use `^[ \t]*`.
    * ❌ NEVER use `\s*$`. ✅ ALWAYS use `[ \t]*$`.
    * ❌ NEVER use `\s*=`. ✅ ALWAYS use `[ \t]*=`.
    * ❌ NEVER nest unbounded quantifiers like `(?:[ \t]*\*+)*` or `(?:(?:public|private)\s+)*`. ✅ ALWAYS use strict numeric clamps like `(?:[ \t*&]+){0,10}` or `(?:(?:public|static)[ \t]+){0,3}`.
6. **The Geometry Inflator Bug:** Do NOT put access modifiers (e.g., public, private, static) in the `linear` array. This artificially inflates the math and turns all files into smooth spheres, destroying visual 3D complexity.
7. **Ghost Satellites:** `func_start` must ONLY match executable logic blocks (methods/functions/constructors). Do NOT match interfaces, types, or classes here.
8. **Thermodynamic Balance (Yin & Yang):** Pay special attention to Phase 5. Ensure that chaos (e.g., concurrency, events, flux) and order (e.g., sync_locks, listeners, freeze_hits) are cleanly separated into their specific regex keys so the physics engine can balance them.

### THE LEXICAL FAMILIES
You must assign the language to one of these optical parsing families based on how it handles comments (Ghost Mass):
* `std_c`: Standard C-style (Line: `//`, Block: `/* ... */`). Examples: C, C++, Java, JS, Go.
* `nested_c`: Supports recursive block nesting (Line: `//`, Block: `/* /* */ */`). Examples: Rust, Swift, Scala.
* `pure_hash`: Hash-style only (Line: `#`, Block: None). Examples: Python, Shell, Makefile.
* `hybrid_hash`: Hash line + custom block (Line: `#`, Block: `<# #>` or `=begin =end`). Examples: PowerShell, Ruby.
* `hybrid_dash`: Dash line + custom block (Line: `--`, Block: `/* */` or `--[[ ]]`). Examples: SQL, Lua, Haskell.
* `polyglot`: Supports multiple line comment tokens (e.g., `//`, `#`, `/* */`). Examples: PHP, LiveCode.
* `positional`: Legacy column-based parsing. Examples: Fortran (C/* in col 1), ABAP.
* `singular`: SGML/XML style block only (``), or unique line delimiters (Assembly `;`). Examples: HTML, XML, Assembly.
* `lisp_semi`: Lisp-style (Line: `;`, Block: `#| |#`). Examples: Scheme, Racket.

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
    "discriminators": [], # Ecosystem gravity anchors (e.g. "package.json")
    "shebangs": [], 
    "lexical_family": "", # See Lexical Families list above
    "rules": {
        # --- OPTICAL SPLITS ---
        "_line_anchor": re.compile(r""), 
        "_inline_comment": re.compile(r""),
        "_block_start": re.compile(r""),
        "_block_end": re.compile(r""),

        # --- PHASE 1: GEOMETRY (The Physical Stars) ---
        # branch: Control flow that forces the CPU to make a decision or jump. High density creates jagged shapes. Includes: if, else, switch, for, while, catch, try, &&, ||, ternary. EXCLUDES: Exceptions (throw, raise) — these belong in bailout_hits.
        "branch": re.compile(r""), 
        # args: Signatures defining input parameters. Drives the physical size/mass of the function. Includes: parameter blocks of functions, methods, and lambdas. Must safely step over type hints.
        "args": re.compile(r""), 
        # linear: Keywords defining structural boundaries and straight-line execution. Smooths the geometry into spheres. Includes: var, return, class, import. EXCLUDES: Access modifiers (public, private) and Immutability keywords (const, final — these belong in freeze_hits).
        "linear": re.compile(r""), 
        # func_start: SATELLITE SPAWNER. Exact syntax anchoring the start of an executable block of logic. Includes: Method signatures, constructors. EXCLUDES: Interfaces, types, and classes.
        "func_start": re.compile(r""), 
        # class_start: ENTITY CENSUS. The syntax that defines an object-oriented class, struct, or record. Drives API Surface Area math.
        "class_start": re.compile(r""), 

        # --- PHASE 2: RISK ENGINE (Integrity & Debt) ---
        # safety: Cyan Fortification. Defensive programming constructs that prevent crashes at runtime. Includes: try/catch, explicit null checks, guard. EXCLUDES: Immutability.
        "safety": re.compile(r""), 
        # safety_neg: Red Fragility. Syntax that actively bypasses type safety, swallows errors, or relies on unpredictable state. Includes: Force unwrapping (!), any, raw memory casting, linter bypasses (@ts-ignore).
        "safety_neg": re.compile(r""), 
        # danger: The Heavy Load. Extreme tech debt, process-killing commands, and catastrophic runtime vulnerabilities. Includes: eval, exec, process.exit. EXCLUDES: TODO/HACK (debt) and print (print_hits).
        "danger": re.compile(r""), 
        # io: Interaction with the disk, network, or external systems. Includes: File writing/reading, HTTP clients, sockets. EXCLUDES: Logging/printing.
        "io": re.compile(r""), 
        # api: The Event Horizon. Code exposed to the outside world. Measures physical surface area (The Yin to encapsulation). Captures explicit visibility markers (export, public) AND implicit architectural defaults. If the linker can touch it, it possesses surface area.
        "api": re.compile(r""), 
        # flux: Boiling Plasma. Mutation of state. Reassignment of variables or modifying collections. (The Yin to freeze_hits). Includes: let, mut, volatile, .push(), .set().
        "flux": re.compile(r""), 
        # graveyard: Necrosis. Commented-out structural code and ghost logic trails. Includes: // if (x), /* var y */.
        "graveyard": re.compile(r""), 
        # doc: The Intent. Structured documentation meant to be parsed by IDEs or generators. Includes: JSDoc, Docstrings.
        "doc": re.compile(r""), 
        # test: Assertions and unit testing framework keywords. (The Yang to test_skip). Includes: describe, it, assert, expect.
        "test": re.compile(r""), 

        # --- PHASE 3: SENSORS (Domain & Architecture) ---
        # concurrency: Temporal Static. Time-bending logic and parallel execution. (The Yin to sync_locks). Includes: async, await, Promise, Thread.
        "concurrency": re.compile(r""), 
        # ui_framework: The View Layer. DOM manipulation, UI components. Includes: HTML tags, React hooks.
        "ui_framework": re.compile(r""), 
        # closures: Functional Depth. Anonymous functions, lambdas, inline callbacks. Includes: Fat arrows (=>).
        "closures": re.compile(r""), 
        # globals: Shared Void. Accessing global state, environment variables, or system registries. Includes: window., process.env.
        "globals": re.compile(r""), 
        # decorators: Metadata Hooks. Annotations applied to classes/methods. Includes: @Injectable, [Obsolete].
        "decorators": re.compile(r""), 
        # generics: Type Abstractions. Type parameters that make logic reusable but harder to read. Includes: <T>, List<T>.
        "generics": re.compile(r""), 
        # comprehensions: High-Density Loops. Functional array transformations or inline looping. Includes: .map(, .filter(.
        "comprehensions": re.compile(r""), 
        # scientific: Compute Core. Math, data science, and complex rendering libraries. Includes: Math., numpy.
        "scientific": re.compile(r""), 
        # heat_triggers: Thermal Radiation. Highly complex, "clever" code that causes cognitive meltdown. Includes: Reflection, Proxy, .bind().
        "heat_triggers": re.compile(r""), 
        # import: Gravity Links. Dependency resolution and module loading. Includes: import, require, using.
        "import": re.compile(r""), 
        # _dependency_capture: Regex strictly capturing group 1 as the exact dependency path string.
        "_dependency_capture": re.compile(r""), 
        # ownership: Authorship metadata. Includes: @author, Created by:.
        "ownership": re.compile(r""), 

        # --- PHASE 4: EXTENDED (Specialized Systems) ---
        # planned_debt: The Promise. Future work that doesn't necessarily imply brokenness. Includes: TODO, WIP, STUB.
        "planned_debt": re.compile(r""), 
        # fragile_debt: The Fracture. Explicit admissions of fragile, dangerous, or ugly logic. Includes: HACK, FIXME, XXX, WTF.
        "fragile_debt": re.compile(r""), 
        # private_info: The Sensitive Assets. Hardcoded secrets, static credentials, or API keys baked into code. Includes: password, secret, token, api_key.
        "private_info": re.compile(r""), 
        # spec_exposure: The Map vs. Territory. Audit tags establishing traceability of intent. Includes: [SPEC-123], [audit].
        "spec_exposure": re.compile(r""), 
        # civil_war: The Indentation Tracker. Structural formatting markers used to calculate Tabs vs. Spaces ratio. Often None.
        "civil_war": None, 
        # ssr_boundaries: Server-Side Rendering computation boundaries where backend meets frontend. Includes: getServerSideProps.
        "ssr_boundaries": re.compile(r""), 
        # events: Pub/Sub Network. Event-driven architecture signatures and message brokers. (The Yin to listeners). Includes: emit, EventEmitter, Kafka, Publisher.
        "events": re.compile(r""), 
        # dependency_injection: Inversion of Control (IoC) injection markers. Includes: @Autowired, @Inject.
        "dependency_injection": re.compile(r""), 
        # macros: Preprocessor Hooks. Compiler pragmas or macro definitions that generate code at compile-time. Includes: #define, macro_rules!.
        "macros": re.compile(r""), 
        # pointers: The Memory Map. Explicit tracking of raw memory addressing and pointer dereferencing. Includes: *const, &mut, IntPtr.
        "pointers": re.compile(r""), 
        # memory_alloc: Manual Memory Management. Explicit unmanaged memory allocations and raw heap manipulations. (The Yin to cleanup). Includes: malloc, new.
        "memory_alloc": re.compile(r""), 
        # inline_asm: The Bare Metal. Direct CPU architecture bridging. Includes: __asm__, asm!.
        "inline_asm": re.compile(r""), 

        # --- PHASE 5: THERMODYNAMIC BALANCE (Yin & Yang) ---
        # telemetry: The Professional. Structured logging and observability frameworks used safely in production. Acts as executable documentation.
        "telemetry": re.compile(r""), 
        # print_hits: The Amateur / Space Debris. Ad-hoc, temporary debug statements pushed to production. Includes: print(, console.log(.
        "print_hits": re.compile(r""), 
        # cast_hits: The "Trust Me" Tax. Explicitly bypassing the compiler's type-checker. Indicates misaligned data structures. Includes: as String, (int), static_cast.
        "cast_hits": re.compile(r""), 
        # bailout_hits: The Detonators. Forcefully destroying the current execution context. Includes: throw, raise, panic!, abort().
        "bailout_hits": re.compile(r""), 
        # halt_hits: Temporal Duct Tape. Forcing a thread to sleep (often an admission of a race condition). Includes: sleep(, delay(.
        "halt_hits": re.compile(r""), 
        # bitwise_hits: Sub-Atomic Math. Manipulating raw bytes and memory registers. Extremely dense, low-level logic. EXCLUDES logical &&/||.
        "bitwise_hits": re.compile(r""), 
        # sync_locks: The Barricades. Explicitly coordinating threaded logic to prevent race conditions. (The Yang to concurrency).
        "sync_locks": re.compile(r""), 
        # freeze_hits: Data Cryogenics. Explicitly locking data so it cannot be mutated. (The Yang to flux). Includes: const, final, readonly.
        "freeze_hits": re.compile(r""), 
        # cleanup: The Janitor. Explicitly destroying state or releasing resources to prevent leaks. (The Yang to memory_alloc and io). Includes: free(, dispose(), .close().
        "cleanup": re.compile(r""), 
        # encapsulation: The Vault. Explicitly hiding logic from the rest of the application. (The Yang to api). Includes: private, protected, internal.
        "encapsulation": re.compile(r""), 
        # listeners: The Sinks. Waiting to receive state from an external broadcast. (The Yang to events). Includes: on(, addEventListener, subscribe(.
        "listeners": re.compile(r""), 
        # test_skip: Safety Theater. Code that uses the testing framework but explicitly bypasses verification. (The Yin to test). Includes: @Ignore, test.skip(.
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