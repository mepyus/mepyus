# Initial Pressure Seed Policy

`fresh_material`은 기존 weak trace에 바로 접지 않고, 첫 pressure-bearing input으로 별도 seed 경로를 연다.

잠금 기준:

- `fresh_material`은 자기 material ref만 가진 trace를 먼저 만든다.
- 그 trace는 `evidence_kind=fresh_pressure_hint`로 기록한다.
- pressure profile은 fresh material과 그 trace를 support로 가진다.
- 첫 seed는 `point_seed`까지만 열고 `space_cell`로 자동 승격하지 않는다.

의도:

- fresh input이 기존 engine-self / observer relation에 종속되지 않게 한다.
- 공간 우선 기준 아래에서 fresh material이 별도 압력 경로를 갖도록 한다.

금지 기준:

- fresh material을 첫 weak trace에 바로 병합하지 않는다.
- 첫 pressure-bearing input 하나로 stable cell이나 stable local을 선언하지 않는다.
- fresh seed를 point closure처럼 읽지 않는다.
