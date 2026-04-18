# line thickening evidence independence note v0

## 목적
`line_thickening`에서 path diversity와 evidence independence를 분리하기 위한 기준 노트다.

## 왜 필요한가
- distinct_path_count는 route가 몇 개였는지를 말한다.
- evidence independence는 그 근거가 primary/raw인지, derived/report/trace인지 말한다.
- 둘을 섞으면 generated report를 새로운 독립 근거로 과장하게 된다.

## 구분
- `primary_raw`: raw fragment, direct span, raw surface에 직접 닿는 근거
- `primary_structured`: raw에 닿지만 span이 약하거나 구조화된 pointer만 있는 근거
- `derived_trace`: split / trace / processing artifact에서 나온 근거
- `derived_report`: operator summary / readable board / generated report에서 나온 근거
- `summary_echo`: preflight처럼 요약면만 있는 신호

## independence class
- `primary`: raw/primary evidence
- `derived`: trace/report 기반 evidence
- `self_referential_derived`: generated report가 자기 자신을 다시 근거처럼 읽는 경우
- `mixed`: 혼합되었거나 아직 분류가 불안정한 경우

## 현재 two-route 상태의 읽기
- observer route는 primary/raw 쪽이다.
- structured_doc_routing route는 derived/report/trace 쪽이다.
- 따라서 `transition_over_surface`는 cross-path 이지만, independent corroboration 이 충분하다고 읽으면 안 된다.

## 경계
- path diversity를 evidence independence로 승격하지 않는다.
- derived/report를 raw evidence처럼 취급하지 않는다.
- global label은 independent evidence가 충분할 때만 검토한다.
