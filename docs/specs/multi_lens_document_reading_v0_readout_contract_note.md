# multi lens document reading v0 readout contract note

## verdict

- `multi_lens_document_reading_v0` readout contract is locked as a spec asset
- this note defines how current outputs should be surfaced and interpreted
- v0 is a readable observation surface, not a maturity engine

## what this note is for

- future supervisor가 현재 multi-lens 출력을 implementation history 없이 바로 읽을 수 있게 한다
- active axis와 parked axis를 분리해서 overclaim을 막는다
- current output을 line maturity verdict가 아니라 per-segment observation readout으로 고정한다

## result surface fields to expose

현재 v0 readout surface는 아래 필드를 노출하면 충분하다.

- document-level
  - `source_id`
  - `lens_ids_used`
  - `is_stable_lens_only`
- per-reading
  - `linked_segment_id`
  - `source_id`
  - `line_id`
  - `line_name`
  - `reading_strength`
  - `reading_basis`
  - `caution_reason`
  - `provenance`

추가 원칙:

- 현재 operator surface는 stable/thick lens 결과를 중심으로 읽는다
- candidate/thin lens는 actual reading distribution 대상이 아니라 metadata로만 남긴다
- `reading_basis` 없는 non-absent 결과는 readout surface에서 유효한 관찰로 취급하지 않는다

## per-segment readout shape

하나의 `linked_segment`는 line별 readout row들로 펼쳐서 읽는다.

최소 readout shape:

- `linked_segment_id`
- `linked_text` 또는 linked segment 참조 정보
- line별 row
  - `line_id`
  - `line_name`
  - `reading_strength`
  - `reading_basis`
  - `caution_reason` if present

운영 원칙:

- 한 segment는 여러 line row를 가질 수 있다
- 한 segment의 readout은 "이 문서의 최종 정답"이 아니라 "이 조각에서 각 line이 어떻게 반응했는가"를 보여준다
- segment 단위 row를 document-level verdict로 합쳐 읽으면 안 된다

## line-level interpretation rules

### strong

- 현재 heuristic 기준에서 해당 line을 지지하는 seed/basis가 보였다는 뜻이다
- stable/thick lens 기준으로 읽을 때, 현재 starter rule에서 비교적 명시적 match가 있었다는 의미다
- 이것만으로 line maturity, line station, operating anchor 승격을 주장하면 안 된다

### weak

- 현재 heuristic 기준에서 partial match, low-confidence downgrade, 또는 제한된 basis가 있었다는 뜻이다
- weak는 line이 "거의 맞다"는 뜻이 아니라, current v0 readout에서 보수적으로 남겨 둔 observation이다
- weak를 strong의 전단계 maturity처럼 읽으면 안 된다

### caution

- v0에서는 최소 사용 원칙을 유지한다
- caution이 있더라도 현재는 heuristic ambiguity 또는 non-primary lens 맥락 정도만 뜻한다
- caution은 maturity 경고판이 아니라 readout 보조 표식이다

### absent

- current heuristic basis에서 relevant seed/basis를 찾지 못했다는 뜻이다
- absent는 의미 부재 증명이 아니다
- 특히 parked axis나 evidence-poor axis에서는 absent가 자연스러운 결과일 수 있다

## parked-axis handling for transition_over_surface

`line_transition_over_surface`는 현재 parked axis로 다룬다.

이유:

- current fixture 안에는 `transition_over_surface` direct textual evidence가 사실상 거의 없다
- weak cue는 일부 있었지만 credible evidence로는 부족했다
- evaluation asset gate는 별도 evidence-bearing asset이 먼저 필요하다고 잠겨 있다

현재 readout에서의 처리 원칙:

- `transition_over_surface` 결과는 active evidence axis처럼 해석하지 않는다
- 현재 `absent`는 heuristic failure 단정이 아니라 parked-axis 상태의 자연스러운 출력일 수 있다
- `weak`가 나오더라도 weak cue 해석 이상으로 확장하지 않는다
- `transition_over_surface`를 근거로 document-level transition claim을 만들면 안 된다

## active-axis handling

현재 active observation axis는 stable/thick lens 중 parked되지 않은 축이다.

운영상 현재는 아래처럼 읽는다.

- `line_input_to_reading_organ`
  - active axis로 읽는다
  - 단, current heuristic output 범위 안에서만 읽는다
  - seed 민감도와 basis 문장을 함께 보고 해석한다

추가 원칙:

- active axis도 maturity engine이 아니다
- active axis에서 `strong`이 나와도 해당 line이 문서 전체를 지배한다고 말하면 안 된다

## operator-reading guidance

### what can be concluded

- 이 segment에서 어떤 stable/thick line이 현재 heuristic 기준으로 반응했는지 볼 수 있다
- `reading_basis`를 통해 왜 `strong / weak / absent`가 나왔는지 추적할 수 있다
- parked axis와 active axis를 구분해 현재 출력의 해석 가능 범위를 알 수 있다
- current fixture에서 어떤 축은 evidence-rich하고 어떤 축은 evidence-poor한지 구분할 수 있다

### what must not be overclaimed

- document 하나의 최종 line verdict를 내리면 안 된다
- `strong`을 line maturity 증명으로 읽으면 안 된다
- `weak`를 성장 중인 line이나 준-확정 line으로 읽으면 안 된다
- `absent`를 의미 부재의 증거로 읽으면 안 된다
- parked axis의 `absent/weak`를 runtime failure로 단정하면 안 된다
- candidate/thin lens를 stable/thick lens와 같은 readout weight로 취급하면 안 된다

## explicit non-goals

- no runtime patch
- no heuristic refinement
- no global score
- no document-level maturity claim
- no candidate/thin promotion
- no aggregation engine expansion
- no line_registry change

## technical summary

- v0 readout은 `SegmentLineReading` collection을 사람이 읽을 수 있는 관찰 surface로 다룬다
- 해석 단위는 per-segment, per-line row다
- active axis와 parked axis를 분리해서 읽어야 한다
- `transition_over_surface`는 parked axis이므로 현재 `absent/weak`를 line failure로 읽지 않는다
- `input_to_reading_organ` 같은 active axis도 heuristic output으로만 읽고, maturity claim으로 올리지 않는다

## user-language summary

- 지금 multi-lens 출력은 "이 조각에서 어떤 line이 어떻게 반응했는지"를 보여주는 읽기 화면이다
- 아직 "이 문서는 결국 이 line이다"라고 판정하는 엔진이 아니다
- `transition_over_surface`는 지금 시험 재료가 부족해서 잠시 세워 둔 축이다
- 그래서 그 축의 `absent`는 고장이라기보다, 아직 제대로 시험할 재료가 없다는 뜻에 가깝다
- 지금 읽을 때는 active axis만 조심스럽게 보고, parked axis는 더 크게 해석하지 않는 것이 맞다

## close-out

- `multi_lens_document_reading_v0`는 현재 readable observation surface로만 운영한다
- parked axis와 active axis를 섞어 maturity claim으로 올리지 않는다
- evidence-bearing evaluation asset이 준비되기 전까지 `transition_over_surface` 축은 parked 상태로 유지한다
