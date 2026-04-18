# Route Signature Schema v0

## 목적

이 문서는 line family 내부의 route를 기술하기 위한
최소 `route signature` 스키마를 고정한다.

핵심은 line을 단순 검색 대상으로 두지 않고,
현재 상황에 맞는 route를 선택할 수 있게 만드는 것이다.

## 최소 필드

- `route_id`
- `family_id`
- `route_name`
- `mode_class`
- `purpose_invariant`
- `activation_conditions`
- `exclusion_conditions`
- `current_position_schema`
- `next_decision_points`

## 보조 필드

- `primary_spaces`
- `input_signals`
- `expected_outputs`
- `fallback_routes`
- `residue_hooks`

## 필드 설명

### route_id

family 내부 route의 식별자

### family_id

어느 root family에 속하는지

### route_name

사람이 읽는 route 이름

### mode_class

이 route의 운용 모드 분류

예:

- `ingest`
- `preprocess`
- `reread`
- `validation`
- `readout`
- `search`

### purpose_invariant

이 route가 family 전체에서 맡는 변형 없는 목적

### activation_conditions

어떤 조건에서 이 route가 열리는지

### exclusion_conditions

어떤 조건이면 이 route를 열면 안 되는지

### current_position_schema

현재 상황을 이 route 안에서 어떻게 읽는지

### next_decision_points

이 route 끝에서 어떤 다음 판단 분기점이 생기는지

## 판단 규칙

### rule 1. route는 family의 목적을 바꾸지 않는다

route는 family의 목적을 수행하는 방식 차이지,
새 family가 아니다.

### rule 2. activation과 exclusion을 함께 적는다

활성 조건만 적으면 route가 과활성화된다.

### rule 3. next_decision_points가 있어야 route가 운용 가능해진다

route가 끝난 뒤 무엇을 고를지 보여주지 못하면
그건 설명 메모에 가깝다.

## JSON-shaped example

```json
{
  "route_id": "route_input_direct_ingest",
  "family_id": "fam_input_to_reading",
  "route_name": "direct ingest",
  "mode_class": "ingest",
  "purpose_invariant": "turn raw input into a visible, traceable readable entry without deeper shaping",
  "activation_conditions": [
    "input is readable enough for split-first entry",
    "no preprocess requirement is detected"
  ],
  "exclusion_conditions": [
    "raw transcript is too noisy",
    "preprocess-required verdict already exists"
  ],
  "current_position_schema": [
    "input_kind detected",
    "split_mode resolved",
    "readable board available"
  ],
  "next_decision_points": [
    "handoff to downstream reading",
    "escalate to preprocess shaping if residue remains high"
  ],
  "primary_spaces": [
    "input_ingest_space"
  ],
  "input_signals": [
    "input_kind",
    "split_mode"
  ],
  "expected_outputs": [
    "source_manifest",
    "split_units",
    "readable_input_board"
  ],
  "fallback_routes": [
    "route_preprocess_compare_first"
  ],
  "residue_hooks": [
    "ingest trace retained as entry residue"
  ]
}
```

## v0 기대 수준

v0는 route scheduler가 아니다.

하지만 아래는 가능해야 한다.

- 왜 이 route가 열리는지 설명 가능
- 왜 이 route를 닫아야 하는지 설명 가능
- route 끝에서 다음 분기점을 말할 수 있음

## 다음 단계 연결

이 스키마 다음에는
현재 family 3개에 대표 route를 실제로 붙이는 것이 자연스럽다.
