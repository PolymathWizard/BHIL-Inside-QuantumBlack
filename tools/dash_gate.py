#!/usr/bin/env python3
"""Dash gate: fail CI if any em dash or en dash appears anywhere in the repo.

BHIL prose convention bans em dashes (U+2014) and en dashes (U+2013) in all
derived prose. The sweep runs on RAW BYTES, not parsed values, because the
SPYGLASS ADR-004 incident showed that a CSV parser can normalize or skip
bytes that still ship to readers. stdlib only.
"""
from __future__ import annotations

import sys
from pathlib import Path

BANNED = {
    b"\xe2\x80\x94": "EM DASH U+2014",
    b"\xe2\x80\x93": "EN DASH U+2013",
}
SCAN_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".csv", ".cff", ".txt", ".html", ".css", ".svg", ".json"}
SKIP_DIRS = {".git", "site", "__pycache__", "engagements", ".cache"}


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and (path.suffix.lower() in SCAN_SUFFIXES or path.name in {"LICENSE", "LICENSE-CONTENT"}):
            yield path


def scan(root: Path) -> list[str]:
    findings: list[str] = []
    for path in iter_files(root):
        raw = path.read_bytes()
        for needle, label in BANNED.items():
            offset = raw.find(needle)
            while offset != -1:
                line = raw.count(b"\n", 0, offset) + 1
                findings.append(f"{path.relative_to(root)}:{line}: {label}")
                offset = raw.find(needle, offset + 1)
    return findings


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    findings = scan(root)
    if findings:
        print("DASH GATE FAIL")
        for f in findings:
            print("  " + f)
        return 1
    print("DASH GATE PASS: no em or en dashes in scanned bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
