# policy executor code split map

## 1. purpose
- 이 문서는 [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py) 내부 역할을 1차로 나누어 보는 맵이다
- 목적은 전체 파일을 지금 당장 분해하는 것이 아니라, 어떤 부분이 executor 인지, 어떤 부분이 policy 인지, 어떤 부분이 output surface 인지 경계선을 먼저 잠그는 것이다

## 2. orchestration / executor
- 핵심 진입점:
  - `evaluate_mixed_path_pair`
- 성격:
  - material gather
  - pair selection
  - trace lookup
  - possibility basis 조립
  - policy 호출 순서 결정
  - 최종 payload 반환

### 현재 executor-heavy helper
- `_find_best_cross_path_trace`
- `_build_possibility_basis`
- `_build_translation_gap_details`
- `_build_promotion_blockers`
- `evaluate_mixed_path_pair`

## 3. policy logic
- 목적:
  - evidence 해석
  - readiness 판정
  - threshold 판단
  - canonicalization / overlap / review 분기

### 현재 policy-heavy helper
- `_build_anchor_review`
- `_build_threshold_review`
- `_build_cross_path_review`
- `_build_cross_path_canonicalization_review`
- `_build_direct_overlap_review`
- `_build_space_entry_review`

### 1차 분리된 policy
- [review_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policies.py)
  - `evaluate_promotion_review_policy`
  - translation / processing / observer / readiness / decision 관련 승인 정책을 얇게 분리

## 4. output surface
- 목적:
  - policy 결과를 현재 엔진의 readable review field 로 재조립
  - outward field 유지

### 현재 output-heavy helper
- `_build_promotion_review`

### 1차 분리된 output surface
- [review_output_surface.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_output_surface.py)
  - `assemble_promotion_review_surface`

## 5. new boundary artifacts
- [review_policy_types.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policy_types.py)
  - `PromotionPolicyContext`
  - `PromotionPolicyResult`
  - `PromotionReviewAssembly`

## 6. practical reading
- 현재 [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py) 는 아직 executor dominant 파일이다
- 하지만 이제 최소한
  - policy input
  - policy decision
  - output assembly
가 외부 callable unit 으로 분리되기 시작했다

## 7. next split candidates
- `cross_path overlap policy`
- `family canonicalization policy`
- `direct overlap promotion policy`
- 그 다음 `space entry policy`
