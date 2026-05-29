# ETL Unpacker (EBCDIC to CSV)

> **Architecture: Binary Translation & Precision Decoding**
>
> **Summary:** The ETL (Extract, Transform, Load) Unpacker acts as the data bridge between the legacy mainframe and the modern cloud. It translates raw, binary EBCDIC byte streams into standard UTF-8 CSV files, unpacking highly compressed mainframe memory formats on the fly.

## Schema-Driven Byte Slicing
Mainframe data files do not have delimiters (like commas or tabs). They are continuous blocks of binary data. To slice them correctly, the unpacker reads the GitGalaxy-generated JSON Schema.
It calculates the exact physical byte length of each field based on its legacy `PIC` clause. For example, it translates `PIC X(50)` into a rigid 50-byte read buffer, allowing it to perfectly segment the binary stream row by row.

## COMP-3 (Packed Decimal) Decoding
To save physical disk space, IBM mainframes compress numeric data using COMP-3. This format packs two digits into a single byte (nibbles), utilizing the final half-byte to store the positive/negative sign.
* The unpacker calculates the compressed byte size using the formula: `ceil((digits + 1) / 2)`.
* It decodes the raw hex values into standard Python floats.
* It validates the final nibble (checking for `D` or `B` to indicate negative values) and applies the schema's defined decimal scale (e.g., shifting the decimal point for `PIC S9(5)V99`).

## EBCDIC Character Translation
Standard text fields and zoned decimals are read in their raw EBCDIC encoding and translated to standard UTF-8. The unpacker strictly uses the `cp037` code page (the standard IBM US EBCDIC character set) to ensure special characters and legacy formatting survive the transition to the cloud intact.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
