# Phase 1.22 Unresolved Boundary Decision Note v0

## Decision Table

| Family / bucket | Current decision | Why |
| --- | --- | --- |
| raw_intake_gap | keep default-sufficient | default keeps the useful boundary reread; flow-aware adds no real gain |
| general_line_vs_flow | conditional-only candidate pressure, but keep default-sufficient for now | thin independent flow survives, but default already exposes it |
| input_layer_wrapper | protect as default-sufficient | flow is real, but tuning is unnecessary and risks misreading the family |
| conditional-only bucket | keep structurally open, currently empty | no clean candidate yet, but the middle bucket should not be closed conceptually |

## Keep Default-Sufficient

- `raw_intake_gap`

Reason:

- current evidence still says default is the most honest operating choice

## Move Toward Block-List

None from this unresolved set.

Reason:

- `raw_intake_gap` stays weak, but not misleading enough yet to justify a block-list move

## Conditional-Only Candidate

- `general_line_vs_flow` only as unresolved pressure, not as active bucket entry

Reason:

- this is the clearest family that could later justify the middle bucket
- current evidence is still too light to promote it there now

## Protect As Default-Sufficient

- `input_layer_wrapper`

Reason:

- flow survival is real
- but tuning adds little and may create future overreach

