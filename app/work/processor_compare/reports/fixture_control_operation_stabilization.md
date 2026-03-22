# fixture control operation stabilization

## 1. current diagnosis

- fixture/control 분리는 이미 문서화돼 있었지만, runner 기준으로는 기대 bridge/review 상태만 비교하고 있었다.
- 이 상태로는 immutable regression fixture와 mutable exploration control이 lifecycle 기대나 drift 허용 수준까지는 다르게 읽히지 않았다.

## 2. exact changes

- [review_fixture_manifest.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_fixture_manifest.py)
  - `expected_lifecycle_temperature`
  - `expected_lifecycle_stage`
  - `allowed_drift`
  필드 추가
- [review_fixture_manifest_v0.json](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/review_fixture_manifest_v0.json)
  - immutable fixture는 `allowed_drift = none`
  - mutable control은 `allowed_drift = exploration_state_change_allowed`
  - 각 fixture에 lifecycle expectation 명시
- [run_review_fixture_check.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_review_fixture_check.py)
  - runner가 bridge/review뿐 아니라 lifecycle expectation도 검사
  - `lifecycle_matches_expected` 출력 추가

## 3. verification

- canonical fixture
  - 모두 `canonical / not_applicable`
  - lifecycle `hot / approved_active`
  - `allowed_drift = none`
- mutable exploration control
  - `probe -> doc_006`
    - `possibility_candidate / candidate`
    - lifecycle `hot / review_active`
    - `allowed_drift = exploration_state_change_allowed`
  - `probe -> doc_005`, `probe -> doc_004`
    - `none / translation_missing`
    - lifecycle `warm / blocked_waiting_revisit`
    - `allowed_drift = exploration_state_change_allowed`
- runner 결과
  - `immutable_pass_count = 3`
  - `mutable_match_count = 3`
  - `lifecycle_match_count = 6`

## 4. current reading

- fixture/control split is now enforceable via runner
- immutable regression fixture와 mutable exploration control은 운영상으로도 다른 존재가 됐다

## 5. next recommendation

1. 다음에는 fixture manifest에 optional owner/phase metadata 정도만 더 붙이기
2. mutable control은 drift를 실패가 아니라 변화 신호로 읽는 방향 유지
3. immutable fixture는 current canonical 기준의 회귀 방어선으로 계속 잠그기
