# Session Timeline Policy

## Decision

session scope가 있을 때는 compact session timeline을 읽을 수 있어야 한다.

## Current rule

- session에 속한 reaction sequence를 시간 순서로 짧게 나열한다.
- reaction counts와 pressure signature spread를 함께 보여준다.
- 이는 observer 출력의 일부이며 코어를 바꾸지 않는다.

## Why

- 같은 세션 안에서 공간이 어떻게 두꺼워지고 이동했는지 한 번에 읽는 것이 중요하다.
- session timeline은 작업 흐름 감각을 복구하는 데 유용하다.

## Follow-up risk

- 아직 session timeline은 compact list 수준이다.
- 다음 단계에서 timeline compression이나 phase labeling을 추가할 수 있다.
