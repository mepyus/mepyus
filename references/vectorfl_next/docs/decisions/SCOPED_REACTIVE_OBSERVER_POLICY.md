# Scoped Reactive Observer Policy

## Decision

reactive observer는 recent window와 family scope로 잘라 읽을 수 있어야 한다.

## Current rule

- `recent_limit`을 주면 가장 최근 reaction event만 읽는다.
- `family_id`를 주면 해당 family material을 포함한 cell만 읽는다.
- `session_id`를 주면 해당 session material을 포함한 cell만 읽는다.
- scope들은 함께 사용할 수 있다.

## Why

- 전체 총량만으로는 현재 움직임을 세밀하게 읽기 어렵다.
- family scope를 보면 특정 material family가 공간을 어떻게 흔드는지 볼 수 있다.

## Follow-up risk

- 아직 duration-based recent window는 없다.
- 다음 단계에서 시간 길이 기준 recent observation을 추가할 수 있다.
