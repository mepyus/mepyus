# Boundary Case Calibration Loop v0.1

목적:
- `scene / role / score`를 전체 문서가 아니라 경계 사례 세트로 제련한다.
- 문서 전체 재독해보다 빠르게 drift를 찾고 줄이기 위한 운영 절차다.

## 1. 왜 이 방식을 쓰는가

현재 병목은 입력기보다 라벨기와 축값이다.

즉 문제는:
- 어디서 자르느냐보다
- 그 조각을 무엇으로 읽느냐
- 얼마나 확신하느냐

따라서 calibration은
전체 문서를 계속 읽는 방식보다
의도적으로 갈리게 만든 경계 사례 세트를 돌리는 쪽이 더 빠르다.

## 2. Loop 개요

1. ChatGPT 또는 Gemini에게 boundary case를 생성시킨다.
2. 생성된 case_text를 Codex / ChatGPT / Gemini에 같은 schema로 라벨링시킨다.
3. scene / role / score만 따로 비교한다.
4. 어디서 갈렸는지 판정 질문으로 다시 읽는다.
5. 작은 decision rule을 수정한다.
6. 같은 세트 또는 후속 세트로 재실험한다.

## 3. 우선순위

첫 루프는 아래 순서로 돈다.

1. scene
2. role
3. confidence / ambiguity
4. stability

direction / intensity는 후순위 보조 신호로 읽는다.

## 4. 추천 경계 세트

### scene

- explanation_vs_reflection
- explanation_vs_evidence
- explanation_vs_comparison

### role

- thesis_vs_expansion
- support_vs_example
- contrast_vs_expansion
- problem_vs_support

### score

- confidence_vs_ambiguity
- stability_vs_mixed

## 5. 판정 질문 방식

비교할 때는 처리자 이름보다 아래 질문을 먼저 본다.

- 이 문단은 실제로 설명인가, 반성인가?
- 이 문단은 일반 주장을 세우는가, 해석을 확장하는가?
- 이 문단은 예시인가, 단순 뒷받침인가?
- ambiguity를 0.05까지 닫아도 되는가?
- fragment가 혼합적인데 stability를 높게 준 이유가 있는가?

즉 `모델 비교`보다 `판정 질문`을 우선한다.

## 6. 리포트 방식

boundary case 리포트는 아래 순서로 본다.

1. boundary_pair
2. processor별 scene
3. processor별 role
4. confidence / ambiguity
5. stability
6. drift 요약
7. decision rule 수정 후보

## 7. 잠금 문장

라벨기 제련은 긴 문서를 다시 읽는 작업이 아니라,
갈릴 수밖에 없는 작은 경계 사례를 반복 비교하면서
작은 판정 규칙을 조정하는 작업이다.
