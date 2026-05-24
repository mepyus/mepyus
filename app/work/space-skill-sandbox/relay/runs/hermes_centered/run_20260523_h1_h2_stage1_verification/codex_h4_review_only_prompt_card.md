# CODEX_REVIEW_ONLY_PROMPT_CARD_H4_HERMES_CENTERED_STAGE1_20260523_V0

status: CODEX_REVIEW_ONLY_PROMPT_WITH_HOLD

## Purpose

Ask Codex to perform H4 review-only structural guard review of the Hermes-centered H1/H2 run.

Codex must not mutate files unless separately approved by the user. This is review-only.

## read_before_work
- `app/work/VECTORFL_PROGRAM_SPINE_STATUS_CARD_20260523_V0.md`
- `app/work/VECTORFL_PERSONAL_PROGRAM_UNIT_POSITION_AND_BUILDUP_20260523_V0.md`
- `app/work/VECTORFL_PERSONAL_PROGRAM_UNIT_CONTRACT_20260523_V0.md`
- `app/work/HERMES_CENTERED_CODEX_GEMINI_OPERATING_LOOP_CONTRACT_20260523_V0.md`
- `app/work/HERMES_CENTERED_EXECUTION_WORKLIST_20260523_V0.md`
- `app/work/TOOL_SPACE_REENTRY_INSTRUCTION_20260523_V0.md`
- `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_h1_h2_stage1_verification/run_brief.md`
- `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_h1_h2_stage1_verification/commands_run.md`
- `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_h1_h2_stage1_verification/tool_calls.md`
- `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_h1_h2_stage1_verification/outputs_summary.md`
- `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_h1_h2_stage1_verification/receipt.md`

## Review Scope

Codex should review only:

1. Whether H1 run folder was created with required files.
2. Whether H2 Stage 1 verification was actually rerun from Hermes.
3. Whether commands/results support the claimed verdict.
4. Whether shared DB unchanged check is sufficient for this step.
5. Whether any overclaim/promotion/authority drift appears.
6. Whether the next smallest action should be H3 Gemini gap scan, H5 live intake gate, or a smaller read-only surface check.

## Required Return Shape

Codex must return:

```text
verdict:
read_before_work:
files_touched:
commands_run:
receipts_created_or_updated:
state_mutations_observed:
WATCH:
HOLD:
next_smallest_action:
```

## Classification Labels Allowed

```text
PASS_REVIEW_ONLY_WITH_HOLD
WATCH_REVIEW_ONLY_NEEDS_REPAIR
STOP_BOUNDARY_DRIFT
```

## Forbidden Claims

Codex must not claim:

- authority mutation approval
- promotion
- Program Alpha readiness
- M3/M4 confirmation
- router/runner implementation
- live DB intake approval
- v1 snapshot creation approval
- Gemini execution occurred
- external model/tool/network bridge is now operational

## Current Hermes Evidence Under Review

Primary receipt:

```text
app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_h1_h2_stage1_verification/receipt.md
```

Hermes verdict under review:

```text
PASS_HERMES_CENTERED_H1_H2_STAGE1_VERIFICATION_WITH_HOLD
```

## HOLD

- authority mutation: NO
- promotion: HOLD
- Program Alpha claim: NO
- M3/M4 claim: NO
- router/runner claim: NO
- external model/tool/network expansion: NO
- live DB intake: HOLD
- v1 snapshot creation: HOLD
- write UI: NO
