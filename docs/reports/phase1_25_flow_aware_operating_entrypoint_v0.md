# Phase 1.25 Flow-Aware Operating Entrypoint v0

## Purpose

This document is the single entry surface for the current flow-aware operating rule.

Use it first.
Then follow the linked operating documents in order.

This is not a tuning document.
This is not a reopening document.

## Current Locked Outcome

### Allow-list

- `route_selection`
- `operating_cell`

### Block-list

- `preprocess_builder`
- `preprocess_jung`
- `compact_title_only`

### Keep default

- `raw_intake_gap`

### Protect as default

- `input_layer_wrapper`

### Default with unresolved pressure

- `general_line_vs_flow`

### Structurally open bucket

- `conditional-only`

## Current Operating Rule at a Glance

- keep global default selection
- allow bounded flow-aware only in allow-list families
- block flow-aware in block-list families
- keep `raw_intake_gap` on default
- protect `input_layer_wrapper` from over-tuning
- keep `general_line_vs_flow` on default while leaving unresolved pressure explicit
- do not reopen unresolved items without trigger evidence

## Why Operation Comes First Now

The current rule is already narrow enough to use.

What is stable:

- allow-list
- block-list
- protected default
- carry-forward operating meaning

What remains open is small and specific.

So the right stance now is:

- use the current rule
- reopen only when a trigger appears

## Read Order

1. this entrypoint
   - [phase1_25_flow_aware_operating_entrypoint_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_operating_entrypoint_v0.md)
2. operating map
   - [phase1_23_flow_aware_operating_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_23_flow_aware_operating_map_v0.md)
3. operator quick reference
   - [phase1_24_flow_aware_operator_quick_reference_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_24_flow_aware_operator_quick_reference_v0.md)
4. reader/operator index
   - [phase1_25_flow_aware_reader_operator_index_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_reader_operator_index_v0.md)
5. protected default guard
   - [phase1_23_flow_aware_protected_default_guard_note_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_23_flow_aware_protected_default_guard_note_v0.md)
6. unresolved hold
   - [phase1_23_flow_aware_unresolved_hold_note_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_23_flow_aware_unresolved_hold_note_v0.md)
7. trigger checklist
   - [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)

## Reopen Rule

Do not reopen because:

- flow exists somewhere
- unresolved pressure remains
- a family resembles an allow-list family
- more tuning feels attractive

Reopen only from explicit trigger evidence.

If no trigger exists:

- keep the current placement
- do not restart broad tuning
