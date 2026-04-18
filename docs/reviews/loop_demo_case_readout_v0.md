# Loop Demo Case Readout v0

## 목적

이 문서는
[entry_execution_loop_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/entry_execution_loop_v0.md)
의 operator/readout 계열 적용 사례를 고정한다.

이번 목적은 아래 두 가지다.

- `operating_readout_space` 에도 같은 entry stack이 붙는지 본다
- broad overview surface가 실제로 `fam_operator_readout` 쪽 line spine을 여는지 확인한다

## demo case 선택

이번 v0 readout demo case는 아래 surface를 쓴다.

- [runtime/views/engine_state_latest/index.json](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_state_latest/index.json)

보조 reference:

- [app/work/operating_ui/operating_ui_payload_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/operating_ui_payload_adapter.py)
- [app/work/operating_ui/run_board_component_demo.py](/Users/sungsookim/universe/vectorfl_replica/app/work/operating_ui/run_board_component_demo.py)

이 surface를 고른 이유는 아래와 같다.

- broad overview readout의 대표 최신면이다
- asset list와 traceability/maturation 상태가 같이 있어 operator board에 적합하다
- signal generation source에서 이미 readout family 기본 source로 가정하고 있다

## 1. source/artifact

이번 케이스의 핵심 source facts:

- `items` array exists
- asset states are listed in one broad view
- each item includes `asset_id`, `maturation_state`, `traceability_status`, `updated_at`
- this is not a narrow query result but a broad current-state surface

즉 이 surface는
단일 answer가 아니라
operator가 현재 상태를 넓게 읽는 board entry에 가깝다.

## 2. signal detection

[signal_generation_sources_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/signal_generation_sources_v0.json)
기준으로 이번 케이스는
`operator_overview_request`
signal을 낳는 것이 맞다.

그 이유:

- `engine_state_latest object available`
- broad readout requested or implied
- narrow query is not required yet

이 조합은
search보다 overview board를 먼저 요구한다.

## 3. issue-root classifier

[issue_root_classifier_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/issue_root_classifier_v0.json)
기준으로 이 signal은 아래 entry를 가진다.

- `selected_family_id = fam_operator_readout`
- `selected_projection_id = proj_operator_board_readout`
- `initial_route_id = route_readonly_board`
- `confidence = high`
- `needs_review = false`

이건 현재 surface와 잘 맞는다.

- current state broad surface 존재
- explicit narrow query 없음
- operator-facing board readout이 먼저다

## 4. family grounding

선택된 family는
`fam_operator_readout`
이다.

[family_invariants_and_routes_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/family_invariants_and_routes_v0.md)
기준으로 root invariant를 다시 붙이면 아래와 같다.

- problem_field:
  current engine/process state becoming operator-readable
- core_distinction:
  raw state payload vs operator-facing readout
- transition_logic:
  state/update payload -> adapted model -> board/detail/search route
- judgment_question:
  현재 상태를 어떤 readout route로 보여주고 조작하게 할 것인가
- completion_criterion:
  operator가 현재 상태, 변화 흔적, 다음 조작점을 읽을 수 있다

즉 이 surface는
단순 JSON index가 아니라
operator readout family의 broad board issue-root다.

## 5. projection selection

선택된 projection은
`proj_operator_board_readout`
이다.

[projection_registry_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/projection_registry_v0.json)
기준 의미는 아래와 같다.

- projection_question:
  current engine state를 broad readable board로 어떻게 보여줄 것인가
- bounded_space:
  `operating_readout_space`
- preferred_route:
  `route_readonly_board`
- residue_return_path:
  presentation caution returns as readout residue

즉 이번 데모는
operator family 안에서도
`search`가 아니라
`board readout` 면이 먼저 열리는 사례다.

## 6. route selection

선택된 route는
`route_readonly_board`
이다.

[route_registry_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/route_registry_v0.json)
기준으로 이 route의 핵심은 아래와 같다.

- mode_class:
  `readout`
- purpose_invariant:
  present current state as broad operator board
- activation_conditions:
  engine_state_latest is available
  broad overview is requested
- next_decision_points:
  drill down to selected detail
  open activity panel
  launch internal search

이번 surface는 이미 broad index와 current update time을 함께 가지므로
route current position과 잘 맞는다.

## 7. execution/readout/validation outcome

이번 route가 만드는 실질 outcome은 아래처럼 읽을 수 있다.

- operator는 asset별 현재 상태를 한 번에 읽을 수 있다
- traceability/maturation/carryover risk를 broad board로 묶어 본다
- 아직 특정 asset으로 좁히지 않는다
- 필요하면 다음 단계로 selected detail 또는 internal search를 연다

즉 이 route는
현재 상태를 wide overview로 정돈하고,
다음 narrow route로 내려갈 수 있는 board를 만든다.

## 8. observed output

이번 loop의 observed output을 최소한으로 적으면 아래와 같다.

- selected_family:
  `fam_operator_readout`
- selected_projection:
  `proj_operator_board_readout`
- selected_route:
  `route_readonly_board`
- observed_status:
  `broad_operator_overview_available`
- immediate_action:
  keep board overview as first readout
- next_branch:
  selected detail or internal search remains available

## 9. residue return

이번 케이스의 residue는
`presentation caution residue`
로 읽는 것이 맞다.

이 residue가 남기는 것은 아래다.

- broad board만으로는 충분하지 않은 세부 설명 수요가 생길 수 있다
- 특정 asset explanation 요청은 search/detail route로 넘겨야 한다
- overview는 readout family의 첫면이지 끝면이 아니다

즉 residue는
board를 버리게 하는 것이 아니라
다음 readout route를 여는 operator attention cue로 남는다.

## 10. next loop / handoff

이번 데모에서 자연스러운 next loop는 세 가지다.

1. same-family narrow readout

- selected detail summary
- activity panel

2. same-family search expansion

- explicit query가 생기면
- `route_internal_search`

3. cross-family handoff

- 특정 transition explanation 요청이면
- `fam_transition_thickening`의 operator readout projection 쪽으로 넘길 수 있다

## 요약

이 케이스는
`surface -> operator_overview_request -> fam_operator_readout -> proj_operator_board_readout -> route_readonly_board -> presentation caution residue`
로 선명하게 따라간다.

즉 지금 구조는
input / transition뿐 아니라
operator broad readout 계열 issue-root에도 실제로 붙는다.
