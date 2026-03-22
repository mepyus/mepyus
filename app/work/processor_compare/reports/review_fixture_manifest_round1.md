# review fixture manifest round1

## 1. current diagnosis
- policy 분리 이후 다음 구조 안정화 포인트는 fixture 기준 고정이었다
- 이번 round1에서는 `control` 을 실제 manifest로 쪼개서
  - immutable regression fixture
  - mutable exploration control
로 고정했다

## 2. exact changes
- 새 코드 파일:
  - [review_fixture_manifest.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_fixture_manifest.py)
- 새 manifest:
  - [review_fixture_manifest_v0.json](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/review_fixture_manifest_v0.json)
  - [review_fixture_manifest_v0.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/review_fixture_manifest_v0.md)

### 새 loader 기능
- `load_review_fixture_manifest(...)`
- `load_review_fixture_entries(...)`
- `split_fixture_entries(...)`

즉 이제 fixture/control 기준은 코드가 읽을 수 있는 상태가 되었다.

## 3. verification
- immutable regression fixture
  - `doc_004 -> doc_005`: `canonical`
  - `doc_005 -> doc_006`: `canonical`
  - `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`: `canonical`
- mutable exploration control
  - `probe -> doc_006`: `possibility_candidate`, `candidate`
  - `probe -> doc_005`: `none`, `translation_missing`
  - `probe -> doc_004`: `none`, `translation_missing`
- loader import / manifest parse 정상

## 4. current reading
- `fixture manifest introduced`
- `control meaning is now split into immutable regression vs mutable exploration`
- `policy split can now be measured against a stable minimal baseline`

## 5. what not changed
- viewer 수정 안 함
- canonical 기준 안 바꿈
- translation 확대 안 함
- lifecycle/pruning 구현 안 함
- test runner 자동화 안 붙임

## 6. next recommendation
1. 다음은 `review surface stabilization`
2. 그다음 `lifecycle tag`
3. fixture runner는 그 뒤에 붙여도 된다

## 7. final sentence
- 이제 current engine은 policy boundary뿐 아니라 fixture boundary도 가진다
- 즉 다음 phase부터는 정책 변경이 regression인지 전진인지 더 안정적으로 읽을 수 있다
