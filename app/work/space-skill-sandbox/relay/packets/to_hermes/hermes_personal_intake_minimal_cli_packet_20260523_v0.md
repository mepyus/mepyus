# HERMES_PERSONAL_INTAKE_MINIMAL_CLI_PACKET_20260523_V0

## 1. Packet Status

packet_id:
  hermes_personal_intake_minimal_cli_packet_20260523_v0

status:
  DRAFT_READY_FOR_USER_REVIEW_WITH_HOLD

target:
  Hermes

role:
  bounded implementation of minimal personal intake CLI against fixture DB first

not:
  authority mutation
  promotion
  Program Alpha evidence
  M3/M4 confirmation
  router/runner implementation
  external model/tool/network expansion
  v1 snapshot creation
  write UI

## 2. Basis

Contract:

```text
app/work/VECTORFL_PERSONAL_PROGRAM_UNIT_CONTRACT_20260523_V0.md
```

Position card:

```text
app/work/VECTORFL_PERSONAL_PROGRAM_UNIT_POSITION_AND_BUILDUP_20260523_V0.md
```

Existing stable cycle:

```text
app/work/vectorfl_ops_phase_1_web_mvp_skeleton/receipts/phase1_deterministic_stable_cycle_receipt.md
```

## 3. Goal

Implement:

```text
app/work/vectorfl_ops_phase_0_5/tools/personal_intake_min.py
```

The script must support fixture-first personal intake into a SQLite DB selected by `VECTORFL_PHASE0_DB`.

## 4. Allowed Behavior

The script may:

- parse CLI arguments
- accept title/body/source_type/lens/boundary_level/valid_for/not_valid_for/placement_candidate
- connect to SQLite DB from `VECTORFL_PHASE0_DB`
- insert one request
- insert one decision
- insert one execution record marked local/no-model
- insert one receipt
- insert one review with HOLD
- insert one maturation candidate with authority mutation NO
- write a markdown receipt under a test/output path

## 5. Required Defaults

```text
authority_status=NO
promotion_status=HOLD
external_execution=NO
real_company_data=NO
program_alpha_evidence=NO
```

## 6. Forbidden

Do not:

- call network/API/MCP/model connector
- implement router
- implement runner.py
- mutate schema
- mutate v0 or v1 snapshots
- create v1 checkpoint
- promote anything
- mutate authority
- add write UI
- run live DB intake unless explicitly asked after fixture tests pass

## 7. Tests Required

Create or update tests under:

```text
app/work/vectorfl_ops_phase_0_5/tests/
```

Required tests:

- fixture DB intake succeeds
- inserted request has promotion HOLD and authority NO
- decision/execution/receipt/review/maturation rows are created
- no fail guardrail events are introduced
- receipt markdown is written
- missing required title/body fails without DB mutation

## 8. Verification Commands

Run:

```bash
python3 -m py_compile app/work/vectorfl_ops_phase_0_5/tools/personal_intake_min.py
python3 app/work/vectorfl_ops_phase_0_5/tests/test_personal_intake_min.py
python3 app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tools/phase1_deterministic_stable_cycle.py
python3 app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py --mode live-safety
```

Expected:

- py_compile PASS
- fixture intake tests PASS
- deterministic stable cycle PASS
- live-safety PASS

## 9. Required Return

Return:

```text
verdict:
files_modified:
commands_run:
test_results:
fixture_db_mutation:
shared_db_mutation:
state_mutations_observed:
WATCH:
HOLD:
next_smallest_action:
```

## 10. HOLD

- authority mutation: NO
- promotion: HOLD
- Program Alpha claim: NO
- M3/M4 claim: NO
- router/runner claim: NO
- external model/tool/network expansion: NO
- live DB intake: HOLD
- write UI: NO
- v1 snapshot creation: NO
