# Ambiguity Checklist

아래 질문에 즉답이 안 되면 설계를 멈추고 문서화한다.

## Object boundary

- 이것이 `trace`인가, 아니면 `bridge_trace`인가
- 이것이 `point_seed`인가, 아니면 이미 `space_cell`인가
- 이것이 `local_space`인가, 아니면 여러 cell의 느슨한 모음인가

## Pressure handling

- 이 변화는 새 필드 추가로 끝나는가
- 아니면 실제 formation path를 바꿔야 하는가
- support refs와 strength hint로 표현 가능한가

## Reentry handling

- 같은 family의 material이 재진입했을 때 기존 구조를 덮어쓰는가
- 아니면 새로운 seed/cell 경로를 열 수 있는가

## Review action

- 애매한 경계는 `docs/decisions/`에 기록
- 구현은 그 다음
