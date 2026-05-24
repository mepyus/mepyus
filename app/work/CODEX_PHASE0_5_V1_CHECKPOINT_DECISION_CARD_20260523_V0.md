# CODEX_PHASE0_5_V1_CHECKPOINT_DECISION_CARD_20260523_V0

status: USER_DECISION_SURFACE_WITH_HOLD
date: 2026-05-23

## Verdict

PHASE0_5_V1_CHECKPOINT_DECISION_READY_WITH_HOLD

## Current Position

Phase 0.5 has two valid but different readings:

1. Frozen v0 snapshot identity
   - current verdict: `FAIL_REPLAY_MISMATCH`
   - meaning: the live files no longer match the original v0 snapshot byte-for-byte

2. Current live local safety
   - current verdict: `PASS_LIVE_SAFETY_INVARIANTS_WITH_HOLD`
   - meaning: current live DB still has no fail events, no authority mutations, and no non-HOLD reviews

These should not be collapsed.

## Decision Needed

Should VectorFL create a new `phase0_5_candidate_baseline_v1` checkpoint from the current live local state?

## Option A: Do Not Create v1 Yet

Meaning:

- Keep v0 as the only snapshot.
- Use `--mode live-safety` for current safety checks.
- Keep frozen replay failure as an honest drift signal.

Best when:

- more patches are expected soon
- user wants to avoid checkpoint churn
- current state is still too active

Result:

```text
NO_NEW_SNAPSHOT__CONTINUE_LIVE_SAFETY_WITH_HOLD
```

## Option B: Create v1 Candidate Checkpoint

Meaning:

- Keep v0 untouched.
- Create new folder:

```text
app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v1/
```

- Record current live files and DB facts.
- Create receipt/export.
- Do not promote.
- Do not mark Program Alpha.

Best when:

- test-isolation patch is accepted as current stable local state
- user wants a clean current checkpoint
- later work should compare against post-isolation state

Result:

```text
CREATE_PHASE0_5_CANDIDATE_BASELINE_V1_WITH_HOLD
```

## Option C: Wait For Gemini Gap Scan First

Meaning:

- Send Gemini bounded gap scan first.
- Ask Gemini to look for more shared-state / baseline drift risks.
- Decide v1 checkpoint after broad scan.

Best when:

- user wants more confidence before checkpointing
- Gemini access is available
- the team wants broader internal archaeology before locking current state

Result:

```text
WAIT_FOR_GEMINI_PROGRAM_SPINE_GAP_SCAN_WITH_HOLD
```

## Codex Recommendation

Recommended default:

```text
OPTION_A_NOW__OPTION_B_AFTER_ONE_MORE_STABLE_PATCH_OR_USER_APPROVAL
```

Reason:

We just changed the validator semantics and test isolation. A v1 checkpoint is useful, but it is better after one short steady-state cycle:

- live-safety PASS
- Phase 1 tests PASS
- no new mutable probe run against shared DB
- user explicitly accepts current live state as a checkpoint

## Stable Cycle Update

One deterministic stable cycle has now passed:

```text
PASS_PHASE1_DETERMINISTIC_STABLE_CYCLE_WITH_HOLD
```

Receipt:

```text
app/work/vectorfl_ops_phase_1_web_mvp_skeleton/receipts/phase1_deterministic_stable_cycle_receipt.md
```

This satisfies the technical "one short steady-state cycle" evidence condition, but it does not itself create or approve a v1 checkpoint.

Updated recommendation:

```text
OPTION_B_IS_NOW_TECHNICALLY_READY_WITH_HOLD__USER_APPROVAL_STILL_REQUIRED
```

## Preflight Lane

Before creating v1, run the read-only preflight:

```text
python3 app/work/vectorfl_ops_phase_0_5/tools/phase0_5_candidate_baseline_v1_preflight.py
```

Expected verdict:

```text
PASS_PHASE0_5_CANDIDATE_BASELINE_V1_PREFLIGHT_WITH_HOLD
```

This preflight writes receipt/export only. It does not create `phase0_5_candidate_baseline_v1`.

Current preflight result:

```text
PASS_PHASE0_5_CANDIDATE_BASELINE_V1_PREFLIGHT_WITH_HOLD
candidate_file_count=69
problem_count=0
v1_snapshot_already_exists=false
```

Updated decision state:

```text
OPTION_B_PREFLIGHT_PASS_WITH_HOLD__EXECUTION_STILL_REQUIRES_EXPLICIT_USER_APPROVAL
```

## Guarded Creator

Guarded creator:

```text
app/work/vectorfl_ops_phase_0_5/tools/phase0_5_candidate_baseline_v1_snapshot.py
```

Default behavior:

```text
HOLD_CONFIRM_OPTION_B_REQUIRED
v1_snapshot_creation=NO
```

Actual v1 creation requires:

```text
--confirm-option-b
```

## If User Chooses Option B

Use Hermes packet:

```text
app/work/space-skill-sandbox/relay/packets/to_hermes/hermes_phase0_5_candidate_baseline_v1_checkpoint_20260523_v0.md
```

## HOLD

- authority mutation: NO
- promotion: HOLD
- Program Alpha claim: NO
- M3/M4 claim: NO
- router/runner claim: NO
- external model/tool/network expansion: NO
- v1 snapshot creation: HOLD until explicit user selection
- baseline/schema/registry mutation: NO beyond approved candidate checkpoint

## Next Smallest Action

Wait for user decision:

- Option A: no v1 yet
- Option B: create v1 candidate checkpoint with HOLD
- Option C: run Gemini gap scan first
