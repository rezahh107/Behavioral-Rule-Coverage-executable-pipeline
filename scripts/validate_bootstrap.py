#!/usr/bin/env python3
"""Bootstrap validation for Behavioral Rule Coverage Executable Pipeline.

This script intentionally uses only the Python standard library. It is not a
complete JSON Schema implementation. It checks the subset of schema features
used by the bootstrap examples so the repository has useful day-zero validation
without adding dependencies.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "STATUS.md",
    "ROADMAP.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "docs/PROJECT_CHARTER.md",
    "docs/ARCHITECTURE.md",
    "docs/CLAIM_BOUNDARIES.md",
    "docs/RULE_COVERAGE_MODEL.md",
    "docs/EXECUTABLE_PIPELINE_MODEL.md",
    "docs/LLM_WORKFLOW.md",
    "docs/ADR/ADR-0001-repository-purpose-and-scope.md",
    "schemas/rule.schema.json",
    "schemas/coverage-record.schema.json",
    "examples/rules/example.behavioral-rule.json",
    "examples/coverage/example.coverage-record.json",
    "scripts/README.md",
    "tests/README.md",
    ".github/pull_request_template.md",
    ".github/workflows/validate-docs.yml",
]


def load_json(relative_path: str) -> Any:
    path = ROOT / relative_path
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def fail(message: str) -> None:
    print(f"FAIL: {message}")


def check_required_files() -> list[str]:
    errors: list[str] = []
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            errors.append(f"Missing required file: {relative_path}")
    return errors


def _type_matches(value: Any, expected: Any) -> bool:
    expected_types = expected if isinstance(expected, list) else [expected]

    for expected_type in expected_types:
        if expected_type == "string" and isinstance(value, str):
            return True
        if expected_type == "boolean" and isinstance(value, bool):
            return True
        if expected_type == "object" and isinstance(value, dict):
            return True
        if expected_type == "array" and isinstance(value, list):
            return True
        if expected_type == "null" and value is None:
            return True
        if expected_type == "number" and isinstance(value, (int, float)) and not isinstance(value, bool):
            return True
        if expected_type == "integer" and isinstance(value, int) and not isinstance(value, bool):
            return True

    return False


def validate_instance(instance: Any, schema: dict[str, Any], path: str = "$") -> list[str]:
    errors: list[str] = []

    if "type" in schema and not _type_matches(instance, schema["type"]):
        errors.append(f"{path}: expected type {schema['type']}, got {type(instance).__name__}")
        return errors

    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                errors.append(f"{path}: missing required property {key}")

        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in instance:
                if key not in properties:
                    errors.append(f"{path}: unexpected property {key}")

        for key, value in instance.items():
            if key in properties:
                errors.extend(validate_instance(value, properties[key], f"{path}.{key}"))

    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{path}: string is shorter than minLength {schema['minLength']}")
        if "pattern" in schema and re.match(schema["pattern"], instance) is None:
            errors.append(f"{path}: value {instance!r} does not match pattern {schema['pattern']!r}")
        if "enum" in schema and instance not in schema["enum"]:
            errors.append(f"{path}: value {instance!r} is not in enum {schema['enum']}")

    if not isinstance(instance, str) and "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value {instance!r} is not in enum {schema['enum']}")

    return errors


def main() -> int:
    errors: list[str] = []

    errors.extend(check_required_files())

    json_files = [
        "schemas/rule.schema.json",
        "schemas/coverage-record.schema.json",
        "examples/rules/example.behavioral-rule.json",
        "examples/coverage/example.coverage-record.json",
    ]

    loaded: dict[str, Any] = {}
    for relative_path in json_files:
        try:
            loaded[relative_path] = load_json(relative_path)
        except json.JSONDecodeError as exc:
            errors.append(f"{relative_path}: invalid JSON: {exc}")

    if not errors:
        errors.extend(
            validate_instance(
                loaded["examples/rules/example.behavioral-rule.json"],
                loaded["schemas/rule.schema.json"],
            )
        )
        errors.extend(
            validate_instance(
                loaded["examples/coverage/example.coverage-record.json"],
                loaded["schemas/coverage-record.schema.json"],
            )
        )

    if errors:
        for error in errors:
            fail(error)
        return 1

    print("PASS: bootstrap validation completed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
