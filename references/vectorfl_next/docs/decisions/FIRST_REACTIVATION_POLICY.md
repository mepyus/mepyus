# First Reactivation Policy

첫 reactivation은 second fresh reentry가 기존 pressure continuity 안에 남아 있을 때만 `thickening`으로 허용한다.

현재 허용 조건:

- 첫 candidate `space_cell`이 이미 하나 존재해야 한다.
- `fresh_material` family에 대한 재유입 material이 새로 들어와야 한다.
- 새 pressure profile은 기존 cell의 pressure signature를 그대로 따라야 한다.

초기 reactivation 구조:

- 재유입 fresh는 새로운 material, trace, pressure, reentry seed를 갖는다.
- candidate cell은 family match를 통해 새 seed와 trace를 흡수할 수 있다.
- 반응은 `thickening`만 허용한다.
- `split`과 `relocation`은 아직 금지한다.

의도:

- 첫 convergence cell이 재유입 아래 실제로 살아 있는지 확인한다.
- 동일 pressure continuity를 먼저 두껍게 읽고, 더 복잡한 분기는 나중으로 미룬다.

금지 기준:

- 첫 reactivation에서 local space를 자동 생성하지 않는다.
- 첫 reactivation에서 split이나 relocation으로 바로 넘어가지 않는다.
- reentry 하나로 stable local을 선언하지 않는다.
