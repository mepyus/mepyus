# Projection Line Schema v0

## 목적

이 문서는 `projection_line` 을
family invariant와 route signature 사이를 잇는 실제 객체로 정의한다.

projection line은
새 family가 아니라,
같은 root family 안에서
어느 면이 달라졌는지 드러내는 투영면이다.

## 왜 필요한가

지금 구조는 아래까지는 있다.

- bounded functional spaces
- upper family layer
- root family invariant
- route registry

하지만 아직 빠진 것이 있다.

- 같은 family 안의 reading / decision / residue / readout line이
  어떻게 다른지
- 어떤 facet가 달라졌는지
- 어느 space에서 주로 작동하는지
- 어느 route와 가장 먼저 연결되는지

이걸 잡는 객체가 `projection_line` 이다.

## projection line의 역할

projection line은 아래를 연결한다.

- `root family`
- `bounded space`
- `line facet`
- `route`

즉 projection line은
“이 family가 이 space 안에서 이 facet를 강조하며 어떤 route로 작동하는가”
를 보여주는 중간 단위다.

## 최소 필드

- `projection_id`
- `family_id`
- `projection_name`
- `projection_role`
- `projection_layer`
- `line_type`
- `changed_facets`
- `bounded_spaces`
- `preferred_routes`
- `projection_question`
- `projection_outputs`

## 보조 필드

- `material_sources`
- `residue_return_path`
- `related_projections`
- `activation_hints`
- `notes`

## 필드 설명

### projection_role

이 projection이 family 안에서 맡는 역할

예:

- `ingest_visibility`
- `preprocess_shaping`
- `latent_reread`
- `corridor_validation`
- `board_readout`
- `search_readout`

### projection_layer

이 projection의 층위

예:

- `entry`
- `validation`
- `decision`
- `readout`
- `residue`

### line_type

projection의 주된 line type

예:

- `reading_line`
- `structural_line`
- `decision_line`
- `residue_line`

### changed_facets

같은 family 안의 다른 projection과 비교했을 때
강조되거나 달라진 facet

예:

- `material_facet`
- `distinction_facet`
- `linkage_facet`
- `direction_facet`
- `operation_facet`
- `residue_facet`

### preferred_routes

이 projection이 우선적으로 연결되는 route들

### projection_question

이 projection이 family의 큰 질문을
자기 층위에서 다시 어떻게 묻는지

### projection_outputs

이 projection이 주로 만드는 산출/표면

## 판단 규칙

### rule 1. projection은 family invariant를 바꾸지 않는다

problem_field, core_distinction, transition_logic, judgment_question, completion_criterion은
root family에 속한다.

projection은 그걸 다른 층위나 면에서 수행한다.

### rule 2. projection 차이는 changed_facets와 preferred_routes로 본다

같은 family라도
무엇을 강조하는지와
어느 route로 주로 작동하는지가 다르면
다른 projection으로 본다.

### rule 3. projection은 local space를 가질 수 있지만 cross-space family를 끊지 않는다

같은 projection family가
서로 다른 bounded space에 걸쳐 있어도
same-root를 유지할 수 있다.

## JSON-shaped example

```json
{
  "projection_id": "proj_input_ingest_visibility",
  "family_id": "fam_input_to_reading",
  "projection_name": "input ingest visibility projection",
  "projection_role": "ingest_visibility",
  "projection_layer": "entry",
  "line_type": "reading_line",
  "changed_facets": [
    "material_facet",
    "direction_facet"
  ],
  "bounded_spaces": [
    "input_ingest_space"
  ],
  "preferred_routes": [
    "route_input_direct_ingest"
  ],
  "projection_question": "How does this raw input become visible and readable enough to enter the space?",
  "projection_outputs": [
    "source_manifest",
    "split_units",
    "readable_input_board"
  ],
  "material_sources": [
    "raw input document",
    "split units",
    "processing trace"
  ],
  "residue_return_path": "entry residue returns to future input shaping",
  "related_projections": [
    "proj_preprocess_shaping"
  ],
  "activation_hints": [
    "new input arrives",
    "direct ingest is viable"
  ]
}
```

## v0 기대 수준

v0는 완전한 graph registry가 아니다.

하지만 아래는 가능해야 한다.

- 같은 family 안의 projection 차이를 설명 가능
- projection이 어느 space와 route에 걸리는지 설명 가능
- 어떤 facet가 달라지는지 보여줄 수 있음

## 다음 단계 연결

이 스키마 다음에는
현재 family 3개에 대해 representative projection을 실제로 채운다.
