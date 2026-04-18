# VectorFL Current Reading Organ Visibility Brief v0

이 문서는 `Current Reading` 중심면 안에서  
기관 책임과 next-hop 진행 구조를 어떻게 보이게 할지 짧게 잠근다.

목적은 current-reading body를 유지하면서도,
Paperclip에서 계승하기로 한 `responsibility + progression visibility`를
VectorFL 의미로 더 선명하게 드러내는 것이다.

## 1. Core Sentence

Current Reading은 단순 summary body가 아니라,  
`지금 어느 기관이 이 case를 받고 있고, 왜 여기 머물며, 다음 기관 후보가 무엇인지`
를 같이 보여주는 중심 console이어야 한다.

## 2. Required Structural Sections

현재 단계에서 `Current Reading` 안에 아래 두 면은 반드시 보여야 한다.

### 2-1. current responsibility strip

- current organ ref
- current lane ref
- placement reason
- active restriction flags

즉 `누가 지금 받고 있는가`를 숨기지 않는다.

### 2-2. progression strip

- previous organ step
- current organ step
- next organ candidates
- held candidate vs preferred candidate 구분

즉 `어디서 왔고 지금 어디 있으며 다음 어디로 갈 수 있는가`가 보여야 한다.

## 3. Relation To Existing Current Reading Sections

위 두 면은 아래 기존 면과 같이 읽힌다.

- current responsibility strip
- current reading body
- lane strip
- progression strip
- governance side
- trace strip

즉 current-reading 중심면은 이제 `body + structure`를 함께 가진다.

## 4. What It Must Not Become

- generic workflow board
- full orchestration dashboard
- manager-only queue screen

즉 중심은 여전히 `current-reading body`이고,  
기관 흐름 표시는 그것을 보강하는 구조면이다.

## 5. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 Current Reading은 summary body만 보여주는 detail이 아니라, current responsibility strip과 progression strip을 함께 포함해 현재 기관 책임과 다음 기관 흐름을 current-reading, governance, trace와 결합해 보여주는 중심 console이어야 한다.`
