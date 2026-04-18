# multi_lens_document_reading_v0 runtime placement and boundary spec

## verdict

- `multi_lens_document_reading_v0` runtime placement and boundary model is locked as a spec asset
- this turn does not change runtime code, heuristic scope, or operating state
- this spec defines where the module lives, what each layer owns, and what boundaries must not be crossed

## runtime placement

### why it belongs in runtime

`multi_lens_document_reading_v0`는 입력 `LinkedSegment`를 받아 현재 line lens를 적용하고 per-segment readout을 생성하는 실행 모듈이므로 runtime에 속한다.

runtime에 두는 이유:

- 입력 surface를 실제로 읽는 실행 단계이기 때문이다
- line registry를 읽어 현재 적용 가능한 stable/thick lens를 불러오기 때문이다
- `SegmentLineReading`과 `DocumentLineLensingResult`를 산출하는 operational pass이기 때문이다

### what it may read

이 모듈은 runtime에서 아래를 읽을 수 있다.

- `context_linked_segmentation_v0`의 `LinkedSegment` 출력
- `runtime/manifests/line_registry.json`
- 현재 runtime pass에 필요한 provenance 정보
- stable/thick lens 기준의 local keyword/seed map

### what it must not decide

이 모듈은 아래를 결정하면 안 된다.

- line maturity verdict
- operating anchor 승격 여부
- agent station readiness
- document-level 최종 line verdict
- parked / active / candidate state promotion
- evidence sufficiency gate 통과 여부

즉 runtime은 readout을 생성할 수는 있지만, governance decision을 대신하면 안 된다.

## ownership by layer

### line definition ownership

owner:

- spec/docs layer
- line registry governance

owns:

- line identity
- line name
- line-side metadata
- stable/thick/candidate 분류 기준
- active / parked / candidate operating-state definition
- evaluation asset requirement definition

does not own:

- 실제 `reading_strength` 산출
- runtime readout formatting

### reading execution ownership

owner:

- `app/core/runtime/multi_lens_document_reading.py`

owns:

- lens application
- seed/keyword match
- partial match handling
- `reading_strength` 산출
- `reading_basis` 생성
- per-segment line reading object 생성

does not own:

- operating state promotion
- parked-axis reopen decision
- document-level maturity interpretation

### result surface ownership

owner:

- readout contract / surface spec
- runtime output schema

owns:

- `SegmentLineReading` field surface
- `DocumentLineLensingResult` field surface
- per-segment readout shape
- operator-facing interpretation guidance
- parked axis / active axis labeling rule

does not own:

- heuristic tuning
- operating decision
- maturity judgment

### operating decision ownership

owner:

- spec/docs governance layer
- supervisor/operator decision layer

owns:

- active / parked / candidate state assignment
- reopen gate
- evaluation asset sufficiency 판단
- patch opening or stopping decision

does not own:

- runtime readout generation
- seed matching implementation

## boundary rules

### execution must not become decision logic

- runtime execution은 `reading_strength`와 `reading_basis`를 만들 수 있다
- 그러나 그 결과를 근거로 line을 active/promoted state로 올리면 안 된다
- execution은 parked axis를 직접 reopen할 수 없다

### result surface must not become maturity judgment

- readout surface는 operator가 현재 출력을 읽는 창이다
- `strong / weak / absent`를 maturity score처럼 재해석하면 안 된다
- `DocumentLineLensingResult`는 variation readout이지 maturity ledger가 아니다

### operating state must not be inferred directly from reading result

- `strong`이 나와도 active/promoted 의미가 아니다
- `weak`가 나와도 candidate 보강 근거가 아니다
- `absent`가 나와도 parked 또는 failed 의미가 아니다
- operating state는 별도 governance decision으로만 바뀐다

## parked-axis handling in code structure

`parked`는 tuning target이 아니라 governance state다.

코드 구조 원칙:

- parked axis는 runtime output에 등장할 수 있다
- parked axis 결과가 `absent` 또는 `weak`여도 자동 실패 처리하지 않는다
- parked axis는 current runtime tuning의 우선 대상이 아니다
- parked axis patch는 evidence-bearing evaluation asset gate를 통과한 뒤에만 열린다

현재 예:

- `line_transition_over_surface`

운영 원칙:

- parked axis가 output에 보이는 것과 parked axis를 runtime 개선 대상으로 삼는 것은 다르다
- output presence는 허용되지만, tuning priority는 gate decision이 따로 정한다

## future extension rules

### changes that belong to docs first

아래 변화는 구현 전에 docs/spec에서 먼저 잠가야 한다.

- operating state 변경
- parked axis reopen
- evaluation asset sufficiency 기준 변경
- readout interpretation rule 변경
- new line을 active observation axis로 올리는 제안
- maturity claim이나 score에 가까운 해석 추가

### changes that may enter runtime

아래 변화는 gate가 잠긴 뒤 runtime patch로 들어갈 수 있다.

- stable/thick active axis의 bounded seed refinement
- `reading_basis` 문장 개선
- per-segment readout 생성 보강
- spec으로 먼저 잠긴 partial-match/termination 규칙 반영

runtime에 바로 들어가면 안 되는 변화:

- parked axis를 direct evidence 없이 확장하는 heuristic patch
- candidate/thin lens 실제 적용 확대
- global scoring layer 추가
- document-level maturity layer 추가

## non-goals

- no runtime patch
- no heuristic expansion
- no state promotion
- no new scoring layer
- no candidate/thin promotion
- no document-level maturity claim

## technical summary

- `multi_lens_document_reading_v0`는 runtime에 두되, runtime은 observation execution까지만 소유한다
- line definition과 operating decision은 docs/governance가 소유한다
- result surface는 output schema와 operator guidance를 소유하지만 maturity judgment를 소유하지 않는다
- execution, surface, decision을 섞지 않아야 parked axis와 active axis를 안정적으로 운영할 수 있다

## user-language summary

- 이 모듈은 runtime 안에 있지만, 할 수 있는 일은 "읽어서 보여주기"까지다
- 어떤 line을 세워 둘지, 다시 열지, 올릴지는 runtime이 아니라 운영 기준이 정한다
- 그래서 `strong`이 나와도 자동 승격이 아니고, `absent`가 나와도 자동 실패가 아니다
- 앞으로 누가 수정안을 내더라도 먼저 그게 docs에서 잠글 문제인지, runtime에서 구현할 문제인지부터 나눠야 한다

## close-out

- future supervisor는 제안된 변경이 line definition, reading execution, result surface, operating decision 중 어디에 속하는지 먼저 판정해야 한다
- `multi_lens_document_reading_v0`는 execution / surface / decision blending 없이 observation runtime으로만 유지한다
