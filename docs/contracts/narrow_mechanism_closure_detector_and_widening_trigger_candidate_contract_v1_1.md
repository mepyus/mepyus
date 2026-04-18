# narrow_mechanism_closure_detector_and_widening_trigger_candidate_contract_v1_1

## 1. 목적

이 문서는 `narrow mechanism closure detector + widening trigger`를
운영 규칙으로 바로 잠그기 위한 문서가 아니다.

현재 목적은:

- paragraph/segment 기반 closure가 이미 닫힌 상태에서
- 그 closure가 row semantics 전체를 충분히 담지 못하고
- 특정 작동 방식, 예시, 출력 경로, 또는 메커니즘 하나로 설명이 좁아지는 경우를 식별하고
- 그런 경우에만 local widening(`current + next`)을 조건부로 검토하는
  **candidate contract**를 더 operational한 형태로 정리하는 것이다.

즉 이 문서는:

- broad default widening rule이 아니라
- `detector`와 `widening trigger`를 분리한
- 감독 기준 후보로 쓸 수 있는 `candidate contract v1.1`

이다.

## 2. 적용 범위

현재 적용 범위는 제한적이다.

- strongest evidence:
  - `grounding_status`
- cross-family overfire guard evidence:
  - `traceability_status`
  - `emergence_status`

이 문서는 아래를 의미하지 않는다.

- `항상 widen`
- `모든 row family에 같은 방식 적용`
- `global default read rule`

현재 범위는:

- active asset reread가 가능하고
- binding closed가 이미 되었으며
- current unit이 표시/읽기 단위로는 성립하지만
- row 의미 전체를 충분히 운반하는지는 아직 의심되는 사례

에 한정된다.

## 3. 문제 정의

현재 확인된 문제는 다음과 같다.

1. binding은 닫힐 수 있다
2. 그러나 닫힌 값이 row semantics 전체를 직접 담지 않고
3. 특정 task / method / output mechanism / example 하나로 의미가 수렴하는 경우가 있다
4. 이런 경우 current unit은 표시/읽기에는 쓸 수 있지만
   row 의미 전체를 싣는 단위로는 좁을 수 있다
5. 일부 사례에서는 `current + next` widening이 semantic fidelity를 실제로 높인다
6. 하지만 다른 사례에서는 widening이 실익 없이 길어지거나 unrelated detail을 덧붙인다

따라서 필요한 것은:

- 먼저 `narrow mechanism closure` 상태를 식별하는 detector
- 그 다음에만 `widening`을 검토하는 trigger

이다.

## 4. Core Definitions

### 4-1. output-worthiness

`output-worthiness`는 현재 문장이
surface/view/re-read unit으로 최소 성립하는지를 뜻한다.

다음 질문에 `yes`면 output-worthy로 본다.

- 이 문장을 단독으로 보여줘도 사용자가 “무엇에 대한 말인지” 최소한 읽을 수 있는가?
- 문장이 단순 token, timestamp, 형식 노이즈가 아니라 실제 읽기 단위인가?

중요:
- `output-worthy`는 `row 의미를 충분히 담는다`와 같은 뜻이 아니다.

### 4-2. meaning-context sufficiency

`meaning-context sufficiency`는 현재 문장이
row semantics 전체를 얼마나 충분히 운반하는지를 뜻한다.

판정 기준:

- `strong`
  - current unit alone으로 row 의미의 중심이 선다
- `minimum sufficient`
  - current unit alone으로 읽기는 가능하지만
    row 의미 전체를 싣기에는 아직 좁다
- `below minimum`
  - current unit alone으로는 row 의미를 사실상 못 싣는다

중요:
- `minimum sufficient`는 단순한 등급이 아니라
  **문장 단독 해석은 가능하지만 row 의미 전체를 충분히 싣지는 못하는 상태**
  를 뜻한다.

## 5. Detector 정의

### 5-1. detector 발동 조건

아래를 모두 만족하면
`narrow_mechanism_closure = true`
로 본다.

1. `binding_closed = yes`
2. `semantic_fidelity = acceptable but narrow mechanism closure`
3. `output_worthiness = yes`
4. `meaning_context_sufficiency = minimum sufficient`
5. current unit 설명이
   - row 전체 의미를 대표하기보다
   - 특정 작동 방식 / 예시 / 출력 메커니즘 / task 하나에 집중된다

### 5-2. operational check points

위 5번을 더 operational하게 풀면 아래 중 2개 이상이 보일 때
`narrow mechanism closure`로 본다.

- current unit이 특정 method/mechanism 하나를 주로 말한다
- current unit이 구체 예시 하나에 의미를 많이 의존한다
- current unit이 output head / classification path / retrieval path 같은 한 작동 경로에 수렴한다
- current unit alone으로는 row label보다 좁은 의미만 또렷하다

예:
- `semantic.label_classification`
- `semantic.class_token_classification`

### 5-3. detector 비발동 조건

아래 중 하나면 detector는 꺼져 있어야 한다.

1. `semantic_fidelity = row-meaning-faithful closure`
2. `meaning_context_sufficiency = strong`
3. `output_worthiness = weak/no`
4. retrieval failure가 더 앞단 병목이다
5. unit quality failure가 더 앞단 병목이다

### 5-4. detector 해석 원칙

이 detector는
“현재 unit이 나쁘다”를 뜻하지 않는다.

뜻하는 것은 오직 하나다.

- `현재 unit은 읽을 수는 있지만, row 의미 전체보다 좁은 작동 메커니즘 하나로 의미가 수렴할 가능성이 있다`

## 6. Widening Trigger 정의

### 6-1. widening trigger 발동 조건

widening은 detector가 먼저 켜진 상태에서만 검토한다.

그 위에서 아래를 만족할 때만
`widening_trigger = on`
으로 본다.

1. detector가 이미 켜져 있다
2. `next sentence`가 current sentence와 같은 task/output path를 이어 준다
3. `next sentence`가 current mechanism의 조건 / 일반화 방향 / 결과 경로를 설명한다
4. `next sentence`가 row 의미를 직접 보강한다

즉 `same semantic field / explanatory arc`는 아래처럼 좁게 읽는다.

- 같은 작동 원리의 연속 설명
- 같은 output path의 후속 설명
- 같은 row 의미를 직접 보강하는 local context

### 6-2. widening 비발동 / 금지 조건

아래 중 하나면 widening은 꺼져 있어야 한다.

1. `next sentence = noise`
2. `next sentence = timestamp / format artifact`
3. `next sentence = unrelated implementation detail`
4. current unit이 line fragment 수준으로 너무 얇아서
   widening 전에 retrieval/unit quality 보강이 더 먼저다
5. `binding_closed = no`

### 6-3. detector와 widening trigger를 분리하는 이유

두 조건을 분리하지 않으면 과발동이 생긴다.

예:
- `traceability_status / cnn`
- `emergence_status / cnn`

이 사례들은 current unit이 다소 좁아 보여도,
next sentence가 current unit의 semantic field를 보강하지 않는다.

따라서:
- detector는 논의 대상이 될 수 있어도
- widening trigger는 꺼져 있어야 한다

즉
- detector = 현재 unit이 좁은 closure인지 식별
- widening trigger = 그 좁음을 local widening으로 풀 수 있는지 식별

이다.

## 7. 비발동 / 금지 / 보류 조건

### 비발동

- current unit이 이미 row-meaning-faithful
- current unit alone이 strong context를 가짐

### 금지

- next sentence가 semantic field를 보강하지 않음
- next sentence가 noise / timestamp / unrelated detail

### 보류

- binding_closed = no
- retrieval mismatch가 더 직접적
- sentence/segment meaning unit 자체가 output-worthy하지 않음

즉 이 contract는
closure 이후의 fidelity 문제를 다루는 것이지,
retrieval이나 canonical mapping 이전 단계 병목을 덮는 용도가 아니다.

## 8. 사례 근거

### 8-1. detector 발동의 핵심 근거

#### `grounding_status / cnn`

- current unit:
  - `레이블은 폭포 / 분류도 폭포`
- 이유:
  - row 전체 의미보다 label/classification example 하나에 설명이 집중된다
- 판정:
  - detector 발동 근거

#### `grounding_status / transformer1`

- current unit:
  - `클래스 토큰 -> 이미지 분류`
- 이유:
  - row 전체 의미보다 class-token classification path 하나에 설명이 수렴한다
- 판정:
  - detector 발동 근거

### 8-2. detector 비발동의 핵심 근거

#### `grounding_status / vlm`

- `positive / negative / label-free comparison`이 current unit 안에서 직접 읽힌다
- strong + faithful closure
- 판정:
  - detector 비발동

#### `traceability_status / vlm`

- current unit alone으로도 traceability/readout 감각이 선다
- widening은 context를 조금 더 풍부하게 할 뿐 핵심 fidelity를 크게 바꾸지 않는다
- 판정:
  - detector 비발동 또는 low-priority

#### `emergence_status / vlm`

- current unit이 이미 `클러스터링 / 리트리벌 / 랭킹`을 직접 담는다
- 판정:
  - detector 비발동

### 8-3. widening 비발동 / 비효율의 핵심 근거

#### `traceability_status / cnn`

- next sentence:
  - `맥스 풀링`, `2014년`
- 이유:
  - current unit의 semantic field를 보강하지 않고 implementation/history detail로 흐른다
- 판정:
  - widening 금지

#### `emergence_status / cnn`

- next sentence:
  - timestamp/format noise에 가깝다
- 판정:
  - widening 금지

### 8-4. widening 발동의 핵심 근거

#### `grounding_status / cnn`

- `current + next`가
  - label/classification example
  - transform/invariance context
  를 이어 준다
- 판정:
  - widening trigger 발동

#### `grounding_status / transformer1`

- `current + next`가
  - class token
  - classifier/head
  output path를 이어 준다
- 판정:
  - widening trigger 발동

## 9. Watchpoints

이 candidate contract를 쓸 때 반드시 같이 봐야 하는 watchpoint는 아래다.

1. `binding closed`와 `semantic fidelity okay`를 혼동하지 말 것
2. `output-worthiness`와 `meaning-context sufficiency`를 계속 별도 판정할 것
3. mechanism-only closure를 row-meaning-faithful closure로 오해하지 말 것
4. 분절 의미문장이 값을 가졌더라도,
   그것이 실제로 출력 가능한 최소 의미 단위인지 별도로 볼 것
5. detector가 켜졌다고 widening이 자동 발동되는 것으로 오해하지 말 것

## 10. Non-goals

이 문서가 지금 하지 않는 것은 아래다.

- broad global widening rule 잠금
- 모든 row family에 대한 일반 계약
- threshold 조정
- taxonomy 확장
- UI/페이지 동작 변경
- retrieval/unit quality 실패를 widening으로 덮는 것

## 11. 다음 검증 필요 항목

이 문서는 candidate contract 수준이므로,
다음 검증이 필요하다.

1. detector false positive / false negative를 row family 1개 정도 더 확인
2. detector 발동 후 widening trigger가 실제 개선을 내는지 추가 사례 검증
3. line-like fragment와 minimum-sufficient paragraph를 더 엄격히 구분할 필요가 있는지 확인

## 12. Supervisor-ready Note

### v1.1은 이제 감독 기준 후보로 써도 되는가?

- `yes, as candidate only`

즉 broad 운영 규칙은 아니지만,
감독자가 이후 validation pass를 걸 때 참고 기준으로 쓰기엔 충분하다.

### validation sample 1개를 더 붙여야 하는가?

- `small yes`

### 다음 턴은 문서 채택인가, 추가 sample 검증인가?

- 추천:
  - `small validation sample 1개 추가`
  - 그 뒤 감독 기준 후보로 채택

즉 현재 상태는:

- full contract까지는 아님
- 하지만 detector + widening trigger를 분리한 candidate contract v1.1은
  감독 기준 후보로는 사용할 수 있다
