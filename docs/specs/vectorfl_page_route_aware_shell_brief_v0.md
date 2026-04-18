# VectorFL Page Route-Aware Shell Brief v0

이 문서는 `VectorFL Page` 첫 unified shell이  
정지된 단일 mock에 머무르지 않고,
`primary surface`를 바꿔 읽을 수 있는 route-aware shell로 확장될 때의 최소 기준을 잠근다.

목적은 여러 면을 열어도 `current-reading first`를 잃지 않게 하고,
Organ Detail이 여전히 contextual panel로만 남게 하는 것이다.

## 1. Core Sentence

Route-aware shell은
`Current Reading`, `Cases / Queue`, `Inputs / Intake`, `History / Trace`, `Programs / Connections`
를 primary surface로 전환할 수 있어야 하지만,
semantic center는 여전히 `Current Reading`에 두고
다른 면들은 그것을 보조하거나 진입시키는 구조로 읽혀야 한다.

## 2. Allowed Primary Surface States

현재 단계에서 허용하는 primary surface state는 아래 다섯 개다.

- `current-reading`
- `cases-queue`
- `inputs-intake`
- `history-trace`
- `programs-connections`

## 3. Meaning Rule For Each State

### 3-1. current-reading

- canonical center state
- contextual panel을 가장 자연스럽게 붙일 수 있는 상태

### 3-2. cases-queue

- current-reading 진입 전 preview state
- case/organ/progression 예고편을 본다

### 3-3. inputs-intake

- current-reading과 case 형성 전의 재료/약함/packet 상태를 본다

### 3-4. history-trace

- trace/residue/reentry를 current-reading 바깥에서 더 길게 읽는 보조 상태다

### 3-5. programs-connections

- linked program과 request boundary를 더 또렷하게 보는 보조 상태다

## 4. Contextual Panel Rule

- contextual panel은 기본적으로 `current-reading` 상태에서 가장 강하다
- 다른 primary state에서도 metadata 수준으로 열 수는 있지만,
  여전히 top-level primary state를 대체하지 않는다

## 5. What Must Not Happen

- cases-queue가 중심 console처럼 drift하는 것
- inputs-intake가 canonical case meaning을 대신하는 것
- history-trace가 generic activity app처럼 drift하는 것
- programs-connections가 control dashboard처럼 drift하는 것

## 6. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 route-aware shell은 다섯 primary surface state를 허용하되, Current Reading을 semantic center로 유지하고, Cases는 진입면, Inputs는 재료면, History는 회고면, Programs는 연결면으로 읽히게 하며, Organ Detail은 계속 contextual panel로만 둔다.`
