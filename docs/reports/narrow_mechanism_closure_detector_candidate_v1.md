# narrow_mechanism_closure_detector_candidate_v1

## 1. 사례 재분류표

이번 턴에서 widening 자체보다 detector를 먼저 본 이유는,
이전 검증으로 widening이 일부 자산/row에서는 실제 semantic fidelity를 높였지만
다른 family에서는 거의 실익이 없다는 점이 확인됐기 때문이다.

즉 지금 필요한 것은
- `widening을 언제 켜야 하는가`
를 broad rule로 정하는 게 아니라,
- 먼저 `current unit이 narrow mechanism closure 상태인가`
를 식별하는 얇은 detector다.

기존 사례를 아래처럼 다시 분류했다.

| 사례 | binding closed | semantic fidelity | output-worthiness | meaning-context sufficiency | widening 결과 | 재분류 |
|---|---|---|---|---|---|---|
| grounding_status / vlm | yes | row-meaning-faithful | yes | strong | 불필요 | `row-meaning-faithful closure` |
| grounding_status / cnn | yes | acceptable but narrow | yes | minimum sufficient | 유효 | `narrow mechanism closure` |
| grounding_status / transformer1 | yes | acceptable but narrow | yes | minimum sufficient | 유효 | `narrow mechanism closure` |
| traceability_status / vlm | yes | 비교적 직접적 | yes | minimum sufficient~strong | 불필요 | `widening 불필요` |
| traceability_status / cnn | yes | narrow / slightly shaky | yes but barely | minimum sufficient | 비효율 | `widening 비효율` |
| emergence_status / vlm | yes | 직접적 | yes | strong | 불필요 | `widening 불필요` |
| emergence_status / cnn | yes | narrow | weak yes | minimum sufficient 이하 | 비효율 | `widening 비효율` |

핵심 분류 기준은 이렇다.

- `row-meaning-faithful closure`
  - current unit이 row semantics를 직접 담는다
- `narrow mechanism closure`
  - current unit은 output-worthy지만 row 의미 전체보다 concrete mechanism 하나로 닫힌다
- `widening 비효율 또는 불필요`
  - 현재 unit이 이미 충분하거나
  - next sentence가 row 의미를 보강하지 못한다

## 2. detector 후보 조건

아래 후보 조건을 사례에 대입해 남겼다.

### 남길 조건

1. `binding closed = yes`
- detector는 closure 이후에만 본다
- 아직 closure 자체가 안 된 경우는 detector 단계가 아니라 retrieval / mapping 단계 문제다

2. `semantic fidelity = acceptable but narrow mechanism closure`
- row 의미 전체보다 concrete mechanism 하나로 닫힌 상태여야 한다
- 이 조건이 핵심이다

3. `output-worthiness = yes`
- current unit이 surface/read unit으로는 이미 성립해야 한다
- 문장이 너무 비어 있으면 detector보다 먼저 unit quality 문제다

4. `meaning-context sufficiency = minimum sufficient`
- strong면 detector 비발동
- below minimum이면 detector보다 unit quality failure 또는 retrieval failure를 의심해야 한다

5. `current unit이 concrete mechanism 하나만 말하고 row 의미 전체는 덜 담음`
- 예:
  - `semantic.label_classification`
  - `semantic.class_token_classification`
- 이건 semantic fidelity 판정의 operational form이다

### 보조 조건

6. `next sentence가 같은 semantic field / explanatory arc를 이어 줌`
- widening trigger로 연결할 때 쓰는 조건이다
- detector 단독 조건은 아니지만, detector 후 widening 연결 여부를 가른다

### 버린 조건

- `binding_source=first_pass_canonical`
  - useful하지만 필수 detector 조건은 아니다
  - closure source보다는 fidelity 상태가 더 직접적이다

- `scene/flow 특정 값`
  - 지금 사례만으로 특정 axis를 detector 조건으로 잠그기엔 증거가 부족하다

## 3. false positive / false negative 점검

### false positive

`vlm / grounding_status`

- 이 사례는 widening 불필요다
- detector가 켜지면 false positive
- 실제로는:
  - semantic fidelity가 already strong
  - meaning-context sufficiency도 strong
- 그래서 위 조건으로는 발동되지 않는다

`traceability_status / cnn`, `emergence_status / cnn`

- 이 둘도 detector가 과하게 켜지면 안 된다
- current unit이 다소 좁아 보이지만,
  next sentence가 same semantic field를 보강하지 않는다
- 따라서 detector가 켜지더라도 widening trigger는 꺼져야 한다
- 이 구분이 없으면 과발동이 된다

### false negative

`cnn / grounding_status`, `transformer1 / grounding_status`

- 둘 다 widening 유효 사례다
- detector가 안 켜지면 false negative
- 실제로는:
  - binding closed = yes
  - semantic fidelity = narrow mechanism closure
  - output-worthiness = yes
  - meaning-context sufficiency = minimum sufficient
- 따라서 detector 조건에 정확히 들어온다

### 과발동 방지 핵심

가장 중요한 분기점은 이것이다.

- detector 발동
  - narrow mechanism closure를 식별
- widening trigger 발동
  - next sentence가 같은 semantic field / explanatory arc를 보강할 때만

즉 detector와 widening trigger를 분리해야
`traceability_status / cnn`, `emergence_status / cnn` 같은 과발동을 막을 수 있다.

## 4. 최종 detector 초안

### detector 발동 조건

아래를 모두 만족할 때 `narrow_mechanism_closure = true`

1. `binding_closed = yes`
2. `semantic_fidelity = acceptable but narrow mechanism closure`
3. `output_worthiness = yes`
4. `meaning_context_sufficiency = minimum sufficient`
5. `current unit`이 row semantics 전체보다 concrete mechanism bucket 하나를 주로 설명함

### detector 비발동 조건

아래 중 하나면 `false`

1. `semantic_fidelity = row-meaning-faithful closure`
2. `meaning_context_sufficiency = strong`
3. `output_worthiness = weak/no`
4. current unit이 row semantics와 무관하거나 retrieval 단계가 더 문제임

### 보류 / watchpoint 조건

아래는 detector가 아니라 watchpoint로 남긴다.

1. `binding closed = no`
2. current unit이 line fragment 수준으로 너무 얇음
3. current unit은 narrow해 보이지만 next sentence가 노이즈/역효과

즉:
- detector는 “지금이 좁은 closure 상태인가”를 식별
- watchpoint는 “지금은 detector보다 앞단 병목인가”를 식별

## 5. widening trigger 연결 조건

detector가 켜진 뒤 widening은 아래 조건에서만 후보가 된다.

1. `next sentence`가 same semantic field를 이어 준다
2. current mechanism을 일반화한다
3. row 의미를 직접 보강한다
4. next sentence가 noise / timestamp / unrelated implementation detail이 아니다

정리하면:

- `narrow_mechanism_closure_detector`
  - 언제 좁은 closure인지 찾는다
- `widening_trigger`
  - 그 좁음을 local context widening으로 풀 수 있는지 본다

## 6. 현재 잠글 수 있는 수준 판정

현재 단계에서 잠글 수 있는 것은:

- `detector candidate` : `yes`
- `detector + widening trigger를 함께 candidate로 둘 수 있는가` : `yes`
- full contract로 잠글 수 있는가 : `not yet`

이유:

- 사례 수는 detector 후보를 만들기엔 충분하다
- 하지만 broader contract로 잠그기엔 아직 family coverage가 좁다
- 따라서 지금은
  - detector candidate
  - widening trigger candidate
를 함께 두는 수준이 적절하다

## 7. 다음 supervisor 지시를 위한 메모

이번 턴이 다음을 어떻게 좁히는가:

- widening을 무조건 켜는 게 아니라
  `narrow mechanism closure`를 먼저 잡아야 한다는 점이 분명해졌다
- detector와 widening trigger를 분리해야 과발동을 막을 수 있다는 점도 확인됐다

다음 supervisor 지시 후보:

1. `narrow mechanism closure detector + widening trigger candidate contract draft`
- 지금 정리한 발동/비발동/trigger 조건을 얇게 계약 초안으로 옮기기

2. 또는 더 보수적으로:
- 다른 row family 1개 정도만 더 봐서 detector false positive/negative를 한 번 더 검증

현재로서는 다음 턴이 contract draft로 가도 무리는 없지만,
그 draft는 broad rule이 아니라 `candidate contract` 수준으로만 잠그는 것이 맞다.
