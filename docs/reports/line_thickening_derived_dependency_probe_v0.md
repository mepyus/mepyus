# line thickening derived dependency probe v0

## What Changed

이번 턴에서는 `line_thickening`에 derived dependency/residue reading 축을 추가했다.

추가된 핵심 필드:

- `derived_support_role`
- `derived_support_summary`
- `primary_vs_derived_balance_summary`
- `primary_support_share_bucket`
- `derived_dependency_hint`
- `primary_support_row_count`
- `derived_support_row_count`
- `self_referential_derived_row_count`
- `summary_row_count`

## Why This Was Needed

`transition_over_surface`는 현재:

- overall:
  - `mixed_derived_supported`
- primary-only:
  - `balanced_broadening_candidate`

이 상태는
"derived가 남아 있음"과
"derived에 실제로 기대고 있음"을 분리해서 읽어야만 설명이 된다.

## Focused Reading

### `transition_over_surface`

- overall profile:
  - `mixed_derived_supported`
- primary-only profile:
  - `balanced_broadening_candidate`
- support ecology bias:
  - `mixed_derived_supported`
- derived support role:
  - `mixed_but_primary_stable`
- derived dependency hint:
  - `medium`

근거:

- `primary_support_row_count=12`
- `derived_support_row_count=2`
- `self_referential_derived_row_count=2`
- `primary_support_share_bucket=high`

현재 읽기:

- derived는 남아 있다
- 하지만 primary rows가 이미 훨씬 많다
- 그래서 현재 mixed는 `derived_dependency_suspected`보다
  `mixed_but_primary_stable`에 가깝다

### `input_to_reading_organ`

- overall profile:
  - `material_heavy_path_narrow`
- primary-only profile:
  - `material_heavy_path_narrow`
- support ecology bias:
  - `primary_dominant`
- derived support role:
  - `primary_dominant`
- derived dependency hint:
  - `low`

현재 읽기:

- 이 line은 primary route 안에서 강해졌고
- derived residue가 현재 해석의 핵심이 아니다

### `pre_read_eye`

- support ecology bias:
  - `summary_only`
- derived support role:
  - `summary_only`

### `raw_return_preservation`

- support ecology bias:
  - `summary_only`
- derived support role:
  - `summary_only`

## Verification

검증은 새 route 없이 current state recompute만 사용했다.

- `python3 -m py_compile app/core/runtime/line_thickening.py scripts/run_transition_over_surface_targeted_breadth_validation.py`
- `python3 scripts/run_transition_over_surface_targeted_breadth_validation.py runtime`
- `refresh_line_registry_entry(...)` for representative lines

확인된 결과:

- `transition_over_surface`
  - `derived_support_role=mixed_but_primary_stable`
  - `derived_dependency_hint=medium`
- `input_to_reading_organ`
  - `derived_support_role=primary_dominant`
  - `derived_dependency_hint=low`
- `pre_read_eye`, `raw_return_preservation`
  - `derived_support_role=summary_only`

## Why Still Not Global Or Clean-Balanced

`transition_over_surface`는 primary side가 강해졌지만,
overall ecology에는 still derived/self-referential support가 남아 있다.

즉:

- clean-balanced로 잠그기에는 residue가 남고
- derived-dependent라고 말하기에는 primary side가 이미 충분히 강하다

그래서 현재 최선의 읽기는:

- `mixed_but_primary_stable`

이다.

## Next Condition

다음에 더 명확해지려면 아래 중 하나가 필요하다.

- derived residue가 실제로 더 줄어드는지
- primary corroboration이 더 늘어 overall mixed를 압도하는지

이번 턴의 목적은 line을 올리거나 내리는 것이 아니라,
`why mixed / how dependent`를 분리해 읽게 만드는 것이었다.
