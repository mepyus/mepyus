# Classifier Priority Policy v0

## 목적

이 문서는 [issue_root_classifier_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/issue_root_classifier_v0.json)
안의 rule이 겹치거나 충돌할 때
무엇을 우선 적용할지 정한다.

즉 이 문서는
classifier의 `conflict resolution policy` 다.

## 왜 필요한가

현재 classifier는 rule set을 이미 갖고 있지만,
아래 같은 충돌이 생길 수 있다.

- 같은 signal_kind에 override rule과 default rule이 동시에 걸릴 때
- broad signal과 narrow signal이 같이 보일 때
- raw_input artifact가 있지만 실제 질문은 blockage explanation일 때
- operator overview와 operator search가 동시에 암시될 때

이럴 때 우선순위가 없으면
입구가 흔들린다.

## 기본 우선순위 원칙

### 1. override beats default

`requested_outcome` 같은 명시 override가 있으면
같은 signal_kind의 default rule보다 우선한다.

예:

- `transition_blockage`
- `requested_outcome=operator_explanation`

이 조합이면
`cls_rule_transition_readout_override`
가
`cls_rule_transition_blockage`
보다 우선한다.

### 2. narrower signal beats broader signal

더 구체적인 signal이 있으면
더 넓은 signal보다 우선한다.

예:

- `preprocess_ambiguity` 가 있으면 `raw_input`보다 우선
- `operator_search_query` 가 있으면 `operator_overview_request`보다 우선

### 3. question intent beats raw artifact presence

현재 artifact보다
질문이 요구하는 판단/설명 방향이 더 강할 수 있다.

예:

- raw transcript가 있어도
  질문이 “왜 지금 막혔는가”이면
  transition 계열 우선 검토

### 4. preservation beats flattening

entry/transition 계열에서는
보존성이 높은 분류를 먼저 택한다.

예:

- `preprocess_ambiguity` 우선
- `transition_blockage` reread 우선

### 5. operator clarity beats broad exploration

readout 계열에서는
operator가 더 빨리 이해할 수 있는 narrow match가 있으면
그걸 broad overview보다 먼저 쓴다.

## v0 precedence order

충돌 시 아래 순서로 우선한다.

1. explicit override rule
2. more specific signal_kind
3. requested_outcome-aligned rule
4. preservation-oriented rule
5. default family rule
6. fallback family
7. `needs_review=true`

## 실제 규칙 적용

## 1. input family

### case A

- `raw_input`
- `preprocess_ambiguity`

동시에 보이면:

- `preprocess_ambiguity` 우선

이유:

- 더 구체적이다
- 보존성이 높다
- direct entry보다 ambiguity review가 먼저다

### case B

- `raw_input` artifact
- 질문이 blockage explanation

이 경우:

- input rule보다 transition rule 검토 우선

이유:

- question intent beats artifact presence

## 2. transition family

### case A

- `transition_blockage`
- `requested_outcome=operator_explanation`

동시에 보이면:

- `cls_rule_transition_readout_override` 우선

이유:

- explicit override
- root family는 유지하면서 projection만 readout으로 바꾸는 것이 가장 보존적이다

### case B

- `transition_blockage`
- `boundary_ambiguity`

동시에 보이면:

- 현재 active line 상태를 먼저 읽어야 하면 `transition_blockage`
- stage lineage narrowing이 더 직접적이면 `boundary_ambiguity`

tie-break:

- active latent line / phase decision가 있으면 `transition_blockage`
- corridor stage artifacts가 더 강하면 `boundary_ambiguity`

## 3. readout family

### case A

- `operator_overview_request`
- `operator_search_query`

동시에 보이면:

- explicit query가 있으면 `operator_search_query` 우선
- query가 없고 broad overview만 있으면 `operator_overview_request`

이유:

- narrower signal beats broader signal

## review로 보내는 조건

아래 경우는 무리하게 classifier를 확정하지 않고
`needs_review=true` 로 남기는 편이 낫다.

- signal_kind가 둘 이상인데 우선순위 근거가 약함
- requested_outcome이 classifier vocabulary 밖에 있음
- current_artifacts가 family를 서로 다르게 가리킴
- default family와 override family가 모두 부적절해 보임

## v0 policy 요약

충돌 시 핵심 문장은 아래다.

- override가 기본보다 우선
- 더 구체적인 신호가 더 넓은 신호보다 우선
- 질문 의도가 artifact보다 강할 수 있음
- 보존성이 높은 분류를 먼저 고름
- 그래도 애매하면 review로 남김

## 다음 단계 연결

이 policy 다음에는
아래 둘 중 하나가 자연스럽다.

1. `signal_generation_sources_v0`
2. `projection_selection_policy_v0`

현재로서는 1번이 더 상위다.
