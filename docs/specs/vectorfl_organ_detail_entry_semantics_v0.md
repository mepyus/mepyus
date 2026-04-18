# VectorFL Organ Detail Entry Semantics v0

이 문서는 `Organ Detail` 면이 언제 열리고,
무엇을 기준으로 어떤 기관 상세를 보여주는지 짧게 잠근다.

목적은 organ detail이 독립 dashboard로 떠버리지 않게 하고,
반드시 current-reading과 연결된 보조 상세면으로 읽히게 하는 것이다.

## 1. Core Sentence

Organ Detail은 기본적으로
`current-reading에서 현재 책임을 가진 기관`
또는
`progression strip의 next candidate 기관`
을 기준으로 열리는 보조 상세면이다.

## 2. Primary Entry Targets

현재 단계에서 먼저 허용하는 entry target은 아래 둘이다.

### 2-1. current organ

- current responsibility strip에 표시된 기관

### 2-2. next candidate organ

- progression strip에 표시된 next candidate 중 하나

## 3. Preferred First Target

첫 mock과 초기 구현에서는 아래를 기본 target으로 둔다.

- `current organ`

이유:

- current-reading와의 연속성이 가장 강하다
- 왜 지금 이 기관이 case를 받고 있는지 바로 설명할 수 있다

## 4. Visible Sections On Entry

organ detail에 들어가면 최소 아래는 보인다.

- organ identity
- role/instruction preview
- accepted handoff preview
- caution profile
- recent return preview

## 5. What It Must Not Become

- separate manager console
- organ assignment board
- generic settings hub

즉 entry는 current-reading를 더 깊게 읽기 위한 것이지,
독립 제품 중심면이 아니다.

## 6. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 Organ Detail은 기본적으로 current-reading의 현재 책임 기관 또는 progression strip의 next candidate 기관에서 열리는 보조 상세면으로 두고, 현재 case와 연결된 instruction/handoff/caution/return 구조를 더 자세히 읽게 하는 용도로만 쓴다.`
