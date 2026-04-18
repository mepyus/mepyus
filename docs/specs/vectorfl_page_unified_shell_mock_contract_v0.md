# VectorFL Page Unified Shell Mock Contract v0

이 문서는 `VectorFL Paper` 첫 mock이  
분리된 demo 페이지 모음이 아니라,
`Cases / Queue -> Current Reading -> Organ Detail` 흐름을
한 shell 안에서 읽게 만드는 최소 계약을 잠근다.

목적은 Paperclip에서 계승하기로 한 `assignment visibility + progression visibility + contextual detail drill-in`을
VectorFL 의미로 실제 앱형 mock에 묶는 것이다.

## 1. Core Sentence

첫 unified shell mock은  
`Current Reading`을 중심 console로 유지하면서,
왼쪽에서는 `Cases / Queue`와 `Inputs / Intake`,
오른쪽에서는 `Governance / History / Programs`를 보게 하고,
현재 책임 기관 또는 next candidate 기관의 detail을
같은 shell 안의 contextual panel로 여는 구조여야 한다.

## 2. Required Unified Relations

현재 단계에서 unified shell은 아래 관계를 동시에 보여야 한다.

- `Cases / Queue`가 current-reading 진입면이라는 점
- `Current Reading`이 case 중심 console라는 점
- `Current Responsibility / Progression`이 기관 흐름을 보여준다는 점
- `Organ Detail`이 독립 대시보드가 아니라 contextual panel이라는 점

## 3. Required Surfaces

### 3-1. left navigation

- current-reading-first primary nav
- optional rail-minimal note

### 3-2. left support column

- queue preview
- inputs/intake preview

### 3-3. center console

- current responsibility strip
- current reading body
- lane strip
- progression strip

### 3-4. right support column

- governance card
- history/trace preview
- programs/connections preview

### 3-5. contextual organ detail panel

- current organ detail
- optional next candidate detail
- explicit entry target and carried refs

## 4. What Must Stay True

- `Current Reading` remains the semantic center
- organ detail does not replace case center
- queue remains entry surface, not manager board
- governance remains core-owned even when panelized
- trace remains carry/history surface, not generic activity feed

## 5. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 첫 unified shell mock은 Cases/Queue, Inputs, Current Reading, Governance, History, Programs를 같은 frame 안에서 보여주되, Current Reading을 중심 console로 유지하고 Organ Detail은 현재 책임 또는 next candidate에 대한 contextual drill-in panel로만 여는 구조여야 한다.`
