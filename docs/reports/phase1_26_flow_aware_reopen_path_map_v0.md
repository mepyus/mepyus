# Phase 1.26 Flow-Aware Reopen Path Map v0

## Purpose

This note maps how reopening should happen if trigger evidence appears.

If no trigger exists, stay on the Phase 1.25 operating rule.

## Reopen Path: `general_line_vs_flow`

Trigger examples:

- repeated middle-case evidence
- default repeatedly missing a better local slice
- carry-forward drifting toward actual reroute handle

Read path:

1. [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)
2. [phase1_23_flow_aware_unresolved_hold_note_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_23_flow_aware_unresolved_hold_note_v0.md)
3. [phase1_22_unresolved_boundary_decision_note_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_22_unresolved_boundary_decision_note_v0.md)

Allowed reopen scope:

- this family only
- bounded unresolved check only

## Reopen Path: `raw_intake_gap`

Trigger examples:

- repeated evidence that current default is no longer honest enough
- repeated overreach/noise pressure toward block-list
- carry-forward classification drift

Read path:

1. [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)
2. [phase1_23_flow_aware_unresolved_hold_note_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_23_flow_aware_unresolved_hold_note_v0.md)
3. [phase1_22_unresolved_boundary_decision_note_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_22_unresolved_boundary_decision_note_v0.md)

Allowed reopen scope:

- this family only
- bounded placement recheck only

## Reopen Path: `conditional-only`

Trigger examples:

- repeated clean middle-bucket case
- current buckets failing to place a family honestly
- repeated contradiction between default-sufficient and allow-list

Read path:

1. [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)
2. [phase1_23_flow_aware_unresolved_hold_note_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_23_flow_aware_unresolved_hold_note_v0.md)
3. [phase1_21_flow_aware_unresolved_boundary_note_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_21_flow_aware_unresolved_boundary_note_v0.md)

Allowed reopen scope:

- bucket-level conceptual check only
- no broad family rewrite

## Reopen Path: `input_layer_wrapper`

Trigger examples:

- default repeatedly missing a better local slice
- stable low-value handle drifting toward actual reroute handle
- repeated bounded flow-aware gain beyond current default

Read path:

1. [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)
2. [phase1_23_flow_aware_protected_default_guard_note_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_23_flow_aware_protected_default_guard_note_v0.md)
3. [phase1_22_unresolved_boundary_decision_note_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_22_unresolved_boundary_decision_note_v0.md)

Allowed reopen scope:

- this family only
- protection rule check only

## Broad Reopen Guard

Without trigger evidence:

- keep Phase 1.25 operating placement
- do not reopen allow-list / block-list globally
- do not reopen emitter work
- do not restart broad tuning
