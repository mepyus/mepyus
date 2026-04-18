# line thickening primary only profile split v0

## What Changed

이번 턴에서는 `line_thickening`에 dual-profile read를 추가했다.

추가된 핵심 필드:

- `primary_only_validation_profile`
- `primary_only_basis_summary`
- `support_ecology_bias`
- `primary_only_path_count`
- `primary_only_material_count`
- `primary_only_source_document_count`
- `primary_only_independent_evidence_count`

## Why This Was Needed

`transition_over_surface`는 현재 두 가지가 동시에 사실이다.

- overall ecology는 아직 `mixed_derived_supported`
- primary side만 보면 breadth improvement가 실제로 발생했다

이 둘을 분리하지 않으면,

- primary improvement가 overall mixed state에 가려지고
- 반대로 overall mixed state를 무시하고 과장 읽기가 생긴다

## Focused Reading

### `transition_over_surface`

- overall profile:
  - `mixed_derived_supported`
- primary-only profile:
  - `balanced_broadening_candidate`
- support ecology bias:
  - `mixed_derived_supported`

현재 읽기:

- overall로는 아직 derived/self-referential support가 섞여 있다
- 하지만 primary evidence만 보면:
  - `primary_only_path_count=2`
  - `primary_only_material_count=5`
  - `primary_only_independent_evidence_count=2`
  - `primary_only_source_document_count=4`

즉 primary side에서의 breadth improvement는 실제다.
다만 overall ecology가 아직 mixed라서 global/balanced read를 바로 잠그면 과하다.

### `input_to_reading_organ`

- overall profile:
  - `material_heavy_path_narrow`
- primary-only profile:
  - `material_heavy_path_narrow`
- support ecology bias:
  - `primary_dominant`

현재 읽기:

- 이 line은 mixed에 가려지는 타입이 아니다
- primary 쪽에서도 같은 shape가 유지된다

### `pre_read_eye`

- overall profile:
  - `weak_summary_local`
- primary-only profile:
  - `weak_summary_local`
- support ecology bias:
  - `summary_only`

### `raw_return_preservation`

- overall profile:
  - `weak_summary_local`
- primary-only profile:
  - `weak_summary_local`
- support ecology bias:
  - `summary_only`

## Verification

검증은 새 route 없이 current state recompute만 사용했다.

- `python3 -m py_compile app/core/runtime/line_thickening.py scripts/run_transition_over_surface_targeted_breadth_validation.py scripts/run_primary_material_breadth_validation.py`
- `python3 scripts/run_transition_over_surface_targeted_breadth_validation.py runtime`
- `refresh_line_registry_entry(...)` for representative lines

확인된 결과:

- `transition_over_surface`
  - overall=`mixed_derived_supported`
  - primary-only=`balanced_broadening_candidate`
- `input_to_reading_organ`
  - overall=`material_heavy_path_narrow`
  - primary-only=`material_heavy_path_narrow`
- `pre_read_eye`
  - overall=`weak_summary_local`
  - primary-only=`weak_summary_local`
- `raw_return_preservation`
  - overall=`weak_summary_local`
  - primary-only=`weak_summary_local`

## Why Still Not Balanced Or Global

`transition_over_surface`는 primary side에서 좋아졌지만,
overall ecology에는 still derived/self-referential support가 남아 있다.

그래서:

- primary-only read는 improvement를 보여주고
- overall read는 여전히 mixed state를 보존한다

이 분리가 지금은 더 중요하다.

## Next Condition

다음에 더 나아가려면 아래 중 하나가 필요하다.

- derived-supported bias가 실제로 줄어드는지 확인
- primary corroboration이 계속 늘어나는지 확인

중요한 점은:

이번 턴의 목적은 새 승격이 아니라
`why mixed / why improved`를 동시에 읽게 만드는 것이었다.
