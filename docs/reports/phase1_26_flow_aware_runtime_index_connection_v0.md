# Phase 1.26 Flow-Aware Runtime Index Connection v0

## Runtime / Reading Index Connection Text

Use the following wording when connecting the flow-aware rule into a higher runtime or reading index.

> The current flow-aware rule is frozen at global default-first operation.  
> Bounded flow-aware selection is allowed only for allow-list families.  
> Block-list families remain default-only.  
> Protected default and unresolved hold remain in place unless trigger evidence appears.  
> Reopen is trigger-based only.

## Operator Entry Order

1. [phase1_25_flow_aware_operating_entrypoint_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_operating_entrypoint_v0.md)
2. [phase1_25_flow_aware_reader_operator_index_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_reader_operator_index_v0.md)
3. [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)

## Codex / Reader Entry Order

1. [phase1_25_flow_aware_operating_entrypoint_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_operating_entrypoint_v0.md)
2. [phase1_23_flow_aware_operating_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_23_flow_aware_operating_map_v0.md)
3. [phase1_25_flow_aware_reader_operator_index_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_reader_operator_index_v0.md)
4. [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)

## Before Any Future Tuning

Always re-read:

- [phase1_23_flow_aware_heuristic_lock_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_23_flow_aware_heuristic_lock_v0.md)
- [phase1_24_flow_aware_closeout_consolidation_note_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_24_flow_aware_closeout_consolidation_note_v0.md)
- [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)

## Connection Summary

The flow-aware rule now sits in the runtime/reading stack as:

- lower support already emitted
- upper bounded reread already validated
- reader-side selection already bounded
- operator-facing rule already frozen provisionally

So the active runtime stance is:

- maintain default
- use allow-list only where proven
- reopen only through trigger path
