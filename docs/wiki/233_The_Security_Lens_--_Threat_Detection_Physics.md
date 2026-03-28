# 2.3.3. The Security Lens (Threat Detection Physics)

> **Structural Reality and Attack Patterns**
>
> The Security Lens acts as GitGalaxy's physics engine for threat detection. Rather than relying on static vulnerability databases, legacy CVE lists, or hunting for specific, hardcoded malicious strings, it operates strictly on **structural reality and attack patterns**.
>
> Hackers constantly change variable names, cycle IP addresses, and obfuscate text, rendering traditional string-matching tools brittle and obsolete. By scanning the raw Active Matter of a file for the *mechanical signatures* and *behavioral structures* of an attack—such as the precise sequence of operations required to open a reverse shell, mutate a global prototype, or dynamically execute a payload—the Lens becomes highly flexible and robust.
>
> This pattern-based approach allows GitGalaxy to proactively shield against novel, zero-day vulnerabilities. Because the engine measures the literal density of dangerous operations and structural intent, it can successfully detect and flag malicious code even if that specific payload has never been seen before in the wild.

## 2.3.3.A. Dynamic Policy Injection (Threshold Governance)

To maintain architectural purity and extreme adaptability, the Security Lens is entirely decoupled from policy-making; it does not hardcode rigid rules or rely on easily bypassed blocklists. Instead, it acts strictly as a structural measurement tool.

Upon initialization, the Lens ingests a dynamic threshold policy (typically provided by `gitgalaxy_standards.ThreatPolicy`). This governs the trigger limits for five core exposure vectors: Secrets Risk, Hidden Malware, Logic Bombs, Injection Surfaces, and Memory Corruption.

Because the underlying sensors detect *categories of malicious behavior* rather than exact string matches, these dynamic thresholds allow security teams to easily dial their risk tolerance up or down. If a novel class of obfuscation or injection emerges, the structural sensors are highly likely to catch its mechanical footprint automatically; the orchestrator simply adjusts the threshold policy to tighten the net. If no strict policy is provided by the orchestrator, the Lens safely falls back to a highly secure baseline threshold.

## 2.3.3.B. Raw Sensors: The 11 Threat Signatures

The engine utilizes specialized, hardware-level regex sensors to scan the logic streams. Crucially, these sensors are not hunting for known, hardcoded malicious strings—they are scanning for the **invariable mechanical footprints of an attack**.

While a hacker can easily change variable names, cycle IP addresses, or invent a novel zero-day payload, they *cannot* change the fundamental laws of computing. To execute a payload, they must eventually spawn a shell; to hide code, they must encode it; to establish command and control, they must open a socket. By measuring these structural necessities, the Security Lens detects the *intent* of the code.

**The Permutation Scale:** Because these sensors use highly advanced regex matrices to account for arbitrary whitespace, variable naming, and nesting depths, a single signature in GitGalaxy effectively scans against millions of syntactical permutations simultaneously. Across all 11 sensors, the engine is evaluating the code against an effectively infinite combination of attack structures in a single pass, rendering evasion highly difficult.

These are the 11 structural patterns the engine actively measures:

1. **The Glassworm (Obfuscation):** Detects the thermal signatures of hidden payloads. Rather than looking for specific malware hashes, this sensor triggers on the *structure* of evasion: nested encoding functions (`atob`, `base64_decode`, `gzuncompress`), massive strings of raw base64 data, and invisible Unicode characters (like Zero-Width Spaces) actively used to bypass standard lexical scanners.
2. **The Trojan (Identity Masking & Safety Bypasses):** Flags logic that actively attempts to disarm the host environment's safety parameters. It detects the structural pattern of lowering shields—such as assigning false to SSL verification (`NODE_TLS_REJECT_UNAUTHORIZED=0`), dynamically turning off `safe_mode` or `open_basedir`, or executing recursive decodes.
3. **Exfiltration Vectors (System IO):** Monitors the code for aggressive external gravity. It doesn't just block known bad domains; it flags the *mechanics* of unauthorized networking, such as hardcoded raw IP structures, anomalous raw socket creation, and direct protocol connections to tunneling services (e.g., `ngrok.io`, `localtunnel.me`, `pastebin.com`).
4. **The Executioner (Dynamic Payloads):** Detects the structural shape of dangerous, dynamic execution capabilities. This catches zero-day payloads by flagging the literal syntax required to execute arbitrary strings, including raw `eval()`, OS-level shell spawning (`child_process.exec`, `passthru`), and dangerous prototype manipulations.
5. **Environment Poisoning (State Flux):** Flags attempts to mutate the fundamental state of the application. It looks for the syntactical patterns of overriding global architectures, triggering on `__proto__` pollution, overriding global `fetch`/`eval` functions, or rewriting core server environment arrays (`$_SERVER`, `sys.modules`).
6. **Shadow Logic (Necrosis / Graveyard):** Scans the Ghost Mass (the isolated `comment_stream`) for dead or hidden threats. By looking for the syntax of active execution (like `nc -e` or `curl | bash`) trapped inside inactive documentation, it catches malicious logic masquerading as innocent prose.
7. **Sub-Atomic Decryption (Bitwise Math):** Detects dense, looping clusters of bitwise XOR (`^`) operations. While occasionally used in legitimate cryptography, the specific looping *structure* of dense XOR clusters in standard application code is a primary, invariable indicator of custom malware decryption routines.
8. **Shadow Imports (Steganography):** Identifies the structural contradiction of attempting to execute non-executable file types. Triggers when the logic stream tries to `require` or `import` media structures (`.png`, `.jpg`), PDFs, or audio files as active logic scripts.
9. **Unicode Smuggling (Homoglyphs & Typosquatting):** Detects Cyrillic or specialized Unicode blocks maliciously injected within standard `import` or `fetch` statements. It identifies the visual spoofing mechanic used to hijack execution flow by mimicking legitimate library names.
10. **The Vault Door (Credential & Secret Leaks):** A highly sensitive sensor scanning the assignment patterns of high-entropy literal strings bound to secure-sounding keys (e.g., `api_key`, `client_secret`, `auth_token`), catching leaked credentials regardless of the specific token value.
11. **Raw Memory Overrides:** Flags the mechanical manipulation of RAM. It detects the specific syntax for manual memory allocation (`malloc`, `memcpy`, `free`) as well as inline assembly instructions (`__asm__`), which are the invariable prerequisites for introducing buffer overflow vulnerabilities.

## 2.3.3.C. The Scan Engine: Structural Reality Capture

During the scan phase, the `scan_content` method acts as a completely passive observer. It channels the file's pure logic stream (the Active Matter) through the 11 hardware sensors, tallying the raw integer count of structural hits.

At this stage, the engine makes absolutely no judgments about intent or risk; it simply captures the physical reality of the code's architecture. By decoupling observation from evaluation, GitGalaxy eliminates the "noisy scanner" problem. A file isn't immediately flagged as malicious just because it contains a single base64 decode or a raw network socket. The scan engine's only job is to generate the pristine, objective telemetry required for the physics engine to calculate its math.

## 2.3.3.D. Risk Evaluation & Exposure Mapping

Traditional security scanners often drown development teams in false positives because they rely on raw hit counts. A 10,000-line monolithic legacy file will naturally contain more IO calls and base64 strings than a 10-line microservice, even if both are completely benign.

To solve this scaling problem, the `evaluate_risk` method calculates **Threat Density** using a strict equation: 

$$\text{Threat Density} = \frac{\text{Total Hits}}{\text{Safe LOC}}$$

By measuring the *concentration* of dangerous patterns relative to the file's total mass, the engine perfectly scales its risk assessment regardless of repository size.

The engine mathematically aggregates the telemetry from the 11 raw sensors into **5 core exposure vectors**. It only triggers actionable alerts if the calculated density breaches the dynamically injected policy thresholds:

* **Hidden Malware Risk:** Measures the density of active evasion and steganography tactics. *(Aggregation: Glassworm + Bitwise Math + Shadow Imports + Homoglyphs)*
* **Logic Bomb Risk:** Detects sabotage and destructive payloads. Because dynamic execution is highly volatile in this context, the engine applies a severe penalty multiplier. *(Aggregation: Graveyard + (Executioner $\times$ 1.5))*
* **Data Injection Risk:** Maps the structural attack surface for unauthorized state manipulation, remote code execution, and data exfiltration. *(Aggregation: System IO + Executioner + State Flux)*
* **Memory Corruption Risk:** Strictly isolates the density of manual memory manipulation, flagging potential buffer overflow and use-after-free vulnerabilities. *(Aggregation: Raw Memory Overrides)*
* **Secrets Leak Risk:** A highly sensitive threshold strictly monitoring Vault Door hits. Because hardcoded credentials require almost zero density to be catastrophic, this vector operates on a micro-threshold to instantly flag leaked keys.
