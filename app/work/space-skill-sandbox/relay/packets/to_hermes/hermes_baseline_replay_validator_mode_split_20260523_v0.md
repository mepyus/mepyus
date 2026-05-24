# HERMES_BASELINE_REPLAY_VALIDATOR_MODE_SPLIT_20260523_V0

## 1. Packet Status

packet_id:
  hermes_baseline_replay_validator_mode_split_20260523_v0

status:
  DRAFT_READY_FOR_USER_APPROVAL_BEFORE_HERMES_EXECUTION

target:
  Hermes

role:
  apply exact local validator mode split and run bounded checks

authority:
  patch packet only

not:
  v1 snapshot creation
  snapshot mutation
  authority mutation
  promotion
  Program Alpha evidence
  M3/M4 confirmation
  router/runner implementation
  external model/tool/network expansion
  schema/registry/baseline mutation

## 2. Problem

`baseline_replay_validator.py` currently mixes two questions:

1. Did all files match the frozen v0 baseline snapshot exactly?
2. Is the current live local loop still safe after append-only verification residue?

Because Phase 0.5 has legitimate live residue, the strict replay is currently:

```text
FAIL_REPLAY_MISMATCH
```

But safety invariants are still healthy:

```json
{
  "fail_events": 0,
  "authority_mutations": 0,
  "non_hold_reviews": 0
}
```

## 3. Patch Goal

Add explicit validator modes:

- `frozen`: strict checksum replay against the selected snapshot
- `live-safety`: DB safety invariants only; no checksum replay claim

Do not create or update a baseline snapshot.

Do not alter existing snapshot files.

## 4. Allowed Modify Paths

- `app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py`
- `app/work/vectorfl_ops_phase_0_5/BASELINE_REPLAY_VALIDATOR.md`

Optional if Hermes wants a receipt after execution:

- `app/work/vectorfl_ops_phase_0_5/receipts/baseline_replay_validator_mode_split_receipt.md`
- `app/work/vectorfl_ops_phase_0_5/exports/baseline_replay_validator_mode_split_export.md`

Forbidden modify paths:

- `app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v0/*`
- `app/work/vectorfl_ops_phase_0_5/data/vectorfl_ops_phase_0_5.sqlite`
- authority manifests
- output_manifest
- registry/schema/baseline docs outside listed files
- Obsidian `05-*` source notes

## 5. Required Code Behavior

### 5.1 CLI interface

Add argparse support:

```bash
python3 tools/baseline_replay_validator.py --mode frozen
python3 tools/baseline_replay_validator.py --mode live-safety
```

Default should remain strict frozen behavior for backward compatibility:

```bash
python3 tools/baseline_replay_validator.py
```

same as:

```bash
python3 tools/baseline_replay_validator.py --mode frozen
```

### 5.2 Frozen mode

Frozen mode should retain current behavior:

- read snapshot manifest
- compute file checksums
- compare exact SHA256
- report checksum mismatches as problems
- report DB fact drift as WATCH unless safety invariants fail
- exit nonzero if checksum problems exist

Current expected result may remain FAIL due to known mismatch.

### 5.3 Live-safety mode

Live-safety mode should:

- read current DB facts
- check only safety invariants:
  - `fail_events == 0`
  - `authority_mutations == 0`
  - `non_hold_reviews == 0`
- include live counts:
  - requests
  - executions
  - receipts
  - reviews
  - maturation_entries
  - guardrail_events
  - probe_requests
- not compare file checksums
- not claim snapshot replay match
- write receipt/export with classification:

```text
PIPELINE_BASELINE_LIVE_SAFETY_VALIDATOR_V0
```

Expected live-safety verdict:

```text
PASS_LIVE_SAFETY_INVARIANTS_WITH_HOLD
```

Exit code:

- 0 if safety invariants pass
- 1 if any safety invariant fails

## 6. Documentation Patch

Update `BASELINE_REPLAY_VALIDATOR.md` to state:

- frozen mode checks snapshot byte identity
- live-safety mode checks current DB safety invariants
- live-safety PASS is not baseline replay PASS
- neither mode is authority, promotion, Program Alpha, or Phase 1 implementation

## 7. Required Hermes Verification Commands

Run:

```bash
python3 -m py_compile app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py
```

Run frozen mode:

```bash
python3 app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py --mode frozen
```

Expected:

- likely nonzero exit
- `FAIL_REPLAY_MISMATCH`
- this is acceptable and should be reported as expected frozen mismatch, not patch failure

Run live-safety mode:

```bash
python3 app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py --mode live-safety
```

Expected:

- zero exit
- `PASS_LIVE_SAFETY_INVARIANTS_WITH_HOLD`

Confirm snapshot files unchanged:

```bash
shasum -a 256 app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v0/baseline_manifest.json app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v0/baseline_checksums.tsv
```

## 8. Required Hermes Return

Return exactly:

```text
verdict:
files_modified:
commands_run:
frozen_mode_result:
live_safety_result:
snapshot_files_unchanged:
state_mutations_observed:
WATCH:
HOLD:
next_smallest_action:
```

## 9. HOLD

- authority mutation: NO
- promotion: HOLD
- Program Alpha claim: NO
- M3/M4 claim: NO
- router/runner claim: NO
- external model/tool/network expansion: NO
- v1 snapshot creation: NO
- snapshot mutation: NO
- baseline/schema/registry mutation: NO
