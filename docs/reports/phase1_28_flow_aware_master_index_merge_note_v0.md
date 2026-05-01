# Phase 1.28 Flow-Aware Master Index Merge Note v0

## Purpose

This note defines how the current flow-aware operating set should be inserted into the larger runtime/reading master index body.

It does not change the rule.
It fixes where the rule lives and how readers should enter it.

## Master Index Insertion Point

The flow-aware operating set should appear in the master runtime/reading index after:

- lower support artifact references
- bounded reread references

and before:

- any future trigger-based reopen request
- any future tuning package

Meaning:

- lower support comes first
- bounded reread operating rule comes next
- reopen path comes only after trigger evidence exists

## Master Index Body Text Draft

Use the following text as the insertion block in the larger master index.

> The current flow-aware operating rule is frozen at global default-first use.  
> Bounded flow-aware selection is allowed only for allow-list families.  
> Block-list families remain default-only.  
> Protected default and unresolved hold remain in place unless trigger evidence is logged.  
> Reopen is family-level or bucket-level only and must follow the trigger checklist and evidence log path.

## Connected Document Set

### Primary operating entry set

- [phase1_25_flow_aware_operating_entrypoint_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_operating_entrypoint_v0.md)
- [phase1_25_flow_aware_reader_operator_index_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_reader_operator_index_v0.md)
- [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)

### Cross-reference and path set

- [phase1_26_flow_aware_cross_reference_note_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_26_flow_aware_cross_reference_note_v0.md)
- [phase1_26_flow_aware_runtime_index_connection_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_26_flow_aware_runtime_index_connection_v0.md)
- [phase1_26_flow_aware_reopen_path_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_26_flow_aware_reopen_path_map_v0.md)

### Reopen evidence set

- [phase1_27_flow_aware_evidence_log_template_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_27_flow_aware_evidence_log_template_v0.md)
- [phase1_27_flow_aware_reopen_permission_boundary_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_27_flow_aware_reopen_permission_boundary_v0.md)

## Operator Entry Order

1. [phase1_25_flow_aware_operating_entrypoint_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_operating_entrypoint_v0.md)
2. [phase1_25_flow_aware_reader_operator_index_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_reader_operator_index_v0.md)
3. [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)
4. [phase1_26_flow_aware_reopen_path_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_26_flow_aware_reopen_path_map_v0.md) only if a trigger exists
5. [phase1_27_flow_aware_evidence_log_template_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_27_flow_aware_evidence_log_template_v0.md) only if a bounded reopen request is actually needed

## Codex Entry Order

1. [phase1_25_flow_aware_operating_entrypoint_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_operating_entrypoint_v0.md)
2. [phase1_23_flow_aware_operating_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_23_flow_aware_operating_map_v0.md)
3. [phase1_25_flow_aware_reader_operator_index_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_reader_operator_index_v0.md)
4. [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)
5. [phase1_26_flow_aware_reopen_path_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_26_flow_aware_reopen_path_map_v0.md) only if a trigger exists
6. [phase1_27_flow_aware_evidence_log_template_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_27_flow_aware_evidence_log_template_v0.md) only if bounded reopen evidence must be recorded

## Default Reference Path When No Trigger Exists

When no trigger exists, the reference path ends at:

1. operating entrypoint
2. reader/operator index
3. trigger checklist

Do not continue into reopen path or evidence log creation.

## Reference Path When Trigger Exists

When a trigger exists, the path becomes:

1. operating entrypoint
2. trigger checklist
3. reopen path map
4. evidence log template
5. reopen permission boundary

Still keep the scope bounded to the affected family or bucket only.
