# Phase 1.31 Flow-Aware Trigger and Log Card v0

## Trigger Rule

If no trigger exists:

- do not reopen
- do not log
- keep the current placement

## Trigger Path

When a trigger exists, use this order:

1. [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)
2. [phase1_26_flow_aware_reopen_path_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_26_flow_aware_reopen_path_map_v0.md)
3. [phase1_27_flow_aware_evidence_log_template_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_27_flow_aware_evidence_log_template_v0.md)
4. [phase1_27_flow_aware_reopen_permission_boundary_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_27_flow_aware_reopen_permission_boundary_v0.md)

## Log Location

- [flow_aware](/Users/sungsookim/universe/vectorfl_replica/runtime/reopen_evidence_logs/flow_aware)

## Log Naming

- `YYYYMMDD_<family>_<trigger-type>_<reopen-scope>_<short-slug>.md`

## Log Scope

Use one file per incident.

Allowed:

- family-level reopen request
- bucket-level reopen request

Not allowed:

- global reopen request
- tuning restart note
- emitter/classifier/schema reopen request

## What The Log Is

- bounded reopen request
- trigger-based note

## What The Log Is Not

- reopen decision
- broad tuning document
- generic idea note

## Broad Reopen Guard

Even with a trigger:

- reopen only the affected family or bucket
- do not reopen allow-list / block-list globally
- do not skip the evidence log
