#!/usr/bin/env python3
"""Regression tests for the repo gates. Every test names the bug it prevents.

stdlib unittest only. Run: python3 -m unittest discover -s tests -v
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import dash_gate  # noqa: E402
import drift_gate  # noqa: E402
import generate_register_page  # noqa: E402
import validate_register  # noqa: E402


class DashGateTests(unittest.TestCase):
    def test_dash_gate_scans_raw_bytes_not_parsed_values(self):
        """Bug (SPYGLASS ADR-004 class): a CSV-parser-based sweep normalized
        cells and missed an en dash that shipped in raw bytes. The gate must
        find banned bytes even inside quoted CSV cells."""
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "sample.csv"
            bad.write_bytes(b'id,title\n1,"range 2023\xe2\x80\x932026"\n')
            findings = dash_gate.scan(Path(tmp))
            self.assertEqual(len(findings), 1)
            self.assertIn("EN DASH", findings[0])

    def test_dash_gate_reports_every_occurrence_not_just_first(self):
        """Bug: an early sweep used find() once per file and stopped at the
        first hit, so a second dash on a later line survived cleanup."""
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "sample.md"
            bad.write_bytes(b"a\xe2\x80\x94b\nplain\nc\xe2\x80\x93d\n")
            findings = dash_gate.scan(Path(tmp))
            self.assertEqual(len(findings), 2)

    def test_repo_prose_is_dash_free(self):
        """Bug: collateral written outside the gate carried em dashes into a
        published README. The whole tree must pass, not just docs/."""
        self.assertEqual(dash_gate.scan(ROOT), [])


class RegisterTests(unittest.TestCase):
    def test_register_matches_ledger_roll_ups(self):
        """Bug: a silent row edit changed tier counts without updating the
        QA ledger. Roll-up equality pins the register to the ledger."""
        self.assertEqual(validate_register.validate(ROOT / "data" / "source_register.csv"), [])

    def test_register_generator_escapes_pipes_in_titles(self):
        """Bug: an artifact title containing a pipe broke the markdown table
        into extra columns and shifted every tier cell one position left."""
        self.assertEqual(generate_register_page.escape("A | B"), "A \\| B")


class DriftTests(unittest.TestCase):
    def test_drift_manifest_covers_every_derived_artifact(self):
        """Bug: a new SVG shipped without a manifest entry, so hand edits to
        it were invisible to CI. Every DERIVED path must be hashed."""
        import json

        recorded = json.loads((ROOT / "data" / "drift_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(sorted(recorded), sorted(drift_gate.DERIVED))

    def test_gates_pass_end_to_end_via_cli(self):
        """Bug: a tool passed when imported but failed as a script because
        __main__ wiring diverged. Exercise the CLI paths CI actually runs."""
        for tool in ("validate_register.py", "dash_gate.py", "drift_gate.py"):
            proc = subprocess.run(
                [sys.executable, str(ROOT / "tools" / tool)],
                capture_output=True,
                text=True,
                cwd=ROOT,
            )
            self.assertEqual(proc.returncode, 0, msg=f"{tool}: {proc.stdout}{proc.stderr}")


if __name__ == "__main__":
    unittest.main()
