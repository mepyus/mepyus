# transition over surface evaluation asset gate note v0

## verdict

- `transition_over_surface` evaluation gate is locked as a spec asset
- this turn does not change implementation code
- current bottleneck is fixed at the gate level before any further heuristic patch

## what current observation established

- current fixture 기준에서 `transition_over_surface`는 전부 `absent`로 남았다
- direct textual evidence는 사실상 없었다
- `explanatory_mechanism`과 `mixed_document`는 weak cue 수준만 남겼다
- `dialogue_continuation`과 `argument_contrast`는 no credible evidence 쪽으로 읽혔다
- 따라서 현재 absent는 실패일 수도 있지만, 자연스러운 결과일 수도 있다

## technical summary

### why this is now an evaluation-asset question

- 지금 병목은 단순 heuristic 부족이라고 바로 단정하기 어렵다
- current fixture 안에는 `transition_over_surface`를 직접 지지하는 wording이 거의 없다
- weak cue와 credible evidence는 다르다
- 이 상태에서 heuristic을 더 넓히면 under-reading을 고치는 대신 over-trigger 회귀를 부를 위험이 크다

## option A: separate evaluation asset needed

별도 evaluation asset이 필요하다고 보는 조건:

- current fixture 안에 direct textual evidence가 거의 없을 때
- weak cue만으로는 line 평가의 정답 기준을 세우기 어려울 때
- absent가 실패인지 자연스러운 결과인지 현재 자산만으로 분리되지 않을 때

필요한 asset의 성격:

- `surface` 축이 직접 드러나는 표현이 있어야 한다
- `transition`과 `surface`의 관계가 함께 보이는 표현이 있어야 한다
- weak cue가 아니라 direct textual evidence가 있어야 한다
- `transition_over_surface`를 line 이름 없이도 문장 구조로 지지할 수 있어야 한다

왜 current fixture와 다른 평가 자산이 필요한가:

- current fixture는 문서 내부 contrast, flow, stage shift는 일부 보여주지만
  `transition_over_surface` line의 조합형 evidence는 거의 제공하지 않는다
- 따라서 현재 fixture는 이 line을 평가하기 위한 시험지로는 재료가 부족하다

## option B: bounded weak-cue patch possible

weak cue만으로 patch를 열 수 있는 최대 범위:

- `explanatory_mechanism`의 단계 전환 문장
- `mixed_document`의 shift/contrast 흐름
- 이 두 fixture 안의 weak cue만 대상으로 한 매우 좁은 실험

왜 이것이 실험일 뿐인가:

- direct evidence가 아니라 간접 단서 해석에 기대기 때문이다
- heuristic이 line 의미를 앞당겨 가정할 위험이 있다

왜 patch 범위를 매우 좁게 둬야 하는가:

- weak cue를 기준으로 넓히면 단독 discourse move가 `transition_over_surface`로 과잉 읽힐 수 있다
- 현재 absent가 맞는 fixture까지 다시 흔들 수 있다

언제 다시 중단해야 하는가:

- direct evidence가 없는 fixture에서 weak cue가 `strong`이나 과도한 `weak`로 늘어날 때
- `dialogue_continuation`이나 `argument_contrast`에 false positive가 생길 때

## comparison of risks

- option A risk
  - 당장 patch 속도는 느리다
  - 그러나 평가 기준을 더 명확히 세울 수 있다

- option B risk
  - 빠르게 under-reading을 완화하려 시도할 수 있다
  - 그러나 weak cue를 direct evidence처럼 다루며 over-trigger가 재발할 위험이 크다

## chosen gate decision

- A 로 간다

이유:

- current fixture 안에는 `transition_over_surface` direct textual evidence가 사실상 없다
- 지금 absent는 heuristic 실패라기보다 평가 자산 부족의 자연스러운 결과일 가능성이 더 높다
- 이 상태에서 patch를 더 열면 weak cue를 과대해석해 over-trigger 회귀를 부를 위험이 크다

## non-goals

- no heuristic patch
- no keyword map change
- no new fixture in this turn
- no aggregation or variation map work
- no input_to_reading_organ re-tuning

## next gate

- 다음 게이트는 `transition_over_surface`용 별도 evaluation asset 필요 여부를 구체화하는 쪽으로 연다
- 그 asset은 아래 조건을 만족해야 한다
  - `surface` 축 직접 표현
  - `transition`과 `surface` 관계의 동시 표현
  - weak cue가 아닌 direct textual evidence

## user-language summary

### current observation

- 지금 fixture 안에는 `transition_over_surface`를 직접 읽게 해 주는 문장이 거의 없다
- 그래서 현재 absent는 실패일 수도 있지만, 오히려 자연스러운 결과일 가능성이 크다

### option A vs B

- A는 시험지를 새로 준비하자는 쪽이다
- B는 지금 있는 약한 힌트만으로 제한적 실험을 해 보자는 쪽이다

### chosen decision

- 지금은 A가 맞다
- 기계를 더 고치기 전에, `transition_over_surface`를 제대로 평가할 수 있는 재료를 먼저 준비해야 한다
