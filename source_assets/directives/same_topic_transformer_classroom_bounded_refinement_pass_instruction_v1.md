[[A]] [[OBJ:codex_directive]] [[SEM:same_topic_transformer_classroom_bounded_refinement_pass_instruction_v1]]

# same_topic_transformer_classroom_bounded_refinement_pass_instruction_v1

## purpose
- transformer classroom comparative 결과를 승격 없이 refinement candidate 수준으로만 재정리한다.
- repeated frame / emphasis split / defer bucket을 더 짧고 선명하게 정리한다.
- current는 유지하고, delta는 실행 사실만 짧게 남긴다.

## canonical inputs
- [choi_ai_classroom_transformer1.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/choi_ai_classroom_transformer1.txt)
- [choi_ai_classroom_transformer2.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/choi_ai_classroom_transformer2.txt)

## operating rule
- repeated frame candidate는 refined되지만 승격되지 않는다.
- emphasis split은 sub-axis candidate로만 남긴다.
- teaching convenience / presenter-style rhetoric는 defer bucket으로 남긴다.
