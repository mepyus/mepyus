# line thickening primary only profile split note v0

## Purpose

이 메모의 목적은 `overall validation profile`과
`primary-only validation profile`을 분리해 읽게 만드는 것이다.

핵심은 아래 두 문장을 동시에 유지하는 데 있다.

- overall state는 mixed ecology를 반영해야 한다
- primary evidence만 놓고 보면 실제 breadth improvement가 가려지지 않아야 한다

## Why This Is Needed

현재 `transition_over_surface`는 실제로 primary material breadth가 넓어졌다.

- `distinct_primary_material_anchor_count = 5`

하지만 overall ecology에는 여전히 derived/self-referential support가 남아 있어
overall profile은 `mixed_derived_supported`로 읽힌다.

이 상태를 하나의 profile로만 보면,

- "왜 mixed인지"
- "왜 primary 쪽은 실제로 좋아졌는지"

를 동시에 읽을 수 없다.

## Added Reading Axes

- `validation_profile`
  - 전체 ecology 기준
- `primary_only_validation_profile`
  - primary evidence만 기준
- `support_ecology_bias`
  - current support가
    - `primary_dominant`
    - `mixed_derived_supported`
    - `derived_heavy`
    - `summary_only`
  중 어디에 가까운지

## Intended Read

### `transition_over_surface`

- overall:
  - `mixed_derived_supported`
- primary-only:
  - `balanced_broadening_candidate`
- bias:
  - `mixed_derived_supported`

즉:

- overall ecology는 아직 mixed
- 하지만 primary side만 보면 balanced broadening candidate 조건은 이미 일부 충족

### `input_to_reading_organ`

- overall:
  - `material_heavy_path_narrow`
- primary-only:
  - `material_heavy_path_narrow`
- bias:
  - `primary_dominant`

즉:

- 이 line은 mixed에 가려진 것이 아니라
- 실제로 primary route 안에서 material-heavy shape를 가진다

### `pre_read_eye`, `raw_return_preservation`

- overall:
  - `weak_summary_local`
- primary-only:
  - `weak_summary_local`
- bias:
  - `summary_only`

## Rule

앞으로는 strong line을 볼 때 아래를 같이 읽는다.

- overall profile
- primary-only profile
- support ecology bias

즉 질문은 이제
"이 line은 strong한가?"가 아니라
"전체 ecology에서는 어떻게 보이고, primary 쪽만 보면 어떻게 보이는가?"가 된다.
