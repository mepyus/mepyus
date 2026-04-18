# Residue-Backed Reentry Rule v0

## 목적

이 문서는
현재 family에서 남은 residue가
다음 entry에서 어떤 family/projection/route bias를 만들 수 있는지 정한다.

이건
[family_cross_handoff_case_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/family_cross_handoff_case_v0.md)
다음 단계다.

즉 handoff reasoning을
문장 설명에서
최소 재진입 규칙으로 내리는 것이다.

## 핵심 문장

residue-backed reentry는
source artifact를 대체하지 않는다.

다만 새 artifact가 열릴 때
과거 residue가
어느 family bias를 먼저 줄지
prebias 층에 추가로 개입한다.

즉 reentry는 아래처럼 읽는다.

- new source artifact
- previous residue bias
- question shift
- reentry prebias
- classifier

## 기본 원칙

### 1. residue is a bias, not a forced jump

residue가 있다고 해서
무조건 다음 family로 강제 이동하지는 않는다.

residue는
new artifact와 question이 맞을 때만
family bias를 강화한다.

### 2. residue must be same-chain plausible

아무 residue나 아무 family에 붙이지 않는다.

reentry는
`same-chain plausible`
해야 한다.

즉 residue와 next question이
서로 이어진 해석 경로여야 한다.

### 3. question shift gates residue reuse

가장 중요한 건
질문이 실제로 바뀌었는가다.

예:

- `entry shaping` 질문이 계속되면 input family에 남는다
- `blockage/closure` 질문이 열리면 transition family bias가 켜진다
- `operator readability` 질문이 열리면 readout family bias가 켜진다

### 4. residue bias is weaker than explicit contradiction

새 artifact가 residue와 정면으로 충돌하면
새 artifact가 더 강하다.

즉 residue는 prebias를 주지만,
classifier override를 이기지는 못한다.

## v0 residue classes

### 1. preservation_before_flattening

source family:

- `fam_input_to_reading`

의미:

- 너무 빨리 canonical ingest나 closure로 닫지 말라

next family bias:

- same family:
  `proj_preprocess_shaping`
- cross family:
  `fam_transition_thickening`

reentry 조건:

- input quality question이 어느 정도 정리됨
- 이제 blockage/closure question이 열린다

resulting bias:

- `transition_family_closure_conflict`
- `proj_transition_preflight_reread`
- `route_preflight_reread`

### 2. closure_before_presentation

source family:

- `fam_transition_thickening`

의미:

- 먼저 closure readiness를 보고,
  presentation은 그 다음에 하라

next family bias:

- same family:
  `proj_transition_preflight_reread`
- cross family:
  `fam_operator_readout`

reentry 조건:

- operator explanation or overview question이 열린다
- transition condition 자체보다 readable explanation이 우선된다

resulting bias:

- same family projection shift first:
  `proj_transition_operator_readout`
- if root shifts:
  `fam_operator_readout`
  `proj_operator_board_readout`
  `route_readonly_board`

### 3. presentation_before_narrow_search

source family:

- `fam_operator_readout`

의미:

- broad board를 먼저 보고,
  narrow search는 그 다음에 열어라

next family bias:

- same family:
  `proj_operator_board_readout`
  or `proj_operator_search_readout`

reentry 조건:

- explicit query appears
- broad overview is already present but insufficient

resulting bias:

- `operator_family_narrow_query_request`
- `proj_operator_search_readout`
- `route_internal_search`

## reentry evaluation order

v0에서는 아래 순서로 본다.

1. new source artifact
2. saved source-to-family hint
3. previous residue bias
4. family-rooted alias
5. signal_kind
6. classifier

즉 residue는
source hint 다음,
alias/signal 이전 정도의 strength로 두는 것이 맞다.

## builder_choi -> transition 예시

previous residue:

- `preservation_before_flattening`

new source:

- [runtime/current_phase.json](/Users/sungsookim/universe/vectorfl_replica/runtime/current_phase.json)

question shift:

- `어떻게 넣을까` -> `왜 closure-ready가 아닌가`

reentry bias:

- `fam_transition_thickening`
- `proj_transition_preflight_reread`
- `route_preflight_reread`

즉 이 예시는
source artifact만이 아니라
이전 residue가 next family bias를 강화하는 첫 reentry case다.

## current limit

v0에서는 아직
residue가 따로 저장된 runtime reentry registry는 없다.

지금은

- hint manifest
- handoff case
- reasoning policy

수준으로만 잠갔다.

## 한 줄 요약

residue-backed reentry rule v0는
과거 residue가 새 artifact와 question shift를 만났을 때
다음 family/projection/route bias를 강화하는 최소 재진입 규칙이다.
