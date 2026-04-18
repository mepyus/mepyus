# stable lens fixture enrichment spec v0

## verdict

현재 stable lens 두 개의 `strong` 부재는 우선적으로 `material` 문제로 다뤄야 한다.

- `line_input_to_reading_organ`
  - current fixture는 `입력 + 처리` 또는 `처리만` 보여주는 경우가 많다
  - `input -> processing -> result` 전체 흐름이 부족하다
- `line_transition_over_surface`
  - current fixture는 `변화`나 `다음 단계`는 보이지만
  - `boundary/surface/layer + transition` 구조가 부족하다

따라서 다음은 strong 기준을 넓히는 patch가 아니라,
`현재 stable lens가 legitimately strong으로 살아날 수 있는 evaluation asset`을 어떻게 더 넣을지 정의하는 단계다.

## target stable lenses

- `line_input_to_reading_organ`
- `line_transition_over_surface`

이번 spec은 이 두 line만 다룬다.

다루지 않는 것:

- `line_pre_read_eye`
- `line_raw_return_preservation`
- candidate line 전반
- multi-line conflict
- numeric scoring

## line_input_to_reading_organ

### strong에 필요한 semantic-flow

아래 세 요소가 한 linked segment 안에서 실제 흐름으로 붙어 있어야 한다.

- `input/material arrival`
  - 자료/입력/문서/조각이 들어온다
- `processing / interpretation / transformation`
  - 읽기/처리/해석/정리/변환이 일어난다
- `result / output / changed readable state`
  - 결과가 나온다
  - 읽을 수 있는 상태로 바뀐다
  - 다음 기관/표면으로 넘길 수 있는 상태가 된다

strong 예시 구조:

- `문서를 받아 -> 구조를 정리하고 -> 읽기 가능한 결과를 만든다`
- `입력을 넣으면 -> parsing/interpretation을 거쳐 -> output/readout이 나온다`

### caution에만 충분한 것

아래는 `caution` 또는 `weak`까지는 가능하지만 strong은 아니다.

- 입력만 있음
- 처리만 있음
- 처리 + 결과만 있음
- 입력 + 처리만 있음
- contrast 문맥에서 결과가 언급됨
- low linkage confidence 상태에서 전환/처리 힌트만 있음

현재 fixture 예:

- `우리는 먼저 입력을 다시 읽어야 합니다. / 그렇지 않으면 얇은 조각만 남습니다.`
  - 입력 + 읽기 힌트는 있음
  - 결과가 output/result 흐름으로 명시되지 않음
- `이 장치는 먼저 입력의 배경을 정리한다. / 예를 들면 약한 조각을 앞뒤 문맥으로 다시 잇는다.`
  - 입력 + 처리 흐름은 있음
  - 결과면이 닫히지 않음

### absent로 남는 경우

- 입력/자료 유입 흔적이 없음
- 처리/해석/변환 흔적이 없음
- 결과/출력/읽힌 상태 변화가 없음

## line_transition_over_surface

### strong에 필요한 semantic-flow

아래 두 묶음이 같이 있어야 한다.

- `transition / movement`
  - 넘어간다
  - 전환된다
  - handoff 된다
  - shift / move across / cross
- `boundary / surface / layer before-and-after`
  - 어느 표면에서 어느 표면으로 가는지
  - 어떤 경계를 넘는지
  - `A에서 B로`, `내부에서 표면으로`, `runtime에서 handoff로`

strong 예시 구조:

- `내부 정리 단계에서 supervisor surface로 넘어간다`
- `runtime 결과를 handoff boundary를 통해 operating surface로 올린다`
- `API boundary를 건너 UI layer로 이동한다`

### caution에만 충분한 것

- `다음 단계로 넘긴다`처럼 전환 느낌만 있음
- 상태 변화는 있지만 어떤 표면/경계인지 없음
- low linkage confidence 상태에서 전환 힌트만 있음
- contrast 문맥에서 이전/이후가 암시될 뿐 표면 전환이 명시되지 않음

현재 fixture 예:

- `이후에는 다른 단계로 넘긴다.`
  - 전환 감각은 있음
  - 전후 표면이 없음
- `그 차이가 이후 reread의 출발점이 된다.`
  - 상태 변화/후속 출발점은 있음
  - 표면/경계 전환은 아님

### absent로 남는 경우

- 전환 행위가 없음
- 경계/표면/레이어 언급이 없음
- 전환 전후 구조가 없음

## material enrichment directions

### A. real internal text candidates

다음은 현재 repo 안에서 strong semantic-flow 후보가 될 가능성이 있는 real material이다.

#### input_to_reading_organ 쪽

- [source_assets/handoffs/codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/handoffs/codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md)
  - `문서 입력 -> routing -> registry/provenance/event -> receipt/board/commands surface`
  - 입력에서 처리, 그리고 결과 표면까지 이어지는 구조가 이미 문장으로 있다
- [source_assets/baselines/repeated_learning_asset_exposure_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/repeated_learning_asset_exposure_baseline_v1.md)
  - `실행 결과`, `판단 이유`, `user-layer translation` 관련 구절
  - 입력/처리/결과 연결 후보가 있다
- [scripts/run_context_linked_segmentation_validation.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_context_linked_segmentation_validation.py)
  - current fixture는 약하지만 enrichment용 synthetic guidance source로는 좋다

#### transition_over_surface 쪽

- [app/core/runtime/multi_lens_runtime_flow.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/multi_lens_runtime_flow.py)
  - `raw_result -> surfaced_readout -> handoff_boundary -> supervisor surface`
  - 전후 표면과 handoff가 분명하다
- [source_assets/handoffs/codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/handoffs/codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md)
  - `latest surface`, `per-run surface`, `pointer surface` 구절
  - surface/layer/boundary 언어가 직접 있다
- [docs/specs/operating_surface_composition_rule_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/operating_surface_composition_rule_v0.md)
  - `readiness -> line state -> surfaced observation -> boundary -> close-out`
  - surface 전환의 운영적 서술 후보가 있다

### B. external reference candidates already allowed into the space

아래는 이미 calibration/reference로 들어와 있어 enrichment source로 허용 가능한 external material이다.

#### input_to_reading_organ 쪽

- [inputs/external_cases/jump_cleaned.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/jump_cleaned.txt)
  - 업무 입력이 Claude Code/agent 구조로 흡수되어 결과물로 바뀌는 흐름이 많다
- [inputs/external_cases/jump2_cleaned.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/jump2_cleaned.txt)
  - 설치/선택/확장/사용 흐름이 들어 있어 input-processing-result candidate가 있다

#### transition_over_surface 쪽

- [references/git_search/claude-code-main](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main)
  - plugin / hook / command / agent 분리
  - surface/layer 전환을 설명하는 material source가 될 수 있다
- [references/git_search/openclaw-main](/Users/sungsookim/universe/vectorfl_replica/references/git_search/openclaw-main)
  - context / approval / lane / loader / runtime organ 구조
  - transition + boundary + destination 구조가 풍부하다

### C. synthetic fixture candidates if necessary

real internal / allowed external material만으로 strong 예시를 균형 있게 못 만들 때만 synthetic fixture를 허용한다.

허용 synthetic fixture 조건:

- line 이름을 그대로 echo하지 않는다
- 실제 repo에서 이미 보이는 의미 흐름만 압축해 재구성한다
- 한 문장 안에 모든 신호를 과하게 다 넣지 않는다
- linked segment 수준에서 자연스럽게 읽히는 길이로 유지한다

synthetic 방향:

- `input_to_reading_organ`
  - 입력 도착
  - 처리/정리
  - readout/result/surface-ready
  를 분명하게 보여주는 2~3 segment mini flow
- `transition_over_surface`
  - before surface
  - handoff / boundary
  - after surface
  를 분명하게 보여주는 2~3 segment mini flow

## explicit guardrails

- strong threshold widening 금지
- line 이름을 그대로 반복하는 fake example 금지
- ontology식 정의문 fixture 금지
- candidate line 확장 금지
- `keyword만 맞춘 문장` 금지
- 현재 heuristic에 맞춘 과잉 최적화 fixture 금지

## evaluation-asset design guidance

### how to create/select examples that show full flow

#### input_to_reading_organ

example selection rule:

- 입력 주체가 보여야 한다
- 처리/해석 단계가 보여야 한다
- 결과/출력/읽힌 상태 변화가 보여야 한다
- 세 요소가 같은 linked segment chain 안에서 이어져야 한다

good shape:

- `문서를 받아서 정리한 뒤 supervisor가 읽을 수 있는 결과면으로 올린다`

bad shape:

- `입력을 읽는다`
- `처리한다`
- `결과가 좋다`

세 문장이 따로 놀면 full flow가 아니다.

#### transition_over_surface

example selection rule:

- 전환 행위가 보여야 한다
- 전후 두 표면이 최소 암시되어야 한다
- handoff/boundary/layer/surface 중 최소 하나가 있어야 한다

good shape:

- `raw output을 handoff boundary를 거쳐 surfaced view로 넘긴다`

bad shape:

- `다음 단계로 간다`
- `상태가 바뀐다`

전환의 방향과 경계가 없으면 strong용 asset이 아니다.

### how to avoid overfitting fixtures to the heuristic

- 한국어/영어 표현을 하나의 단어 세트로만 몰지 않는다
- 같은 의미를 다른 표현으로도 구성한다
- input/result, transition/boundary를 직접 말하되 line 이름은 쓰지 않는다
- 하나의 fixture가 한 line에만 과하게 맞지 않게 한다
- weak/caution asset도 같이 유지한다
- strong asset과 weak/caution asset의 비율을 함께 본다

즉 strong fixture만 늘리는 게 아니라,
`현재 stable lens가 strong/weak/caution/absent를 모두 분리할 수 있는지`를 보는 자산 세트로 가야 한다.

## next-step decision rule

다음 조건이 충족되면 enrichment가 충분하다.

- `line_input_to_reading_organ`
  - full `input -> processing -> result` asset이 최소 2개 이상 있다
  - partial flow asset도 같이 있다
- `line_transition_over_surface`
  - `transition + boundary/surface` asset이 최소 2개 이상 있다
  - transition-only asset도 같이 있다
- real internal or allowed external material이 최소 절반 이상이다
  - synthetic이 majority가 되면 안 된다

이 조건을 만족하면:

- validation을 다시 돌린다

아직 아래 상태면 hold가 맞다.

- strong asset이 synthetic 위주다
- current material에서 full flow를 아직 정직하게 못 뽑았다
- weak/caution/absent와의 구분이 불안정하다

즉 enrichment가 충분할 때만 re-run하고,
그 전에는 heuristic을 더 만지지 말고 hold한다.

## what this is not

이 spec은 아래를 하지 않는다.

- heuristic patch 작성
- strong 기준 완화
- numeric scoring
- candidate line 확장
- ontology식 line 정의 잠금

이 spec은 오직:

- stable lens strong semantic-flow에 필요한 material 조건
- enrichment source 방향
- evaluation asset 설계 기준
- re-run vs hold decision rule

만 고정한다.
