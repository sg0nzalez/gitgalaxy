# Entity & Memory Mapping

> **Architecture: Strict Memory Boundary Enforcement**
>
> **Summary:** The Java Spring Entity Forge translates the generated JSON schemas into standard Spring Boot JPA Entities (`@Entity`). Because COBOL utilizes highly specific memory layouts that do not naturally exist in Java, the forge applies advanced annotation strategies to recreate the legacy memory constraints in the cloud.

## Memory Overlay Resolution (REDEFINES)

In COBOL, the `REDEFINES` clause allows two variables to occupy the exact same physical memory address. Relational databases do not support this concept natively. 

When the Entity Forge detects a `redefines` constraint in the JSON schema, it maps the primary variable to the database column, but maps the redefined alias as a `@Transient` variable. This ensures the alias is accessible to the Java business logic at runtime without attempting to create duplicate, conflicting columns in the PostgreSQL schema.

## Array Generation (OCCURS)

Legacy `OCCURS` clauses define fixed-length arrays within records. The Entity Forge translates these into Java `List<T>` structures, automatically annotating them with `@ElementCollection` and `@CollectionTable`. It strictly wires the join columns to ensure the normalized array data maps perfectly back to the parent entity's `sys_id`.

## Financial Precision (PIC Clauses)

The forge parses legacy `PIC` (Picture) clauses to enforce strict structural boundaries on the generated JPA columns:
* **Strings (`PIC X` / `PIC A`):** Extracts the exact byte length and maps it directly to the `@Column(length = N)` annotation.
* **Decimals (`PIC S9V99` / `PIC Z`):** Calculates the exact number of integers and fractional digits, mapping them to `BigDecimal` types with strict `@Column(precision = P, scale = S)` boundaries.

## Lexical Sanitization

To ensure the generated Java code compiles instantly, the Entity Forge applies a multi-pass sanitization protocol to all legacy variable names:
1. **CamelCase Conversion:** Legacy hyphens (`CUSTOMER-NAME`) are converted to standard Java camelCase (`customerName`).
2. **Numeric Prefixing:** Java variables cannot begin with a number. Legacy variables like `1099-FORM` are automatically prefixed (`v1099Form`).
3. **Reserved Keyword Shielding:** If a legacy variable directly collides with a Java reserved keyword (e.g., `class`, `public`, `return`, `int`), the forge automatically appends a `Val` suffix (e.g., `classVal`) to guarantee successful Maven compilation.