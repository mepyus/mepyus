# VectorFL Page Left Rail Semantics v0

이 문서는 Paperclip의 `CompanyRail`을 참고하되,
`VectorFL Page`에서 left rail이 어떤 의미를 가질 수 있는지 현재 단계 기준으로 잠근다.

목적은 company selector를 그대로 들이지 않고,
개인용 VectorFL Page에서 rail이 필요한지, 필요하다면 무엇을 바꾸는지 먼저 정리하는 것이다.

## 1. Core Sentence

VectorFL Page의 left rail은
기본적으로 `company selector`가 아니라,
개인용 인스턴스 안에서 `current reading context`를 크게 흔들지 않는 한정된 전환 rail이어야 한다.

## 2. Current Reading

현재 단계에서는 left rail을 강한 중심 요소로 두지 않는다.

이유:

- VectorFL Page는 개인용 프로그램이다
- company/workspace switching이 primary 가치가 아니다
- current-reading continuity가 더 중요하다

즉 rail은 있더라도 sidebar보다 더 약한 보조 구조다.

## 3. Allowed Meanings

현재 단계에서 left rail에 허용 가능한 의미는 아래 정도다.

### 3-1. instance / profile switch

- 다른 VectorFL 인스턴스나 개인 work mode 전환

### 3-2. linked program focus switch

- 현재 읽기 기준 프로그램을 좁게 전환

### 3-3. saved workspace focus

- 자주 보는 bounded focus set 전환

## 4. Not Allowed Meanings

- company hierarchy
- org workspace tree
- multi-tenant company switching as canonical model

즉 Paperclip rail의 핵심 의미는 거의 그대로 쓰지 않는다.

## 5. Practical Rule

첫 구현 단계에서는 아래처럼 읽는 것이 가장 안전하다.

- left rail은 optional
- sidebar와 center console이 먼저
- rail은 나중에 필요가 생기면 얇게 붙인다

즉 지금 당장은 `rail-minimal`이 맞다.

## 6. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 left rail은 Paperclip처럼 company selector를 중심으로 두지 않고, 현재 단계에서는 optional한 보조 전환 구조로만 두며, personal instance/profile focus나 linked program focus 정도만 미래 후보로 열어두는 rail-minimal semantics가 맞다.`
