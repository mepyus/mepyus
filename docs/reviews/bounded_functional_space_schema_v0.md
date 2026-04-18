# Bounded Functional Space Schema v0

## 목적

이 문서는 `bounded functional space` 를
현재 VectorFL 메인 공간 안에서 실제로 기술하기 위한
최소 공통 스키마를 고정한다.

이 스키마는 폴더 분류용이 아니라
`어떤 기능 공간이 어떤 root issue를 받고, 어떤 family를 자라게 하며, 어떤 route와 action을 제공하는가`
를 적기 위한 것이다.

## 핵심 원칙

- bounded functional space는 line 저장소가 아니다
- 특정 도메인의 issue-root가 들어와 family로 자라는 운용 구역이다
- 각 space는 purpose, entry, route, action, residue를 최소한 설명할 수 있어야 한다

## 최소 필드

### 1. identity

- `space_id`
- `space_name`
- `space_status`

`space_status` 후보:

- `candidate`
- `emergent`
- `active`
- `frozen`

### 2. purpose

- `space_purpose`
- `bounded_question`

`bounded_question` 은
이 space가 반복적으로 답하려는 질문을 적는다.

### 3. scope

- `scope_objects`
- `excluded_scope`

여기서 중요한 건
무엇을 다루는지만이 아니라
무엇을 이 공간에서 일부러 다루지 않는지도 적는 것이다.

### 4. surfaces

- `state_surface`
- `action_surface`
- `evidence_paths`

정의:

- `state_surface`: 현재 상태를 읽는 면
- `action_surface`: 사람이 보거나 시스템이 실행할 수 있는 조작/진입 면
- `evidence_paths`: 이 space가 실제로 존재함을 보여주는 경로

### 5. root entry

- `root_entry_conditions`
- `root_entry_examples`

`root_entry_conditions` 는 어떤 상황에서 이 space가 열린다고 판단하는지,
`root_entry_examples` 는 대표적 입구 사례를 적는다.

### 6. family and routing

- `family_domains`
- `route_modes`
- `activation_signals`

정의:

- `family_domains`: 이 space 안에서 자라는 family 종류
- `route_modes`: 이 space 안에서 나뉘는 대표 route
- `activation_signals`: 어떤 신호가 특정 route를 활성화하는지

### 7. boundary and residue

- `boundary_rules`
- `residue_policy`

정의:

- `boundary_rules`: 어디까지가 이 공간의 일인지
- `residue_policy`: 무엇을 residue로 남기고 무엇은 흘려보내는지

### 8. upper links

- `upper_family_links`
- `related_spaces`

이 필드는 아직 약해도 된다.
하지만 나중에 upper family layer를 붙일 때 연결 자리가 필요하다.

## JSON-shaped example

```json
{
  "space_id": "input_ingest_space",
  "space_name": "Input Ingest Space",
  "space_status": "active",
  "space_purpose": "make input ingest visible and traceable before deeper reading",
  "bounded_question": "How does raw input enter the space in a readable and minimally traced way?",
  "scope_objects": [
    "raw input documents",
    "split units",
    "processing trace"
  ],
  "excluded_scope": [
    "deep linkage inference",
    "promotion governance"
  ],
  "state_surface": [
    "source_manifest_*",
    "split_units_*",
    "readable_input_board_*"
  ],
  "action_surface": [
    "direct ingest",
    "registry ingest",
    "readable-board review"
  ],
  "evidence_paths": [
    "app/work/observer_ingest_min",
    "runtime/manifests/origin_maps"
  ],
  "root_entry_conditions": [
    "new raw input arrives",
    "structured doc routing target is created"
  ],
  "root_entry_examples": [
    "direct mode input",
    "registry mode ingest"
  ],
  "family_domains": [
    "input routing family",
    "source registration family"
  ],
  "route_modes": [
    "direct ingest",
    "split-first review"
  ],
  "activation_signals": [
    "input_kind detected",
    "split_mode resolved"
  ],
  "boundary_rules": [
    "easy ingest only",
    "deep linkage excluded"
  ],
  "residue_policy": [
    "keep source manifest and readable board",
    "do not escalate ingest-only traces as higher-order interpretation"
  ],
  "upper_family_links": [],
  "related_spaces": [
    "external_input_preprocess_space"
  ]
}
```

## 해석 규칙

### rule 1. 폴더와 space를 동일시하지 않는다

하나의 folder belt가 하나의 bounded space 후보일 수는 있지만,
항상 같은 것은 아니다.

### rule 2. state_surface와 action_surface를 둘 다 적는다

상태만 읽히고 action이 없으면 보고 belt에 가깝고,
action만 있고 상태가 없으면 도구 belt에 가깝다.

bounded functional space는 이 둘을 함께 가져야 한다.

### rule 3. excluded_scope를 반드시 적는다

경계는 포함보다 제외에서 더 잘 드러난다.

### rule 4. residue_policy가 있어야 숙성 공간이 된다

residue를 어떻게 남기는지 적지 못하면
그건 아직 숙성 공간보다 실행 도구에 가깝다.

## v0에서 기대하는 수준

v0는 완전한 family/route graph를 요구하지 않는다.

대신 아래만 되면 충분하다.

- 이 공간이 무엇을 위해 존재하는지 말할 수 있다
- 어떤 issue-root가 이 공간을 연다고 말할 수 있다
- 어떤 route들이 대표적인지 말할 수 있다
- 무엇을 residue로 남기는지 말할 수 있다

## 다음 단계 연결

이 스키마 다음에는 아래 둘이 자연스럽다.

1. 강한 후보 4개를 이 스키마로 실제 채우기
2. 그 이후 `upper_family_layer` 가 이 space들 사이를 어떻게 묶는지 정의하기
