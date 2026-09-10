# Evidence discipline

Every assertion in this repository carries one of five tiers, applied at
the lowest defensible level. This is the part of the method that keeps a
style study from quietly becoming a marketing claim.

## The five tiers

| Tier | Meaning |
| --- | --- |
| VERIFIED | Confirmed against a primary record the analyst inspected |
| CORROBORATED | Supported by two or more independent sources |
| UNCORROBORATED | Single thin source, such as a marketing case card |
| INFERENCE | Analyst judgment; mandatory for claims resting on fewer than three artifacts |
| STATED | The firm's claim about its own methods or results, quarantined |

## The STATED quarantine

McKinsey's statements about its own impact are always STATED, never
promoted without independent confirmation. Examples quarantined in this
study: the economic-potential value band, a named client's drafting-hours
reduction, the share of respondents qualifying as high performers, and all
forward-looking market sizings. The structure of the artifact that carries
the claim is observable; the outcome inside it is not.

## No CLEAN verdicts

No component of this repo ever outputs CLEAN. Absence of an anomaly report
is INCONCLUSIVE. The register validator prints exactly that reminder on
success, and probes classify transport-level results only, leaving
provenance verdicts to content review.

## Row-level and claim-level roll-ups

The register in this repo counts tiers at row level: 13 VERIFIED, 15
CORROBORATED, 3 UNCORROBORATED, 1 STATED across 32 rows. The parent brief
also reports a claim-level roll-up that counts quarantined STATED claims
embedded inside rows and the 4 INFERENCE-tier DNA claims from the
codebook. Both are correct; they count different things, and the
validator pins the row-level ledger so drift is loud.

## What this buys a designer

When a guide says "survey reports place roughly one exhibit every one to
two pages," you can trace that to counted pages in named artifacts. When
it says a case pattern exists, the register shows the pattern rests on
thin case cards and is held at lower confidence. Style advice with an
evidence trail ages better than style advice with vibes.
