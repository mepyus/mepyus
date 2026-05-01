# Phase 1.33 Flow-Aware Front Card Boundary Clarification Note v0

## Verdict

LOCK_FRONT_AS_OPERATOR_INTAKE

## Why Clarification Was Needed

Phase 1.32 showed one narrow risk:

- `general_line_vs_flow` could be read too quickly as a family that is already halfway into reopen permission

The actual rule is narrower:

- it stays on default
- unresolved pressure stays explicit
- reopen still requires a real trigger

## Card Updated

- [phase1_31_flow_aware_family_mode_card_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_31_flow_aware_family_mode_card_v0.md)

## Exact Clarification Added

1. In the `general_line_vs_flow` row:

- from:
  - `keep default; do not treat thin flow as tuning permission`
- to:
  - `keep default; do not treat thin flow or unresolved pressure as reopen permission by itself`

2. In `Quick Rule`:

- added:
  - `trigger candidate is not the same thing as actual reopen permission`

## Why Only This Was Added

This was the smallest boundary fix that addressed the acceptance note directly.

It was enough because:

- the operator cards already handled start / stop / trigger path correctly
- the remaining risk was only the interpretation of unresolved pressure at the family row level

## Why Other Nuance Stayed In Reference

The following still should not move into front cards:

- full unresolved handling for `general_line_vs_flow`
- `conditional-only` bucket treatment
- protected-default detailed reasoning for `input_layer_wrapper`
- broader reopen reasoning

Those remain better as reference notes because they are not needed for first operator intake.

## Current Judgment

After this clarification, the front cards are narrow enough and clear enough to be provisionally locked as operator intake surface.
