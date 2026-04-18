[[DOCROLE:reference]] [[RUNMODE:ingest_only]] [[PRIORITY:high]]
[[A]] [[OBJ:external_case_example]] [[SEM:saltlux_goover_relation_reading_example]] [[ROLE:reference]]

# 예시문 v0
## 외부 기술 사례가 공간에 들어왔을 때 어떻게 읽히고 기록되는가

### 0. 이 예시문의 목적
이 문서는 선언문이 아니다.  
이 문서는 “이 철학이 실제로 엔진 안에서 어떻게 작동해야 하는가”를 보여주는 **예시문**이다.

핵심은:
- 외부 기술 사례 1건이 들어왔을 때
- 그것이 기존 공간과 어떤 의미 관계를 가지는지
- 무엇을 차용할 수 있고 무엇을 분리해야 하는지
- 그 결과가 앞으로 어디에 쓰일 수 있는지

를 엔진 친화적인 형태로 남기는 것이다.

---

## 1. 입력 재료
### 입력 이름
Saltlux Goover / Ontology-based Multi-Agent System 사례 요약

### 입력 종류
- 외부 기술 사례
- 구조 비교 재료
- 탐색 실험 재료
- 엔진 정교화 자극 재료

### 입력 요약
이 사례는
- ontology / graph rag / knowledge graph
- role-based agent
- grounding / verification loop
- structure-to-visual
- enterprise-grade orchestration

같은 요소를 가진다.

즉 표면적으로는 “기술 서비스 사례”지만,
우리 공간 안에서는 단순 제품 설명이 아니라
**비교축 + 구조 추출 재료**로 읽힌다.

---

## 2. 현재 읽힘
### focus_object
Saltlux 사례 전체

### material_role
- 비교축
- 구조 차용 재료
- 엔진 점검기
- 탐색 예시 입력

### current_reading
이 입력은 우리와 같은 종류의 엔진을 그대로 보여주는 것은 아니다.  
하지만 “복잡한 의미를 어떻게 구조로 다루는가”라는 점에서  
우리 공간과 강한 비교 가능성을 가진다.

즉 현재 읽힘은:
- 같은 결과물을 만들자는 사례 = 아님
- 구조적 방법을 차용할 수 있는 사례 = 맞음
- 우리 엔진의 부족한 점을 비춰보는 거울 = 맞음

---

## 3. 기존 공간과의 닿음
### 3-1. 닿는 축 A — 의미층 / 실행층 분리
Saltlux 사례는 ontology/graph와 agent workflow를 분리한다.  
이건 우리 공간의 아래 자산들과 닿는다.

- docs/contracts / policies / guides / reports 분리
- Codex / Gemini / User 역할 분리
- app / scripts / runtime / references 분리
- 엔진 본체와 관찰/보조 도구의 구분

### 관계 판독
- relation_kind: STRUCTURE_BORROWABLE
- user_language_summary:
  이 사례는 “지식의 뼈대와 실행 도구를 섞지 않는다”는 점에서
  우리 구조와 닿는다.
  그대로 복제할 대상은 아니지만,
  분리 원리는 차용 가능하다.

### relation_reason
우리도 이미
- 구조와 실행을 분리하려는 방향
- 기준문/운영문서/관찰면을 나누는 방향
- Codex/Gemini의 역할을 분리하는 방향
을 가지고 있다.
즉 이 사례는 새로운 개념이라기보다,
우리의 기존 방향을 더 또렷하게 해주는 비교 재료다.

---

### 3-2. 닿는 축 B — grounding / verification loop
Saltlux 사례는 생성 결과를 ontology/graph와 대조해 hallucination을 줄이려 한다.  
이건 우리 공간의 아래 자산들과 닿는다.

- provenance
- per-run evidence
- latest pointer
- observer log
- why / trace / write-back 확인 흐름

### 관계 판독
- relation_kind: DIFFERENT_MEANING_SAME_CONTEXT
- user_language_summary:
  이 사례와 우리는 “결과를 그냥 믿지 않고 다시 근거를 확인한다”는 문제의식은 같다.
  다만 저쪽은 ontology/graph를 더 강한 기준면으로 쓰고,
  우리는 provenance / evidence / readback 구조를 더 중심에 둔다.

### relation_reason
문제의식은 비슷하지만 구현 철학은 다르다.
그러므로 그대로 이식이 아니라,
“검증 루프를 더 분명히 가져야 한다”는 압력으로 읽는 것이 맞다.

---

### 3-3. 닿는 축 C — role-based agent / orchestration
Saltlux는 signal agent / briefing agent / drafting agent를 둔다.
이건 우리 공간에서 다음과 닿는다.

- Codex = 수정 / 실행 / 기록 생성
- Gemini = 후단 판독 / 비교 / 브리핑
- User = 방향 / 승인 / 최종 판단

### 관계 판독
- relation_kind: STRUCTURE_BORROWABLE
- user_language_summary:
  우리는 기업형 멀티에이전트 시스템은 아니지만,
  “역할을 섞지 말자”는 운용 원리는 강하게 차용 가능하다.

### relation_reason
우리 쪽은 agent 수를 늘리는 것이 목표가 아니다.
하지만 역할 분리 원리는 이미 작동 중이고,
이 사례는 그 원리를 더 선명하게 정리할 수 있게 해준다.

---

### 3-4. 닿지만 분리해야 하는 축 D — ontology 선고정
Saltlux는 ontology가 강한 기준면으로 먼저 서 있다.
이 부분은 우리와 다르다.

### 관계 판독
- relation_kind: SAME_CONTEXT_DIFFERENT_FLOW
- user_language_summary:
  이 사례는 “개념을 먼저 잠그고 그 위에 데이터를 얹는 쪽”에 가깝고,
  우리는 “점과 연결이 먼저 생기고 나중에 개념이 응결되는 쪽”에 가깝다.
  따라서 이 부분은 그대로 가져오면 우리 공간의 숙성 전 상태를 너무 빨리 굳혀버릴 위험이 있다.

### not_adopted_reason
현재 우리 엔진은
- 후 구조화
- 응결 우선
- 희미한 연결 보존
- 가능한 의미의 다결성 유지
가 중요하다.
그러므로 ontology 선고정 방식은 지금 코어에 넣으면 과하다.

---

## 4. 이번 입력으로 새로 또렷해진 것
이 사례가 들어오면서 우리 공간에서 새로 또렷해진 것은 아래다.

### 4-1. 탐색은 단순 조회가 아니다
외부 기술 사례 1건이 들어왔을 때,
그것을 구조 차용 / 분리 유지 / 비교축 / 점검기 / 프롬프트 재료로 읽을 수 있다는 점이 더 또렷해졌다.

### 4-2. 관계 종류 기록이 필요하다
단순히 “연결됨”이 아니라
- 구조 차용 가능
- 같은 문제지만 다른 흐름
- 지금은 분리 유지
같은 관계 종류를 안정적으로 남길 필요가 더 선명해졌다.

### 4-3. 사용자 언어 번역면이 필요하다
엔진 내부값만으로는 부족하고,
“왜 이 사례가 우리와 닿는지/안 닿는지”를 사용자 언어로 읽어주는 층이 필요함이 또렷해졌다.

### 4-4. 외부 기술 문서는 기능 후보이자 엔진 점검기다
이 문서는 단순 참고자료가 아니라
- 엔진 정교화 재료
- 탐색 기능 정의 재료
- 비교축
- 문서 구조 보강 재료
로 동시에 작동한다는 점이 또렷해졌다.

---

## 5. 앞으로 어디에 쓸 수 있는가
### future_use_hint
이 입력은 앞으로 아래 용도로 다시 쓸 수 있다.

1. 탐색 기능 정의 예시  
2. 관계 판독 분류 예시  
3. “구조 차용 가능 / 분리 유지” 판단 예시  
4. Codex 점검 시나리오 입력  
5. Gemini observer 브리핑 예시  
6. 엔진 해석 부품 후보 슬롯 검토 예시  
7. 문서 레이어 분리의 의미 보강 예시

---

## 6. 코어에 넣을 것 vs 외곽에 둘 것
### 코어에 남길 만한 것
- relation_kind 필요성
- relation_reason 필요성
- structure_borrowable 구분 필요성
- same_context_different_flow 구분 필요성
- user_language_summary 필요성

### 외곽에 둘 것
- Saltlux 상세 제품 정보
- 기업형 구현 세부
- MCP 상세 표준
- 서비스 기능 상세 소개
- 멀티에이전트 산업 적용 세부 사례

즉 코어에는 “판단 구조”만 남기고,
사례 상세는 외곽 비교 재료로 남기는 것이 맞다.

---

## 7. 보류할 것
### hold / defer note
지금은 아래를 바로 하지 않는다.

- ontology-like hard schema 코어 도입
- enterprise orchestration 모방
- 에이전트 수 확장
- 전역 command center UI 설계

이 사례는 지금 기능 설계보다
구조 점검과 관계 판독 기준 보강에 먼저 쓰는 것이 맞다.

---

## 8. 이 예시가 Codex 학습에 좋은 이유
이런 예시문이 쌓이면 Codex는 단순히
“문서 요약을 잘 하는 법”을 배우는 게 아니라,
아래를 점점 더 안정적으로 읽게 된다.

- 외부 입력을 어떤 역할의 재료로 볼 것인가
- 기존 공간과의 관계를 어떤 종류로 판독할 것인가
- 무엇을 차용하고 무엇을 분리할 것인가
- 무엇을 코어에 남기고 무엇을 외곽에 둘 것인가
- 어떻게 사용자 언어로 번역할 것인가
- 어떻게 미래 사용 힌트까지 남길 것인가

즉 이런 예시문이 많아질수록
Codex는 “기술 문서 요약기”가 아니라
**우리 엔진식 탐색 판독자**로 점점 학습되기 쉬워진다.

---

## 9. 한 줄 요약
Saltlux 사례는 우리 공간에서 단순 기술 소개문이 아니라,
비교축 / 구조 차용 재료 / 엔진 점검기 / 탐색 예시 입력 / 기능 후보 발생점으로 작동한다.
핵심은 서비스를 복제하는 것이 아니라,
그 사례를 통해 우리 엔진의 관계 판독 구조와 탐색 구조를 더 또렷하게 만드는 데 있다.
