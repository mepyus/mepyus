# external_case_relation_reading_contract_v1

## purpose
외부 기술 사례가 공간에 들어왔을 때 단순 참고자료가 아니라
비교축 / 구조 차용 재료 / 분리 유지 판단 재료로 읽히도록
최소 판독 필드를 고정한다.

## minimum fields
- `focus_object`
- `material_role`
- `current_reading`
- `relation_kind`
- `relation_reason`
- `user_language_summary`
- `future_use_hint`
- `core_keep`
- `outer_keep`
- `hold_or_defer`

## relation kinds
- `STRUCTURE_BORROWABLE`
- `DIFFERENT_MEANING_SAME_CONTEXT`
- `SAME_CONTEXT_DIFFERENT_FLOW`
- `KEEP_SEPARATE_FOR_NOW`

## reading rule
- 외부 기술 사례는 기능 소개문으로만 읽지 않는다.
- 기존 공간과의 닿음, 차용 가능성, 분리 유지 이유를 같이 남긴다.
- 사례 상세를 코어에 넣지 말고, 판단 구조만 코어에 남긴다.

## note
이 계약의 목적은 외부 기술 사례를 복제 대상으로 읽게 하는 것이 아니라,
우리 엔진의 비교축과 탐색 판독 구조를 더 선명하게 만드는 데 있다.
