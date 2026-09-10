#!/usr/bin/env python3
"""Validate the canonical source register against the STENCIL evidence rules.

Checks, in order:
  1. Schema: exact header, no empty required cells.
  2. IDs: STN-MCK-### format, unique, contiguous 001..032.
  3. Taxonomy: T1 through T6 only.
  4. Tier: one of the five STENCIL tiers.
  5. Row-level tier counts match the register ledger (13 V, 15 C, 3 U,
     1 S). The parent brief reports a claim-level roll-up (9/12/3/4/4)
     that also counts quarantined STATED claims embedded inside rows and
     INFERENCE-tier DNA claims; those live in the codebook, not here.
  6. No component may claim CLEAN; absence of anomaly is INCONCLUSIVE,
     so this tool never prints CLEAN.

stdlib only.
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

EXPECTED_HEADER = ["id", "title", "taxonomy", "date", "locator", "discovery", "access", "tier", "notes"]
VALID_TAXONOMY = {"T1", "T2", "T3", "T4", "T5", "T6"}
VALID_TIERS = {"VERIFIED", "CORROBORATED", "UNCORROBORATED", "INFERENCE", "STATED"}
EXPECTED_TIER_COUNTS = {"VERIFIED": 13, "CORROBORATED": 15, "UNCORROBORATED": 3, "STATED": 1}
EXPECTED_TAXONOMY_COUNTS = {"T1": 15, "T2": 5, "T3": 2, "T4": 4, "T5": 4, "T6": 2}
ID_PATTERN = re.compile(r"^STN-MCK-(\d{3})$")


def load(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    header, rows = load(path)
    if header != EXPECTED_HEADER:
        errors.append(f"header mismatch: {header}")
    seen_numbers: list[int] = []
    for row in rows:
        rid = row.get("id", "")
        match = ID_PATTERN.match(rid)
        if not match:
            errors.append(f"bad id format: {rid!r}")
            continue
        seen_numbers.append(int(match.group(1)))
        for field in ("title", "taxonomy", "date", "locator", "discovery", "access", "tier"):
            if not row.get(field, "").strip():
                errors.append(f"{rid}: empty required field {field}")
        if row["taxonomy"].split("/")[0] not in VALID_TAXONOMY:
            errors.append(f"{rid}: invalid taxonomy {row['taxonomy']!r}")
        if row["tier"] not in VALID_TIERS:
            errors.append(f"{rid}: invalid tier {row['tier']!r}")
    if sorted(seen_numbers) != list(range(1, len(rows) + 1)):
        errors.append("ids are not contiguous from 001")
    if len(seen_numbers) != len(set(seen_numbers)):
        errors.append("duplicate ids present")

    tier_counts = Counter(row["tier"] for row in rows)
    if dict(tier_counts) != EXPECTED_TIER_COUNTS:
        errors.append(f"tier roll-up drifted: {dict(tier_counts)} expected {EXPECTED_TIER_COUNTS}")
    tax_counts = Counter(row["taxonomy"].split("/")[0] for row in rows)
    if dict(tax_counts) != EXPECTED_TAXONOMY_COUNTS:
        errors.append(f"taxonomy roll-up drifted: {dict(tax_counts)} expected {EXPECTED_TAXONOMY_COUNTS}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    path = root / "data" / "source_register.csv"
    errors = validate(path)
    if errors:
        print("REGISTER VALIDATION FAIL")
        for err in errors:
            print("  " + err)
        return 1
    print("REGISTER VALIDATION PASS: 32 rows, roll-ups match ledger. Absence of anomaly is INCONCLUSIVE, not CLEAN.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
