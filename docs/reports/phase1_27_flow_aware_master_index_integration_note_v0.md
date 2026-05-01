# Phase 1.27 Flow-Aware Master Index Integration Note v0

## Purpose

This note places the current flow-aware operating set inside the larger runtime/reading master index.

It does not reopen the rule.
It connects the existing rule to a stable entry path.

## Core Operating Set

The active flow-aware operating set is:

- [phase1_25_flow_aware_operating_entrypoint_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_operating_entrypoint_v0.md)
- [phase1_25_flow_aware_reader_operator_index_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_reader_operator_index_v0.md)
- [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)
- [phase1_26_flow_aware_cross_reference_note_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_26_flow_aware_cross_reference_note_v0.md)
- [phase1_26_flow_aware_runtime_index_connection_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_26_flow_aware_runtime_index_connection_v0.md)
- [phase1_26_flow_aware_reopen_path_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_26_flow_aware_reopen_path_map_v0.md)

## Position In The Larger Reading / Runtime Context

### Lower

Lower-side camera support belongs before this operating set.

Use lower references when the question is:

- how camera support is shaped
- how lower support artifacts are emitted

Then move into the flow-aware operating entrypoint.

### Upper

Upper bounded reread consumes the lower support outputs.
This operating set belongs here.

Meaning:

- after lower support emission
- before any future lens/axis work
- before any reopen attempt

### Reader

Reader-side use starts from:

1. operating entrypoint
2. reader/operator index
3. trigger checklist

### Operator

Operator-side use starts from:

1. operating entrypoint
2. operator index
3. trigger checklist
4. reopen path map only if a trigger exists

## Operator Entry Order

1. [phase1_25_flow_aware_operating_entrypoint_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_operating_entrypoint_v0.md)
2. [phase1_25_flow_aware_reader_operator_index_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_reader_operator_index_v0.md)
3. [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)
4. [phase1_26_flow_aware_reopen_path_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_26_flow_aware_reopen_path_map_v0.md) only if a trigger exists

## Codex Entry Order

1. [phase1_25_flow_aware_operating_entrypoint_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_operating_entrypoint_v0.md)
2. [phase1_23_flow_aware_operating_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_23_flow_aware_operating_map_v0.md)
3. [phase1_25_flow_aware_reader_operator_index_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_reader_operator_index_v0.md)
4. [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)
5. [phase1_26_flow_aware_reopen_path_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_26_flow_aware_reopen_path_map_v0.md) only if a trigger exists

## Current Frozen Placement

- allow-list
  - `route_selection`
  - `operating_cell`
- block-list
  - `preprocess_builder`
  - `preprocess_jung`
  - `compact_title_only`
- keep default-sufficient
  - `raw_intake_gap`
- protect as default-sufficient
  - `input_layer_wrapper`
- default-sufficient with unresolved pressure
  - `general_line_vs_flow`
- structurally open
  - `conditional-only`

## Broad Reopen Guard

Keep the current operating set in place until explicit trigger evidence exists.

Without trigger evidence:

- do not reopen families broadly
- do not reopen selection tuning
- do not reopen emitter/classifier/schema work
