# line thickening derived dependency probe note v0

## Purpose

이 메모의 목적은 `mixed_derived_supported`를 더 쪼개어,

- derived residue가 남아 있는 상태
- derived support에 실제로 기대는 상태

를 구분하게 만드는 것이다.

핵심은 `transition_over_surface`처럼

- overall은 mixed
- primary-only는 already strong

인 line을 더 정직하게 읽는 데 있다.

## Why This Is Needed

현재 `transition_over_surface`는 아래 둘이 동시에 사실이다.

- overall:
  - `mixed_derived_supported`
- primary-only:
  - `balanced_broadening_candidate`

이 상태를 하나의 mixed label로만 읽으면,
derived가 단지 남아 있는지,
아니면 현재 상태가 실제로 derived에 기대는지 구분할 수 없다.

## Added Reading Axes

- `derived_support_role`
  - `summary_only`
  - `primary_dominant`
  - `residue_present`
  - `mixed_but_primary_stable`
  - `derived_dependency_suspected`
  - `derived_heavy`
- `derived_support_summary`
- `primary_vs_derived_balance_summary`
- `primary_support_share_bucket`
- `derived_dependency_hint`

## Intended Reads

### `transition_over_surface`

- overall:
  - `mixed_derived_supported`
- primary-only:
  - `balanced_broadening_candidate`
- derived support role:
  - `mixed_but_primary_stable`

즉:

- derived가 분명 남아 있다
- 하지만 primary side가 이미 약하지 않다
- 따라서 현재 mixed는 dependency보다는 residue가 더 강한 쪽으로 읽힌다

### `input_to_reading_organ`

- derived support role:
  - `primary_dominant`

즉:

- 이 line은 derived residue가 현재 핵심이 아니다

### `pre_read_eye`, `raw_return_preservation`

- derived support role:
  - `summary_only`

## Rule

앞으로 mixed line을 볼 때는 아래 순서로 읽는다.

- overall profile
- primary-only profile
- support ecology bias
- derived support role

즉 질문은 이제
"mixed인가?"가 아니라
"mixed라면 residue인가, dependency인가?"가 된다.
