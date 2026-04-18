# line_thickening residue trend persistence probe v0

## Result

The current state keeps the residue trend probe honest and adds persistence on top of it.

- `transition_over_surface`
  - `derived_residue_trend=decaying`
  - `derived_residue_persistence=persistent_decay`
  - `recent_decay_streak=2`
  - `last_derived_support_offset=10`
- `input_to_reading_organ`
  - `derived_residue_trend=stable`
  - `derived_residue_persistence=stable_mixed`
  - no derived support in history
- `pre_read_eye`
  - `insufficient_history`
- `raw_return_preservation`
  - `insufficient_history`

## Interpretation

`transition_over_surface` is not just temporarily cleaner. The current primary-only refresh leaves the recent window clean, so the decay signal persists.

`input_to_reading_organ` is not a decay case. It is a primary-dominant line with no derived residue, so the corrected persistence read is `stable_mixed`.

## What changed

- Added `derived_residue_persistence`
- Added `recent_decay_streak`
- Added `last_derived_support_offset`
- Added `persistence_basis_summary`
- Corrected the no-derived-history branch so a clean primary-only line does not get misread as decay

## What did not change

- No new route
- No breadth expansion
- No status or scope promotion change
- No UI / graph / ontology work
