# Flow-Aware Reopen Evidence Logs

This directory is only for **trigger-based bounded reopen evidence logs**.

## Use Rule

- do not create a new log unless a trigger actually exists
- do not use this directory for broad reopen requests
- do not use this directory for generic tuning ideas

## File Unit Rule

Use **one file per incident**.

Each file should represent:

- one family-level reopen request, or
- one bucket-level reopen request

## File Naming Rule

Use:

- `YYYYMMDD_<family>_<trigger-type>_<reopen-scope>_<short-slug>.md`

Examples:

- `20260422_general_line_vs_flow_middle_case_pressure_family_recheck_v1.md`
- `20260422_raw_intake_gap_default_rule_contradiction_placement_recheck_v1.md`

## What This File Is

An evidence log is:

- a bounded reopen request
- a trigger-based record
- a family-level or bucket-level note

An evidence log is **not**:

- a reopen decision
- a broad tuning request
- a global heuristic rewrite request

## Read These First

Before writing a log, read:

- [phase1_25_flow_aware_operating_entrypoint_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_operating_entrypoint_v0.md)
- [phase1_25_flow_aware_reader_operator_index_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_reader_operator_index_v0.md)
- [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)

Only if a trigger exists, then also read:

- [phase1_26_flow_aware_reopen_path_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_26_flow_aware_reopen_path_map_v0.md)
- [phase1_27_flow_aware_evidence_log_template_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_27_flow_aware_evidence_log_template_v0.md)
- [phase1_27_flow_aware_reopen_permission_boundary_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_27_flow_aware_reopen_permission_boundary_v0.md)

## Guardrail

Without a trigger:

- do not create a log
- do not reopen anything
- keep the current flow-aware operating placement
