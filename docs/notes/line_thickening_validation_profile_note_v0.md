# line_thickening_validation_profile_note_v0

## purpose

- 이번 note의 목적은 strong line을 한 종류로 뭉개지 않고, 어떤 basis에서 강해졌는지 따로 읽게 만드는 것이다.

## why profile is needed

- 지금 상태에서는 `transition_over_surface`와 `input_to_reading_organ`이 둘 다 strong로 보일 수 있다.
- 하지만 실제 모양은 다르다.
  - `transition_over_surface`
    - path-heavy
    - materially still narrow
  - `input_to_reading_organ`
    - materially broader
    - path는 아직 좁다

- 그래서 `status / thickness / scope`만으로는 부족하고,
  `validation_profile`이 해석 보조축으로 필요하다.

## profile rule

- `weak_summary_local`
  - summary/local line
- `path_heavy_material_narrow`
  - path와 independent evidence는 열렸지만 primary material breadth는 아직 좁음
- `material_heavy_path_narrow`
  - primary material breadth는 넓지만 path는 아직 좁음
- `balanced_broadening_candidate`
  - path/material 양쪽이 같이 넓어질 후보
- `mixed_derived_supported`
  - strongness는 있으나 derived/self-referential support가 의미상 섞여 있음
- `insufficient_profile`
  - 아직 충분한 shape 판단 불가

## current read

- `transition_over_surface` -> `path_heavy_material_narrow`
- `input_to_reading_organ` -> `material_heavy_path_narrow`
- `pre_read_eye` -> `weak_summary_local`
- `raw_return_preservation` -> `weak_summary_local`

## boundary

- profile은 status/scope 대체물이 아니다.
- profile은 “왜 강한가”를 읽는 보조축이다.
