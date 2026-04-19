# Zero-Trust Meta Auditor

> **Architecture: Diff Calculation & I/O Validation**
>
> **Summary:** The JCL Meta Auditor acts as a verification gateway. It compares the newly forged GitGalaxy Zero-Trust JCLs against the original IBM legacy JCLs to calculate exact code bloat reduction and quantify the elimination of over-permissioned I/O access.

## Intent Parsing & Legacy Mapping
Mainframe environments often contain dozens of duplicated, fragmented, or obsolete JCL scripts that call the same underlying COBOL program. 
* The auditor scans the original repository and groups legacy JCLs by their primary executable (`EXEC PGM=`).
* If multiple legacy scripts call the same program, the auditor maps the "worst offender"—the script with the highest lines of code and the most data definitions—as the baseline for comparison.
* It strictly filters out standard IBM system noise (e.g., `STEPLIB`, `SYSOUT`, `IEFBR14`, `IDCAMS`) to focus solely on custom business data definitions.

## The Security Diff Calculation
The auditor compares the baseline legacy metrics against the newly forged GitGalaxy JCLs:
* **Code Bloat Reduction:** Calculates the exact number of lines saved by moving from monolithic, multi-step legacy jobs to streamlined, program-specific emulators.
* **Over-Permissioned I/O Shedding:** Calculates the `excess_dds_blocked`. If a legacy JCL granted access to 15 datasets, but the COBOL AST proves the program only ever opens 3 of them, the auditor records the 12 blocked datasets as a quantifiable security improvement (Least Privilege Enforcement).