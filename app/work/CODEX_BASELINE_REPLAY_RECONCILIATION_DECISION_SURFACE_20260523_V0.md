# CODEX_BASELINE_REPLAY_RECONCILIATION_DECISION_SURFACE_20260523_V0

status: DECISION_SURFACE_WITH_HOLD
date: 2026-05-23

## Verdict

BASELINE_REPLAY_RECONCILIATION_DECISION_REQUIRED_WITH_HOLD

## Source Basis

Current Phase 0.5 baseline snapshot:

- `app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v0/baseline_manifest.json`
- `app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v0/baseline_checksums.tsv`
- snapshot receipt: `app/work/vectorfl_ops_phase_0_5/receipts/phase0_5_candidate_baseline_snapshot_receipt.md`

Current replay receipt:

- `app/work/vectorfl_ops_phase_0_5/receipts/pipeline_baseline_replay_validator_receipt.md`

Related test isolation patch:

- `app/work/CODEX_REVIEW_PHASE0_5_PHASE1_TEST_ISOLATION_PATCH_RESULT_20260523_V0.md`

## Current State

Baseline replay status:

```text
FAIL_REPLAY_MISMATCH
```

Mismatch type:

- file checksum mismatch: 5 files
- DB fact drift: WATCH

Known current live DB facts:

```json
{
  "requests": 10,
  "executions": 3,
  "receipts": 5,
  "reviews": 4,
  "maturation_entries": 4,
  "guardrail_events": 25,
  "fail_events": 0,
  "authority_mutations": 0,
  "non_hold_reviews": 0,
  "probe_requests": 6
}
```

Known frozen snapshot DB facts:

```json
{
  "requests": 7,
  "executions": 3,
  "receipts": 4,
  "reviews": 4,
  "maturation_entries": 4,
  "guardrail_events": 22,
  "fail_events": 0,
  "authority_mutations": 0,
  "non_hold_reviews": 0,
  "probe_requests": 3
}
```

Safety invariant status:

- fail_events: 0
- authority_mutations: 0
- non_hold_reviews: 0

## Interpretation

The replay mismatch is real.

It does not currently indicate safety failure. It indicates that the Phase 0.5 candidate baseline snapshot is frozen at an earlier local evidence state while live verification residue continued to accumulate.

The correct question is not "make the failure disappear." The correct question is which baseline role the snapshot should play.

## Decision Options

### Option A: Preserve v0 snapshot as frozen origin

Meaning:

- Keep `phase0_5_candidate_baseline_v0` unchanged.
- Keep replay validator strict against v0.
- Accept `FAIL_REPLAY_MISMATCH` as expected once live evidence has drifted.
- Use it as origin integrity evidence, not current live-state evidence.

Pros:

- preserves historical baseline truth
- no mutation of snapshot files
- strong guard against silent drift

Cons:

- replay stays red after legitimate local evidence changes
- Phase 1 current-state tests need separate live/invariant checks

Best if:

- user wants historical baseline preservation over green replay

### Option B: Create v1 live candidate baseline snapshot

Meaning:

- Leave v0 untouched.
- Create `phase0_5_candidate_baseline_v1` from current live state.
- Add v1 manifest/checksums/receipt.
- Update or add validator support for selecting snapshot version.

Pros:

- preserves v0 and creates current-state checkpoint
- makes current live replay checkable without erasing history
- fits VectorFL's receipt-first maturation style

Cons:

- requires new snapshot tooling or careful manual generation
- risk of over-reading v1 as promotion unless HOLD labels are strict

Best if:

- user wants a new current local prototype checkpoint after test-isolation patch

### Option C: Split validator into frozen replay and live safety modes

Meaning:

- `frozen_replay`: exact checksum match against a named snapshot.
- `live_safety`: safety invariants only, allows append-only evidence drift.
- `live_checkpoint`: optional snapshot creation only after approval.

Pros:

- accurately represents two different questions
- avoids false pressure to resnapshot
- makes future testing more robust

Cons:

- requires small tool change and docs update
- still needs a later user decision for v1 snapshot

Best if:

- user wants program maturity before new baseline creation

## Codex Recommendation

Recommended next:

```text
OPTION_C_FIRST__SPLIT_VALIDATOR_SEMANTICS_THEN_OPTIONAL_V1_SNAPSHOT
```

Reason:

VectorFL should distinguish:

- "Did the old snapshot remain byte-identical?"
- "Is the current live local loop still safe?"
- "Should we create a new checkpoint?"

Those are separate questions. Merging them is what produced confusing failure pressure.

## Proposed Next Packet

Prepare a Hermes execution packet for:

1. Add a non-mutating `live_safety` mode to baseline replay validation.
2. Keep strict exact replay as default or explicit `--mode frozen`.
3. Do not create v1 snapshot yet.
4. Run:
   - frozen mode: expected FAIL or current mismatch report
   - live safety mode: expected PASS if safety invariants hold

## HOLD

- authority mutation: NO
- promotion: HOLD
- Program Alpha claim: NO
- M3/M4 claim: NO
- router/runner claim: NO
- external model/tool/network expansion: NO
- baseline/schema/registry mutation: NO for Option C
- v1 snapshot creation: HOLD until separately approved

## Next Smallest Action

Create Hermes packet:

`app/work/space-skill-sandbox/relay/packets/to_hermes/hermes_baseline_replay_validator_mode_split_20260523_v0.md`
