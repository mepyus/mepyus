# line_thickening residue robustness probe note v0

## Why this probe exists

`derived_residue_trend=decaying` and `derived_residue_persistence=persistent_decay` still depend on a chosen recent window.

This probe asks a narrower question:

- if the same append-only history is re-read with windows `3 / 5 / 7 / 9`
- does the decaying/persistent direction still hold
- or is that read only an artifact of one cutoff

## Reading rule

- `robust_decay`
  - multiple tested windows agree on a decaying direction and persistent decay
- `weak_decay`
  - some windows decay, but agreement is thin
- `window_sensitive`
  - the window choice changes the interpretation materially
- `non_decay_stable`
  - there is no derived residue story to decay; the line is simply stable without it
- `insufficient_history`
  - not enough informative history exists for the tested windows

## Guardrail

This axis does not change status, thickness, scope, or promotion. It only states how reliable the current residue-trend reading is under multiple recent-window cuts.
