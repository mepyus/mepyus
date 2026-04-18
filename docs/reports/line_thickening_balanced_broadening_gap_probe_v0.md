# line thickening balanced broadening gap probe v0

## What Changed

이번 턴에서는 `line_thickening`에 `gap` 해석축을 추가했다.

추가된 핵심 필드:

- `broadening_gap_type`
- `next_missing_axis`
- `gap_basis_summary`

이 축은 `validation_profile`을 대체하지 않고,
왜 아직 `balanced_broadening_candidate`가 비어 있는지를 읽게 해준다.

## Why This Before More Expansion

지금 필요한 것은 새 route를 더 붙이는 것이 아니라,
현재 strong line이 어디서 막히는지를 basis 축에서 정직하게 읽는 일이다.

그 이유는 이미 strong line이 둘로 갈라져 있기 때문이다.

- `transition_over_surface`
  - cross-path strong
  - but materially still narrow
- `input_to_reading_organ`
  - observer-local path
  - but materially broader

둘 다 `balanced_broadening_candidate`가 아니지만,
부족한 축은 서로 다르다.

## Current Gap Reading

### `transition_over_surface`

- `validation_profile=path_heavy_material_narrow`
- `broadening_gap_type=missing_primary_material_breadth`
- `next_missing_axis=primary_material`

현재 읽기:

- path diversity는 이미 열려 있다
- independent evidence도 2까지 올라와 있다
- 하지만 primary material anchor breadth는 아직 2라서 균형형으로 읽기 어렵다

### `input_to_reading_organ`

- `validation_profile=material_heavy_path_narrow`
- `broadening_gap_type=missing_path_diversity`
- `next_missing_axis=path`

현재 읽기:

- observer route 안에서 primary material breadth는 더 넓다
- 하지만 path diversity가 1이라 balanced broadening으로는 갈 수 없다

### `pre_read_eye`

- `validation_profile=weak_summary_local`
- `broadening_gap_type=summary_only`
- `next_missing_axis=multiple`

현재 읽기:

- widening candidate가 아니라 summary gate line이다

### `raw_return_preservation`

- `validation_profile=weak_summary_local`
- `broadening_gap_type=summary_only`
- `next_missing_axis=multiple`

현재 읽기:

- 아직 source-linked grounded reread 없이 summary echo에 머문다

## Verification

검증은 기존 상태 재계산만 사용했다.

- `python3 -m py_compile app/core/runtime/line_thickening.py scripts/run_primary_material_breadth_validation.py scripts/run_runtime_preflight.py`
- `python3 scripts/run_primary_material_breadth_validation.py runtime`
- `python3 scripts/run_runtime_preflight.py runtime --mode space_reading --ref inputs/external_cases/enterprise.txt --record-line-thickening`

이 결과:

- `transition_over_surface`는 `missing_primary_material_breadth`
- `input_to_reading_organ`은 `missing_path_diversity`
- `pre_read_eye` / `raw_return_preservation`은 `summary_only`

즉 `balanced_broadening_candidate`가 비어 있어도,
왜 비어 있는지는 이제 registry와 promotion log에서 직접 읽을 수 있다.

## Still Intentionally Not Done

- 새 route 추가
- breadth expansion
- profile/gap을 새 승격 엔진으로 사용하는 작업
- UI surface 연결

## Next Condition

다음에 균형형으로 가려면 line마다 부족 축이 다르게 채워져야 한다.

- `transition_over_surface`
  - 새로운 primary material anchors
- `input_to_reading_organ`
  - genuinely different primary validation path
- `pre_read_eye`, `raw_return_preservation`
  - summary echo를 넘는 grounded reread
