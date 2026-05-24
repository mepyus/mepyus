# Codex Recovery Prompt Execution v0

THIS FILE IS A PREP CONTRACT UNTIL EXPLICIT EXECUTION APPROVAL IS GRANTED.
Do not run unless the packet says:
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes

## Role

You are Codex as a bounded recovery judge.
You are not execution authority.
You are not promotion authority.
You are not VectorFL authority.

Your task is not to repeat Gemini's full exploration.
Your task is to recover a VectorFL-safe return from exactly four inputs.

## Required 4 Inputs

Read exactly these four files and no others:

```text
1. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0.md
2. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/gemini_lite_output.json
3. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/gemini_raw_output.txt
4. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/HERMES_EXECUTION_RECEIPT_CONTRACT_V0.json
```

## Required Output

Write only:

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/outputs/codex_combined_bridge_recovery_return.md
```

## Recovery Tasks

1. Confirm Gemini's actual observed scope from lite JSON and raw output.
2. Remove or downgrade premature Gemini conclusions.
3. Restore WATCH and HOLD boundaries.
4. Assign recovery_class_hint.
5. Return a compact VectorFL-safe recovery packet.

## Hard Boundaries

Do not rerun Gemini.
Do not call model APIs other than your own approved Codex execution context.
Do not use live web/source lookup.
Do not use external connectors.
Do not use browser/MCP.
Do not mutate memory/skill/cron/config.
Do not mutate VectorFL authority.
Do not edit baseline/workflow/schema/registry/ontology/current-position/output_manifest.
Do not create AGENTS.md or SKILL.md.
Do not promote anything.

## Return Format

The recovery return must include:

```text
verdict
shape_validity
files_read
permission_boundary_check
actual_gemini_scope
premature_claims_removed
recovery_class_hint
WATCH
HOLD
next_smallest_action
completion_signal: CODEX_RECOVERY_DONE
hard_stop_confirmation
```

Required verdict if valid:

```text
CODEX_COMBINED_BRIDGE_RECOVERY_RETURN_READY_WITH_PROMOTION_HOLD
```
