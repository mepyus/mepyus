# cross path canonicalization process log

## 목적
- 이 문서는 `doc_006`을 canonical로 올렸다는 기록이 아니다
- 이 문서는 `doc_006`이 왜 아직 canonical이 아닌지, 그 과정이 어떻게 분해되어 왔는지를 남기는 로그다
- 즉 결과보다 과정, 승격보다 보류 구조를 기록한다

## 고정 대상
- review candidate:
  - `engine_phase1_observer_probe_20260321 -> doc_006`
- control:
  - `engine_phase1_observer_probe_20260321 -> doc_005`
  - `engine_phase1_observer_probe_20260321 -> doc_004`
- canonical controls:
  - `doc_004 -> doc_005`
  - `doc_005 -> doc_006`
  - `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`

## 과정 로그

### 1. possibility lane 진입
- 상태:
  - `bridge_mode = possibility_candidate`
- 의미:
  - canonical은 아니지만 weak trace를 버리지 않고 가능성 lane에 보존
- 핵심:
  - `doc_006`만 possibility로 올라가고 `doc_005/doc_004`는 control로 남음

### 2. translation / processing / observer gate 분리
- 상태:
  - `translation_gate = true`
  - `processing_gate = true`
  - `observer_gate = true`
  - `canonical_anchor_gate = false`
- 의미:
  - `doc_006`의 병목은 translation/processing/observer가 아니라 anchor review로 좁혀짐

### 3. typed canonical review candidate 분리
- 상태:
  - `promotion_readiness_class = anchor_alignment_pending`
  - `promotion_decision = review_canonical_anchor_alignment`
- 의미:
  - 단순 possibility가 아니라 canonical review candidate로 읽히기 시작함

### 4. anchor family review split
- 상태:
  - 초기에는 `semantic_anchor_present_but_subcritical`
  - `semantic_overlap = [graph, rag]`
- 의미:
  - semantic family만 direct support로 잡히고 다른 family는 비어 있음

### 5. same-local_ref accumulation
- 상태:
  - `anchor_support_scope = same_local_ref`
  - `anchor_family_additions.same_local_ref = [structural, process, object]`
  - `anchor_alignment_compound_state = multi_family_compound_candidate`
- 의미:
  - imported best local_ref 내부에서는 semantic 외 family가 실제로 모임
- 전환점:
  - 병목이 internal support 부족에서 cross-path 부족으로 이동

### 6. threshold split
- 상태:
  - `support_density_class = dense_same_local_ref`
  - `threshold_gap_class = cross_path_anchor_overlap_below_threshold`
- 의미:
  - same-local_ref 내부 밀도는 충분하지만 cross-path canonical overlap count는 부족

### 7. cross-path corroboration split
- 상태:
  - `cross_path_overlap_family_count = 1`
  - `cross_path_overlap_quality_class = semantic_only`
  - `cross_path_corroboration_state = semantic_only_cross_path`
  - `cross_path_threshold_gap_class = cross_path_family_diversity_below_threshold`
- 의미:
  - 내부 multi-family support와 외부 direct corroboration을 분리해 읽게 됨

### 8. live-side support split
- 상태:
  - `live_side_support_class = multi_family_live_support_present`
  - `live_side_support_families = [semantic, structural, object]`
  - `cross_path_uncorroborated_live_families = [structural, object]`
  - `next_review_blocker = live_side_family_present_but_not_canonicalized`
- 의미:
  - live 쪽 family가 없는 게 아니라, direct canonical overlap으로 안 넘어가는 상태로 좁혀짐

### 9. canonicalization candidate 분리
- 상태:
  - `cross_path_canonicalization_candidate_class = multi_family_canonicalization_candidate`
  - `cross_path_canonicalization_candidate_families = [structural, object]`
  - `cross_path_canonicalization_gap_class = cross_path_family_present_needs_canonicalization`
- 의미:
  - 이제 structural/object는 단순 missing이 아니라 canonicalization 후보임

### 10. proposal trace 분리
- 상태:
  - `cross_path_canonicalization_proposal_state = hint_only_candidates_present`
  - `cross_path_canonicalization_proposals.object = [property, ontology, object]`
  - `cross_path_canonicalization_proposals.structural = [graph structure, rag structure, graph rag 구조, rag 구조]`
  - `cross_path_canonicalization_proposal_blockers.object = hint_only_needs_tokenization`
  - `cross_path_canonicalization_proposal_blockers.structural = imported_side_token_missing`
- 의미:
  - 이제 `왜 안 되는지`가 아니라 `무엇을 canonical token/support로 바꿔야 하는지`까지 기록됨

### 11. live-side family present but not canonicalized
- 상태:
  - `live_side_support_class = multi_family_live_support_present`
  - `cross_path_uncorroborated_live_families = [structural, object]`
  - `cross_path_canonicalization_candidate_class = multi_family_canonicalization_candidate`
- 의미:
  - live 쪽 family 부재가 아니라 direct cross-path canonicalization 부재로 병목이 더 좁혀짐

### 12. partial tokenization progress
- 상태:
  - `cross_path_canonicalization_proposal_state = partial_tokenization_progress`
  - `cross_path_canonicalization_ready_families = [structural]`
  - `cross_path_canonicalization_hint_only_families = [object]`
  - `cross_path_canonicalization_proposal_blockers.object = hint_only_needs_tokenization`
- 의미:
  - `structural` 은 best_local_ref 범위에서 token-supported candidate 까지 올라옴
  - `object` 는 아직 hint-only 단계라 다음 canonicalization 대상이 더 분명해짐

### 13. token-supported candidate expansion
- 상태:
  - `cross_path_canonicalization_proposal_state = token_supported_candidates_present`
  - `cross_path_canonicalization_ready_families = [object, structural]`
  - `cross_path_canonicalization_hint_only_families = []`
- 의미:
  - `object` 도 best_local_ref 범위에서 token-supported candidate 로 올라옴
  - 이제 병목은 family canonicalization 후보 부재가 아니라
    `token-supported candidate -> direct canonical overlap`
    전환 문제로 더 좁혀짐

### 14. direct overlap candidate split
- 상태:
  - `direct_overlap_candidate_families = [object, structural]`
  - `direct_overlap_gap_class = token_pair_exists_but_alignment_rule_not_satisfied`
  - `token_pair_alignment_state = candidate_pairs_present_but_noncanonical`
  - `canonicalizable_token_pair_count = 4`
- 의미:
  - 이제 `object/structural` 둘 다 direct overlap 후보이며, 실제 token pair 도 존재한다
  - 하지만 현재 review/canonicalization 규칙은 이 pair를 아직 canonical direct overlap 으로 승격하지 않는다

### 15. family rule refinement split
- 상태:
  - `family_rule_refinement_state.structural = one_side_direct_one_side_derived`
  - `family_rule_refinement_state.object = both_sides_derived_pair`
  - `direct_overlap_candidate_lead_family = structural`
- 의미:
  - 이제 `structural`과 `object`를 같은 refinement 대상으로 보지 않는다
  - `structural`이 더 앞서 있고, `object`는 더 보수적으로 다뤄야 한다

### 16. space pre-entry
- 상태:
  - `space_entry_state = structural_led_space_pre_entry`
  - `space_entry_ready_families = [object, structural]`
  - `space_entry_blocker = token_pair_exists_but_alignment_rule_not_satisfied`
- 의미:
  - `doc_006`은 review lane 안에서 구조적으로 `space 초입`까지는 도달했다
  - 남은 것은 승격이 아니라 canonical direct overlap 승인 규칙이다

## control 유지 의미
- `doc_005`, `doc_004`는 계속 `translation_missing`
- 이 control들이 유지되기 때문에 `doc_006`의 승격 직전 상태를 과장하지 않고 읽을 수 있음

## 현재 판정
- `doc_006`은 canonical이 아니다
- 하지만 단순 possibility도 아니다
- 현재는:
  - translation 통과
  - processing 통과
  - observer 통과
  - imported same-local_ref 내부 multi-family support 확보
  - live side multi-family support 존재 확인
  - cross-path semantic overlap 확보
  - structural/object canonicalization candidate 및 proposal trace 확보
- 아직 남은 것:
  - `object canonicalizable token pair -> direct canonical overlap`
  - `structural canonicalizable token pair -> direct canonical overlap`
  - 단, 순서는 `structural -> object`

## 다음 자연스러운 수
- `doc_006 best_local_ref <-> live probe` 범위에서
  - object hint-to-token conversion
  - imported-side structural token recovery
- 중요한 점:
  - 이 다음 작업도 `canonical 자동 승격`이 아니라
  - canonicalization 과정의 다음 단계를 기록하는 작업이어야 함
