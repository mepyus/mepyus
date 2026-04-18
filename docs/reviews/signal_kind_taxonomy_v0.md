# Signal Kind Taxonomy v0

## 목적

이 문서는 `issue_root_classifier_v0` 가 사용하는
`signal_kind` 를 더 체계적으로 정리한다.

지금 classifier는 이미 작동 가능한 rule set을 갖고 있지만,
입력 신호 vocabulary가 아직 얇다.

따라서 이 문서는

- 어떤 signal_kind가 있는지
- 각 signal이 무엇을 뜻하는지
- 각 signal이 어떤 family-rooted alias를 갖는지
- 어떤 family로 주로 들어가는지
- 어떤 artifact/sign을 함께 보는지

를 고정한다.

## 핵심 원칙

### 1. signal은 issue-root entry 단위다

signal은 family나 route가 아니다.

signal은
“지금 어떤 종류의 entry 문제/요청/상황이 열렸는가”
를 나타내는 입력 표식이다.

### 2. signal은 family 선택 이전에 읽힌다

classifier는 먼저 signal을 읽고,
그 다음 family/projection/route를 고른다.

### 3. signal은 표면 제목보다 artifact와 requested outcome을 함께 본다

오직 제목만으로 signal을 고정하지 않는다.

### 4. signal에는 family-rooted alias를 함께 둘 수 있다

v0부터는 기존 `signal_kind` 를 유지하면서도,
각 signal이 어떤 family invariant conflict인지 더 빨리 드러내는
`family_rooted_alias` 를 함께 둘 수 있다.

## signal category

v0에서는 아래 세 category로 나눈다.

- `entry_signal`
- `transition_signal`
- `readout_signal`

## 1. entry_signal

입력 진입과 shapeing에 관련된 신호

포함:

- `raw_input`
- `preprocess_ambiguity`

## 2. transition_signal

전환, 막힘, thickening, corridor boundary에 관련된 신호

포함:

- `transition_blockage`
- `boundary_ambiguity`

## 3. readout_signal

operator overview, search, explanation 표면에 관련된 신호

포함:

- `operator_overview_request`
- `operator_search_query`

## signal 정의

## 1. raw_input

### category

`entry_signal`

### 의미

새 재료가 아직 entry shaping 이전 상태로 들어온 경우

### family-rooted alias

`input_family_entry_material`

### 주 신호

- transcript, note, memo, article 같은 raw material 존재
- split/trace/readable entry가 아직 없음 또는 막 생성되려 함

### 주 family

`fam_input_to_reading`

### 대표 projection

`proj_input_ingest_visibility`

### 대표 route

`route_input_direct_ingest`

## 2. preprocess_ambiguity

### category

`entry_signal`

### 의미

raw input을 바로 넣을지,
먼저 reshape/compare/probe 해야 할지 애매한 경우

### family-rooted alias

`input_family_preservation_conflict`

### 주 신호

- transcript too noisy
- uncertain-needs-probe
- preprocess necessity unresolved

### 주 family

`fam_input_to_reading`

### 대표 projection

`proj_preprocess_shaping`

### 대표 route

`route_preprocess_compare_first`

## 3. transition_blockage

### category

`transition_signal`

### 의미

현재 전환이 왜 막혔는지,
active line이 어떤 상태인지 다시 읽어야 하는 경우

### family-rooted alias

`transition_family_closure_conflict`

### 주 신호

- phase decision exists
- active latent line exists
- blockage explanation requested

### 주 family

`fam_transition_thickening`

### 대표 projection

`proj_transition_preflight_reread`

### 대표 route

`route_preflight_reread`

## 4. boundary_ambiguity

### category

`transition_signal`

### 의미

지금 local reread만으로는 부족하고,
corridor/stage lineage를 따라 경계를 좁혀야 하는 경우

### family-rooted alias

`transition_family_boundary_narrowing_conflict`

### 주 신호

- stage outputs exist
- corridor boundary note exists
- narrowing still needed

### 주 family

`fam_transition_thickening`

### 대표 projection

`proj_transition_corridor_validation`

### 대표 route

`route_stage_corridor_probe`

## 5. operator_overview_request

### category

`readout_signal`

### 의미

operator가 현재 상태를 넓게 보고 싶어 하는 경우

### family-rooted alias

`operator_family_broad_readout_request`

### 주 신호

- engine_state_latest exists
- overview requested
- search보다 board가 먼저 필요한 상황

### 주 family

`fam_operator_readout`

### 대표 projection

`proj_operator_board_readout`

### 대표 route

`route_readonly_board`

## 6. operator_search_query

### category

`readout_signal`

### 의미

operator가 좁은 질의나 특정 answer route를 먼저 원할 때

### family-rooted alias

`operator_family_narrow_query_request`

`readout_signal`

### 의미

operator가 특정 질문/키워드/내부 route를 찾으려는 경우

### 주 신호

- explicit query text exists
- internal search surface available

### 주 family

`fam_operator_readout`

### 대표 projection

`proj_operator_search_readout`

### 대표 route

`route_internal_search`

## override signal reading

### 1. transition_blockage + operator_explanation

signal 자체는 `transition_blockage` 이지만
requested outcome이 `operator_explanation` 이면

- family는 transition에 두고
- projection만 readout projection으로 바꾼다

즉 root는 유지하고 surface만 달라진다.

### 2. raw_input + blockage question

raw input artifact가 있어도
질문이 전환/막힘 설명이면
entry signal보다 transition signal 해석을 우선 검토한다.

## v0 taxonomy 기대 수준

v0에서 중요한 것은 완벽한 taxonomy가 아니다.

중요한 것은 classifier 입력면이 아래처럼 보이게 되는 것이다.

- signal category
- signal meaning
- main artifact hints
- default family/projection/route
- override 가능성

## 다음 단계 연결

이 taxonomy 다음에는
classifier가 쓰는 signal 필드와 registry를 더 정교하게 맞추거나,
rule 충돌 우선순위를 따로 잠그는 것이 자연스럽다.
