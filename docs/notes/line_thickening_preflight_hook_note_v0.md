# line thickening preflight hook note v0

## Purpose

This note records the smallest bounded integration from the existing preflight reread path into the `line_thickening` runtime slice.

The goal is not to turn preflight into a new pipeline.
The goal is to let the existing reread gate emit line-centered observation packets when, and only when, the hook is explicitly enabled.

## Hook point

The natural hook point is `scripts/run_runtime_preflight.py` after the existing preflight outputs have already been written:

1. `preflight_last_decision.json`
2. breadcrumb append
3. phase decision append
4. optional pipeline observation append
5. optional line thickening append

This keeps preflight as the owner of the reread path and makes line thickening a sink.

## Opt-in control

The hook is gated by a new explicit flag:

- `--record-line-thickening`

Default behavior stays unchanged when the flag is absent.

## Mapping rule

The hook maps the actual preflight reread output into the minimum `RereadObservation` shape.

Minimum fields filled from preflight:

- `line_name` from the active latent line names selected by the preflight gate
- `asset_or_surface` from the current first-read target or the current reread surface
- `view_type` from the selected mode
- `evidence` from the preflight decision context
- `grounding_type` as direct for active latent lines
- `support_points`
- `weakness_points`
- `resistance_or_counterexample`
- `next_probe_surface`
- `thickness_before`
- `thickness_after`

## Behavior preserved

- Existing preflight behavior remains intact when the flag is off.
- The line-thickening slice does not replace breadcrumbs or phase decisions.
- The line-thickening registry remains a derived current-state surface.
- Append-only logs remain the source of truth.

## Current risk

- Only exact duplicate suppression is implemented.
- This is sufficient for the thin-slice insertion, but it does not remove fuzzy semantic duplication risk.
- The hook remains bounded and opt-in so that this risk stays local.

## One-line lock

> line thickening is a bounded sink attached to the existing preflight reread path, not a new owner of the reread flow.
