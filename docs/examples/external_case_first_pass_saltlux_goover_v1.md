# external_case_first_pass_saltlux_goover_v1

## 1. 사례 개요
- 사례명: Saltlux Goover / ontology-based multi-agent system
- source_ref:
  - [external_case_example_saltlux_goover_relation_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/external_case_example_saltlux_goover_relation_reading_v0.md)
  - [tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md](/Users/sungsookim/universe/vectorfl_replica/tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md)
- 선택 이유:
  - 이미 공간에 들어와 있고
  - 구조 차용 / 분리 유지 / 탐색 판독 예시로 적합하며
  - thin operation rules를 실제로 검증하기에 크기가 과하지 않다.

## 2. 이 사례에서 실제로 관측한 것
- ontology/graph와 agent workflow를 분리하는 구조가 선명하다.
- grounding / verification loop를 강한 기준면으로 운영한다.
- role-based agent orchestration이 분명하다.
- ontology 선고정 방식은 현재 우리 엔진의 후 구조화 흐름과 다르다.

## 3. 우리 엔진 기준으로 바로 유효한 요소
- 의미층과 실행층을 섞지 않는 구조 분리 원리
- 결과를 근거와 다시 대조하는 검증 루프 문제의식
- 역할을 섞지 않는 운영 원리

## 4. 아직 보류할 요소
- ontology 선고정
- enterprise orchestration 상세 구현
- MCP 상세 표준
- 기업형 서비스 기능 세부

## 5. core / outer / defer / observer_only 1차 판독

### 후보 A. relation_kind / relation_reason / user_language_summary 슬롯
- status: `core_candidate`
- reason:
  - 이미 탐색 사례, 외부 사례 판독, stage1 문서, LLM 증류 문서에서 반복된다.
  - 다른 문맥에서도 재등장하며, 후속 판독 구조를 설명하는 축 역할을 한다.
  - outer layer에만 두기엔 엔진의 최소 판독 뼈대로서 중요하다.

### 후보 B. 구조 분리 원리(의미층 / 실행층 분리)
- status: `outer_candidate`
- reason:
  - 설명력은 크지만 현재 우리 엔진의 최소 코어 축으로 바로 잠그기엔 아직 문맥이 더 필요하다.
  - 보고서 / 기준문 / 탐색 note에서 계속 재사용하는 것이 우선 적절하다.

### 후보 C. ontology 선고정 방식
- status: `defer`
- reason:
  - 같은 문제권에서 비교는 가능하지만 현재 엔진 흐름과 다르다.
  - 지금 코어로 끌어오면 premature generalization risk가 높다.

### 후보 D. Saltlux 상세 제품 / 산업 적용 세부
- status: `observer_only`
- reason:
  - 현재는 관찰과 비교 참고용으로만 충분하다.
  - 코어 승격 판단 대상이라기보다 외곽 비교 재료에 가깝다.

## 6. refinement trigger 관점 현재 상태
- status: `watch`
- reason:
  - external case가 5건 누적된 상태는 아니다.
  - 하지만 relation slot 반복과 구조 차용/분리 유지 패턴은 이미 여러 문서에서 재등장한다.
  - 지금 바로 refinement를 열 정도는 아니지만, 다음 1~2건 누적 시 repeated pattern을 재확인할 가치가 있다.

## 7. 다음 액션 힌트
- 같은 형식으로 외부 사례 1~2건을 더 넣어 repeated pattern이 실제로 살아남는지 본다.
- 그다음 `relation_kind / relation_reason / future_use_hint` 계열이 정말 core 후보인지 정련 패스 사례로 다시 판독한다.
