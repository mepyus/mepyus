# line_thickening_primary_material_breadth_note_v0

## purpose

- 이번 note의 목적은 new route를 더 붙이는 것이 아니라, 이미 연결된 두 primary route 위에서 `distinct_primary_material_anchor_count`가 실제로 넓어지는지 검증하는 것이다.

## why breadth validation now

- `path diversity`는 이미 열려 있다.
- 하지만 strong line이 same-material multi-path illusion인지, broader primary material line인지 아직 따로 확인해야 한다.
- 그래서 지금은:
  - `internal_observer`
  - `source_fragment_view`
  두 route만 다시 사용한다.

## reading rule

- same material across multiple paths:
  - `cross-path`는 맞다
  - `cross-material`은 아니다

- distinct primary materials across one or more primary routes:
  - 이것이 실제 breadth 후보다

## cohort rule

- small cohort만 사용한다.
- 이번 검증은 아래를 섞는다.
  - same document, different fragment
  - different document, pointer-bearing fragment
  - already-known anchor control

## line expectations

- `transition_over_surface`
  - contrast/direct-span 기반 strong line
  - 하지만 current primary material ceiling이 낮을 수 있다

- `input_to_reading_organ`
  - observer route 안에서 여러 primary material anchors에 걸쳐 나올 수 있다
  - 따라서 route는 좁아도 material breadth는 더 넓을 수 있다

- `pre_read_eye`, `raw_return_preservation`
  - summary line으로 남아야 한다
