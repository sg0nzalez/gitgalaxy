# 2.2.B. Sub-Equations

To ensure the equations above are actionable, the following variables
are defined based on the scanner\'s regex hits:

**branch_hits:** Control flow constructs including
conditionals (*if*, *switch*), loops (*for*,
*while*), jumps (*break*, *throw*), and logical
operators (*&&*, *\|\|*) that divert execution paths.


-   **args_hits:** Function signatures, parameter lists,
input registers, or lambda arguments that define the data inputs for
a logic block.

```{=html}
<!-- -->
```
-   **linear_hits:** Sequential flow markers, including
variable declarations (*const*, *var*), imports, returns, and
structural keywords that indicate non-branching logic.

```{=html}
<!-- -->
```
-   **func_start_hits:** The syntactic anchor identifying
the beginning of a named function, method, subroutine, or procedure
definition (excluding classes/interfaces).

```{=html}
<!-- -->
```
-   **class_start_hits:** The syntax that defines an
object-oriented class, struct, record, or enum, driving API surface
area calculations.

```{=html}
<!-- -->
```
-   **safety_hits:** Defensive constructs such as
exception handling (*try/catch*), type assertions, null checks, and
memory protection mechanisms (*readonly*).

```{=html}
<!-- -->
```
-   **safety_neg_hits:** Risk factors including error
suppression, dynamic code execution (*eval*), type-system bypasses
(*any*, *!*), and unsafe pointer usage.

```{=html}
<!-- -->
```
-   **danger_hits:** Critical indicators of technical debt
(*TODO/FIXME*), destructive system calls (*process.exit*), hardcoded
secrets, or catastrophic failure modes.

```{=html}
<!-- -->
```
-   **io_hits:** Interactions with external boundaries,
including file systems, network requests (*fetch*), database
queries, and hardware I/O.

```{=html}
<!-- -->
```
-   **api_hits:** Keywords identifying public interfaces
(*export*, *public*), exported members, or globally accessible entry
points that define surface area.

```{=html}
<!-- -->
```
-   **flux_hits:** Markers of state change, including
variable assignment (*let*, *mut*), mutable collections, pointer
updates, and side-effect triggers.

```{=html}
<!-- -->
```
-   **graveyard_hits:** Patterns detecting commented-out
code blocks (*// if*), legacy logic, or \"zombie\" code (*//
console.log*) that remains in the source file.

```{=html}
<!-- -->
```
-   **doc_hits:** Structured documentation syntax,
including JSDoc (*/\*\**), XML comments, and standard metadata tags
describing code intent.

```{=html}
<!-- -->
```
-   **test_hits:** Framework-specific keywords for
assertions, unit test definitions, mocks, and verification suites
(*describe*, *assert*, *mock*).

```{=html}
<!-- -->
```
-   **concurrency_hits:** Constructs for asynchronous
execution (*async/await*), threading, parallel processing,
coroutines, and synchronization primitives.

```{=html}
<!-- -->
```
-   **ui_framework_hits:** Patterns specific to frontend
or UI development, including component definitions, view bindings
(*document.getElementById*), and rendering logic.

```{=html}
<!-- -->
```
-   **closures_hits:** Syntax for anonymous functions,
lambdas, blocks, or inline delegates that capture local context
(*=\>*).

```{=html}
<!-- -->
```
-   **globals_hits:** References to global scope
(*window.*, *process.env*), environment variables, singletons, or
system-wide shared state.

```{=html}
<!-- -->
```
-   **decorators_hits:** Annotations, attributes, or
wrapper syntax used to modify or tag classes and methods with
metadata (*\@Injectable*).

```{=html}
<!-- -->
```
-   **generics_hits:** Syntax defining type parameters
(*\<T\>*), templates, or polymorphic structures for type-agnostic
logic.

```{=html}
<!-- -->
```
-   **comprehensions_hits:** High-density logic patterns
including list comprehensions, functional chains (*.map*,
*.filter*), and array transformations.

```{=html}
<!-- -->
```
-   **scientific_hits:** Usage of mathematical libraries
(*Math.*, *numpy*), tensor operations, arbitrary precision
arithmetic, or complex number processing.

```{=html}
<!-- -->
```
-   **heat_triggers_hits:** High-complexity constructs
such as metaprogramming, reflection (*Proxy*, *eval*), macros, or
dynamic dispatch that increase cognitive load.

```{=html}
<!-- -->
```
-   **import_hits:** Syntax for dependency management,
module loading (*import*, *require*), file inclusion, or library
linking.

```{=html}
<!-- -->
```
-   **ownership_hits:** Metadata extraction patterns for
identifying authors, maintainers, or copyright holders within file
headers (*\@author*).


