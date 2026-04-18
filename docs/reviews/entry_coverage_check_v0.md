# Entry Coverage Check v0

## 목적

이 문서는 지금까지 만든 세 demo case를 한 장에서 비교한다.

대상:

- [loop_demo_case_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/loop_demo_case_v0.md)
- [loop_demo_case_transition_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/loop_demo_case_transition_v0.md)
- [loop_demo_case_readout_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/loop_demo_case_readout_v0.md)

핵심 질문은 아래다.

- 지금 만든 entry grammar가 세 family 모두에 실제로 붙는가
- 어디까지가 공통 구조이고, 어디서부터 family별 차이가 커지는가
- 지금 구조를 `general entry spine` 으로 불러도 되는가

## 결론 먼저

현재 v0에서는
`input / transition / readout`
세 family 모두에
동일한 entry spine이 붙는다.

즉 아래 공통 구조는 세 경우 모두 성립한다.

`artifact or surface -> source hint -> family-rooted alias -> signal_kind -> classifier -> family -> projection -> route -> residue`

다만
family에 들어간 뒤의 실제 판단 질문과 residue 성격은 꽤 다르다.

즉 지금 구조는
`공통 entry grammar + family-specific execution meaning`
으로 읽는 것이 맞다.

## 1. coverage table

### case 1. input family

- source:
  [builder_choi_interview_transcript_preprocess_comparison.json](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json)
- hint:
  `fam_input_to_reading`
- alias:
  `input_family_preservation_conflict`
- signal:
  `preprocess_ambiguity`
- family:
  `fam_input_to_reading`
- projection:
  `proj_preprocess_shaping`
- route:
  `route_preprocess_compare_first`
- residue:
  `preprocess ambiguity residue`

### case 2. transition family

- source:
  [runtime/preflight_last_decision.json](/Users/sungsookim/universe/vectorfl_replica/runtime/preflight_last_decision.json)
- hint:
  `fam_transition_thickening`
- alias:
  `transition_family_closure_conflict`
- signal:
  `transition_blockage`
- family:
  `fam_transition_thickening`
- projection:
  `proj_transition_preflight_reread`
- route:
  `route_preflight_reread`
- residue:
  `unresolved transition edge residue`

### case 3. readout family

- source:
  [runtime/views/engine_state_latest/index.json](/Users/sungsookim/universe/vectorfl_replica/runtime/views/engine_state_latest/index.json)
- hint:
  `fam_operator_readout`
- alias:
  `operator_family_broad_readout_request`
- signal:
  `operator_overview_request`
- family:
  `fam_operator_readout`
- projection:
  `proj_operator_board_readout`
- route:
  `route_readonly_board`
- residue:
  `presentation caution residue`

## 2. 공통으로 성립하는 것

### 2-1. artifact-first entry

세 경우 모두
entry는 line이 아니라
artifact 또는 surface에서 시작한다.

즉 현재 구조는 끝까지
source reading을 버리지 않는다.

### 2-2. hint가 classifier를 미리 기울인다

세 경우 모두
[source_to_family_hints_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/source_to_family_hints_v0.json)
에 high-confidence hint를 둘 수 있었다.

즉 source가 이미
family/projection/route 쪽 bias를 준다.

### 2-3. alias가 family 질문을 더 빨리 연다

세 경우 모두
signal은 단순 상태명이 아니라
family-rooted alias를 같이 가질 수 있었다.

즉 entry vocabulary는 점점
artifact 상태명보다 family question 쪽으로 이동한다.

### 2-4. classifier 이후에는 line spine이 안정적이다

세 경우 모두
family에 들어간 뒤에는
projection / route / residue 추적이 비교적 안정적이다.

즉 current v0의 강점은
여전히 `entry 이후의 line spine` 이다.

## 3. family별로 달라지는 것

### 3-1. input family

핵심 질문:

- readable entry로 넣을 수 있는가
- preservation before flattening이 필요한가

즉 distinction이
`entry visibility vs preprocess shaping`
쪽에 강하다.

### 3-2. transition family

핵심 질문:

- 현재 전환이 왜 closure-ready가 아닌가
- reread를 계속할지, corridor narrowing으로 갈지

즉 distinction이
`active condition vs closure`
쪽에 강하다.

### 3-3. readout family

핵심 질문:

- broad board가 먼저인가
- narrow search/detail로 내려가야 하는가

즉 distinction이
`broad overview vs narrow operator route`
쪽에 강하다.

## 4. 어디까지 general entry spine인가

현재 구조를 general entry spine으로 부를 수 있는 이유는 아래다.

- source에서 시작한다
- source hint를 둘 수 있다
- alias로 family 질문을 열 수 있다
- classifier가 family/projection/route를 고른다
- residue가 다시 family로 되돌아간다

즉 이 문법 자체는 세 family에서 공통이다.

다만 아직 general runtime engine이라고 부르기엔 이른 이유도 있다.

- signal generation은 여전히 family별 artifact knowledge에 의존한다
- hint 생성도 아직 수동 예시에 가깝다
- classifier는 rule-based 문서/registry 수준이다

## 5. 지금 구조를 어떻게 불러야 하나

지금 단계에서 가장 정확한 표현은 아래 둘 중 하나다.

- `family-spanning entry grammar`
- `line-centered multi-family entry spine`

이건 이미
한 family에만 맞는 local trick은 아니다.

하지만 아직
fully generalized engine adapter도 아니다.

## 6. 다음 과제

coverage 관점에서 다음 과제는 세 가지다.

### 6-1. auto hint generation

지금은 source hint가 수동 예시다.
다음엔 artifact field를 읽어 hint를 자동 생성하는 규칙이 필요하다.

### 6-2. family-cross handoff demo

지금 demo는 각 family 내부에서 닫힌다.
다음엔 `input -> transition`, `transition -> readout` handoff 사례가 필요하다.

### 6-3. residue-backed reentry demo

지금은 residue를 적었지만,
그 residue가 다음 entry에서 실제 bias로 돌아오는 사례는 아직 없다.

## 한 줄 요약

현재 VectorFL v0의 entry 구조는
`input / transition / readout` 세 family 모두에 붙는 공통 line-centered entry grammar까지는 도달했지만,
아직 자동 hint 생성과 residue-backed reentry까지 닫힌 상태는 아니다.
