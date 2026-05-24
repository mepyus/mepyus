# Codex Review-Only Task Packet
# FILLED_INSTANCE_EXECUTION_V0_CONTRACT_SHAPE_REVIEW_ONLY

## 1. Task Type

Review-only contract shape validation.

Do not execute Gemini.
Do not execute Codex recovery.
Do not perform Hermes dispatch.
Do not call model APIs beyond the already-approved review context if this prompt is manually pasted into Codex by the user.
Do not use live web/source lookup.
Do not use external connector.
Do not mutate VectorFL authority.
Do not promote anything.
Do not modify any files.

## 2. Purpose

Validate whether the execution candidate packet shape can survive the step immediately before real execution.
This is not execution.
This is not dispatch approval.
This is not promotion approval.

## 3. Target Packet

Read only this target packet for the primary review:

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0.md
```

Optional shape-reference files, read-only if needed:

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/GEMINI_PROMPT_EXECUTION_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/CODEX_RECOVERY_PROMPT_EXECUTION_V0.md
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/HERMES_EXECUTION_RECEIPT_CONTRACT_V0.json
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/HERMES_EXECUTION_REPORT_CONTRACT_V0.md
```

## 4. Non-Action Boundaries

```text
real Gemini execution: HOLD
real Codex recovery execution: HOLD
Hermes dispatch: HOLD
model API transport for bridge execution: HOLD
live web/source lookup: HOLD
external connector: HOLD
browser/MCP: HOLD
memory/skill/cron/config mutation: HOLD
VectorFL authority mutation: HOLD
promotion: HOLD
component/workflow/schema/registry/ontology/baseline: HOLD
AGENTS.md / SKILL.md: HOLD
current-position / output_manifest: HOLD
```

## 5. Review Checklist

Check only contract shape:

```text
1. EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET is no.
2. APPROVED_PROMOTION is no.
3. target packet is execution_prep_only.
4. dry-run directory is referenced as proof and protected from mutation.
5. Gemini raw stdout materialization path is explicit.
6. Gemini lite JSON materialization path is explicit.
7. Gemini lite JSON required keys are explicit.
8. Gemini completion signal is GEMINI_LITE_OUTPUT_DONE.
9. Codex 4-input recovery contract is explicit.
10. Codex reads filled packet, gemini_lite_output.json, gemini_raw_output.txt, receipt contract.
11. Codex output path is explicit and single.
12. proposed commands are clearly non-approved while approval is no.
13. STOP conditions cover premature execution, missing materialization, missing validation, authority mutation, and promotion.
14. boundary distinctions are explicit:
    command exists in packet != execution approval
    execution approval != promotion approval
    Gemini output != truth
    Codex recovery != authority mutation
    Hermes success != VectorFL approval
15. final line preserves no execution/no promotion/candidate status.
```

## 6. Failure Conditions

Return STOP if any of these are true:

```text
approval defaults are ambiguous
EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET is yes
APPROVED_PROMOTION is yes
Gemini output file materialization is not explicit
Gemini lite JSON validation is not explicit
Codex 4-input contract is missing or indirect
Codex can read broad repo/source by implication
Codex can write outside declared output
proposed command can be mistaken as current approval
receipt/report can be mistaken as VectorFL authority
promotion path is implied
VectorFL authority mutation is allowed or ambiguous
dry-run proof can be modified
```

## 7. Required Return Format

Return only a compact review report:

```text
verdict:
files_reviewed:
shape_validity:
contract_gaps:
gemini_materialization_check:
codex_4_input_check:
approval_boundary_check:
promotion_boundary_check:
VectorFL_authority_boundary_check:
WATCH:
HOLD:
next_smallest_action:
hard_stop_confirmation:
```

## 8. Required Verdicts

If valid:

```text
FILLED_INSTANCE_EXECUTION_V0_CONTRACT_SHAPE_REVIEW_READY_WITH_EXECUTION_HOLD
```

If invalid:

```text
FILLED_INSTANCE_EXECUTION_V0_CONTRACT_SHAPE_REVIEW_STOP
```

## 9. Required Hard Stop Confirmation

```text
No Gemini execution was performed.
No Codex recovery execution was performed.
No Hermes dispatch was performed.
No promotion was performed.
No VectorFL authority mutation was performed.
```
