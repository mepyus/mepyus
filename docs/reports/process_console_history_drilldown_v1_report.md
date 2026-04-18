[[A]] [[OBJ:process_console_history_drilldown_v1_report]] [[SEM:report_for_lineage_surface_added_to_process_console]]

# process_console_history_drilldown_v1_report

## 1. purpose

- 이번 report의 목적은 process console에 asset별 state history drill-down을 연결한 범위와 lineage reading 결과를 기록하는 것이다.

## 2. read source

- authoritative history:
  - `runtime/state/engine_state_history/<asset_id>.jsonl`
- helper event surface:
  - `runtime/views/engine_state_update_events/<asset_id>.json`
- current latest link:
  - `runtime/views/engine_state_latest/<asset_id>.json`

즉 history drill-down은 jsonl history를 본원장으로 읽고, event surface는 얇은 helper로만 사용한다.

## 3. changed_fields calculation

- history record 자체에 changed field가 없으므로 selector에서 인접 이전 record와 canonical 8필드를 비교해 계산한다.
- 배열 field:
  - `comparison_memory_reason`
  - `gate_blocker_summary`
  는 set-like 비교를 사용한다.
- first record:
  - bootstrap/backfill 형성 record로 보고 canonical 8필드 전체를 changed로 취급한다.
- latest runtime append처럼 canonical drift가 없는 경우:
  - `changed_fields = []`
  - `provenance_only_update = true`

## 4. connected UI surfaces

- state panel:
  - `HistorySummaryStrip` 연결
- right panel:
  - `LatestLineageLink`
  - `recent history` timeline
  - timeline item expand/collapse
- latest surface:
  - 그대로 primary
- experimental namespace:
  - presence만 표기, 내용은 기본 숨김 유지

## 5. representative asset read

대표 4개 자산에서 확인한 것:

- `youtube_03_22`
  - latest trigger: `runtime_evidence`
  - latest change kind: `provenance_only`
  - recent history count: `5`
- `openai_02_11`
  - latest trigger: `runtime_evidence`
  - latest change kind: `provenance_only`
  - recent history count: `5`
- `knowledge_editing_youtube`
  - latest trigger: `runtime_evidence`
  - latest change kind: `provenance_only`
  - recent history count: `4`
- `gary_tan_brain`
  - latest trigger: `runtime_evidence`
  - latest change kind: `provenance_only`
  - recent history count: `4`

### current read

- runtime bridge adoption run은 canonical drift보다 provenance 강화 append였기 때문에, lineage surface에서 `provenance_only`로 읽히는 것이 맞다.
- backfill record와 runtime_evidence record는 trigger badge가 분리돼 보여서 bootstrap과 recent operational update가 섞이지 않는다.

## 6. canonical vs experimental separation

- canonical snapshot은 timeline item expand 안에서만 표시한다.
- experimental namespace는 `present / hidden by default` 신호만 준다.
- naming-heavy field는 canonical change처럼 렌더하지 않는다.

## 7. latest/history linkage

- latest는 계속 state-first surface로 유지된다.
- history summary는 `recent update count`, `latest trigger`, `latest reason`, `latest change kind`를 얇게 보여준다.
- latest lineage link는 `current latest formed from recent N updates` 형식으로 latest를 시간축 위에 다시 놓는다.

## 8. remaining limits

- 현재는 full diff engine 전 단계라서 old/new value diff는 아직 개별 item 내부에 직접 표시하지 않는다.
- malformed history item에 대한 warning UI는 최소 수준이다.
- history overflow에 대한 expand-more interaction은 아직 단순 count 노출 수준이다.

## 9. one-line verdict

> 이번 drill-down으로 process console은 latest canonical state를 단순 현재값이 아니라, backfill과 runtime_evidence가 어떤 순서와 근거로 쌓였는지 읽게 하는 lineage surface까지 갖추게 됐다.
