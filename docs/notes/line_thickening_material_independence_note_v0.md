# line_thickening_material_independence_note_v0

## purpose

- 이번 note의 목적은 route diversity 와 material diversity 를 분리하는 것이다.
- 같은 line이 여러 validation path에서 다시 보이더라도, 그 path들이 같은 fragment/material slice를 다시 읽고 있다면 그것은 cross-path corroboration이지 cross-material corroboration은 아니다.

## why the split is needed

- `internal_observer`와 `source_fragment_view`는 genuinely different path다.
- 하지만 둘 다 `frag_basic3_002`, `frag_basic4_003` 같은 같은 fragment anchor를 다시 볼 수 있다.
- 따라서 `distinct_independent_evidence_count=2`만 보면 primary route는 둘이지만, material breadth까지 둘이라고 읽으면 과장일 수 있다.

## material anchor rule

- material anchor는 아래 순서로 잡는다.
  1. `fragment_id`
  2. `source_path + source_range`
  3. `row/source pointer`
  4. section-like source fallback

- 핵심은:
  - 같은 underlying fragment면 path가 달라도 같은 material anchor로 본다.
  - 없는 anchor를 꾸며서 만들지 않는다.

## reading rule

- same material across multiple paths
  - `cross-path` 는 맞다
  - `cross-material` 은 아니다

- current strong line을 깎을 필요는 없다.
- 대신 corroboration breadth를 읽을 때는 아래를 따로 본다.
  - `distinct_path_count`
  - `distinct_independent_evidence_count`
  - `distinct_material_anchor_count`
  - `distinct_primary_material_anchor_count`

## current interpretation

- `transition_over_surface`는 현재 strong line일 수 있다.
- 하지만 그 strongness는
  - route diversity
  - source/pointer recurrence
  - 일부 shared material cross-path reread
  가 섞여 있는 상태다.
- 따라서 global breadth를 말하기 전에는 material axis를 같이 읽어야 한다.
