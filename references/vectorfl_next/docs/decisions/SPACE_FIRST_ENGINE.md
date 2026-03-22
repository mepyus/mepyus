# Space-First Engine

## Decision

`vectorfl_next`는 점을 만들어 공간을 설명하는 엔진이 아니라, 공간을 먼저 형성하고 그 안에 관찰 입자를 두어 반응을 확인하는 엔진으로 간다.

## Agreement

- `vectorfl`는 실패 패턴을 읽는 frozen reference로만 쓴다.
- 새 엔진은 앞단 수렴보다 공간 형성을 우선한다.
- 점은 코어를 닫는 단위가 아니라 관찰 도구다.
- 구현 우선순위는 `space_cell`, `local_space`, `bridge_trace` 반응 규칙이다.

## Why

- 기존 실패는 candidate, point, cluster 쪽으로 너무 빨리 닫히는 중력에서 반복되었다.
- 공간을 먼저 세우면 점은 판정 중심이 아니라 실험 도구가 된다.
- 이 방식이 formation-first와 anti-collapse를 함께 지킨다.

## Immediate implication

- 다음 구현은 point promotion이 아니라 `space_cell reaction spec`과 `local space criteria` 강화로 간다.
- probe는 `docs/probes/SPACE_FIRST_PROBING.md` 기준 아래에서만 사용한다.
