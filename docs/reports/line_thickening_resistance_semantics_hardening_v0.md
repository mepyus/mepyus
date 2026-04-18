# Line Thickening Resistance Semantics Hardening v0

## Verdict

`implemented`

## Summary

The line thickening slice now separates `contradiction`, `weakness`, and `caution` in both observation packets and derived registry counts.

### Semantics split

- `contradiction_points`: actual counterevidence only
- `weakness_points`: line is still thin, but not opposed
- `caution_points`: promotion should slow down, but not because of contradiction

Legacy `resistance_or_counterexample` is retained for compatibility, but it no longer automatically increments contradiction. It is classified as caution unless it clearly reads like counterevidence.

### Registry hardening

- `support_count`
- `contradiction_count`
- `weakness_count`
- `caution_count`

`resistance_count` remains as a compatibility field only.

### Promotion behavior

- `summary_echo` remains thin.
- `source_linked` can support medium, but only when recurrence is real.
- `direct_span` recurrence can lift a line beyond thin.
- caution and weakness slow promotion without being treated as contradiction.

## Verification

The grounded internal-observer cohort was rerun through the existing `scripts/apply_internal_observer.py` path with bounded recurrence enabled. The results showed:

- exact same-fragment replay stayed suppressed
- new distinct fragments appended with direct-span or source-linked grounding
- old "single-run / summary-only" language moved into caution rather than contradiction
- `transition_over_surface` advanced to `medium`
- `input_to_reading_organ` advanced to `thick`

## Why this was needed before widening

Without this split, the line could keep accumulating pseudo-resistance and remain artificially thin. This change makes the thickening path reflect actual grounding quality instead of conflating "not enough yet" with "actively opposed."

## Deferred

- no new entrypoint
- no UI
- no graph / ontology / object lift
- no fuzzy dedupe
- no broad refactor
