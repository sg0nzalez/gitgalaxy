# IMPORTANT: Adjust this path to match exactly where your file is located
from gitgalaxy.tools.ai_guardrails.ai_appsec_sensor import AIAppSecSensor


# ==============================================================================
# TEST 1: The RCE Funnel (Weaponized Prompt Injection)
# ==============================================================================
def test_rce_funnel_detection():
    """
    Proves that an LLM directly wired to OS execution (eval/subprocess)
    and exposed via a public API correctly triggers the RCE Funnel alert.
    """
    sensor = AIAppSecSensor()

    mock_files = [
        {
            "telemetry": {
                "llm_api": 1,  # ☢️ AI is present
                "arch_api": 1,  # ☢️ Exposed to the public internet
                "sec_high_risk_execution": 1,  # ☢️ Contains eval() or subprocess execution
                "safety_density": 0.9,
            }
        }
    ]

    result = sensor.hunt_threats(mock_files)
    appsec_report = result[0]["telemetry"]["ai_appsec"]

    assert appsec_report["is_rce_funnel"] is True, "Failed to detect the RCE Funnel!"
    assert any(
        "RCE Funnel" in warning for warning in appsec_report["critical_warnings"]
    )


# ==============================================================================
# TEST 2: The God-Mode Agent (Autonomous Data Corruption)
# ==============================================================================
def test_god_mode_agent_detection():
    """
    Proves that an AI agent given autonomous tools, write-access to complex
    databases, and low defensive programming density triggers the God-Mode alert.
    """
    sensor = AIAppSecSensor()

    mock_files = [
        {
            "max_db_complexity": 3,  # ☢️ Heavy database write access
            "telemetry": {
                "ai_tools": 1,  # ☢️ Agentic tool calling enabled
                "safety_density": 0.2,  # ☢️ Dangerously low defensive programming
            },
        }
    ]

    result = sensor.hunt_threats(mock_files)
    appsec_report = result[0]["telemetry"]["ai_appsec"]

    assert appsec_report["over_permissioned_agent"] is True, (
        "Failed to detect the God-Mode Agent!"
    )
    assert any(
        "God-Mode Agent" in warning for warning in appsec_report["critical_warnings"]
    )


# ==============================================================================
# TEST 3: The Exfiltration Vector (Unsandboxed Sockets)
# ==============================================================================
def test_exfiltration_vector_detection():
    """
    Proves that an LLM with access to both raw network sockets and hardcoded
    environment secrets triggers the Exfiltration Vector alert.
    """
    sensor = AIAppSecSensor()

    mock_files = [
        {
            "telemetry": {
                "llm_api": 1,  # ☢️ AI is present
                "arch_io": 1,  # ☢️ Can make outbound network requests
                "sec_secrets": 1,  # ☢️ Has access to AWS keys/passwords
            }
        }
    ]

    result = sensor.hunt_threats(mock_files)
    appsec_report = result[0]["telemetry"]["ai_appsec"]

    assert appsec_report["agentic_exfiltration_risk"] is True, (
        "Failed to detect the Exfiltration Vector!"
    )
    assert any(
        "Exfiltration Vector" in warning
        for warning in appsec_report["critical_warnings"]
    )


# ==============================================================================
# TEST 4: The Clean Baseline (False-Positive Guard)
# ==============================================================================
def test_safe_baseline():
    """
    Proves that a properly sandboxed AI integration (e.g., an LLM script with
    no network execution, no eval(), and high safety density) passes cleanly.
    """
    sensor = AIAppSecSensor()

    mock_files = [
        {
            "max_db_complexity": 0,
            "telemetry": {
                "llm_api": 1,  # ✅ AI is present
                "arch_api": 0,  # ✅ Not exposed to the public
                "sec_high_risk_execution": 0,  # ✅ No eval/subprocess
                "sec_secrets": 0,  # ✅ No secrets exposed
                "safety_density": 0.95,  # ✅ High defensive try/catch density
            },
        }
    ]

    result = sensor.hunt_threats(mock_files)
    appsec_report = result[0]["telemetry"]["ai_appsec"]

    # Assert absolutely NO flags were triggered
    assert appsec_report["is_rce_funnel"] is False
    assert appsec_report["over_permissioned_agent"] is False
    assert appsec_report["agentic_exfiltration_risk"] is False
    assert len(appsec_report["critical_warnings"]) == 0, (
        "False positive triggered on a safe file!"
    )
