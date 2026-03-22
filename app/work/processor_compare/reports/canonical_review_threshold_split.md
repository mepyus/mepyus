# canonical review threshold split

## 1. current diagnosis
- `doc_006`은 이제 `same_local_ref` 안에서 `structural / process / object` family support가 모두 붙는 `multi_family_compound_candidate`다
- 하지만 canonical review 기준으로 보면, 실제 cross-path canonical anchor overlap count는 아직 `1` 이다
- 따라서 현재 가장 강한 review threshold blocker는 `cross_path_anchor_overlap_below_threshold` 다
- control:
  - `doc_004`, `doc_005`는 여전히 `translation_missing`

## 2. exact changes
- 변경 파일: `app/core/runtime/live_input_space.py`
- 추가:
  - `support_density_class`
  - `corroboration_scope_class`
  - `threshold_gap_class`
  - `threshold_review_vector`
- 적용:
  - same/nearby local_ref support strength를 threshold review로 분리
  - multi-family support와 actual cross-path anchor overlap count를 분리 기록
  - canonical 기준은 유지
- 유지:
  - canonical lane
  - possibility lane
  - translation scope
  - control case 상태

## 3. verification
- review candidate:
  - `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode=possibility_candidate`
  - `review_anchor_support_class=multi_family_same_local_ref_support_present`
  - `anchor_alignment_compound_state=multi_family_compound_candidate`
  - `support_density_class=dense_same_local_ref`
  - `corroboration_scope_class=same_local_ref`
  - `threshold_gap_class=cross_path_anchor_overlap_below_threshold`
  - `threshold_review_vector.same_local_ref_support_strength=3`
  - `threshold_review_vector.nearby_local_ref_support_strength=0`
  - `threshold_review_vector.canonical_anchor_alignment_count=1`
  - `next_review_blocker=cross_path_anchor_overlap_below_threshold`
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
- `doc_006`은 support density 자체는 약하지 않다
- 문제는 `same_local_ref multi-family support`가 있어도, 그 support가 live 쪽과 직접 compound 되는 canonical anchor overlap로는 아직 충분히 변환되지 않았다는 점이다
- 즉 다음 병목은 translation도 processing도 accumulation도 아니라, `cross-path anchor corroboration threshold` 그 자체다

## 5. next recommendation
- 다음 축은 `canonical review threshold`를 더 분리하는 것이다
- 구체적으로는
  - multi-family same-local_ref support를 어느 정도면 canonical review 통과 후보로 볼지
  - cross-path direct anchor overlap count를 몇 개까지 요구할지
  - translation-hit semantic과 non-semantic family를 어떻게 corroboration으로 인정할지
  를 엔진 기준으로 더 명확히 나누는 쪽이 맞다
