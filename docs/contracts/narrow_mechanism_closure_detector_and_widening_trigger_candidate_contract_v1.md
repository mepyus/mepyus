# narrow_mechanism_closure_detector_and_widening_trigger_candidate_contract_v1

## 1. 목적

이 문서는 `narrow mechanism closure detector + widening trigger`를
운영 규칙으로 바로 잠그기 위한 문서가 아니다.

현재 목적은:

- paragraph/segment 기반 closure가 이미 닫힌 상태에서
- 그 closure가 row semantics 전체를 충분히 담지 못하고
  concrete mechanism bucket 하나로 좁아지는 경우를 식별하고
- 그런 경우에만 local widening(`current + next`)을 조건부로 검토하는
  **candidate contract**를 정리하는 것이다.

즉 이 문서는:

- broad default widening rule이 아니라
- `detector`와 `widening trigger`를 분리한
- 후속 validation pass를 위한 얇은 계약 초안이다.

## 2. 적용 범위

현재 적용 범위는 제한적이다.

- row family:
  - `grounding_status`를 가장 강한 근거로 삼는다
- cross-family 과발동 방지 근거:
  - `traceability_status`
  - `emergence_status`

즉 이 문서는

- `항상 widen`
- `모든 family에 같은 방식 적용`

을 의미하지 않는다.

현재 범위는:

- active asset reread가 가능하고
- binding closed가 이미 되었으며
- output-worthy current unit이 있으나
- semantic fidelity가 다소 좁아 보이는 사례

에 한정된 candidate contract다.

## 3. 문제 정의

현재 확인된 문제는 다음과 같다.

1. binding은 닫힐 수 있다
2. 그러나 닫힌 값이 row semantics 전체를 직접 담지 않고
3. concrete mechanism bucket 하나로 좁게 닫히는 경우가 있다
4. 이런 경우 current paragraph는 output-worthy지만
   meaning-context sufficiency가 `minimum sufficient` 수준에 머문다
5. 일부 사례에서는 `current + next` widening이 semantic fidelity를 실제로 개선한다
6. 하지만 다른 family에서는 widening이 실익 없이 길어지거나 오히려 초점을 흐린다

따라서 필요한 것은:

- 먼저 `narrow mechanism closure` 상태를 식별하는 detector
- 그 다음에만 `widening`을 검토하는 trigger

이다.

## 4. Detector 정의

### 4-1. detector 발동 조건

아래를 모두 만족하면
`narrow_mechanism_closure = true`
로 본다.

1. `binding_closed = yes`
2. `semantic_fidelity = acceptable but narrow mechanism closure`
3. `output_worthiness = yes`
4. `meaning_context_sufficiency = minimum sufficient`
5. current unit이 row semantics 전체보다
   `concrete mechanism bucket` 하나를 주로 설명한다

### 4-2. detector 비발동 조건

아래 중 하나면 detector는 꺼져 있어야 한다.

1. `semantic_fidelity = row-meaning-faithful closure`
2. `meaning_context_sufficiency = strong`
3. `output_worthiness = weak/no`
4. retrieval failure가 더 앞단 병목이다
5. unit quality failure가 더 앞단 병목이다

### 4-3. detector 해석 원칙

이 detector는
“현재 unit이 나쁘다”를 뜻하지 않는다.

뜻하는 것은 오직 하나다.

- `현재 unit은 읽을 수는 있지만, row 의미 전체보다 좁은 mechanism closure를 만들 가능성이 있다`

## 5. Widening Trigger 정의

### 5-1. widening trigger 발동 조건

widening은 detector가 먼저 켜진 상태에서만 검토한다.

그 위에서 아래를 만족할 때만
`widening_trigger = on`
으로 본다.

1. detector가 이미 켜져 있다
2. `next sentence`가 같은 semantic field를 이어 준다
3. `next sentence`가 같은 explanatory arc를 이어 준다
4. `next sentence`가 current mechanism을 일반화하거나
   row 의미를 직접 보강한다

### 5-2. widening 비발동 / 금지 조건

아래 중 하나면 widening은 꺼져 있어야 한다.

1. `next sentence = noise`
2. `next sentence = timestamp / format artifact`
3. `next sentence = unrelated implementation detail`
4. current unit이 line fragment 수준으로 너무 얇아서
   widening 전에 retrieval/unit quality 보강이 더 먼저다
5. `binding_closed = no`

### 5-3. detector와 widening trigger를 분리하는 이유

두 조건을 분리하지 않으면 과발동이 생긴다.

예:
- `traceability_status / cnn`
- `emergence_status / cnn`

이 사례들은 current unit이 다소 좁아 보여도,
next sentence가 same semantic field를 보강하지 않는다.

따라서:
- detector는 논의 대상이 될 수 있어도
- widening trigger는 꺼져 있어야 한다

즉
- detector = 현재 unit이 좁은 closure인지 식별
- widening trigger = 그 좁음을 local widening으로 풀 수 있는지 식별

이다.

## 6. 비발동 / 금지 / 보류 조건

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

## 7. 사례 근거

### 7-1. detector 발동의 핵심 근거

#### `grounding_status / cnn`

- binding closed: yes
- semantic fidelity: acceptable but narrow
- output-worthiness: yes
- meaning-context sufficiency: minimum sufficient
- current unit:
  - `레이블은 폭포 / 분류도 폭포`
- 판단:
  - detector 발동 근거
  - current paragraph가 좁은 mechanism closure를 만든다

#### `grounding_status / transformer1`

- binding closed: yes
- semantic fidelity: acceptable but narrow
- output-worthiness: yes
- meaning-context sufficiency: minimum sufficient
- current unit:
  - `클래스 토큰 -> 이미지 분류`
- 판단:
  - detector 발동 근거
  - concrete mechanism closure가 row semantics 전체보다 좁다

### 7-2. detector 비발동의 핵심 근거

#### `grounding_status / vlm`

- binding closed: yes
- semantic fidelity: row-meaning-faithful
- output-worthiness: yes
- meaning-context sufficiency: strong
- 판단:
  - detector 비발동 근거

#### `traceability_status / vlm`

- current paragraph만으로도 traceability/readout 감각이 선다
- widening은 context를 조금 더 풍부하게 할 뿐 실질적 개선은 작다
- 판단:
  - detector 비발동 또는 low-priority case

#### `emergence_status / vlm`

- current paragraph가 이미 `클러스터링 / 리트리벌 / 랭킹`을 직접 말한다
- 판단:
  - detector 비발동 근거

### 7-3. widening 비발동 / 비효율의 핵심 근거

#### `traceability_status / cnn`

- current paragraph:
  - `가장 가까운 거겠죠 ... 맥스 풀링이`
- next sentence:
  - `2014년` 등 implementation/history detail 쪽으로 흐른다
- 판단:
  - detector/guard 대상이 되더라도 widening trigger는 꺼져야 함

#### `emergence_status / cnn`

- current paragraph는 얇고,
- next sentence는 사실상 timestamp/format noise에 가깝다
- 판단:
  - widening 금지 근거

### 7-4. widening 발동의 핵심 근거

#### `grounding_status / cnn`

- `current + next`가
  - label/classification example
  - transform/invariance context
  를 이어 준다
- 판단:
  - widening trigger 발동 근거

#### `grounding_status / transformer1`

- `current + next`가
  - class token
  - classifier/head
  explanatory arc를 이어 준다
- 판단:
  - widening trigger 발동 근거

## 8. Watchpoints

이 candidate contract를 쓸 때 반드시 같이 봐야 하는 watchpoint는 아래다.

1. `binding closed`와 `semantic fidelity okay`를 혼동하지 말 것
2. `output-worthiness`와 `meaning-context sufficiency`를 계속 별도 판정할 것
3. mechanism-only closure를 row-meaning-faithful closure로 오해하지 말 것
4. 분절 의미문장이 값을 가졌더라도,
   그것이 실제로 출력 가능한 최소 의미 단위인지 별도로 봐야 할 것
5. detector가 켜졌다고 widening이 자동 발동되는 것으로 오해하지 말 것

## 9. Non-goals

이 문서가 지금 하지 않는 것은 아래다.

- broad global widening rule 잠금
- 모든 row family에 대한 일반 계약
- threshold 조정
- taxonomy 확장
- UI/페이지 동작 변경
- retrieval/unit quality 실패를 widening으로 덮는 것

## 10. 다음 검증 필요 항목

이 문서는 candidate contract 수준이므로,
다음 검증이 필요하다.

1. detector false positive / false negative를 row family 1개 정도 더 확인
2. detector 발동 후 widening trigger가 실제 개선을 내는지 추가 사례 검증
3. line-like fragment와 minimum-sufficient paragraph를 더 엄격히 구분할 필요가 있는지 확인

## 11. Supervisor-ready Note

### 이 candidate contract를 바로 운영 규칙으로 써도 되는가?

- `no`

이유:
- 현재 근거는 충분히 강하지만 아직 family coverage가 좁다
- broad rule이 아니라 `candidate contract` 수준으로 유지해야 한다

### 추가 false positive / false negative 검증이 더 필요한가?

- `yes`

### 다음 턴은 구현이 아니라 contract validation pass로 가야 하는가?

- `yes`

추천:
- 다음 턴은 구현보다 `contract validation pass`
- 또는 row family 1개 추가 cross-check

즉 현재 상태는:

- full contract까지는 아님
- 하지만 detector + widening trigger를 분리한 candidate contract draft로는 충분히 잠글 수 있다
