[[DOCROLE:reference]] [[RUNMODE:ingest_only]] [[PRIORITY:normal]]
[[A]] [[OBJ:tech_analysis_example]] [[SEM:saltlux_goover_ontology_based_multi_agent_system]] [[ROLE:reference]]

# [Tech-Analysis] Saltlux Goover: Ontology-based Multi-Agent System

## 1. 개요 (Architecture Overview)
솔트룩스의 '구버(Goover)'는 단순 LLM 래퍼(Wrapper)가 아닌, **뉴로-심볼릭(Neuro-Symbolic) AI** 접근법을 채택한 지식 가공 플랫폼이다. 지식의 뼈대(Ontology)와 실행 엔진(Multi-Agent)을 분리하여 신뢰성과 확장성을 확보한 것이 핵심이다.

---

## 2. 핵심 기술 스택 (Key Technology Stack)

### 2.1. 지식 표현 및 추론: Graph RAG & Ontology
* **Semantic Ontology (T-Box/A-Box):** 도메인 지식(기업, 기술, 인물 등)의 관계를 정의하는 상위 스키마를 기반으로 데이터를 구조화함.
* **Connectome (Knowledge Graph):** 비정형 데이터를 실시간으로 추출(Extraction)하여 엔티티 간의 연결망으로 변환.
* **Multi-hop Reasoning:** 벡터 유사도 검색의 한계를 넘어, 그래프 경로를 따라 파편화된 정보를 논리적으로 결합하여 답변을 생성.
* **Grounding:** 생성된 답변을 지식 그래프의 사실 관계와 대조하여 할루시네이션(Hallucination)을 기술적으로 억제.

### 2.2. 추론 엔진: Luxia 3.5 (LLM)
* **Reasoning-First:** 사고 과정(Chain-of-Thought)을 스스로 설계하는 추론형 모델.
* **Structure-to-Visual:** 분석된 데이터를 단순 텍스트가 아닌 PPT 슬라이드, 차트 등 구조적 시각물로 즉시 변환하는 멀티모달 최적화.

### 2.3. 실행 아키텍처: Agentic Workflow
* **MCP (Model Context Protocol):** 에이전트 간 컨텍스트 공유 및 도구 활용을 위한 표준 프로토콜 준수.
* **Role-based Agents:**
  * `Signal Agent`: 외부 이슈 트리거링 및 실시간 감시.
  * `Briefing Agent`: 데이터 요약 및 개인화 큐레이션.
  * `Drafting Agent`: 리포트 및 프레젠테이션 자동 생성.

---

## 3. 아키텍트적 시사점 (Architect's Insight)
1. **지식의 정형화:** 비정형 데이터(News, Report)를 정형 데이터(Graph)로 변환하는 파이프라인의 자동화가 시스템의 본질적 가치임.
2. **확장성:** MCP 도입을 통해 향후 기업 내부 시스템(ERP, Legacy DB)과의 유연한 결합 가능성을 열어둠.
3. **검증 루프:** LLM의 출력을 온톨로지라는 '정답지'와 대조하는 구조는 산업용 미션 크리티컬 시스템 설계 시 필수적인 참조 모델임.

---

## 4. 관련 키워드
#AI_Agent #Graph_RAG #Ontology #Neuro_Symbolic #Saltlux #Luxia #MCP #Knowledge_Graph
