import os
import sys
import json
import yaml
import pytest
from pathlib import Path
from unittest.mock import patch

from gitgalaxy.tools.network_auditing.full_api_network_map import (
    run_api_audit,
    main,
    auto_discover_swagger,
    parse_official_swagger,
    map_physical_codebase,
)


# ==============================================================================
# TEST 1: The Core Framework Regex Traps (All Languages)
# ==============================================================================
def test_all_framework_regex_traps(tmp_path):
    """Proves the physical mapper correctly extracts endpoints from all supported backends."""
    repo_dir = tmp_path / "all_frameworks_repo"
    repo_dir.mkdir()

    # Create dummy files for every supported framework
    (repo_dir / "app.py").write_text('@app.get("/api/py")', encoding="utf-8")
    (repo_dir / "server.js").write_text('router.post("/api/js")', encoding="utf-8")
    (repo_dir / "Controller.java").write_text('@DeleteMapping("/api/java")', encoding="utf-8")
    (repo_dir / "main.go").write_text('.PUT("/api/go")', encoding="utf-8")
    (repo_dir / "Api.cs").write_text('[HttpPatch("/api/cs")]', encoding="utf-8")
    (repo_dir / "MinApi.cs").write_text('.MapGet("/api/csmin")', encoding="utf-8")
    (repo_dir / "routes.php").write_text('Route::delete("/api/php")', encoding="utf-8")
    (repo_dir / "main.rs").write_text('#[post("/api/rs")]', encoding="utf-8")
    (repo_dir / "routes.rb").write_text('get "/api/rb"', encoding="utf-8")

    physical_apis, frameworks = map_physical_codebase(repo_dir)

    # Verify all frameworks were successfully detected
    assert len(frameworks) == 9, "Not all frameworks were detected by the regex traps!"
    endpoints = set(physical_apis.keys())
    assert "GET /api/py" in endpoints
    assert "POST /api/js" in endpoints
    assert "DELETE /api/java" in endpoints
    assert "PUT /api/go" in endpoints
    assert "PATCH /api/cs" in endpoints
    assert "GET /api/csmin" in endpoints
    assert "DELETE /api/php" in endpoints
    assert "POST /api/rs" in endpoints
    assert "GET /api/rb" in endpoints


# ==============================================================================
# TEST 2: Swagger Parser (JSON, YAML, and Exceptions)
# ==============================================================================
def test_swagger_parser_yaml_and_errors(tmp_path, capsys):
    """Proves the parser handles YAML specs and correctly raises SystemExit on corruption."""
    # 1. Valid YAML
    yaml_file = tmp_path / "openapi.yaml"
    yaml_data = {"paths": {"/api/yaml": {"get": {}}}}
    yaml_file.write_text(yaml.dump(yaml_data), encoding="utf-8")

    routes = parse_official_swagger(yaml_file)
    assert "GET /api/yaml" in routes

    # 2. Corrupted File Exception Trap
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("{ CORRUPTED JSON", encoding="utf-8")

    with pytest.raises(SystemExit) as exc_info:
        parse_official_swagger(bad_file)

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "Error reading Swagger file" in captured.out


# ==============================================================================
# TEST 3: Auto-Discovery Engine (Fast Path vs Deep Grep)
# ==============================================================================
def test_auto_discover_swagger_logic(tmp_path):
    """Proves the engine finds exact filenames OR deep-greps for Swagger signatures."""
    # 1. Fast Path (Exact name match)
    (tmp_path / "swagger.json").write_text("{}", encoding="utf-8")

    # 2. Deep Grep (Weird name, but contains OpenAPI signature)
    (tmp_path / "hidden_spec.yml").write_text('openapi: "3.0.0"\npaths: {}', encoding="utf-8")

    # 3. Decoy (Valid extension, no signature)
    (tmp_path / "package.json").write_text('{"name": "app"}', encoding="utf-8")

    candidates = auto_discover_swagger(tmp_path)
    names = [c.name for c in candidates]

    assert "swagger.json" in names
    assert "hidden_spec.yml" in names
    assert "package.json" not in names


# ==============================================================================
# TEST 4: Physical Codebase I/O Exception Trap
# ==============================================================================
def test_physical_mapper_exception_trap(tmp_path):
    """Proves the physical mapper skips unreadable files without crashing."""
    (tmp_path / "app.py").write_text('@app.get("/api/test")', encoding="utf-8")

    # Mock Path.read_text to raise an exception
    with patch("pathlib.Path.read_text", side_effect=PermissionError("Locked file!")):
        apis, frameworks = map_physical_codebase(tmp_path)

    assert len(apis) == 0, "The engine failed to swallow the I/O exception!"


# ==============================================================================
# TEST 5: CLI Main - Missing Target Error
# ==============================================================================
def test_main_missing_target(capsys):
    """Proves the CLI aborts if the target directory doesn't exist."""
    with patch("sys.argv", ["api_map", "missing_repo_12345"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 1
    assert "Error: Target source directory" in capsys.readouterr().out


# ==============================================================================
# TEST 6: CLI Main - No Swagger Found Error
# ==============================================================================
def test_main_no_swagger_found(tmp_path, capsys):
    """Proves the CLI aborts if auto-discovery finds zero Swagger files."""
    repo_dir = tmp_path / "empty_repo"
    repo_dir.mkdir()

    with patch("sys.argv", ["api_map", str(repo_dir)]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 1
    assert "[ABORT] No OpenAPI/Swagger specifications found" in capsys.readouterr().out


# ==============================================================================
# TEST 7: CLI Main - Ambiguous Swaggers Error (No Merge Flag)
# ==============================================================================
def test_main_ambiguous_swaggers(tmp_path, capsys):
    """Proves the CLI halts and requires intervention if multiple primary Swaggers exist."""
    repo_dir = tmp_path / "multi_repo"
    repo_dir.mkdir()

    (repo_dir / "api_v1").mkdir()
    (repo_dir / "api_v2").mkdir()

    (repo_dir / "api_v1" / "swagger.json").write_text('{"paths":{}}', encoding="utf-8")
    (repo_dir / "api_v2" / "swagger.json").write_text('{"paths":{}}', encoding="utf-8")

    with patch("sys.argv", ["api_map", str(repo_dir)]):
        with pytest.raises(SystemExit) as exc_info:
            main()

    assert exc_info.value.code == 1
    captured = capsys.readouterr()
    assert "[AMBIGUITY] Multiple OpenAPI/Swagger specifications found" in captured.out
    assert "OR use the --merge-all flag" in captured.out


# ==============================================================================
# TEST 8: CLI Main - Ambiguous Swaggers WITH --merge-all
# ==============================================================================
def test_main_ambiguous_merge_all(tmp_path, capsys):
    """Proves the --merge-all flag unifies multiple Swaggers into one state."""
    repo_dir = tmp_path / "multi_repo_merge"
    repo_dir.mkdir()

    # We must inject the "openapi" signature so the Deep Grep engine recognizes them!
    (repo_dir / "swagger1.json").write_text('{"openapi": "3.0.0", "paths":{"/api/one":{"get":{}}}}', encoding="utf-8")
    (repo_dir / "swagger2.json").write_text('{"openapi": "3.0.0", "paths":{"/api/two":{"post":{}}}}', encoding="utf-8")

    # Add a physical file so the dashboard prints cleanly
    (repo_dir / "app.py").write_text('@app.get("/api/one")\n@app.post("/api/two")', encoding="utf-8")

    with patch("sys.argv", ["api_map", str(repo_dir), "--merge-all"]):
        main()  # Should NOT raise SystemExit

    captured = capsys.readouterr()
    assert "--merge-all active. Unioning 2 discovered specifications" in captured.out
    assert "Documented Endpoints (Swagger) : 2" in captured.out
    assert "No Shadow APIs detected" in captured.out


# ==============================================================================
# TEST 9: CLI Main - Explicit --swagger Flag (Valid and Invalid)
# ==============================================================================
def test_main_explicit_swagger_flag(tmp_path, capsys):
    """Proves the --swagger flag bypasses discovery, and traps invalid paths."""
    repo_dir = tmp_path / "explicit_repo"
    repo_dir.mkdir()

    spec_path = repo_dir / "custom_spec.json"
    spec_path.write_text('{"paths":{"/api/explicit":{"get":{}}}}', encoding="utf-8")

    # Invalid Path
    with patch(
        "sys.argv",
        ["api_map", str(repo_dir), "--swagger", str(repo_dir / "missing.json")],
    ):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert "Error: Provided Swagger file" in capsys.readouterr().out

    # Valid Path
    with patch("sys.argv", ["api_map", str(repo_dir), "--swagger", str(spec_path)]):
        main()

    assert "Documented Endpoints (Swagger) : 1" in capsys.readouterr().out


# ==============================================================================
# TEST 10: CLI Main - Presentation Dashboard (Shadow and Ghost APIs)
# ==============================================================================
def test_main_presentation_dashboard(tmp_path, capsys):
    """Proves the CLI successfully prints the full Shadow/Ghost API dashboard."""
    repo_dir = tmp_path / "dashboard_repo"
    repo_dir.mkdir()

    # 1. Official Swagger (Has a Ghost)
    (repo_dir / "swagger.json").write_text(
        '{"paths":{"/api/ghost":{"get":{}}, "/api/shared":{"post":{}}}}',
        encoding="utf-8",
    )

    # 2. Source Code (Has a Shadow and the Shared endpoint)
    (repo_dir / "app.py").write_text('@app.post("/api/shared")\n@app.delete("/api/shadow")', encoding="utf-8")

    with patch("sys.argv", ["api_map", str(repo_dir)]):
        main()

    captured = capsys.readouterr().out
    assert "SHADOW API SECURITY AUDIT" in captured
    assert "SHADOW APIS DETECTED: 1" in captured
    assert "DELETE /api/shadow" in captured
    assert "GHOST APIS DETECTED: 1" in captured
    assert "GET /api/ghost" in captured


# ==============================================================================
# TEST 11: Programmatic Edge Cases (run_api_audit)
# ==============================================================================
def test_run_api_audit_edge_cases(tmp_path):
    """Proves the programmatic entry point safely returns edge case dictionaries."""
    # 1. No Swagger
    repo_dir = tmp_path / "prog_repo"
    repo_dir.mkdir()
    res1 = run_api_audit(repo_dir)
    assert res1["status"] == "no_swagger"

    # 2. Ambiguous Swaggers
    (repo_dir / "api_v1").mkdir()
    (repo_dir / "api_v2").mkdir()
    (repo_dir / "api_v1" / "swagger.json").write_text("{}", encoding="utf-8")
    (repo_dir / "api_v2" / "swagger.json").write_text("{}", encoding="utf-8")

    res2 = run_api_audit(repo_dir)
    assert res2["status"] == "ambiguous"


# ==============================================================================
# TEST 12: Programmatic Success (Test Auto-Bypass)
# ==============================================================================
def test_run_api_audit_success(tmp_path):
    """Proves the programmatic entry point succeeds and bypasses test schemas."""
    repo_dir = tmp_path / "prog_success"
    repo_dir.mkdir()

    # Primary Spec
    (repo_dir / "openapi.json").write_text('{"paths":{"/api/real":{"get":{}}}}', encoding="utf-8")

    # Test Spec (Should be ignored automatically)
    # The programmatic entry point strictly looks for "test", not "tests"
    test_dir = repo_dir / "test"
    test_dir.mkdir()
    (test_dir / "swagger.json").write_text('{"paths":{"/api/test":{"get":{}}}}', encoding="utf-8")

    # Source Code
    (repo_dir / "app.py").write_text('@app.get("/api/real")\n@app.post("/api/shadow")', encoding="utf-8")

    result = run_api_audit(repo_dir)
    assert result["status"] == "success"
    assert result["shadow_count"] == 1
    assert "POST /api/shadow" in result["shadow_apis"]
    assert result["ghost_count"] == 0
