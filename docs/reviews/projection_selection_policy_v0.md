# Projection Selection Policy v0

## 목적

이 문서는 family 안에서
어떤 `projection_line` 을 먼저 볼지에 대한
최소 selection policy를 고정한다.

지금 구조는 이미 아래를 갖고 있다.

- signal taxonomy
- issue-root classifier
- classifier priority policy
- family invariant
- projection registry
- route registry
- route selection policy

하지만 family 안에서
projection을 어떤 순서로 먼저 열어야 하는지는
아직 별도 정책이 없었다.

## projection selection의 역할

projection selection은 아래를 정한다.

1. 같은 family 안에 여러 projection이 있을 때
   무엇을 먼저 본다
2. 언제 다른 projection으로 넘어간다
3. broad projection과 narrow projection이 겹칠 때
   무엇을 우선한다

즉 이 정책은
family 내부의 `projection precedence` 다.

## 기본 원칙

### 1. narrower projection wins

같은 family 안에서 더 좁고 더 문제지향적인 projection이 있으면
그걸 더 broad한 projection보다 먼저 본다.

### 2. preservation before flattening

entry/transition 계열에서는
원본과 residue를 더 잘 보존하는 projection을 먼저 본다.

### 3. decision before presentation

같은 family 안에서
실제 판단용 projection과 presentation/readout projection이 같이 있을 때,
판단용 projection을 먼저 본다.

단, operator-facing requested outcome이 explicit하면 예외다.

### 4. explanation projection is downstream

readout projection은
같은 family 안의 reading/decision projection을 대체하지 않는다.

대개는 그 결과를 표면화하는 downstream projection이다.

## family별 v0 정책

## 1. fam_input_to_reading

### candidate projections

- `proj_input_ingest_visibility`
- `proj_preprocess_shaping`

### selection rule

기본 우선순위는 아래다.

1. raw transcript가 noisy하거나 preprocess ambiguity가 있으면 `proj_preprocess_shaping`
2. direct entry가 가능하면 `proj_input_ingest_visibility`

### 왜

- `proj_preprocess_shaping` 이 더 좁고 보존적이다
- `proj_input_ingest_visibility` 는 더 broad하고 entry를 빠르게 여는 projection이다

### fallback

- ambiguity 해소 후
  `proj_preprocess_shaping` -> `proj_input_ingest_visibility`
- direct ingest에서 residue 확대 시
  `proj_input_ingest_visibility` -> `proj_preprocess_shaping`

## 2. fam_transition_thickening

### candidate projections

- `proj_transition_preflight_reread`
- `proj_transition_corridor_validation`
- `proj_transition_operator_readout`

### selection rule

기본 우선순위는 아래다.

1. active latent line / phase signal reread가 필요하면 `proj_transition_preflight_reread`
2. staged lineage와 boundary narrowing이 핵심이면 `proj_transition_corridor_validation`
3. operator-facing explanation이 explicit하면 `proj_transition_operator_readout`

### 왜

- `proj_transition_preflight_reread` 는 가장 local하고 판단지향적이다
- `proj_transition_corridor_validation` 은 더 넓고 staged lineage 중심이다
- `proj_transition_operator_readout` 은 presentation/downstream 성격이 강하다

### fallback

- local reread만으로 부족하면
  `proj_transition_preflight_reread` -> `proj_transition_corridor_validation`
- 판단은 끝났고 표면화가 필요하면
  `proj_transition_preflight_reread` 또는 `proj_transition_corridor_validation`
  -> `proj_transition_operator_readout`

## 3. fam_operator_readout

### candidate projections

- `proj_operator_board_readout`
- `proj_operator_search_readout`

### selection rule

기본 우선순위는 아래다.

1. explicit query가 있으면 `proj_operator_search_readout`
2. broad overview면 `proj_operator_board_readout`

### 왜

- search projection이 더 좁고 목적지향적이다
- board projection은 broad overview와 general readout을 위한 projection이다

### fallback

- search 결과가 너무 빈약하거나 broad context가 더 필요하면
  `proj_operator_search_readout` -> `proj_operator_board_readout`
- board만으로 부족하고 narrow 탐색이 필요하면
  `proj_operator_board_readout` -> `proj_operator_search_readout`

## override 규칙

### 1. requested_outcome explicit override

요청 결과가 명시적으로 projection을 가리키면
기본 precedence보다 우선한다.

예:

- `transition_blockage`
- `requested_outcome=operator_explanation`

이 경우
`proj_transition_operator_readout`
가
`proj_transition_preflight_reread`
보다 우선할 수 있다.

### 2. current_artifacts stronger than generic signal

generic signal보다
특정 artifact가 projection을 더 강하게 가리키면
그 projection을 우선 검토할 수 있다.

예:

- stage corridor outputs가 분명하면
  `proj_transition_corridor_validation` 우선

## v0 precedence summary

projection 충돌 시 아래 순서로 우선한다.

1. explicit projection override
2. narrower projection
3. preservation-oriented projection
4. decision-oriented projection
5. broad readout projection
6. fallback projection
7. `needs_review`

## 현재 결론

이 policy가 생기면
이제 family 안에서도
무엇을 먼저 볼지 문서적으로 잠겼다.

즉 스택은 아래처럼 더 닫힌다.

- signal
- classifier
- family
- projection selection
- route selection

## 다음 단계

다음으로 자연스러운 일은 아래 둘 중 하나다.

1. `signal_to_classifier_binding_v0`
2. `entry_execution_loop_v0`

현재로서는 2번이 더 다음 실험에 가깝다.
