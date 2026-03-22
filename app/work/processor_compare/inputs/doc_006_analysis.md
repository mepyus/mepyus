# doc_006 Analysis

## 적합성 판단

- 비교 실험용 장문 입력으로 적절하다.
- `Vector RAG 한계 -> Graph RAG 정의 -> 아키텍처 -> multi-hop 비교 -> 활용 사례 -> 기술 과제 -> 결론` 흐름이 분명하다.
- 처리자마다 기술 메커니즘, 비교 사례, 적용 전략, 과제, 결론을 어떻게 분리하는지 보기 좋다.

## Codex 기준선 절단 판단

### fragment 1
- 범위: LLM 한계와 기존 RAG 한계, Graph RAG 도입
- 중심 움직임: `graph_rag motivation`

### fragment 2
- 범위: Graph DB 정의와 관계 중심 저장 구조
- 중심 움직임: `graph_db definition`

### fragment 3
- 범위: Graph RAG 정의와 Vector RAG 대비 하이브리드 구조
- 중심 움직임: `graph_rag definition and hybrid`

### fragment 4
- 범위: 지식 그래프 구축 단계
- 중심 움직임: `graph_construction_pipeline`

### fragment 5
- 범위: 사용자 질의 처리 및 답변 생성 단계
- 중심 움직임: `query_answer_pipeline`

### fragment 6
- 범위: Multi-hop 질의에서 Vector RAG와 Graph RAG 차이
- 중심 움직임: `multi_hop comparison`

### fragment 7
- 범위: Vector RAG 처리 흐름과 한계
- 중심 움직임: `vector_rag limitation example`

### fragment 8
- 범위: Graph RAG 처리 흐름과 답변 가능성
- 중심 움직임: `graph_rag success example`

### fragment 9
- 범위: 활용 사례와 산업 적용 전략
- 중심 움직임: `application strategy`

### fragment 10
- 범위: 기술 과제와 해결 전략
- 중심 움직임: `technical challenges and guardrails`

### fragment 11
- 범위: 결론과 전망
- 중심 움직임: `future outlook`

## 관찰 포인트

- `Graph DB`와 `Graph RAG`를 독립 개념으로 자르는지 하나의 도입 묶음으로 유지하는지 차이가 날 수 있다.
- `아키텍처 단계`와 `multi-hop 예시`를 분리하는지, 파이프라인 설명에 예시를 흡수시키는지 차이가 날 수 있다.
- `활용 전략`과 `기술 과제`를 별도 fragment로 분리하는지, 하나의 확장 블록으로 묶는지 흔들릴 수 있다.
- 결론에서 `thesis`로 두는지 `reflection/meta`로 올리는지 재확인할 가치가 있다.

## 비교 메모

- Codex는 11 fragment로 절단했고, `문제 도입 -> Graph DB 정의 -> Graph RAG 정의 -> 구축 단계 -> 질의 단계 -> multi-hop 비교 -> Vector 한계 -> Graph 성공 -> 활용 사례 -> 기술 과제 -> 결론` 흐름을 가장 구조적으로 유지했다.
- ChatGPT도 11 fragment로 Codex와 거의 같은 granularity를 유지했다. `doc_005`와 달리 과세분화가 줄었고, 구조가 명확한 기술 문서에서는 상대적으로 안정적이라는 신호가 나온다.
- Gemini는 8 fragment로 크게 묶었다. 특히 `아키텍처 구축 단계`, `질의 처리 단계`, `비교 예시`, `기술 과제+정리`를 더 큰 블록으로 흡수하는 경향이 보였다.
- ChatGPT는 schema를 지켰지만, Graph RAG 정의 파트를 `comparison/thesis`로 밀어 논지화하는 경향이 있다.
- Gemini는 `scene=process`를 2회 사용하여 schema를 어겼다. 이는 과정 서술을 별도 scene처럼 처리하려는 경향을 보여준다.
- 축값 평균은 Codex 대비 ChatGPT가 더 높은 direction/intensity/confidence와 더 낮은 ambiguity를 유지했고, Gemini는 direction/intensity는 더 낮지만 stability/confidence는 높게 유지했다.
- 결론적으로 `doc_006`은 구조가 분명한 장문 기술 문서에서 `Codex=구조 보존`, `ChatGPT=논지화`, `Gemini=대묶음/과정 scene 오용` 패턴을 확인시켜주는 calibration 문서다.
