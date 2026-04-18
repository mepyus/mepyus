# transition over surface evaluation asset requirement note v0

## verdict

- `transition_over_surface` evaluation asset requirement is locked as a spec asset
- this turn does not change runtime code, heuristic scope, or evaluation fixtures
- this axis is parked until evidence-bearing evaluation assets exist

## why current fixture is insufficient

- current fixture 안에는 `transition_over_surface` direct textual evidence가 사실상 거의 없다
- 일부 fixture에는 weak cue가 남지만, weak cue만으로는 line 평가 기준을 세우기 어렵다
- 따라서 현재 `absent`는 heuristic failure일 수도 있으나, fixture wording 부족의 자연스러운 결과일 가능성이 더 크다
- future supervisor는 이 note만 보고도 "이 asset이 reopening 기준을 충족하는가"를 판정할 수 있어야 한다

## technical summary

### direct textual evidence definition

아래 조건이 함께 보이면 `transition_over_surface` direct textual evidence 후보로 본다.

- `surface` 축이 직접 드러난다
- `transition`과 `surface`의 관계가 함께 드러난다
- "표면 위에서 전환이 일어남" 또는 그에 준하는 직접 관계 표현이 있다
- 영어/한국어 표현 모두 가능하되, 단순 분위기나 흐름이 아니라 relation-bearing wording이어야 한다

direct textual evidence 후보 예시:

- `표면 전환`
- `표면 위 전환`
- `표면 넘어 전환`
- `transition over surface`
- `surface transition`
- `surface-level transition`
- `표면을 넘어 ... 로 전환`
- `... surface 를 거쳐 transition 된다`

이 표현들이 direct evidence인 이유:

- `surface`와 `transition`이 같은 구절 또는 인접 구절에서 직접 연결된다
- 흐름 변화의 느낌이 아니라, 관계 자체를 문장으로 드러낸다

### weak cue vs credible evidence boundary

아래는 여전히 weak cue 수준으로 둔다.

- 단순 전환감
- contrast / causal 흐름만 있는 표현
- stage handoff 느낌만 있는 표현
- `surface` 축이 없는 `전환` 류
- `surface` 단어는 있으나 transition 관계가 없는 표현

weak cue 예시:

- `이후에는 다른 단계로 넘긴다`
- `하지만 ... 다른 결과가 나온다`
- `따라서 ... 다시 열린다`
- `그러나 ... 과잉 읽기가 생긴다`

credible evidence로 넘어가려면 아래가 필요하다.

- `surface`와 `transition`의 관계가 문장 안에서 직접 말해진다
- 단순 discourse move가 아니라 line relation을 지지한다
- weak cue만으로 strong/weak를 부여하지 않아도 되는 설명 가능성이 있다

이 경계는 weak-cue overinterpretation 방지용이다. 흐름 변화만 보인다고 `transition_over_surface`를 다시 열면 안 된다.

### positive asset requirements

평가 자산은 최소 아래를 만족해야 한다.

- direct evidence가 실제 텍스트 안에 있어야 한다
- weak cue가 아니라 relation-bearing wording이 있어야 한다
- `transition`과 `surface`가 같은 구절 또는 인접 구절 안에서 연결되어야 한다
- positive candidate와 negative control을 함께 포함해야 한다
- 한두 문장 예시가 아니라 비교 가능한 묶음이어야 한다

권장 asset structure:

- positive slice
  - `surface`와 `transition` 관계를 직접 말하는 문장 묶음
- negative control
  - `transition`만 있거나 `surface`만 있는 문장 묶음
- weak cue slice
  - stage handoff, contrast, causal만 있는 문장 묶음

이렇게 해야 `absent / weak / strong` 경계가 과잉 추측 없이 비교 가능해진다.

### example evidence patterns

- direct evidence pattern
  - `표면 전환이 일어난다`
  - `표면 위에서 다른 층으로 전환된다`
  - `surface transition begins here`
  - `the system moves over the surface into a new transition layer`

- weak cue pattern
  - `이후에는 다른 단계로 넘긴다`
  - `하지만 다른 결과가 나온다`
  - `따라서 흐름이 바뀐다`

- negative control pattern
  - `표면이 거칠다`
  - `전환이 필요하다`
  - `surface quality changed`
  - `transition was discussed`

### negative examples / insufficient asset patterns

아래는 evaluation asset의 direct evidence로 쓰면 안 된다.

- 단독 `표면`
- 단독 `transition` / `전환`
- contrast만 있는 문장
- causal만 있는 문장
- 설명형 handoff만 있는 문장
- `surface` 단어가 있지만 relation이 없는 경우
- weak cue만 여러 개 쌓아 direct evidence처럼 포장한 경우

이 패턴들은 evaluation asset scarcity를 해결하지 못한다. quantity가 늘어도 direct relation wording이 없으면 reopening 근거가 되지 않는다.

### reopen gate conditions

아래가 충족되면 다시 patch/evaluation loop를 열 수 있다.

- direct evidence 포함 evaluation asset 확보
- positive candidate / negative control 함께 확보
- current fixture와 별도로 `transition_over_surface` 전용 관찰 가능
- weak cue와 direct evidence를 비교할 수 있는 구조 확보

reopen decision rule:

- 위 조건이 충족되기 전에는 runtime patch를 다시 열지 않는다
- weak cue만 있는 asset은 reopening 승인 근거가 아니다
- supervisor는 새 asset이 direct evidence와 negative control을 모두 갖췄는지 먼저 판정한다

## non-goals

- no runtime patch
- no heuristic expansion
- no candidate/thin promotion
- no scoring formula
- no new fixture in this turn
- no keyword map change
- no aggregation or variation map work
- no input_to_reading_organ re-tuning

## user-language summary

### direct evidence vs weak cue

- `transition_over_surface`를 제대로 평가하려면 단순한 전환 느낌이 아니라 `surface`와 `transition` 관계를 직접 말하는 문장이 필요하다
- contrast, causal, stage handoff는 weak cue일 수는 있어도 direct evidence는 아니다

### why current fixture is insufficient

- 지금 fixture에는 그런 direct evidence가 거의 없다
- 그래서 지금은 기계를 더 손볼 차례보다, `transition_over_surface`를 시험할 수 있는 재료를 먼저 준비할 차례다

### close-out

- 이 축은 evidence-bearing evaluation asset이 준비될 때까지 parked 상태로 둔다
- weak cue만으로 reopening 하지 않는다
- supervisor는 새 asset이 direct evidence, negative control, 비교 가능한 묶음을 갖췄을 때만 다음 patch/evaluation을 열면 된다
