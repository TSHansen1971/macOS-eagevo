#!/usr/bin/env python3
"""
Repo-local validator for macOS-eagevo Approval Evidence Package contracts.

Scope:
- Python stdlib only.
- No network.
- No pip/jsonschema dependency.
- Reads approval contract JSON files from schemas/approval.
- Validates one selected Approval Evidence Package JSON file.
- Performs contract-specific checks required for
  EAGEVO-MACOS-APPROVAL-PACKAGE-VALIDATOR-001A.

This is not a full JSON Schema engine and does not assert system approval.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = "0.1"

SCHEMA_DIR = Path("schemas/approval")
MAIN_SCHEMA_PATH = SCHEMA_DIR / "eagevo-approval-evidence-package.schema.json"
DECISION_SCHEMA_PATH = SCHEMA_DIR / "eagevo-approval-decision-record.schema.json"
CHANGE_SCHEMA_PATH = SCHEMA_DIR / "eagevo-change-assessment.schema.json"
TEMPORARY_USE_SCHEMA_PATH = SCHEMA_DIR / "eagevo-temporary-use-permit.schema.json"

CONTRACT_PATHS = [
    MAIN_SCHEMA_PATH,
    DECISION_SCHEMA_PATH,
    CHANGE_SCHEMA_PATH,
    TEMPORARY_USE_SCHEMA_PATH,
]

FALLBACK_PACKAGE_TYPES = {
    "initial_approval",
    "renewal_approval",
    "change_approval",
    "temporary_use",
    "withdrawal",
}

FALLBACK_PACKAGE_STATUSES = {
    "draft",
    "evidence_complete",
    "owner_decision_required",
    "approved_by_system_owner",
    "rejected_by_system_owner",
    "temporary_use_permit_required",
    "withdrawn",
}

SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")


class ValidationError(Exception):
    """Controlled validation error."""


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError as exc:
        raise ValidationError(f"missing JSON file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(
            f"invalid JSON syntax in {path}: line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def as_object(value: Any, path: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationError(f"{path} must be an object")
    return value


def as_array(value: Any, path: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValidationError(f"{path} must be an array")
    return value


def require_fields(obj: dict[str, Any], required: Iterable[str], path: str) -> None:
    missing = [field for field in required if field not in obj]
    if missing:
        raise ValidationError(f"{path} missing required field(s): {', '.join(missing)}")


def schema_required_fields(schema: dict[str, Any], schema_name: str) -> list[str]:
    required = schema.get("required", [])
    if not isinstance(required, list) or not all(isinstance(item, str) for item in required):
        raise ValidationError(f"{schema_name}.required must be an array of strings")
    return required


def schema_object_contract(schema: dict[str, Any], schema_name: str) -> None:
    if schema.get("type") != "object":
        raise ValidationError(f"{schema_name}.type must be object")

    properties = schema.get("properties")
    if not isinstance(properties, dict) or not properties:
        raise ValidationError(f"{schema_name}.properties must be a non-empty object")

    schema_required_fields(schema, schema_name)


def property_enum(schema: dict[str, Any], property_name: str) -> list[Any]:
    properties = schema.get("properties", {})
    if not isinstance(properties, dict):
        return []

    prop = properties.get(property_name)
    if not isinstance(prop, dict):
        return []

    enum = prop.get("enum")
    if isinstance(enum, list):
        return enum

    return []


def check_enum(value: Any, allowed: Iterable[Any], path: str) -> None:
    allowed_list = list(allowed)
    if value not in allowed_list:
        allowed_text = ", ".join(repr(item) for item in allowed_list)
        raise ValidationError(f"{path} has illegal value {value!r}; allowed: {allowed_text}")


def get_object(obj: dict[str, Any], key: str, path: str) -> dict[str, Any]:
    if key not in obj:
        raise ValidationError(f"{path}.{key} missing")
    return as_object(obj[key], f"{path}.{key}")


def check_bool(obj: dict[str, Any], key: str, expected: bool, path: str) -> None:
    actual = obj.get(key)
    if actual is not expected:
        raise ValidationError(f"{path}.{key} must be {str(expected).lower()}")


def check_approval_decision(package: dict[str, Any]) -> None:
    if "approval_decision" not in package:
        raise ValidationError("package.approval_decision missing")

    decision = package["approval_decision"]
    if decision is None:
        return

    if not isinstance(decision, dict):
        raise ValidationError("package.approval_decision must be null or an object")

    if decision.get("schema_version") != SCHEMA_VERSION:
        raise ValidationError("package.approval_decision.schema_version must be 0.1 when set")

    if not any(key in decision for key in ("decision_status", "decision", "decision_maker", "system_owner")):
        raise ValidationError(
            "package.approval_decision object is not recognisable as a structured decision record"
        )


def check_security_core_principles(package: dict[str, Any]) -> None:
    classification_profile = get_object(package, "classification_profile", "package")
    clearance_model = get_object(package, "clearance_model", "package")
    authorization_model = get_object(package, "authorization_model", "package")

    check_bool(
        classification_profile,
        "classification_does_not_grant_access",
        True,
        "package.classification_profile",
    )
    check_bool(
        clearance_model,
        "clearance_grants_access",
        False,
        "package.clearance_model",
    )

    if authorization_model.get("default_authorization") != "deny":
        raise ValidationError(
            "package.authorization_model.default_authorization must be 'deny'"
        )

    check_bool(
        authorization_model,
        "authorization_is_access_decision",
        True,
        "package.authorization_model",
    )


def check_information_values(package: dict[str, Any]) -> None:
    values = as_array(package.get("information_values"), "package.information_values")
    if not values:
        raise ValidationError("package.information_values must not be empty")


def check_evidence_references(package: dict[str, Any]) -> None:
    references = as_array(package.get("evidence_references"), "package.evidence_references")

    for index, reference in enumerate(references):
        path = f"package.evidence_references[{index}]"
        reference_obj = as_object(reference, path)
        sha256 = reference_obj.get("sha256")

        if sha256 in (None, ""):
            continue

        if not isinstance(sha256, str):
            raise ValidationError(f"{path}.sha256 must be a string when set")

        if not SHA256_RE.match(sha256):
            raise ValidationError(f"{path}.sha256 must be 64 hex characters")


def check_owner_decision_required_policy(package: dict[str, Any]) -> None:
    if package.get("package_status") != "owner_decision_required":
        return

    if package.get("approval_decision") is not None:
        raise ValidationError(
            "owner_decision_required package must not already contain an approval decision"
        )

    residual_risk = get_object(package, "residual_risk", "package")
    if residual_risk.get("accepted_by_system_owner") is not False:
        raise ValidationError(
            "owner_decision_required package residual_risk.accepted_by_system_owner must be false"
        )


def check_example_policy(package: dict[str, Any], package_path: Path) -> None:
    if package_path.as_posix() != "examples/approval/first-approval-package.example.json":
        return

    if package.get("package_status") != "owner_decision_required":
        raise ValidationError("example package package_status must be owner_decision_required")

    check_owner_decision_required_policy(package)


def validate_contracts() -> dict[str, Any]:
    schemas: dict[str, Any] = {}

    for path in CONTRACT_PATHS:
        schema = as_object(load_json(path), str(path))
        schema_object_contract(schema, str(path))
        schemas[path.name] = schema

    return schemas


def validate_package(package_path: Path) -> None:
    schemas = validate_contracts()
    main_schema = schemas[MAIN_SCHEMA_PATH.name]

    package = as_object(load_json(package_path), str(package_path))

    require_fields(package, schema_required_fields(main_schema, str(MAIN_SCHEMA_PATH)), "package")

    if package.get("schema_version") != SCHEMA_VERSION:
        raise ValidationError("package.schema_version must be 0.1")

    package_types = property_enum(main_schema, "package_type") or sorted(FALLBACK_PACKAGE_TYPES)
    package_statuses = property_enum(main_schema, "package_status") or sorted(FALLBACK_PACKAGE_STATUSES)

    check_enum(package.get("package_type"), package_types, "package.package_type")
    check_enum(package.get("package_status"), package_statuses, "package.package_status")

    check_approval_decision(package)
    check_security_core_principles(package)
    check_information_values(package)
    check_evidence_references(package)
    check_owner_decision_required_policy(package)
    check_example_policy(package, package_path)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a macOS-eagevo Approval Evidence Package using repo-local stdlib checks."
    )
    parser.add_argument("package", help="Path to Approval Evidence Package JSON file.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    package_path = Path(args.package)

    try:
        validate_package(package_path)
    except ValidationError as exc:
        print("validation: RED")
        print(f"error: {exc}")
        return 1

    print("validation: GREEN")
    print(f"package: {package_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
