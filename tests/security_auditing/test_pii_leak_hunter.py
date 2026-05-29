import pytest
import sys
from pathlib import Path
from unittest.mock import patch

# IMPORTANT: Adjust this path to match exactly where your file is located
import gitgalaxy.tools.terabyte_log_scanning.pii_leak_hunter as pii_module


# ==============================================================================
# TEST 1: The Masking Engine (Data Destruction Verification)
# ==============================================================================
def test_pii_masking_engine():
    """
    Mathematically verifies that the regex engine correctly intercepts and
    destroys sensitive PII data while preserving the safe formatting.
    """
    # 1. VISA Test (Destroy 12 digits, keep last 4)
    assert pii_module.mask_pii("Card: 4123456789012345") == "Card: VISA-MASKED-2345"

    # 2. MASTERCARD Test (Destroy 12 digits, keep last 4)
    assert pii_module.mask_pii("Card: 5123456789012345") == "Card: MC-MASKED-2345"

    # 3. SSN Test (Destroy first 5 digits, keep last 4)
    assert pii_module.mask_pii("ID: 123-45-6789") == "ID: XXX-XX-6789"

    # 4. AWS KEY Test (Keep prefix and last 4, destroy the 12-char middle)
    assert pii_module.mask_pii("Key: AKIAIOSFODNN7EXAMPLE") == "Key: AKIA-XXXX-MPLE"

    # 5. The Combo Test (Multiple leaks in a single log line)
    combo_log = "User AKIAIOSFODNN7EXAMPLE charged 4123456789012345"
    assert (
        pii_module.mask_pii(combo_log) == "User AKIA-XXXX-MPLE charged VISA-MASKED-2345"
    )


# ==============================================================================
# TEST 2: The E2E Stream Filter (File I/O and Isolation)
# ==============================================================================
def test_pii_leak_hunter_e2e(tmp_path):
    """
    End-to-End test simulating a live log stream.
    Proves that clean lines are dropped, PII lines are safely written,
    and no raw sensitive data ever touches the output evidence log.
    """
    # 1. Setup the physical mock log file
    log_dir = tmp_path / "logs"
    log_dir.mkdir()
    target_log = log_dir / "production_dump.log"

    # Inject a mix of clean lines and highly sensitive data
    target_log.write_text(
        "2026-05-11T09:00 [INFO] System boot sequence normal\n"
        "2026-05-11T10:00 [DEBUG] Transaction 4111111111111111 processed\n"
        "2026-05-11T11:00 [ERROR] Failed AWS auth with AKIAIOSFODNN7EXAMPLE\n"
        "2026-05-11T12:00 [WARN] Input SSN 999-99-9999 failed validation\n",
        encoding="utf-8",
    )

    # 2. Execute the CLI tool
    test_args = ["pii_leak_hunter.py", str(target_log)]
    with patch.object(sys, "argv", test_args):
        pii_module.main()

    # 3. Verify the Evidence Log
    evidence_file = log_dir / "production_dump_pii_leak_evidence.log"
    assert (
        evidence_file.exists()
    ), "The hunter failed to generate the safe evidence log!"

    content = evidence_file.read_text(encoding="utf-8")

    # A) Ensure the clean lines were ignored (Saving disk space/CPU)
    assert "System boot sequence normal" not in content

    # B) Ensure the masked data made it to the file
    assert "VISA-MASKED-1111" in content
    assert "AKIA-XXXX-MPLE" in content
    assert "XXX-XX-9999" in content

    # C) ZERO-TRUST GUARANTEE: Ensure the raw PII was completely obliterated
    assert (
        "4111111111111111" not in content
    ), "CRITICAL LEAK: Raw VISA card written to disk!"
    assert (
        "AKIAIOSFODNN7EXAMPLE" not in content
    ), "CRITICAL LEAK: Raw AWS Key written to disk!"
    assert "999-99-9999" not in content, "CRITICAL LEAK: Raw SSN written to disk!"
