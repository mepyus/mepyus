# line_thickening sandbox recovery check v0

## Focus

This pass closed the sentinel loop for `transition_over_surface` in a sandbox runtime only.

The main runtime was not touched.

## Method

- copied only the sentinel-relevant runtime files into a sandbox runtime
- appended one sandbox-only derived `structured_doc_routing` row to trip the sentinel
- appended five distinct primary-only rows from existing routes to push that derived row back outside the active recent window

## Loop result

- before
  - `observed_but_outside_window`
  - `derived_route_refresh`
  - `last_derived_reintroduction_offset=12`
- after trip
  - `observed_recently`
  - `derived_route_refresh`
  - `last_derived_reintroduction_offset=0`
- after recovery
  - `observed_but_outside_window`
  - `derived_route_refresh`
  - `last_derived_reintroduction_offset=5`

## Recovery read

- the sentinel loop is real
- the derived row can re-enter the active recent window
- the same derived row can be pushed back out again by later primary-only refresh
- after recovery the overall line is still mixed, but the recent read returns to clean primary-only dominance

## Why this matters

This confirms the sentinel is not a static historical label and not a one-way trip flag.
It can both trip and recover under bounded, sandbox-only conditions.
