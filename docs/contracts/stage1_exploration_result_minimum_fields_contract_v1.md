# stage1_exploration_result_minimum_fields_contract_v1

## purpose
새 입력 1건을 응결핵처럼 넣었을 때
현재 엔진이 탐색 결과로 최소 무엇을 반환해야 하는지 고정한다.

## minimum fields
- `input_ref`
- `input_summary`
- `focus_anchor`
- `focus_labels`
- `focus_object`
- `related_assets`
- `relation_kind`
- `relation_reason`
- `same_meaning_hint`
- `same_context_hint`
- `different_flow_hint`
- `borrowable_structure`
- `not_adopted_reason`
- `separation_reason`
- `hold_reason`
- `write_trace`
- `related_run_ids`
- `related_session_ids`
- `evidence_refs`
- `future_use_hint`
- `record_target`

## field notes
- `related_assets`
  - 단순 path 목록이 아니라 asset role과 함께 남긴다.
- `relation_kind`
  - 내부 분류값.
- `relation_reason`
  - 왜 그렇게 읽혔는지 사용자 언어 전 단계 설명.
- `same_meaning_hint`
  - 정말 같은 의미로 읽히는지의 보수적 힌트.
- `same_context_hint`
  - 다른 의미지만 같은 작업면인지 여부.
- `different_flow_hint`
  - 같은 문제를 다른 방식으로 푸는지 여부.
- `borrowable_structure`
  - 차용 가능한 구조 / 방법 / 설계 원리.
- `not_adopted_reason`
  - 붙이지 말아야 할 이유.
- `write_trace`
  - receipt, provenance, observer, sidecar note 등 실제 기록 포인터.
- `record_target`
  - 이번 탐색 결과를 어디에 남길지.

## baseline relation kind set
- `SAME_MEANING`
- `DIFFERENT_MEANING_SAME_CONTEXT`
- `SAME_CONTEXT_DIFFERENT_FLOW`
- `STRUCTURE_BORROWABLE`
- `WEAK_LINK`
- `HOLD`
- `SEPARATED`

## output rule
- 내부 상태값만 반환하면 부족하다.
- 최소 한 줄 이상의 사용자 언어 설명을 같이 반환해야 한다.
- relation kind는 최종 답이 아니라 현재 판독 상태로 남긴다.
