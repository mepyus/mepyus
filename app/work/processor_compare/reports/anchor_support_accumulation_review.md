# anchor support accumulation review

## 1. current diagnosis
- `doc_006` typed canonical review candidate는 이제 semantic single-family 상태에서 한 단계 더 올라왔다
- 현재 읽힘:
  - semantic overlap: `graph`, `rag`
  - same local_ref accumulation: `structural`, `process`, `object`
  - nearby local_ref accumulation: 없음
- 즉 단순 `single_family_only`나 `semantic_plus_process_weak`를 넘어서 `multi_family_compound_candidate` 상태까지 왔다
- 가장 강한 잔여 blocker는 `multi_family_support_below_canonical`

## 2. exact changes
- 변경 파일: `app/core/runtime/live_input_space.py`
- 추가:
  - `anchor_support_scope`
  - `anchor_family_additions`
  - `anchor_family_support_strength`
  - `compound_candidate_families`
  - `compound_support_scope`
- 적용:
  - `best_local_ref` 중심 same/nearby local_ref 기준 anchor family accumulation 추적
  - translation hit와 canonical support는 계속 분리 유지
  - same local_ref와 nearby local_ref를 구분한 compound state 계산
- 유지:
  - canonical 기준
  - possibility 기준
  - translation scope
  - control case 상태

## 3. verification
- review candidate:
  - `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode=possibility_candidate`
  - `translation_gate=true`
  - `processing_gate=true`
  - `observer_gate=true`
  - `canonical_anchor_gate=false`
  - `review_anchor_gap_class=multi_family_support_below_canonical`
  - `review_anchor_support_class=multi_family_same_local_ref_support_present`
  - `anchor_alignment_compound_state=multi_family_compound_candidate`
  - `anchor_support_scope=same_local_ref`
  - `anchor_family_additions.same_local_ref=[structural, process, object]`
  - `anchor_family_additions.nearby_local_ref=[]`
  - `compound_candidate_families=[structural, process, object]`
  - `compound_support_scope=same_local_ref`
  - `next_review_blocker=multi_family_support_below_canonical`
- control:
  - `engine_phase1_observer_probe_20260321 -> doc_004`
    - `review_state=translation_missing`
  - `engine_phase1_observer_probe_20260321 -> doc_005`
    - `review_state=translation_missing`
- canonical 유지:
  - `doc_004 -> doc_005`: `canonical`
  - `doc_005 -> doc_006`: `canonical`
  - `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`: `canonical`

## 4. current reading
- `doc_006`은 이제 semantic만 있는 후보가 아니다
- 같은 local_ref 안에서 structural/process/object family가 같이 붙는 `multi_family_compound_candidate`로 읽힌다
- 다만 이 support는 아직 canonical corroboration으로 인정되진 않고, `compound는 됐지만 canonical support strength가 아직 임계치 미만`인 상태다
- 즉 다음 엔진 우선순위는 translation이나 processing 재확장이 아니라, review candidate의 multi-family support를 canonical review 기준으로 어떻게 해석할지 분리하는 쪽이다

## 5. next recommendation
- 다음 축은 `anchor support accumulation` 추가 확장보다 `canonical review threshold split` 이다
- 즉 `doc_006`의 multi-family same-local_ref support를 canonical review 기준에서 어느 수준까지 인정할지, 그리고 왜 아직 canonical로는 안 올리는지 더 명시적으로 분리하는 게 맞다
