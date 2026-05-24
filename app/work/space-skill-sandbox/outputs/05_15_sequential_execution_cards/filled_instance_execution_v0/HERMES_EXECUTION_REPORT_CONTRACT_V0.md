# Hermes Execution Report Contract v0

## Verdict

```text
FILLED_INSTANCE_EXECUTION_V0_PREPARED_WITH_EXECUTION_HOLD
```

## Purpose

This report contract defines how Hermes must close an approved future execution of the bounded combined bridge execution candidate.
At the current prep stage, this file is a contract only.

## Source Proof Preservation

```text
dry_run_reference: /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/template_instance_dry_run_v0/
dry_run_mutation_allowed: no
```

## Required Prep Confirmation

```text
execution_prep_only: yes
real_gemini_execution: no
real_codex_execution: no
model_api_transport_used: no
promotion_performed: no
vectorfl_authority_mutation: no
```

## Required Future Execution Report Sections

If execution is later explicitly approved, Hermes must report:

```text
verdict
files inspected
files created/modified
execution approval source
Gemini raw stdout path
Gemini lite JSON path
Gemini lite JSON validation result
Codex 4-input recovery result path
receipt negative evidence
what was carried over from dry-run
what was fixed for real-execution readiness
WATCH
HOLD
next smallest action
hard stop confirmation
```

## Required Future Receipt Fields

```text
real_gemini_executed
real_codex_executed
model_api_transport_used
live_web_lookup_used
external_connector_used
browser_used
mcp_used
memory_modified
skill_modified
cron_modified
config_modified
vectorfl_authority_modified
promotion_performed
dry_run_directory_modified
gemini_raw_output_written
gemini_lite_output_written
gemini_lite_required_keys_present
gemini_lite_completion_signal_valid
codex_four_inputs_declared
codex_recovery_return_written
codex_completion_signal_valid
```

## WATCH

```text
filled packet mistaken for dispatch approval
command in packet mistaken for execution
Gemini stdout not materialized
Gemini lite JSON not validated
Codex recovery prompt missing declared inputs
Gemini conclusion treated as truth
Codex recovery treated as authority update
Hermes receipt treated as approval
dry-run directory modified
execution_v0 prep mistaken as real run
```

## HOLD

```text
real Gemini execution before approval
real Codex execution before approval
model API transport before approval
live web/source lookup
external connector
browser/MCP
memory/skill/cron/config mutation
VectorFL authority mutation
promotion
component/workflow/schema/registry/ontology/baseline
AGENTS.md / SKILL.md
current-position / output_manifest
```

## Required Final Line

```text
No execution was performed. No promotion was performed. Recovery class remains candidate.
```
