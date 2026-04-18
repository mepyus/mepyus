# operating_ui_phase1 input readiness wording and data quality refinement note v0

## verdict

- the `Input Readiness` panel wording is now clearer at the current scope
- the patch improves readability, not engine intelligence
- direct vs proxy readiness signals are now easier to distinguish

## what changed

- readiness wording now explicitly distinguishes:
  - `ready`
  - `partially ready`
  - `unavailable`
- field labeling now separates:
  - direct field
  - proxy field
- provenance wording is now framed as a pointer rather than a stronger readiness claim

## what stayed the same

- no runtime or heuristic change
- no composition redesign
- no decision or maturity behavior
- missing fields still remain placeholder or empty-state

## boundary

- this patch does not create deeper runtime intelligence
- it only makes the first panel easier to read honestly
