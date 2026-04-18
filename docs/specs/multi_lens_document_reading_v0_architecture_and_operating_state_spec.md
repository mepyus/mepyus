# multi_lens_document_reading_v0 architecture and operating state spec

## verdict

- `multi_lens_document_reading_v0` architecture and operating state model is locked as a spec asset
- this module is an observation engine, not a maturity engine
- this turn does not change runtime code or heuristic scope

## module identity

`multi_lens_document_reading_v0`는 `LinkedSegment`를 받아 line lens별 reading result를 펼쳐 보이는 observation engine이다.

이 모듈의 역할:

- 같은 문서 안의 segment variation을 line별로 드러낸다
- per-segment reading result를 readable surface로 남긴다
- active axis와 parked axis를 구분해 operator가 현재 출력의 해석 범위를 알 수 있게 한다

이 모듈의 역할이 아닌 것:

- line maturity를 판정하는 일
- document 하나를 최종 verdict로 닫는 일
- operating anchor 승격을 결정하는 일
- agent station readiness를 결정하는 일

## four-layer structure

### 1. line definition

이 레이어는 "무슨 line을 lens로 볼 것인가"를 다룬다.

포함 범위:

- line identity
- line name
- line registry source
- status / thickness 같은 line-side metadata
- active / parked / candidate 같은 operating-state annotation

이 레이어에 속하는 변경 예:

- 특정 line을 parked로 전환
- 특정 line의 evaluation asset requirement 정의
- line registry에서 stable/thick line을 primary 대상으로 본다는 정책 명시

### 2. reading execution

이 레이어는 "입력 segment에 lens를 어떻게 적용하는가"를 다룬다.

포함 범위:

- seed/keyword heuristic
- partial match rule
- linkage_confidence 기반 weak downgrade
- per-line reading_strength 산출
- reading_basis 생성

이 레이어에 속하는 변경 예:

- stable/thick lens의 keyword seed refinement
- 특정 line의 partial-match 규칙 조정
- `reading_basis` 문장 형식 조정

### 3. result surface

이 레이어는 "현재 결과를 operator에게 어떻게 드러내는가"를 다룬다.

포함 범위:

- `SegmentLineReading` readout shape
- `DocumentLineLensingResult` surface
- per-segment row display 원칙
- active axis / parked axis 표시
- operator-reading guidance

이 레이어에 속하는 변경 예:

- readout field 추가/정리
- parked axis badge 표기
- `reading_basis`를 surface에서 어떻게 보일지 명시

### 4. operating decision

이 레이어는 "현재 출력 이후 어떤 운영 결정을 허용할 것인가"를 다룬다.

포함 범위:

- 어떤 축을 patch 대상으로 다시 열 수 있는가
- 어떤 line이 parked 상태인지
- reopen gate 조건
- evaluation asset requirement

이 레이어에 속하는 변경 예:

- `transition_over_surface` reopen gate 잠금
- evidence-bearing evaluation asset requirement 승인
- current fixture로는 patch를 열지 않는 운영 결정

## line operating states

### active

- 현재 stable/thick lens로 실제 readout 해석 대상인 line
- operator가 current heuristic output을 observation surface로 읽을 수 있는 축
- active라고 해서 maturity가 높다는 뜻은 아니다

현재 예:

- `line_input_to_reading_organ`

### parked

- 현재 readout에는 존재할 수 있으나, 적극 해석 또는 patch iteration 대상은 아닌 line
- direct evidence 부족, evaluation asset scarcity, 또는 gate decision에 의해 일시 정지된 축
- parked는 failure가 아니라 operating hold 상태다

현재 예:

- `line_transition_over_surface`

운영 원칙:

- parked axis는 evidence-bearing evaluation asset이 준비되기 전까지 reopen하지 않는다

### candidate

- 아직 primary stable/thick observation axis로 올리지 않은 line
- metadata 수준 또는 secondary lens 수준으로만 남는 축
- candidate는 strong/weak 분포 해석의 주대상이 아니다

현재 예:

- `line_pre_read_eye`
- `line_raw_return_preservation`

## separation rule

`reading result != operating state`

이 분리는 반드시 유지한다.

의미:

- `strong`이 나와도 그 line이 active가 되는 것은 아니다
- `absent`가 나와도 그 line이 parked여야 한다는 뜻은 아니다
- parked axis에서 `weak`가 나와도 reopen 근거가 되지 않는다
- candidate line에서 일부 match가 나와도 promotion 근거가 되지 않는다

정리:

- reading result는 execution/output layer의 산물이다
- operating state는 governance/decision layer의 산물이다
- 둘을 섞으면 multi-lens가 maturity engine처럼 오해된다

## transition_over_surface treatment

`line_transition_over_surface`는 현재 parked axis다.

현재 처리 원칙:

- current fixture 안에는 direct textual evidence가 사실상 거의 없다
- weak cue는 일부 있으나 credible evidence로는 부족하다
- current `absent/weak`는 heuristic failure 단정보다 evidence scarcity에 가까운 상태로 읽는다

reopen rule:

- evidence-bearing evaluation asset이 확보되기 전에는 runtime patch를 다시 열지 않는다
- weak cue만으로는 reopen하지 않는다
- positive candidate / negative control / direct evidence 구성이 있어야 다음 evaluation loop를 연다

## supervisor/operator guidance

future change proposal은 아래 질문으로 배치한다.

### this belongs to line definition when

- line status나 state를 바꾸려 한다
- active / parked / candidate 분류를 바꾸려 한다
- 특정 line의 evidence requirement를 잠그려 한다

### this belongs to reading execution when

- keyword seed를 바꾸려 한다
- partial match rule을 바꾸려 한다
- `reading_strength` 산출 규칙을 바꾸려 한다
- `reading_basis` 생성 방식을 바꾸려 한다

### this belongs to result surface when

- operator가 보는 field를 바꾸려 한다
- per-segment readout shape를 바꾸려 한다
- parked axis 표기나 readout guidance를 바꾸려 한다

### this belongs to operating decision when

- 어떤 축을 reopen할지 결정하려 한다
- patch를 열어도 되는지 gate를 판단하려 한다
- evaluation asset sufficiency를 판정하려 한다

## non-goals

- no runtime patch
- no heuristic expansion
- no candidate promotion
- no global scoring
- no document-level maturity claim
- no aggregation engine expansion
- no parked-axis reopening in this turn

## technical summary

- `multi_lens_document_reading_v0`는 observation engine이다
- 구조는 `line definition -> reading execution -> result surface -> operating decision`의 네 레이어로 본다
- `active / parked / candidate`는 operating state이며, reading result와 분리된다
- `transition_over_surface`는 parked axis이고, evidence-bearing evaluation asset 없이는 reopen하지 않는다
- 이 분리를 유지해야 multi-lens v0를 maturity engine으로 오해하지 않는다

## user-language summary

- 이 모듈은 "무슨 line이 얼마나 성숙했는지 판정하는 기계"가 아니다
- 지금은 문서 조각마다 line이 어떻게 반응했는지를 보여주는 관찰 기계다
- 어떤 line은 지금 읽어볼 수 있는 active 축이고, 어떤 line은 재료가 부족해서 잠시 세워 둔 parked 축이다
- `transition_over_surface`는 바로 그런 parked 축이다
- 앞으로 누가 변경을 제안하더라도, 그게 line 정의 문제인지, 읽기 규칙 문제인지, 결과 표면 문제인지, 운영 결정 문제인지 먼저 레이어를 나눠서 봐야 한다

## close-out

- `multi_lens_document_reading_v0`는 현재 observation engine으로만 운영한다
- active / parked / candidate를 reading result와 섞어 해석하지 않는다
- future supervisor는 제안된 변경이 어느 레이어에 속하는지 먼저 판정한 뒤에만 다음 결정을 열면 된다
