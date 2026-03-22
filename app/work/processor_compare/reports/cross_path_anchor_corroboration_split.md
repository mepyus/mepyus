# cross path anchor corroboration split

## 1. current diagnosis
- `doc_006`은 same-local_ref 내부 support 부족으로 막힌 상태가 아니다
- 현재 상태는 `dense same-local_ref multi-family support` 가 이미 있으나, live 쪽과 직접 겹치는 canonical corroboration 이 `semantic` family 1종뿐인 상태다
- 가장 강한 잔여 threshold blocker 는 `cross_path_family_diversity_below_threshold` 다
- control cases:
  - `doc_004`, `doc_005` 는 여전히 `translation_missing`

## 2. exact changes
- 변경 파일: `app/core/runtime/live_input_space.py`
- 추가 필드:
  - `cross_path_overlap_family_count`
  - `cross_path_overlap_quality_class`
  - `cross_path_corroboration_state`
  - `cross_path_threshold_gap_class`
  - `cross_path_overlap_families`
  - `cross_path_missing_families`
  - `cross_path_subcritical_families`
  - `cross_path_overlap_evidence`
- 추가: `translation_gate / processing_gate / observer_gate / canonical_anchor_gate` 를 `promotion_review` top-level 에 다시 노출
- 적용: same-local_ref 내부 support 와 cross-path canonical corroboration 을 분리 기록
- 적용: translation-assisted hit 와 canonicalizable overlap 을 분리 기록
- 유지: canonical 기준
- 유지: possibility 기준
- 유지: translation scope
- 유지: control case state

## 3. verification
- review candidate:
  - `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode=possibility_candidate`
  - `translation_gate=true`
  - `processing_gate=true`
  - `observer_gate=true`
  - `canonical_anchor_gate=false`
  - `review_anchor_support_class=multi_family_same_local_ref_support_present`
  - `anchor_alignment_compound_state=multi_family_compound_candidate`
  - `support_density_class=dense_same_local_ref`
  - `corroboration_scope_class=same_local_ref`
  - `cross_path_overlap_family_count=1`
  - `cross_path_overlap_quality_class=semantic_only`
  - `cross_path_corroboration_state=semantic_only_cross_path`
  - `cross_path_threshold_gap_class=cross_path_family_diversity_below_threshold`
  - `cross_path_overlap_families=[semantic]`
  - `cross_path_missing_families=[structural, process, object]`
  - `cross_path_subcritical_families=[semantic]`
  - `cross_path_overlap_evidence.canonicalizable_overlap_count=2`
  - `cross_path_overlap_evidence.translation_assisted_overlap_count=1`
  - `cross_path_overlap_evidence.translated_but_not_canonicalized_count=0`
  - `cross_path_overlap_evidence.raw_anchor_overlap_count=2`
  - `cross_path_overlap_evidence.derived_anchor_overlap_count=1`
  - `cross_path_overlap_evidence.translated_handles=[rag]`
  - `next_review_blocker=cross_path_family_diversity_below_threshold`
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
- `doc_006`은 내부 support 부족으로 막힌 후보가 아니다
- imported 쪽 same-local_ref 안에서는 semantic + structural + process + object support 가 이미 review candidate 수준으로 모여 있다
- 하지만 live 쪽과 직접 canonical corroboration 으로 겹치는 것은 아직 `semantic` family 뿐이다
- 즉 지금 막힘은 `same-local_ref dense support` 와 `cross-path direct corroboration` 의 차이에서 온다
- 번역 적중은 있고 `rag` 는 실제로 translation-assisted overlap 으로 잡히지만, 그것만으로는 cross-path family diversity 를 만들지 못한다
- 따라서 현재 `doc_006`은 `semantic-only cross-path overlap` 상태의 typed canonical review candidate 로 읽힌다

## 5. next recommendation
- 다음 축은 translation breadth 가 아니라 `cross-path anchor canonicalization/support` 쪽이다
- 우선순위 후보:
  - live-side anchor support accumulation
  - cross-path anchor canonicalization refinement
  - canonical review threshold 분해 한 턴 더
- 지금 단계에서 가장 맞는 한 줄은:
  - `내부 multi-family support 는 충분하지만, live 쪽 direct corroboration family diversity 가 아직 얇다`
