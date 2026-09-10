#!/usr/bin/env python3
"""Drift gate: SHA-256 manifest over derived artifacts.

Derived artifacts are generated from canonical sources and never
hand-edited. This gate hashes each derived file and compares against
data/drift_manifest.json. Any mismatch fails CI, which forces edits back
through the canonical source and generator. stdlib only.

Usage:
  python3 tools/drift_gate.py           check mode (CI)
  python3 tools/drift_gate.py --write   refresh manifest after regeneration
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

DERIVED = [
    "docs/registry/source-register.md",
    "docs/assets/narrative-flow.svg",
    "docs/assets/framework-placement.svg",
    "docs/assets/vocabulary-migration.svg",
    "docs/assets/readme-banner.svg",
    "docs/assets/readme-badge-gates.svg",
    "docs/assets/readme-badge-license.svg",
    "docs/assets/readme-badge-artifacts.svg",
    "docs/assets/readme-badge-python.svg",
    "docs/assets/readme-sample-exhibit.svg",
    "docs/assets/readme-page-wireframe.svg",
    "docs/assets/readme-evidence-waffle.svg",
    "docs/assets/readme-artifact-mix.svg",
    "docs/assets/readme-stencil-pipeline.svg",
]
MANIFEST = "data/drift_manifest.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    manifest_path = root / MANIFEST
    current = {rel: sha256(root / rel) for rel in DERIVED if (root / rel).exists()}
    missing = [rel for rel in DERIVED if rel not in current]

    if "--write" in sys.argv:
        if missing:
            print("DRIFT GATE FAIL: cannot write manifest, derived files missing:")
            for rel in missing:
                print("  " + rel)
            return 1
        manifest_path.write_text(json.dumps(current, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {MANIFEST} covering {len(current)} derived artifacts")
        return 0

    if not manifest_path.exists():
        print("DRIFT GATE FAIL: manifest missing. Run with --write after generation.")
        return 1
    recorded = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    for rel in DERIVED:
        if rel not in recorded:
            errors.append(f"unhashed derived artifact: {rel}")
        elif rel in current and recorded[rel] != current[rel]:
            errors.append(f"hash mismatch (hand edit?): {rel}")
    errors.extend(f"derived file missing on disk: {rel}" for rel in missing)
    for rel in recorded:
        if rel not in DERIVED:
            errors.append(f"manifest entry no longer tracked: {rel}")
    if errors:
        print("DRIFT GATE FAIL")
        for err in errors:
            print("  " + err)
        return 1
    print(f"DRIFT GATE PASS: {len(DERIVED)} derived artifacts match manifest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
