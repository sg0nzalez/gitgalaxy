import json
import logging
from pathlib import Path
import pytest

# Adjust this import based on your actual project structure
from gitgalaxy.security.manifest_parser import ManifestParser


@pytest.fixture
def parser():
    """Provides a fresh ManifestParser instance with a silenced logger for clean test output."""
    logger = logging.getLogger("test_manifest_parser")
    logger.addHandler(logging.NullHandler())
    return ManifestParser(parent_logger=logger)


# ==============================================================================
# 1. package.json Tests (Aliasing & Local Spoofing)
# ==============================================================================
def test_package_json_npm_aliasing(parser, tmp_path):
    """Verifies that npm: aliases and scoped aliases are correctly dereferenced."""
    pkg_file = tmp_path / "package.json"
    pkg_file.write_text(
        json.dumps(
            {
                "dependencies": {
                    "lodash": "npm:malicious-lodash@1.0.0",
                    "express": "npm:@hacker-scope/express-shadow@2.1.1",
                    "react": "^18.0.0",  # Standard package, should be ignored
                }
            }
        )
    )

    result = parser.build_translation_map([str(pkg_file)])

    assert "lodash" in result
    assert result["lodash"] == "malicious-lodash"

    assert "express" in result
    assert result["express"] == "@hacker-scope/express-shadow"

    # Standard packages shouldn't be added to the translation map by package.json
    assert "react" not in result


def test_package_json_git_and_file_spoofing(parser, tmp_path):
    """Verifies that direct file system or git repository overrides are flagged."""
    pkg_file = tmp_path / "package.json"
    pkg_file.write_text(
        json.dumps(
            {
                "devDependencies": {
                    "jest": "github:evil/jest",
                    "mocha": "file:./local-malware.js",
                    "eslint": "git+https://evil.com/eslint.git",
                }
            }
        )
    )

    result = parser.build_translation_map([str(pkg_file)])

    assert result["jest"] == "github:evil/jest"
    assert result["mocha"] == "file:./local-malware.js"
    assert result["eslint"] == "git+https://evil.com/eslint.git"


def test_package_json_invalid_json(parser, tmp_path):
    """Ensures the parser degrades gracefully without crashing if the manifest is corrupted."""
    pkg_file = tmp_path / "package.json"
    pkg_file.write_text("{ THIS IS INVALID JSON ]")

    # Should not throw an exception, just return an empty map
    result = parser.build_translation_map([str(pkg_file)])
    assert result == {}


# ==============================================================================
# 2. package-lock.json Tests (Namespace Hijacking)
# ==============================================================================
def test_package_lock_namespace_hijacking(parser, tmp_path):
    """Verifies that external, non-NPM registry resolutions are intercepted."""
    lock_file = tmp_path / "package-lock.json"

    lock_file.write_text(
        json.dumps(
            {
                "packages": {
                    "node_modules/clean-pkg": {
                        # Note: Testing against the exact string present in your parser logic
                        "resolved": "[https://registry.npmjs.org/](https://registry.npmjs.org/)/clean-pkg.tgz"
                    },
                    "node_modules/dirty-pkg": {
                        "resolved": "[https://evil-registry.com/dirty-pkg.tgz](https://evil-registry.com/dirty-pkg.tgz)"
                    },
                }
            }
        )
    )

    result = parser.build_translation_map([str(lock_file)])

    # Standard registries should be ignored
    assert "clean-pkg" not in result

    # Suspicious registries should be mapped so the firewall can block them
    assert "dirty-pkg" in result
    assert result["dirty-pkg"] == "[https://evil-registry.com/dirty-pkg.tgz](https://evil-registry.com/dirty-pkg.tgz)"


# ==============================================================================
# 3. requirements.txt Tests (Injections)
# ==============================================================================
def test_requirements_txt_parsing(parser, tmp_path):
    """Verifies standard python packages and hostile URL injections are captured."""
    req_file = tmp_path / "requirements.txt"
    req_file.write_text(
        "# This is a comment\n"
        "requests==2.25.1\n"
        "flask>=1.1.0\n"
        "git+[https://github.com/hacker/malware.git](https://github.com/hacker/malware.git)\n"
        "file:///etc/passwd\n"
    )

    result = parser.build_translation_map([str(req_file)])

    # Standard packages map to themselves
    assert result["requests"] == "requests"
    assert result["flask"] == "flask"

    # Injections map the full string to ensure the firewall catches the URL
    assert (
        result["git+[https://github.com/hacker/malware.git](https://github.com/hacker/malware.git)"]
        == "git+[https://github.com/hacker/malware.git](https://github.com/hacker/malware.git)"
    )
    assert result["file:///etc/passwd"] == "file:///etc/passwd"


# ==============================================================================
# 4. pip.conf Tests (Registry Spoofing)
# ==============================================================================
def test_pip_conf_insecure_registry(parser, tmp_path):
    """Verifies that HTTP or ngrok tunnel registries are instantly flagged."""
    pip_file = tmp_path / "pip.conf"
    pip_file.write_text(
        "[global]\n"
        "index-url = [http://pypi.org/simple](http://pypi.org/simple)\n"  # Insecure HTTP
        "extra-index-url = [https://hacker-tunnel.ngrok.io](https://hacker-tunnel.ngrok.io)\n"  # ngrok tunneling
        "trusted-host = pypi.org\n"
    )

    result = parser.build_translation_map([str(pip_file)])

    # The parser uses a hardcoded key for insecure registries.
    # It will store the last matched insecure URL in the file.
    assert "INSECURE_REGISTRY_pip.conf" in result
    assert "ngrok" in result["INSECURE_REGISTRY_pip.conf"]


# ==============================================================================
# 5. Global Monorepo Tests (Multiple Files)
# ==============================================================================
def test_multiple_manifests_simultaneously(parser, tmp_path):
    """Verifies the parser can handle a monorepo setup with multiple formats at once."""
    pkg_file = tmp_path / "package.json"
    req_file = tmp_path / "requirements.txt"

    pkg_file.write_text(json.dumps({"dependencies": {"lodash": "npm:evil-lodash"}}))
    req_file.write_text("numpy==1.20.0")

    result = parser.build_translation_map([str(pkg_file), str(req_file)])

    assert len(result) == 2
    assert result["lodash"] == "evil-lodash"
    assert result["numpy"] == "numpy"
