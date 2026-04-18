# llm_standard_doc_structure_slot_mapping_v0

## purpose
LLM 답변 구조와
사용자 표준 문서 구조(선언문 / 기준문 / 지시서)가
어디서 겹치고 어디서 갈라지는지 정리한다.

## declaration extractable slots
- `why_this_exists`
- `top_direction`
- `what_to_protect`
- `what_not_to_become`
- `value_axis`
- `future_use_orientation`

## baseline extractable slots
- `current_state_reading`
- `allowed_vs_forbidden`
- `relation_rule`
- `operation_principle`
- `boundary_note`
- `lock_level`

## directive extractable slots
- `purpose`
- `scope`
- `review_questions`
- `expected_outputs`
- `forbidden_actions`
- `success_condition`
- `next_action_hint`

## overlapping slots
- `current_reading`
  - 기준문과 LLM 답변 둘 다 현재 상태 판정을 수행함
- `relation_reason`
  - 기준문, 외부 사례 readout, LLM 답변 모두 이유 서술을 가짐
- `boundary_note`
  - 선언문/기준문/지시서/LLM 답변 모두 경계 설정이 반복됨
- `future_use_hint`
  - 외부 사례 readout, 탐색 readout, LLM 보강 답변에서 반복됨
- `next_action_hint`
  - 지시서와 LLM 보조 답변이 강하게 공유
- `user_language_summary`
  - 선언문/예시문/observer 요약에 이미 반쯤 존재

## slots stronger in standard docs
- `lock_level`
- `forbidden_actions`
- `success_condition`
- `what_to_protect`
- `what_not_to_become`

## slots stronger in llm-style responses
- `plain_readout`
- `comparison framing`
- `candidate alternatives`
- `uncertainty phrasing`
- `summary compression`

## newly worth locking as shared engine slots
- `focus_object`
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

## reading
- 새 이론이 필요한 것이 아니다.
- 사용자 문서 구조와 LLM 답변 구조는 이미 상당 부분 겹친다.
- 따라서 핵심은 반복되는 슬롯을 엔진용 추출 스키마로 고정하는 것이다.
