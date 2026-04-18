[[A]] [[OBJ:codex_directive]] [[SEM:graphrag_neosh_negative_control_pass_instruction_v1]]

# graphrag_neosh_negative_control_pass_instruction_v1

## purpose
- `graphrag_neosh.txt`를 negative control external case로 읽어, transformer classroom frame의 false generalization 가능성을 bounded하게 점검한다.
- transformer source identity를 건드리지 않고, repeated explanatory frame이 기술 설명 일반 frame인지 아닌지만 얇게 확인한다.
- current는 유지하고, delta는 실행 사실만 짧게 남긴다.

## canonical input
- [graphrag_neosh.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/graphrag_neosh.txt)

## operating rule
- negative control doc는 source를 대체하지 않는다.
- 이번 턴은 승격이 아니라 false generalization check다.
- 결과는 repeated frame persistence / drift / partial overlap 정도로만 남긴다.
