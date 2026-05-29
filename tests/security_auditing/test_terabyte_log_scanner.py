import pytest
import sys
import json
from unittest.mock import patch

# IMPORTANT: Adjust this path to match exactly where your file is located
import gitgalaxy.tools.terabyte_log_scanning.terabyte_log_scanner as scanner_module


# ==============================================================================
# TEST 1: The IR State Handshake & Binary Extraction
# ==============================================================================
def test_scanner_json_handshake_and_extraction(tmp_path):
    """
    Proves that the engine correctly parses the IR state JSON, extracts the targets,
    scans a binary log stream, and safely extracts only the matching lines to disk.
    """
    # 1. Setup the physical mock workspace
    work_dir = tmp_path / "scanner_workspace"
    work_dir.mkdir()

    # A) The Mock IR State (GitGalaxy Standard Schema)
    ir_state = {"analysis": {"known_programs": ["PGM_ALPHA", "PGM_BETA"]}}
    state_file = work_dir / "ir_state.json"
    state_file.write_text(json.dumps(ir_state), encoding="utf-8")

    # B) The Mock Terabyte Log (Mix of noise and target hits)
    target_log = work_dir / "mainframe_dump.log"
    target_log.write_text(
        "2026-05-11 09:15 [INFO] System boot sequence initialized\n"
        "2026-05-11 09:20 [EXEC] PGM_ALPHA executed successfully\n"
        "2026-05-11 09:25 [WARN] Unrelated process memory spike\n"
        "2026-05-11 10:00 [EXEC] PGM_BETA encountered warning 04\n"
        "2026-05-11 10:05 [EXEC] PGM_ALPHA restarted\n",
        encoding="utf-8",
    )

    # 2. Execute the Engine
    test_args = [
        "terabyte_log_scanner.py",
        str(target_log),
        "--input_state",
        str(state_file),
    ]

    with patch.object(sys, "argv", test_args):
        # We don't trap SystemExit here because a successful run should exit normally (no sys.exit call)
        scanner_module.main()

    # 3. The Invariant Assertions
    # A) Verify the filtered results log
    results_file = work_dir / "mainframe_dump_results.txt"
    assert results_file.exists(), "Scanner failed to create the results output file!"

    results_content = results_file.read_text(encoding="utf-8")

    assert "PGM_ALPHA executed successfully" in results_content
    assert "PGM_BETA encountered warning 04" in results_content
    assert (
        "System boot sequence initialized" not in results_content
    ), "Noise slipped through the binary filter!"

    # B) Verify the Telemetry Sidecar
    sidecar_file = work_dir / "dynamic_telemetry.json"
    assert sidecar_file.exists(), "Scanner failed to generate the JSON sidecar!"

    telemetry = json.loads(sidecar_file.read_text(encoding="utf-8"))
    counts = telemetry.get("execution_counts", {})

    # PGM_ALPHA appeared twice, PGM_BETA appeared once
    assert (
        counts.get("PGM_ALPHA") == 2
    ), "Mathematical aggregation failed for PGM_ALPHA!"
    assert counts.get("PGM_BETA") == 1, "Mathematical aggregation failed for PGM_BETA!"


# ==============================================================================
# TEST 2: The Schema Guard (Invalid JSON Rejection)
# ==============================================================================
def test_scanner_invalid_json_schema(tmp_path):
    """
    Proves that if a malformed or incorrect JSON schema is provided, the
    scanner aggressively aborts to prevent silent failures down the pipeline.
    """
    work_dir = tmp_path / "schema_repo"
    work_dir.mkdir()

    # Create a JSON file missing the required 'analysis' -> 'known_programs' path
    bad_state_file = work_dir / "bad_state.json"
    bad_state_file.write_text(json.dumps({"wrong_root": []}), encoding="utf-8")

    dummy_log = work_dir / "dummy.log"
    dummy_log.write_text("empty", encoding="utf-8")

    test_args = [
        "terabyte_log_scanner.py",
        str(dummy_log),
        "--input_state",
        str(bad_state_file),
    ]

    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as exc:
            scanner_module.main()

        # The engine must throw a fatal error (exit code 1) on schema mismatch
        assert exc.value.code == 1, "Scanner failed to block an invalid JSON schema!"


# ==============================================================================
# TEST 3: The Manual CLI Override (-k Flag)
# ==============================================================================
def test_scanner_manual_keyword_override(tmp_path):
    """
    Proves that the scanner can bypass the JSON input state and process
    raw CLI keyword arguments correctly.
    """
    work_dir = tmp_path / "cli_repo"
    work_dir.mkdir()

    target_log = work_dir / "app.log"
    target_log.write_text(
        "Line 1: ERROR 500\n" "Line 2: SUCCESS 200\n" "Line 3: ERROR 404\n",
        encoding="utf-8",
    )

    # Use -k ERROR to hunt for errors
    test_args = ["terabyte_log_scanner.py", str(target_log), "-k", "ERROR"]

    with patch.object(sys, "argv", test_args):
        scanner_module.main()

    results_file = work_dir / "app_results.txt"
    content = results_file.read_text(encoding="utf-8")

    assert "ERROR 500" in content
    assert "ERROR 404" in content
    assert "SUCCESS 200" not in content, "Manual keyword override failed to filter!"
