import subprocess
import json
from pathlib import Path


def test_galaxyscope_python_fixture(tmp_path):
    """
    Tests that GalaxyScope can parse a micro-repo (iwubi),
    complete its mission, and trigger all 4 recorders successfully.
    """
    # 1. Dynamically get the absolute path to the GitGalaxy root
    test_dir = Path(__file__).parent
    project_root = test_dir.parent.parent  # <--- Added second .parent

    # 2. Build absolute paths for the script and the fixture
    script_path = project_root / "gitgalaxy" / "galaxyscope.py"
    fixture_path = (
        test_dir.parent / "fixtures" / "iwubi_frankenstein_test"
    )  # <--- Added .parent

    # Force output to a temporary directory
    output_dir = tmp_path / "test_run"

    # 3. Pass the absolute paths to the subprocess
    result = subprocess.run(
        ["python", str(script_path), str(fixture_path), "--output", str(output_dir)],
        capture_output=True,
        text=True,
    )

    # INVARIANT 1: CLI Exit Code & Billboard Output
    assert result.returncode == 0, f"GalaxyScope crashed! Stderr: {result.stderr}"
    assert (
        "MISSION_SUCCESS" in result.stdout
    ), "CLI did not print the success billboard."

    # The engine uses the target folder name to build the filenames automatically
    target_name = "iwubi_frankenstein_test"

    gpu_file = output_dir / f"{target_name}_galaxy_gpu.json"
    audit_file = output_dir / f"{target_name}_galaxy_audit.json"
    llm_file = output_dir / f"{target_name}_galaxy_llm.md"
    db_file = output_dir / f"{target_name}_galaxy_master.db"

    # INVARIANT 2: File Generation (Did all 4 recorders fire?)
    assert gpu_file.exists(), f"GPU Recorder failed to output JSON at {gpu_file}"
    assert audit_file.exists(), f"Audit Recorder failed to output JSON at {audit_file}"
    assert llm_file.exists(), f"LLM Recorder failed to output Markdown at {llm_file}"
    assert db_file.exists(), f"SQLite Recorder failed to output DB at {db_file}"

    # INVARIANT 3: GPU Recorder Internals (Non-blank structural check)
    with open(gpu_file, "r", encoding="utf-8") as f:
        gpu_data = json.load(f)
        assert "meta" in gpu_data, "GPU JSON missing 'meta' object"
        assert "galaxy" in gpu_data, "GPU JSON missing 'galaxy' object"
        assert len(gpu_data["galaxy"]["names"]) >= 1, "GPU Recorder found 0 files"
        assert "iwubi.py" in gpu_data["galaxy"]["names"], "Failed to identify iwubi.py"

    # INVARIANT 4: LLM Recorder Internals (Text check)
    with open(llm_file, "r", encoding="utf-8") as f:
        md_content = f.read()
        assert "# ARCHITECTURAL_BRIEF" in md_content, "LLM Markdown missing main header"
        assert "MACRO STATE" in md_content, "LLM Markdown missing MACRO STATE section"

    # INVARIANT 5: SQLite Database (Byte check)
    assert db_file.stat().st_size > 1000, "SQLite database appears to be empty"
