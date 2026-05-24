# HERMES_CENTERED_EXECUTION_WORKLIST_20260523_V0

status: EXECUTION_WORKLIST_WITH_HOLD
date: 2026-05-23

## Verdict

HERMES_WORKLIST_READY_FOR_STAGE1_PERSONAL_PROGRAM_BUILDUP_WITH_HOLD

## Current Target

```text
VECTORFL_PERSONAL_LOCAL_PROGRAM_UNIT_V0
```

Current achieved state:

```text
personal_intake_min.py implemented and fixture-tested
live DB intake not executed
read-only Phase 1 stable cycle PASS
```

## Work Item H1. Establish Hermes-Centered Run Folder

Status:

```text
READY
```

Goal:

Create:

```text
app/work/space-skill-sandbox/relay/runs/hermes_centered/
```

and a first run folder for the current Stage 1 buildup.

Required files:

```text
run_brief.md
commands_run.md
tool_calls.md
outputs_summary.md
receipt.md
```

HOLD:

- no code mutation required
- no authority mutation
- no promotion

## Work Item H2. Re-Run Stage 1 Verification From Hermes

Status:

```text
READY
```

Commands:

```bash
python3 app/work/vectorfl_ops_phase_0_5/tests/test_personal_intake_min.py
python3 app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tools/phase1_deterministic_stable_cycle.py
python3 app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py --mode live-safety
python3 app/work/vectorfl_ops_phase_0_5/tools/phase0_5_candidate_baseline_v1_preflight.py
```

Expected:

```text
test_personal_intake_min.py PASS
PASS_PHASE1_DETERMINISTIC_STABLE_CYCLE_WITH_HOLD
PASS_LIVE_SAFETY_INVARIANTS_WITH_HOLD
PASS_PHASE0_5_CANDIDATE_BASELINE_V1_PREFLIGHT_WITH_HOLD
```

Receipt:

```text
app/work/space-skill-sandbox/relay/runs/hermes_centered/<run>/receipt.md
```

## Work Item H3. Gemini Personal Program Gap Scan

Status:

```text
READY_WHEN_GEMINI_SESSION_AVAILABLE
```

Packet:

```text
app/work/space-skill-sandbox/relay/packets/to_gemini/gemini_personal_program_unit_gap_scan_20260523_v0.md
```

Expected return:

```text
gemini_gap_scan_return.md
```

HOLD:

- review-only exploration
- no repo mutation
- no promotion

## Work Item H4. Codex Review Of Hermes-Centered Setup

Status:

```text
READY_AFTER_H1_H2
```

Goal:

Ask Codex to review:

- Hermes run receipt
- commands_run
- worklist alignment
- overclaim risk
- next smallest action

Return:

```text
codex_review_return.md
```

HOLD:

- review-only
- no authority mutation
- no promotion

## Work Item H5. Live Personal Intake Approval Gate

Status:

```text
NOT_READY_UNTIL_USER_APPROVES_LIVE_DB_MUTATION
```

Goal:

Prepare, but do not execute, a live DB personal intake command.

Preconditions:

- H2 verification PASS
- user explicitly approves live DB mutation
- command is recorded before execution
- post-run live-safety is required

Forbidden until approval:

- inserting personal intake into shared DB
- changing v1 snapshot state
- claiming production app behavior

## Work Item H6. Read-Only Personal Intake Surface Check

Status:

```text
READY_AFTER_LIVE_INTAKE_OR_FIXTURE_SURFACE_DECISION
```

Goal:

Confirm whether Phase 1 read-only UI/API clearly surfaces `PERSONAL_INTAKE` records.

Possible outputs:

- UI already sufficient
- add read-only label/filter
- defer until live intake exists

HOLD:

- no write UI
- no schema mutation unless separately approved

## Work Item H7. V1 Candidate Checkpoint

Status:

```text
TECHNICALLY_READY_BUT_HELD
```

Tool:

```text
app/work/vectorfl_ops_phase_0_5/tools/phase0_5_candidate_baseline_v1_snapshot.py
```

Required explicit flag:

```text
--confirm-option-b
```

Default behavior:

```text
HOLD_CONFIRM_OPTION_B_REQUIRED
v1_snapshot_creation=NO
```

Do not execute unless user explicitly approves v1 checkpoint creation.

## Work Item H8. Update Status Cards

Status:

```text
READY_AFTER_EACH_COMPLETED_HERMES_RUN
```

Allowed updates:

- append evidence-backed status
- link receipts
- update WATCH
- update next smallest action

Forbidden:

- promotion
- authority mutation
- M3/M4 claim
- router/runner claim
- Program Alpha claim

## Priority Order

Recommended order:

```text
H1 -> H2 -> H3 -> H4 -> H5/H6 decision -> H7 only if explicitly approved
```

## HOLD

- authority mutation: NO
- promotion: HOLD
- Program Alpha claim: NO
- M3/M4 claim: NO
- router/runner claim: NO
- external model/tool/network expansion: NO unless separately packeted
- live DB mutation: HOLD
- v1 snapshot creation: HOLD
- write UI: NO
