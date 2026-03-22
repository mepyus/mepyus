# Space Cell Spec

`space_cell`은 pressure profile 아래 함께 유지되는 material, trace, seed를 보존하는 최소 반응 공간이다.

핵심 잠금 문장:

- 살아 있는 `space_cell`은 재등장과 압력 변화에 따라 내부 결속, 경계, 재배치 방식이 달라질 수 있는 최소 반응 공간이다.
- 죽은 `space_cell`은 material, trace, seed를 보유하더라도 재등장과 압력 변화가 구조 변화로 이어지지 않는 정적 보관 단위다.

필수 요소:

- `material_refs`
- `trace_refs`
- `seed_refs`
- `pressure_profile_id`
- `boundary`
- `state`
- `cohesion_note`

`boundary`는 아래를 가진다.

- `interior_refs`
- `exterior_refs`
- `permeability_hint`

살아 있는 cell의 최소 반응:

- `thickening`: recurrence, cohesion, trace layer, boundary 선명도가 증가한다.
- `split`: 내부 긴장 증가로 하나의 cell로 유지되기 어려워지고 내부 경계가 생긴다.
- `relocation`: 재등장 material 또는 seed가 기존 cell의 주 결속에서 실질적으로 이탈해 다른 cell 경로나 다른 local space 가능성으로 이동한다.

죽은 cell 판정 신호:

- 재등장해도 항상 같은 seed/cell로만 귀속된다.
- pressure가 저장만 되고 형성 경로를 바꾸지 못한다.
- boundary evidence가 거의 늘지 않는다.
- reader 없이는 변화 흔적이 잘 보이지 않는다.

살아 있는 cell 판정 신호:

- 재등장이 `thickening`, `split`, `relocation` 중 하나를 유발한다.
- pressure 변화가 trace, seed, cell 형성 경로에 실제 영향을 준다.
- boundary evidence와 state transition이 append-only로 남는다.
- 새로운 bridge candidate 또는 local space variation 가능성이 생긴다.

금지:

- cluster candidate로 재해석하는 것
- promoted point의 약한 버전으로 다루는 것
- bridge 생성과 동시에 merge시키는 것
