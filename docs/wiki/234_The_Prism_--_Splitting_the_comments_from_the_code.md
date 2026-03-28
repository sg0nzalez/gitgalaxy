# 2.3.4. The Prism (Splitting Comments from Code)

> **Structural Refraction**
>
> Following the successful completion of the language identification, the engine performs a Structural Refraction—splitting a single source file into mutually exclusive streams. Under the Strategy v6.2.0 Protocol, this dual-capture process yields the pure logic `code_stream` (Active Matter), the documentation `comment_stream` (Ghost Mass), and accurate LOC metrics (`coding_loc` and `doc_loc`).
>
> This phase is critical for preventing "Logic Erosion," where documentation or URLs inside strings might otherwise inflate the perceived mass or branching density of the star. The split is a non-destructive process allowing the system to analyze the skeleton of the code and the spirit of the documentation independently.

## 2.3.4.A. The Refraction Mechanics (The Prism Protocol)

The refraction process relies on the linguistic parameters established by the Language Lens. By operating on verified signals, the Prism eliminates the "Neighborhood Guessing" common in standard scanners, achieving near-perfect accuracy in its separation of code from comments. *(Note: In v6.2.0, multi-language `lang_mix` tracking is fully delegated upstream to the Detector).*

### 1. Verified Hand-off & Singularity Bypass
The Optical Splitter is the primary "Refraction Gate" in the physics pipeline. It utilizes two absolute bypasses to protect edge cases and preserve structural integrity:
* **The Singularity Bypass:** Any file identified as `undeterminable` or `unknown` bypasses the split entirely. All content is routed to the `code_stream` as intact "Dark Matter" to ensure no potentially vital logic is lost.
* **The Prose Bypass:** Files identified as pure literature (`markdown`, `plaintext`, `xml`) route their entire payload directly to the `comment_stream` (Ghost Mass), instantly protecting human prose and markup from being miscalculated as structural logic.

### 2. The 8 Mechanical Families (COMMENT_DEFINITIONS)
The engine utilizes a standardized execution matrix to route files based on their mechanical stripping requirements.

| ID | Key | Refraction Strategy | Coverage |
| :--- | :--- | :--- | :--- |
| **1** | `std_c` | Standard Line (`//`) and Block (`/* */`) | JS, TS, Java, C#, C++, C, Go, Kotlin, Obj-C, Apex, Dart, CSS |
| **2** | `nested_c` | Recursive "While-Peel" extraction for nested blocks | Rust, Swift, Scala |
| **3** | `pure_hash` | Single-pass hash (`#`) extraction | Python, MicroPython, Shell, AGC, Dockerfile, Makefile |
| **4** | `hybrid_hash` | Hash line + Custom blocks (`<#`, `=pod`) | PowerShell, Perl, Ruby |
| **5** | `hybrid_dash` | Double-dash (`--`) + Unique blocks (`{-`) | SQL, Lua, Haskell |
| **6** | `polyglot` | Multi-token extraction (`//`, `#`, `/*`) | PHP, LiveCode |
| **7** | `positional` | Column-Anchored (Col 1/7) extraction | COBOL, Fortran, ABAP |
| **8** | `singular` | Unique markup/logic delimiters (`
