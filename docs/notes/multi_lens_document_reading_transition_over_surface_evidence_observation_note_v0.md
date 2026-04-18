# multi lens document reading transition over surface evidence observation note v0

## verdict

- `transition_over_surface` evidence reading is locked as an observation note
- this turn does not change implementation code
- current fixture set is now documented as evidence-bearing vs evidence-poor for this lens

## what the recent patch did and did not show

- recent patch는 `transition_over_surface`에 조합형 seed 경계를 넣었지만
  현재 fixture 기준 결과는 전부 `absent`였다
- 이 결과는 두 가지 가능성을 남긴다
  - partial-match rule이 여전히 부족하다
  - 현재 fixture wording 안에 `transition_over_surface` evidence 자체가 거의 없다

이 note의 목적은 이 둘을 구분하는 것이다.

## technical summary

### fixture-by-fixture reading

#### dialogue_continuation

- candidate phrase/span
  - direct textual evidence: 없음
  - weak indirect cue: 질문 후 다른 화자/다른 발화로 넘어가는 느낌은 있으나,
    `surface` 또는 `표면` 계열 표현이 전혀 없다
- 현재 absent가 자연스러운 이유
  - discourse change는 보이지만 `transition_over_surface`라는 이름이 요구하는
    조합형 단서가 없다
- 현재 seed combination으로 안 잡히는 이유
  - `transition` 맥락은 매우 약하고 `surface` 측 단서가 없다
- 판단
  - `no credible evidence`
  - patch로 해결할 문제보다 fixture evidence 부재에 가깝다

#### explanatory_mechanism

- candidate phrase/span
  - direct textual evidence: 없음
  - weak indirect cue:
    - `이후에는 다른 단계로 넘긴다`
    - 단계 전환 느낌은 있으나 `surface`/`표면` 계열 표현은 없다
- 현재 absent가 자연스러운 이유
  - mechanism에서 next stage로 넘어가는 흐름은 보이지만,
    그것이 `transition_over_surface`라는 특정 line wording을 직접 뒷받침하지는 않는다
- 현재 seed combination으로 안 잡히는 이유
  - 전환성은 일부 있지만 `surface` 축이 빠져 있다
- 판단
  - `weak indirect cue`
  - 현 wording 기준으로는 absent가 더 자연스럽다

#### argument_contrast

- candidate phrase/span
  - direct textual evidence: 없음
  - weak indirect cue:
    - `하지만 여러 line lens를 열면 다른 결과가 나온다`
    - contrast는 있으나 surface/표면 표현이 없다
- 현재 absent가 자연스러운 이유
  - contrast와 variation은 보이지만
    `transition_over_surface` 조합 단서로 보기엔 증거가 부족하다
- 현재 seed combination으로 안 잡히는 이유
  - `transition` 혹은 `surface` 어느 쪽도 명시되지 않는다
- 판단
  - `no credible evidence`
  - absent 유지가 자연스럽다

#### mixed_document

- candidate phrase/span
  - direct textual evidence: 없음
  - weak indirect cue:
    - `따라서 같은 문서 안에서도 여러 결이 다시 열린다`
    - `그러나 모든 조각을 묶으면 과잉 읽기가 생긴다`
    - 전환감은 있으나 surface/표면 표현은 없다
- 현재 absent가 자연스러운 이유
  - 문서 내부 variation과 contrast는 읽히지만,
    `transition_over_surface`라는 조합형 line을 직접 지지할 phrase는 거의 없다
- 현재 seed combination으로 안 잡히는 이유
  - `transition` 계열과 `surface` 계열이 함께 드러나는 wording이 없다
- 판단
  - `weak indirect cue`
  - under-reading보다는 evidence-poor fixture일 가능성이 더 높다

### candidate evidence spans or phrases

- `dialogue_continuation`
  - direct textual evidence: 없음
  - weak indirect cue: 화자 전환 느낌

- `explanatory_mechanism`
  - direct textual evidence: 없음
  - weak indirect cue: `이후에는 다른 단계로 넘긴다`

- `argument_contrast`
  - direct textual evidence: 없음
  - weak indirect cue: `하지만 여러 line lens를 열면`

- `mixed_document`
  - direct textual evidence: 없음
  - weak indirect cue:
    - `따라서 ... 다시 열린다`
    - `그러나 ... 과잉 읽기`

### why current absent may be justified

- 네 fixture 모두에서 `surface`/`표면` 계열 직접 표현이 거의 없다
- `transition`에 해당할 수 있는 discourse move는 일부 있으나,
  `transition_over_surface`라는 line 이름이 요구하는 조합형 evidence는 부족하다
- 따라서 현재 absent가 heuristic miss라기보다
  fixture wording 자체의 evidence scarcity일 가능성이 높다

### where under-reading is still plausible

- `explanatory_mechanism`
  - 단계 전환 문장은 transition 약한 단서로 읽을 여지가 있다
- `mixed_document`
  - `따라서`와 `그러나`가 이어지는 contrast/shift 흐름은
    transition 계열 약한 cue로 볼 여지는 있다

하지만 이 둘도 현재 wording만으로 `surface` 축까지 확보되진 않는다.

### non-goals

- no heuristic patch
- no keyword map edit
- no new fixture
- no aggregation or variation map work

### next patch gate

- 만약 current fixture 안에 credible direct evidence가 실제로 보인다면
  -> `transition_over_surface` evidence-basis minimal patch를 검토할 수 있다
- 현재처럼 credible direct evidence가 거의 없다면
  -> 이 fixture 세트에서는 absent 유지가 자연스럽고,
     이후 별도 evaluation asset이 필요하다고 본다

## user-language summary

### fixture-by-fixture reading

- `dialogue_continuation`
  - 전환 느낌은 있어도 `surface` 쪽 표현이 없어 credible evidence로 보기 어렵다
- `explanatory_mechanism`
  - 단계 전환 느낌은 있지만 `surface` 축이 없어 weak cue 수준이다
- `argument_contrast`
  - contrast는 있지만 `transition_over_surface`를 직접 지지하는 wording은 없다
- `mixed_document`
  - 흐름 변화는 있으나 `surface` 축이 없어 weak cue 수준이다

### direct evidence / weak cue / no credible evidence

- direct textual evidence
  - 네 fixture 모두 사실상 없음
- weak indirect cue
  - `explanatory_mechanism`, `mixed_document`
- no credible evidence
  - `dialogue_continuation`, `argument_contrast`

### user-language restatement

- 이번 턴에서 잠근 핵심은 단순하다
- 지금 문제는 partial-match rule 부족일 수도 있지만,
  그보다 먼저 현재 fixture 안에 `transition_over_surface` evidence 자체가 거의 없다는 점이 크다
- 그래서 지금은 patch보다 observation lock이 먼저다
