# multi_lens_document_reading_v0 invocation and flow integration spec

## verdict

- `multi_lens_document_reading_v0` invocation and flow integration model is locked as a spec asset
- this turn does not change runtime code, output schema, or operating state
- this spec defines where the module is invoked, how inputs/outputs move, and where runtime responsibility ends

## invocation point in the broader engine flow

`multi_lens_document_reading_v0`는 broader engine flow에서 `context_linked_segmentation_v0` 다음에 호출된다.

최소 흐름:

1. raw input enters the engine
2. segmentation produces ordered `Segment` units
3. `context_linked_segmentation_v0` produces ordered `LinkedSegment` units
4. `multi_lens_document_reading_v0` reads those `LinkedSegment` units through current stable/thick lenses
5. runtime emits per-segment reading results and readable surface output
6. supervisor/docs/operating loop interprets whether anything should be changed later

호출 위치 원칙:

- `multi_lens_document_reading_v0`는 linked segment surface가 준비된 뒤에만 호출한다
- raw document나 unlinked shard에 바로 적용하지 않는다
- document verdict 단계로 가는 모듈이 아니라 variation readout 단계에 위치한다

## minimum input contract

runtime invocation에 필요한 최소 입력은 ordered `LinkedSegment` list다.

필수 필드:

- `linked_segment_id`
- `source_id`
- `segment_ids`
- `linked_text`
- `linkage_reason`
- `linkage_confidence`
- `provenance`

추가 runtime requirement:

- 입력은 같은 `source_id` 기준으로 정렬되어 있어야 한다
- input batch 안에서 `linked_segment_id`는 유일해야 한다
- runtime은 line lens source로 `runtime/manifests/line_registry.json`을 읽을 수 있어야 한다
- current v0에서는 stable/thick lens만 actual reading 대상으로 사용한다

입력 전제:

- `LinkedSegment`는 이미 의미 연결 복원 단계를 통과한 surface여야 한다
- segmentation quality나 linkage governance는 이 모듈 안에서 다시 결정하지 않는다

## output routing

### raw reading result

runtime이 직접 산출하는 1차 결과는 아래다.

- `SegmentLineReading` collection
- `DocumentLineLensingResult`

이 결과는 runtime의 raw observation output이다.

### surfaced readout

operator에게 보이는 surfaced readout은 raw reading result를 그대로 또는 얕게 정리한 surface다.

최소 surface:

- document-level
  - `source_id`
  - `lens_ids_used`
  - `is_stable_lens_only`
- per-reading
  - `linked_segment_id`
  - `line_id`
  - `line_name`
  - `reading_strength`
  - `reading_basis`
  - `caution_reason`
  - `provenance`

readout 원칙:

- surfaced readout은 operator-readable observation이어야 한다
- current output을 maturity ledger나 operating-state ledger로 바꾸면 안 된다

### what may be persisted vs what should remain observational

persist 가능:

- raw `SegmentLineReading` rows
- `DocumentLineLensingResult`
- provenance
- parked axis / active axis annotation metadata

observation-only로 남겨야 하는 것:

- current `strong / weak / absent` 패턴에 대한 maturity 해석
- output만 보고 만든 승격 판단
- parked axis reopen 해석
- document-level final verdict

원칙:

- persistence는 history/audit을 위한 것이다
- persistence가 곧 decision legitimacy를 뜻하지는 않는다

## operator visibility rules

operator는 아래를 볼 수 있어야 한다.

- 어떤 linked segment에서 어떤 line이 읽혔는가
- `reading_strength`가 왜 그렇게 나왔는가
- 어떤 line이 active axis이고 어떤 line이 parked axis인가
- current run이 stable/thick only readout인지

operator는 아래를 보면 안 된다.

- hidden global score
- implicit maturity rank
- output pattern만으로 계산된 state promotion
- parked axis를 실패처럼 암시하는 화면

가시성 원칙:

- readout은 설명 가능해야 한다
- `reading_basis` 없는 non-absent 결과는 operator-facing surface에서 신뢰 가능한 readout으로 보이면 안 된다

## decision handoff boundary

### where runtime stops

runtime responsibility는 아래에서 끝난다.

- ordered `LinkedSegment`를 읽는다
- line별 `SegmentLineReading`을 만든다
- `DocumentLineLensingResult`를 반환한다
- current observation surface를 남긴다

runtime이 여기서 넘어가면 안 되는 것:

- line operating state 변경
- parked axis reopen
- candidate promotion
- document-level maturity claim
- output pattern만으로 운영 결정을 내리는 것

### where supervisor/docs/operating loop takes over

아래는 supervisor/docs/operating loop가 맡는다.

- output 해석의 governance
- parked axis 유지 또는 reopen 여부 판단
- evaluation asset sufficiency 판단
- future patch gate 설정
- spec 변경 또는 lock

핸드오프 원칙:

- runtime output은 decision input일 수는 있다
- 그러나 decision authority는 runtime 밖에 있다

## parked-axis flow handling

parked axis는 output flow 안에는 존재할 수 있지만, decision flow의 자동 트리거가 아니다.

현재 원칙:

- parked axis는 current readout에 row로 나타날 수 있다
- parked axis의 `absent`는 failure로 처리하지 않는다
- parked axis의 `weak`는 reopen signal이 아니다
- parked axis는 evidence-bearing evaluation asset gate를 통과하기 전까지 tuning target이 아니다

현재 예:

- `line_transition_over_surface`

flow separation:

- output flow에 등장하는 것
- operating loop에서 다시 여는 것

이 둘은 분리한다.

## non-goals

- no auto promotion
- no automatic state transition
- no maturity decision
- no reopen from output pattern alone
- no hidden decision engine
- no heuristic expansion in this turn

## technical summary

- `multi_lens_document_reading_v0`는 `context_linked_segmentation_v0` 다음에 호출되는 runtime observation pass다
- 입력은 ordered `LinkedSegment`와 current line registry다
- 출력은 raw reading result와 surfaced readout으로 이동하지만, decision authority는 runtime 밖에 남긴다
- parked axis는 output에 나타날 수 있으나, output pattern만으로 reopen하지 않는다
- 이 handoff boundary를 유지해야 module이 hidden decision engine으로 drift하지 않는다

## user-language summary

- 이 모듈은 문서 조각을 line lens로 읽어 결과를 보여주는 단계에서 불린다
- 여기서 하는 일은 "읽어서 보여주기"까지고, "그래서 이 line을 올릴지 말지 결정하기"는 여기서 하지 않는다
- `transition_over_surface` 같은 parked 축도 결과에는 보일 수 있지만, 그걸 보고 자동으로 다시 여는 일은 없다
- 앞으로 누가 이 모듈을 건드리려면, 먼저 그 변경이 runtime readout의 일인지, 운영 판단의 일인지 구분해야 한다

## close-out

- future supervisor는 `multi_lens_document_reading_v0`를 `context_linked_segmentation_v0` 다음 observation pass로 배치하면 된다
- output movement는 `raw reading result -> surfaced readout -> supervisor/operating loop handoff`로 본다
- runtime은 readout에서 멈추고, decision은 runtime 밖에서만 열린다
