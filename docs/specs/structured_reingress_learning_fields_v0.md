# Structured Reingress Learning Fields v0

## Status

- phase: `phase1_8_structured_asset_reading_hardening`
- authority: `working_spec`

## Execution

Additional structured learning fields:

- `useful_structured_modes`
- `salient_paths_summary`
- `weak_structured_areas`
- `shape_only_warning`
- `next_structured_probe_hint`
- `reusable_structured_assets`
- `generated_asset_reading_note`

## Interpretation

Structured reading cannot end with "JSON read." The next run needs to know which paths mattered, which assets only exposed shape, and which generated artifacts remained shallow.

Weak structured areas are useful because they tell the next run where to probe, not because they block the current run.

## Validation

- Salient paths remain visible.
- Shape-only warning is explicit.
- Reusable structured assets are listed.
