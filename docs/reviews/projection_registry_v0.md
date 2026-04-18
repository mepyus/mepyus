# Projection Registry v0

## 목적

이 문서는 [projection_registry_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/projection_registry_v0.json)
을 현재 family 기반 projection의 첫 registry로 고정한다.

projection registry는

- family invariant
- bounded space
- line facet emphasis
- preferred route

를 한 객체 안에서 이어 붙인다.

## 현재 포함된 projection

### fam_input_to_reading

- `proj_input_ingest_visibility`
- `proj_preprocess_shaping`

### fam_transition_thickening

- `proj_transition_preflight_reread`
- `proj_transition_corridor_validation`
- `proj_transition_operator_readout`

### fam_operator_readout

- `proj_operator_board_readout`
- `proj_operator_search_readout`

## registry 의미

이 registry가 생기면서
이제 같은 family 안에서도
무엇이 다른 projection인지 명시적으로 말할 수 있다.

예를 들면:

- 같은 `fam_input_to_reading` 이라도
  `ingest visibility` 와 `preprocess shaping` 은
  다른 changed facet, 다른 preferred route, 다른 output을 가진다.

- 같은 `fam_transition_thickening` 이라도
  `preflight reread`, `corridor validation`, `operator readout` 은
  decision/validation/readout 층위가 다르다.

## 아직 남은 약점

### 1. projection selection policy는 아직 없다

지금은 route selection policy만 있고,
projection을 언제 우선 고를지에 대한 정책은 별도 필요하다.

### 2. issue-root에서 바로 projection으로 들어가는 규칙은 아직 없다

현재는 family와 route를 거쳐서만 설명된다.

### 3. projection과 실제 runtime evidence 연결은 더 촘촘해질 수 있다

지금은 material_sources 수준이다.

## 다음 단계

다음으로 자연스러운 일은 아래 둘 중 하나다.

1. `projection_selection_policy_v0` 를 만들어 family 안에서 어떤 projection을 먼저 볼지 정한다
2. 또는 `issue_root_classifier_v0` 를 만들어 issue-root가 어느 family/projection으로 들어갈지 정한다

현재로서는 2번이 더 상위라서 먼저다.
