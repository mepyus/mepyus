# First Convergence Policy

첫 convergence는 weak trace terrain과 fresh pressure terrain이 처음 만나는 최소 `candidate space cell`만 허용한다.

현재 허용 조건:

- `observer_reflection` trace가 이미 있어야 한다.
- `fresh_pressure_hint` trace와 그에 연결된 `point_seed`가 이미 있어야 한다.
- preexisting `space_cell`은 없어야 한다.

초기 convergence 구조:

- `fresh_material`과 `observer_material`을 cell interior 쪽으로 둔다.
- `engine_self_material`은 아직 exterior 쪽에 둔다.
- `observer_reflection` trace도 exterior boundary 쪽에 남겨 완전한 흡수를 막는다.
- pressure는 fresh seed가 가진 profile을 그대로 사용한다.

의도:

- fresh pressure terrain이 weak relation terrain과 만나되, engine-self 전체가 즉시 안쪽으로 접히지 않게 한다.
- 첫 cell은 convergence proof이지 안정 공간 선언이 아니다.

금지 기준:

- 첫 convergence 하나로 stable local을 선언하지 않는다.
- 첫 convergence에서 local space나 bridge를 자동 생성하지 않는다.
- weak trace terrain 전체를 interior로 흡수해 early closure를 만들지 않는다.
