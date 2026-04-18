[[A]] [[OBJ:codex_directive]] [[SEM:negative_control_external_case_selection_criteria_v1]]

# negative_control_external_case_selection_criteria_v1

## purpose
- next negative control test용 파일을 지금 당장 실행하지 않고, 선택 기준을 먼저 고정한다.
- `claude_code_index.txt`와 `graphrag_neosh.txt` 중 어떤 파일이 transformer same-topic frame의 false generalization 여부를 보기 더 적절한지 판단한다.

## selection rule
- transformer와 충분한 주제 거리가 있어야 한다.
- 그래도 기술 설명형 구조가 살아 있어야 한다.
- rhetoric을 걷어낸 뒤에도 비교 가능한 설명 흐름이 남아야 한다.
- bounded test 1회로 다룰 수 있는 길이여야 한다.
- 독립 canonical input으로 처리하기 쉬워야 한다.

## current repo note
- 현재 `inputs/external_cases/claude_code_index.txt`는 존재하며 코드 에이전트 운용/프로젝트 컨텍스트 정리 설명 자료로 읽힌다.
- 현재 `inputs/external_cases/graphrag_neosh.txt`는 존재하며 graph / retrieval / architecture 설명형 자료로 읽힌다.
