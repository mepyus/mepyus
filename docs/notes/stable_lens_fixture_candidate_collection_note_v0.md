# stable lens fixture candidate collection note v0

## verdict

이번 수집은 stable lens 두 개만 다뤘다.

- `line_input_to_reading_organ`
- `line_transition_over_surface`

결론부터 말하면:

- `line_input_to_reading_organ`
  - 현재 수집한 후보만으로도 `enriched validation`을 한 번 돌려볼 수 있다
- `line_transition_over_surface`
  - strong-capable internal candidate는 확보됐다
  - 다만 자연어형 external candidate가 아직 얇아, validation은 가능하지만 이후 추가 수집 여지는 남는다

이번 note는 threshold를 넓히지 않는다.
line 이름을 echo하는 fake example도 넣지 않는다.

## line_input_to_reading_organ

### candidate 1

- source
  - [codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/handoffs/codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md)
- why candidate
  - `문서 입력 -> routing -> registry/provenance/event -> receipt/board/commands surface`
  - 입력 도착, 처리 경로, 결과 표면이 한 줄로 이어진다
- classification
  - `strong-flow candidate`
- semantic-flow present
  - input/material arrival: `문서 입력`
  - processing/transform: `routing -> registry/provenance/event`
  - result/output state: `receipt/board/commands surface`
- semantic-flow missing
  - 자연어 서술의 다양성은 적다
  - linked segment용으로는 약간 압축된 선언형 문장이다
- overfit risk
  - 중간
  - 너무 깔끔한 화살표 구조라 heuristic에 잘 맞을 수 있다
  - 그래도 line 이름 echo는 아니고 실제 internal material이라 허용 가능

### candidate 2

- source
  - [jump2_cleaned.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/jump2_cleaned.txt)
- why candidate
  - `프롬프트를 입력 -> 에이전트 가이드 기반 메타프롬프팅 제작 -> 결과 리스폰스`
  - 입력, 처리, 결과가 자연어로 이어진다
- classification
  - `strong-flow candidate`
- semantic-flow present
  - input/material arrival: `이런 프롬프트를 입력`
  - processing/transform: `가이드를 기반으로 ... 메타프롬프팅을 제작`
  - result/output state: `그거에 대한 결과 리스폰스가 이렇게 쭉 나오게`
- semantic-flow missing
  - 내부 reading organ보다는 agent workflow 설명에 가깝다
  - `읽기 기관`보다는 `업무 agent 흐름` 쪽으로 읽힐 가능성은 있다
- overfit risk
  - 낮음
  - 자연어가 충분히 거칠고 실제 사용 설명이라 keyword-only 최적화는 아니다

### candidate 3

- source
  - [jump_cleaned.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/jump_cleaned.txt)
- why candidate
  - `질문 -> 자동 에이전트 라우팅 -> 결과물 생성`
  - 업무 입력이 agent 구조에 흡수되는 흐름을 보여준다
- classification
  - `strong-flow candidate`
- semantic-flow present
  - input/material arrival: `부가세 예측해 줘`
  - processing/transform: `부가세라는 키워드를 보고 자동으로 관련된 에이전트를 부른`
  - result/output state: `결과를 다시 한번 다른 섹션에서 검증`, `결과물`
- semantic-flow missing
  - 결과가 `readout/result surface`보다는 business output에 더 가깝다
  - linked segment를 어떻게 자르느냐에 따라 full flow가 분산될 수 있다
- overfit risk
  - 낮음
  - heuristic을 만족시키려고 만든 문장이 아니라 실제 external material이다

### candidate 4

- source
  - [repeated_learning_asset_exposure_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/repeated_learning_asset_exposure_baseline_v1.md)
- why candidate
  - `실행 결과`, `판단 이유`, `output만 쌓지 않는다`
  - 결과면과 판단 흔적은 보인다
- classification
  - `caution-only candidate`
- semantic-flow present
  - result/output state: 강함
  - processing hint: 일부 있음
- semantic-flow missing
  - 입력 arrival이 약하다
  - full input -> processing -> result 흐름이 없다
- overfit risk
  - 낮음
  - 다만 strong용 asset으로 쓰면 과장 판정이 날 수 있다

### rejected / still insufficient

- source
  - [scripts/run_context_linked_segmentation_validation.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_context_linked_segmentation_validation.py)
- why rejected
  - current fixture origin으로는 유용하지만, 현 상태 문장들은 이미 `partial flow` 문제를 드러낸다
- classification
  - `still insufficient`
- semantic-flow present
  - 입력 또는 처리 힌트 일부
- semantic-flow missing
  - result/output closure가 약하다
- overfit risk
  - 중간
  - 현재 실패한 fixture를 그대로 재사용하면 gap을 반복할 가능성이 높다

## line_transition_over_surface

### candidate 1

- source
  - [multi_lens_runtime_flow.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/multi_lens_runtime_flow.py)
- why candidate
  - `raw_result -> surfaced_readout -> handoff_boundary -> supervisor surface`
  - 전환 행위와 전후 표면이 모두 선명하다
- classification
  - `strong-flow candidate`
- semantic-flow present
  - transition/movement: `stops_after`, `next_owner`, `handoff`
  - boundary/surface: `raw_reading_result`, `surfaced_readout`, `supervisor_surface`
  - before/after structure: 명확함
- semantic-flow missing
  - 자연어형 문장보다는 code/runtime naming에 가깝다
- overfit risk
  - 중간
  - runtime naming이 직접적이라 heuristic에 잘 맞을 수 있다
  - 그래도 실제 body material이라 정당성은 높다

### candidate 2

- source
  - [codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/handoffs/codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md)
- why candidate
  - `문서가 들어오고, routing 되고, 기록되고, 조회 surface로 남는 경로`
  - `latest surface`, `per-run surface`, `pointer surface`
  - 내부에서 surface로 넘어가는 운영 언어가 직접 있다
- classification
  - `strong-flow candidate`
- semantic-flow present
  - transition/movement: `들어오고`, `routing 되고`, `기록되고`, `남는 경로`
  - boundary/surface: `receipt/board/commands surface`, `latest surface`, `per-run surface`
  - before/after structure: input side -> surface side가 보임
- semantic-flow missing
  - handoff/boundary가 한 linked segment에서 얼마나 응집적으로 잡힐지는 확인이 필요하다
- overfit risk
  - 낮음
  - internal prose지만 line name echo가 아니고 실제 운영 문장이다

### candidate 3

- source
  - [operating_surface_composition_rule_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/operating_surface_composition_rule_v0.md)
- why candidate
  - `입력 -> line 상태 -> 관찰 표면 -> handoff -> close-out`
  - surface sequence를 직접 말한다
- classification
  - `caution-only candidate`
- semantic-flow present
  - surface/layer: 강함
  - ordering/sequence: 강함
- semantic-flow missing
  - 실제 전환 행위가 구체적이지 않다
  - `A에서 B로 넘어간다`보다는 panel order 설명에 가깝다
- overfit risk
  - 낮음
  - 하지만 strong fixture로 쓰면 surface 단어만 많고 transition body는 약할 수 있다

### candidate 4

- source
  - [openclaw-main/VISION.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/openclaw-main/VISION.md)
- why candidate
  - `channels`, `plugins`, `MCP bridge`, `CLI/web frontend` 같은 표면 언어는 많다
- classification
  - `still insufficient`
- semantic-flow present
  - surface/boundary vocabulary
- semantic-flow missing
  - конкрет한 one-step transition before/after가 약하다
  - 현재 note 기준 stable lens evaluation asset로는 너무 넓고 서술적이다
- overfit risk
  - 중간
  - surface/layer 단어가 많아 lexical false positive를 부를 수 있다

### candidate 5

- source
  - [claude-code-main/README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/README.md)
- why candidate
  - `terminal`, `IDE`, `Github`, `plugins` 등 표면 후보는 있다
- classification
  - `still insufficient`
- semantic-flow present
  - multiple surface nouns
- semantic-flow missing
  - explicit transition/boundary movement
  - before/after flow
- overfit risk
  - 높음
  - plugin/surface nouns만으로 over-read될 가능성이 있다

## synthetic fixture candidates

현재 수집 상태에서는 synthetic fixture를 아직 강하게 열 필요는 없다.

- `line_input_to_reading_organ`
  - strong-capable real/internal + allowed external 후보가 이미 3개 있다
- `line_transition_over_surface`
  - strong-capable internal 후보가 2개 있다

즉 지금 synthetic으로 먼저 메우기보다,
현재 수집 후보로 한 번 enriched validation을 돌려보고
transition 쪽 자연어 다양성이 부족할 때만 synthetic을 좁게 여는 게 맞다.

## final recommendation

### line_input_to_reading_organ

- recommendation
  - `run enriched validation`
- reason
  - current collected candidates already include
    - strong-capable internal 1개
    - strong-capable external 2개
    - caution-only control 1개
  - strong / caution 구분을 시험해볼 최소 세트는 확보됐다

### line_transition_over_surface

- recommendation
  - `run enriched validation`, but keep collection open after the run
- reason
  - strong-capable internal 2개는 확보됐다
  - caution-only control 1개도 있다
  - 다만 external natural-language strong candidate는 아직 얇다
  - 따라서 validation은 가능하지만, 결과가 너무 runtime-internal naming에 치우치면 추가 수집이 필요하다

## short grouped index

### line_input_to_reading_organ

- strong-flow candidate
  - [codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/handoffs/codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md)
  - [jump2_cleaned.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/jump2_cleaned.txt)
  - [jump_cleaned.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/jump_cleaned.txt)
- caution-only candidate
  - [repeated_learning_asset_exposure_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines/repeated_learning_asset_exposure_baseline_v1.md)
- still insufficient
  - [run_context_linked_segmentation_validation.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_context_linked_segmentation_validation.py)

### line_transition_over_surface

- strong-flow candidate
  - [multi_lens_runtime_flow.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/multi_lens_runtime_flow.py)
  - [codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/handoffs/codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md)
- caution-only candidate
  - [operating_surface_composition_rule_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/operating_surface_composition_rule_v0.md)
- still insufficient
  - [VISION.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/openclaw-main/VISION.md)
  - [README.md](/Users/sungsookim/universe/vectorfl_replica/references/git_search/claude-code-main/README.md)
