# input_to_reading_organ bounded reader narrowness inspection note v0

## verdict

현재 `line_input_to_reading_organ`은 candidate material이 없어서 `weak/caution`에 머무는 상태가 아니다.

현재 더 정확한 판정은 이렇다.

- material은 이미 있다
- input / processing / result 흐름도 candidate 안에 실제로 보인다
- 하지만 current bounded reader가 `processing flow`를 좁게 읽어서
  full flow를 `strong`까지 닫지 못한다

즉 이번 note의 핵심은
`transition_over_surface`처럼 material scarcity를 먼저 말하는 것이 아니라,
`input_to_reading_organ`에서 reader가 정확히 어디서 under-read하는지 분리하는 것이다.

## current observed limitation

현재 collected candidate들은 대체로 아래 구조를 이미 품고 있다.

- input arrival
- processing / interpretation / transformation
- result / output / changed readable state

그런데 current reader의 processing token set은 아래 쪽에 더 가깝다.

- `읽`
- `해석`
- `파싱`
- `처리`
- `변환`
- `정리`
- `가공`
- `parse`
- `interpret`
- `process`
- `transform`

그래서 실제 material에 많이 나오는 아래 표현을 좁게 읽는다.

- `routing`
- `제작`
- `자동으로 관련된 에이전트를 부른`
- `검증`

즉 current reader는 processing의 의미를 읽는 게 아니라
`processing token set에 직접 들어오는 표현`만 비교적 잘 읽는 상태에 가깝다.

## per-candidate inspection

### candidate 1

- source
  - [codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/handoffs/codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md)
- candidate text
  - `문서 입력 -> routing -> registry/provenance/event -> receipt/board/commands surface`
- input visible
  - `문서 입력`
- processing visible
  - `routing -> registry/provenance/event`
- result visible
  - `receipt/board/commands surface`
- where current reader stops short
  - `routing`을 processing으로 강하게 읽지 못한다
  - result side는 `surface`로 읽히지만 processing이 직접 토큰 매칭으로 닫히지 않아 `weak`에 머문다

### candidate 2

- source
  - [jump2_cleaned.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/jump2_cleaned.txt)
- candidate text
  - `카피라이팅 에이전트가 이런 프롬프트를 입력을 한 겁니다. 에이전트에 있는 가이드를 기반으로 자기가 작업할 메타프롬프팅을 제작을 한 겁니다. 그거에 대한 결과 리스폰스가 이렇게 쭉 나오게 되는 거죠.`
- input visible
  - `프롬프트를 입력`
- processing visible
  - `가이드를 기반으로 ... 메타프롬프팅을 제작`
- result visible
  - `결과 리스폰스가 ... 나오게`
- where current reader stops short
  - `제작`이 current processing token set에 직접 잡히지 않는다
  - 결과는 `response`로 잡히지만 processing 해석이 좁아 full flow를 strong으로 닫지 못한다

### candidate 3

- source
  - [jump_cleaned.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/jump_cleaned.txt)
- candidate text
  - `26년 부가세 예측해 줘라고 얘기를 했고요. 부가세라는 키워드를 보고 자동으로 관련된 에이전트를 부른 거예요. 그래서 결과를 다시 한번 다른 섹션에서 검증을 하게끔 합니다.`
- input visible
  - `부가세 예측해 줘`
- processing visible
  - `키워드를 보고 자동으로 관련된 에이전트를 부른`
- result visible
  - `결과를 다시 한번 다른 섹션에서 검증`
- where current reader stops short
  - `에이전트를 부른`을 processing/interpretation chain으로 약하게만 본다
  - `검증`도 post-result operation이지만 current token set에는 직접 없다
  - 그래서 semantic flow는 강한데 token coverage는 좁다

### candidate 4

- source
  - [repeated_learning_asset_exposure_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/repeated_learning_asset_exposure_baseline_v1.md)
- candidate text
  - `리뷰 리포트에서 결과와 판단 이유를 다시 되짚는 방식으로 반복 노출되어야 한다. 실행 결과만이 아니라 판단 이유도 같이 남긴다. 단순 output pattern만이 아니다.`
- input visible
  - 약함
- processing visible
  - `다시 되짚는`, `같이 남긴다` 정도의 후행 처리 감각만 있음
- result visible
  - `결과`, `output pattern`
- where current reader stops short
  - 여기서는 reader under-read보다 actual material limitation이 더 크다
  - input arrival이 거의 없어서 strong까지 못 가는 것이 정직하다

## separation of causes

### bounded-spec conservatism

- current spec은 `input -> processing -> result` 전 흐름을 비교적 엄격하게 본다
- 이 보수성 자체는 현재 branch에서 유지하는 것이 맞다
- 따라서 result가 있어도 processing이 직접 닫히지 않으면 `weak`에 머무는 구조가 자연스럽다

### current reader narrowness

이게 이번 note의 핵심 원인이다.

- `routing`
- `제작`
- `자동으로 ... 부른`
- `검증`

같은 실제 processing/interpretation/transform 의미가
current reader에서는 processing token set에 충분히 포섭되지 않는다.

즉 reader는 semantic flow를 본다고 했지만,
여전히 `좁은 processing 어휘`에 기댄 판독을 하고 있다.

### true material insufficiency

이건 candidate 4에 더 가깝다.

- `repeated_learning_asset_exposure_baseline_v1.md` 구절은
  result/output은 강하지만
  input arrival이 약하다
- 이 경우는 reader under-read보다 material 자체가 full flow를 덜 품고 있다

## explicit non-goals

- code patch 없음
- strong threshold widening 없음
- strong forcing 없음
- 다른 stable line과 혼합 분석 없음
- candidate-line expansion 없음

## recommendation

- next move
  - `refine reader interpretation narrowly`

이유:

- collected material 중 최소 3개는 input / processing / result를 실제로 품고 있다
- 현재 weak 지배는 material 부재보다 reader의 processing 해석 폭이 좁은 쪽에 더 가깝다
- 특히 `routing`, `제작`, `자동 라우팅`, `검증` 같은 처리 흐름을
  현재 bounded reader가 충분히 processing chain으로 읽지 못한다

즉 이 line의 다음 단계는
`transition_over_surface`처럼 더 많은 material을 먼저 모으는 것보다,
현재 collected material을 기준으로 reader가 어디까지 semantic interpretation을 좁게 하고 있는지
narrow patch 수준에서 다시 점검하는 쪽이 더 맞다.
