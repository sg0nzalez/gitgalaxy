# The Neural Auditor (Weight Inspection)

> **Inspecting the AI Brain**
>
> As developers increasingly check Large Language Models (LLMs) and LoRA adapters directly into their repositories, scanners face a physical constraint: you cannot load a 70GB model weight file into RAM just to parse it. 
>
> The Neural Auditor (`neural_auditor.py`) solves this by surgically inspecting massive AI model binaries (`.safetensors`, `.gguf`) without ever loading the full file into memory. It extracts parameter counts, quantization levels, and architecture families directly from the binary headers, allowing GitGalaxy to map the exact scale of local AI compute.

## Zero-RAM Inspection

When the Aperture Filter relegates a massive binary file to "Dark Matter," the Orchestrator checks if the file is a known AI model format. If so, it passes the file path to the Neural Auditor, which executes a highly targeted, zero-RAM byte read. 

The Auditor routes the file to the correct parser based on its extension:

### 1. Safetensors Extraction
The `.safetensors` format (standardized by HuggingFace) is designed for safe, fast loading. The Auditor leverages this structure:
* **The 8-Byte Header Read:** The engine reads only the first 8 bytes of the file (a little-endian `uint64`) to determine the exact size of the JSON metadata header.
* **The Anti-Hallucination Shield:** Before reading the JSON, it checks if the reported header size is suspiciously large (e.g., > 100MB). If so, it aborts the read to prevent maliciously crafted files from causing a memory overflow.
* **Parameter Mathematics:** Once the JSON header is securely parsed, the Auditor extracts the architecture family (e.g., LLaMA, Mistral). It then calculates the exact parameter count of the model by multiplying the multidimensional shapes of every tensor listed in the file.
* **Formatting:** It converts the raw integer count into human-readable formats (e.g., "8.0B" or "350.0M").

### 2. GGUF Heuristics
The `.gguf` format (used heavily by `llama.cpp` for local quantized inference) embeds its metadata as Key-Value pairs scattered through the binary header. 
* **Magic Byte Verification:** The Auditor reads the first 4 bytes to verify the `GGUF` magic number, ensuring it isn't a spoofed file.
* **The 1MB Chunk Scan:** Fully unpacking the GGUF binary tree natively in Python is computationally expensive. Instead, the Auditor reads a raw 1MB chunk of the header and decodes it as an ASCII string.
* **Heuristic Extraction:** It uses fast heuristic string matching to identify the architecture family (e.g., "llama", "qwen") and the specific quantization level (e.g., "Q4_K", "Q8_0") utilized by the model.

## The Neural Supernova

Once the Auditor successfully extracts the model's metadata, it passes the intelligence back to the Orchestrator. 

Because AI model weights are incredibly dense and represent massive local compute gravity, the Orchestrator injects this data back into the 3D map as a **Neural Supernova**. The file is given a massive gravitational footprint (calculated by dividing its gigabyte size by a scalar) and its extracted metadata (Architecture, Parameter Count, Quantization) is attached directly to the visual node, allowing architects to see exactly what kind of AI brain is embedded in their repository.

<br><br>

---

### 🌌 Powered by the blAST Engine

This documentation is part of the [GitGalaxy Ecosystem](https://github.com/squid-protocol/gitgalaxy), an AST-free, LLM-free heuristic knowledge graph engine.

* 🪐 **[Explore the GitHub Repository](https://github.com/squid-protocol/gitgalaxy)** for code, tools, and updates.
* 🔭 **[Visualize your own repository at GitGalaxy.io](https://gitgalaxy.io/)** using our interactive 3D WebGPU dashboard.



---

**[⬅️ Back to Master Index](index.md)**
