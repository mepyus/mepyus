# VectorFL Organ Detail Surface Translation v0

이 문서는 Paperclip의 agent detail surface를 참고해,  
VectorFL Paper에서 나중에 `기관 상세면`이 어떤 의미로 필요할지 번역 기준을 잠근다.

목적은 지금 당장 기관 상세 페이지를 구현하는 것이 아니라,  
기관 수가 많아졌을 때 무엇을 한 자리에 보여주고 무엇은 중심면 밖으로 빼야 하는지 미리 흔들리지 않게 하는 것이다.

## 1. Core Sentence

VectorFL Paper에서 `기관 상세면`은  
기관을 설명하는 프로필 페이지가 아니라,
`기관 instruction bundle + accepted handoff + recent return trace + caution profile`
를 함께 보는 상세면으로 읽는 것이 맞다.

## 2. Why A Detail Surface Will Matter Later

앞으로 기관이 많아지면 아래를 별도 면에서 봐야 할 가능성이 크다.

- 이 기관은 무엇을 읽는가
- 어떤 handoff packet을 받을 수 있는가
- 어떤 반환 형식을 내는가
- 어떤 caution/governance 규칙을 가진가
- 최근 어떤 trace/summary를 남겼는가

즉 기관이 늘어날수록
`Current Reading만으로는 다 담기지 않는 기관별 책임면`
이 필요해진다.

## 3. Translated Sections

Paperclip agent detail의 구조를 VectorFL 언어로 번역하면 아래 section이 먼저 보인다.

### 3-1. instruction bundle section

- 기관 role sentence
- reading priorities
- output contract
- caution rules

### 3-2. accepted handoff section

- accepted inputs
- required packet fields
- common trigger types

### 3-3. recent return section

- recent summary returns
- recent trace carries
- recent governance cautions

### 3-4. continuity section

- case/lane continuity hints
- previous trace refs
- carry summary

## 4. What Must Stay Out Of The Center

기관 상세면이 생겨도 아래는 여전히 중심 console가 아니다.

- generic organ dashboard
- full execution control panel
- cost-first metrics panel
- external program orchestrator

즉 기관 상세면은 보조면이고,
`Current Reading`이 여전히 중심 console다.

## 5. Relation To Current Reading

기관 상세면은 current-reading를 대체하지 않는다.

- current-reading:
  - 현재 case와 현재 흐름 중심
- organ detail:
  - 특정 기관의 책임/지시/반환 계약 중심

즉 `case 중심면`과 `기관 중심면`은 나중에 분리될 수 있다.

## 6. Relation To Paperclip Reference

Paperclip에서 가져오는 감각은 아래다.

- 하나의 node 상세면에 설정/지시/실행 흔적을 묶는 구조
- 탭 또는 section으로 구획하는 감각

가져오지 않는 것은 아래다.

- agent naming
- adapter/cost 중심 가치
- skill market worldview

## 7. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Paper에서 기관 상세면은 나중에 기관별 instruction bundle, accepted handoff, recent return trace, caution profile을 함께 보는 보조면으로 읽는 것이 맞고, 이는 Current Reading을 대체하지 않고 기관 수가 늘어날 때 책임과 전달 구조를 더 명시적으로 보이게 하는 용도로 준비되어야 한다.`
