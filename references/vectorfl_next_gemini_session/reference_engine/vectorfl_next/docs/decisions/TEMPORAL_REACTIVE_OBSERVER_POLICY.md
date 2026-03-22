# Temporal Reactive Observer Policy

## Decision

reactive observer는 총량만이 아니라 반응 시퀀스와 pressure signature spread도 읽을 수 있어야 한다.

## Current rule

- `space_cell_reacted` 이벤트를 시간 순서로 요약한다.
- 각 반응 이벤트가 어떤 pressure signature 아래 일어났는지 센다.
- 이는 코어를 바꾸지 않고 읽기 전용으로 제공한다.

## Why

- 공간은 총량만이 아니라 변화 순서에서도 읽혀야 한다.
- pressure spread를 보면 같은 reaction이라도 어떤 압력장에서 나타나는지 볼 수 있다.

## Follow-up risk

- 아직 time window slicing은 없다.
- 다음 단계에서 recent-only observation 또는 session-specific observation이 가능해질 수 있다.
