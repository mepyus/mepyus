# line_thickening sandbox reintroduction trip note v0

## Why sandbox is required

This check must prove that the derived reintroduction sentinel can actually flip.

That requires inserting a fresh derived row into the recent window.
Doing that in the main runtime would contaminate the current append-only history, so the trip test must run on a sandbox copy.

## Trip method

- copy only the sentinel-relevant runtime files into a sandbox runtime
- reuse the existing `structured_doc_routing` path family
- clone the latest `transition_over_surface` derived row from that path family
- append the cloned derived row into the sandbox only

## Expected flip

- before: `observed_but_outside_window`
- after: `observed_recently`
- trigger: `derived_route_refresh`

## Guardrail

The point is not promotion or widening.
The point is only to prove that the sentinel behaves like a real trip signal.
