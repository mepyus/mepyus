# cross path canonicalization candidate review

## 1. current diagnosis
- `doc_006`은 live/imported 양쪽에 `structural/object` family 가 모두 존재하지만, 아직 direct canonical overlap 으로는 안 잡히는 상태다
- 현재 이 family 들은 `canonicalization candidate` 로는 보이지만, `token-supported` 가 아니라 `text-hint-supported` 수준이다
- 가장 강한 잔여 blocker 는 그대로 `live_side_family_present_but_not_canonicalized` 다

## 2. exact changes
- 변경 파일: `app/core/runtime/live_input_space.py`
- 추가 필드:
  - `cross_path_canonicalization_scope`
  - `cross_path_canonicalization_strengths`
  - `cross_path_canonicalization_evidence`
  - `cross_path_canonicalization_ready_families`
  - `cross_path_canonicalization_hint_only_families`
- 적용:
  - `best_local_ref` 범위에서만 review 용 canonicalization evidence 분리
  - `token-supported` 와 `text-hint-supported` 를 구분
- 유지:
  - canonical 기준
  - possibility 기준
  - local_ref translation scope

## 3. verification
- review candidate:
  - `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode=possibility_candidate`
  - `cross_path_canonicalization_candidate_class=multi_family_canonicalization_candidate`
  - `cross_path_canonicalization_scope=best_local_ref`
  - `cross_path_canonicalization_ready_families=[]`
  - `cross_path_canonicalization_hint_only_families=[object, structural]`
  - `cross_path_canonicalization_strengths.object=text_hint_supported`
  - `cross_path_canonicalization_strengths.structural=text_hint_supported`
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
- `doc_006`의 `structural/object` 는 없는 게 아니다
- 하지만 지금은 `best_local_ref` 범위에서
  - direct token overlap 으로 canonicalizable 하진 않고
  - 양쪽 텍스트 힌트로만 연결 가능한 후보 상태다
- 즉 다음 병목은 translation 폭이 아니라
  - `text hint -> canonical token/support` 변환
  - 즉 `cross-path anchor canonicalization refinement`
  쪽이다

## 5. next recommendation
- 다음 우선순위:
  - `doc_006 best_local_ref <-> live probe` 범위의 `cross-path anchor canonicalization refinement`
- 구체적으로는:
  - `structural/object` family 에 대해
  - hint-only 상태를 token-supported canonical overlap 으로 바꿀 수 있는지
  - local scope 에서만 시험하는 게 맞다
