# line_thickening residue robustness probe v0

## Focus

This pass re-read the current append-only history only.

No new route, no new breadth, and no new observation expansion were added.

## Result

`transition_over_surface` now carries:

- `derived_residue_trend=decaying`
- `derived_residue_persistence=persistent_decay`
- `derived_residue_robustness=robust_decay`

The read remains mixed overall, but the residue-cleaning direction is not just a single-window artifact.

## Multi-window read

The current append-only history was re-read with windows `3 / 5 / 7 / 9`.

- `w=3`
  - `trend=decaying`
  - `persistence=persistent_decay`
- `w=5`
  - `trend=decaying`
  - `persistence=persistent_decay`
- `w=7`
  - `trend=decaying`
  - `persistence=unconfirmed_decay`
- `w=9`
  - `trend=decaying`
  - `persistence=unconfirmed_decay`

That means the direction is robust even though the larger windows soften the persistence strength.

## Comparison read

- `input_to_reading_organ`
  - `derived_residue_robustness=non_decay_stable`
- `pre_read_eye`
  - `insufficient_history`
- `raw_return_preservation`
  - `insufficient_history`

## Why this matters

`transition_over_surface` is still not clean-balanced or global.
But its recent derived residue read is now stronger than a one-window heuristic:
the recent windows agree that the derived residue is staying behind the current primary-only front.
