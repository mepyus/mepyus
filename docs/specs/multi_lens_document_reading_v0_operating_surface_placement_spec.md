# multi_lens_document_reading_v0_operating_surface_placement_spec

## verdict

- `multi_lens_document_reading_v0` operating-surface placement is locked as a spec asset
- current supervisor surface is placed as an observation-first panel, not a decision panel
- this turn does not change runtime code, UI code, or operating-state semantics

## placement in operating / supervisor surface

### panel / section location

`multi_lens_document_reading_v0` surface는 operating/supervisor UI에서
document processing 결과를 읽는 영역 안의
`observation readout` panel 또는 `line observation` section에 놓는다.

권장 위치:

- document-level processing summary 아래
- decision/action control 영역보다 앞
- raw artifact / audit reference 영역보다 위

즉 배치 순서는 아래가 맞다.

1. document processing context
2. multi-lens observation surface
3. optional raw/reference links
4. separate supervisor decision or follow-up controls, if any exist elsewhere

### why this placement fits current observation-only role

이 위치가 맞는 이유:

- current multi-lens output은 explanation-first readout이기 때문이다
- runtime이 여기서 멈추고, decision authority는 별도 supervisor/docs loop에 남기기 때문이다
- active / parked / handoff 정보를 보여 주되, 그것이 곧 행동 버튼이나 승격 신호가 되면 안 되기 때문이다

## default visible fields

supervisor/operator 기본 화면에서 바로 보여야 하는 필드는 아래다.

- `surfaced_readout`
- `line_states`
- `parked_axes`
- `handoff_boundary`

document-level 기본 표시:

- `source_id`
- `line_states`
- `parked_axes`
- `handoff_boundary`

per-reading 기본 표시:

- `linked_segment_id`
- `line_id`
- `line_name`
- `reading_strength`
- `reading_basis`
- `operating_state`

원칙:

- 기본 화면만으로 active / parked / handoff를 함께 읽을 수 있어야 한다
- 기본 화면만으로도 raw artifact를 열지 않고 현재 observation 의미를 파악할 수 있어야 한다

## secondary / expandable fields

아래는 secondary 또는 expandable로 둔다.

- `raw_output_reference`
- deeper artifact link / observation artifact path
- raw execution-oriented payload
- full provenance internals

표시 원칙:

- raw output은 default open 상태가 아니라 reference link 상태가 맞다
- operator가 deeper audit이 필요할 때만 펼치게 한다
- surfaced panel이 raw artifact dump처럼 보이면 안 된다

## reading order for operators / supervisors

current surface는 아래 순서로 읽게 해야 한다.

1. `line_states`로 active / parked 축을 먼저 확인한다
2. `parked_axes`로 parked line을 다시 확인한다
3. `surfaced_readout`에서 segment별 `reading_strength`와 `reading_basis`를 읽는다
4. `handoff_boundary`로 runtime이 decision 전에 멈췄는지 확인한다
5. 필요할 때만 `raw_output_reference`를 연다

이 순서를 지켜야:

- parked axis를 failure로 오해하지 않고
- weak를 promotion 신호로 오해하지 않고
- surfaced view를 decision panel로 읽지 않게 된다

## explicit overclaim guards in UI wording

UI wording 자체에 아래 guard가 유지되어야 한다.

- observation only
- explanation-first
- not a decision panel
- not a maturity panel
- active is not promotion readiness
- parked absence is not failure
- display alone does not reopen a line

최소 UI copy 방향:

- `current observation`
- `current surfaced readout`
- `runtime handoff complete`
- `raw artifact available as reference`

피해야 할 wording:

- `recommended action`
- `promotion candidate`
- `maturity level`
- `ready for anchor`
- `reopen suggested`

## non-goals

- no decision panel
- no maturity panel
- no promotion signal
- no reopen trigger from display alone
- no scoring display
- no hidden ranking display

## technical summary

- current multi-lens supervisor surface belongs in the observation/readout region of operating UI
- default visible fields are `surfaced_readout`, `line_states`, `parked_axes`, and `handoff_boundary`
- raw artifact access stays secondary/expandable
- operator reading order must preserve active/parked distinction before per-reading interpretation
- UI wording must keep the surface observational and explanation-first

## user-language summary

- 이 화면은 "이번에 어떻게 읽혔는가"를 보여주는 칸에 놓는 게 맞다
- 판단 버튼 옆이나 승격 패널 안에 두면 안 된다
- 기본으로는 surfaced readout과 active/parked, handoff만 보이고, raw 파일은 필요할 때만 열게 해야 한다
- 이 표면은 설명 화면이지 결정 화면이 아니다

## close-out

- future supervisor는 이 spec만 보고 multi-lens surface를 operating UI 어디에 둘지 바로 판단할 수 있다
- placement, default fields, secondary fields, reading order, overclaim guard는 여기서 고정된다
- current surface는 explanation-first observational panel로만 유지한다
