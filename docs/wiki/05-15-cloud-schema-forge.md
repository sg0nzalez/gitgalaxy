# Cloud Schema Forge

> **Architecture: Multi-Target DDL & Schema Generation**
>
> **Summary:** The Cloud Schema Forge translates the raw byte-maps of the COBOL Data Division into modern, relational data structures. It outputs both strict PostgreSQL Data Definition Language (DDL) statements and REST-compliant JSON Schemas simultaneously.

## PIC Clause Translation
The forge parses legacy `PIC` (Picture) constraints and translates them into modern relational bounds:
* **String Allocation:** Translates `PIC X(50)` directly into `VARCHAR(50)`.
* **Integer Mapping:** Analyzes numeric length to intelligently map to `SMALLINT`, `INTEGER`, or `BIGINT` to optimize cloud database storage.
* **Decimal Precision:** Splits clauses like `PIC S9(7)V99` into their base and fractional components, mapping them to strict `DECIMAL(9, 2)` SQL bounds.

## The Bloat Cutter (IR Synergy)
Before generating a column for a detected variable, the Schema Forge queries the IR State Manager. If the Graveyard Reaper previously flagged the variable as orphaned or unused memory, the forge instantly drops it. This ensures the resulting PostgreSQL tables are lean and free of the legacy memory bloat that accumulates over decades of maintenance.

## Honesty Sensors (Dynamic Memory)
The forge scans for complex mainframe-specific memory behaviors and injects architectural warnings directly into the generated SQL as comments:
* **Dynamic Arrays:** If it detects an `OCCURS DEPENDING ON` clause (an array whose length changes dynamically at runtime), it flags the column with a critical warning to utilize a `JSONB` data type, as strict relational columns cannot handle dynamic array allocation.
* **Packed Decimals:** It flags `COMP-3` variables to alert downstream engineering teams that the original data source is binary-compressed.