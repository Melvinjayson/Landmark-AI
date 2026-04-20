"""Minimal OpenAPI breaking-change guardrail.

This script validates contract stability for critical operations and exits non-zero
if required paths or methods disappear.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

OPENAPI_FILE = Path("specs/openapi.yaml")
REQUIRED_OPERATIONS = {
    ("/health", "get"),
    ("/vaults", "post"),
    ("/vaults/{vaultId}", "get"),
    ("/documents", "post"),
    ("/documents/{documentId}", "get"),
    ("/trust-scores/{vaultId}", "get"),
    ("/trust-scores/{vaultId}", "post"),
}


def load_contract() -> dict:
    if not OPENAPI_FILE.exists():
        raise FileNotFoundError(f"Missing {OPENAPI_FILE}")

    with OPENAPI_FILE.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def assert_required_operations(contract: dict) -> list[str]:
    paths: dict = contract.get("paths", {})
    errors: list[str] = []

    for path, method in sorted(REQUIRED_OPERATIONS):
        path_item = paths.get(path)
        if not path_item:
            errors.append(f"Missing required path: {path}")
            continue
        if method not in path_item:
            errors.append(f"Missing required operation: {method.upper()} {path}")

    return errors


def main() -> int:
    contract = load_contract()
    errors = assert_required_operations(contract)

    if errors:
        print("OpenAPI compatibility check failed:")
        for err in errors:
            print(f" - {err}")
        return 1

    print("OpenAPI compatibility check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
