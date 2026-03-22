# engine definition and structure

## 1. what we built

우리가 만든 것은 단순한 `space viewer`가 아니다.  
우리가 만든 것은 입력을 받아 다음을 생성하고 보존하는 `연결 층위 엔진`이다.

- 입력기 output
- 라벨기 output
- 앵커기 output
- weak / strong / blocked connection tier
- review candidate
- promotion review
- blocker
- proposal trace
- canonical approval candidate

즉 이 엔진은 `무엇이 정답 연결인가`만 찾지 않는다.  
입력을 갈래로 나누고, 그 갈래 사이의 같음 / 유사 / 연결 가능 / 강한 연결 / 보류 자산을 함께 읽고 저장하는 엔진이다.

## 2. what this engine is not

- 최종 정답 분류기만이 아니다
- viewer 자체가 아니다
- canonical만 남기는 승인기만이 아니다
- 하나의 값으로 닫는 ontology 기계가 아니다

특히 `space`는 엔진 본체가 아니다.  
space는 이 엔진이 만든 연결 구조를 읽는 하나의 view 이다.

## 3. engine definition

이 엔진을 한 문장으로 정의하면 이렇다.

`입력기 + 라벨기 + 앵커기가 만든 반복 가능한 출력 위에서, 원본의 갈래와 갈래 사이의 연결 층위를 생성하고, weak trace / review / blocker / proposal / canonical approval 을 함께 저장하고 다시 읽을 수 있게 하는 연결 층위 엔진`

## 4. core philosophy

### 4-1. do not close too early
- canonical이 아니어도 버리지 않는다
- weak trace도 미래 가능성의 자산으로 본다
- blocked 상태도 이유와 함께 남긴다

### 4-2. process is also result
- 값 하나보다
  - 생성 과정
  - 변화 과정
  - 손실 과정
  - 번역 과정
  - 재해석 과정
을 추적 가능하게 남긴다

### 4-3. separate approval from space
- `canonical 승인 기준`과 `space 인정 기준`은 다르다
- 승인은 좁고 엄격하다
- space 인정은 더 넓고 가능성 중심이다

## 5. where we are now

현재 엔진은 `space 초입 checkpoint`까지 왔다.

핵심 상태:
- viewer는 Phase 1 freeze
- 엔진은 `none / possibility / review candidate / canonical` 층위를 분리
- `doc_006`은 `space pre-entry` review candidate
- `doc_005`, `doc_004`는 control 유지
- canonical controls는 안정적으로 유지

현재 대표 review candidate:
- `engine_phase1_observer_probe_20260321 -> doc_006`

현재 대표 control:
- `engine_phase1_observer_probe_20260321 -> doc_005`
- `engine_phase1_observer_probe_20260321 -> doc_004`

현재 대표 canonical controls:
- `doc_004 -> doc_005`
- `doc_005 -> doc_006`
- `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`

## 6. current state of doc_006

현재 `doc_006`은 이렇게 읽힌다.

- `bridge_mode = possibility_candidate`
- `translation_gate = true`
- `processing_gate = true`
- `observer_gate = true`
- `canonical_anchor_gate = false`
- `space_entry_state = structural_led_space_pre_entry`
- `space_entry_ready_families = [object, structural]`
- `space_entry_lead_family = structural`
- `space_entry_blocker = token_pair_exists_but_alignment_rule_not_satisfied`

즉 이 케이스는:
- canonical은 아니다
- 하지만 단순 weak trace도 아니다
- translation / processing / observer / same-local support / direct overlap candidate family를 모두 가진 `space 형성 후보`다

## 7. current state of controls

`doc_005`, `doc_004`는 현재 계속 control로 유지된다.

- `bridge_mode = none`
- `review_state = translation_missing`

이 control이 유지되기 때문에 `doc_006`을 과장하지 않고 읽을 수 있다.

## 8. engine tiers

현재 엔진 층위는 아래처럼 읽으면 된다.

### none
- 아직 space 형성 전
- 의미 있는 translation / processing / observer / family support가 부족

### possibility
- 약한 연결 가능성
- weak trace는 있으나 strong approval은 아님
- 버리지 않고 보존해야 하는 층위

### review candidate
- 구조적으로 의미 있는 연결 후보
- translation / processing / observer / anchor review가 분리되어 읽힘

### space pre-entry
- review candidate 중에서도 space 형성 쪽으로 더 올라온 상태
- internal support와 direct overlap candidate family가 있음
- 하지만 canonical direct overlap 승인 규칙은 아직 충족하지 않음

### canonical
- 승인된 강한 연결
- direct corroboration 과 family corroboration 이 닫힌 상태

## 9. policy mapping

사용자 정책 초안을 현재 엔진에 바로 매핑하면 아래와 같다.

### 같음
- `canonical`
- `direct canonical overlap`

### 유사
- family-level partial overlap
- typed anchor support
- semantic-only cross-path support

### 연결 가능
- `possibility_candidate`
- mixed review lane

### 강한 연결
- `multi_family_same_local_ref_support_present`
- `multi_family_compound_candidate`
- `direct_overlap_candidate_families`

### 보류 자산
- blocker
- promotion review
- proposal trace
- control trace
- `space_entry_state`

## 10. high-level data flow

현재 엔진 흐름은 대략 이렇게 읽으면 된다.

1. inputter
2. live_input
3. labeler
4. anchor / processing / observer materialization
5. imported/live material contract attachment
6. mixed pair evaluation
7. promotion review construction
8. threshold / corroboration / canonicalization review
9. direct overlap review
10. space entry reading

즉 입력은 곧바로 canonical로 닫히지 않고, review 가능한 여러 층위를 거쳐 읽힌다.

## 11. detailed runtime structure

핵심 구현 파일:
- [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)

핵심 진입점:
- `evaluate_mixed_path_pair` at [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):108

이 함수는 mixed live/imported pair를 평가하고, 아래 review builders를 통과시켜 구조화한다.

### promotion review builder
- `_build_promotion_review` at [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):798
- 역할:
  - 전체 review payload 조립
  - gate / anchor / threshold / cross-path / canonicalization / direct overlap / space entry 결과 통합

### threshold review
- `_build_threshold_review` at [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):1035
- 역할:
  - support density
  - corroboration scope
  - threshold gap
  를 분리

### cross-path review
- `_build_cross_path_review` at [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):1075
- 역할:
  - cross-path overlap count
  - family diversity
  - overlap quality
  - corroboration state
  분해

### anchor review
- `_build_anchor_review` at [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):1168
- 역할:
  - review candidate의 family support
  - missing types
  - subcritical types
  - compound state
  를 분리

### cross-path canonicalization review
- `_build_cross_path_canonicalization_review` at [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):1446
- 역할:
  - token-supported candidate
  - proposal trace
  - canonicalization candidate family
  - ready vs hint-only family
  를 분리

### direct overlap review
- `_build_direct_overlap_review` at [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):1551
- 역할:
  - direct overlap candidate family
  - token pair alignment state
  - canonicalizable pair count
  - family direct overlap blocker
  를 분리

### space entry review
- `_build_space_entry_review` at [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py):1661
- 역할:
  - current review candidate를 space 초입 상태로 읽을 수 있는지 분리

## 12. important engine fields

### gate layer
- `translation_gate`
- `processing_gate`
- `observer_gate`
- `canonical_anchor_gate`

### anchor review layer
- `review_anchor_gap_class`
- `review_anchor_support_class`
- `anchor_alignment_evidence`
- `anchor_alignment_missing_types`
- `anchor_alignment_subcritical_types`
- `anchor_alignment_compound_state`

### threshold layer
- `support_density_class`
- `corroboration_scope_class`
- `threshold_gap_class`
- `threshold_review_vector`

### cross-path corroboration layer
- `cross_path_overlap_family_count`
- `cross_path_overlap_quality_class`
- `cross_path_corroboration_state`
- `cross_path_threshold_gap_class`

### canonicalization layer
- `cross_path_canonicalization_candidate_families`
- `cross_path_canonicalization_candidate_class`
- `cross_path_canonicalization_gap_class`
- `cross_path_canonicalization_proposal_state`
- `cross_path_canonicalization_proposals`
- `cross_path_canonicalization_proposal_blockers`

### direct overlap layer
- `direct_overlap_candidate_families`
- `direct_overlap_gap_class`
- `family_direct_overlap_ready`
- `family_direct_overlap_blockers`
- `token_pair_alignment_state`
- `canonicalizable_token_pair_count`
- `family_rule_refinement_state`

### space layer
- `space_entry_state`
- `space_entry_vector`
- `space_entry_ready_families`
- `space_entry_lead_family`
- `space_entry_blocker`

## 13. what changed structurally across this phase

이 phase에서 확보한 구조적 전진은 아래다.

1. possibility lane 도입
2. review lane 도입
3. typed canonical review candidate 분리
4. same-local_ref accumulation 분리
5. threshold split
6. cross-path corroboration split
7. live-side support split
8. canonicalization candidate split
9. proposal trace 기록
10. direct overlap candidate split
11. family rule refinement split
12. space pre-entry 상태 분리

## 14. exact meaning of space

중요:
space는 엔진 자체가 아니다.

space는 아래를 읽는 one surface 이다.
- connection tier
- review lane
- proposal trace
- blocker
- pre-entry
- canonical approval

즉 같은 엔진 출력은 아래처럼도 읽을 수 있다.
- space view
- graph view
- review queue
- promotion trace
- ledger
- database query result

## 15. why this matters for ChatGPT / Gemini

외부 모델이 이 엔진을 이해할 때 중요한 건:

1. 이 엔진은 canonical만 만드는 엔진이 아니다
2. weak/blocked/review 상태도 의도적으로 저장한다
3. process is also result 이다
4. space는 본체가 아니라 surface다
5. `doc_006` 같은 케이스는 실패가 아니라 `space pre-entry review candidate`다

즉 외부 모델은 이 엔진을
`정답 추출기`가 아니라
`연결 층위 생성기 + 보류 자산 보존기 + review/promotion trace engine`
로 읽어야 한다.

## 16. what is still not done

아직 남은 것은 다음이다.

- `family canonicalization rule refinement`
- 특히 우선순위:
  - `structural`
  - 그 다음 `object`

즉 다음 phase는:
- translation 확대
- viewer 복귀
- processing 전역 재작업
이 아니라
- token-supported candidate를 어떤 조건에서 direct canonical overlap으로 인정할지
를 설계하는 정책/규칙 phase다

## 17. final definition

현재까지 만든 엔진을 최종적으로 정의하면 이렇다.

`vectorfl_replica의 현재 엔진은, 입력기/라벨기/앵커기의 반복 가능한 출력 위에서 원본의 갈래와 갈래 사이의 연결 층위를 생성하고, canonical / possibility / review / blocker / proposal / pre-entry를 함께 저장하며, 정답 승인과 공간 형성을 분리해서 읽는 연결 층위 엔진이다.`
