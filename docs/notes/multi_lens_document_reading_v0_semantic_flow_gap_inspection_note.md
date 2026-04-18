# multi_lens_document_reading_v0 semantic-flow gap inspection note

## verdict

현재 stable lens 두 개는 meaning-pattern patch 이후 `caution`까지는 가지만 `strong`까지는 못 간다.

- `line_input_to_reading_organ`
  - partial input/processing flow는 잡힌다
  - 하지만 fixture 안에 `input -> processing -> result` 전 흐름이 거의 없다
- `line_transition_over_surface`
  - low-confidence 조각은 `caution`으로 분리됐다
  - 하지만 fixture 안에 `boundary/layer/surface + transition` 구조가 거의 없다

이번 판정은 strong 기준을 넓힐 문제가 아니라, 현재 validation fixture가 strong semantic-flow를 얼마나 실제로 담고 있는지 확인하는 문제에 더 가깝다.

## line_input_to_reading_organ

### caution까지는 왜 갔는가

현재 fixture에서는 아래 두 경우가 `caution`까지는 충분했다.

- `low_linkage_confidence`
  - `dialogue_continuation:2-2`
  - `dialogue_continuation:3-3`
  - `explanatory_mechanism:3-3`
  - `argument_contrast:3-3`
  - `mixed_document:3-3`
- `contrast_pair_context`
  - `argument_contrast:1-2`
    - 예시: `문서 내부 variation이 눌린다. / 하지만 여러 line lens를 열면 다른 결과가 나온다.`
  - `mixed_document:2-3`
    - 예시: `따라서 같은 문서 안에서도 여러 결이 다시 열린다. / 그러나 모든 조각을 묶으면 과잉 읽기가 생긴다.`

즉 현재 `caution`은
- 처리/변화 힌트는 보이지만
- linkage confidence가 낮거나
- contrast 문맥에 묶여 있어
- `입력 -> 처리 -> 결과` 전체 흐름으로 밀기 어려운 경우에 도달한다.

### strong에 아직 부족한 것

현재 fixture에는 아래 요소가 같이 보이지 않는다.

- `입력 재료`가 분명히 들어오는 쪽
- 그 재료가 `처리/해석/변환`되는 쪽
- 처리 후 `결과/출력/읽힌 상태 변화`가 명시되는 쪽

예시:

- `dialogue_continuation:0-1`
  - `우리는 먼저 입력을 다시 읽어야 합니다. / 그렇지 않으면 얇은 조각만 남습니다.`
  - 입력과 읽기 쪽은 보인다
  - 하지만 처리 후 결과가 독립적인 output/result 흐름으로 명확하지 않다
- `explanatory_mechanism:0-1`
  - `이 장치는 먼저 입력의 배경을 정리한다. / 예를 들면 약한 조각을 앞뒤 문맥으로 다시 잇는다.`
  - 입력과 처리/정리 쪽은 보인다
  - 하지만 결과가 별도 output/result 구조로 닫히지 않는다

### material scarcity

- 현재 fixture 문장은 대체로 `입력 + 처리` 또는 `처리만` 보여준다
- `결과가 출력면으로 이어지는 문장`은 거의 없다
- 그래서 current fixture만으로는 strong evidence가 얇다

### bounded-spec limitation

- 현재 spec은 `input -> processing -> result`를 비교적 엄격하게 본다
- 결과/출력 쪽이 약하면 `weak` 또는 `caution`에 머문다
- 지금 fixture 문장 밀도에서는 이 기준이 보수적으로 작동할 수밖에 없다

## line_transition_over_surface

### caution까지는 왜 갔는가

현재 fixture에서 `caution`은 거의 전부 `low_linkage_confidence`에서만 나왔다.

- `dialogue_continuation:2-2`
- `dialogue_continuation:3-3`
- `explanatory_mechanism:3-3`
- `argument_contrast:3-3`

즉 `transition`처럼 읽을 수도 있는 얇은 변화 힌트는 있었지만,
- link confidence가 낮고
- 실제 `표면/경계/레이어` 전환으로 보기엔 근거가 부족해서
- `absent` 대신 `caution`으로만 남았다.

### strong에 아직 부족한 것

현재 fixture에는 아래 요소가 거의 없다.

- `경계/표면/레이어/interface` 명시
- `A에서 B로` 같은 전환 전후 양쪽 구조
- `handoff`, `boundary`, `surface`, `layer` 같은 전환 명시어

예시:

- `explanatory_mechanism:3-3`
  - `이후에는 다른 단계로 넘긴다.`
  - 전환 느낌은 있다
  - 하지만 어느 표면에서 어느 표면으로 가는지 전후 양쪽이 없다
- `argument_contrast:3-3`
  - `그 차이가 이후 reread의 출발점이 된다.`
  - 상태 변화나 후속 출발점은 보이지만
  - 표면/경계 전환이라고 보기엔 구조가 부족하다

### material scarcity

- 현재 fixture 텍스트는 대부분 `전환 행위`보다 `논증/설명/재독해 감각`에 치우쳐 있다
- `surface`, `boundary`, `layer`, `handoff` 같은 material이 거의 없다
- 그래서 strong은 물론 weak도 쉽게 만들기 어렵다

### bounded-spec limitation

- 현재 spec은 `transition + boundary/surface` 또는 `A -> B` 구조를 요구한다
- 현재 fixture의 일반적 변화 문장은 이 기준을 거의 충족하지 못한다
- 즉 현재 absent가 많은 것은 heuristic failure만이 아니라 spec이 요구하는 재료 부족과도 연결된다

## explicit fixture examples

### input_to_reading_organ

- weak example
  - `dialogue_continuation:0-1`
  - `우리는 먼저 입력을 다시 읽어야 합니다. / 그렇지 않으면 얇은 조각만 남습니다.`
  - 입력과 읽기/처리 힌트는 있음
  - 결과 흐름은 partial
- caution example
  - `argument_contrast:1-2`
  - `문서 내부 variation이 눌린다. / 하지만 여러 line lens를 열면 다른 결과가 나온다.`
  - 결과 쪽은 보이지만 contrast 문맥이라 흐름이 불안정

### transition_over_surface

- caution example
  - `explanatory_mechanism:3-3`
  - `이후에는 다른 단계로 넘긴다.`
  - 전환 감각은 있으나 low-confidence 단독 문장
- absent example
  - `mixed_document:3-4`
  - `그러나 모든 조각을 묶으면 과잉 읽기가 생긴다. / 그래서 보수적으로 남겨야 하는 조각도 있다.`
  - 변화나 운영 판단은 보이지만 표면/경계 전환은 없음

## recommendation

다음 한 단계는 `fixture/evaluation asset enrichment`가 맞다.

이유:

- 현재 strong을 못 만드는 가장 큰 원인은 fixture 재료 부족이다
- 특히
  - `line_input_to_reading_organ`은 `result/output` 쪽이 약하고
  - `line_transition_over_surface`는 `boundary/surface` 재료가 거의 없다
- 지금 strong 기준을 더 넓히면 bounded patch의 보수성이 먼저 무너질 가능성이 있다

즉 다음은 broad heuristic debate를 다시 여는 게 아니라,
현재 stable lens가 실제 strong semantic-flow를 담는 fixture를 더 넣을지 먼저 결정하는 쪽이 맞다.
