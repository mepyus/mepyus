# Phase 1.25 Flow-Aware Trigger Checklist v0

## Global Rule

Triggers must be evidence-based.

Do not reopen from:

- single anecdotal sample
- naming intuition
- generic flow wording
- unresolved pressure by itself

Do not reopen broadly.
Reopen only the affected family or bucket.

## `general_line_vs_flow` Reopen Trigger

Reopen only if one of the following is true.

- repeated samples show a real middle case between default and allow-list
- default repeatedly misses a better local slice
- carry-forward shifts toward actual reroute usefulness across repeated cases

Without one of these:

- keep current placement

## `raw_intake_gap` Reopen Trigger

Reopen only if one of the following is true.

- repeated evidence shows current default is no longer honest enough
- flow-aware repeatedly adds overreach or noise strongly enough to justify a block-list move
- carry-forward or local slice evidence changes enough to destabilize current placement

Without one of these:

- keep current placement

## `conditional-only` Bucket Reopen Trigger

Reopen only if one of the following is true.

- a family repeatedly cannot be placed honestly in either default-sufficient or allow-list
- a bounded middle case appears repeatedly across samples
- current buckets create repeated contradiction

Without one of these:

- keep the bucket structurally open but operationally empty

## `input_layer_wrapper` Reopen Trigger

Reopen only if one of the following is true.

- default repeatedly misses a better local slice
- carry-forward shifts from stable low-value to actual reroute handle
- bounded flow-aware repeatedly yields real narrowing beyond current default

Without one of these:

- protect current default placement

## Broad Reopen Guard

Without a trigger:

- do not reopen allow-list / block-list
- do not reopen emitter work
- do not restart tuning rounds
