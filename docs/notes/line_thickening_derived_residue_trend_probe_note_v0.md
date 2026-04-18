# line_thickening_derived_residue_trend_probe_note_v0

## 한 줄 정의
`derived_residue_trend`는 혼합 상태를 고정된 스냅샷으로만 보지 않고, 최근 윈도우에서 derived residue가 줄어드는지/유지되는지/다시 붙는지를 읽는 해석 보조축이다.

## 왜 필요한가
- `transition_over_surface`는 overall로는 `mixed_derived_supported`였지만, primary-only로는 이미 `balanced_broadening_candidate`였다.
- 그래서 문제는 "강한가"가 아니라 "남아 있는 derived residue가 시간적으로 줄어드는가"였다.
- 누적만 보면 오래된 derived residue가 현재를 과장할 수 있고, 최근만 보면 역사적 residue를 놓칠 수 있다.
- 따라서 cumulative read와 recent-window read를 분리해야 했다.

## 읽기 규칙
- `decaying`: 최근 윈도우에서 derived rows가 줄었고, 누적 대비 residue가 약해지는 방향.
- `stable`: derived residue가 남아 있지만 최근 추세가 크게 바뀌지 않음.
- `reappearing`: 최근 윈도우에서 derived residue가 다시 붙는 방향.
- `insufficient_history`: primary/derived non-summary history가 아직 너무 얇음.

## 이번 턴의 경계
- 상태/승격 규칙은 바꾸지 않는다.
- 새 route, breadth expansion, UI, graph, ontology는 건드리지 않는다.
- trend는 해석 보조축이며, 새 승격 엔진이 아니다.
