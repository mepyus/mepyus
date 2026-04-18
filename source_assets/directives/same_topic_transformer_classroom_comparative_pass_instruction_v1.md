[[A]] [[OBJ:codex_directive]] [[SEM:same_topic_transformer_classroom_comparative_pass_instruction_v1]]

# same_topic_transformer_classroom_comparative_pass_instruction_v1

## purpose
- `choi_ai_classroom_transformer1.txt`와 `choi_ai_classroom_transformer2.txt`를 독립 canonical input으로 유지한 채 comparative pass를 수행한다.
- repeated explanatory outer frame, case-specific emphasis, defer-worthy simplification만 얇게 판독한다.
- current는 유지하고, delta는 필요 시 짧게만 반영한다.

## canonical inputs
- [choi_ai_classroom_transformer1.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/choi_ai_classroom_transformer1.txt)
- [choi_ai_classroom_transformer2.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/choi_ai_classroom_transformer2.txt)

## operating rule
- 두 문서를 합쳐 새 source를 만들지 않는다.
- comparative doc는 report/example일 뿐 source를 대체하지 않는다.
- 이번 턴에서는 refinement value만 얇게 보고, core promotion은 열지 않는다.
