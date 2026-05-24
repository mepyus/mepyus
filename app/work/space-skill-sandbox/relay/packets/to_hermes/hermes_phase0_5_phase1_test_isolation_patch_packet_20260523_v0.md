# HERMES_PHASE0_5_PHASE1_TEST_ISOLATION_PATCH_PACKET_20260523_V0

## 1. Packet Status

packet_id:
  hermes_phase0_5_phase1_test_isolation_patch_packet_20260523_v0

status:
  DRAFT_READY_FOR_USER_APPROVAL_BEFORE_HERMES_EXECUTION

target:
  Hermes

role:
  apply exact local test-isolation patch and run bounded validators

authority:
  patch packet only

not:
  authority mutation
  promotion
  Program Alpha evidence
  M3/M4 confirmation
  router/runner implementation
  external model/tool/network expansion
  schema/registry/baseline mutation

## 2. Problem

Codex verification found a program-design defect:

`app/work/vectorfl_ops_phase_0_5/probes/guardrail_probe_runner.py` appends probe requests and guardrail events into the shared SQLite DB:

```text
app/work/vectorfl_ops_phase_0_5/data/vectorfl_ops_phase_0_5.sqlite
```

After one rerun:

```json
{
  "requests": 10,
  "guardrail_events": 25,
  "probe_requests": 6,
  "fail_events": 0,
  "authority_mutations": 0,
  "non_hold_reviews": 0
}
```

Phase 1 tests then failed because they expected fixed baseline counts:

- `len(reqs) == 7`
- `len(guardrails) == 22`
- `probe_requests == 3`

This is not an authority failure. It is a test isolation / live ledger design problem.

## 3. Patch Goal

Make verification repeatable without mutating the shared baseline evidence DB.

Patch principles:

- Phase 0.5 mutable probes must accept an alternate DB path.
- Phase 1 tests must run against an isolated DB copy.
- Phase 1 contract tests should assert safety invariants, not brittle exact counts, unless using a known fixture DB.
- No production behavior expansion.

## 4. Exact Patch Scope

Allowed modify paths:

- `app/work/vectorfl_ops_phase_0_5/probes/guardrail_probe_runner.py`
- `app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_readonly_contract.py`
- `app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_ui_surface_completeness.py`

Optional modify path if needed:

- `app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tools/api_contract_replay.py`

Forbidden modify paths:

- `app/work/vectorfl_ops_phase_0_5/data/vectorfl_ops_phase_0_5.sqlite`
- `app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v0/*`
- authority manifests
- output_manifest
- registry/schema/baseline docs
- Obsidian `05-*` source notes

## 5. Proposed Code Changes

### 5.1 `guardrail_probe_runner.py`

Change DB definition from hardcoded path to env-overridable path:

```python
import os

DB=Path(os.environ.get('VECTORFL_PHASE0_DB', str(ROOT/'data'/'vectorfl_ops_phase_0_5.sqlite')))
```

Keep default behavior unchanged when `VECTORFL_PHASE0_DB` is not set.

### 5.2 `test_readonly_contract.py`

In `setUpClass`, before starting the server:

1. Create a temporary directory.
2. Copy the current Phase 0.5 SQLite DB into the temp directory.
3. Set `VECTORFL_PHASE0_DB` to the temp copy.
4. Start Phase 1 server against that temp copy.

Required imports:

```python
import shutil
import tempfile
```

Add class cleanup:

```python
cls.tmpdir.cleanup()
```

Change brittle assertions:

```python
self.assertEqual(len(reqs),7)
self.assertEqual(len(gs),22)
```

to invariant assertions:

```python
self.assertGreaterEqual(len(reqs),7)
self.assertGreaterEqual(len(gs),22)
```

Also assert safety invariants remain:

```python
self.assertEqual(data['counts']['fail_events'],0)
self.assertEqual(data['counts']['authority_mutations'],0)
self.assertEqual(data['counts']['non_hold_reviews'],0)
```

### 5.3 `test_ui_surface_completeness.py`

Apply same temp DB copy setup.

Change:

```python
self.assertEqual(d['intentional_residue']['probe_requests'],3)
```

to:

```python
self.assertGreaterEqual(d['intentional_residue']['probe_requests'],3)
```

Keep:

```python
self.assertEqual(d['intentional_residue']['receipts_without_reviews'],1)
```

only if it remains stable with the isolated copied DB. If not stable, change to:

```python
self.assertGreaterEqual(d['intentional_residue']['receipts_without_reviews'],1)
```

## 6. Required Hermes Verification Commands

Run after patch:

```bash
python3 -m py_compile app/work/vectorfl_ops_phase_0_5/probes/guardrail_probe_runner.py app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_readonly_contract.py app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_ui_surface_completeness.py
```

```bash
python3 app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_readonly_contract.py
```

```bash
python3 app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tests/test_ui_surface_completeness.py
```

Then verify the shared DB did not change during the two Phase 1 tests:

```bash
python3 - <<'PY'
import sqlite3, json
from pathlib import Path
p=Path('app/work/vectorfl_ops_phase_0_5/data/vectorfl_ops_phase_0_5.sqlite')
con=sqlite3.connect(p)
cur=con.cursor()
facts={
  'requests':cur.execute('select count(*) from requests').fetchone()[0],
  'guardrail_events':cur.execute('select count(*) from guardrail_events').fetchone()[0],
  'probe_requests':cur.execute("select count(*) from requests where title like 'Probe %'").fetchone()[0],
  'fail_events':cur.execute("select count(*) from guardrail_events where result like 'FAIL%'").fetchone()[0],
  'authority_mutations':cur.execute("select count(*) from maturation_entries where authority_mutation!='NO'").fetchone()[0],
  'non_hold_reviews':cur.execute("select count(*) from reviews where promotion_status!='HOLD' or authority_status!='NO'").fetchone()[0],
}
print(json.dumps(facts, indent=2))
PY
```

Expected current shared DB facts before and after Phase 1 isolated tests:

```json
{
  "requests": 10,
  "guardrail_events": 25,
  "probe_requests": 6,
  "fail_events": 0,
  "authority_mutations": 0,
  "non_hold_reviews": 0
}
```

## 7. Expected Result

Expected:

- py_compile PASS
- read-only contract test PASS
- UI surface completeness test PASS
- shared DB count unchanged by Phase 1 tests
- HOLD boundaries unchanged

Not expected:

- baseline replay checksum PASS
- DB count rollback
- snapshot update
- authority promotion

Baseline replay may still fail until a separate baseline resnapshot or reconciliation decision is explicitly approved.

## 8. Hermes Return Format

Return exactly:

```text
verdict:
files_modified:
commands_run:
test_results:
shared_db_before:
shared_db_after:
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
- baseline/schema/registry mutation: NO
