# BHIL-Inside-QuantumBlack

A designer field guide to how McKinsey QuantumBlack strategically communicates.

This repository turns a BHIL STENCIL deconstruction of 32 public McKinsey
Digital and QuantumBlack artifacts into a working reference for designers,
information architects, and research communicators. It explains the argument
structure, exhibit grammar, framework placement, page architecture, lexical
register, and publishing cadence behind one of the most disciplined publishing
systems in professional services, and it packages those observations as
reusable build recipes with a hard intellectual-property firewall.

The study is an analysis of public materials. It records structure, sequence,
chart types, and phrase patterns as observations. It does not reproduce
McKinsey content, logos, trademarked framework names, or trade dress, and the
build recipes require original names and original visual identity throughout.

## Who this is for

* Designers who want to understand why QuantumBlack pages read so fast.
* Research and intelligence teams raising their own artifact standard.
* Writers building survey reports, paradox essays, or trend compendia.
* Anyone studying strategic communication as a craft, not a costume.

## The one-line finding

The exhibit is the atomic unit: one idea, one conclusion, one proof. The
firm varies its vocabulary every year and its structure almost never.

## Repository map

| Path | What it holds |
| --- | --- |
| `docs/method/` | The STENCIL method, evidence discipline, and IP firewall |
| `docs/guide/` | Twelve field-guide chapters on the communication system |
| `docs/recipes/` | Three build recipes plus the production checklist |
| `docs/registry/` | Source register (derived) and the QA ledger |
| `data/` | Canonical CSVs: source register, narrative coding, constructs |
| `tools/` | stdlib-only Python: gates, generators, validators |
| `tests/` | Regression tests; every test names the bug it prevents |
| `ADRs/` | Architecture decision records with open questions |
| `collateral/` | GitHub descriptions and LinkedIn launch posts |

## Quickstart

```bash
# validate the canonical register against the QA ledger roll-ups
python3 tools/validate_register.py

# regenerate derived artifacts, then refresh the drift manifest
python3 tools/generate_register_page.py
python3 tools/generate_diagrams.py
python3 tools/drift_gate.py --write

# run every gate the CI runs
python3 tools/dash_gate.py
python3 tools/drift_gate.py
python3 -m unittest discover -s tests -v

# build the site
pip install mkdocs-material
mkdocs build --strict
```

## Governance rules this repo enforces

* **Canonical source enforcement.** `data/source_register.csv` is the single
  source of truth. `docs/registry/source-register.md` and the SVG diagrams
  are derived artifacts behind a SHA-256 drift gate. Hand edits fail CI.
* **Evidence discipline.** Every register row carries one of five tiers.
  Firm self-claims are always STATED and never promoted. No tool in this
  repo ever reports CLEAN; absence of anomaly is INCONCLUSIVE.
* **Dash gate.** Em dashes and en dashes are banned in all prose and are
  swept on raw bytes, not parsed values.
* **Regression tests name their bugs.** See `tests/test_gates.py`.

## Companion artifacts

* BHIL STENCIL deconstruction brief, REF STN-MCK-001/V1.
* Source register and discovery index, REF STN-MCK-001/A1.
* Inside QuantumBlack visual field guide (20-page PDF companion deck).

## Licensing

Dual licensed: MIT for code, schemas, and tooling; CC BY 4.0 for prose
content in `docs/` and `ADRs/`. See `LICENSE` and `LICENSE-CONTENT`.

---

BHIL, Barry Hurd Intelligence Lab. Human-Directed. AI-Enabled. Commercially Tested.
