import json

# Updated import path to match the network_auditing folder
from gitgalaxy.tools.network_auditing.full_api_network_map import run_api_audit

def test_shadow_and_ghost_api_detection(tmp_path):
    """
    End-to-End test for the API Network Map.
    Verifies the multi-language regex traps, Swagger auto-discovery (and test exclusion),
    and the strict Shadow/Ghost API set-difference math.
    """
    # 1. Construct the Mock Repository Space
    repo_dir = tmp_path / "mock_api_repo"
    repo_dir.mkdir()

    # ==========================================================================
    # A. Mock Source Code (The Physical Endpoints)
    # ==========================================================================
    # Python FastAPI
    (repo_dir / "main.py").write_text('@app.get("/api/health")', encoding="utf-8")
    
    # Node Express
    (repo_dir / "server.js").write_text('router.post("/api/users")', encoding="utf-8")
    
    # Java Spring Boot
    (repo_dir / "UserController.java").write_text('@DeleteMapping("/api/users/{id}")', encoding="utf-8")
    
    # Ruby Rails (THE SHADOW API - Intentionally omitted from Swagger docs)
    (repo_dir / "admin.rb").write_text('get "/api/secret_debug"', encoding="utf-8")

    # ==========================================================================
    # B. Mock Official Documentation (The Approved Endpoints)
    # ==========================================================================
    official_swagger = {
        "openapi": "3.0.0",
        "paths": {
            "/api/health": {"get": {}},
            "/api/users": {"post": {}},
            "/api/users/{id}": {"delete": {}},
            "/api/legacy_v1_sync": {"put": {}} # THE GHOST API (In docs, but deleted from code)
        }
    }
    (repo_dir / "openapi.json").write_text(json.dumps(official_swagger), encoding="utf-8")

    # ==========================================================================
    # C. Mock Test Swagger (Must be ignored by auto-discovery!)
    # ==========================================================================
    # We name this exactly "test" to trigger the programmatic filter inside run_api_audit
    test_dir = repo_dir / "test"
    test_dir.mkdir()
    test_swagger = {"openapi": "3.0.0", "paths": {"/test/mock": {"get": {}}}}
    (test_dir / "swagger.json").write_text(json.dumps(test_swagger), encoding="utf-8")

    # ==========================================================================
    # 2. Execute the Engine
    # ==========================================================================
    result = run_api_audit(repo_dir)

    # ==========================================================================
    # 3. The Invariant Assertions
    # ==========================================================================
    assert result["status"] == "success", f"Failed to audit: status was {result['status']}"

    # A) Prove the Multi-Language Regex Traps worked
    frameworks = result["frameworks"]
    assert "Python (FastAPI/Flask/Django)" in frameworks
    assert "Node.js (Express/Fastify/Koa)" in frameworks
    assert "Java (Spring Boot)" in frameworks
    assert "Ruby (Rails/Sinatra)" in frameworks

    # B) Prove Shadow API detection (Physical code without Documentation)
    assert result["shadow_count"] == 1
    assert "GET /api/secret_debug" in result["shadow_apis"], "Engine failed to flag the undocumented Ruby Shadow API!"

    # C) Prove Ghost API detection (Documentation without Physical code)
    assert result["ghost_count"] == 1

    # D) Prove Auto-Discovery segregation (It ignored the test directory)
    # If it read the test swagger, the ghost count would be 2 (because /test/mock isn't in the code).
    assert "GET /test/mock" not in result["shadow_apis"]