# ADR-002: The dash gate sweeps raw bytes, not parsed values

## Status

Accepted.

## Context

BHIL prose convention bans em and en dashes in derived prose. An earlier
implementation in another repo swept parsed CSV values; the parser
normalized some cells and a banned byte shipped. The fix, recorded in
that repo's ADR-004, is the precedent here.

## Decision

`tools/dash_gate.py` reads files as bytes and searches for the UTF-8
sequences of U+2014 and U+2013 directly. It reports every occurrence with
a line number, not just the first, and scans the whole tree including
code comments, workflows, and collateral.

## Consequences

The gate cannot be fooled by encoding tricks a text-mode read would
normalize, and it is fast enough to run on every push. The cost is that
legitimate dashes in third-party content cannot enter the repo; vendored
content is out of scope by policy anyway.

## Open questions

1. Should the ban extend to horizontal bars and minus signs used as
   dashes? Settling criterion: extend on the first observed instance in
   a review; do not pre-ban characters with legitimate uses.
2. Should the gate offer an autofix mode? Settling criterion: add it if
   findings exceed five per month; below that, manual fixes keep authors
   conscious of the rule.
