# 2.3.9. The Audit Recorder

> **The SHBOM (Structural Health Bill of Materials)**
>
> The Astrograph Auditor (`audit_recorder.py`) is the final stage of the GitGalaxy pipeline. It extracts the raw telemetry from live RAM and compiles it into a verbose, human-readable forensic JSON manifest. Designed for strict enterprise compliance and deep-dive debugging, it guarantees absolute traceability for every file evaluated.

## 2.3.9.A. Key Architectural Features

* **The Traceability Anchor:** Imprints the exact Git footprint (Branch, SHA-1 Hash, Remote URL) and engine timestamp into the header, ensuring the audit is permanently cryptographically tied to the state of the repository at the exact moment of the scan.
* **Hierarchical Constellation Mapping:** Rather than dumping a flat list of files, the Auditor intelligently sorts the "Visible Matter" by Constellation (folder) and ranks them descending by total structural mass.
* **Security Triage Routing:** To prevent alert fatigue, the engine explicitly decouples active malicious threats from general structural risks. It evaluates the raw threat signatures and assigns a strict repository status: `SECURE`, `ELEVATED_SURFACE_RISK`, or `CRITICAL_THREATS_DETECTED`.
* **Dark Matter Preservation:** Files rejected during the pipeline are never silently deleted. They are logged in the Dark Matter archive with explicit diagnostic reasons (e.g., "Optical Bypass," "Ecosystem Orphan," "Unsupported Extension") so engineers can audit the pipeline's blind spots.

## 2.3.9.B. The Blank Audit Skeleton (`galaxy_audit.json`)

Here is the structural blueprint of the final output. You can use this blank template to understand the exact data hierarchy GitGalaxy produces:

```json
{
  "Audit Protocol": "GitGalaxy v6.2.0-Audit",
  "1. Forensic Trail (Traceability)": {
    "Analysis Context": {
      "Engine Identity": "",
      "Target Root Name": "",
      "Absolute Project Path": "",
      "Analysis ISO Timestamp": "",
      "Total Scan Duration": ""
    },
    "Source Control Footprint (Immutable Anchor)": {
      "Active Branch": "",
      "Commit Hash (SHA-1)": "",
      "Remote Origin URL": "",
      "Last Code Integration Date": ""
    }
  },
  "2. Global Synthesis Summary": {
    "summary": {},
    "singularity": {},
    "health": {},
    "composition": {},
    "constellations": {}
  },
  "3. Forensic Security & Vulnerability Audit": {
    "Audit Status": "[SECURE | ELEVATED_SURFACE_RISK | CRITICAL_THREATS_DETECTED]",
    "Scope": {},
    "Exposed Secrets & Credentials (Quarantined Files)": [],
    "Vulnerability Exposures (Threshold Breaches)": {},
    "Raw Threat Signature Hits (Total Repository Occurrences)": {}
  },
  "4. High-Value Forensic Report": {
    "exposures": {
      "cognitive_load": { "highest": [], "lowest": [] },
      "safety_score": { "highest": [], "lowest": [] },
      "tech_debt": { "highest": [], "lowest": [] }
      // ... iterates through all 18 risk exposures
    },
    "file_impact": { "highest": [], "lowest": [] },
    "function_impact": { "highest": [], "lowest": [] },
    "cumulative_risk": { "highest": [], "lowest": [] }
  },
  "5. Dark Matter (Excluded Artifacts)": [
    {
      "Path": "",
      "Forensic Category": "Dark Matter (Excluded Artifact)",
      "Diagnostic Reason": "",
      "Size": "",
      "Identity Confidence": "",
      "Discovery Proof": ""
    }
  ],
  "6. Visible Matter (Scanned Artifacts)": {
    "[Constellation/Folder Name]": {
      "Constellation Mass": 0.0,
      "File Count": 0,
      "Average Risk Exposures": {},
      "Stars / Files": {
        "[File Path]": {
          "1. Identity": {},
          "2. Spatial Coordinates": {},
          "3. Galactic Profile": {},
          "4. Risk Exposures": {},
          "5. Function Analysis (Satellites)": [],
          "6. Structural DNA (Raw Hits)": {},
          "7. Extracted Dependencies": []
        }
      }
    }
  }
}
