# Signal Kind Taxonomy Registry v0

## 목적

이 문서는 [signal_kind_taxonomy_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/signal_kind_taxonomy_v0.json)
을 현재 classifier 입력 신호의 첫 taxonomy registry로 고정한다.

## 현재 category

- `entry_signal`
- `transition_signal`
- `readout_signal`

## 현재 signal_kind

- `raw_input`
- `preprocess_ambiguity`
- `transition_blockage`
- `boundary_ambiguity`
- `operator_overview_request`
- `operator_search_query`

## registry 의미

이 registry가 생기면서
classifier 입력이 단순 문자열 모음이 아니라,

- category
- meaning
- artifact hints
- default family/projection/route
- override notes

를 가진 structured vocabulary가 된다.

## 아직 남은 약점

### 1. signal generation path는 아직 없다

지금은 taxonomy만 있고,
어떤 관찰기나 입력기에서 이 signal을 생산하는지는 별도다.

### 2. category 수가 아직 적다

v0는 entry/transition/readout 세 갈래만 쓴다.

### 3. override 우선순위는 아직 classifier policy 쪽에 남아 있다

taxonomy는 vocabulary를 주고,
충돌 해소는 아직 별도 정책이 필요하다.

## 다음 단계

다음으로 자연스러운 일은 아래 둘 중 하나다.

1. `classifier_priority_policy_v0` 를 만들어 rule 충돌 우선순위를 잠근다
2. 또는 `signal_generation_sources_v0` 를 만들어 어떤 runtime/work artifact가 어떤 signal을 낳는지 연결한다

현재로서는 1번이 더 직접적이다.
