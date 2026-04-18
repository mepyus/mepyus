# line_thickening derived reintroduction sentinel note v0

## Why this sentinel exists

`decaying`, `persistent_decay`, and `robust_decay` still need one more guard:
if derived residue comes back into the active recent window, the current clean-direction read should not be treated as if nothing changed.

## What this axis reads

- whether derived residue has re-entered the active recent window
- whether it exists only outside the current window
- what kind of trigger last introduced the derived row

## Sentinel classes

- `not_observed`
- `observed_recently`
- `observed_but_outside_window`
- `insufficient_history`

## Trigger classes

- `derived_route_refresh`
- `summary_echo_refresh`
- `mixed_source_refresh`
- `unknown`

## Guardrail

This is a monitoring axis only. It does not change status, thickness, scope, or promotion.
