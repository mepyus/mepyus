# operating surface composition rule v0

## 0. 목적

이 문서는 operating surface를 단순 패널 나열 화면이 아니라,
**입력 -> line 상태 점검 -> 관찰 표면 -> handoff 확인 -> close-out / next branch**
의 운영 리듬이 드러나는 화면으로 구성하기 위한 규칙이다.

핵심 목적은 두 가지다.

1. supervisor/operator가 무엇을 어떤 순서로 읽어야 하는지 고정한다.
2. 관찰 panel이 decision/maturity/promotion panel로 미끄러지는 것을 막는다.

## 1. operating surface의 기본 성격

operating surface는 결과 전시판이 아니다.

이 surface는 아래를 함께 보여줘야 한다.

- 지금 읽을 재료가 준비되었는가
- 지금 어떤 line이 active / parked / candidate인가
- line으로 읽었을 때 무엇이 surfaced되었는가
- runtime이 어디서 멈췄는가
- 지금 branch를 닫아야 하는가, 더 가야 하는가

즉 operating surface는
**운영 리듬을 읽는 표면**이어야 한다.

## 2. composition의 기본 원칙

### 원칙 1. 입력/준비 상태가 먼저다
관찰 결과보다 먼저,
지금 읽을 재료가 준비되었는지 보여야 한다.

### 원칙 2. line 상태가 관찰 결과보다 먼저다
readout을 보기 전에,
이 readout이 active axis에서 나왔는지 parked axis가 포함됐는지 먼저 보여야 한다.

### 원칙 3. surfaced readout이 primary다
기본 소비 표면은 explanation-first surfaced view여야 한다.
raw artifact는 secondary reference다.

### 원칙 4. handoff boundary가 항상 같이 보인다
관찰 결과만 단독으로 두면 decision처럼 오해된다.
따라서 handoff_boundary는 observation panel 근처에서 같이 보여야 한다.

### 원칙 5. close-out / next branch 정보가 끝에 있어야 한다
운영 surface는 현재 관찰만 보여주고 끝나면 안 된다.
지금 범위를 닫을 것인지, 다음 branch가 무엇인지도 보여줘야 한다.

## 3. operating surface의 권장 panel 순서

### panel 1. input readiness panel
역할:
- 현재 재료가 읽기 가능한 상태인가를 보여준다

기본 항목:
- source
- split status
- linked status
- receipt / provenance pointer
- observation-ready 여부

질문:
- 지금 이 재료는 이미 읽기 가능한가?

### panel 2. line status panel
역할:
- 어떤 line이 지금 운용 대상인지 먼저 보여준다

기본 항목:
- active lines
- parked lines
- candidate lines
- current non-goal
- reopen gate 여부

질문:
- 지금 이 readout을 만든 line은 어떤 신분인가?

### panel 3. observation readout panel
역할:
- line 기반 관찰 결과를 explanation-first로 보여준다

기본 visible:
- surfaced_readout
- line_states
- parked_axes
- handoff_boundary

secondary / expandable:
- raw_output_reference
- deeper artifact link/reference

질문:
- 이 line으로 읽었을 때 지금 무엇이 보였고 무엇은 아직 안 보이는가?

### panel 4. boundary / interpretation guard panel
역할:
- 현재 표면을 어디까지 읽고 어디서 멈춰야 하는지 명시한다

기본 항목:
- observation only
- not a decision surface
- not a maturity surface
- no promotion signal
- no reopen trigger from display alone

질문:
- 이 표면을 무엇으로 오해하면 안 되는가?

### panel 5. close-out / next branch panel
역할:
- 현재 범위를 닫고 다음 이동을 정하는 panel

기본 항목:
- current scope complete 여부
- what changed
- what did not change
- prohibition
- next branch options

질문:
- 지금 여기서 멈추고 닫아야 하는가?
- 다음에 열 축은 무엇인가?

## 4. supervisor/operator 기본 reading path

operating surface에서 기본 reading path는 아래 순서를 따른다.

### 1단. 재료 준비 상태 확인
먼저 입력이 읽기 가능한 상태인지 본다.

### 2단. line 상태 확인
active / parked / candidate를 먼저 본다.

### 3단. surfaced readout 확인
그 다음 explanation-first readout을 읽는다.

### 4단. handoff boundary 확인
runtime이 decision을 하지 않았음을 확인한다.

### 5단. 필요할 때만 raw/reference로 내려간다
기본 소비는 surfaced_readout 중심이다.

### 6단. close-out / next branch 판단
현재 범위를 닫을지, 다음 축으로 갈지 본다.

즉 reading path는

**readiness -> line state -> surfaced observation -> boundary -> deeper reference -> branch decision**

순서로 고정한다.

## 5. panel 간 관계 규칙

### 규칙 1. observation panel은 line status panel 없이 단독 배치하지 않는다
이유:
- active/parked 문맥이 사라지면 readout이 과장된다.

### 규칙 2. handoff boundary는 observation panel에서 멀리 떼지 않는다
이유:
- readout과 boundary가 분리되면 decision surface처럼 보인다.

### 규칙 3. raw artifact는 기본 노출면으로 올리지 않는다
이유:
- raw는 reference용이지 1차 소비면이 아니다.

### 규칙 4. close-out panel은 항상 마지막에 둔다
이유:
- close-out은 관찰을 읽은 뒤에만 의미를 가진다.

### 규칙 5. parked axis는 항상 visible marker를 가져야 한다
이유:
- parked absent를 failure처럼 읽지 않게 해야 한다.

## 6. explicit overclaim guards

operating surface 전체에서 아래 해석은 금지한다.

- active = maturity
- weak = promotion evidence
- parked absent = failure
- artifact persistence = legitimacy
- observation readout = decision trigger
- surface display = reopen justification

UI wording과 panel label도 이 금지선을 넘지 않아야 한다.

## 7. 현재 `multi_lens`의 배치 규칙

현재 `multi_lens_document_reading_v0`는
operating surface에서 아래 위치를 가진다.

- 위치:
  - observation readout panel
- 기본 표시:
  - surfaced_readout
  - line_states
  - parked_axes
  - handoff_boundary
- secondary:
  - raw_output_reference

현재 해석:
- observation only
- not decision
- not maturity
- not promotion
- transition_over_surface remains parked
- input_to_reading_organ remains active but not maturity evidence

즉 `multi_lens`는
operating surface의 **관찰 패널 대표 사례**
로 취급한다.

## 8. 운영 drift 점검 질문

operating surface를 점검할 때는 아래 질문을 사용한다.

### 입력 쪽 질문
- 지금 재료가 실제로 observation-ready인가?

### line 쪽 질문
- 이 readout이 어떤 operating state line에서 나왔는가?

### 표면 쪽 질문
- surfaced_readout이 explanation-first인가?
- decision처럼 보이지 않는가?

### 경계 쪽 질문
- handoff boundary가 충분히 visible한가?

### 종료 쪽 질문
- 지금 이 branch는 닫혀야 하는가?
- 아니면 next bounded package가 필요한가?

## 9. non-goals

이 rule은 아래를 하지 않는다.

- 새로운 runtime heuristic 정의
- panel 내부 scoring 추가
- maturity UI 설계
- decision UI 설계
- promotion signal 설계
- reopen trigger 자동화

즉 이 문서는
**operating surface 구성 질서**
를 다루는 문서이지,
판정 엔진 확장 문서가 아니다.

## 10. 현재 한 줄 결론

operating surface는 단순 결과 나열면이 아니라,
**입력 준비 -> line 상태 -> 관찰 표면 -> 경계 확인 -> close-out / next branch**
의 운영 리듬을 supervisor/operator가 같은 화면에서 안전하게 따라갈 수 있도록
구성되어야 한다.
