# Family-Rooted Signal Grammar v0

## 목적

이 문서는
[signal_kind_taxonomy_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/signal_kind_taxonomy_v0.md)
의 signal vocabulary를
조금 더 family-rooted하게 바꾸기 위한 중간 단계다.

[line_only_traceability_check_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/line_only_traceability_check_v0.md)
에서 확인했듯이,
현재 entry는 아직 artifact vocabulary에 많이 의존한다.

따라서 v0에서는
기존 `signal_kind` 를 버리지 않고,
각 signal에 `family-rooted alias` 를 붙인다.

## 핵심 원칙

### 1. 기존 signal_kind는 유지한다

지금 classifier와 registry는
`raw_input`, `preprocess_ambiguity` 같은 현재 이름으로 이미 맞물려 있다.

v0에서는 기존 이름을 깨지 않는다.

### 2. family-rooted alias를 함께 둔다

signal을
단순 상태명으로만 두지 않고,
어떤 family invariant conflict인지 같이 적는다.

즉 signal은

- current signal_kind
- family_rooted_alias

둘을 함께 가진다.

### 3. alias는 same-root 감각을 더 빨리 열어야 한다

좋은 alias는
artifact 상태 자체보다
어떤 family 질문이 열렸는지를 먼저 보여줘야 한다.

## alias 설계 원칙

alias는 가능하면 아래를 드러내야 한다.

- 어느 family에 속하는가
- 어떤 core distinction이 흔들리는가
- 지금 preservation / narrowing / explanation 중 무엇이 문제인가

## v0 alias table

### 1. raw_input

- signal_kind:
  `raw_input`
- family_rooted_alias:
  `input_family_entry_material`

의미:

- 아직 shaping 이전이지만
- root family는 input entry 쪽임이 분명하다

### 2. preprocess_ambiguity

- signal_kind:
  `preprocess_ambiguity`
- family_rooted_alias:
  `input_family_preservation_conflict`

의미:

- direct ingest보다
- preservation before flattening 질문이 먼저 열린다

### 3. transition_blockage

- signal_kind:
  `transition_blockage`
- family_rooted_alias:
  `transition_family_closure_conflict`

의미:

- 현재 transition line이 닫히지 못하고
- reread 또는 explanation이 필요하다

### 4. boundary_ambiguity

- signal_kind:
  `boundary_ambiguity`
- family_rooted_alias:
  `transition_family_boundary_narrowing_conflict`

의미:

- local status만으로는 부족하고
- staged corridor lineage를 따라 narrowing이 필요하다

### 5. operator_overview_request

- signal_kind:
  `operator_overview_request`
- family_rooted_alias:
  `operator_family_broad_readout_request`

의미:

- query가 아니라
- state surface 전체를 먼저 읽고 싶은 요청이다

### 6. operator_search_query

- signal_kind:
  `operator_search_query`
- family_rooted_alias:
  `operator_family_narrow_query_request`

의미:

- broad board보다
- 좁은 질의 기반 route가 먼저 열린다

## 왜 필요한가

이 alias 층이 있으면
entry vocabulary가 아래처럼 바뀐다.

- before:
  artifact 상태명 위주
- after:
  family 질문 위주

즉 classifier가
“이건 preprocess ambiguity다”
에서 멈추지 않고
“이건 input family의 preservation conflict다”
라고 더 빨리 말할 수 있다.

## v0 한계

이 alias는 아직 classifier를 대체하지 않는다.

현재는

- artifact
- signal_kind
- family_rooted_alias
- classifier

순으로 보는 것이 맞다.

즉 alias는
entry를 line 쪽으로 더 당기는 보조 층이다.

## 한 줄 요약

family-rooted signal grammar v0는
기존 signal_kind를 유지한 채,
각 signal이 어떤 family invariant conflict인지 더 빨리 드러내는 alias 층이다.
