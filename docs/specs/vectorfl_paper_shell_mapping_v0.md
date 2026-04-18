# VectorFL Paper Shell Mapping v0

이 문서는 `VectorFL canonical object`를  
`paperclip-ref shell composition` 위에 어떤 view model로 올릴지 최소 매핑표 형태로 잠근다.  
세부 UI 설계 문서가 아니라, 구현 전 점검용 mapping lock 문서다.

## 1. 목적

현재 필요한 것은 다음 두 가지를 한 장에서 보는 것이다.

- VectorFL의 canonical object가 무엇인가
- 그것이 shell에서 어떤 view model / panel / surface로 드러나는가

즉 이 문서는 core object와 shell surface 사이의 최소 대응표를 잠근다.

## 2. Mapping Table

### 2-1. Intake Layer -> Inputs / Intake Shell

- canonical object:
  - `Source Registry Entry`
  - `Intake Block`
  - `Intake Packet`
  - `Intake Status Record`
- shell output:
  - `Input Detail View Model`
- primary shell sections:
  - source header
  - context layer summary
  - intake block summary
  - weakness / fallback card
  - intake status summary
  - linked case preview
- note:
  - shell은 intake 의미를 재판정하지 않고 readable detail로 적응시킨다

### 2-2. Case / Lane -> Cases / Queue Shell

- canonical object:
  - `Case Record`
  - `Lane State Record`
  - `Governance Record`
  - `Surface Packet`
- shell output:
  - `Case Queue Item View Model`
- primary shell sections:
  - case identity
  - lane snapshot
  - governance snapshot
  - current surface preview
  - linked program snapshot
  - trace freshness
- note:
  - queue는 진입면이지 canonical case source가 아니다

### 2-3. Surface / Governance / Trace -> Current Reading Shell

- canonical object:
  - `Case Record`
  - `Lane State Record`
  - `Governance Record`
  - `Surface Packet`
  - `Trace / Memory Record` preview
- shell output:
  - `Current Reading View Model`
- primary shell sections:
  - case header
  - current reading body
  - lane strip
  - governance card
  - trace strip
- note:
  - current-reading은 shell의 중심면이지만, canonical 판단은 계속 core 소유다

### 2-4. Program Links -> Programs / Connections Shell

- canonical object:
  - `Case Record.linked_program_refs`
  - `Lane State Record`의 program 관련 input/output refs
  - 관련 `Governance Record`의 action 제한 정보
- shell output:
  - `Program Connection View Model`
- primary shell sections:
  - linked program list
  - current connection status
  - action request preview
  - governance restriction note
- note:
  - 세부 contract는 아직 별도 문서로 내려가지 않았고, 현재는 mapping 수준만 잠근다

### 2-5. Trace / Memory -> History / Trace Shell

- canonical object:
  - `Trace / Memory Record`
  - `Governance Record.decision_trace_ref`
  - 관련 `Surface Packet.trace_preview_refs`
- shell output:
  - `History / Trace Panel View Model`
- primary shell sections:
  - latest trace list
  - residue notes
  - reentry hints
  - decision trace anchors
- note:
  - history panel은 append-only 성격을 가볍게라도 보여야 하며, UI summary가 trace 사실을 대체하면 안 된다

## 3. Mapping Rules

- shell output은 모두 `view model`이지 canonical object가 아니다
- shell은 canonical object를 보기 좋게 재배열할 수 있지만, 의미와 판정은 바꾸지 않는다
- governance와 weakness는 mapping 과정에서 빠지지 않는다
- trace/history는 preview될 수 있지만, append-only source를 대체하지 않는다

## 4. First Implementation Focus

현재 단계에서 가장 먼저 구현 대상으로 보기 좋은 mapping은 아래다.

1. `Surface / Governance / Trace -> Current Reading Shell`
2. `Intake Layer -> Inputs / Intake Shell`
3. `Case / Lane -> Cases / Queue Shell`

즉 current-reading 중심 구현을 먼저 두고,
input과 queue는 그 주변 진입면으로 붙이는 것이 맞다.

## 5. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Paper shell은 canonical object를 직접 소유하지 않고, intake는 Input Detail, case/lane은 Queue Item, surface/governance/trace는 Current Reading, program link는 Connections, trace/memory는 History panel view model로 적응시키는 mapping 위에서 작동한다.`
