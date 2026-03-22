# Initial Trace Policy

첫 trace는 공간을 닫기 위한 판정이 아니라, 초기 material 사이의 약한 관계를 기록하는 데 목적이 있다.

현재 첫 trace는 아래 두 formation role 사이에서만 연다.

- `engine_self_material`
- `observer_material`

잠금 기준:

- 첫 trace는 `evidence_kind=observer_reflection`으로 기록한다.
- support는 material ref만 사용하고, reader 해석어를 core ontology로 올리지 않는다.
- 첫 trace는 seed, cell, local space로 자동 승격하지 않는다.

의도:

- engine 자기기록과 observer 요약 사이의 약한 반사 관계를 남긴다.
- 첫 relation을 공간 바깥 해석이 아니라 코어 append-only 기록으로 확보한다.

금지 기준:

- 첫 trace를 point 승격의 전처리처럼 다루지 않는다.
- 첫 trace 하나로 stable relation이나 canonical linkage를 선언하지 않는다.
