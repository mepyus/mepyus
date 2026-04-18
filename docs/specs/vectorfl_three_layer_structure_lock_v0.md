# VectorFL Three-Layer Structure Lock v0

이 문서는 지금 단계에서 바로 잠글 수 있는 구조만 짧게 고정한다.  
완결 아키텍처를 선언하는 문서가 아니라, 현재 논의에서 반복 확인된 기준선을 잠그는 문서다.

## 1. Locked Core Sentence

현재까지 잠기는 기본 구조는 아래 3층이다.

- `qmd-ref intake layer`
- `VectorFL core layer`
- `paperclip-ref host shell layer`

외부 레퍼런스는 참조 부품이며, canonical 의미체계와 운용 질서는 `VectorFL core`가 가진다.

## 2. Layer Roles

### 2-1. qmd-ref intake layer

- 역할:
  - source registry
  - context attachment
  - 조금 더 큰 intake block 생성
  - structure-aware split
  - graceful fallback
  - context-bearing intake packet 생성
- 핵심 판정:
  - 입력기는 작은 값 생성기가 아니다
  - line/state가 잘 생길 수 있는 전단 재료를 준비하는 `line-aware intake organ`이다

### 2-2. VectorFL core layer

- 역할:
  - 원본 읽기기 또는 그에 준하는 초기 reading
  - 입력기 결과 수용
  - case 구성
  - lane state 유지
  - line/state 생성
  - 라인번역
  - 흐름해석
  - 감독/hold
  - current-reading surface 유지
  - trace/memory 보존
- 핵심 판정:
  - 실제 중심 의미체계는 이 층에 있다
  - current-reading, governance, trace 질서는 core first-class로 유지한다

### 2-3. paperclip-ref host shell layer

- 역할:
  - case queue
  - lane progression
  - current-reading console
  - governance panel
  - trace/history panel
  - programs/connections 화면
- 핵심 판정:
  - Paperclip는 ontology reference가 아니라 shell reference다
  - shell은 core를 operator가 다룰 수 있게 보여주는 상위 운용면이다

## 3. Non-Mixing Rules

### 3-1. qmd에서 core로 가져오지 말 것

- 문서 collection worldview 전체
- 입력을 전부 문서처럼 다루는 습관
- search 제품 ontology를 core ontology로 올리는 방식

### 3-2. Paperclip에서 canonical로 잠그지 말 것

- `company`
- `issue`
- `project`
- `heartbeat`
- `approval / budget` naming

즉 Paperclip는 운용 shell 감각 참조이지, core naming source가 아니다.

### 3-3. VectorFL core에서 계속 유지할 것

- line 중심 구조
- current-reading surface
- governance surface
- trace/memory
- case 기반 운용
- line-only reduction 금지

## 4. Intake Re-Definition Lock

현재 단계에서 입력기의 새 정의는 아래로 잠근다.

`입력기 = line-aware intake organ`

의미:

- source를 등록한다
- source family와 subgroup 문맥을 붙인다
- line/state가 잘 생길 수 있는 block으로 분해한다
- provenance/origin을 유지한다
- weak/fallback/residue를 버리지 않는다
- 후속 lane이 바로 사용할 수 있는 intake packet을 만든다

즉 입력기의 목적은 작은 값 생산이 아니라 `line/state 형성에 유리한 재료 준비`다.

## 5. Minimal Object Ownership Lock

지금 단계에서 층별 대표 객체는 아래처럼 읽는다.

### intake layer objects

- `Source Registry Entry`
- `Intake Block`
- `Intake Packet`
- `Intake Status Record`

### core layer objects

- `Case Record`
- `Lane State Record`
- `Line/State Formation Record`
- `Translation Record`
- `Flow Interpretation Record`
- `Governance Record`
- `Surface Packet`
- `Trace/Memory Record`

### shell layer objects

- `Case Queue Item`
- `Current Reading View Model`
- `Input Detail View Model`
- `Program Connection View Model`

이 잠금은 field schema 확정이 아니라 `어느 층의 소유 객체인가`를 먼저 나누는 잠금이다.

## 6. Base Packet Flow Lock

기본 흐름은 아래처럼 읽는다.

`외부 입력 / 프로그램 이벤트 / 문서 / OCR / 음성`
-> `qmd-ref intake layer`
-> `intake packet`
-> `VectorFL core organ/lane 처리`
-> `current-reading / governance / trace 생성`
-> `paperclip-ref host shell 표시`
-> `필요 시 외부 프로그램 action request / response`

즉:

- 입력기 = 재료 준비
- core = 해석 / 판단 / 중개
- shell = 운용면 표시

## 7. What Is Locked Now

지금 바로 잠기는 것은 아래다.

- 3층 구조
- 층별 역할 분리
- qmd/Paperclip/VectorFL 사이의 non-mixing rules
- 입력기의 새 정의
- 층별 대표 객체 소유 구분
- base packet flow

## 8. What Needs Criteria Before Lock

아래는 바로 field lock으로 내려가지 않고, 먼저 기준이 필요한 항목이다.

- canonical object별 minimum required fields
- intake-to-core lossless handoff 기준
- shell display-only boundary
- governance decision vs governance display boundary

## 9. Final Lock Sentence

현재까지의 기준선은 다음 문장으로 잠근다.

`qmd는 입력기 참조, Paperclip는 shell 참조, 실제 의미체계와 운용 질서는 VectorFL core가 가진다. 다음 단계는 구조 확장보다 객체 계약과 handoff 기준을 잠그는 것이다.`
