#!/usr/bin/env python3
# ==============================================================================
# GitGalaxy Tool: AI Application Security (AppSec) Sensor
#
# PURPOSE:
# Scans the repository for vulnerable AI architectures built by developers.
# It flags dangerous intersections where LLMs (which are vulnerable to Prompt
# Injection) are given access to OS commands, database writes, or unfiltered
# network sockets.
#
# ARCHITECTURAL DECISION:
# AI agents with unconstrained execution boundaries represent a critical 
# security risk. By analyzing the structural topology of the codebase, this 
# sensor deterministically identifies Autonomous Execution Vectors and 
# Over-Permissioned Agents before they reach production.
# ==============================================================================
import logging
from typing import List, Dict, Any


class AIAppSecSensor:
    """
    AI Application Security (AppSec) Threat Sensor.
    """

    def __init__(self, parent_logger=None):
        self.logger = parent_logger.getChild("appsec_sensor") if parent_logger else logging.getLogger("appsec_sensor")

    def hunt_threats(self, parsed_files: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        self.logger.info("AI AppSec Sensor: Scanning for Agentic Vulnerabilities...")

        for file_data in parsed_files:
            # Extract the raw structural signatures (assuming they are tallied in 'telemetry')
            telemetry = file_data.get("telemetry", {})

            # Extract specific architectural signals
            ai_orchestrator = telemetry.get("ai_orchestrator", 0) > 0
            llm_api = telemetry.get("llm_api", 0) > 0
            ai_tools = telemetry.get("ai_tools", 0) > 0

            arch_api = telemetry.get("arch_api", 0) > 0  # Publicly exposed
            arch_io = telemetry.get("arch_io", 0) > 0  # Network/Disk I/O
            db_complexity = file_data.get("max_db_complexity", 0)  # Data gravity

            # Security Structural Signatures
            sec_danger = telemetry.get("sec_high_risk_execution", 0) > 0  # eval, exec, subprocess
            sec_secrets = telemetry.get("sec_secrets", 0) > 0  # Hardcoded keys/env access
            safety_density = telemetry.get("safety_density", 1.0)  # Defensive programming (try/catch, regex)

            appsec_report = {
                "is_rce_funnel": False,
                "over_permissioned_agent": False,
                "agentic_exfiltration_risk": False,
                "critical_warnings": [],
            }

            # 1. Autonomous Execution Vector (Weaponized Prompt Injection)
            # LLM Logic + Public API Router + OS Command Execution
            if (ai_orchestrator or llm_api) and arch_api and sec_danger:
                appsec_report["is_rce_funnel"] = True
                appsec_report["critical_warnings"].append(
                    "CRITICAL [Autonomous Execution Vector]: AI logic is adjacent to OS-level execution (eval/subprocess) and exposed via API. Immediate Prompt Injection -> Autonomous Execution vulnerability."
                )

            # 2. Over-Permissioned Agent Binding (Autonomous Escalation)
            # AI Agent Tools + State Mutation (DB or Disk) + Low Defensive Safety
            if ai_tools and (db_complexity >= 2 or arch_io) and safety_density < 0.5:
                appsec_report["over_permissioned_agent"] = True
                appsec_report["critical_warnings"].append(
                    "CRITICAL [Over-Permissioned Agent]: AI is bound to tools with raw Database/IO write access and < 50% safety density. High risk of autonomous data corruption."
                )

            # 3. Agentic Exfiltration Vector (Unsandboxed Sockets)
            # LLM Logic + Outbound Sockets/Fetch + Access to Secrets
            if llm_api and arch_io and sec_secrets:
                appsec_report["agentic_exfiltration_risk"] = True
                appsec_report["critical_warnings"].append(
                    "CRITICAL [Agentic Exfiltration Vector]: LLM logic has access to network sockets AND environment secrets. High risk of SSRF and key exfiltration via prompt injection."
                )

            # Inject the AppSec report back into the file's telemetry
            file_data["telemetry"]["ai_appsec"] = appsec_report

        return parsed_files