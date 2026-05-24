# Commands Run

## current_time

```bash
date "+%Y-%m-%d %H:%M:%S %Z"
```

exit_code: 0

```text
2026-05-23 07:29:24 KST
```

## shared_db_before

```bash
python3 - <<'PY'
import sqlite3, json
from pathlib import Path
p=Path('app/work/vectorfl_ops_phase_0_5/data/vectorfl_ops_phase_0_5.sqlite')
con=sqlite3.connect(p)
cur=con.cursor()
facts={
  'requests':cur.execute('select count(*) from requests').fetchone()[0],
  'executions':cur.execute('select count(*) from executions').fetchone()[0],
  'receipts':cur.execute('select count(*) from receipts').fetchone()[0],
  'reviews':cur.execute('select count(*) from reviews').fetchone()[0],
  'maturation_entries':cur.execute('select count(*) from maturation_entries').fetchone()[0],
  'guardrail_events':cur.execute('select count(*) from guardrail_events').fetchone()[0],
  'probe_requests':cur.execute("select count(*) from requests where title like 'Probe %'").fetchone()[0],
  'fail_events':cur.execute("select count(*) from guardrail_events where result like 'FAIL%'").fetchone()[0],
  'authority_mutations':cur.execute("select count(*) from maturation_entries where authority_mutation!='NO'").fetchone()[0],
  'non_hold_reviews':cur.execute("select count(*) from reviews where promotion_status!='HOLD' or authority_status!='NO'").fetchone()[0],
}
print(json.dumps(facts, indent=2, sort_keys=True))
PY
```

exit_code: 0

```text
{
  "authority_mutations": 0,
  "executions": 3,
  "fail_events": 0,
  "guardrail_events": 25,
  "maturation_entries": 4,
  "non_hold_reviews": 0,
  "probe_requests": 6,
  "receipts": 5,
  "requests": 10,
  "reviews": 4
}
```

## personal_intake_tests

```bash
python3 app/work/vectorfl_ops_phase_0_5/tests/test_personal_intake_min.py
```

exit_code: 0

```text
test_fixture_db_intake_succeeds_and_writes_receipt (__main__.PersonalIntakeMinTests) ... ok
test_inserted_rows_preserve_hold_and_no_authority (__main__.PersonalIntakeMinTests) ... ok
test_missing_required_body_fails_without_db_mutation (__main__.PersonalIntakeMinTests) ... ok
test_missing_required_title_fails_without_db_mutation (__main__.PersonalIntakeMinTests) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.379s

OK
```

## phase1_deterministic_stable_cycle

```bash
python3 app/work/vectorfl_ops_phase_1_web_mvp_skeleton/tools/phase1_deterministic_stable_cycle.py
```

exit_code: 0

```text
PASS_PHASE1_DETERMINISTIC_STABLE_CYCLE_WITH_HOLD
problem_count=0
report=/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_1_web_mvp_skeleton/reports/phase1_deterministic_stable_cycle_report.json
receipt=/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_1_web_mvp_skeleton/receipts/phase1_deterministic_stable_cycle_receipt.md
```

## live_safety

```bash
python3 app/work/vectorfl_ops_phase_0_5/tools/baseline_replay_validator.py --mode live-safety
```

exit_code: 0

```text
BASELINE_LIVE_SAFETY_PASS
verdict=PASS_LIVE_SAFETY_INVARIANTS_WITH_HOLD
problem_count=0
receipt=/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_0_5/receipts/pipeline_baseline_live_safety_validator_receipt.md
export=/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_0_5/exports/pipeline_baseline_live_safety_validator_export.md
```

## v1_preflight

```bash
python3 app/work/vectorfl_ops_phase_0_5/tools/phase0_5_candidate_baseline_v1_preflight.py
```

exit_code: 0

```text
PASS_PHASE0_5_CANDIDATE_BASELINE_V1_PREFLIGHT_WITH_HOLD
candidate_file_count=71
problem_count=0
receipt=/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_0_5/receipts/phase0_5_candidate_baseline_v1_preflight_receipt.md
export=/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_0_5/exports/phase0_5_candidate_baseline_v1_preflight_export.md
```

## shared_db_after

```bash
python3 - <<'PY'
import sqlite3, json
from pathlib import Path
p=Path('app/work/vectorfl_ops_phase_0_5/data/vectorfl_ops_phase_0_5.sqlite')
con=sqlite3.connect(p)
cur=con.cursor()
facts={
  'requests':cur.execute('select count(*) from requests').fetchone()[0],
  'executions':cur.execute('select count(*) from executions').fetchone()[0],
  'receipts':cur.execute('select count(*) from receipts').fetchone()[0],
  'reviews':cur.execute('select count(*) from reviews').fetchone()[0],
  'maturation_entries':cur.execute('select count(*) from maturation_entries').fetchone()[0],
  'guardrail_events':cur.execute('select count(*) from guardrail_events').fetchone()[0],
  'probe_requests':cur.execute("select count(*) from requests where title like 'Probe %'").fetchone()[0],
  'fail_events':cur.execute("select count(*) from guardrail_events where result like 'FAIL%'").fetchone()[0],
  'authority_mutations':cur.execute("select count(*) from maturation_entries where authority_mutation!='NO'").fetchone()[0],
  'non_hold_reviews':cur.execute("select count(*) from reviews where promotion_status!='HOLD' or authority_status!='NO'").fetchone()[0],
}
print(json.dumps(facts, indent=2, sort_keys=True))
PY
```

exit_code: 0

```text
{
  "authority_mutations": 0,
  "executions": 3,
  "fail_events": 0,
  "guardrail_events": 25,
  "maturation_entries": 4,
  "non_hold_reviews": 0,
  "probe_requests": 6,
  "receipts": 5,
  "requests": 10,
  "reviews": 4
}
```

