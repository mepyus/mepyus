# multi_lens_document_reading_v0 minimum implementation package spec

## verdict

- `multi_lens_document_reading_v0` minimum implementation package is locked as a spec asset
- this package plan translates the already locked architecture into a minimal implementation scope
- this turn does not reopen heuristic tuning, maturity interpretation, or operating-state debate

## minimum code assets required for v0

v0에서 필요한 최소 code asset은 아래로 한정한다.

- `app/core/runtime/multi_lens_document_reading.py`
- `app/core/runtime/context_linked_segmentation.py`
- `runtime/manifests/line_registry.json`
- `scripts/run_multi_lens_document_reading_probe.py`
- `scripts/run_multi_lens_document_reading_strength_validation.py`

보조 문서 asset:

- `docs/specs/multi_lens_document_reading_v0_contract_spec.md`
- `docs/specs/multi_lens_document_reading_v0_readout_contract_note.md`
- `docs/specs/multi_lens_document_reading_v0_architecture_and_operating_state_spec.md`
- `docs/specs/multi_lens_document_reading_v0_runtime_placement_and_boundary_spec.md`
- `docs/specs/multi_lens_document_reading_v0_invocation_and_flow_integration_spec.md`

## responsibility of each asset

### `app/core/runtime/multi_lens_document_reading.py`

책임:

- `LinkedSegment` 입력 받기
- runtime line registry 읽기
- stable/thick lens 적용
- `SegmentLineReading` 생성
- `DocumentLineLensingResult` 생성
- current v0 readout을 runtime observation output으로 반환

하지 않는 일:

- operating state 변경
- maturity 판단
- parked axis reopen

### `app/core/runtime/context_linked_segmentation.py`

책임:

- `LinkedSegment` surface를 upstream에서 제공
- `multi_lens_document_reading_v0`의 최소 입력을 보장

하지 않는 일:

- multi-lens 결과 해석
- line-level operating decision

### `runtime/manifests/line_registry.json`

책임:

- line source of truth 제공
- line identity, status, thickness metadata 제공
- stable/thick vs candidate/thin 구분 근거 제공

하지 않는 일:

- runtime readout scoring
- operating decision 자동화

### `scripts/run_multi_lens_document_reading_probe.py`

책임:

- self-contained probe 실행
- minimal runtime path 점검
- linked segment 입력에서 readout 생성 확인

### `scripts/run_multi_lens_document_reading_strength_validation.py`

책임:

- current fixture 기준의 observation output 수집
- strength 분포와 bias를 관찰용으로 기록
- regression-like observation reference 제공

## initial implementation scope

### what is in v0 now

현재 v0 범위 안에 들어 있는 것:

- `LinkedSegment` 기반 invocation
- stable/thick lens actual application
- candidate/thin lens metadata-only treatment
- per-segment `SegmentLineReading`
- document-level `DocumentLineLensingResult`
- `reading_strength` starter heuristic
- `reading_basis` explanation string
- probe / strength validation script
- parked axis and active axis를 분리해서 읽는 operator guidance

### what should be implemented first

최초 concrete package는 아래 순서로 충분하다.

1. `LinkedSegment -> MultiLensDocumentReader.read()` 연결
2. line registry 로드
3. stable/thick lens 적용
4. `SegmentLineReading` 반환
5. `DocumentLineLensingResult` 반환
6. probe와 validation으로 current output 확인

의미:

- v0의 first package는 "읽고 보여주는 최소 runtime path"까지만 구현하면 된다
- operating decision이나 maturity 해석은 첫 패키지에 포함하지 않는다

## deferred scope

아래는 명시적으로 v0 minimum package 밖에 둔다.

- candidate promotion
- auto state transition
- scoring
- maturity decision
- reopen automation
- candidate/thin actual application expansion
- document-level verdict layer
- hidden ranking layer

deferred 원칙:

- current readout이 존재한다고 해서 위 기능을 암묵적으로 여는 것으로 해석하면 안 된다
- deferred scope는 docs/governance lock 없이 runtime으로 들어가면 안 된다

## integration order

### what gets connected first

먼저 연결할 것:

1. `context_linked_segmentation_v0` output
2. `multi_lens_document_reading_v0` runtime invocation
3. stable/thick line registry loading
4. per-segment readout generation
5. surfaced readout for operator visibility

### what remains document/supervisor-side

문서/운영 쪽에 남겨둘 것:

- active / parked / candidate state governance
- parked axis reopen gate
- evaluation asset sufficiency 판단
- operator interpretation rule lock
- future patch gate
- maturity/anchor/agent-level 해석

원칙:

- integration은 runtime readout까지만 먼저 연결한다
- 운영 판단은 docs/supervisor-side에서 계속 분리한다

## guardrails

### execution/readout/decision separation

- execution은 `reading_strength`와 `reading_basis`를 만든다
- readout은 그것을 operator가 읽을 수 있게 드러낸다
- decision은 runtime 밖에 남긴다

이 셋을 섞으면 안 된다.

### parked axis handling

- parked axis는 output에 나타날 수 있다
- parked axis는 tuning priority가 아니다
- parked axis의 `absent/weak`를 failure나 reopen signal로 읽지 않는다
- 현재 `transition_over_surface`는 이 규칙을 따른다

### runtime stops before operating decision

- runtime 책임은 readout 생성에서 끝난다
- operating decision은 supervisor/docs/operating loop가 맡는다
- output pattern alone으로 promotion, reopen, maturity claim을 만들면 안 된다

## technical summary

- v0 minimum package는 `multi_lens_document_reading.py` 중심의 observation runtime path다
- 필요한 자산은 upstream linked segment provider, line registry, probe/validation script 정도로 한정된다
- first package는 stable/thick lens readout까지 연결하면 충분하다
- candidate promotion, scoring, maturity decision, reopen automation은 deferred scope로 fence off 한다
- execution/readout/decision 분리와 parked-axis handling이 핵심 guardrail이다

## user-language summary

- 지금 당장 구현해야 하는 최소 묶음은 복잡하지 않다
- 문맥 연결이 끝난 segment를 받아서, stable/thick line으로 읽고, 그 결과를 보여주는 데까지만 연결하면 된다
- 그 다음에 "이 line을 올릴까", "state를 바꿀까", "점수를 만들까" 같은 일은 지금 패키지에 넣지 않는다
- 특히 `transition_over_surface` 같은 parked 축은 결과에 보일 수는 있어도, 지금 구현 패키지의 조정 대상이 아니다

## close-out

- future supervisor는 이 spec만 보고 첫 concrete implementation package를 할당할 수 있다
- minimum code assets와 책임은 여기서 고정된다
- deferred scope는 architecture debate 없이 fence off 된 상태로 유지한다
