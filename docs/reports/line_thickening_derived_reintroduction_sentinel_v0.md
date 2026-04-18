# line_thickening derived reintroduction sentinel v0

## Focus

This pass adds a sentinel for derived residue re-entry.

It does not add routes, breadth, or new observations.

## Current read

`transition_over_surface` now carries:

- `derived_residue_trend=decaying`
- `derived_residue_persistence=persistent_decay`
- `derived_residue_robustness=robust_decay`
- `derived_reintroduction_status=observed_but_outside_window`
- `derived_reintroduction_trigger=derived_route_refresh`

## Interpretation

The line is still mixed overall, but the last derived support currently sits outside the active recent window.
That means there is residue in history, but no current re-entry signal.

## Comparison

- `input_to_reading_organ`
  - `derived_reintroduction_status=not_observed`
- `pre_read_eye`
  - `insufficient_history`
- `raw_return_preservation`
  - `insufficient_history`

## Why this matters

This sentinel separates:

- clean recent windows with old derived residue still in the ledger
- actual recent re-entry of derived support

That keeps the current robust-decay read honest without pretending the mixed history disappeared.
