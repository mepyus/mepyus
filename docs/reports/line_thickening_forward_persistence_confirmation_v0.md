# line_thickening forward persistence confirmation v0

## Target

This pass checked `transition_over_surface` only.

## Forward refresh

Used existing primary route only:

- `source_fragment_view`

Used two pointer-bearing primary anchors that were not part of the previous persistence confirmation:

- `frag_basic3_003`
- `frag_ytex_002`

## Result

`transition_over_surface` keeps:

- `derived_residue_trend=decaying`
- `derived_residue_persistence=persistent_decay`

Current supporting read after the forward refresh:

- `recent_decay_streak=2`
- `last_derived_support_offset=12`
- `recent_primary_rows=5`
- `recent_derived_rows=0`
- `distinct_primary_material_anchor_count=9`

The persistence read still holds after the additional primary-only refresh.

## Interpretation

This line is still mixed overall, but the mixed residue is not moving back into the recent window.
The current direction remains: primary corroboration continues to arrive while derived residue stays pushed back.

## Failure conditions

`persistent_decay` would break if derived support re-entered the recent window.
If that happened, the line would read as `reappearing` or fall back toward a mixed recent state.

`stable_mixed` is not the read for this line.
That class is reserved for lines that have enough history but no derived residue history to decay from.

## Non-result

This pass does not claim broader scope, cleaner overall ecology, or any new promotion step.
