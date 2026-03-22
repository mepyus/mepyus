# policy executor boundary round4

## 1. current diagnosis
- round3까지 오면서 `promotion review`, `cross_path overlap`, `direct overlap` 축이 분리되었다
- 이번 round4는 나머지 핵심 policy 축인
  - `cross_path canonicalization`
  - `space entry`
를 분리했다
- 이 둘은 review lane 후반부의 상태 승격 해석을 담당하므로, 코어 파일 안에 계속 남겨두면 다음 phase 정책이 다시 응축될 위험이 컸다

## 2. exact changes

### 새 타입
- [review_policy_types.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policy_types.py)
  - `CanonicalizationPolicyContext`
  - `CanonicalizationPolicyResult`
  - `SpaceEntryPolicyContext`
  - `SpaceEntryPolicyResult`

### 새 policy 함수
- [review_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policies.py)
  - `evaluate_canonicalization_family_policy`
  - `evaluate_space_entry_policy`

### live_input_space.py 에서 줄인 책임
- `_build_cross_path_canonicalization_review`
  - family별 strength / blocker / token source 판정을 external policy 호출로 전환
- `_build_space_entry_review`
  - state / blocker / reason 판정을 external policy 호출로 전환

즉 round4부터는 canonicalization 과 space entry의 상태 분기 또한 callable policy 경계를 가진다.

## 3. verification

### compile
- `python3 -m py_compile` 통과

### canonical fixture
- `doc_004 -> doc_005`: `canonical`
- `doc_005 -> doc_006`: `canonical`
- `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`: `canonical`

### review candidate
- `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode = possibility_candidate`
  - `review_state = candidate`
  - `cross_path_canonicalization_proposal_state = token_supported_candidates_present`
  - `space_entry_state = structural_led_space_pre_entry`
  - `space_entry_blocker = token_pair_exists_but_alignment_rule_not_satisfied`

### control
- `engine_phase1_observer_probe_20260321 -> doc_005`
  - `bridge_mode = none`
  - `review_state = translation_missing`
- `engine_phase1_observer_probe_20260321 -> doc_004`
  - `bridge_mode = none`
  - `review_state = translation_missing`

## 4. current reading
- `promotion / cross_path / direct_overlap / canonicalization / space_entry` 까지 주요 policy 축은 callable boundary를 가졌다
- executor 는 아직 dominant 이지만, policy 증식이 그대로 코어 함수 안으로 박히는 구조는 상당히 줄었다
- 이제 [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py) 는 evidence collect + context assemble + policy call + surface assemble 구조로 읽기 시작할 수 있다

## 5. what not changed
- canonical 기준 안 바꿈
- translation 확대 안 함
- processing refinement 안 건드림
- viewer 수정 안 함
- lifecycle/pruning 구현 안 함
- fixture manifest 아직 안 붙임

## 6. next recommendation
1. 다음은 `fixture manifest`를 붙이는 것이 자연스럽다
2. 그 다음 `review surface`를 더 명확한 assembler 계층으로 정리할 수 있다
3. lifecycle tag는 이 뒤에 붙여도 늦지 않다

## 7. final sentence
- round4까지 오면서 현재 엔진의 가장 중요한 review/canonicalization policy 축은 대부분 외부 callable policy로 빠지기 시작했다
- 이제 다음 phase는 policy 증설보다 `fixture / lifecycle / output surface stabilization` 쪽으로 옮길 수 있다
