# Root Family Invariant Schema v0

## 목적

이 문서는 `same-root` 판정을 위해
line family가 공통으로 가져야 하는 invariant 스키마를 고정한다.

핵심은 단순 유사 주제 판정이 아니다.

표면 process, UI, 파일 위치가 달라도
같은 root family인지 판정할 수 있어야 한다.

## 왜 필요한가

VectorFL은 낱개 line 저장소가 아니라
family를 생성·분기·활성화·회수하는 공간으로 가고 있다.

그러려면 아래가 필요하다.

- 무엇이 같은 root family인지
- projection 차이인지
- 새 family branching인지

를 안정적으로 가르는 기준

그 기준이 `root invariant` 다.

## 최소 필드

### 1. identity

- `family_id`
- `family_name`
- `family_status`

`family_status` 후보:

- `candidate`
- `emergent`
- `active`
- `stable`

### 2. same-root core

- `problem_field`
- `core_distinction`
- `transition_logic`
- `judgment_question`
- `completion_criterion`

이 다섯 개가 v0의 핵심 invariant다.

## 보조 필드

- `bounded_spaces`
- `scope_objects`
- `route_modes`
- `primary_line_types`
- `primary_facets`
- `residue_return_mode`

이 보조 필드는 family가 실제로 어디서 작동하는지와
어떤 형태로 두꺼워지는지를 보조 설명한다.

## 필드 설명

### problem_field

이 family가 반복적으로 다루는 문제장

### core_distinction

이 family가 재료 안에서 가장 먼저 긋는 차이

### transition_logic

이 family가 보는 핵심 전환 구조

### judgment_question

이 family가 반복적으로 답하려는 질문

### completion_criterion

이 family가 한 사이클에서 “충분하다”고 보는 종료/도달 기준

## 판단 규칙

### rule 1. same-root는 다섯 invariant를 먼저 본다

아래 다섯 개가 실질적으로 같다면
표면 절차 차이가 있어도 같은 root family로 본다.

- `problem_field`
- `core_distinction`
- `transition_logic`
- `judgment_question`
- `completion_criterion`

### rule 2. changed facet만 다르면 projection이다

같은 family에서

- reading projection
- decision projection
- residue projection

처럼 갈리는 것은
새 family보다 projection으로 우선 본다.

### rule 3. judgment_question이 바뀌면 branching 가능성이 높다

같은 문제장이라도
판단 질문이 달라졌다면 새 family 분기 가능성을 우선 본다.

## JSON-shaped example

```json
{
  "family_id": "fam_input_to_reading",
  "family_name": "Input To Reading",
  "family_status": "active",
  "problem_field": "raw input becoming readable operating material",
  "core_distinction": "raw input vs readable structured entry",
  "transition_logic": "ingest -> split/shape -> readable entry",
  "judgment_question": "How should this input be turned into a readable entry path?",
  "completion_criterion": "input becomes traceable, readable, and safe to hand off",
  "bounded_spaces": [
    "input_ingest_space",
    "external_input_preprocess_space"
  ],
  "scope_objects": [
    "raw input documents",
    "split units",
    "preprocess outputs"
  ],
  "route_modes": [
    "direct ingest",
    "compare-first preprocess"
  ],
  "primary_line_types": [
    "reading_line",
    "structural_line"
  ],
  "primary_facets": [
    "material_facet",
    "distinction_facet",
    "linkage_facet",
    "direction_facet"
  ],
  "residue_return_mode": "preprocess and ingest residue return to future entry shaping"
}
```

## v0 기대 수준

v0는 수학적 판정기가 아니다.

하지만 아래는 가능해야 한다.

- family의 본질 질문을 한 문장으로 말할 수 있다
- 다른 projection을 같은 root 아래 묶을 수 있다
- 새 line이 기존 family thickening인지 branching인지 토론할 수 있다

## 다음 단계 연결

이 스키마 다음에는
실제 family instance를 채우고,
route signature와 붙여 읽는 것이 자연스럽다.
