# family canonicalization rule refinement

## 1. current diagnosis
- `doc_006`의 `object/structural` 둘 다 direct overlap candidate 이지만 상태는 같지 않다
- `structural`은 `one_side_direct_one_side_derived`
- `object`는 `both_sides_derived_pair`
- 따라서 현재는 `structural`이 `object`보다 direct canonical overlap 에 더 가깝다

## 2. exact changes
- 변경 파일: `app/core/runtime/live_input_space.py`
- 추가 필드:
  - `family_rule_refinement_state`
  - `direct_overlap_candidate_lead_family`
- 적용:
  - family별 direct overlap 후보의 rule 상태를 분리
  - 어느 family가 먼저 canonicalization refinement 대상인지 출력만 보고 읽히게 함
- 유지:
  - canonical 기준
  - possibility 기준
  - local_ref translation scope

## 3. verification
- review candidate:
  - `engine_phase1_observer_probe_20260321 -> doc_006`
  - `direct_overlap_candidate_families=[object, structural]`
  - `family_rule_refinement_state.object=both_sides_derived_pair`
  - `family_rule_refinement_state.structural=one_side_direct_one_side_derived`
  - `direct_overlap_candidate_lead_family=structural`
  - `family_direct_overlap_blockers.object=token_pair_exists_but_alignment_rule_not_satisfied`
  - `family_direct_overlap_blockers.structural=token_pair_exists_but_alignment_rule_not_satisfied`
  - `next_review_blocker=live_side_family_present_but_not_canonicalized`
- control:
  - `engine_phase1_observer_probe_20260321 -> doc_005`
    - `bridge_mode=none`
    - `review_state=translation_missing`
- canonical 유지:
  - `doc_004 -> doc_005`: `canonical`
  - `doc_005 -> doc_006`: `canonical`
  - `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`: `canonical`

## 4. current reading
- `structural`은 live 쪽에서 직접 form 이 이미 있고 imported 쪽만 derived 보강이라 더 앞선다
- `object`는 live/imported 양쪽이 모두 derived token pair 이라 더 조심스럽게 봐야 한다
- 즉 다음 refinement 가 같은 강도로 갈 게 아니라 family별로 달라져야 한다

## 5. next recommendation
- 다음 우선순위:
  - `structural` family canonicalization rule refinement
- 그 다음:
  - `object` family token pair promotion 기준 분리
- 지금 단계에서 translation breadth 확대는 불필요하다
