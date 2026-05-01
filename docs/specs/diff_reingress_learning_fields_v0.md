# Diff Reingress Learning Fields v0

## Execution

Additional fields:

- `useful_diff_modes`
- `salient_diff_paths_summary`
- `weak_diff_areas`
- `trivial_diff_warning`
- `next_diff_probe_hint`
- `reusable_comparison_pairs`
- `generated_diff_note`

## Interpretation

Comparison should not end with "different." Reingress should preserve which changed paths mattered and which comparisons were weak.

## Validation

- Next comparison run can reuse pairs and salient paths.
- Trivial differences remain visible but not over-promoted.
