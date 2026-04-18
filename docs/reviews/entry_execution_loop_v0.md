# Entry Execution Loop v0

## 목적

이 문서는 지금까지 만든 구조를
실제 한 번의 운용 루프로 묶는다.

지금까지는 아래가 이미 있다.

- signal taxonomy
- signal generation sources
- issue-root classifier
- classifier priority policy
- bounded functional spaces
- upper family layer
- root family invariants
- projection registry
- projection selection policy
- route registry
- route selection policy

이제 필요한 것은
이것들이 어떤 순서로 한 번의 실행 사이클을 이루는지 적는 것이다.

## 핵심 문장

한 번의 entry 실행은 아래 순서로 간다.

- source/artifact를 읽는다
- signal을 생성한다
- issue-root를 family로 분류한다
- family 안에서 projection을 고른다
- projection에 맞는 route를 고른다
- 그 route를 통해 state/action/readout을 수행한다
- 결과와 residue를 append-only로 남긴다
- 필요하면 다음 family 또는 다음 route로 handoff 한다

## loop 개요

```text
artifact/source
-> signal_kind
-> classifier
-> family
-> projection
-> route
-> execution / readout / validation
-> observed output + residue
-> reinject / handoff / next loop
```

## step-by-step v0

## 1. source capture

입력은 실제 artifact/surface/operator input에서 시작한다.

예:

- raw transcript
- preprocess comparison result
- phase decision log
- stage corridor output
- engine_state_latest
- internal search query

이 단계는 [signal_generation_sources_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/signal_generation_sources_v0.json) 기준으로 읽는다.

## 2. signal detection

source에서 `signal_kind` 를 감지한다.

예:

- raw_input
- preprocess_ambiguity
- transition_blockage
- boundary_ambiguity
- operator_overview_request
- operator_search_query

이 단계는 [signal_kind_taxonomy_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/signal_kind_taxonomy_v0.json)과
[signal_generation_sources_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/signal_generation_sources_v0.json)을 함께 본다.

## 3. classifier entry

감지된 signal과 requested outcome, current artifacts를 바탕으로
첫 entry를 고른다.

출력:

- `selected_family_id`
- `selected_projection_id`
- `initial_route_id`
- `confidence`
- `needs_review`

이 단계는 [issue_root_classifier_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/issue_root_classifier_v0.json)과
[classifier_priority_policy_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/classifier_priority_policy_v0.md)을 따른다.

## 4. family grounding

선택된 family가 실제로 무엇을 묻는지 다시 고정한다.

즉 아래를 현재 issue-root에 다시 붙인다.

- problem_field
- core_distinction
- transition_logic
- judgment_question
- completion_criterion

이 단계는 [family_invariants_and_routes_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/family_invariants_and_routes_v0.md)을 따른다.

## 5. projection selection

family 안에서
현재 무엇을 먼저 봐야 하는지 결정한다.

예:

- input family에서는 preprocess shaping vs ingest visibility
- transition family에서는 preflight reread vs corridor validation vs operator readout
- readout family에서는 board vs search

이 단계는 [projection_selection_policy_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/projection_selection_policy_v0.md)와
[projection_registry_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/projection_registry_v0.json)을 따른다.

## 6. route selection

선택된 projection이 선호하는 route들 중
현재 상황에 맞는 route를 고른다.

예:

- direct ingest
- compare-first preprocess
- preflight reread
- stage corridor probe
- readonly board
- internal search

이 단계는 [route_selection_policy_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/route_selection_policy_v0.md)와
[route_registry_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/route_registry_v0.json)을 따른다.

## 7. route execution

route가 실제로 state/readout/validation/action을 수행한다.

예:

- manifest/split/board 생성
- preprocess comparison/reshape 판단
- phase reread와 next check trigger 도출
- stage corridor validation 실행
- readonly board 또는 search 결과 생성

이 단계는 bounded space의 action surface 안에서 일어난다.

## 8. observed output capture

실행 결과를 단순 output으로 끝내지 않고,
현재 loop 관점에서 관찰 가능한 산출로 적는다.

출력 예:

- source_manifest / split_units / readable_input_board
- preprocess comparison result
- updated phase decision
- reread observation entry
- board excerpt / selected detail / search result

## 9. residue return

실행 뒤 남는 것을 residue로 되돌린다.

질문:

- 이 residue가 같은 family thickening인가
- projection fallback 신호인가
- 다음 family handoff 신호인가

예:

- preprocess ambiguity residue
- unresolved transition edge
- presentation caution
- query/result mismatch

## 10. handoff or next loop

결과에 따라 다음으로 간다.

### same-family next route

예:

- preprocess shaping 후 direct ingest
- preflight reread 후 corridor validation
- readonly board 후 internal search

### cross-family handoff

예:

- input family -> transition family
- transition family -> readout family

### stop and hold

애매하면 `needs_review` 또는 residue hold로 남긴다.

## loop 사례

## case A. noisy transcript entry

1. source:
   preprocess comparison JSON
2. signal:
   `preprocess_ambiguity`
3. classifier:
   `fam_input_to_reading`
   -> `proj_preprocess_shaping`
   -> `route_preprocess_compare_first`
4. execution:
   preprocess necessity, regroup/probe 판단
5. residue:
   ambiguity remains -> next shaping residue
6. next:
   ambiguity 해소 시 `proj_input_ingest_visibility`

## case B. transition blockage explanation

1. source:
   phase decision log with `active_latent_lines`
2. signal:
   `transition_blockage`
3. classifier:
   `fam_transition_thickening`
   -> `proj_transition_preflight_reread`
   -> `route_preflight_reread`
4. execution:
   current thickening/closure position 재판독
5. residue:
   unresolved edges remain
6. next:
   boundary ambiguity persists -> `proj_transition_corridor_validation`

## case C. operator asks a narrow question

1. source:
   internal search query
2. signal:
   `operator_search_query`
3. classifier:
   `fam_operator_readout`
   -> `proj_operator_search_readout`
   -> `route_internal_search`
4. execution:
   search result and selected context 생성
5. residue:
   query/result mismatch 남김 가능
6. next:
   result가 빈약하면 broad board fallback

## v0에서 중요한 것

v0의 핵심은 완전한 자동 엔진이 아니다.

핵심은 지금까지 흩어져 있던 구조를
하나의 운용 문장으로 묶는 것이다.

즉 이제 VectorFL의 entry path는 아래로 말할 수 있다.

- 어떤 source가 signal을 낳고
- 그 signal이 classifier를 통해 family/projection/route를 고르고
- 실행 결과와 residue가 다시 다음 loop의 source가 된다

## 현재 결론

이 문서가 생기면
지금 구조는 단순한 문서 모음이 아니라
`conceptual execution loop` 로 읽힌다.

즉 실제 코드 엔진은 아직 아니어도,
개념적으로는 이미 한 바퀴 도는 운용 루프가 생긴다.

## 다음 단계

다음으로 자연스러운 일은 아래 둘 중 하나다.

1. `entry_execution_trace_schema_v0`
2. `loop_demo_case_v0`

현재로서는 2번이 더 가볍고 바로 검증 가능하다.
