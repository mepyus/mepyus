[[A]] [[OBJ:codex_directive]] [[SEM:same_topic_external_case_input_transformer_classroom_batch_instruction_v1]]

# same_topic_external_case_input_transformer_classroom_batch_instruction_v1

## purpose
- `choi_ai_classroom_transformer1.txt`와 `choi_ai_classroom_transformer2.txt`를 각각 독립 canonical input으로 intake한다.
- source / derived / report / evidence 경계를 유지한 채 bounded intake batch를 닫는다.
- current는 기본적으로 유지하고, delta는 필요 시 짧게만 갱신한다.

## canonical inputs
- [choi_ai_classroom_transformer1.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/choi_ai_classroom_transformer1.txt)
- [choi_ai_classroom_transformer2.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/choi_ai_classroom_transformer2.txt)

## operating rule
- 두 txt는 같은 주제라도 서로를 대체하지 않는다.
- first-pass/example 문서는 source를 대체하지 않는다.
- batch report는 intake 결과 요약일 뿐 기준선이 아니다.
