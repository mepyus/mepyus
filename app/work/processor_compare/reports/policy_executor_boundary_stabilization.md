# policy executor boundary stabilization

## 1. current diagnosis

- 가장 큰 구조 리스크는 `live_input_space.py`가 다시 policy 쓰레기통처럼 자라는 역류였다.
- 이미 policy callable boundary는 생겼지만, orchestration / policy call / output assemble의 경계가 코드상에서 충분히 드러나지 않으면 다음 패치가 다시 코어 파일에 하드코딩될 위험이 있었다.

## 2. exact changes

- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)
  - `evaluate_mixed_path_pair(...)`에 executor section / lifecycle section / output surface section 역할 주석 추가
  - `_build_promotion_review(...)`에 orchestration-only 경계 주석 추가
  - 새 승인 규칙은 [review_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policies.py) 에 둔다는 경계선을 코드에 명시
- policy 동작 자체는 변경하지 않았다.
- output surface field도 유지했다.

## 3. verification

- `python3 -m py_compile ...` 통과
- canonical fixture 유지
  - `doc_004 -> doc_005`
  - `doc_005 -> doc_006`
  - `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`
- exploration control 유지
  - `probe -> doc_006`: `possibility_candidate / candidate`
  - `probe -> doc_005`, `probe -> doc_004`: `none / translation_missing`

## 4. current reading

- boundary documented only 단계는 넘었다.
- 지금은 `policy/executor boundary now operationally visible` 로 읽을 수 있다.
- executor는 아직 dominant지만, policy 추가가 코어로 역류하지 않도록 최소 방어선은 생겼다.

## 5. next recommendation

1. 추가 규칙은 계속 [review_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policies.py) 로만 넣기
2. 다음 code split이 필요하면 executor 자체보다 builder/helper 정리를 우선
3. 현재 phase에서는 더 많은 policy 분리보다 stabilization 유지가 우선
