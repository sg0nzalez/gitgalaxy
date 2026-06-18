#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Spoke: Autonomous Agent Task Forge
# Purpose: Converts architectural anomalies into structured JSON job tickets
#          designed for automated LLM agent dispatchers.
# ==============================================================================
import json
from pathlib import Path


def generate_agent_ticket(
    file_name: str, source_file: Path, anomalies: list, ir_state: dict
) -> dict:
    """Forges a structured JSON task ticket for an autonomous agent."""

    # Extract lineage to give the agent dependency context
    lineage = {}
    if ir_state:
        lineage = ir_state.get("analysis", {}).get("lineage", {})

    clean_anomalies = [
        a.split("]", 1)[-1].strip() if "]" in a else a for a in anomalies
    ]

    ticket = {
        "job_id": f"{file_name.split('.')[0]}_REMEDIATION",
        "status": "PENDING",
        "task_type": "STRUCTURAL_ANOMALY_RESOLUTION",
        "target_file": str(source_file.resolve()),
        "context": {
            "detected_anomalies": clean_anomalies,
            "inputs_required": list(lineage.get("inputs", [])),
            "outputs_produced": list(lineage.get("outputs", [])),
            "external_calls": list(lineage.get("unresolved_calls", [])),
        },
        "system_prompt": (
            "You are a deterministic legacy systems architect. Your task is to analyze the "
            "provided 'target_file' and resolve the issues listed in 'detected_anomalies'. "
            "Do not alter the core business logic. Return your proposed solution as a valid JSON "
            "object containing a 'diagnosis' string and a 'patched_code' string."
        ),
    }

    return ticket


def forge_agent_jobs(clean_room_dir: Path, source_dir: Path, honesty_flags: list):
    """Parses global flags and generates individual JSON job tickets per file."""
    if not honesty_flags:
        return 0

    out_dir = clean_room_dir / "06_ai_agent_jobs"
    out_dir.mkdir(parents=True, exist_ok=True)
    ir_dir = clean_room_dir / "04_ir_state_dumps"

    # Group flags by file
    file_flags = {}
    for flag in honesty_flags:
        if flag.startswith("[") and "]" in flag:
            file_name = flag[1 : flag.index("]")]
            if file_name not in file_flags:
                file_flags[file_name] = []
            file_flags[file_name].append(flag)

    jobs_generated = 0
    for file_name, anomalies in file_flags.items():
        source_file = next(source_dir.rglob(file_name), None)
        if not source_file:
            continue

        # Grab the IR state for extra context if it exists
        prog_id = file_name.split(".")[0]
        ir_file = ir_dir / f"{prog_id}_ir.json"
        ir_state = (
            json.loads(ir_file.read_text(encoding="utf-8"))
            if ir_file.exists()
            else None
        )

        ticket = generate_agent_ticket(file_name, source_file, anomalies, ir_state)

        ticket_file = out_dir / f"{prog_id}_agent_job.json"
        ticket_file.write_text(json.dumps(ticket, indent=2), encoding="utf-8")
        jobs_generated += 1

    return jobs_generated
