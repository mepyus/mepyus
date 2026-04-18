# narrow_mechanism_closure_detector_and_widening_trigger_validation_pass_v1

## 1. validation matrix

이번 validation pass의 목적은
`narrow_mechanism_closure_detector + widening_trigger`
candidate contract가 기존 사례들에서

- false positive를 줄이고
- false negative를 줄이며
- broad default rule처럼 오작동하지 않는지

검증하는 것이다.

우선 contract 기준표를 고정한다.

### contract 기준표

#### detector 발동 조건

- `binding_closed = yes`
- `semantic_fidelity = acceptable but narrow mechanism closure`
- `output_worthiness = yes`
- `meaning_context_sufficiency = minimum sufficient`
- current unit이 row semantics 전체보다 concrete mechanism bucket 하나를 주로 설명함

#### detector 비발동 조건

- `semantic_fidelity = row-meaning-faithful closure`
- `meaning_context_sufficiency = strong`
- `output_worthiness = weak/no`
- retrieval failure 또는 unit quality failure가 더 앞단 병목

#### widening trigger 조건

- detector가 이미 켜져 있음
- next sentence가 같은 semantic field / explanatory arc를 이어 줌
- current mechanism을 일반화하거나 row 의미를 직접 보강함

#### widening 금지 / 보류 조건

- next sentence가 noise
- next sentence가 timestamp / format artifact
- next sentence가 unrelated implementation detail
- current unit이 line fragment 수준으로 너무 얇아 widening 전에 retrieval / unit quality 보강이 먼저임
- `binding_closed = no`

### 사례별 matrix

| 사례 | binding_closed | semantic_fidelity | output_worthiness | meaning_context_sufficiency | current unit 성격 | detector should fire? | detector did fit? | widening should fire? | widening did fit? |
|---|---|---|---|---|---|---|---|---|---|
| grounding_status / vlm | yes | row-meaning-faithful | yes | strong | faithful explanatory unit | no | no | no | no |
| grounding_status / cnn | yes | acceptable but narrow | yes | minimum sufficient | narrow mechanism | yes | yes | yes | yes |
| grounding_status / transformer1 | yes | acceptable but narrow | yes | minimum sufficient | narrow mechanism | yes | yes | yes | yes |
| traceability_status / vlm | yes | 비교적 직접적 | yes | minimum sufficient~strong | direct enough readback unit | no | mostly no | no | no |
| traceability_status / cnn | yes | narrow / slightly shaky | yes but barely | minimum sufficient | shaky unit + unrelated next detail | no | mostly no | no | no |
| emergence_status / vlm | yes | 직접적 | yes | strong | faithful/strong unit | no | no | no | no |
| emergence_status / cnn | yes | narrow | weak yes | minimum sufficient 이하 | line-like thin unit | no | no | no | no |

### matrix 해석

- `grounding_status / cnn`, `grounding_status / transformer1`
  - detector가 켜져야 하고 실제로도 맞게 켜진다
  - widening trigger도 실제로 유효했다

- `grounding_status / vlm`
  - detector가 켜지면 false positive인데, 현재 조건으론 비발동이 맞다

- `traceability_status / cnn`
  - 가장 중요한 validation 사례다
  - current unit이 다소 좁고 shaky해 보이지만
  - semantic fidelity가 `acceptable but narrow mechanism closure`까지는 아니다
  - next sentence도 unrelated detail이므로 widening trigger가 꺼져야 한다
  - 현재 contract는 이 사례에서 broad widening rule로 오작동하지 않는다

- `emergence_status / cnn`
  - 현재 unit이 너무 얇아 detector보다 unit quality watchpoint가 먼저다
  - widening trigger는 당연히 꺼져야 한다

## 2. false positive / false negative / ambiguity 요약

### false positive 사례

명확한 false positive는 현재 없다.

특히 아래 두 사례에서 과발동이 막힌 것이 중요하다.

- `grounding_status / vlm`
  - strong/faithful closure라 detector 비발동이 맞다
- `traceability_status / cnn`
  - 좁아 보여도 next sentence가 row 의미를 보강하지 않으므로 widening 비발동이 맞다

### false negative 사례

명확한 false negative도 현재 없다.

- `grounding_status / cnn`
- `grounding_status / transformer1`

둘 다 detector와 widening trigger가 모두 켜져야 하는 사례인데,
현재 contract는 이를 포착한다.

### widening 과발동 사례

현재 contract 기준으로 명시적 과발동은 없다.

다만 watchpoint는 있다.

- `traceability_status / cnn`
- `emergence_status / cnn`

이 둘은 current unit이 다소 좁거나 얇아 보여서
detector 문구를 너무 넓게 해석하면 과발동 여지가 있다.

### widening 누락 사례

현재 사례군 안에서는 명시적 누락은 없다.

### ambiguity 사례

가장 애매한 사례는 `traceability_status / vlm`이다.

- current unit은 충분히 direct하다
- 하지만 `current + next`를 붙이면 recommendation/readout 감각이 조금 더 좋아진다

즉 이 사례는:
- detector 발동 사례는 아니지만
- widening이 “조금 도움”은 되는 사례다

따라서 contract는 이걸 “widening 불필요” 쪽으로 두고 있지만,
경계선 사례라는 점은 문서에서 더 분명히 적어야 한다.

## 3. contract 문구 보정 필요 항목

이번 validation pass에서 가장 중요한 문구 보정 포인트는 아래 4개다.

### 3-1. `current unit이 concrete mechanism bucket 하나를 주로 설명함`

현 상태:
- 핵심 조건이지만 조금 추상적이다

보정 필요:
- 아래처럼 operational note가 붙는 편이 낫다
  - `row label보다 더 좁은 task/method/output mechanism 하나로 의미가 수렴함`
  - 예:
    - `label classification`
    - `class token classification`

### 3-2. `meaning_context_sufficiency = minimum sufficient`

현 상태:
- detector 조건으로는 유효했다
- 하지만 이것만으로는 부족하다

보정 필요:
- `minimum sufficient`이면서 동시에
  - `row semantics 전체는 아직 충분히 안 담김`
  이라는 설명이 같이 붙어야 한다

### 3-3. `same semantic field / explanatory arc`

현 상태:
- widening trigger 핵심인데 조금 넓다

보정 필요:
- 다음 문장이
  - current mechanism을 일반화하거나
  - 같은 task/output path를 이어 주거나
  - row 의미를 직접 보강하는 경우
  로 더 구체화하는 편이 좋다

### 3-4. output-worthiness와 meaning-context sufficiency의 관계

현 상태:
- 둘을 분리한 점은 맞다

보정 필요:
- 아래를 더 분명히 적는 편이 좋다
  - `output-worthy != semantically sufficient`
  - 읽을 수 있는 문장이라고 해서 row 의미를 충분히 담는 것은 아님

## 4. validation verdict

판정:

- `경미 수정 후 candidate contract v1.1 필요`

이유:

1. 현재 contract는 사례들에 대해 전반적으로 잘 맞는다
2. false positive / false negative도 현재 사례군에서는 크지 않다
3. 하지만 몇 개 문구가 아직 추상적이라,
   다음 감독 기준으로 바로 쓰기엔 해석 오차 여지가 있다

즉:

- draft 자체는 유효하다
- 다만 wording/operational note를 조금 더 분명히 한 `v1.1`이 적절하다

## 5. 다음 supervisor 지시를 위한 메모

### 지금 이 candidate contract를 다음부터 감독 기준으로 써도 되는가?

- `부분적으로 yes`
- 다만 현재 버전 그대로보다는 `v1.1 wording refinement`를 거친 뒤 쓰는 편이 안전하다

### 추가 cross-check가 더 필요한가?

- `소규모 yes`
- contract 핵심은 맞지만, 경계선 사례 1개 정도를 더 보면 더 안정적이다

### 구현 전에 문서 수준에서 더 잠글 것 하나가 있는가?

- `yes`
- 다음 턴은 구현이 아니라 아래 둘 중 하나가 맞다

1. `candidate contract v1.1 wording refinement`
2. 또는 더 보수적으로 `validation sample 1개 추가`

현재 추천:

- 먼저 `v1.1 wording refinement`
- 그 다음 필요하면 sample 1개 추가

즉 이번 verdict는:

- full contract로 올리기엔 아직 이르고
- detector/widening 구조는 유효하므로
- `candidate contract v1.1`로 얇게 다듬은 뒤 감독 기준으로 쓰는 것이 맞다
