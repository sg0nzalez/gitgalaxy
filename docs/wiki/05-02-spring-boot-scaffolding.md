# Spring Boot Scaffolding (The Cloud Escape Hatch)

> **Architecture: Automated Build Systems & Legacy Decoders**
>
> **Summary:** The Java Translation Controller acts as the "Cloud Escape Hatch." It ingests the JSON IR dumps from the clean room and generates a fully compilable Spring Boot microservice scaffolding. This completely automates the bridge between legacy procedural execution and modern Object-Oriented/REST paradigms.

## The Build System Forge

The orchestrator automatically generates the foundational configuration required to boot the application, ensuring a zero-friction handoff to the engineering team or autonomous agents.

* **`pom.xml`**: Injects strict dependency trees for Spring Web, Spring Data JPA, Spring Batch, and PostgreSQL, locked to Java 17 standards.
* **`application.yml`**: Auto-configures the database connections, Hibernate DDL settings, and disables auto-running batch jobs to prevent accidental execution loops on startup.
* **Application Entry Point**: Generates the primary `@SpringBootApplication` main class.
* **Compliance Injection**: Automatically scans for a `corporate_header.txt` file and wraps it into a standardized Java block comment, injecting it at the top of every generated file to maintain legal compliance.

## The EBCDIC & COMP-3 Decoder Utility

Modern cloud infrastructure operates on ASCII/UTF-8 and standard floating-point math, while legacy mainframes operate on EBCDIC character sets and Packed Decimal (COMP-3) byte arrays. To prevent catastrophic runtime crashes when the new Java system attempts to process dirty legacy data, the controller forges a strict `EbcdicDecoderUtil.java` class.

**Strict Hex-Boundary Validation:**
The decoder unpacks COMP-3 byte arrays into Java `BigDecimal` objects. Because legacy databases frequently contain shifted or corrupt bytes, the generated utility includes strict validation:
* It verifies that the high nibble of every byte is a valid integer (0-9).
* It enforces that the final low nibble is a valid sign identifier (A-F).
* If a dirty byte is detected, the utility safely intercepts the error, logs a hex-dump warning, and defaults to `BigDecimal.ZERO` to prevent the entire Spring Boot application from crashing.