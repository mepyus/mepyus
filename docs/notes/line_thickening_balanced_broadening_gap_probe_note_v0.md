# line thickening balanced broadening gap probe note v0

## Purpose

이 메모의 목적은 `balanced_broadening_candidate`를 억지로 만드는 것이 아니라,
왜 현재 strong line들이 아직 균형형 broadening으로 가지 못하는지를
현재 basis 축 위에서 정직하게 읽게 만드는 것이다.

핵심은 `validation_profile` 옆에 `gap` 축을 두어,
지금 다음에 부족한 축이 무엇인지 바로 보이게 하는 데 있다.

## Why This Is Needed

현재 strong line은 이미 둘로 갈라진다.

- `transition_over_surface`
  - path-heavy
  - cross-path는 열렸지만 primary material breadth는 아직 좁다
- `input_to_reading_organ`
  - material-heavy
  - primary material breadth는 넓지만 path diversity는 아직 좁다

이 둘이 모두 `strong` 혹은 `thick`로만 보이면,
다음에 어디를 넓혀야 하는지 읽을 수 없다.

## Gap Reading Principle

`gap` 축은 새 승격 엔진이 아니다.
현재 basis를 읽는 해석 보조축이다.

최소 구분은 아래와 같다.

- `missing_path_diversity`
  - material은 넓어졌지만 path가 아직 좁다
- `missing_primary_material_breadth`
  - path는 열렸지만 primary material breadth가 아직 좁다
- `missing_independent_evidence`
  - path/material은 일부 열렸지만 independent corroboration이 아직 부족하다
- `summary_only`
  - summary echo 기반이라 widening candidate가 아니다
- `mixed_gap`
  - 한 축으로 단정하기 어려운 혼합 부족 상태

## Intended Reads

- `transition_over_surface`
  - `next_missing_axis=primary_material`
- `input_to_reading_organ`
  - `next_missing_axis=path`
- `pre_read_eye`
  - `summary_only`
- `raw_return_preservation`
  - `summary_only`

## Reading Rule

앞으로는 strong line을 볼 때 아래를 같이 읽는다.

- `validation_profile`
- `broadening_gap_type`
- `next_missing_axis`
- `profile_basis_summary`
- `gap_basis_summary`

즉 질문은
"이 line은 strong한가?"에서 끝나지 않고,
"어떤 모양으로 strong하며, 다음에 무엇이 부족한가?"로 이어져야 한다.
