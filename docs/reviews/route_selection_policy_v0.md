# Route Selection Policy v0

## 목적

이 문서는 [route_registry_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/route_registry_v0.json)
에 들어 있는 route들 중
현재 어떤 route를 먼저 고를지에 대한
최소 selection policy를 고정한다.

v0의 목적은 full scheduler가 아니라
과활성화와 애매한 선택을 줄이는 것이다.

## selection 기본 원칙

### 1. family first

먼저 family를 고른다.
route는 그 다음이다.

즉 순서는 아래다.

1. 현재 issue/root signal이 어느 family에 속하는가
2. 그 family 안에서 어떤 route가 활성 조건에 더 맞는가
3. exclusion 조건이 없는가
4. fallback이 필요한가

### 2. narrower route wins

같은 family 안에서 둘 다 열릴 수 있으면,
더 좁고 더 특수한 route를 먼저 쓴다.

이유:

- broad route를 먼저 열면 residue가 평평해진다
- 특수 route가 필요한 상황을 놓친다

### 3. preservation before collapse

input과 transition 계열에서는
먼저 보존성이 높은 route를 고른다.

예:

- 무작정 closure보다 reread
- 무작정 direct ingest보다 preprocess compare

### 4. operator clarity before cleverness

readout 계열에서는
먼저 operator가 가장 빨리 이해할 수 있는 route를 연다.

예:

- broad state overview가 필요한 상황에서 internal search부터 열지 않는다

## family별 v0 정책

## 1. fam_input_to_reading

### candidate routes

- `route_input_direct_ingest`
- `route_preprocess_compare_first`

### selection rule

기본 우선순위는 아래다.

1. preprocess necessity ambiguity가 보이면 `route_preprocess_compare_first`
2. ambiguity가 없고 split-first entry가 가능하면 `route_input_direct_ingest`

### practical reading

- raw transcript가 거칠거나
- uncertain-needs-probe 류 판정이 있으면
  direct ingest보다 compare-first를 우선한다

- 반대로 입력이 이미 읽기 가능한 수준이면
  direct ingest를 우선한다

### fallback

- `route_input_direct_ingest` 실패/잔여 확대
  -> `route_preprocess_compare_first`
- `route_preprocess_compare_first`에서 ambiguity 해소
  -> `route_input_direct_ingest`

## 2. fam_transition_thickening

### candidate routes

- `route_preflight_reread`
- `route_stage_corridor_probe`

### selection rule

기본 우선순위는 아래다.

1. active latent line과 phase signal이 있으면 `route_preflight_reread`
2. stage lineage가 분명하고 boundary ambiguity를 좁혀야 하면 `route_stage_corridor_probe`

### practical reading

- 현재 문제를 “지금 active line이 어떤 상태인가”로 읽는 경우
  `route_preflight_reread`가 기본이다

- corridor lineage를 따라 boundary를 실제로 더 좁혀야 할 때만
  `route_stage_corridor_probe`로 간다

### fallback

- `route_preflight_reread` 후 boundary ambiguity가 유지
  -> `route_stage_corridor_probe`
- `route_stage_corridor_probe` 후 local evidence가 다시 필요
  -> `route_preflight_reread`

## 3. fam_operator_readout

### candidate routes

- `route_readonly_board`
- `route_internal_search`

### selection rule

기본 우선순위는 아래다.

1. broad overview 요청이거나 현재 상태를 먼저 보여줘야 하면 `route_readonly_board`
2. explicit query가 있고 broad board보다 탐색이 필요한 경우 `route_internal_search`

### practical reading

- operator가 “지금 상태가 뭐지?”에 가깝다면
  `route_readonly_board`

- operator가 “이 문제와 관련된 내부 route나 근거가 뭐지?”에 가깝다면
  `route_internal_search`

### fallback

- `route_readonly_board`에서 더 좁은 탐색 필요
  -> `route_internal_search`
- `route_internal_search` 결과가 빈약하거나 과한 경우
  -> `route_readonly_board`

## cross-family handoff 정책

### 1. input -> transition

입력 family에서 direct ingest 또는 preprocess shaping이 끝난 뒤,
실제 전환/막힘/두꺼워짐 판단이 필요하면
`fam_transition_thickening`으로 넘긴다.

### 2. transition -> readout

transition family에서 나온 판단이
operator-facing explanation이나 현재 상태 해석으로 가야 하면
`fam_operator_readout`으로 넘긴다.

### 3. readout does not replace transition

readout family는 설명과 표면화가 목적이지,
transition 판단 자체를 대체하지 않는다.

## selection order 요약

v0에서 route 선택 순서는 아래로 고정한다.

1. family 판정
2. activation condition 확인
3. exclusion condition 확인
4. same-family 특수 route 우선
5. broad route fallback
6. 필요 시 다음 family handoff

## 아직 약한 부분

### 1. signal 값이 정량화돼 있지 않다

지금은 `high residue`, `ambiguity`, `overview request` 같은 문장형 규칙이 많다.

### 2. policy는 projection registry와 아직 분리돼 있다

나중에는 projection layer와 함께 읽어야 더 정확해진다.

### 3. family selection도 아직 문서적이다

issue-root classifier 수준의 규칙은 다음 단계에서 별도 필요하다.

## 현재 결론

v0에서 중요한 것은 완벽한 자동 선택이 아니다.

중요한 것은 아래를 잠그는 것이다.

- 같은 family 안에서 무엇을 먼저 여는가
- 언제 fallback 하는가
- 언제 다음 family로 넘기는가

이 정책이 있어야 route registry가
단순 목록이 아니라 실제 운용 규칙으로 읽힌다.
