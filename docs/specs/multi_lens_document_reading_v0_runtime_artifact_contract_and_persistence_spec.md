# multi_lens_document_reading_v0 runtime artifact contract and persistence spec

## verdict

- `multi_lens_document_reading_v0` runtime artifact contract is locked as a spec asset
- this spec defines the official artifact fields, their roles, and persistence boundaries
- this turn does not change runtime code, heuristic scope, or operating-state behavior

## official artifact fields

official runtime artifact는 아래 top-level fields를 포함한다.

- `kind`
- `source_id`
- `observer_run_id`
- `split_units_path`
- `invocation_stage`
- `linked_segments`
- `raw_reading_result`
- `surfaced_readout`
- `parked_axes`
- `handoff_boundary`

이 중 핵심 contract fields는 아래 다섯 개다.

- `linked_segments`
- `raw_reading_result`
- `surfaced_readout`
- `parked_axes`
- `handoff_boundary`

## field roles

### observational fields

아래는 observational record다.

- `linked_segments`
- `raw_reading_result`

의미:

- upstream segmentation 이후 어떤 surface가 들어왔는지 보여준다
- runtime이 line lens를 적용해 어떤 raw reading rows를 만들었는지 보여준다
- 이 필드들은 observation trace이지 decision trace가 아니다

### surfaced / operator-facing fields

아래는 operator-facing surface다.

- `surfaced_readout`
- `parked_axes`

의미:

- operator가 현재 run에서 어떤 line이 active/parked 상태로 보이는지 읽을 수 있게 한다
- `surfaced_readout`는 per-segment readout을 readable하게 보여준다
- `parked_axes`는 parked line을 명시적으로 드러내 overclaim을 막는다

### handoff metadata fields

아래는 handoff metadata다.

- `handoff_boundary`
- `invocation_stage`
- `observer_run_id`
- `split_units_path`

의미:

- runtime responsibility가 어디서 끝나는지 기록한다
- artifact가 어떤 stage에서 생성되었는지 기록한다
- 다음 owner가 runtime 밖이라는 점을 남긴다

## official field semantics

### `linked_segments`

- `context_linked_segmentation_v0` output snapshot
- multi-lens observation pass가 실제로 무엇을 입력으로 받았는지 기록한다
- maturity evidence ledger가 아니다

### `raw_reading_result`

- runtime execution이 직접 만든 raw result
- `DocumentLineLensingResult`와 그 내부 `SegmentLineReading` collection을 담는다
- operator explanation 이전의 execution output이다

### `surfaced_readout`

- operator-facing readout
- per-segment, per-line row를 readable surface로 남긴다
- surfaced output은 still observational이며 decision output이 아니다

### `parked_axes`

- current run에서 parked operating-state로 다뤄지는 line id 목록
- parked axis의 현재 해석 경계를 명시하는 표식이다
- parked axis가 output에 보인다는 사실은 failure나 reopen 신호가 아니다

### `handoff_boundary`

- runtime stops after what
- next owner is who
- whether decision logic was performed in runtime

최소 의미:

- runtime은 readout에서 멈춘다
- 다음 단계는 supervisor/docs/operating loop가 맡는다
- output pattern alone으로 decision이 내려지지 않았음을 보장한다

## persistence rules

### what may be persisted

아래는 runtime artifact로 persist해도 된다.

- `linked_segments`
- `raw_reading_result`
- `surfaced_readout`
- `parked_axes`
- `handoff_boundary`
- `observer_run_id`
- `source_id`
- provenance-like invocation metadata

persist 이유:

- audit trail
- reproducible observation review
- operator-facing inspection
- supervisor handoff

### what remains observational only

아래는 artifact에 남더라도 observational only로 다뤄야 한다.

- `strong / weak / absent` 패턴의 의미 해석
- parked axis의 현재 absence/weakness 해석
- line importance ranking
- document-level final line verdict
- maturity or promotion implication

원칙:

- persisted 되었다고 해서 governance legitimacy가 생기는 것은 아니다
- persistence는 저장 허용이지 decision 승인 의미가 아니다

## interpretation guardrails

- 이 artifact는 maturity record가 아니다
- 이 artifact는 decision record가 아니다
- parked-axis `absent`는 failure가 아니다
- parked-axis `weak`는 reopen 근거가 아니다
- `strong`은 current heuristic observation일 뿐이며 promotion 의미가 아니다
- `raw_reading_result`와 `surfaced_readout`를 합쳐도 operating decision이 되지 않는다

## future extension fences

- no scoring
- no auto decision
- no reopen from output pattern alone
- no hidden rank field
- no maturity summary field
- no candidate/thin promotion via artifact growth

확장 원칙:

- 새 field가 operator explanation을 넘어 decision semantics를 담기 시작하면 docs/spec에서 먼저 잠가야 한다
- artifact 확장은 observation trace와 handoff metadata 범위 안에서만 허용한다

## review rule for future supervisors

future supervisor는 artifact를 볼 때 아래 순서로 확인한다.

1. 이것이 observation artifact인지 확인한다
2. `linked_segments -> raw_reading_result -> surfaced_readout` 흐름이 유지되는지 확인한다
3. `parked_axes`와 `handoff_boundary`가 명시되어 있는지 확인한다
4. payload 안에 maturity, promotion, reopen 의미가 섞이지 않았는지 확인한다

## technical summary

- official artifact는 segmentation snapshot, raw reading result, surfaced readout, parked-axis marker, handoff metadata를 함께 담는다
- persist는 허용되지만 semantics는 observational로 제한된다
- artifact는 maturity record나 decision record로 확장되면 안 된다
- parked-axis absence는 failure가 아니며, output pattern alone으로 reopen할 수 없다

## user-language summary

- 이 artifact는 "기계가 이번에 어떻게 읽었는지"를 남기는 기록이다
- "그래서 이 line을 올릴지 말지 결정했다"는 기록이 아니다
- `transition_over_surface` 같은 parked 축이 `absent`로 나와도, 그건 지금 시험 재료가 부족한 상태를 보여줄 수 있을 뿐 실패 판정은 아니다
- 앞으로도 이 파일은 관찰 기록과 handoff 메모까지만 담아야 하고, 점수나 자동 판단이 들어오면 안 된다

## close-out

- future supervisor는 이 spec만 보고 multi-lens runtime artifact가 무엇인지, 무엇이 아닌지, 어떻게 persist할 수 있는지 판정할 수 있다
- official field set과 semantics는 여기서 고정된다
- artifact drift와 overclaim은 이 경계 안에서 막는다
