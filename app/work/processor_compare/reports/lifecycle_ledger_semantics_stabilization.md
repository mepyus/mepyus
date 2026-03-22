# lifecycle ledger semantics stabilization

## 1. current diagnosis

- `trace_temperature`, `lifecycle_stage`, `evaluated_at`, `state_signature`는 이미 있었지만 운영 의미가 runner와 ledger까지 충분히 연결되지는 않았다.
- ledger가 단순 축적 파일로만 남으면 revisit나 warm 유지 여부를 읽기 어렵다.

## 2. exact changes

- [review_state_ledger.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_state_ledger.py)
  - `summarize_review_state_entry(...)` 추가
  - ledger entry에서
    - `revisit_recommended`
    - `warm_downgrade_candidate`
    를 읽는 최소 운영 요약 추가
- [run_review_fixture_check.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_review_fixture_check.py)
  - ledger baseline과 현재 state signature를 비교
  - `ledger_state_signature_unchanged`
  - `persisted_last_reviewed_at`
  - `persisted_review_count`
  - `ledger_revisit_recommended`
  - `ledger_warm_downgrade_candidate`
  출력 추가
- [review_state_ledger.json](/Users/sungsookim/universe/vectorfl_replica/runtime/review_ledgers/review_state_ledger.json)
  - fixture별 persisted review state 저장

## 3. semantics

- `hot`
  - 현재 활성 승인/리뷰 상태
- `warm`
  - 보존해야 하지만 즉시 승인되진 않는 blocked/deferred 상태
- `cold`
  - 현재 활성 신호가 얇은 archive 후보 상태
- `approved_active`
  - canonical 승인 상태
- `review_active`
  - active review candidate 상태
- `blocked_waiting_revisit`
  - blocked control이지만 revisit 가치가 있는 상태

## 4. verification

- runner 결과
  - `unchanged_signature_count = 6`
  - `unchanged_ledger_signature_count = 6`
  - `changed_signature_count = 0`
  - `changed_ledger_signature_count = 0`
- ledger read
  - canonical fixture는 `revisit_recommended = false`
  - `probe -> doc_006`은 `hot / review_active`, `revisit_recommended = false`
  - `probe -> doc_005`, `probe -> doc_004`는 `warm / blocked_waiting_revisit`, `revisit_recommended = true`, `warm_downgrade_candidate = true`

## 5. current reading

- lifecycle semantics documented and minimally wired
- review ledger is now usable for revisit semantics

## 6. next recommendation

1. 실제 pruning automation은 아직 미루기
2. 다음 phase에서 `review_count + age` 기준이 필요하면 그때 warm/cold rule을 자동화
3. 지금은 runner + ledger 조합으로 drift/revisit 운영 의미를 유지하는 게 충분
