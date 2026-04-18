# VectorFL Page Navigation Semantics v0

이 문서는 `VectorFL Page`를 개인용 forked shell로 가져올 때  
어떤 navigation과 panel semantics를 중심으로 다시 소유할지 잠근다.  
세부 UI 설계 문서가 아니라, page/frame 수준의 의미 배치를 먼저 고정하는 문서다.

## 1. Core Sentence

VectorFL Page의 navigation은 `current-reading first`를 중심으로 잡고,  
나머지 입력/queue/history/connections는 그 주변에서 current-reading을 보조하는 면으로 둔다.

즉 이 프로그램의 중심은 `task board`가 아니라 `current-reading console`이다.

## 2. Primary Navigation Order

현재 단계에서 VectorFL Page의 1차 navigation 우선순위는 아래처럼 잠근다.

1. `Current Reading`
2. `Inputs / Intake`
3. `Cases / Queue`
4. `History / Trace`
5. `Programs / Connections`

### note

- `Current Reading`이 중심면이다
- `Inputs / Intake`는 재료 진입면이다
- `Cases / Queue`는 여러 case 사이 이동을 돕는 진입면이다
- `History / Trace`는 append-only 회고면이다
- `Programs / Connections`는 외부 프로그램과의 연결면이다

## 3. Primary Page Semantics

### 3-1. Current Reading

- 역할:
  - 지금 무엇을 읽고 있는가
  - 어느 lane에 있는가
  - 무엇이 hold 상태인가
  - 어떤 trace/residue가 남아 있는가
- 중심 객체:
  - `Surface Packet`
  - `Governance Record`
  - `Lane State Record`
  - `Trace / Memory Record` preview
- 성격:
  - 이 프로그램의 중심 console

### 3-2. Inputs / Intake

- 역할:
  - 어떤 source가 들어왔는가
  - 어떤 context가 붙었는가
  - 어떻게 block이 준비됐는가
  - weak/fallback 상태가 있는가
- 중심 객체:
  - `Source Registry Entry`
  - `Intake Block`
  - `Intake Packet`
  - `Intake Status Record`
- 성격:
  - 전단 재료 확인면

### 3-3. Cases / Queue

- 역할:
  - 어떤 case들이 현재 살아 있는가
  - 어느 lane에 머무는가
  - 어떤 hold/restriction이 걸려 있는가
  - 어떤 current surface preview가 있는가
- 중심 객체:
  - `Case Record`
  - `Lane State Record`
  - `Governance Record`
  - `Surface Packet`
- 성격:
  - current-reading 진입면

### 3-4. History / Trace

- 역할:
  - append-only 흔적을 회고적으로 읽는다
  - residue와 reentry 단서를 다시 본다
  - decision trace를 따라간다
- 중심 객체:
  - `Trace / Memory Record`
  - `Governance Record.decision_trace_ref`
- 성격:
  - 회고 / 기억면

### 3-5. Programs / Connections

- 역할:
  - 외부 프로그램 연결 상태를 본다
  - action request나 response 경계가 어디에 있는지 본다
  - linked program이 case/lane과 어떻게 접속하는지 본다
- 중심 객체:
  - `Case Record.linked_program_refs`
  - program connection related refs
- 성격:
  - 외부 접속면

## 4. Panel Semantics Inside Current Reading

현재 단계에서 `Current Reading` 내부 panel semantics는 아래처럼 잠근다.

### center pane

- 의미:
  - `current reading body`
  - 지금 가장 먼저 읽어야 하는 핵심 surface

### lane strip

- 의미:
  - 현재 lane과 next hop candidate를 좁게 보여주는 진행 strip

### governance card / panel

- 의미:
  - hold, restriction, release condition, next check trigger를 숨기지 않는 감독면

### trace strip / history preview

- 의미:
  - 최신 residue/reentry/trace 흔적을 current-reading과 접속시켜 보여주는 회고 strip

### supporting context side

- 의미:
  - supporting units, linked program hints, related anchors를 보조적으로 보여주는 면

## 5. What The Navigation Must Not Drift Into

아래 쪽으로 drift하면 안 된다.

- issue board 중심 프로그램
- assignment manager 중심 프로그램
- company/project hierarchy 중심 프로그램
- generic dashboard

즉 이 프로그램은 `current-reading, governance, trace, intake`를 중심으로 읽혀야 한다.

## 6. Personal Program Note

VectorFL Page는 개인용 프로그램이므로 navigation도 내 운용 기준을 따른다.

즉:

- 가장 자주 드나드는 면은 current-reading이어야 한다
- queue는 중심이 아니라 진입/정리용 면이다
- inputs는 재료 품질을 보는 면이다
- history와 programs는 필요 시 여는 보조면이다

## 7. What Is Not Locked Yet

현재 문서에서 아직 잠그지 않는 것은 아래다.

- exact tab names
- route path strings
- icon system
- keyboard shortcuts
- multi-pane responsive behavior
- panel resizing behavior

즉 지금은 page/frame 수준의 의미 배치만 잠근다.

## 8. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page는 Current Reading을 중심 console로 두고, Inputs는 재료 진입면, Cases는 current-reading 진입 queue, History는 trace 회고면, Programs는 외부 접속면으로 두는 current-reading-first navigation semantics 위에서 작동한다.`
