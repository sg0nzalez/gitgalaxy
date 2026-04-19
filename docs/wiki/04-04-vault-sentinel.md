# Vault Sentinel (High-Speed Secrets Scanner)

> **Guarding the Cryptographic Vault**
>
> Committing a hardcoded AWS key or Stripe token to a Git repository is a catastrophic security failure. By the time a background CI/CD job catches it, bots have already scraped the key from the public commit history.
>
> The Vault Sentinel (`vault_sentinel.py`) is GitGalaxy's specialized, ultra-fast secrets scanner. It is specifically engineered to act as a localized pre-commit hook, instantly scanning files for hardcoded secrets, `.env` exposures, and cryptographic keys *before* they ever leave the developer's machine.

## High-Speed Physics (Neutering the Lens)

Because pre-commit hooks must execute in milliseconds to avoid frustrating developers, the Sentinel cannot afford to run the full, computationally heavy 60-point optical scan. 

To achieve massive velocity, the Orchestrator instantiates the `SecurityLens` in "paranoid" mode but explicitly **neuters the lens**. It rips out all threat signatures except for two:
* `private_info`: Hunts for high-entropy strings, AWS API keys, SaaS tokens, and database passwords.
* `graveyard`: Hunts for commented-out logic (developers frequently comment out old API keys instead of deleting them).

## The Two-Pass Funnel

The Sentinel processes files using a strict two-pass funnel to optimize I/O and CPU cycles:

### 1. Tier 0 Path Scan (The Surface Radar)
Before opening a single file, the Sentinel evaluates the file paths against the `ApertureFilter` and `DENYLIST_PATTERNS`. 
* It instantly flags any file claiming to be a `.pem` certificate, an `id_rsa` private key, or a `.env` file.
* If a Tier 0 Path Breach is detected, the Sentinel immediately increments the leak counter and flags the file without wasting CPU cycles reading its contents.

### 2. The Deep Content Scan
If the file path is safe, the Sentinel loads the file's contents into memory and runs the neutered Security Lens to hunt for:
* Cloud Infrastructure Keys (AWS, GCP, Azure)
* SaaS & CI/CD Tokens (GitHub Personal Access Tokens, Stripe Secret Keys)
* Cryptographic Vaults

When a hardcoded credential is breached, the Sentinel dumps the exact snippet to the console so the developer can immediately locate and scrub the token.

## Allowlist Bypasses & CI/CD Integration

In testing environments, developers often use mock API keys or dummy certificates. To prevent the Sentinel from blocking legitimate test data, it cross-references the file path against the `ALLOWLIST_PATHS` defined in the global `gitgalaxy_config.py`. If a mock secret is found in an allowlisted test file, the tool logs it as an `[ALLOWED BYPASS]` but does not fail the build.

When the scan is complete, the Sentinel generates a strict Mission Report detailing the Uncontrolled Leaks. If even a single unauthorized secret is exposed, the script exits with a status code of `1`, violently blocking the `git commit` or Pull Request.