# PII Leak Hunter (Privacy Incident Responder)

> **Sanitizing the Data Stream**
>
> Applications frequently leak Personally Identifiable Information (PII)—like user credit cards, Social Security Numbers, or internal AWS API keys—into standard application logs or database exports. 
>
> The PII Leak Hunter (`pii_leak_hunter.py`) is GitGalaxy's high-speed, single-pass incident response spoke. It is engineered to slice through gigabytes of raw log data, identify exposed sensitive information, and stream out a structurally safe, masked evidence log for security teams.

## The Regex Physics (Binary Optimization)

Parsing massive log files using standard string evaluation is incredibly slow. To achieve maximum computational velocity (often processing multiple gigabytes per second), the Leak Hunter optimizes its search at the byte level.

The engine compiles its mathematical traps (Regex for VISA, Mastercard, SSN, and AWS Keys) strictly as **binary byte patterns** (`br'\b4[0-9]{12}...'`) rather than standard strings. This allows the engine to search the raw physical data stream without paying the CPU penalty of decoding every line into UTF-8 text first.

## The Memory Shield & Safe Masking

Security tools often create secondary security breaches by copying unencrypted credit cards into their own error logs. The Leak Hunter utilizes a strict Memory Shield to prevent this:

1. **Lazy Decoding:** It reads the target file in a raw binary stream. It only decodes a line into readable text *if* one of the binary regex traps is triggered.
2. **Active Masking:** Once a hit is confirmed, the engine passes the string through a surgical masking function (`mask_pii`). 
    * Credit cards are truncated (e.g., `VISA-MASKED-1234`).
    * SSNs are partially obscured (`XXX-XX-1234`).
    * AWS Keys have their internal characters scrubbed (`AKIA-XXXX-ABCD`).
3. **The Evidence Log:** These safe, masked strings are then streamed into a dedicated `_pii_leak_evidence.log` file. This allows incident responders to prove the leak exists and see its surrounding context without actually handling toxic, unencrypted PII.

## Time-Series Exfiltration Histograms

A single exposed credit card in a log file is a bug. Ten thousand exposed credit cards clustered at 2:00 AM is a data exfiltration breach.

As the Hunter streams through the logs, it uses a chronological regex pattern to extract the timestamp of every single PII hit. It aggregates this data into time buckets and draws a dynamically scaled ASCII histogram directly in the terminal.

* **Spike Filtering:** If the log covers a massive time period, the dashboard intelligently filters the view to show only the Top 15 highest-volume spikes.
* **Anomaly Detection:** It calculates the average hit rate across the timeline. If a specific time bucket breaches the anomaly threshold (> 3x the average volume), it actively flags the bucket with a `<-- MASSIVE EXFILTRATION SPIKE` warning.

## Executive Dashboard

Upon completion, the tool prints a final executive summary detailing the total number of hits per category (Visa, SSN, etc.), the total time elapsed, and the exact Processing Velocity in GB/s.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
