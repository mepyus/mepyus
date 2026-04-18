# llm_distillation_engine_attachment_feasibility_v0

## purpose
LLM 답변 구조 슬롯이 현재 엔진에 어디까지 붙을 수 있는지
bounded하게 평가한다.

## ALREADY_ATTACHABLE

### 1. `focus_object`
- current hook:
  - external case relation reading docs
  - exploration reports
- attachment:
  - docs/report level에서 이미 자연스럽게 사용 가능

### 2. `relation_kind`
- current hook:
  - [external_case_relation_reading_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/external_case_relation_reading_contract_v1.md)
  - [stage1_exploration_result_minimum_fields_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/stage1_exploration_result_minimum_fields_contract_v1.md)
- attachment:
  - contract/document level로는 이미 부착 가능

### 3. `relation_reason`
- current hook:
  - exploration reports
  - external case example docs
- attachment:
  - report / note / observer readout에 이미 수용 가능

### 4. `future_use_hint`
- current hook:
  - external case example
  - exploration one-turn readout
- attachment:
  - docs/report layer에서 바로 사용 가능

### 5. `user_language_summary`
- current hook:
  - Gemini observer summaries
  - external case reading docs
- attachment:
  - observer/guides/report layer에 바로 수용 가능

## ATTACHABLE_AS_SIDECAR

### 6. `material_role`
- why:
  - runtime 표준 필드로는 아직 약함
- attachment:
  - exploration sidecar json / observation note

### 7. `current_reading`
- why:
  - 현재는 문서 서술 관습에 머묾
- attachment:
  - runtime observation artifact

### 8. `structure_borrowable`
- why:
  - 현재 contracts에는 있으나 runtime 표준 기록이 없음
- attachment:
  - sidecar note field

### 9. `not_adopted_reason`
- why:
  - 보류/분리 이유가 통일 필드로 잠기지 않음
- attachment:
  - sidecar json or exploration note

### 10. `next_action_hint`
- why:
  - 계획 문서에는 있으나 탐색 결과물 필드로는 없음
- attachment:
  - exploration observation artifact

## DOCUMENT_ONLY_FOR_NOW

### 11. `overreach_risk`
- reading:
  - 지금은 정책/기준문에서만 관리하는 편이 안전함

### 12. `do_not_lock`
- reading:
  - 코어 값보다는 선언/기준문 레이어에서 계속 관리하는 것이 적절함

### 13. `observer_limit`
- reading:
  - Gemini 역할 계약, observer policy 쪽 문서 관리가 우선

## NOT_NEEDED_YET

### 14. `possible_feature_seed`
- reading:
  - 아직 코어에 넣을 필요 없음. 리포트 문장 수준이면 충분함

### 15. `prompt_material_hint`
- reading:
  - 현재는 guides / prompt docs에서 다루면 충분함

## recommendation
- 지금 필요한 건 새 지능 부품이 아니다.
- 가장 안전한 다음 단계는 `exploration/llm-distillation sidecar` 를 붙여
  반복 슬롯을 구조화해 누적하는 것이다.
- 코어에는 최소 판단 슬롯만 남기고,
  풍부한 문장 설명은 observer/report layer로 유지하는 것이 맞다.
