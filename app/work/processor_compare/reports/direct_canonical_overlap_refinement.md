# direct canonical overlap refinement

## 1. current diagnosis
- `doc_006`은 이제 `structural/object` family 모두 `token-supported candidate` 이고, direct overlap candidate 까지 잡힌다
- 하지만 아직 canonical direct overlap 으로는 인정되지 않는다
- 가장 강한 잔여 blocker 는 `token_pair_exists_but_alignment_rule_not_satisfied` 다
- 현재 상태에서는 `structural`과 `object`가 거의 같은 병목을 가진다

## 2. exact changes
- 변경 파일: `app/core/runtime/live_input_space.py`
- 추가 필드:
  - `direct_overlap_candidate_families`
  - `direct_overlap_gap_class`
  - `direct_overlap_evidence`
  - `family_canonicalization_strengths`
  - `family_direct_overlap_ready`
  - `family_direct_overlap_blockers`
  - `token_pair_alignment_state`
  - `live_anchor_form_state`
  - `canonicalizable_token_pair_count`
  - `noncanonical_token_pair_count`
  - `family_mapping_state`
- 적용:
  - family별로 token-supported candidate 가 direct overlap 후보인지 분리
  - token pair 는 있는데 왜 아직 canonical direct overlap 이 아닌지 기록
- 유지:
  - canonical 기준
  - possibility 기준
  - local_ref translation scope

## 3. verification
- review candidate:
  - `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode=possibility_candidate`
  - `direct_overlap_candidate_families=[object, structural]`
  - `direct_overlap_gap_class=token_pair_exists_but_alignment_rule_not_satisfied`
  - `family_direct_overlap_ready.object=false`
  - `family_direct_overlap_ready.structural=false`
  - `family_direct_overlap_blockers.object=token_pair_exists_but_alignment_rule_not_satisfied`
  - `family_direct_overlap_blockers.structural=token_pair_exists_but_alignment_rule_not_satisfied`
  - `token_pair_alignment_state=candidate_pairs_present_but_noncanonical`
  - `live_anchor_form_state=present`
  - `canonicalizable_token_pair_count=4`
  - `noncanonical_token_pair_count=4`
  - `family_mapping_state=canonicalizable_pairs_present`
- direct overlap evidence:
  - `object.canonicalizable_token_pairs=[object, ontology, property]`
  - `structural.canonicalizable_token_pairs=[rag 구조]`
  - `direct_overlap_tokens=[]`
- control:
  - `engine_phase1_observer_probe_20260321 -> doc_005`
    - `bridge_mode=none`
    - `review_state=translation_missing`
- canonical 유지:
  - `doc_004 -> doc_005`: `canonical`
  - `doc_005 -> doc_006`: `canonical`
  - `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`: `canonical`

## 4. current reading
- `doc_006`은 이제 direct overlap candidate family가 분명하다
- `object`와 `structural` 둘 다 token pair 자체는 있다
- 그런데 현재 canonical review는 이 pair들을 아직 direct canonical overlap 증거 형식으로 승격하지 않는다
- 즉 남은 병목은 translation 폭이 아니라
  - family별 canonicalization rule
  - token pair normalization / promotion
  쪽이다

## 5. next recommendation
- 다음 우선순위:
  - `family canonicalization rule refinement`
- 구체적으로는:
  - `object`: `property / ontology / object` token pair 를 direct canonical overlap 으로 인정할 최소 규칙
  - `structural`: `rag 구조` 같은 pair를 direct corroboration 으로 올릴 최소 규칙
- 지금 단계에서는 viewer나 translation 확대보다 이 규칙 분리가 더 맞다
