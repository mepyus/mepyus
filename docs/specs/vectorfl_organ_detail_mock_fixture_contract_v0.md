# VectorFL Organ Detail Mock Fixture Contract v0

이 문서는 `기관 상세면(organ detail surface)` 첫 mock에 필요한 fixture 계약을 잠근다.

목적은 agent detail 참조를 그대로 들이지 않고,
VectorFL 방식의 `instruction bundle + accepted handoff + recent return trace + caution profile`
를 보여주는 보조면을 실제로 시험할 수 있게 하는 것이다.

## 1. Core Sentence

첫 organ detail mock은 특정 기관 하나를 중심으로  
그 기관이 무엇을 읽고, 무엇을 받고, 무엇을 남기며, 어디서 보수적으로 멈추는지를
한 장에서 볼 수 있어야 한다.

## 2. Minimum Fixture Sections

### 2-1. organ identity

- organ ref
- organ role label
- current status
- related lane refs

### 2-2. instruction bundle preview

- role sentence
- reading priorities
- output contract

### 2-3. accepted handoff preview

- accepted input kinds
- required packet fields
- common triggers

### 2-4. caution profile

- stop/hold conditions
- preserve-first rules
- avoid wording summary

### 2-5. recent return preview

- recent summary return
- recent handoff target
- recent trace carry

## 3. First Organ Choice

첫 mock 대상으로는 `translation organ`이 가장 적절하다.

이유:

- intake와 flow interpretation 사이에 놓여 있어 역할이 선명하다
- grammar shift와 lane hint를 같이 보여주기 좋다
- current-reading 중심 구조와도 잘 이어진다

## 4. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL organ detail first mock은 translation organ을 우선 대상으로 삼아, identity, instruction bundle preview, accepted handoff preview, caution profile, recent return preview를 한 장에서 보여주는 fixture 계약으로 시작하는 것이 맞다.`
