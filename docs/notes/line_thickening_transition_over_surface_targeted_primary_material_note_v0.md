# line thickening transition_over_surface targeted primary material note v0

## Purpose

이번 턴의 목적은 `transition_over_surface` 한 line만 대상으로,
새 route를 더 붙이지 않고 기존 primary routes 안에서
`distinct_primary_material_anchor_count`가 실제로 늘어나는지 확인하는 것이다.

핵심은 `same-material multi-path`가 아니라
`new primary materials`가 들어오는지를 보는 데 있다.

## Why This Cohort

현재 `transition_over_surface`의 known primary materials는 아래 둘이다.

- `frag_basic3_002`
- `frag_basic4_003`

이번에는 아래처럼 좁게 본다.

- control
  - `frag_basic3_002`
- new primary materials
  - `frag_basic_004`
  - `frag_basic3_004`
  - `frag_ytex_003`

## Reading Rule

- observer route는 current direct-span control만 유지한다
- breadth 확장은 `source_fragment_view`의 pointer-bearing primary rows로만 본다
- 같은 fragment를 다른 path가 다시 본 것은 breadth 증가가 아니다
- 새로운 `fragment_id`가 들어올 때만 primary material breadth 증가로 읽는다

## Intended Read

이번 턴의 성공은 아래 둘 중 하나다.

- `distinct_primary_material_anchor_count`가 실제로 증가한다
- 또는 증가하지 않더라도, 왜 증가하지 않았는지 정직하게 드러난다

중요:

- `balanced_broadening_candidate`를 억지로 만들지 않는다
- `transition_over_surface`만 읽는다
