# Boundary Case Request Template v1

경계 사례를 만들 때 아래 형식을 사용한다.

```text
다음 boundary case 세트를 만들어라.

총 개수: 30

분포:
- explanation_vs_reflection: 5
- explanation_vs_evidence: 4
- explanation_vs_comparison: 3
- thesis_vs_expansion: 4
- support_vs_example: 4
- contrast_vs_expansion: 3
- problem_vs_support: 3
- confidence_vs_ambiguity: 2
- stability_vs_mixed: 2

문체 제약:
- 설명문 / 비평문 / 회고문 / 대화문이 고르게 섞이게 할 것
- 특정 도메인만 반복하지 말 것
- 실제 문서 조각처럼 자연스럽게 쓸 것
```

권장 순서:

1. `standards/boundary_case_generation_prompt_v1.md`
2. 위 요청 블록

생성 결과 저장 권장 위치:

- `inputs/boundary_cases/raw_generations/chatgpt/`
- `inputs/boundary_cases/raw_generations/gemini/`

라벨링용으로 정리한 최종 세트 저장 권장 위치:

- `inputs/boundary_cases/final_sets/`
