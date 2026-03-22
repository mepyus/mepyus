# space entry review lane

## 1. current diagnosis
- `doc_006`은 이제 단순 review candidate가 아니라 `space pre-entry` 상태로 읽힌다
- 현재 상태는 `structural_led_space_pre_entry`
- 가장 강한 잔여 blocker 는 `token_pair_exists_but_alignment_rule_not_satisfied` 다

## 2. exact changes
- 변경 파일: `app/core/runtime/live_input_space.py`
- 추가 필드:
  - `space_entry_state`
  - `space_entry_vector`
  - `space_entry_ready_families`
  - `space_entry_lead_family`
  - `space_entry_blocker`
  - `space_entry_reason`
- 적용:
  - canonical 승격 없이 review layer 안에 `space entry` 초입 상태를 별도로 기록
- 유지:
  - canonical 기준
  - possibility 기준
  - control state

## 3. verification
- review candidate:
  - `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode=possibility_candidate`
  - `space_entry_state=structural_led_space_pre_entry`
  - `space_entry_vector.translation_gate=true`
  - `space_entry_vector.processing_gate=true`
  - `space_entry_vector.observer_gate=true`
  - `space_entry_vector.same_local_ref_support_strength=3`
  - `space_entry_vector.direct_overlap_candidate_count=2`
  - `space_entry_vector.canonicalizable_token_pair_count=4`
  - `space_entry_ready_families=[object, structural]`
  - `space_entry_lead_family=structural`
  - `space_entry_blocker=token_pair_exists_but_alignment_rule_not_satisfied`
  - `space_entry_reason=lead_family_is_closest_to_direct_canonical_overlap`
- control:
  - `engine_phase1_observer_probe_20260321 -> doc_005`
    - `bridge_mode=none`
    - `review_state=translation_missing`
- canonical 유지:
  - `doc_004 -> doc_005`: `canonical`
  - `doc_005 -> doc_006`: `canonical`
  - `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`: `canonical`

## 4. current reading
- `doc_006`은 이제 구조적으로 `space 초입` 까지는 왔다고 볼 수 있다
- translation / processing / observer / internal multi-family support / direct overlap candidate family 까지는 확보됐다
- 아직 없는 것은 `canonical direct overlap 승인 규칙` 이다

## 5. next recommendation
- 다음 우선순위:
  - `structural family canonicalization rule refinement`
- 그 다음:
  - `object family token pair promotion rule`
