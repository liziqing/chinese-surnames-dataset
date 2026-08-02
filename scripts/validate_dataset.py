#!/usr/bin/env python3
"""Validate the Chinese Surnames Dataset and report quality metrics."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "surnames.json"
SCHEMA_PATH = ROOT / "schema" / "surnames.schema.json"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        fail(f"file not found: {path}")
    except json.JSONDecodeError as error:
        fail(f"invalid JSON in {path}: line {error.lineno}, column {error.colno}: {error.msg}")


def main() -> int:
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        fail("the 'jsonschema' package is required; install it with 'python -m pip install jsonschema'")

    data = load_json(DATA_PATH)
    schema = load_json(SCHEMA_PATH)

    if not isinstance(data, list):
        fail("surnames.json must contain a top-level array")

    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema["$defs"]["surname"])
    schema_errors: list[str] = []
    whitespace_errors: list[str] = []
    variant_duplicate_errors: list[str] = []

    for index, record in enumerate(data, start=1):
        for error in validator.iter_errors(record):
            location = ".".join(str(part) for part in error.absolute_path) or "record"
            schema_errors.append(f"record {index} ({location}): {error.message}")

        if isinstance(record, dict):
            for field, value in record.items():
                if isinstance(value, str) and value != value.strip():
                    whitespace_errors.append(
                        f"record {index} ({record.get('hanzi', '?')}).{field} has leading or trailing whitespace"
                    )

            variants = record.get("variants")
            if isinstance(variants, list):
                duplicates = [value for value, count in Counter(variants).items() if count > 1]
                if duplicates:
                    variant_duplicate_errors.append(
                        f"record {index} ({record.get('hanzi', '?')}).variants repeats: {duplicates}"
                    )

    hanzi_values = [record.get("hanzi") for record in data if isinstance(record, dict)]
    combinations = [
        (record.get("hanzi"), record.get("pinyin"))
        for record in data
        if isinstance(record, dict)
    ]
    duplicate_hanzi = sorted(value for value, count in Counter(hanzi_values).items() if count > 1)
    duplicate_combinations = sorted(
        value for value, count in Counter(combinations).items() if count > 1
    )

    print("Chinese Surnames Dataset validation")
    print(f"Records: {len(data)}")
    print(f"Schema errors: {len(schema_errors)}")
    print(f"Duplicate Hanzi: {len(duplicate_hanzi)}")
    print(f"Duplicate Hanzi/Pinyin pairs: {len(duplicate_combinations)}")
    print(f"Duplicate variants: {len(variant_duplicate_errors)}")
    print(f"Whitespace issues: {len(whitespace_errors)}")

    problems = schema_errors + variant_duplicate_errors + whitespace_errors
    if duplicate_hanzi:
        problems.append(f"duplicate Hanzi values: {duplicate_hanzi}")
    if duplicate_combinations:
        problems.append(f"duplicate Hanzi/Pinyin pairs: {duplicate_combinations}")

    if problems:
        print("\nValidation failed:", file=sys.stderr)
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1

    print("Dataset validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
