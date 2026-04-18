# multi_lens_document_reading_v0_supervisor_reading_surface_spec

## verdict

- `multi_lens_document_reading_v0` supervisor reading surface is locked as a spec asset
- current readout is for safe observation consumption only
- this surface remains observational, not judgmental

## minimum surfaced fields for supervisor/operator consumption

supervisor/operator가 최소로 봐야 하는 surfaced fields는 아래다.

### document-level

- `source_id`
- `lens_ids_used`
- `is_stable_lens_only`
- `line_states`
- `parked_axes`
- `handoff_boundary`

### per-reading

- `linked_segment_id`
- `line_id`
- `line_name`
- `reading_strength`
- `reading_basis`
- `operating_state`
- `is_primary_lens`
- `caution_reason` if present

이 필드 조합이면 operator는:

- 어떤 line이 현재 실제 readout 대상인지
- 어떤 segment에서 어떤 reading이 나왔는지
- 그 이유가 무엇인지
- parked axis가 무엇인지
- runtime이 어디서 멈췄는지

를 읽을 수 있다.

## what stays hidden or secondary

아래는 supervisor main surface에서 hidden 또는 secondary로 둔다.

- full `linked_segments` payload
- full raw provenance internals
- raw execution-oriented bookkeeping
- candidate/thin lens metadata details
- registry-internal details
- any future scoring-like internal helper value

원칙:

- `linked_segments`와 raw artifact는 audit/reference용으로는 남길 수 있다
- 그러나 supervisor first surface는 surfaced readout 중심으로 유지한다
- candidate/thin 관련 정보는 current operator reading 중심축이 아니다

## how active vs parked axes are displayed

active / parked는 surfaced output에서 반드시 구분되어야 한다.

최소 규칙:

- `operating_state=active`
  - current observation axis
- `operating_state=parked`
  - current readout에 나타날 수 있으나 적극 해석하지 않는 axis

표시 원칙:

- `line_states`에서 line별 state를 먼저 보여준다
- per-reading row에서도 `operating_state`를 반복 표시한다
- `parked_axes`를 document-level surface에 별도로 둔다

해석 원칙:

- active는 readout visibility 상태이지 maturity 상태가 아니다
- parked는 failure 상태가 아니라 operating hold 상태다

## how raw vs surfaced outputs are distinguished

raw output과 surfaced output은 반드시 구분한다.

### raw output

- execution trace
- machine-facing or audit-facing layer
- `raw_reading_result`

### surfaced output

- operator-facing reading surface
- explanation-first layer
- `surfaced_readout`

구분 원칙:

- supervisor first view는 surfaced output이다
- raw output은 필요할 때만 reference로 내려간다
- raw와 surfaced가 둘 다 존재해도 surfaced가 decision surface가 되는 것은 아니다

## explicit overclaim guards in the reading surface

reading surface 자체에 아래 경계를 명시적으로 유지해야 한다.

- `strong / weak / absent`는 maturity scale이 아니다
- `active`는 promotion readiness가 아니다
- parked-axis `absent`는 failure가 아니다
- parked-axis `weak`는 reopen trigger가 아니다
- clearer `reading_basis`는 stronger governance claim이 아니다
- surfaced readout은 document-level final verdict를 만들지 않는다

표면상 guard 문장으로 유지해야 할 핵심:

- observation only
- not a decision surface
- not a maturity surface
- handoff occurs after surfaced readout

## non-goals

- no decision surface
- no maturity interpretation
- no promotion signal
- no reopen trigger from readout alone
- no scoring surface
- no hidden ranking layer

## technical summary

- supervisor/operator surface는 surfaced readout 중심으로 구성한다
- minimum fields는 reading explanation, operating state visibility, parked-axis visibility, handoff boundary visibility를 충족해야 한다
- raw output은 secondary reference로 남기고, supervisor first view는 surfaced output으로 제한한다
- active/parked distinction은 보여 주되, 그것을 maturity/promotion semantics로 확장하지 않는다

## user-language summary

- 앞으로 supervisor가 multi-lens 결과를 볼 때는 "어느 segment에서 어떤 line이 어떻게 읽혔는가"만 보면 된다
- `active`와 `parked`는 같이 보여야 하지만, 그걸 보고 바로 승격이나 실패 판단을 하면 안 된다
- raw output은 필요할 때만 참고하고, 기본 읽기 화면은 surfaced readout이면 충분하다
- 이 화면은 판단 화면이 아니라 설명 화면이다

## close-out

- future supervisor는 이 spec만 보고 current multi-lens output을 안전하게 소비할 수 있다
- supervisor reading surface는 여기서 observational surface로 고정된다
- judgment, promotion, maturity, reopen semantics는 이 surface 안으로 들어오지 않는다
