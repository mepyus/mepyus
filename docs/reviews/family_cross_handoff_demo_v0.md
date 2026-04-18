# Family Cross Handoff Demo v0

## 목적

이 문서는
각 family 내부 demo를 넘어서
한 family의 residue 또는 question shift가
다음 family entry를 여는 handoff 사례를 적는다.

대상:

- `input -> transition`
- `transition -> readout`

## 핵심 문장

family-cross handoff는
현재 family를 부정하는 것이 아니라
현재 family에서 남은 residue와 바뀐 질문이
다음 family issue-root를 여는 방식이다.

즉 handoff는
line spine의 절단이 아니라
family 간 재진입이다.

## case A. input -> transition

source family:

- `fam_input_to_reading`
- [loop_demo_case_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/loop_demo_case_v0.md)

current residue:

- `preprocess ambiguity residue`
- line readiness is not yet stable
- downstream path/breadth claims should not be made yet

handoff trigger:

- entry quality stabilizes enough for downstream reading
- 질문이 더 이상 “어떻게 넣을까”가 아니라 “왜 여기서 막히는가”로 바뀐다
- actual blockage/closure question opens

next family entry:

- signal:
  `transition_blockage`
- family:
  `fam_transition_thickening`
- projection:
  `proj_transition_preflight_reread`
- route:
  `route_preflight_reread`

의미:

input family는
entry shaping question을 다루고 끝난다.
그 다음 blockage/closure question이 열리는 순간
transition family가 시작된다.

## case B. transition -> readout

source family:

- `fam_transition_thickening`
- [loop_demo_case_transition_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/loop_demo_case_transition_v0.md)

current residue or state:

- unresolved transition edge remains
- thickening is active
- closure is not yet ready

handoff trigger:

- requested outcome becomes operator explanation
- question changes from reread to presentation
- operator wants readable explanation or board

next path has two variants.

### variant 1. same family projection shift

- family remains:
  `fam_transition_thickening`
- projection becomes:
  `proj_transition_operator_readout`
- route becomes:
  `route_readonly_board` or `route_internal_search`

이건 root family는 유지하고
operator-facing projection만 여는 경우다.

### variant 2. full handoff to readout family

- signal:
  `operator_overview_request` or `operator_search_query`
- family:
  `fam_operator_readout`
- projection:
  `proj_operator_board_readout` or `proj_operator_search_readout`
- route:
  `route_readonly_board` or `route_internal_search`

이건 question의 중심이 이미
transition condition 자체보다
operator-facing readability로 이동한 경우다.

## handoff 판단 기준

### 1. question shift가 artifact change보다 강하다

family-cross handoff는
source 종류보다
지금 무엇을 묻고 있는지가 더 중요하다.

### 2. residue는 handoff cue가 될 수 있다

현재 family residue는
다음 family entry bias를 만든다.

예:

- input residue:
  `preservation_before_flattening`
- transition residue:
  `closure_before_presentation`
- readout residue:
  `presentation_before_narrow_search`

### 3. projection shift와 full handoff를 구분해야 한다

- root family가 유지되면 projection shift
- root family가 바뀌면 full family handoff

## v0 판단

현재 가장 자연스러운 handoff는 아래다.

- input family에서 blockage/closure question이 열리면:
  full handoff to transition family
- transition family에서 operator explanation question이 열리면:
  first try projection shift, then full handoff to readout family if needed

## 한 줄 요약

family-cross handoff v0는
현재 family의 residue와 question shift가
다음 family의 issue-root를 여는 방식이며,
projection shift와 full family handoff를 구분해서 읽어야 한다.
