# VectorFL Page Drill-In Navigation Contract v0

이 문서는 `VectorFL Page` 안에서
주요 면들 사이의 최소 drill-in 이동 관계를 잠근다.

목적은 route 문자열을 확정하는 것이 아니라,
사용자가 어떤 면에서 어떤 면으로 내려가며
무엇을 더 자세히 읽게 되는지 의미 관계를 먼저 고정하는 것이다.

## 1. Core Sentence

현재 단계에서 VectorFL Page의 핵심 drill-in은 아래 두 축이다.

- `Cases / Queue` -> `Current Reading`
- `Current Reading` -> `Organ Detail`

즉 queue는 current-reading 진입면이고,
current-reading은 다시 기관 책임/지시/반환 구조로 drill-in 되는 중심면이다.

## 2. Cases / Queue -> Current Reading

### entry purpose

- 특정 case를 current-reading 중심으로 다시 읽기 위해 들어간다

### minimum carried refs

- `case_ref`
- `current_lane_ref`
- `current_surface_ref`
- `governance_state_ref`

### what becomes more visible

- current reading body
- governance state
- trace preview
- current responsibility
- progression strip

### what does not change

- queue는 canonical source가 아니다
- case/lane/governance meaning은 core 소유다

## 3. Current Reading -> Organ Detail

### entry purpose

- 현재 case를 받고 있는 기관의 역할, handoff, caution, return 구조를 더 자세히 보기 위해 들어간다

### minimum carried refs

- `organ_ref`
- `case_ref`
- `current_lane_ref`
- optional `recent_trace_refs`

### what becomes more visible

- instruction bundle preview
- accepted handoff
- caution profile
- recent return preview

### what does not change

- organ detail은 current-reading를 대체하지 않는다
- case 중심 의미는 여전히 current-reading에 남는다

## 4. Inputs / Intake -> Current Reading

이 관계는 아직 보조 drill-in으로 둔다.

### entry purpose

- intake 재료가 실제 current-reading에서 어떻게 쓰였는지 따라가기 위함

### note

- 중심 drill-in은 아니지만,
  나중에 `input detail -> linked case current-reading` 관계는 중요해질 수 있다

## 5. Current Reading -> History / Trace

이 관계도 현재는 보조 drill-in이다.

### entry purpose

- current-reading에 걸린 trace/residue/reentry를 더 길게 보기 위함

### note

- trace는 current-reading 바깥의 독립면이지만,
  현재는 current-reading에 붙은 preview에서 내려가는 구조가 자연스럽다

## 6. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 중심 drill-in 관계는 Cases/Queue에서 Current Reading으로 들어가 case 중심면을 열고, Current Reading에서 다시 현재 기관의 instruction/handoff/caution/return을 보는 Organ Detail로 내려가는 2단 구조로 읽는 것이 가장 적절하다.`
