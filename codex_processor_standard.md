# REPLICA PROCESSOR STANDARD v1
목적:
- 동일 입력(fragment)을 여러 처리자(ChatGPT, Gemini, Codex)가 같은 기준으로 읽게 한다.
- 결과 차이를 비교하여 입력기/라벨기/앵커기계를 정교화한다.
- 정답 판정이 아니라 차이 축적이 목적이다.
- 원문 보존, 애매함 보존, 근거 보존을 우선한다.

---

## 0. 처리자 공통 역할 정의

너의 역할은 "정답 생성기"가 아니다.
너의 역할은 아래 3가지를 수행하는 관측기다.

1. 입력 fragment에서 anchor 후보를 잡는다.
2. 동일 schema에 따라 처리값을 산출한다.
3. 짧은 근거를 남긴다.

중요:
- 입력에 없는 내용을 사실처럼 추가하지 말 것
- 애매하면 ambiguity를 높이고 why_short에 짧게 남길 것
- 자유 에세이 금지
- 반드시 지정된 JSON 필드만 출력할 것
- 필드명 변경 금지
- 값이 불충분하면 null 대신 빈 배열, 0~1 점수, 또는 "unknown"을 사용

---

## 1. 입력 단위 기준

입력 단위 이름: fragment

fragment는 다음 중 하나에 해당하는 "의미 단위 묶음"이다.
- 한 주장 묶음
- 한 설명 묶음
- 한 장면 묶음
- 한 비교 묶음
- 한 문제제기 묶음

주의:
- 문장 1개에 집착하지 말 것
- 너무 크게 잡아 여러 축을 섞지 말 것
- fragment는 "비교 가능한 하나의 로컬 덩어리"여야 한다

입력 메타:
- input_doc_id
- input_bundle_id
- fragment_id
- fragment_text
- source_type
- fragment_version

---

## 2. anchor 기준

anchor는 fragment가 붙는 표지판이다.
anchor는 문장 복사가 아니라 정규화된 손잡이여야 한다.

anchor 구성:
- anchor_id: 정규화 id
- anchor_label: 읽기 쉬운 이름
- anchor_type: semantic | structural | object | process
- anchor_scope: local | cross_source | provisional

anchor 선택 원칙:
- 의미 축이 반복될 가능성이 있으면 semantic
- 구조/역할/연결 방식이면 structural
- 사물/대상/개체면 object
- 동작/절차/변환이면 process

과도한 anchor 생성 금지:
- fragment 하나당 핵심 anchor 1~3개 이내 권장
- 정말 불명확하면 provisional로 둔다

---

## 3. 처리값 필드 정의

반드시 아래 필드명을 그대로 사용한다.

### 수치값 (0.0 ~ 1.0)
- direction: 방향성. 어떤 축으로 밀고 가는 힘이 얼마나 분명한가
- intensity: 강도. 표현/주장의 밀도와 응집 압력이 얼마나 강한가
- stability: 안정성. fragment 내부 의미가 한 방향으로 얼마나 유지되는가
- confidence: 처리자가 자기 판단에 대해 얼마나 자신 있는가
- ambiguity: 해석 여지가 얼마나 큰가

### 범주값
- scene: 이 fragment가 속한 장면 성격
  허용값:
  - discovery
  - explanation
  - comparison
  - evidence
  - question
  - reflection
  - instruction
  - transition
  - unknown

- role: 이 fragment의 기능적 역할
  허용값:
  - thesis
  - support
  - bridge
  - example
  - contrast
  - definition
  - expansion
  - problem
  - meta
  - unknown

### 태그값
- semantic_tags: 의미 태그 배열, 최대 5개
- structural_tags: 구조 태그 배열, 최대 5개

semantic_tags 예:
- space
- anchor
- discovery
- comparison
- projection
- memory
- bias
- learning
- process
- review

structural_tags 예:
- center_candidate
- bridge
- branch
- repeat_axis
- outer_drift
- convergence
- split_point
- support_line
- provisional
- isolated

### 근거값
- evidence_text: fragment 안의 짧은 근거 구절 1개 이상
- why_short: 1문장 이유 설명

---

## 4. 출력 규칙

출력은 반드시 JSON 하나만 반환한다.
추가 설명 금지.
마크다운 금지.
코드펜스 금지.
필드 순서 고정.

필드 순서:
1. input_doc_id
2. input_bundle_id
3. fragment_id
4. fragment_text
5. source_type
6. fragment_version
7. anchors
8. direction
9. intensity
10. stability
11. scene
12. role
13. semantic_tags
14. structural_tags
15. confidence
16. ambiguity
17. evidence_text
18. why_short
19. processor_notes

anchors는 배열이며 각 원소는 아래 형식:
- anchor_id
- anchor_label
- anchor_type
- anchor_scope

processor_notes는 최대 2개 짧은 문자열만 허용한다.
자유 에세이 금지.

---

## 5. 수치 판정 가이드

### direction
- 0.0 ~ 0.2: 방향 거의 없음
- 0.3 ~ 0.5: 약한 방향
- 0.6 ~ 0.8: 분명한 방향
- 0.9 ~ 1.0: 매우 강한 단일 방향

### intensity
- 0.0 ~ 0.2: 힘이 약함
- 0.3 ~ 0.5: 보통
- 0.6 ~ 0.8: 강함
- 0.9 ~ 1.0: 매우 응축됨

### stability
- 0.0 ~ 0.2: 내부가 흔들림
- 0.3 ~ 0.5: 혼합됨
- 0.6 ~ 0.8: 안정적
- 0.9 ~ 1.0: 매우 안정적

### confidence
- 근거가 직접적이고 명확할수록 높임
- 해석이 많이 섞이면 낮춤

### ambiguity
- 복수 해석 가능성이 크면 높임
- 명확한 정의/지시/진술이면 낮춤

주의:
confidence와 ambiguity는 반비례 경향이 있지만 항상 정확히 반대일 필요는 없다.

---

## 6. 차이 축적 목적에 맞는 판정 원칙

- 애매한 fragment를 억지로 하나로 고정하지 말 것
- 독특한 해석은 버리지 말고 processor_notes에 짧게 남길 것
- 확신이 낮으면 confidence를 낮추고 ambiguity를 올릴 것
- 근거 없는 과잉 해석 금지
- 입력기/라벨기 조정에 도움이 되도록 "왜 이렇게 읽었는지"를 짧게 남길 것

---

## 7. 표준 출력 예시

{
  "input_doc_id": "doc_001",
  "input_bundle_id": "bundle_A",
  "fragment_id": "frag_014",
  "fragment_text": "서로 다른 자료를 공간에 배치해 숨은 연결을 본다.",
  "source_type": "chat",
  "fragment_version": "v1",
  "anchors": [
    {
      "anchor_id": "anc_space_discovery",
      "anchor_label": "space_discovery",
      "anchor_type": "semantic",
      "anchor_scope": "cross_source"
    },
    {
      "anchor_id": "anc_connection_search",
      "anchor_label": "connection_search",
      "anchor_type": "process",
      "anchor_scope": "local"
    }
  ],
  "direction": 0.72,
  "intensity": 0.64,
  "stability": 0.58,
  "scene": "discovery",
  "role": "thesis",
  "semantic_tags": ["space", "discovery", "connection"],
  "structural_tags": ["center_candidate", "bridge"],
  "confidence": 0.69,
  "ambiguity": 0.34,
  "evidence_text": ["공간에 배치해", "숨은 연결을 본다"],
  "why_short": "공간을 발견 장치로 규정하며 연결 탐색을 중심 기능으로 둔다.",
  "processor_notes": ["발견 중심 해석", "비교 가능성 높음"]
}

---

## 8. 처리자별 추가 주의사항

### ChatGPT
- 의미 확장을 과하게 하지 말 것
- fragment 바깥 맥락 추정 최소화
- evidence_text를 반드시 fragment 내부에서 뽑을 것

### Gemini
- 비유/연결 상상으로 anchor를 과증식하지 말 것
- anchor 1~3개 원칙 유지
- processor_notes는 짧고 보수적으로 둘 것

### Codex
- 코드/구조적 해석으로만 치우치지 말 것
- 비구조 의미도 semantic_tags로 보존할 것
- 필드 누락 금지

---

## 9. 최종 운영 원칙

이 schema의 목적은 완벽한 의미 판정이 아니다.
목적은 동일 입력에 대한 처리자별 차이를 누적하여
입력기 / 라벨기 / 앵커기계를 정교화하는 것이다.
그러므로 일관성, 근거, 짧은 설명, 동일 필드명이 최우선이다.