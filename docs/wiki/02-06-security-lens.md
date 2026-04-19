# The Security Lens (Threat Detection Physics)

> **Structural Reality and Attack Patterns**
>
> The Security Lens acts as GitGalaxy's physics engine for threat detection. Rather than relying on static vulnerability databases, legacy CVE lists, or hunting for specific, hardcoded malicious strings, it operates strictly on **structural reality and attack patterns**.
>
> Hackers constantly change variable names, cycle IP addresses, and obfuscate text, rendering traditional string-matching tools brittle and obsolete. By scanning the raw Active Matter of a file for the *mechanical signatures* and *behavioral structures* of an attack—such as the precise sequence of operations required to open a reverse shell, mutate a global prototype, or dynamically execute a payload—the Lens becomes highly flexible and robust.
>
> This pattern-based approach allows GitGalaxy to proactively shield against novel, zero-day vulnerabilities. Because the engine measures the literal density of dangerous operations and structural intent, it can successfully detect and flag malicious code even if that specific payload has never been seen before in the wild.

## Dynamic Policy Injection (Threshold Governance)

To maintain architectural purity and extreme adaptability, the Security Lens is entirely decoupled from policy-making; it does not hardcode rigid rules or rely on easily bypassed blocklists. Instead, it acts strictly as a structural measurement tool.

Upon initialization, the Lens ingests a dynamic threshold policy (typically provided by `gitgalaxy_standards.ThreatPolicy`). This governs the trigger limits for core exposure vectors like Secrets Risk, Hidden Malware, Logic Bombs, Injection Surfaces, and Memory Corruption.

Because the underlying sensors detect *categories of malicious behavior* rather than exact string matches, these dynamic thresholds allow security teams to easily dial their risk tolerance up or down. If a novel class of obfuscation or injection emerges, the structural sensors are highly likely to catch its mechanical footprint automatically; the orchestrator simply adjusts the threshold policy to tighten the net. 

## Raw Sensors: The Threat Signatures

The engine utilizes specialized, hardware-level regex sensors to scan the logic streams. Crucially, these sensors are not hunting for known, hardcoded malicious strings—they are scanning for the **invariable mechanical footprints of an attack**.

While a hacker can easily change variable names or invent a novel zero-day payload, they *cannot* change the fundamental laws of computing. To execute a payload, they must eventually spawn a shell; to hide code, they must encode it; to establish command and control, they must open a socket. By measuring these structural necessities, the Security Lens detects the *intent* of the code.

These are the structural patterns the engine actively measures:

1. **The Glassworm (Obfuscation):** Detects the thermal signatures of hidden payloads. This sensor triggers on the *structure* of evasion: nested encoding functions (`atob`, `base64_decode`, `gzuncompress`), massive strings of raw base64 data, and invisible Unicode characters actively used to bypass standard lexical scanners.
2. **The Trojan (Identity Masking & Safety Bypasses):** Flags logic that actively attempts to disarm the host environment's safety parameters. It detects the structural pattern of lowering shields—such as assigning false to SSL verification (`NODE_TLS_REJECT_UNAUTHORIZED=0`), dynamically turning off `safe_mode`, or executing recursive decodes.
3. **Exfiltration Vectors (System IO):** Monitors the code for aggressive external gravity. It flags the *mechanics* of unauthorized networking, such as hardcoded raw IP structures, anomalous raw socket creation, and direct protocol connections to tunneling services (e.g., `ngrok.io`, `pastebin.com`).
4. **The Executioner (Dynamic Payloads):** Detects the structural shape of dangerous, dynamic execution capabilities. This catches zero-day payloads by flagging the literal syntax required to execute arbitrary strings, including raw `eval()`, OS-level shell spawning (`child_process.exec`), and dangerous prototype manipulations.
5. **Environment Poisoning (State Flux):** Flags attempts to mutate the fundamental state of the application. It looks for the syntactical patterns of overriding global architectures, triggering on `__proto__` pollution, overriding global `fetch`/`eval` functions, or rewriting core server environment arrays.
6. **Shadow Logic (Necrosis / Graveyard):** Scans the Ghost Mass (the isolated `comment_stream`) for dead or hidden threats. By looking for the syntax of active execution (like `nc -e` or `curl | bash`) trapped inside inactive documentation, it catches malicious logic masquerading as innocent prose.
7. **Sub-Atomic Decryption (Bitwise Math):** Detects dense, looping clusters of bitwise XOR (`^`) operations. The specific looping *structure* of dense XOR clusters in standard application code is a primary, invariable indicator of custom malware decryption routines.
8. **Shadow Imports (Steganography):** Identifies the structural contradiction of attempting to execute non-executable file types. Triggers when the logic stream tries to `require` or `import` media structures (`.png`, `.jpg`), PDFs, or audio files as active logic scripts.
9. **Unicode Smuggling (Homoglyphs & Typosquatting):** Detects Cyrillic or specialized Unicode blocks maliciously injected within standard `import` or `fetch` statements. It identifies the visual spoofing mechanic used to hijack execution flow by mimicking legitimate library names.
10. **The Vault Door (Credential & Secret Leaks):** A highly sensitive sensor scanning the assignment patterns of high-entropy literal strings bound to secure-sounding keys (e.g., `api_key`, `client_secret`), catching leaked credentials regardless of the specific token value.
11. **Raw Memory Overrides:** Flags the mechanical manipulation of RAM. It detects the specific syntax for manual memory allocation (`malloc`, `memcpy`, `free`) as well as inline assembly instructions (`__asm__`), which are the invariable prerequisites for introducing buffer overflow vulnerabilities.
12. **Agentic RCE & Prompt Injection Boundaries:** Identifies hooks to external LLMs (OpenAI, Anthropic, Langchain) to establish the presence of autonomous AI logic.
13. **Raw Database Sinks:** Identifies raw SQL execution commands, providing the downstream taint analyzer with terminal endpoints for injection attacks.

## The Scan Engine: Structural Reality Capture

During the scan phase, the `scan_content` method acts as a completely passive observer. It channels the file's pure logic stream through the hardware sensors, tallying the raw integer count of structural hits.

* **The Minification Shield:** The engine isolates snippets only from human-readable lines (under 250 chars) to prevent massive minified bundles from stalling the regex engine.
* **The Auto-Gen Shield:** If a file announces itself as machine-generated (e.g., `DO NOT EDIT`), the engine skips entropy and homoglyph checks, as generated code naturally contains massive string blocks and ugly escapes that would trigger false positives.

### Shannon Entropy (The Math of Chaos)
For strings longer than 64 characters, the engine calculates the Shannon Entropy. Uncompressed text usually hovers around 4-5. Encrypted or heavily packed payloads push 7.9+. If a string breaches the high-entropy threshold, it is flagged as a potential hidden payload.

### N-Dimensional Taint Analysis (The LHS Slicer)
The engine doesn't just look for isolated dangerous commands; it tracks the *flow* of data.
* **Same-Line Detonation:** Instantly flags if an I/O command and an Execution command happen on the same line (e.g., fetching a URL and immediately passing it to `eval`).
* **The LHS Slicer:** If an I/O command or LLM hook assigns data to a variable, the engine stores that variable in a "Tainted" set.
* **The Downward Scan:** As the engine continues down the file, if it sees a tainted variable passed into a dangerous execution command, it confirms a severe injection vulnerability.
* **Agentic RCE:** Specifically tracks if data from an LLM flows directly into an OS-level execution command, flagging a critical Agentic Remote Code Execution flaw.

## Risk Evaluation & Exposure Mapping

Traditional security scanners often drown development teams in false positives because they rely on raw hit counts. A 10,000-line monolithic legacy file will naturally contain more IO calls and base64 strings than a 10-line microservice, even if both are completely benign.

To solve this scaling problem, the `evaluate_risk` method calculates **Threat Density** using a strict equation: 

$$\text{Threat Density} = \frac{\text{Total Hits}}{\text{Safe LOC}}$$

By measuring the *concentration* of dangerous patterns relative to the file's total mass, the engine scales its risk assessment regardless of repository size.

### The Network Gravity Modifier
A file with a massive blast radius cannot be allowed to have even minor threat densities. The engine imports the file's `PageRank` and `Betweenness` scores from the `NetworkRiskSensor`. If a file is highly central (a "God Node"), its perceived threat density is multiplied exponentially, ensuring that critical infrastructure is held to a near-zero tolerance standard.

The engine mathematically aggregates the telemetry into core exposure vectors, triggering alerts if the calculated density breaches the dynamically injected policy thresholds:

* **Hidden Malware Risk:** Measures the density of active evasion and steganography tactics. *(Aggregation: Glassworm + Bitwise Math + Shadow Imports + Homoglyphs + Entropy)*
* **Logic Bomb Risk:** Detects sabotage and destructive payloads. *(Aggregation: Graveyard + (Executioner $\times$ 1.5))*
* **Data Injection Risk:** Maps the structural attack surface for unauthorized state manipulation, remote code execution, and data exfiltration. *(Aggregation: System IO + Executioner + State Flux)*
* **Memory Corruption Risk:** Strictly isolates the density of manual memory manipulation, flagging potential buffer overflow vulnerabilities.
* **Secrets Leak Risk:** A highly sensitive threshold strictly monitoring Vault Door hits.
* **Agentic RCE & Prompt Injection Risk:** A critical alert specifically triggered if the Taint Analyzer confirmed untrusted data flowing into an LLM, or an LLM controlling OS execution.

## The X-Ray Binary Sensor
When the Aperture Filter encounters an opaque binary (e.g., `.png`, `.zip`, `.dll`), the Security Lens performs a zero-RAM X-Ray on the first 8KB of the payload.
* **Magic Byte Verification:** Checks if the file's internal binary header actually matches its extension.
* **Parasite Detection:** Scans the binary chunk for embedded execution headers (like `ELF`, `MZ`, or `#!/bin/`) hiding inside non-executable files.
* **High-Entropy Carving:** Measures the entropy of the binary chunk. If it exceeds 7.95, it flags the binary as an encrypted or heavily packed weaponized payload.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.

