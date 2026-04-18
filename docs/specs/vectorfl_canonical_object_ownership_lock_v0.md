# VectorFL Canonical Object Ownership Lock v0

이 문서는 3층 구조, handoff boundary, 필요성 잠금 위에서  
현재 VectorFL이 먼저 canonical로 쥐어야 할 객체와 층별 소유권을 짧게 고정한다.  
field schema 전체를 확정하는 문서가 아니라, `무엇이 어느 층의 주인인가`를 먼저 잠그는 문서다.

## 1. 목적

지금 단계에서 중요한 것은
field를 많이 나열하는 것보다

- 어떤 객체가 canonical object인가
- 그 객체의 주인이 intake인지 core인지 shell인지
- 어디서 결정되고 어디서는 표시만 되는가

를 먼저 잠그는 것이다.

## 2. Ownership Rule

기본 원칙은 아래처럼 잠근다.

- `intake layer`는 source, context, split, packet의 주인이다
- `core layer`는 case, lane, interpretation, governance, surface, trace의 주인이다
- `shell layer`는 canonical object의 주인이 아니라, core object를 operator-facing view model로 적응시키는 층이다

즉:

- intake는 재료를 준비한다
- core는 의미와 판단을 만든다
- shell은 운용면으로 보이게 한다

## 3. Intake-Layer Canonical Objects

### 3-1. Source Registry Entry

- owner: `qmd-ref intake layer`
- role: 입력 원천과 source family를 등록하고 식별한다
- must carry:
  - source identity
  - source locator
  - source family / subgroup
  - default context anchor
  - update / trust 관련 기본 상태
- must not be collapsed into:
  - case object
  - shell view row

### 3-2. Intake Block

- owner: `qmd-ref intake layer`
- role: line/state가 잘 생길 수 있도록 조금 더 큰 관찰 단위를 준비한다
- must carry:
  - structure-aware split 결과
  - overlap / protected region 흔적
  - provenance/origin 연결
  - split reason 또는 약한 이유
- must not be treated as:
  - final line
  - final surface summary

### 3-3. Intake Packet

- owner: `qmd-ref intake layer`
- role: 후속 lane이 바로 사용할 수 있는 context-bearing contract
- must carry:
  - source ref
  - context layers
  - classification
  - block refs
  - weakness / fallback
  - receipt / provenance
  - next lane hint
- handoff note:
  - core로 넘어갈 때 lossless handoff의 기준 객체가 된다

### 3-4. Intake Status Record

- owner: `qmd-ref intake layer`
- role: 입력 건강도와 fallback 상태를 visible하게 유지한다
- must carry:
  - registered / attached / split / fallback / readiness 상태
- must not decide:
  - canonical lane progression
  - governance release

## 4. Core-Layer Canonical Objects

### 4-1. Case Record

- owner: `VectorFL core layer`
- role: intake material과 후속 해석/운용을 묶는 중심 사례 단위
- must carry:
  - origin packet refs
  - current lane
  - linked programs
  - current governance state
  - current surface ref
  - trace refs
- must not be reduced to:
  - raw queue row only
  - intake source only

### 4-2. Lane State Record

- owner: `VectorFL core layer`
- role: case 내부 진행 상태와 현재 lane 결과/보류를 유지한다
- must carry:
  - lane kind
  - status
  - input refs
  - current outputs
  - next hop candidates
  - hold related state
- note:
  - lane progression은 shell에 보일 수 있지만, canonical lane state는 core 소유다

### 4-3. Governance Record

- owner: `VectorFL core layer`
- role: hold, observer-only, promotion 금지, mixed corridor, release condition을 canonical하게 유지한다
- must carry:
  - restriction state
  - reason
  - release condition
  - next check trigger
  - decision trace ref
- must not be owned by:
  - shell badge layer

### 4-4. Surface Packet

- owner: `VectorFL core layer`
- role: current-reading에 올릴 canonical surface payload를 형성한다
- must carry:
  - case anchor
  - current reading summary
  - supporting units
  - governance badges or refs
  - trace preview refs
- note:
  - shell은 이 packet을 표시용 view model로 적응시킨다

### 4-5. Trace / Memory Record

- owner: `VectorFL core layer`
- role: append-only event/history/residue/reentry 단서를 남긴다
- must carry:
  - event/history summary
  - origin ref
  - residue note
  - reentry hint
  - created/observed timing
- note:
  - broad cleanup보다 retention이 우선된다

## 5. Shell-Layer Non-Canonical Objects

shell은 현재 단계에서 아래 객체를 가질 수 있지만,
이것들은 canonical object가 아니라 display/adaptation object로 읽는다.

### 5-1. Case Queue Item

- owner: `paperclip-ref host shell layer`
- role: 여러 case를 queue 형태로 보여주는 row/view model
- source of truth: `Case Record`

### 5-2. Current Reading View Model

- owner: `paperclip-ref host shell layer`
- role: current-reading surface를 operator-facing console로 적응
- source of truth: `Surface Packet`

### 5-3. Input Detail View Model

- owner: `paperclip-ref host shell layer`
- role: intake source/context/block/status를 operator가 읽기 쉽게 보여줌
- source of truth: `Source Registry Entry`, `Intake Packet`, `Intake Status Record`

### 5-4. Program Connection View Model

- owner: `paperclip-ref host shell layer`
- role: 외부 프로그램과 case/lane의 연결 상태를 보여줌
- source of truth: `Case Record`, `Lane State Record`, 관련 program status refs

## 6. Non-Mixing Object Rules

현재 단계에서 아래 혼합은 금지 기준으로 읽는다.

- `Source Registry Entry`를 곧바로 `Case Record`로 환원하지 않는다
- `Intake Block`을 곧바로 final `line`이나 final `surface`로 환원하지 않는다
- `Governance Record`를 shell badge 모음으로 대체하지 않는다
- `Surface Packet`을 shell page state와 동일시하지 않는다
- `Trace/Memory Record`를 임시 UI history와 동일시하지 않는다

## 7. What Is Ready To Lock Next

이 ownership 잠금 위에서 다음에 field schema로 내려갈 수 있는 객체는 아래다.

- `Intake Packet`
- `Case Record`
- `Lane State Record`
- `Governance Record`
- `Surface Packet`
- `Trace/Memory Record`

즉 다음 단계의 schema field lock은 이 여섯 객체를 중심으로 내려가면 된다.

## 8. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`입력기 층은 source/context/split/packet의 canonical owner이고, VectorFL core는 case/lane/governance/surface/trace의 canonical owner이며, shell은 이 canonical object를 operator-facing view model로 적응시키는 층이지 의미체계와 판정의 원천이 아니다.`
