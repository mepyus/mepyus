# grounding_status_meaning_unit_widening_check_v1

## 1. 자산별 current closure 기준 단위

이번 턴에서 focus가 closure에서 meaning-unit quality로 이동한 이유는 분명하다.

- `vlm / cnn / transformer1` 모두 이제 `grounding_status`에서 `first_pass_canonical` closure를 갖는다.
- 하지만 comparative guard 결과, `cnn`과 `transformer1`은 row semantics 전체보다 narrower mechanism bucket으로 닫히는 경향이 확인되었다.
- 따라서 지금 질문은 “더 닫히게 할 것인가”가 아니라, “현재 paragraph 단위가 row 의미를 너무 좁게 만들고 있는가”였다.

현재 기준 단위는 아래와 같다.

### `choi_ai_classroom_vlm`

- current paragraph:
  - `lines 415-416 @ 22:10`
  - `네거티브하고 파지티브로 이렇게 막 비교하는 이런 대조 학습이 어 레이블 없이 이제 하게 됩니다. 아까는`
- current primary_rule_key:
  - `semantic.contrastive_learning`
- current semantic fidelity:
  - `row-meaning-faithful`에 가장 가까움
- current output-worthiness:
  - `yes`
- current meaning-context sufficiency:
  - `strong`

### `choi_ai_classroom_cnn`

- current paragraph:
  - `lines 69-70 @ 3:49`
  - `어, 결국은 다 똑같이 어, 폭포죠. 그렇죠? 똑같이 레이블은 폭포라고 할 수 있고 분류도 폭포로 해야 되죠.`
- current primary_rule_key:
  - `semantic.label_classification`
- current semantic fidelity:
  - `acceptable but narrow mechanism closure`
- current output-worthiness:
  - `yes`
- current meaning-context sufficiency:
  - `minimum sufficient`

### `choi_ai_classroom_transformer1`

- current paragraph:
  - `lines 691-692 @ 36:33`
  - `보통 이제 비전 트랜스포머에 보면은 예요 클래스 토큰으로부터 나온 걸 가지고 이미지 분류를 보통 하죠.네`
- current primary_rule_key:
  - `semantic.class_token_classification`
- current semantic fidelity:
  - `acceptable but narrow mechanism closure`
- current output-worthiness:
  - `yes`
- current meaning-context sufficiency:
  - `minimum sufficient`

## 2. 자산별 widening 후보

이번 턴에서는 무작정 길게 늘리지 않고, 현재 mechanism-only closure를 완화할 가능성이 가장 높은 최소 widening만 봤다.

### `vlm`

선택 후보:
- `current + next`

후보 이유:
- current paragraph만으로도 contrastive learning mechanism이 충분히 읽힌다.
- next 문장에는 `파지티브 레이블`과 `레이블링`이 붙어 있어 current 의미를 조금 더 풀어 준다.

### `cnn`

선택 후보:
- `current + next`

후보 이유:
- current paragraph는 `폭포 / 레이블 / 분류` 예시에 많이 기대고 있어 좁다.
- next 문장에는 `시프트 / 로테이션 / 스케일에 대해서도 균일하게 성능`이 붙어 있어,
  왜 같은 label grounding이 유지되는지의 맥락을 더 준다.

### `transformer1`

선택 후보:
- `current + next`

후보 이유:
- current paragraph는 `클래스 토큰 -> 이미지 분류`라는 한 메커니즘만 말한다.
- next 문장에는 `클래시파이어를 여기다 다는 경우`가 붙어 있어,
  output head / classification path 문맥이 조금 더 드러난다.

## 3. widening 전/후 semantic fidelity 비교

### `vlm`

current only:
- `네거티브 / 파지티브 / 레이블 없이`가 직접 나와서 `grounding_status`의 기준 형성 방식이 바로 읽힌다.

current + next:
- `파지티브 레이블`과 `레이블링`이 붙으면서 contrastive setup의 주변 설명은 더 늘어난다.
- 하지만 current paragraph가 이미 충분히 직접적이라 fidelity 개선 폭은 크지 않다.

판정:
- widening이 의미를 해치진 않지만, 현재보다 크게 좋아지지도 않는다.

### `cnn`

current only:
- `레이블은 폭포`, `분류도 폭포`
- label/classification grounding은 읽히지만, 왜 그런 grounding이 유지되는지는 잘 안 보인다.

current + next:
- `시프트 / 로테이션 / 스케일에 대해서도 균일하게 성능`
- 같은 label이 유지되는 이유가 geometric invariance 문맥으로 이어진다.
- 즉 current paragraph의 예시성(`폭포`)이 next 문장과 붙으면서,
  단순 label assignment에서 “변형에도 grounding이 유지되는 상태” 쪽으로 read unit이 넓어진다.

판정:
- widening이 실제로 semantic fidelity를 높인다.
- `grounding_status`가 단순 분류 bucket이 아니라 “변형 속에서도 유지되는 grounding”으로 조금 더 직접적으로 읽힌다.

### `transformer1`

current only:
- `클래스 토큰으로부터 나온 걸 가지고 이미지 분류`
- classification output mechanism은 읽히지만, 한 문장만 보면 조금 abrupt하다.

current + next:
- `클래시파이어를 여기다 다는 경우들이 더 많습니다`
- class token paragraph가 output head / classifier 문맥으로 이어져,
  단일 메커니즘 설명에서 “어떤 경로로 최종 분류로 나가는가”의 최소 맥락이 더 붙는다.

판정:
- widening이 semantic fidelity를 아주 크게 높이진 않지만, mechanism-only closure의 abruptness는 줄인다.
- directness는 유지하면서 context sufficiency가 조금 좋아진다.

## 4. output-worthiness / meaning-context sufficiency 비교

### `vlm`

- widening 전:
  - output-worthiness `yes`
  - meaning-context sufficiency `strong`
- widening 후:
  - output-worthiness `yes`
  - meaning-context sufficiency `strong+`
- 변화:
  - context는 조금 더 풍부해지지만, 실제 필요성은 낮다

### `cnn`

- widening 전:
  - output-worthiness `yes`
  - meaning-context sufficiency `minimum sufficient`
- widening 후:
  - output-worthiness `yes`
  - meaning-context sufficiency `improved`
- 변화:
  - paragraph가 예시 중심에서 invariance context를 가진 local unit으로 바뀐다
  - drift risk가 조금 줄어든다

### `transformer1`

- widening 전:
  - output-worthiness `yes`
  - meaning-context sufficiency `minimum sufficient`
- widening 후:
  - output-worthiness `yes`
  - meaning-context sufficiency `improved but still narrow`
- 변화:
  - 한 문장만의 abruptness는 줄어든다
  - 하지만 row semantics 전체를 충분히 넓게 담는 수준까지는 아니다

## 5. 자산별 widening 분류

### `choi_ai_classroom_vlm`

- 분류:
  - `widening 불필요`
- 이유:
  - 현재 paragraph만으로도 row 의미 직접성이 충분하다
  - widening은 context를 늘리지만 핵심 fidelity를 크게 높이지 않는다

### `choi_ai_classroom_cnn`

- 분류:
  - `widening 유효`
- 이유:
  - current paragraph의 좁은 label/classification closure가
    next 문장과 붙으면 transform/invariance grounding 문맥까지 읽히게 된다
  - semantic drift를 줄이는 데 실제 도움이 된다

### `choi_ai_classroom_transformer1`

- 분류:
  - `widening 유효`
- 이유:
  - current paragraph는 mechanism-only closure가 너무 abrupt한 편이다
  - next 문장과 붙으면 classifier/head 문맥이 따라와 output-worthy read unit으로 조금 더 안정된다
  - 다만 개선 폭은 `cnn`보다 작다

## 6. 종합 판정

### meaning-unit widening을 다음 일반 조건 후보로 올려야 하는가?

- `yes`

이유:

- `vlm`처럼 현재 paragraph가 충분히 강한 경우는 widening이 거의 필요 없다.
- 하지만 `cnn`, `transformer1`처럼 narrower mechanism closure로 닫히는 자산은
  최소 widening(`current + next`)만으로도 semantic fidelity와 meaning-context sufficiency가 실제로 좋아진다.

### semantic fidelity guard만으로 충분한가?

- `no`

guard만으로는 “이 closure가 좁다”는 판정은 가능하지만,
`어떻게 더 나은 read unit으로 볼 것인가`까지는 못 간다.
이번 턴 결과는 widening이 실제 개선 효과를 낼 수 있다는 쪽을 지지한다.

### widening이 필요한 자산 유형 / 필요 없는 자산 유형

필요 없는 유형:
- current paragraph 자체가 row 의미를 직접적으로 담는 자산
- 예: `vlm`

필요한 유형:
- paragraph가 mechanism-only closure를 만들지만 surrounding context가 row 의미를 보강하는 자산
- 예: `cnn`, `transformer1`

## 7. 다음 supervisor 지시를 위한 메모

이번 턴이 다음을 좁히는 이유:

- closure 비교만으로는 `cnn`, `transformer1`의 좁은 mechanism closure를 완전히 방어할 수 없다
- 최소 widening이 실제 semantic fidelity 개선 효과를 내는 자산이 확인됐다

권장 다음 지시:

1. `grounding_status wider-read unit rule candidate check`
- `current + next` 같은 local widening을 일반 조건 후보로 잠글 수 있는지

2. 또는 더 직접적으로:
- `meaning-unit widening contract draft for grounding_status-family rows`

다만 아직 바로 계약으로 잠그기보다는,
다른 row family(`traceability_status` 등)에도 같은 widening 효과가 나는지 한 번 더 cross-check 한 뒤 잠그는 것이 안전하다.
