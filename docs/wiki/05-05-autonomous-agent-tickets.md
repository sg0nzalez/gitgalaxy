# Autonomous Agent Tickets

> **Architecture: Deterministic LLM Task Orchestration**
>
> **Summary:** To complete the modernization loop, the generated Java code must be populated with the extracted COBOL business rules. Instead of feeding raw COBOL directly into an LLM (which guarantees hallucinations), GitGalaxy packages the isolated logic slices into strict, structured JSON Task Tickets designed for autonomous agents.

## The JSON Ticket Payload

The Agent Forge generates a strict JSON contract (`{prog_id}_java_service_job.json`) that bounds the AI agent to a highly specific, restricted context.

* **Isolated Business Rules:** The ticket contains only the localized logic slice extracted by the Microservice Slicer. The LLM cannot see the whole COBOL monolith; it only sees the exact paragraphs required for the target variable.
* **External Dependencies:** The ticket explicitly lists the unresolved `CALL` statements discovered by the DAG. 
* **Architectural Warnings:** The ticket injects the "Honesty Protocol" flags (e.g., system limit overrides, dynamic jumps) directly into the context window, forcing the AI to account for legacy edge cases.

## The Anti-Hallucination Constraints

The ticket includes a strict System Prompt engineered to suppress generative hallucinations:
1. **No External Systems:** The agent is explicitly forbidden from inventing external systems or databases not defined in the JSON context.
2. **Interface Forcing:** The agent is instructed to write standard interface calls to the provided `external_dependencies`, rather than attempting to guess and write the external logic itself.
3. **Deterministic Output:** The agent is required to return a valid JSON object containing a `diagnosis` string and the isolated `java_code`, ensuring the pipeline can programmatically insert the result into the forged `@Service` class.