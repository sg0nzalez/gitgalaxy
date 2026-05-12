# ⚔️ The Strict Extraction Gauntlets

Welcome to the **Strict Extraction** test suite. 

Because GitGalaxy is an **AST-free structural parser**, our regular expressions *are* the compiler. A poorly written regex won't just fail to parse a file—it will hallucinate architecture, corrupt the forensic math, or trigger a Catastrophic Backtracking (ReDoS) death spiral.

These four test files form the ultimate proving ground. They mathematically verify that our structural spawners can cleanly isolate exact identifiers across 30+ languages while surviving adversarial formatting.

## 📂 The Four Pillars of Extraction

### 1. `test_function_extraction_strict.py` (The Satellite Spawner)
Validates the `func_start` rules. Proves the engine can pinpoint exact function and method names (the "Satellites") while stepping over massive attribute stacks, asynchronous modifiers, explicit return types, and C++ macro garbage.

### 2. `test_class_extraction_strict.py` (The Entity Census)
Validates the `class_start` rules. Proves the engine can isolate the precise name of an Object-Oriented entity (Class, Struct, Interface, Trait, Enum) while ignoring complex inheritance chains, generics, and visibility modifiers.

### 3. `test_args_extraction_strict.py` (The Coupling Mass)
Validates the `args` rules. The hardest structural component to parse with regex. Proves the engine can swallow massive parameter blocks, default arguments, and multi-line lambda closures without collapsing into a ReDoS spiral caused by nested parentheses.

### 4. `test_dependency_extraction_strict.py` (The Gravity Links)
Validates the `_dependency_capture` rules. Proves the engine can trace information flow by extracting the exact file path or module name from an import statement, completely ignoring aliases, destructuring syntax, and `require()` wrappers.

---

## 🧪 The 3-Tier Testing Matrix

Every language mapped in these gauntlets is subjected to three distinct phases of adversarial testing:

1. **`valid` (The Iron Wall):**
   * *Purpose:* Proves baseline functionality.
   * *Pass Condition:* The regex must match the payload AND strictly isolate the exact target string (using Capture Groups where defined), leaving behind no dirty modifiers.
2. **`invalid` (Ghost Prevention):**
   * *Purpose:* Proves the regex won't hallucinate architecture.
   * *Pass Condition:* The regex MUST return `None` when fed structural lookalikes (e.g., instantiation `new Target()`, control flow `if (Target)`, or variable assignment `Target = function`).
3. **`pathological` (The Frankenstein Test):**
   * *Purpose:* Proves ReDoS immunity and vertical parsing capability.
   * *Pass Condition:* The regex must successfully extract the target from code formatted with absurd vertical newlines, tabs, and extreme modifier stacking, executing in $O(1)$ or $O(N)$ time without locking the CPU.

---

## 🛠️ How to Add a New Language

To subject a new language to the gauntlet, simply inject it into the constant dictionaries at the top of each test file using the standard schema:

```python
"new_language": {
    "valid": [
        ("function TargetName() {", "TargetName")
    ],
    "invalid": [
        "var TargetName = 5;",
        "if (TargetName) {"
    ],
    "pathological": [
        ("public \n async \n function \n TargetName \n (", "TargetName")
    ]
}
```

## 🚀 Execution Commands

Execute these tests from the project root while within the `galaxy_venv`.

**Run all extraction gauntlets:**
```bash
python -m pytest tests/extraction/ -v
```

**Run a specific gauntlet with fast-fail:**
```bash
python -m pytest tests/extraction/test_function_extraction_strict.py -v -x
```