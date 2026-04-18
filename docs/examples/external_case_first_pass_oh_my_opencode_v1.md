# external_case_first_pass_oh_my_opencode_v1

## 1. 사례 개요
- 사례명: `oh_my_opencode_raw_input_v1`
- source_ref: [oh_my_opencode.txt](/Users/sungsookim/universe/vectorfl_replica/docs/guides/oh_my_opencode.txt)
- source_type: `external_case_primary_input`
- source_origin: `raw_external_text_or_transcript`
- source_status: `primary_input_uncompressed`
- raw primary input으로 취급한 이유:
  - 원문이 대화/설명/사용기/운영 감각이 혼합된 비압축 입력이기 때문이다.
  - 그래서 미리 요약하지 않고 구조/실무/강한 주장/수사를 먼저 분리하는 것이 우선이다.

## 2. 원문에서 실제로 관측한 구조
- 여러 모델을 역할별로 위임해 조합하는 멀티모델/멀티에이전트 하네스 프레임이 강하다.
- 사용자는 자세히 몰라도 되고, 하네스와 에이전트가 알아서 탐색/계획/실행을 분담한다는 방향이 반복된다.
- 컨텍스트 윈도우 문제를 “모든 것을 다 넣는 것”이 아니라 역할 분리와 핵심 정보 보고 체계로 다루는 프레임이 있다.
- `울트라 워크`처럼 병렬 탐색, 구조 분석, 설계, 실행을 한 번에 트리거하는 작업 방식이 나타난다.
- 비개발자도 사용할 수 있게 장벽을 낮추는 UX와 온보딩 감각이 강하다.

## 3. outer로 둔 프레임
- 멀티모델/멀티에이전트 하네스 프레임
- 사용자는 몰라도 되고 에이전트가 알아서 진행하는 위임형 작업 프레임
- 컨텍스트를 역할 분리와 핵심 정보 보고 체계로 관리하는 프레임
- `울트라 워크`형 병렬 작업 트리거 프레임
- 비개발자 진입 장벽 축소 / 쉬운 설치 / 쉬운 온보딩 프레임

## 4. defer로 보낸 강한 주장
- “다른 CLI나 다른 에이전트 툴로 돌아갈 수 없다”류의 우위 선언
- “개발은 끝났다”, “1시간 안에 끝난다” 같은 강한 효율 주장
- 모델/도구 우위에 대한 과장 가능성이 있는 비교 문장
- 토큰 사용 / 품질 / 생산성에 대한 강한 일반화

## 5. observer_only로 남긴 수사 / 감상
- 화자의 감탄
- 바이럴/열광 분위기 묘사
- 브랜딩/세계관 네이밍
- 커뮤니티 반응을 통해 강조하는 선언적 표현

## 6. core / outer / defer / observer_only 1차 판독 결과

### 후보 1. 멀티모델 / 멀티에이전트 하네스 프레임
- status: `outer_candidate`
- reason:
  - 도구 위임과 역할 분할을 구조적으로 읽는 프레임으로 가치가 높다.
  - 하지만 특정 도구 구현에 강하게 묶여 있어 지금 당장 코어 축으로 올리기보다 외곽 운영 프레임으로 반복 관찰하는 편이 안전하다.

### 후보 2. 사용자는 몰라도 되고 에이전트가 알아서 진행하는 위임형 작업 프레임
- status: `outer_candidate`
- reason:
  - page/UI 이후의 사용성 방향과 닿고, agentic UX 관점에서도 재사용 가치가 있다.
  - 다만 현재는 설명축과 운영 힌트로 남기는 것이 적절하다.

### 후보 3. 컨텍스트를 역할 분리와 핵심 정보 보고 체계로 관리하는 프레임
- status: `outer_candidate`
- reason:
  - 우리 엔진의 session/run/pointer/provenance 구조와 간접적으로 닿는 운영 감각이다.
  - 반복 관찰 가치가 높지만 아직 코어 슬롯으로 잠그기엔 이르다.

### 후보 4. `울트라 워크`형 병렬 작업 트리거 프레임
- status: `outer_candidate`
- reason:
  - 작업을 한 번에 구조 분석/탐색/설계/실행으로 넘기는 트리거 개념은 흥미롭다.
  - 하지만 현재는 구현 프레임이자 도구 패턴이지 코어 규칙은 아니다.

### 후보 5. 강한 효율 / 우위 / 생산성 주장
- status: `defer`
- reason:
  - 성능, 생산성, 다른 도구 대비 우위는 과장 가능성이 있고 검증 전 일반화 위험이 크다.

### 후보 6. 바이럴 반응 / 브랜딩 / 화자의 감상
- status: `observer_only`
- reason:
  - 현재는 관측 가치가 더 크고 엔진 규칙 후보로 보기엔 이르다.

## 7. 기존 사례와 반복된 구조
- `agentic_workflow_orchestration_frame`
  - saltlux: reasoning + planning + tool use + multi-agent coordination
  - aifrontier: harness, guardrail, agentic tool use, batch/orchestration usability
  - oh_my_opencode: 멀티모델/멀티에이전트 하네스, 병렬 작업, 역할 분담형 실행
- `agentic_ux_or_barrier_reduction_frame`
  - aifrontier에서 강했던 일반 사용자 장벽 하락/CLI 장벽 축소와 강하게 반복된다

## 8. 이번 사례에서 새로 뜬 구조
- 하네스를 하나의 “패키징된 작업 세계관”으로 다루는 프레임
- 컨텍스트 윈도우를 사람 조직/보고 체계에 비유해 관리하는 프레임
- 에이전트 이름/역할 분리 기반의 협업 설계 프레임
- “울트라 워크”처럼 작업 강도를 트리거 키워드로 압축하는 프레임

## 9. 기존 사례에는 강했지만 이번 사례에서는 약한 프레임
- ontology 직접 프레임
- semantic interoperability / data fabric 직접 프레임
- grounding + symbolic layer 직접 프레임
- 시장/벤더 전략 전체를 다루는 시황성 프레임

## 10. refinement trigger 현재 상태
- status: `watch`
- reason:
  - 외부 사례가 3건으로 늘었고 outer/defer 분리 패턴과 agentic workflow 반복은 더 또렷해졌다.
  - 그래도 아직 refinement를 성급히 열기보다 한 건 더 보거나, 지금까지의 outer 후보 중 하나를 정련 패스 후보로 좁히는 단계가 맞다.

## 11. 다음 액션 힌트
- 4번째 외부 사례 1건을 더 넣어 반복성을 더 본다.
- 아니면 지금까지 나온 outer 후보들 중 하나를 골라 정련 패스 후보 1건을 만든다.
