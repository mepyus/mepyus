# cross path canonicalization proposal trace

## 1. current diagnosis
- `doc_006`은 `structural/object` family가 아예 없는 상태가 아니라, canonicalization proposal 까지는 가능하지만 아직 `hint-only` 단계다
- 즉 지금 남은 문제는 support 부재가 아니라 `proposal -> tokenized canonical overlap` 전환 미도달이다
- 가장 강한 blocker 는 그대로 `live_side_family_present_but_not_canonicalized` 다

## 2. exact changes
- 변경 파일: `app/core/runtime/live_input_space.py`
- 추가 필드:
  - `cross_path_canonicalization_proposal_state`
  - `cross_path_canonicalization_proposals`
  - `cross_path_canonicalization_proposal_blockers`
- 적용:
  - `best_local_ref` 범위에서 family별 proposal token 생성
  - proposal 단계 blocker 를 family별로 분리
- 유지:
  - canonical 기준
  - possibility 기준
  - local_ref translation scope

## 3. verification
- review candidate:
  - `engine_phase1_observer_probe_20260321 -> doc_006`
  - `bridge_mode=possibility_candidate`
  - `cross_path_canonicalization_proposal_state=hint_only_candidates_present`
  - `cross_path_canonicalization_candidate_class=multi_family_canonicalization_candidate`
  - `cross_path_canonicalization_ready_families=[]`
  - `cross_path_canonicalization_hint_only_families=[object, structural]`
  - `cross_path_canonicalization_proposals.object=[property, ontology, object]`
  - `cross_path_canonicalization_proposals.structural=[graph structure, rag structure, graph rag 구조, rag 구조]`
  - `cross_path_canonicalization_proposal_blockers.object=hint_only_needs_tokenization`
  - `cross_path_canonicalization_proposal_blockers.structural=imported_side_token_missing`
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
- `doc_006`은 이제 `structural/object`의 proposal token 까지는 생성 가능하다
- 하지만 아직 둘 다 direct canonical overlap 으로는 못 올라간다
- `object`는 양쪽 다 hint 는 있는데 token 이 비어 있어서 `hint_only_needs_tokenization`
- `structural`은 live 쪽 token 은 있지만 imported best_local_ref 쪽 direct token 이 비어 있어서 `imported_side_token_missing`
- 즉 다음 축은 translation 확대가 아니라
  - `best_local_ref` 범위의
  - `cross-path canonical tokenization / canonicalization refinement`
  쪽이다

## 5. next recommendation
- 다음 우선순위:
  - `doc_006 best_local_ref <-> live probe` 범위에서
  - `structural/object` family의 hint-only proposal 을 token-supported canonical overlap 으로 바꿀 수 있는지 보기
- 특히:
  - object: hint를 token으로 올리는 국소 tokenization
  - structural: imported side direct structural token 복원/정규화
