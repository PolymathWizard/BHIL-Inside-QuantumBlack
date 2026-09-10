# ADR-003: IP firewall scope for a style study

## Status

Accepted.

## Context

This repository teaches the communication discipline of a named firm. The
line between craft study and passing off must be explicit, enforceable,
and visible to every reader, because the audience is designers who will
build from it.

## Decision

Four walls, stated in `docs/method/ip-firewall.md` and repeated inside
every recipe: structural extraction only with a 25-word quotation budget;
no passing off; no trademarked construct names in generated work;
no trade-dress replication. Observed construct names live in
`data/constructs.csv` as generic descriptions rather than the firm's
coined labels wherever a generic description communicates the same
structural fact.

## Consequences

The repo can be published and cited without a rights question. Recipes
are slightly wordier because the guardrail repeats. Some readers will ask
for the coined names; the register points them to the primary sources
where those names appear in context.

## Open questions

1. Should the constructs CSV carry the coined names verbatim as
   competitive facts? Settling criterion: add a column if a downstream
   analysis needs exact-name matching; the guide itself does not.
2. Should generated-artifact templates ship in this repo? Settling
   criterion: ship them when the recipes stabilize for one full quarter
   without edits; templates fossilize whatever they copy.
