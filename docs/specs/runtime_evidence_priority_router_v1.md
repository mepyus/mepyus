# Runtime Evidence Priority Router v1

## Purpose
- Route runtime evidence and adjacent canonical diff into an operating priority band.
- Preserve canonical truth as-is and add only an attention-ordering layer.

## Inputs
- `asset_id`
- `update_trigger_type`
- `changed_fields`
- `diff_class`
- `interpretation_badges`
- `evidence_refs` presence/count
- `provenance_only`
- blocker added/removed
- traceability / grounding / packet texture / maturation shifts

## Outputs
- `priority_level`
- `attention_reason`
- `queue_candidate`
- `suppress_reason`
- `routed_at`

## Priority Bands
- `critical`
  - `traceability_status` change
  - `grounding_status` change
  - `packet_texture` change
  - blocker added
  - `manual_correction`
- `high`
  - `mixed_shift`
  - `emergence_status` change
  - `carryover_risk` change
  - `maturation_state` change
  - blocker removed
- `medium`
  - `comparison_memory_reason` change
  - generic canonical change
  - `no_previous_state` anchor
- `low`
  - provenance-only non-runtime update
- `background`
  - provenance-only runtime update
  - repeated background adoption run

## Suppression
- Repeated `provenance_only` runtime updates do not become active queue items.
- They may be summarized as compact background attention summaries.

## Guards
- Router never edits canonical state.
- Router never uses `experimental_namespace` as a primary importance key.
- Router never promotes naming-heavy interpretation into priority reason.
