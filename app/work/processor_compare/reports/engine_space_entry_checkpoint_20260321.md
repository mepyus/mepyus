# engine space entry checkpoint

## 1. checkpoint intent
- 이 문서는 `viewer` 작업을 다시 여는 문서가 아니다
- 이 문서는 현재 엔진이 어디까지 왔는지 `space 초입` 기준으로 잠그는 문서다
- 핵심은 결과 하나를 선언하는 것이 아니라, 현재까지 확보한 연결 층위와 과정 자산을 고정하는 것이다

## 2. current locked state
- viewer는 Phase 1 freeze 유지
- 엔진은 `none / possibility / review candidate / canonical` 층위를 분리한 상태다
- weak trace, blocked reason, promotion review, proposal trace를 삭제하지 않고 보존한다
- `doc_006`은 `space pre-entry` 까지 도달한 review candidate다
- `doc_005`, `doc_004`는 control로 유지된다

## 3. fixed cases
- canonical controls
  - `doc_004 -> doc_005`
  - `doc_005 -> doc_006`
  - `test_live_space_sync_20260321 -> test_canonical_ingest_20260321`
- review candidate
  - `engine_phase1_observer_probe_20260321 -> doc_006`
- controls
  - `engine_phase1_observer_probe_20260321 -> doc_005`
  - `engine_phase1_observer_probe_20260321 -> doc_004`

## 4. current engine reading

### doc_006
- `bridge_mode = possibility_candidate`
- `translation_gate = true`
- `processing_gate = true`
- `observer_gate = true`
- `canonical_anchor_gate = false`
- `space_entry_state = structural_led_space_pre_entry`
- `space_entry_ready_families = [object, structural]`
- `space_entry_lead_family = structural`
- `space_entry_blocker = token_pair_exists_but_alignment_rule_not_satisfied`

### doc_005 / doc_004
- `bridge_mode = none`
- `review_state = translation_missing`
- control case로 유지된다

## 5. what has been structurally completed
1. possibility lane 도입
2. promotion review lane 도입
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

## 6. policy draft mapping

### 같음
- 현재 엔진 대응:
  - `canonical`
  - `direct canonical overlap`
- 의미:
  - 중심과 관점이 실제 canonical overlap으로 닫히는 층위

### 유사
- 현재 엔진 대응:
  - family-level partial overlap
  - typed anchor support
  - `semantic_only_cross_path`
- 의미:
  - 일부 family나 일부 갈래가 맞지만 direct canonical 승인까지는 가지 않은 층위

### 연결 가능
- 현재 엔진 대응:
  - `possibility_candidate`
  - translation / processing / observer gate를 통과한 mixed review candidate
- 의미:
  - 지금 당장 canonical은 아니지만 전이 가능성을 실제로 여는 층위

### 강한 연결
- 현재 엔진 대응:
  - `multi_family_same_local_ref_support_present`
  - `multi_family_compound_candidate`
  - `direct_overlap_candidate_families`
- 의미:
  - 여러 family가 동시에 같은 후보를 지지하는 높은 준비 상태

### 보류 자산
- 현재 엔진 대응:
  - blocker
  - promotion review
  - proposal trace
  - control trace
  - `space pre-entry`
- 의미:
  - 아직 승인되지 않았지만 미래 승격과 재해석의 재료로 남는 층위

## 7. why this is a valid stopping line
- 지금은 `왜 아직 canonical이 아닌가`를 높은 해상도로 설명할 수 있다
- `doc_006`은 더 이상 단순 possibility가 아니라 typed review candidate다
- `structural/object`는 hint-only를 넘어 token-supported candidate와 direct overlap candidate까지 분리됐다
- 남은 일은 해상도 상승이 아니라 `family canonicalization rule` 설계에 가깝다
- 즉 다음 수는 디버깅보다 정책/규칙 phase에 가깝다

## 8. strongest remaining blocker
- `doc_006`의 병목은 내부 support 부족이 아니다
- imported best local_ref 내부 multi-family support는 충분하다
- live 쪽 family도 일부 존재한다
- 남은 병목은:
  - `token_pair_exists_but_alignment_rule_not_satisfied`
  - 즉 canonicalization rule이 token-supported candidate를 direct canonical overlap으로 아직 승격하지 않는 점이다

## 9. what should not be reopened here
- viewer 확장
- region semantics 확장
- translation breadth 확대
- processing 전역 재정비
- canonical threshold 완화
- control case 상향 시도

## 10. next phase boundary
- 다음 phase의 본질은 `family canonicalization rule refinement` 이다
- 우선순위:
  - `structural`
  - 그 다음 `object`
- 즉 다음 phase는
  - direct canonical overlap을 어떤 규칙으로 인정할지
  - token-supported pair를 어떤 조건에서 canonicalizable direct overlap으로 볼지
  를 설계하는 엔진 정책 턴이다

## 11. final reading
- 현재 엔진은 아직 완전한 space engine 전체는 아니다
- 하지만 bridge 이후 레이어는 이미
  - 가능성 보존
  - review lane
  - blocker decomposition
  - proposal trace
  - pre-entry state
를 갖춘 `연결 층위 엔진`으로 읽힌다
- 따라서 지금은 `space 초입 checkpoint`로 잠그고,
  다음은 `canonicalization policy phase`로 넘기는 것이 맞다
