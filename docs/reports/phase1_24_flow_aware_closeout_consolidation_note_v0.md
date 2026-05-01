# Phase 1.24 Flow-Aware Closeout Consolidation Note v0

## Purpose

This note closes the current flow-aware selection package by connecting the locked heuristic to a higher operating surface.

It does not add new tuning.
It does not reopen unresolved items broadly.
It consolidates what is now stable enough for operator and reader use.

## Phase Path Summary

The current flow-aware rule was not produced in one step.
It was narrowed through the following sequence.

1. lower camera support was specified as a bounded support artifact
2. lower camera support was emitted as `evidence_only`
3. upper bounded reread confirmed that `boundary` and `change + boundary` were already usable reread handles
4. flow validation showed that flow is neither globally weak nor globally useful
5. selection pressure validation showed the main bottleneck was reader-side selection, not broad emitter failure
6. selection tuning narrowed where flow-aware reread helps and where it does not
7. heuristic lock separated:
   - allow-list
   - block-list
   - default-sufficient
   - protected default-sufficient
   - unresolved hold

## Current Locked Operating Rule

### Allow-list

- `route_selection`
- `operating_cell`

Meaning:

- bounded flow-aware selection may be used
- only because flow reroute has shown actual reread gain

### Block-list

- `preprocess_builder`
- `preprocess_jung`
- `compact_title_only`

Meaning:

- flow-aware selection should not be used
- the gain is too small or absent
- bias risk is higher than value

### Keep default-sufficient

- `raw_intake_gap`

Meaning:

- default remains the honest current operating mode
- no extra tuning is justified now

### Protect as default-sufficient

- `input_layer_wrapper`

Meaning:

- flow exists
- but flow-aware selection should still not be turned on
- this family must be protected from over-tuning

### Default-sufficient with unresolved pressure

- `general_line_vs_flow`

Meaning:

- default stays correct for now
- unresolved middle pressure remains
- do not silently upgrade this into a tuning target

### Structurally open bucket

- `conditional-only`

Meaning:

- empty in the current operating rule
- not conceptually deleted
- only reopen through explicit triggers

## Carry-Forward Handle Rule

The three carry-forward classes are now part of operating interpretation.

### actual reroute handle

- may support bounded flow-aware justification

### stable but low-value handle

- may show real flow presence
- does not justify tuning by itself

### mostly formal ref

- do not use as flow-aware justification

## Why Freeze Maintenance Now Comes First

The current structure is already narrow enough to operate with.

What is stable:

- allow-list
- block-list
- protected default rule
- carry-forward operating meaning

What remains open is small enough that broad tuning would create more churn than value.

So the right next stance is:

- maintain the current freeze
- use trigger-based reopening only

## Why Future Change Must Be Trigger-Based

Future change should not begin from:

- generic flow intuition
- family resemblance
- one thin sample
- pressure to keep tuning because the structure is open somewhere

Future change should begin only from bounded trigger evidence.

That means:

- repeated contradiction
- failed current placement
- carry-forward classification drift
- new family evidence that current buckets cannot place honestly

## Current Operating Placement Summary

| Placement | Families |
| --- | --- |
| allow-list | `route_selection`, `operating_cell` |
| block-list | `preprocess_builder`, `preprocess_jung`, `compact_title_only` |
| keep default-sufficient | `raw_intake_gap` |
| protect as default-sufficient | `input_layer_wrapper` |
| default-sufficient with unresolved pressure | `general_line_vs_flow` |
| structurally open bucket | `conditional-only` |
