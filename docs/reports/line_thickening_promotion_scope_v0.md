# Line Thickening Promotion Scope v0

## Verdict

`implemented`

## Summary

`line_thickening` now distinguishes line strength from validation scope.

### Strength

- `status` remains the operational line state
- `thickness_level` remains the local strength signal

### Scope

- `promotion_scope` says how broadly the line has actually been validated
- `scope_basis_summary` records the evidence basis in a short derived form
- `distinct_path_count`, `distinct_source_family_count`, `distinct_surface_family_count`, `distinct_run_count`, `distinct_asset_count`, and `distinct_source_pointer_count` are recorded as basis axes

### Current behavior

- preflight summary lines remain `path_local`
- local grounded lines can become `source_family_local`
- stronger grounded recurrence across distinct source families inside one validation route can become `cross_family_candidate`
- `global_operating` is not auto-assigned

## Verification

The grounded path was rerun through `scripts/apply_internal_observer.py` with bounded recurrence validation. The registry now stores scope alongside thickness and basis axes for the touched lines, and the promotion log records scope basis separately from thickness.

Observed examples:

- `pre_read_eye`: `thin`, `path_local`
- `raw_return_preservation`: `thin`, `path_local`
- `transition_over_surface`: `medium`, `source_family_local` in the existing registry history; this turn did not need to widen it further
- `input_to_reading_organ`: `thick`, `cross_family_candidate` with `distinct_path_count=1`

## Why this matters

The system can now say:

- strong local line
- validated on a bounded path
- not yet global

That prevents local success from being read as a global operating guarantee.
