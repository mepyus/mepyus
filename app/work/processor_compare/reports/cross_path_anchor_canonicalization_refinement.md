# cross path anchor canonicalization refinement

## 1. current diagnosis
- `doc_006`은 이제 단순 `semantic-only` 후보가 아니라, live 쪽에도 있는 `structural/object` family가 아직 canonical direct overlap 으로는 안 넘어간 상태로 읽힌다
- 즉 현재 병목은 family 부재가 아니라 `cross-path family present needs canonicalization` 이다
- 가장 강한 잔여 blocker 는 `live_side_family_present_but_not_canonicalized` 다

## 2. exact changes
- 변경 파일: `app/core/runtime/live_input_space.py`
- 추가 필드:
  - `cross_path_canonicalization_candidate_families`
  - `cross_path_canonicalization_candidate_class`
  - `cross_path_canonicalization_gap_class`
- 적용:
  - live side 와 imported candidate 쪽에 모두 존재하지만 direct overlap 으로는 아직 안 잡히는 family 를 `canonicalization candidate` 로 분리 기록
  - translation breadth 는 건드리지 않음
  - canonical / possibility threshold 는 그대로 유지

## 3. verification
- review candidate:
  - `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode=possibility_candidate`
  - `translation_gate=true`
  - `processing_gate=true`
  - `observer_gate=true`
  - `canonical_anchor_gate=false`
  - `live_side_support_class=multi_family_live_support_present`
  - `cross_path_overlap_quality_class=semantic_only`
  - `cross_path_threshold_gap_class=live_side_family_present_but_not_canonicalized`
  - `cross_path_uncorroborated_live_families=[structural, object]`
  - `cross_path_canonicalization_candidate_families=[structural, object]`
  - `cross_path_canonicalization_candidate_class=multi_family_canonicalization_candidate`
  - `cross_path_canonicalization_gap_class=cross_path_family_present_needs_canonicalization`
  - `next_review_blocker=live_side_family_present_but_not_canonicalized`
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
- `doc_006`은 imported 쪽 internal support 만 강한 후보가 아니다
- live 쪽에도 `structural/object` family 는 이미 있다
- 다만 그 family 들이 현재는 cross-path direct canonical overlap 으로 canonicalization 되지 않는다
- 따라서 다음 패치 방향은 `translation 확대`가 아니라 `cross-path anchor canonicalization refinement` 가 맞다

## 5. next recommendation
- 다음 우선순위:
  - `cross-path anchor canonicalization refinement`
- 그 안에서도 가장 좁은 시작점:
  - `doc_006 best_local_ref <-> live probe` 쌍에서
  - `structural/object` family 를 direct canonical overlap 으로 인정할 수 있는 derivation/canonicalization 규칙 보강
- 아직 하지 말 것:
  - document-wide translation
  - canonical threshold 완화
