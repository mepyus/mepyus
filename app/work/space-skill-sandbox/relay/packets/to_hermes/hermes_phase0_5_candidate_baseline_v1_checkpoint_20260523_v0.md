# HERMES_PHASE0_5_CANDIDATE_BASELINE_V1_CHECKPOINT_20260523_V0

## 1. Packet Status

packet_id:
  hermes_phase0_5_candidate_baseline_v1_checkpoint_20260523_v0

status:
  DRAFT_READY_ONLY_IF_USER_SELECTS_OPTION_B

target:
  Hermes

role:
  create current local Phase 0.5 candidate baseline v1 checkpoint

authority:
  checkpoint creation packet only

not:
  authority mutation
  promotion
  Program Alpha evidence
  M3/M4 confirmation
  router/runner implementation
  external model/tool/network expansion
  v0 snapshot mutation
  schema/registry mutation

## 2. Preconditions

Do not execute unless user explicitly chooses:

```text
Option B: Create v1 Candidate Checkpoint
```

Required prechecks:

```bash
python3 app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py --mode live-safety
python3 app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tools/phase1_deterministic_stable_cycle.py
python3 app/work/vectorfl_ops_phase_0_5/tools/phase0_5_candidate_baseline_v1_preflight.py
python3 app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_readonly_contract.py
python3 app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_ui_surface_completeness.py
```

Expected:

- live-safety PASS
- deterministic stable cycle PASS
- v1 preflight PASS
- Phase 1 tests PASS
- no authority mutation
- promotion HOLD

Current preflight evidence:

```text
app/work/vectorfl_ops_phase_0_5/receipts/phase0_5_candidate_baseline_v1_preflight_receipt.md
PASS_PHASE0_5_CANDIDATE_BASELINE_V1_PREFLIGHT_WITH_HOLD
candidate_file_count=69
problem_count=0
v1_snapshot_already_exists=false
```

## 3. Allowed Create Paths

Create only:

```text
app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v1/
app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v1/baseline_manifest.json
app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v1/baseline_checksums.tsv
app/work/vectorfl_ops_phase_0_5/receipts/phase0_5_candidate_baseline_v1_snapshot_receipt.md
app/work/vectorfl_ops_phase_0_5/exports/phase0_5_candidate_baseline_v1_snapshot_export.md
```

Forbidden:

- modify `phase0_5_candidate_baseline_v0`
- delete old receipts
- rewrite shared DB
- mutate authority manifests
- update output_manifest
- promote anything

## 4. Snapshot Contents

Record current files under:

```text
app/work/vectorfl_ops_phase_0_5/
```

Use the same general manifest style as v0:

- classification
- verdict
- created_at
- root
- snapshot_dir
- file_count
- manifest_entries with:
  - path
  - relative_path
  - exists
  - kind
  - bytes
  - sha256
- db_facts
- HOLD fields

Exclude from v1 manifest if needed:

- `__pycache__`
- `.DS_Store`
- transient temp files

Do not exclude receipts/exports merely because they are inconvenient. If included, their hashes define the v1 checkpoint state.

## 4.1 Guarded Local Tool

Codex prepared a guarded local creator:

```text
app/work/vectorfl_ops_phase_0_5/tools/phase0_5_candidate_baseline_v1_snapshot.py
```

Default run must not create v1:

```bash
python3 app/work/vectorfl_ops_phase_0_5/tools/phase0_5_candidate_baseline_v1_snapshot.py
```

Expected:

```text
HOLD_CONFIRM_OPTION_B_REQUIRED
v1_snapshot_creation=NO
```

Only if the user explicitly approves Option B, execute:

```bash
python3 app/work/vectorfl_ops_phase_0_5/tools/phase0_5_candidate_baseline_v1_snapshot.py --confirm-option-b
```

## 5. Required Receipt Language

Receipt verdict:

```text
PASS_PHASE0_5_CANDIDATE_BASELINE_V1_SNAPSHOT_CREATED_WITH_HOLD
```

Receipt must state:

- v0 preserved
- v1 is candidate checkpoint only
- no authority mutation
- promotion HOLD
- Program Alpha NO
- Phase 1 production readiness NO
- external execution NO
- live-safety was PASS before snapshot
- frozen v0 replay may remain FAIL

## 6. Verification After Creation

Run:

```bash
python3 app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py --mode live-safety
```

Also verify files exist:

```bash
test -f app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v1/baseline_manifest.json
test -f app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v1/baseline_checksums.tsv
test -f app/work/vectorfl_ops_phase_0_5/receipts/phase0_5_candidate_baseline_v1_snapshot_receipt.md
test -f app/work/vectorfl_ops_phase_0_5/exports/phase0_5_candidate_baseline_v1_snapshot_export.md
```

## 7. Required Hermes Return

Return exactly:

```text
verdict:
prechecks:
created:
file_count:
db_facts:
v0_preserved:
live_safety_after:
state_mutations_observed:
WATCH:
HOLD:
next_smallest_action:
```

## 8. HOLD

- authority mutation: NO
- promotion: HOLD
- Program Alpha claim: NO
- M3/M4 claim: NO
- router/runner claim: NO
- external model/tool/network expansion: NO
- v0 snapshot mutation: NO
- schema/registry mutation: NO
