# policy executor boundary round2

## 1. current diagnosis
- round1에서 `promotion review` 축의 policy/output 경계를 만들었다
- 이번 round2에서는 그 다음 핵심 병목인 `cross_path overlap` 분류를 분리했다
- 이유:
  - 이 축이 앞으로 `family canonicalization rule` 과 직접 붙는 자리이기 때문이다
  - semantic-only / thin-direct / translated-only / cross-family-corroborated 같은 상태가 policy 성격을 강하게 띠고 있다

## 2. exact changes

### 새로 분리된 것
- [review_policy_types.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policy_types.py)
  - `CrossPathPolicyContext`
  - `CrossPathPolicyResult`
- [review_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policies.py)
  - `evaluate_cross_path_overlap_policy`
- [review_output_surface.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_output_surface.py)
  - `assemble_cross_path_review_surface`

### live_input_space.py 에서 줄인 책임
- `_build_cross_path_review` 는 이제
  - overlap evidence 수집
  - policy context 조립
  - policy 호출
  - output surface 조립
  흐름으로 바뀌었다
- 즉 classification 자체는 코어 파일에서 빠지기 시작했다

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
  - `cross_path_overlap_quality_class = semantic_only`
  - `space_entry_state = structural_led_space_pre_entry`

### control
- `engine_phase1_observer_probe_20260321 -> doc_005`
  - `bridge_mode = none`
  - `review_state = translation_missing`
- `engine_phase1_observer_probe_20260321 -> doc_004`
  - `bridge_mode = none`
  - `review_state = translation_missing`

## 4. current reading
- `cross_path overlap policy separated, executor still dominant`
- `promotion review + cross_path classification now both have callable policy boundaries`
- `output surface separation is partial but stable`

## 5. what not changed
- canonical 기준 안 바꿈
- translation 범위 안 넓힘
- processing refinement 안 건드림
- family canonicalization rule 안 바꿈
- viewer 수정 안 함

## 6. next recommendation
1. 다음 분리 1순위는 `family canonicalization policy`
2. 그다음 `direct overlap promotion policy`
3. 그 다음 `fixture manifest`

## 7. final sentence
- round2까지 오면서 [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py) 는 여전히 orchestrator 중심이지만,
  최소한 `promotion review` 와 `cross_path overlap classification` 은 외부 policy callable로 분리되기 시작했다
