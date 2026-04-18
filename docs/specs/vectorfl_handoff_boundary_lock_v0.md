# VectorFL Handoff Boundary Lock v0

이 문서는 3층 구조 위에서 실제 handoff가 일어날 때
무엇을 잃지 말아야 하는지, 무엇은 core가 결정하고 무엇은 shell이 표시만 해야 하는지를 짧게 잠근다.  
field schema를 확정하는 문서가 아니라, handoff 경계를 먼저 고정하는 문서다.

## 1. 목적

현재 단계에서 먼저 잠가야 할 것은
`무슨 필드가 있나`보다
`층 사이를 건널 때 무엇을 잃으면 안 되는가`와
`누가 결정권을 가지는가`이다.

이 문서는 아래 네 handoff 기준을 잠근다.

- intake -> core lossless handoff
- core -> shell display-only boundary
- governance decision vs display boundary
- weak/fallback carry rule

## 2. Intake -> Core Lossless Handoff

입력기에서 core로 넘어갈 때 아래 정보는 손실 없이 넘어가야 한다.

- `source_ref`
- `context layers`
- `provenance / origin`
- `intake classification`
- `intake blocks`
- `weakness note`
- `fallback used`
- `receipt / receipt_ref`
- `next_lane_hint`

### lock

- 입력기는 재료를 packet으로 만든 뒤 core에 넘긴다.
- core는 이 packet을 받아 line/state/lane/governance 흐름에 올릴 수 있다.
- 이 과정에서 `weakness`, `fallback`, `provenance`를 지우거나 평탄화하지 않는다.

### note

즉 lossless handoff의 핵심은
`좋은 입력만 넘기는 것`이 아니라
`약함과 출처를 포함한 입력을 그대로 넘기는 것`이다.

## 3. Core -> Shell Display-Only Boundary

shell은 core를 operator가 읽고 다루게 하는 운용면이지만,
canonical 의미체계와 판정권은 core에 남는다.

### shell이 보여줄 수 있는 것

- `case state`
- `lane progression`
- `current-reading summary`
- `governance badges`
- `trace / history preview`
- `linked program status`
- `surface packet view model`

### shell이 결정하면 안 되는 것

- `line / state 확정`
- `governance release`
- `promotion 허용`
- `next-hop canonical decision`
- `core interpretation rewrite`

### lock

- shell은 운용면과 view model을 가진다.
- shell은 core 결과를 읽기 좋게 적응시킬 수 있다.
- shell은 core의 canonical object를 대체하거나 판정을 재정의하지 않는다.

## 4. Governance Decision vs Display Boundary

governance는 shell panel에 보일 수 있지만,
판정권은 core의 governance 축에 남는다.

### core가 판정하는 것

- `hold`
- `observer-only`
- `promotion 금지`
- `mixed corridor`
- `release condition`
- `next check trigger`

### shell이 표시하는 것

- `hold badge`
- `reason summary`
- `release pending state`
- `next check reminder`
- `governance panel explanation`

### lock

- governance decision은 core 소유다.
- governance display는 shell 소유다.
- shell은 governance를 보이게 할 수 있지만, hold를 임의로 해제하거나 승격 조건을 바꾸지 않는다.

## 5. Weak/Fallback Carry Rule

약한 입력과 fallback 상태는 intake 단계에서만 의미가 있는 정보가 아니다.  
그것은 core 판단과 shell 표시에도 계속 살아 있어야 한다.

### carry targets

- intake -> core
- core -> surface packet
- surface packet -> shell view

### lock

- `weak intake`
- `mixed classification`
- `fallback used`
- `residue-only readiness`
- `re-read needed`

같은 상태는 중간 handoff에서 숨기거나 제거하지 않는다.

### note

이 규칙은 `실패를 감추지 않는다`는 원칙과 연결된다.  
약함은 지워야 할 noise가 아니라, governance와 reread를 더 정확하게 만드는 입력이다.

## 6. Handoff Summary

현재 기준의 handoff는 아래처럼 잠근다.

`intake layer`
-> `lossless packet handoff`
-> `core interpretation / governance / surface preparation`
-> `display-only shell adaptation`

즉:

- intake는 재료와 약함을 같이 넘긴다
- core는 해석과 판정을 맡는다
- shell은 보이게 하지만 재판정하지 않는다

## 7. Final Lock Sentence

현재 handoff 기준은 다음 문장으로 잠근다.

`입력기에서 core로 넘어갈 때는 출처, 문맥, 약함, fallback을 잃지 않고 넘기며, core에서 shell로 넘어갈 때는 current-reading과 governance를 표시용으로 적응시키되 canonical 판정권은 core에 남긴다.`
