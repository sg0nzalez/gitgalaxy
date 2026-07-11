# GitGalaxy: CI/CD Distribution & Architecture Context

## 1. Architectural Overview (The Hub and Spoke Model)
GitGalaxy utilizes a centralized distribution architecture to maintain a single source of truth while achieving maximum cross-platform compatibility. 

* **The Hub (PyPI):** The compiled Python codebase (the blAST engine) is hosted exclusively on the Python Package Index.
* **The Spokes (GitHub, GitLab, Jenkins, etc.):** Enterprise CI/CD platforms do not host the engine natively. Instead, they use lightweight YAML wrappers to dynamically pull the engine via `pip install gitgalaxy` and execute it within their isolated runners.

This allows us to instantly push updates to Azure DevOps, Bitbucket, GitLab, and GitHub Actions simultaneously just by tagging a new release.

## 2. Core CI/CD Configurations & Files

### GitHub Actions (The Orchestrator)
GitHub acts as the central command center for the project's source code and deployment triggers.
* **`.github/workflows/publish.yml`**: The release pipeline. Triggered strictly by Git tags (e.g., `v2.4.1`). It builds the Python wheel/sdist and authenticates with PyPI via OIDC to publish the package.
* **`.github/workflows/gitlab-sync.yml`**: The mirror pipeline. Fires alongside the PyPI publish workflow. It securely pushes the latest code and tags directly to the `squid-protocol1/gitgalaxy` repository on GitLab, keeping both platforms in perfect sync.
* **`action.yml`**: The native GitHub Action wrapper. Allows GitHub users to invoke GitGalaxy using standard `uses: squid-protocol/gitgalaxy@v2` syntax.

### GitLab CI/CD Catalog (The Enterprise Gate)
* **`scan.yml`**: The native GitLab CI/CD Component definition. This file defines the `gitgalaxy_scan` job, pulling the `python:3.12-slim` image, installing the engine from PyPI, and executing the Zero-Trust Spectral Audit with enterprise failure ratchets (`--max-risk-exposure`, `--fail-on-secrets`). It automatically exposes the generated `gitgalaxy-results_sarif.json` to GitLab's security dashboards.

### Project Build & Versioning
* **`pyproject.toml`**: The modern Python build configuration. It defines dependencies, CLI entry points (like `galaxyscope` and `supply-chain-firewall`), and uses `setuptools_scm` to dynamically generate the package version directly from Git tags (e.g., matching the `v2.4.1` regex).

## 3. Recent Engine Hardening & Security Patches

To support enterprise CI/CD environments, several critical stability and security patches were recently integrated:

* **CLI Pipeline Gates (`galaxyscope.py`)**: Added native `argparse` flags (`--fail-on-secrets`, `--fail-on-malware`, `--max-risk-exposure`) to allow CI/CD runners to programmatically fail builds when strict security thresholds are breached.
* **Regex ReDoS Armor (`language_standards.py`)**: 
  * Mitigated Catastrophic Backtracking (ReDoS) vulnerabilities in the C/C++ parser when handling massive, malformed K&R payload blocks by enforcing strict lazy consumers (`[^;{]*?;`).
  * Patched the `_dependency_capture` regex for Python and JavaScript to strip line anchors, allowing the Supply Chain Firewall to accurately detect inline, dynamic, and comma-separated dependency imports (e.g., `import os, requests`).
* **Dependency Auditing (`requirements.txt`)**: Bumped `mistune>=3.2.2` to resolve a high-severity CPU exhaustion vulnerability (CVE-2026-49851) flagged by the Muninn Security Scanner in our documentation build chain.
