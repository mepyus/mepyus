# line thickening transition_over_surface targeted primary material v0

## What Was Done

이번 턴에서는 `transition_over_surface`만 대상으로
기존 primary routes 안에서 targeted primary material breadth validation을 수행했다.

사용한 route:

- `internal_observer`
- `source_fragment_view`

새 route는 추가하지 않았다.

## Cohort

### observer control

- `frag_basic3_002`
- `frag_basic4_003`

### source view targeted materials

- `frag_basic3_002` (control)
- `frag_basic_004` (new)
- `frag_basic3_004` (new)
- `frag_ytex_003` (new)

즉 이번 턴은 control 1개를 유지하면서,
새 primary material anchors 3개를 좁게 추가하는 방식이다.

## Why This Was The Right Next Move

현재 `transition_over_surface`의 gap는

- `validation_profile=path_heavy_material_narrow`
- `broadening_gap_type=missing_primary_material_breadth`
- `next_missing_axis=primary_material`

이었기 때문에,
가장 자연스러운 다음은 path를 더 붙이는 것이 아니라
primary material anchors를 늘리는 것이다.

## Result Reading

이번 실행 후 읽힌 핵심은 아래다.

- `distinct_primary_material_anchor_count`
  - `2 -> 5`
- `distinct_source_document_count`
  - `4 -> 6`
- `validation_profile`
  - `path_heavy_material_narrow -> mixed_derived_supported`
- `broadening_gap_type`
  - `missing_primary_material_breadth -> mixed_gap`
- `next_missing_axis`
  - `primary_material -> multiple`

즉 gap는 실제로 줄었다.
하지만 균형형 broadening으로 바로 열린 것은 아니다.

## What Was Newly Added

이번 턴에서 실제로 새 primary material로 들어온 것은 아래다.

- `frag_basic_004`
- `frag_basic3_004`
- `frag_ytex_003`

control로 다시 본 것은 아래다.

- `frag_basic3_002`
- `frag_basic4_003`

중요한 점은:

- control은 same-material continuity 확인용이다
- breadth 증가는 새 `fragment_id` 3개에서 왔다

## Why It Still May Not Be Balanced

primary material breadth가 늘더라도,
아래가 남아 있으면 아직 balanced broadening으로는 읽지 않는다.

- derived/self-referential support history
- limited independent evidence ecology
- still-bounded primary validation path set

즉 breadth 증가가 곧 균형형 broadening은 아니다.

## Next Condition

다음에 더 나아가려면 아래 둘을 같이 봐야 한다.

- 새 primary materials가 계속 반복되는가
- breadth가 늘어난 뒤에도 derived-supported bias가 남는가

현재 상태를 한 줄로 잠그면:

- `transition_over_surface`는 여전히 strong하다
- primary material breadth는 실제로 넓어졌다
- 하지만 derived/self-referential support history가 남아 있어
  아직 `balanced_broadening_candidate`로 읽으면 과하다

핵심은:

`transition_over_surface`의 gap를 줄이는 것이지,
이번 턴에 억지로 균형형으로 승격시키는 것이 아니다.
