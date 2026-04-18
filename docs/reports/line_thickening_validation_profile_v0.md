# line_thickening_validation_profile_v0

## what changed

- registry와 promotion log에 아래 필드를 추가했다.
  - `validation_profile`
  - `profile_basis_summary`

- profile은 아래 basis에서 파생된다.
  - `distinct_path_count`
  - `distinct_independent_evidence_count`
  - `distinct_primary_material_anchor_count`
  - `has_self_referential_derived_support`
  - summary/local 여부

## profile set

- `weak_summary_local`
- `path_heavy_material_narrow`
- `material_heavy_path_narrow`
- `balanced_broadening_candidate`
- `mixed_derived_supported`
- `insufficient_profile`

## current read

### transition_over_surface

- `status=stable`
- `thickness_level=thick`
- `promotion_scope=cross_family_candidate`
- `validation_profile=path_heavy_material_narrow`
- `profile_basis_summary=path_rich=3; independent_evidence=2; primary_materials=2`

읽힘:

- cross-path strong line
- but materially still narrow

### input_to_reading_organ

- `status=stable`
- `thickness_level=thick`
- `promotion_scope=cross_family_candidate`
- `validation_profile=material_heavy_path_narrow`

읽힘:

- observer-local route 안에서 primary materials가 더 넓게 반복된 line
- path breadth는 아직 좁음

### pre_read_eye / raw_return_preservation

- `validation_profile=weak_summary_local`

읽힘:

- summary/local line
- 아직 strong validation shape로 읽지 않음

## why this matters

- 이번 작업은 새 route나 breadth를 더 여는 작업이 아니다.
- strong line들의 “shape”를 분리해서,
  같은 strong처럼 보이던 line들을 다르게 읽게 만드는 작업이다.

## verification

used:

```bash
python3 scripts/run_primary_material_breadth_validation.py runtime
python3 scripts/run_runtime_preflight.py runtime --mode space_reading --ref inputs/external_cases/enterprise.txt --record-line-thickening
python3 - <<'PY'
from pathlib import Path
from app.core.runtime.line_thickening import refresh_line_registry_entry
runtime_root=Path('runtime').resolve()
for line_name in ['input_to_reading_organ','transition_over_surface','pre_read_eye','raw_return_preservation']:
    refresh_line_registry_entry(runtime_root, line_name)
PY
```

result:

- `transition_over_surface` and `input_to_reading_organ` now diverge at profile level.
- summary lines remain weak summary profile.

## next boundary

- 다음에 필요한 것은 new route expansion보다,
  현재 line들이 truly balanced broadening으로 가는지 아닌지를 계속 보는 것이다.
- 즉 profile은 다음 확장의 입구가 아니라,
  현재 state를 과장 없이 읽게 하는 해석 규율이다.
