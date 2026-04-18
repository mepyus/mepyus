# Auto Hint Generation v0

## 목적

이 문서는
[source_to_family_hints_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/source_to_family_hints_v0.md)
의 수동 hint 예시를
어떤 규칙으로 자동 생성할 수 있는지 정한다.

현재 coverage에서 확인한 핵심 약점은 아래였다.

- source hint가 아직 수동 예시에 가깝다
- family마다 artifact knowledge를 사람이 직접 적어야 한다

따라서 v0에서는
`artifact field pattern -> candidate hint`
규칙을 최소 수준으로 먼저 고정한다.

## 핵심 문장

auto hint generation은
classifier를 대체하는 분류기가 아니다.

이건 artifact를 읽어
먼저 `candidate family/projection/route bias`
를 생성하는 얇은 adapter 층이다.

## 입력과 출력

### 입력

- artifact path
- artifact kind
- selected field patterns
- optional signal generation source match

### 출력

- `candidate_family_ids`
- `candidate_projection_ids`
- `candidate_route_ids`
- `hint_confidence`
- `hint_reason`
- `hint_source_fields`
- `residue_reentry_bias`

## v0 규칙 원칙

### 1. explicit field beats weak surface resemblance

명시 필드가 있으면
파일 경로나 폴더 이름보다 우선한다.

예:

- `before_gate.decision = preprocess_required`
- `active_latent_lines present`
- `items[].traceability_status exists`

### 2. same-root pattern bundle를 본다

한 필드 하나만 보지 않고,
같이 반복되는 bundle을 본다.

예:

- `before_gate.decision`
- `after_gate.decision`
- `pre_ingest_gate.status`

이 셋이 함께 있으면
input family preprocess shaping 쪽으로 강하게 기운다.

### 3. confidence는 field density와 specificity로 정한다

- `high`:
  same-root field bundle이 2~3개 이상 명확히 맞음
- `medium`:
  family는 맞지만 projection/route는 약함
- `low`:
  broad family hint만 겨우 성립

### 4. hint는 conservative first route를 우선한다

자동 생성은 항상
가장 보존적인 첫 route를 먼저 제안한다.

예:

- input family:
  `route_preprocess_compare_first`
- transition family:
  `route_preflight_reread`
- readout family:
  `route_readonly_board`

## v0 rule families

### 1. input preprocess shaping rule

trigger field bundle:

- `before_gate.decision = preprocess_required`
- `after_gate.decision = uncertain_needs_probe`
- `after_gate.checkpoints.pre_ingest_gate.status = uncertain_needs_probe`

generated hint:

- family:
  `fam_input_to_reading`
- projection:
  `proj_preprocess_shaping`
- route:
  `route_preprocess_compare_first`
- confidence:
  `high`
- residue bias:
  `preservation_before_flattening`

### 2. transition preflight reread rule

trigger field bundle:

- `active_latent_lines` exists
- `decision = thickening`
- `next_check_trigger` exists

generated hint:

- family:
  `fam_transition_thickening`
- projection:
  `proj_transition_preflight_reread`
- route:
  `route_preflight_reread`
- confidence:
  `high`
- residue bias:
  `closure_before_presentation`

### 3. operator broad readout rule

trigger field bundle:

- `items` array exists
- `items[].asset_id` exists
- `items[].maturation_state` exists
- `items[].traceability_status` exists

generated hint:

- family:
  `fam_operator_readout`
- projection:
  `proj_operator_board_readout`
- route:
  `route_readonly_board`
- confidence:
  `high`
- residue bias:
  `presentation_before_narrow_search`

## generation order

v0 auto generation은 아래 순서로 읽는다.

1. artifact path resolves
2. known rule bundle scan
3. highest-specificity bundle match
4. candidate hint object 생성
5. prebias layer로 전달

즉 지금은
general inference보다
`known high-value bundle matching`
에 가깝다.

## signal generation과의 관계

auto hint generation은
signal generation과 겹치지만 역할이 다르다.

- signal generation:
  artifact를 signal_kind로 번역
- auto hint generation:
  artifact를 family/projection/route bias로 번역

둘은 병렬로 존재할 수 있고,
둘 다 prebias 층으로 들어간다.

## v0 한계

### 1. known bundles only

현재는 세 family의 대표 bundle만 다룬다.

### 2. path-level heuristics가 약하다

지금은 field bundle이 중심이고,
경로/파일명 힌트는 보조다.

### 3. family-cross artifact는 아직 어렵다

하나의 artifact가 여러 family를 강하게 동시에 가리키는 경우는
아직 별도 tie-break가 필요하다.

## 다음 단계

이 문서 다음에는 아래 둘 중 하나가 자연스럽다.

1. `auto_hint_generation_rules_v0.json`
2. `hint_generation_adapter_stub_v0`

지금은 1번이 먼저다.

## 한 줄 요약

auto hint generation v0는
artifact field bundle을 읽어
conservative first family/projection/route hint를 자동으로 생성하는 최소 adapter 규칙이다.
