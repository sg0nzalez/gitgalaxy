import os
import sys
import time
import datetime
import hashlib
import hmac

LICENSING_VERIFICATION_SECRET = b"gg_offline_verification_salt_v1"


def _validate_offline_key(license_key: str) -> bool:
    """Mathematically verifies an offline license key and checks expiration."""
    try:
        parts = license_key.split("-")
        # Key now has 5 parts: GG - TIER - CUSTOMER - EXPDATE - HASH
        if len(parts) != 5 or parts[0] != "GG":
            return False

        tier, customer, exp_date_str, provided_signature = parts[1], parts[2], parts[3], parts[4]

        # 1. Verify the Expiration Date
        try:
            exp_date = datetime.datetime.strptime(exp_date_str, "%Y%m%d")
            if datetime.datetime.now() > exp_date:
                # Key is mathematically valid, but expired.
                return False
        except ValueError:
            return False

        # 2. Verify Cryptographic Integrity
        payload = f"{tier}-{customer}-{exp_date_str}".encode("utf-8")

        expected_signature = hmac.new(LICENSING_VERIFICATION_SECRET, payload, hashlib.sha256).hexdigest()

        return hmac.compare_digest(expected_signature, provided_signature)
    except Exception:
        return False


def enforce_licensing_guard(tool_name: str = "GitGalaxy Engine"):
    """
    Evaluates runtime environment for PolyForm compliance.
    Injects operational friction or audit tripwires for unverified environments.
    """
    if os.environ.get("GITGALAXY_ENV") == "development":
        return

    license_key = os.environ.get("GITGALAXY_LICENSE_KEY", "").strip()

    # 1. THE FULLY LICENSED CLEAN ROOM
    # If they paid you, they get absolute silence and maximum speed.
    if _validate_offline_key(license_key):
        return

    # 2. THE AUDIT TRIPWIRE (Community Free Tier)
    # No time delay, but burns a loud legal warning into their CI/CD audit logs.
    if license_key == "COMMUNITY_FREE_TIER":
        print("\n" + "=" * 80, file=sys.stderr)
        print(f" 🪐 {tool_name.upper()} ONLINE — COMMUNITY FREE TIER", file=sys.stderr)
        print("=" * 80, file=sys.stderr)
        print(" LEGAL AUDIT TRIPWIRE: Executing under PolyForm Noncommercial License 1.0.0.", file=sys.stderr)
        print(" WARNING: This key is NOT a legitimate license for commercial enterprise use.", file=sys.stderr)
        print(" If this engine is running in a corporate CI/CD pipeline, you are out of compliance.", file=sys.stderr)
        print(" Contact joe@gitgalaxy.io to acquire a commercial enterprise key.", file=sys.stderr)
        print("=" * 80 + "\n", file=sys.stderr)
        sys.stderr.flush()
        return

    # 3. THE UNLICENSED FRICTION TRAP
    # Missing or fake keys get the 5-second delay AND the warning.
    print("\n" + "=" * 80, file=sys.stderr)
    print(f" 🪐 {tool_name.upper()} ONLINE", file=sys.stderr)
    print("=" * 80, file=sys.stderr)
    print(" WARNING: Executing under PolyForm Noncommercial License 1.0.0.", file=sys.stderr)
    print(" Commercial use in corporate networks or CI/CD pipelines requires a license.", file=sys.stderr)
    print(" Contact joe@gitgalaxy.io to acquire a commercial key.", file=sys.stderr)
    print("\n >>> Enforcing 5-second synchronization delay for compliance visibility...", file=sys.stderr)
    print("=" * 80 + "\n", file=sys.stderr)

    sys.stderr.flush()
    time.sleep(5.0)
