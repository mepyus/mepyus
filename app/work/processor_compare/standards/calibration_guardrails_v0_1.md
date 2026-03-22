# Calibration Guardrails v0.1

목적:
- 입력기(fragment boundary), 라벨기(scene/role), 점수(score), anchor/tag 판정을 실제 작업에 바로 적용할 수 있도록 구체 규칙을 제공한다.
- `doc_001`부터 `doc_006`까지의 비교 결과, 특히 `doc_005`, `doc_006`에서 반복적으로 드러난 편향을 보정하기 위한 운영 문서다.

이 문서는 방향 문서가 아니라 실행 문서다.
즉 비교/분석/문서화 시 아래 규칙을 실제 판정 기준으로 사용한다.

## 1. 입력기 Guardrail

핵심 원칙:
- fragment는 "짧은 조각"이 아니라 "비교 가능한 하나의 로컬 의미 움직임"이어야 한다.
- 문장 수보다 의미축 수를 우선 본다.
- 한 fragment 안에 주축이 2개 이상 강하게 섞이면 분리 후보로 본다.
- 너무 잘게 잘라 evidence_text만 남고 의미가 사라지면 실패한 절단이다.

### 1.1 분리 신호

아래 신호가 2개 이상 동시에 보이면 분리 후보로 우선 판정한다.

- 문단 기능이 바뀐다.
  예: 정의 -> 사례, 문제 -> 해법, 메커니즘 -> 가치
- 서술 모드가 바뀐다.
  예: 설명 -> 비교, 설명 -> 질문, 설명 -> 반성
- 핵심 명사가 바뀐다.
  예: `Graph DB` 중심 -> `Graph RAG` 중심
- 논리 연결어가 강한 전환을 만든다.
  예: `그러나`, `반면`, `나아가`, `예를 들어`, `이처럼`, `즉`
- 새로운 독립 질의가 열린다.
  예: "왜 필요한가?", "어떻게 동작하는가?", "실제로 어디에 쓰이는가?"

### 1.2 통합 신호

아래 신호가 강하면 하나의 fragment로 유지한다.

- 하나의 개념을 바로 이어 설명한다.
- 사례가 직전 정의의 즉시 설명 역할만 한다.
- 전환 문장이 있더라도 의미축이 바뀌지 않는다.
- 분리하면 근거 구절만 남고 설명 단위가 사라진다.

### 1.3 대표 Boundary Pattern

#### A. 요약/도입 vs 정의

기본 규칙:
- 도입/요약과 명시적 정의는 기본적으로 분리 후보다.

분리 조건:
- 도입이 "왜 이 주제를 말하는가"를 설명하고
- 다음 구간이 "그것이 무엇인가"를 직접 정의할 때

통합 조건:
- 도입이 사실상 정의의 쉬운 말 재진술일 때

비고:
- `doc_005`, `doc_006` 모두에서 Gemini가 이 둘을 더 쉽게 합친다.
- 이 경우 Codex는 우선 분리 후보로 본다.

#### B. 문제 제기 vs 해법 진술

기본 규칙:
- 문제와 해법은 논리 기능이 다르므로 분리 후보다.

분리 조건:
- 문제 서술이 3문장 이상 독립적으로 지속될 때
- 해법이 새로운 가치 주장으로 전환될 때

통합 조건:
- 문제 직후 1~2문장으로 해법이 바로 귀결될 때
- 문제와 해법이 하나의 반문 구조 안에 묶여 있을 때

리포트 신호:
- `problem_solution_boundary_candidate`

#### C. 메커니즘 vs 가치/활용

기본 규칙:
- "어떻게 구현되는가"와 "왜 중요한가"는 분리 후보다.

분리 조건:
- 구현 방식 나열 후 활용/가치/AI reasoning 설명이 이어질 때
- 기술 설명이 독립적으로 3문장 이상 지속될 때

통합 조건:
- 구현과 가치가 짧은 한 문단 안에서 inseparable하게 붙어 있을 때

리포트 신호:
- `mechanism_value_boundary_candidate`

#### D. 과정 서술 vs 장면 판정

기본 규칙:
- 과정 설명은 별도 scene이 아니라 `scene=explanation` 안에서 처리한다.

주의:
- `process`는 scene이 아니다.
- Gemini가 `scene=process`로 가는 경향은 schema drift로 기록한다.

리포트 신호:
- `scene_schema_violation`

## 2. Scene/Role Guardrail

핵심 원칙:
- scene과 role은 다른 축이다.
- scene은 "서술 모드", role은 "논리 기능"이다.
- role 값을 scene으로 쓰지 않는다.

### 2.1 Scene 빠른 판정

`explanation`
- 기본값이다.
- 정의, 사례, 문제, 해법, 메커니즘, 결론 대부분은 우선 explanation 후보로 본다.

`comparison`
- 둘 이상의 접근법/방법/대상을 직접 대비할 때만 쓴다.
- `doc_006`의 Vector RAG vs Graph RAG 파트처럼 비교 구조가 명시적일 때

`evidence`
- 구체 사례, 결과, 실험, 처리 결과, 확인된 근거를 보여줄 때
- 단순 예시 소개와는 구별한다.

`reflection`
- 문서가 한 단계 위에서 자기 해석/한계/전망/메타 총평을 할 때만 허용
- 결론이라고 자동으로 reflection으로 가지 않는다

`instruction`
- 실제 수행 순서, 절차, 사용법, 명령형 안내가 중심일 때만 쓴다
- 기술 파이프라인 설명은 우선 explanation으로 본다

`discovery`
- 새로운 발견, 드러남, 깨달음, 뜻밖의 연결을 강조할 때만 제한적으로 사용

`question`
- 질문이 장면의 중심일 때만 사용

`transition`
- 독립 정보보다 전환 문장 자체가 기능할 때만 사용

`unknown`
- 어떤 장면으로도 명확히 판정하기 어려울 때만 사용

### 2.2 Role 빠른 판정

`definition`
- 개념, 구조, 용어를 직접 규정할 때

`example`
- 사례, 예시, illustration가 중심일 때

`problem`
- 한계, 어려움, 부담, 실패, 제약을 제시할 때

`thesis`
- 핵심 주장, 결론, 글의 중심 메시지를 직접 세울 때

`support`
- 앞선 정의/주장/구조를 보강할 때

`bridge`
- 다음 섹션으로 전환하면서 비교/개요/연결을 열 때

`expansion`
- 기존 설명을 확장, 응용, 활용, 전망 쪽으로 넓힐 때

`meta`
- 텍스트 내용보다 텍스트의 관점/틀/해석 수준을 다룰 때만 사용

### 2.3 강제 매핑

- 정의 설명 문단:
  `scene=explanation`, `role=definition`
- 사례 문단:
  `scene=explanation`, `role=example`
- 문제 제기 문단:
  `scene=explanation`, `role=problem`
- 결론/핵심 주장:
  `scene=explanation`, `role=thesis`
- 비교 도입/전환:
  `scene=comparison` 또는 `scene=explanation`, `role=bridge`
- 진짜 메타 총평:
  `scene=reflection`, `role=meta`

### 2.4 금지 패턴

- `scene=definition`
- `scene=example`
- `scene=process`
- `scene=thesis`
- `scene=support`

이 값들은 모두 schema violation로 기록한다.

## 3. Score Guardrail

핵심 원칙:
- 높은 점수는 좋은 점수가 아니라 "강한 판정"이다.
- 낮은 ambiguity는 좋은 것이 아니라 "해석을 빨리 닫은 것"일 수 있다.

### 3.1 direction

높여야 할 때:
- 중심 주장이 명확하다
- 전개가 한 방향으로 밀린다

낮춰야 할 때:
- 정의/사례/비교/결론이 한 fragment에 섞여 있다
- 의미축이 두 개 이상 경쟁한다

### 3.2 intensity

높여야 할 때:
- 개념 밀도와 정보 압축도가 높다
- 핵심 표현이 응집되어 있다

낮춰야 할 때:
- 단순 나열이 많다
- 개요 문단이 길지만 밀도는 낮다

### 3.3 stability

높여야 할 때:
- 내부 의미가 한 방향으로 유지된다

낮춰야 할 때:
- 전환 문장, 사례, 메타 해석이 한 덩어리에 섞여 있다
- 처리자가 크게 묶으면서도 성격이 다른 문단을 합쳤다

주의:
- Gemini는 큰 덩어리로 묶고도 stability를 높게 주는 경향이 있다.
- 이 경우 "대묶음에 의한 과대 stability" 가능성을 검토한다.

### 3.4 confidence

낮춰야 할 때:
- 절단이 과감했다
- scene/role 경계가 애매하다
- anchor가 지나치게 추상적이다

주의:
- ChatGPT는 과세분화와 함께 confidence를 높게 주는 경향이 있다.
- 높은 confidence가 calibration 기준에서는 오히려 drift 신호일 수 있다.

### 3.5 ambiguity

높여야 할 때:
- 문제/해법 경계가 짧게 붙어 있다
- 메커니즘/가치가 섞여 있다
- 결론이 thesis인지 meta인지 애매하다

낮춰야 할 때:
- 정의가 직접적이고 기능이 명확하다

주의:
- ChatGPT와 Gemini는 ambiguity를 너무 낮게 주는 경향이 반복됐다.
- 장문 설명문이라고 ambiguity를 자동으로 낮추지 않는다.

## 4. Anchor/Tag Guardrail

### 4.1 Anchor 수

- 기본 1~3개
- 4개 이상은 과증식 후보로 본다

### 4.2 과세분화 신호

- 거의 같은 상위 개념을 다른 이름으로 반복 anchor화
- 해법, 결론, 가치 진술을 각각 따로 미세 anchor로 승격

예:
- `integration_reduction`
- `tool_framework_interoperability`
- `mcp_standard_protocol`

이 셋이 모두 독립 핵심 anchor인지 재검토한다.

### 4.3 과대추상화 신호

- 원문에 있는 중요한 중간 손잡이가 사라진다
- 너무 큰 상위 개념 하나로 덮는다

예:
- `reality_decomposition`
- `ontology_centric_system`
- `digital_twin_reflection`

이 경우 원문 수준의 구조 손잡이가 사라졌는지 확인한다.

### 4.4 Tag 원칙

- semantic_tags = 무엇을 말하는가
- structural_tags = 어떻게 작동하는가 / 어떤 위치를 차지하는가

금지:
- 장문형 태그
- 문장 자체를 태그화
- scene/role 값을 그대로 태그로 반복

## 5. 처리자별 보정 프롬프트 해석

### ChatGPT

주요 위험:
- 과세분화
- 높은 confidence
- scene enum 오용

보정 포인트:
- definition/example는 role로 보내고 scene은 explanation에 남긴다
- 결론을 너무 빨리 thesis로 세우는지 확인한다

### Gemini

주요 위험:
- 대묶음
- 추상화 확대
- meta/reflection 과사용
- 비표준 scene 생성

보정 포인트:
- 과정 설명은 scene=explanation으로 유지한다
- 결론이 실제 meta인지 thesis인지 재판정한다

### Codex

목표:
- 중간 granularity 유지
- 구조적 분해 유지
- 점수는 보수적으로
- anchor는 중간 granularity 유지

## 6. 리포트 작성 체크리스트

문서 하나를 비교할 때 아래를 반드시 기록한다.

1. fragment count 차이
2. 평균 점수 차이
3. 요약/정의 경계 차이
4. 문제/해법 경계 차이
5. 메커니즘/가치 경계 차이
6. scene schema violation 유무
7. meta_overreach 유무
8. anchor granularity 차이
9. calibration 포인트 1줄

## 7. 기본 리포트 신호명

- `summary_definition_boundary_candidate`
- `problem_solution_boundary_candidate`
- `mechanism_value_boundary_candidate`
- `scene_schema_violation`
- `meta_overreach_candidate`
- `oversegmentation_candidate`
- `overmerged_candidate`
- `mid_granularity_candidate`
