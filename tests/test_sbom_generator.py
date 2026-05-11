import pytest
import json
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# IMPORTANT: Adjust this import path depending on where sbom_generator.py lives
from gitgalaxy.tools.compliance.sbom_generator import UniversalManifestSlicer, main

# ==============================================================================
# TEST 1: The Multi-Ecosystem Slicer Guard
# ==============================================================================
def test_universal_manifest_slicer(tmp_path):
    """
    Proves that the regex and JSON parsing can perfectly extract dependencies
    across diverse language ecosystems without dropping packages.
    """
    slicer = UniversalManifestSlicer()
    
    # 1. Test NPM (JSON Parsing)
    pkg_json = tmp_path / "package.json"
    pkg_json.write_text('{"dependencies": {"express": "^4.17.1"}, "devDependencies": {"jest": "27.0.0"}}', encoding='utf-8')
    eco1, deps1 = slicer.slice_manifest(pkg_json)
    
    assert eco1 == "npm"
    assert deps1["express"] == "^4.17.1"
    assert deps1["jest"] == "27.0.0"

    # 2. Test PyPI (Text / Operator Regex)
    req_txt = tmp_path / "requirements.txt"
    req_txt.write_text("requests==2.26.0\n# comment ignored\nurllib3>=1.26.0", encoding='utf-8')
    eco2, deps2 = slicer.slice_manifest(req_txt)
    
    assert eco2 == "pypi"
    assert deps2["requests"] == "2.26.0"
    assert deps2["urllib3"] == "latest" # The slicer defaults to 'latest' for non '==' operators

    # 3. Test Rust / Cargo (Toml Block Regex)
    cargo_toml = tmp_path / "Cargo.toml"
    cargo_toml.write_text("[package]\nname=\"test\"\n\n[dependencies]\ntokio = \"1.0\"\nserde = \"1.0\"", encoding='utf-8')
    eco3, deps3 = slicer.slice_manifest(cargo_toml)
    
    assert eco3 == "cargo"
    assert deps3["tokio"] == "latest"
    assert deps3["serde"] == "latest"

# ==============================================================================
# TEST 2: The Zero-Trust CycloneDX Matrix
# ==============================================================================
@patch("gitgalaxy.tools.compliance.sbom_generator.SecurityLens")
@patch("gitgalaxy.tools.compliance.sbom_generator.LanguageDetector")
def test_zero_trust_sbom_generation(mock_detector_class, mock_security_class, tmp_path):
    """
    Proves that the physical audit matrix correctly translates missing packages 
    and spoofed files into strict CycloneDX JSON properties.
    """
    # 1. Setup Mock Workspace
    project_dir = tmp_path / "target_project"
    project_dir.mkdir()
    
    # Create a package.json with two dependencies
    pkg_json = project_dir / "package.json"
    pkg_json.write_text('{"dependencies": {"safe-lib": "1.0", "ghost-lib": "2.0"}}', encoding='utf-8')
    
    # Simulate "safe-lib" existing physically on disk, but "ghost-lib" is missing
    safe_lib_dir = project_dir / "node_modules" / "safe-lib"
    safe_lib_dir.mkdir(parents=True)
    (safe_lib_dir / "index.js").write_text("console.log('hello');", encoding='utf-8')

    # 2. Configure the Mocks to simulate a Spoof Detection
    mock_sec_instance = mock_security_class.return_value
    mock_det_instance = mock_detector_class.return_value
    
    # We will pretend the SecurityLens found high entropy malware in safe-lib!
    mock_sec_instance.scan_content.return_value = {"counts": {"entropy": 5.2}}
    mock_det_instance.inspect.return_value = {"anomaly_flags": ["Disguised Executable"]}

    # 3. Execute the Generator
    test_args = ["sbom_generator.py", str(project_dir), "--out", "test_bom.json"]
    with patch.object(sys, 'argv', test_args):
        main()
        
    # 4. Verify the CycloneDX Output
    bom_file = tmp_path / "target_project_test_bom.json"
    assert bom_file.exists(), "SBOM generator failed to create the output JSON."
    
    bom_data = json.loads(bom_file.read_text(encoding='utf-8'))
    
    assert bom_data["bomFormat"] == "CycloneDX"
    assert len(bom_data["components"]) == 2
    
    # Extract components by name for easy assertion
    components = {c["name"]: c for c in bom_data["components"]}
    
    # Assert Ghost-Lib (Missing on Disk)
    ghost_props = {p["name"]: p["value"] for p in components["ghost-lib"]["properties"]}
    assert ghost_props["gitgalaxy:trust_status"] == "UNVERIFIED_MISSING_ON_DISK"
    
    # Assert Safe-Lib (Malware Spoof Detected)
    safe_props = {p["name"]: p["value"] for p in components["safe-lib"]["properties"]}
    assert safe_props["gitgalaxy:trust_status"] == "SPOOF_DETECTED"
    assert "High Entropy" in safe_props["gitgalaxy:anomaly_notes"]