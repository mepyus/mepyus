# llm_response_structure_slot_catalog_v0

## purpose
LLM 답변에서 반복적으로 나타나는 판단 구조를
엔진이 견딜 수 있는 슬롯 단위로 압축해 기록한다.

## slot groups

### 1. 대상 규정
- `focus_object`
  - 지금 다루는 중심 대상
- `input_type`
  - 문서 / 사례 / 기능 후보 / 운영 기준 등 입력 종류
- `material_role`
  - 비교축 / 구조 추출 재료 / 점검기 / 보조 설명 재료
- `scope_note`
  - 이번 판독 범위 메모

### 2. 현재 상태 판정
- `current_reading`
  - 지금 이 입력을 어떻게 읽는가
- `maturity_state`
  - already / partial / early / defer 같은 성숙도
- `priority_note`
  - 지금 우선순위
- `overreach_risk`
  - 지금 붙이면 과한지 여부

### 3. 관계 판독
- `relation_kind`
  - 내부 분류값
- `same_meaning_hint`
- `same_context_hint`
- `different_flow_hint`
- `structure_borrowable`
- `weak_link_note`
- `hold_reason`
- `separated_reason`

### 4. 이유 서술
- `relation_reason`
- `borrow_reason`
- `not_adopted_reason`
- `boundary_reason`
- `evidence_trace_hint`

### 5. 사용 가능성
- `future_use_hint`
- `applicable_layer`
- `possible_feature_seed`
- `prompt_material_hint`
- `engine_refinement_hint`

### 6. 경계 설정
- `boundary_note`
- `do_not_adopt`
- `do_not_lock`
- `observer_limit`

### 7. 다음 단계
- `next_action_hint`
- `attachment_strategy`
- `defer_note`
- `bounded_next_step`

### 8. 사용자 언어 번역
- `user_language_summary`
- `plain_readout`
- `interpretation_note`

## example readout
- `focus_object`: Saltlux Goover 사례
- `material_role`: 구조 차용 재료
- `current_reading`: 같은 엔진은 아니지만 비교축으로 유효
- `relation_kind`: `STRUCTURE_BORROWABLE`
- `relation_reason`: 의미층과 실행층 분리 원리는 이미 우리 구조와 닿음
- `not_adopted_reason`: ontology 선고정은 현재 엔진과 흐름이 다름
- `future_use_hint`: 탐색 판독 예시, 비교축, 기능 후보 검토 재료
- `user_language_summary`: 구조는 빌릴 수 있지만 지금 그대로 이식하면 과하다

## recommended minimum subset
현재 엔진에 우선 붙일 최소 슬롯은 아래다.
- `focus_object`
- `input_type`
- `material_role`
- `current_reading`
- `relation_kind`
- `relation_reason`
- `structure_borrowable`
- `not_adopted_reason`
- `boundary_note`
- `future_use_hint`
- `next_action_hint`
- `user_language_summary`

## note
- 이 카탈로그의 목적은 좋은 문장을 모으는 것이 아니다.
- 판단 구조를 반복 가능한 값으로 바꾸는 것이 목적이다.
