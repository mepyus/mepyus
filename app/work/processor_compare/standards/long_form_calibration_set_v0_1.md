# Long Form Calibration Set v0.1

목적:
- 장문 설명문과 장문 기술문에서 입력기/라벨기 drift를 점검하기 위한 calibration 문서 세트를 정의한다.
- 현재 기준 세트는 `doc_005`, `doc_006`이다.

## 1. 문서 구성

### doc_005
- 성격: 블로그형 장문 설명문
- 핵심 축:
  - 팔란티어 온톨로지 요약
  - 디지털 트윈 정의
  - 객체/관계/행동 예시
  - 데이터 사일로 문제
  - Object / Property / Link / Action
  - 운영 자동화 결론

주요 calibration 포인트:
- 요약/정의 경계
- 문제/해법 경계
- Link 메커니즘/가치 경계
- 결론의 thesis vs meta 판정

### doc_006
- 성격: 구조가 분명한 장문 기술 설명문
- 핵심 축:
  - Vector RAG 한계
  - Graph DB 정의
  - Graph RAG 정의
  - 아키텍처 단계
  - multi-hop 비교 예시
  - 활용 사례
  - 기술 과제
  - 결론 전망

주요 calibration 포인트:
- Graph DB / Graph RAG 분리 여부
- 구축 단계 / 질의 단계 분리 여부
- 비교 예시 / 파이프라인 설명 경계
- 과정 서술을 scene으로 잘못 보내는지 여부

## 2. 처리자별 관찰 패턴

### Codex
- 장문에서도 중간 granularity를 유지한다
- 구조 분리를 비교적 안정적으로 보존한다
- 결론을 thesis로 두되 과도한 meta화는 적다

### ChatGPT
- 블로그형 장문(`doc_005`)에서는 과세분화가 두드러진다
- 구조가 분명한 기술 장문(`doc_006`)에서는 Codex와 유사한 granularity로 수렴한다
- 높은 confidence, 낮은 ambiguity 경향은 장문에서도 유지된다
- scene schema 오용은 여전히 반복된다

### Gemini
- 두 장문 모두에서 큰 의미 블록으로 묶는 경향이 강하다
- `doc_005`에서는 상위 추상화와 meta 해석 증가
- `doc_006`에서는 과정 설명을 `scene=process`로 보내는 drift가 발생

## 3. 운영 규칙

장문 문서를 비교할 때 아래 순서를 기본으로 한다.

1. fragment count 비교
2. 평균 score 비교
3. 대표 boundary pattern 비교
- summary_definition_boundary_candidate
- problem_solution_boundary_candidate
- mechanism_value_boundary_candidate
4. scene schema drift 확인
5. meta_overreach_candidate 확인
6. oversegmentation_candidate / overmerged_candidate 확인

## 4. 판정 기대값

현재 기준에서 장문 문서 비교 시 기대되는 이상적인 중간값은 다음과 같다.

- Codex 수준의 중간 granularity
- scene은 explanation/comparison/evidence 중심
- role은 definition/problem/example/thesis/bridge/expansion을 기능대로 분리
- 높은 confidence는 근거가 명확한 정의/구조 설명에서만 허용
- 장문 결론이라고 해서 자동으로 reflection/meta로 올리지 않음

## 5. 재실행 기준

아래 중 하나를 바꾸면 `doc_005`, `doc_006`을 반드시 다시 돌린다.

- fragment 절단 규칙
- scene/role 기준
- score 가이드
- anchor normalization 규칙
- compare 분류 기준

## 6. 잠금 문장

`doc_005`는 장문 블로그형 calibration 문서다.
`doc_006`은 장문 기술형 calibration 문서다.
둘을 함께 돌려야 장문 문서에서의 과세분화, 대묶음, scene drift, meta overreach를 동시에 점검할 수 있다.
