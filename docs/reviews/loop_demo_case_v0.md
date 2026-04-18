# Loop Demo Case v0

## 목적

이 문서는
[entry_execution_loop_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/entry_execution_loop_v0.md)의 구조를
실제 한 케이스에 통과시켜 본다.

목표는 두 가지다.

- 지금 만든 `signal -> classifier -> family -> projection -> route` 구조가 실제 artifact 하나에 붙는지 확인한다
- 이 흐름이 어디까지 `line/family/projection/route`만으로 추적 가능한지 다음 문서의 점검 재료를 만든다

## demo case 선택

이번 v0 demo case는
[builder_choi_interview_transcript_preprocess_comparison.json](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json)
이다.

이 artifact를 고른 이유는 아래와 같다.

- 실제 generated artifact가 이미 존재한다
- `before_gate` 와 `after_gate`가 함께 있어 entry ambiguity가 잘 보인다
- input family와 preprocess shaping projection을 시험하기 좋다
- residue가 남는 구조가 비교적 명확하다

## 1. source/artifact

source artifact:

- [builder_choi_interview_transcript_preprocess_comparison.json](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json)

이 artifact에서 바로 읽히는 핵심 사실:

- `before_gate.decision = preprocess_required`
- `after_gate.decision = uncertain_needs_probe`
- `after_gate.checkpoints.pre_ingest_gate.status = uncertain_needs_probe`
- raw transcript를 바로 ingest 하기에는 shape ambiguity가 남아 있다

## 2. signal detection

이 artifact는
[signal_generation_sources_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/signal_generation_sources_v0.json)
기준으로 `preprocess_ambiguity` signal을 낳는다.

signal 판단 이유:

- preprocess necessity가 이미 explicit하게 비교 artifact 안에 있다
- 최종 상태가 `uncertain_needs_probe` 이므로 flattening 없이 shaping-first entry가 필요하다
- 직접 ingest로 밀어넣기보다 compare/probe branch를 한 번 더 여는 것이 맞다

## 3. issue-root classifier

[issue_root_classifier_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/issue_root_classifier_v0.json)
기준으로 이 signal은 아래 entry를 가진다.

- `selected_family_id = fam_input_to_reading`
- `selected_projection_id = proj_preprocess_shaping`
- `initial_route_id = route_preprocess_compare_first`
- `confidence = high`
- `needs_review = false`

classifier reason을 이 케이스에 다시 붙이면:

- ambiguity는 downstream 해석보다 input shaping에서 먼저 다뤄야 한다
- projection은 direct entry보다 raw-return preservation 쪽이 맞다

## 4. family grounding

선택된 family는
`fam_input_to_reading`
이다.

[family_invariants_and_routes_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/family_invariants_and_routes_v0.md)
기준으로 이 family의 root invariant는 대략 아래 질문으로 재고정된다.

- problem_field:
  raw input이 readable entry로 넘어가기 전 shaping이 필요한가
- core_distinction:
  direct ingest 가능 input vs shaping/probe가 필요한 input
- transition_logic:
  input이 visible entry가 되기 전에 ambiguity를 줄여야 downstream line이 덜 왜곡된다
- judgment_question:
  지금 이 input은 바로 ingest 해야 하는가, compare/probe를 먼저 해야 하는가
- completion_criterion:
  direct ingest 또는 preprocess/probe branch 중 하나가 충분히 정당화된다

즉 이 케이스는 단순 파일 처리 문제가 아니라
`entry line family` 안에서
`preserve before normalize`
질문을 여는 issue-root가 된다.

## 5. projection selection

선택된 projection은
`proj_preprocess_shaping`
이다.

[projection_registry_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/projection_registry_v0.json)
기준으로 이 projection의 의미는 아래와 같다.

- projection_question:
  이 raw transcript를 future reading line을 죽이지 않고 어떻게 shape할 것인가
- bounded_space:
  `external_input_preprocess_space`
- preferred_route:
  `route_preprocess_compare_first`
- residue_return_path:
  preprocess ambiguity returns as future entry-shaping residue

즉 이번 데모는
`input family` 안에서도
`visible entry`가 아니라
`preprocess shaping` 쪽 면이 먼저 열리는 사례다.

## 6. route selection

선택된 route는
`route_preprocess_compare_first`
이다.

[route_registry_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/route_registry_v0.json)
기준으로 이 route의 핵심은 아래와 같다.

- mode_class:
  `preprocess`
- purpose_invariant:
  raw input reshaping 전에 preprocess necessity를 판단한다
- activation_conditions:
  transcript가 direct ingest에 비해 너무 raw하다
  또는 `uncertain-needs-probe` 상태가 보인다
- next_decision_points:
  `regroup-first`
  `post-preprocess probe`
  `return to direct ingest`

이번 artifact는 이미 `before/after comparison`을 갖고 있으므로
route의 `current_position_schema`도 맞아떨어진다.

## 7. execution/readout/validation outcome

이 route가 이번 케이스에서 실질적으로 만드는 outcome은 아래처럼 읽을 수 있다.

- before gate는 `preprocess_required`
- after gate는 `uncertain_needs_probe`
- 즉 완전한 direct ingest 허용으로 닫히지 않았다
- compare-first route가 계속 정당화된다
- immediate normalization보다 probe-aware shaping이 남는다

이 단계의 산출은:

- preprocess comparison result
- regroup candidate reference
- probe-first decision context

## 8. observed output

이번 loop의 observed output을 최소한으로 적으면 아래와 같다.

- selected_family:
  `fam_input_to_reading`
- selected_projection:
  `proj_preprocess_shaping`
- selected_route:
  `route_preprocess_compare_first`
- observed_status:
  `uncertain_needs_probe`
- immediate_action:
  do not flatten into canonical ingest yet
- next_branch:
  probe-first or regroup-first remains open

## 9. residue return

이번 케이스의 residue는
`preprocess ambiguity residue`
로 읽는 것이 맞다.

이 residue가 남기는 것은 아래다.

- transcript-like input은 regroup 후에도 바로 canonical ingest로 닫히지 않을 수 있다
- line readiness는 input quality stabilization 이후에만 읽어야 한다
- shard accumulation만으로 breadth/path 판단을 만들면 안 된다

즉 residue는 단순 미완료 표시가 아니라,
다음 entry에서도 `preservation before flattening`을 먼저 묻게 하는
future shaping bias로 남는다.

## 10. next loop / handoff

이번 데모에서 자연스러운 next loop는 세 가지다.

1. same-family next route

- `route_preprocess_compare_first`
- 이후 `regroup-first` 또는 `post-preprocess probe`

2. same-family fallback to direct ingest

- ambiguity가 충분히 해소되면
- `route_input_direct_ingest`

3. downstream handoff

- entry quality가 안정화된 뒤에만
- input family 바깥의 reading/transition 해석으로 넘긴다

## 요약

이 케이스는
`artifact -> preprocess_ambiguity -> fam_input_to_reading -> proj_preprocess_shaping -> route_preprocess_compare_first -> preprocess ambiguity residue`
로 비교적 선명하게 따라간다.

즉 지금 구조는
적어도 input shaping 계열의 issue-root 하나에 대해서는
실제 artifact를 family/projection/route spine 위에 올릴 수 있다.
