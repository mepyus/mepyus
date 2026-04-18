# line_thickening_derived_residue_trend_probe_v0

## Verdict
`implemented`

## 무엇을 넣었는가
- `derived_residue_trend`
- `cumulative_primary_rows`
- `cumulative_derived_rows`
- `recent_primary_rows`
- `recent_derived_rows`
- `recent_window_size_used`
- `recent_primary_vs_derived_summary`
- `derived_residue_trend_summary`

## 대표 라인 읽힘
- `transition_over_surface`
  - overall: `mixed_derived_supported`
  - primary-only: `balanced_broadening_candidate`
  - residue trend: `decaying`
  - 최근 5개 row는 primary-only였고, derived residue는 앞 구간에만 남아 있었다.
- `input_to_reading_organ`
  - primary-dominant
  - residue trend: `stable`
  - derived residue가 없어서 residue는 줄어들고 있다기보다 애초에 붙어 있지 않다.
- `pre_read_eye` / `raw_return_preservation`
  - `weak_summary_local`
  - residue trend: `insufficient_history`

## 해석
- cumulative read는 현재 ecology의 전체 그림을 보여준다.
- recent trend는 residue가 실제로 사라지는 쪽인지, 남는 쪽인지, 다시 붙는 쪽인지를 보여준다.
- `transition_over_surface`는 mixed이지만, 최근에는 derived residue가 줄어드는 방향으로 읽힌다.

## 남은 것
- balanced/global로 올릴 계획은 없다.
- 다음에 볼 것은 residue 자체가 아니라, primary corroboration이 더 늘어나는지 여부다.
