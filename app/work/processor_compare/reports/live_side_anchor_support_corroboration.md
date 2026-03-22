# live side anchor support corroboration

## 1. current diagnosis
- `doc_006` review candidate 는 더 이상 내부 support 부족으로 막힌 상태가 아니다
- imported 쪽 same-local_ref 에는 `semantic + structural + process + object` family support 가 있고, live 쪽에도 `semantic + structural + object` family support 는 있다
- 그러나 direct cross-path corroboration 으로 canonicalizable 하게 겹치는 family 는 아직 `semantic` 뿐이다
- 현재 가장 강한 blocker 는 `live_side_family_present_but_not_canonicalized` 다

## 2. exact changes
- 변경 파일: `app/core/runtime/live_input_space.py`
- 추가 필드:
  - `live_side_support_class`
  - `live_side_support_families`
  - `live_side_missing_families`
  - `live_side_anchor_evidence`
  - `cross_path_uncorroborated_live_families`
- 적용:
  - live side family support 를 review 출력에 분리
  - imported candidate family 와 live side family 가 둘 다 있는데 direct overlap 으로는 안 잡히는 경우를 별도 blocker 로 기록
- 유지:
  - canonical 기준
  - possibility 기준
  - local_ref translation scope
  - control case state

## 3. verification
- review candidate:
  - `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode=possibility_candidate`
  - `translation_gate=true`
  - `processing_gate=true`
  - `observer_gate=true`
  - `canonical_anchor_gate=false`
  - `live_side_support_class=multi_family_live_support_present`
  - `live_side_support_families=[semantic, structural, object]`
  - `live_side_missing_families=[process]`
  - `cross_path_overlap_quality_class=semantic_only`
  - `cross_path_threshold_gap_class=live_side_family_present_but_not_canonicalized`
  - `cross_path_uncorroborated_live_families=[structural, object]`
  - `next_review_blocker=live_side_family_present_but_not_canonicalized`
- live side evidence:
  - `semantic_tokens=[graph, graph rag, rag]`
  - `structural_tokens=[graph rag 구조, rag 구조, rag 구조 on, 구조 on]`
  - `text_hint_families=[structural, object]`
- control:
  - `engine_phase1_observer_probe_20260321 -> doc_004`
    - `bridge_mode=none`
    - `review_state=translation_missing`
  - `engine_phase1_observer_probe_20260321 -> doc_005`
    - `bridge_mode=none`
    - `review_state=translation_missing`
- canonical 유지:
  - `doc_004 -> doc_005`: `canonical`
  - `doc_005 -> doc_006`: `canonical`
  - `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`: `canonical`

## 4. current reading
- `doc_006` 은 imported 내부 support 만 강한 후보가 아니다
- live 쪽에도 `structural/object` family 는 존재한다
- 하지만 그 family 들이 cross-path direct corroboration 으로 canonicalizable 하게 연결되지는 않는다
- 즉 현재 병목은 `support family absence` 가 아니라 `family canonicalization gap` 이다
- 그래서 다음 패치 방향은 translation breadth 가 아니라 `cross-path anchor canonicalization` 쪽이 더 맞다

## 5. next recommendation
- 다음 우선순위:
  - `cross-path anchor canonicalization refinement`
- 그 다음 후보:
  - live-side anchor token derivation refinement
  - canonical review threshold split 추가 분해
- 지금 단계에서는 document-wide 확장보다
  - `doc_006 best_local_ref <-> live probe` 수준의 family canonicalization 이 더 맞다
