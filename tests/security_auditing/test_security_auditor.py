import pytest
import numpy as np
from unittest.mock import patch

# We patch the schemas before importing so the Auditor doesn't fail on boot
MOCK_SCHEMAS = {"SIGNAL_SCHEMA": ["danger", "io", "flux", "safety", "graveyard"]}

with patch("gitgalaxy.security.security_auditor.RECORDING_SCHEMAS", MOCK_SCHEMAS):
    from gitgalaxy.security.security_auditor import SecurityAuditor


@pytest.fixture
def mock_stars():
    """Provides a baseline payload with a circular dependency to test the graph resolver."""
    return [
        {
            "path": "src/main.py",
            "name": "main.py",
            "raw_imports": ["src/utils.py"],
            "telemetry": {"popularity": 5, "control_flow_ratio": 0.5},
            "hit_vector": [5, 2, 0, 0, 0],  # High danger, some IO
            "file_impact": 0.8,
            "structural_mass": 0.9,  # High mass for shadow patch testing
            "coding_loc": 100,
        },
        {
            "path": "src/utils.py",
            "name": "utils.py",
            "raw_imports": ["src/main.py"],  # Circular loop!
            "telemetry": {"popularity": 1},
            "hit_vector": [0, 0, 0, 0, 0],
            "file_impact": 0.2,
            "coding_loc": 20,
        },
    ]


# ==============================================================================
# TEST 1: DEPENDENCY GRAPH RESOLUTION (NetworkX vs Pure Python Deque)
# ==============================================================================
def test_dependency_graph_pure_python(mock_stars):
    """Proves the pure-Python O(1) Deque resolver survives circular dependencies."""
    auditor = SecurityAuditor()

    with patch("gitgalaxy.security.security_auditor.HAS_NETWORKX", False):
        resolved_stars = auditor._resolve_dependency_graph(mock_stars)

    main_star = next(s for s in resolved_stars if s["name"] == "main.py")
    assert "dependency_network" in main_star
    # The deque BFS considers the node itself as a visited descendant/ancestor in a circular loop
    assert main_star["dependency_network"]["total_upstream"] == 2
    assert main_star["dependency_network"]["total_downstream"] == 2


def test_dependency_graph_networkx(mock_stars):
    """Proves the C-optimized NetworkX resolver handles the exact same circular loop."""
    auditor = SecurityAuditor()

    with patch("gitgalaxy.security.security_auditor.HAS_NETWORKX", True):
        resolved_stars = auditor._resolve_dependency_graph(mock_stars)

    main_star = next(s for s in resolved_stars if s["name"] == "main.py")
    assert main_star["dependency_network"]["total_upstream"] == 1


# ==============================================================================
# TEST 2: PANDAS FEATURE MATRIX CONSTRUCTION
# ==============================================================================
def test_construct_feature_matrix(mock_stars):
    """Proves the matrix builder accurately maps star metrics to a Pandas DataFrame."""
    auditor = SecurityAuditor()

    # Explicitly inject the schema into the instance so the dictionary mapping works
    auditor.SIGNAL_SCHEMA = ["danger", "io", "flux", "safety", "graveyard"]
    auditor._resolve_dependency_graph(mock_stars)  # Pre-load graph data

    df = auditor._construct_feature_matrix(mock_stars)

    assert not df.empty
    assert len(df) == 2
    # Ensure the log_density math didn't crash
    assert "log_density_hit_danger" in df.columns
    assert "log_logic_loc" in df.columns


def test_construct_feature_matrix_exception_fallback():
    """Proves a corrupted star payload generates a safe, empty fallback row."""
    auditor = SecurityAuditor()
    corrupted_stars = [{"path": "broken.py", "telemetry": "THIS_SHOULD_BE_A_DICT"}]

    df = auditor._construct_feature_matrix(corrupted_stars)
    assert not df.empty

    # Pandas get_dummies converts 'language' into 'language_unknown'
    assert "language_unknown" in df.columns
    assert df.iloc[0]["language_unknown"] in [True, 1]
    assert df.iloc[0]["structural_mass"] == 0.0


# ==============================================================================
# TEST 3: XGBOOST MULTICLASS INFERENCE & SHADOW PATCHES
# ==============================================================================
@patch("gitgalaxy.security.security_auditor.xgb.XGBClassifier")
def test_audit_galaxy_ml_inference(mock_xgb_class, mock_stars):
    """
    Proves the orchestrator successfully formats data, predicts Multiclass threats,
    and injects the Shadow Patch override when a heavy file mutates silently.
    """
    # 1. Setup the Mock Model
    mock_model = mock_xgb_class.return_value
    mock_model.feature_names_in_ = ["log_logic_loc", "log_density_hit_danger"]

    # Predict probabilities for 2 files across 5 classes (0=Safe, 1=Botnet, 2=Trojan, etc)
    # File 1: 99% confident it's a Botnet (Class 1)
    # File 2: 99% confident it's Safe Code (Class 0)
    mock_model.predict_proba.return_value = np.array(
        [[0.01, 0.99, 0.0, 0.0, 0.0], [0.99, 0.01, 0.0, 0.0, 0.0]]
    )

    auditor = SecurityAuditor()
    auditor.model = mock_model  # Inject the mock model
    auditor.feature_names = mock_model.feature_names_in_

    # 2. Run the Audit WITH Shadow Patch enabled
    audited_stars = auditor.audit_galaxy(mock_stars, is_shadow_patch=True)

    main_star = audited_stars[0]
    utils_star = audited_stars[1]

    # 3. Assert Shadow Patch Override (main.py has structural_mass > 0.5)
    # Even though the model predicted Class 1 (Botnet), the Shadow Patch forces it to Class 2 (Trojan/Stealer)
    assert main_star["is_ml_threat"] is True
    assert (
        main_star["telemetry"]["domain_context"]["AI Threat Class"]
        == "Stealer / Trojan"
    )
    assert (
        "SHADOW PATCH: Hash mutated"
        in main_star["telemetry"]["domain_context"]["alert"]
    )

    # 4. Assert Safe File (utils.py)
    assert utils_star["is_ml_threat"] is False


# ==============================================================================
# TEST 4: FATAL DESYNC & EXCEPTION CATCHING
# ==============================================================================
@patch("gitgalaxy.security.security_auditor.xgb.XGBClassifier")
def test_audit_galaxy_fatal_desync(mock_xgb_class, mock_stars):
    """Proves the engine aborts cleanly if XGBoost returns the wrong number of rows."""
    mock_model = mock_xgb_class.return_value
    mock_model.feature_names_in_ = ["log_logic_loc"]

    # Return 1 prediction for 2 files (Fatal Desync)
    mock_model.predict_proba.return_value = np.array([[0.99, 0.01, 0.0, 0.0, 0.0]])

    auditor = SecurityAuditor()
    auditor.model = mock_model
    auditor.feature_names = mock_model.feature_names_in_

    # It should log the error and return the stars unmodified without crashing
    audited_stars = auditor.audit_galaxy(mock_stars)
    assert "is_ml_threat" not in audited_stars[0]


def test_audit_galaxy_no_model(mock_stars):
    """Proves the engine gracefully skips ML if the model file is missing."""
    auditor = SecurityAuditor(model_path="does_not_exist.json")

    # Should resolve graphs but skip ML
    audited_stars = auditor.audit_galaxy(mock_stars)
    assert "dependency_network" in audited_stars[0]
    assert "is_ml_threat" not in audited_stars[0]
