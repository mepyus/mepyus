# TOOL_SPACE_REENTRY_INSTRUCTION_20260523_V0

status: CROSS_TOOL_REENTRY_INSTRUCTION_WITH_HOLD
date: 2026-05-23

## Verdict

TOOLS_MUST_USE_SHARED_SPACE_AS_MEMORY_NOT_PRIVATE_MODEL_MEMORY

## Purpose

Codex, Gemini, and Hermes must be able to understand each other's work without private learning or hidden memory.

The shared repo/Obsidian space is the source of truth.

## Core Rule

Before any tool acts, it must read the current shared-space anchors relevant to the task.

Do not rely on:

- prior chat memory
- model memory
- unstated assumptions
- tool-specific private context

## Universal Re-Entry Read List

Every tool starts with:

```text
app/work/VECTORFL_PROGRAM_SPINE_STATUS_CARD_20260523_V0.md
app/work/VECTORFL_PERSONAL_PROGRAM_UNIT_POSITION_AND_BUILDUP_20260523_V0.md
app/work/VECTORFL_PERSONAL_PROGRAM_UNIT_CONTRACT_20260523_V0.md
app/work/HERMES_CENTERED_CODEX_GEMINI_OPERATING_LOOP_CONTRACT_20260523_V0.md
app/work/HERMES_CENTERED_EXECUTION_WORKLIST_20260523_V0.md
```

When working on personal intake:

```text
app/work/CODEX_REVIEW_PERSONAL_INTAKE_MIN_IMPLEMENTATION_20260523_V0.md
app/work/vectorfl_ops_phase_0_5/tools/personal_intake_min.py
app/work/vectorfl_ops_phase_0_5/tests/test_personal_intake_min.py
```

When working on Phase 1 surface:

```text
app/work/vectorfl_ops_phase_1_web_mvp_skeleton/README.md
app/work/vectorfl_ops_phase_1_web_mvp_skeleton/receipts/phase1_deterministic_stable_cycle_receipt.md
```

When working on v1 checkpoint:

```text
app/work/CODEX_PHASE0_5_V1_CHECKPOINT_DECISION_CARD_20260523_V0.md
app/work/vectorfl_ops_phase_0_5/receipts/phase0_5_candidate_baseline_v1_preflight_receipt.md
app/work/CODEX_REVIEW_PHASE0_5_V1_GUARDED_CREATOR_STAGED_20260523_V0.md
```

## Tool Return Requirement

Every tool return must include:

```text
read_before_work:
files_touched:
commands_run:
receipts_created_or_updated:
state_mutations_observed:
WATCH:
HOLD:
next_smallest_action:
```

## Location Card Requirement

If a run changes the working position, create or update a location/status card.

Recommended path:

```text
app/work/space-skill-sandbox/relay/runs/hermes_centered/<run>/receipt.md
```

If the change is global, update:

```text
app/work/VECTORFL_PROGRAM_SPINE_STATUS_CARD_20260523_V0.md
```

Only update global cards with evidence-backed facts.

## Codex Re-Entry Instruction

Codex should read the universal list, then classify:

```text
implementation
prototype
candidate material
residue
WATCH
STOP
```

Codex must explicitly check for:

- overclaim
- missing tests
- authority mutation
- promotion drift
- router/runner drift
- M3/M4 drift

## Gemini Re-Entry Instruction

Gemini should read the universal list plus task packet.

Gemini returns broad findings only, classified as:

```text
READY_FOR_CONTRACT
CANDIDATE_MATERIAL
WATCH
STOP
OUT_OF_SCOPE
```

Gemini must list:

- files/assets read
- assets not inspected
- confidence and gaps

Gemini must not write repo files unless separately wrapped by Hermes and approved.

## Hermes Re-Entry Instruction

Hermes should read the universal list plus worklist item.

Hermes executes only bounded tasks.

Hermes must write:

```text
commands_run.md
receipt.md
outputs_summary.md
```

Hermes must record whether shared state changed.

## State Mutation Labels

Use these labels:

```text
NO_MUTATION
FIXTURE_ONLY_MUTATION
RECEIPT_ONLY_MUTATION
CODE_PATCH_MUTATION
SHARED_DB_MUTATION
SNAPSHOT_MUTATION
SCHEMA_MUTATION
AUTHORITY_MUTATION
PROMOTION_MUTATION
```

`AUTHORITY_MUTATION` and `PROMOTION_MUTATION` require explicit user approval and should normally be STOP.

## Forbidden Cross-Tool Assumptions

Do not say:

- Gemini found it, therefore it is true
- Codex reviewed it, therefore it is promoted
- Hermes executed it, therefore it is authority
- a receipt exists, therefore M3/M4 is confirmed
- a script exists, therefore router/runner exists

## HOLD

- authority mutation: NO
- promotion: HOLD
- Program Alpha claim: NO
- M3/M4 claim: NO
- router/runner claim: NO
- external model/tool/network expansion: NO unless separately packeted

## One-Line Instruction

```text
Every tool re-enters through the shared space, works inside a packet, writes a receipt, and leaves promotion/authority on HOLD.
```
