# line_thickening sandbox reintroduction trip v0

## Focus

This pass tested whether the derived reintroduction sentinel actually flips when a fresh derived row enters the recent window.

The main runtime was not touched.

## Method

- copied only the sentinel-relevant runtime files into a sandbox runtime
- reused the existing `structured_doc_routing` path family
- cloned the latest `transition_over_surface` derived row from that path family
- appended that cloned row into the sandbox only

## Expected read

- before trip
  - `observed_but_outside_window`
- after trip
  - `observed_recently`
  - `derived_reintroduction_trigger=derived_route_refresh`

## Why this matters

This confirms the sentinel is not just a static label on old history.
It can actually trip when derived residue returns into the active recent window.

## Actual observed flip

- before
  - `observed_but_outside_window`
  - `derived_route_refresh`
  - `last_derived_reintroduction_offset=12`
- after
  - `observed_recently`
  - `derived_route_refresh`
  - `last_derived_reintroduction_offset=0`
- side effect
  - the recent-window residue read becomes `stable / stable_mixed / non_decay_stable` because one fresh derived row is now back inside the active window
