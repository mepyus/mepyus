# CODEX_REVIEW_BASELINE_REPLAY_VALIDATOR_MODE_SPLIT_20260523_V0

status: REVIEW_ONLY_VERIFICATION_WITH_HOLD
date: 2026-05-23

## Verdict

PASS_CODEX_REVIEW_BASELINE_REPLAY_VALIDATOR_MODE_SPLIT_WITH_HOLD

## Scope Reviewed

Applied mode split within packet scope:

- `app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py`
- `app/work/vectorfl_ops_phase_0_5/BASELINE_REPLAY_VALIDATOR.md`

Related packet:

- `app/work/space-skill-sandbox/relay/packets/to_hermes/hermes_baseline_replay_validator_mode_split_20260523_v0.md`

## What Changed

The validator now separates two questions:

- `--mode frozen`: strict byte-identity replay against the v0 snapshot.
- `--mode live-safety`: current DB safety invariant check only.

Default remains frozen mode.

Live-safety writes separate outputs:

- `app/work/vectorfl_ops_phase_0_5/receipts/pipeline_baseline_live_safety_validator_receipt.md`
- `app/work/vectorfl_ops_phase_0_5/exports/pipeline_baseline_live_safety_validator_export.md`

Frozen replay keeps the original outputs:

- `app/work/vectorfl_ops_phase_0_5/receipts/pipeline_baseline_replay_validator_receipt.md`
- `app/work/vectorfl_ops_phase_0_5/exports/pipeline_baseline_replay_validator_export.md`

## Commands Run

```bash
python3 -m py_compile app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py
```

Result: PASS

```bash
python3 app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py --mode live-safety
```

Result:

```text
BASELINE_LIVE_SAFETY_PASS
verdict=PASS_LIVE_SAFETY_INVARIANTS_WITH_HOLD
problem_count=0
```

```bash
python3 app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py --mode frozen
```

Result:

```text
BASELINE_REPLAY_FAIL
checked_files=45
matched_files=39
problem_count=6
watch_count=1
```

Frozen mismatch paths:

- `data/vectorfl_ops_phase_0_5.sqlite`
- `exports/guardrail_probe_negative_results.md`
- `exports/pipeline_transition_table_hardening_export.md`
- `probes/guardrail_probe_runner.py`
- `receipts/guardrail_probe_receipt.md`
- `receipts/pipeline_transition_table_hardening_receipt.md`

## Snapshot Files

Snapshot files were not intentionally modified.

Observed current hashes:

```text
419d8f304b123447b8275b5163f4d34f1bce5ad0e920a3a0be58555af597f83a  app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v0/baseline_manifest.json
36995c145c71c2e6b483c173563ce0cce33b9c4824ab5d0548478d1fdbe6f16b  app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v0/baseline_checksums.tsv
```

## Interpretation

This is the intended split:

- frozen mode remains strict and currently FAILS
- live-safety mode passes current safety invariants
- live-safety PASS is not baseline replay PASS
- no v1 snapshot was created

## WATCH

- Frozen replay failure remains real.
- The validator and documentation changes themselves add another frozen mismatch if those files were part of the original snapshot.
- The original replay receipt/export are still overwritten by frozen mode runs.
- The new live-safety receipt/export are separate and do not claim snapshot replay.
- Snapshot resnapshot/reconciliation remains unperformed.

## HOLD

- authority mutation: NO
- promotion: HOLD
- Program Alpha claim: NO
- M3/M4 claim: NO
- router/runner claim: NO
- external model/tool/network expansion: NO
- v1 snapshot creation: NO
- snapshot mutation: NO
- baseline/schema/registry mutation: NO

## Next Smallest Action

Use `--mode live-safety` for current local safety checks.

Use `--mode frozen` only when asking whether v0 snapshot byte identity still holds.

Do not create `phase0_5_candidate_baseline_v1` until separately approved.
