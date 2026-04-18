[[A]] [[OBJ:state_change_diff_surface_v1]] [[SEM:diff_surface_spec_for_adjacent_canonical_state_comparison]]

# state_change_diff_surface_v1

## 1. purpose

- 이번 surface의 목적은 연속된 두 canonical state record 사이에서 무엇이 실제로 바뀌었고 무엇이 바뀌지 않았는지를 빠르게 읽게 하는 것이다.
- diff는 별도 truth layer가 아니라 history lineage 위에 붙는 얇은 읽기면이다.

## 2. read source

- authoritative source:
  - `runtime/state/engine_state_history/<asset_id>.jsonl`
- auxiliary source:
  - `runtime/views/engine_state_update_events/<asset_id>.json`
  - `runtime/views/engine_state_latest/<asset_id>.json`

## 3. code split

- pair loader:
  - [state_change_diff_loader.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/state_change_diff_loader.py)
- diff selectors:
  - [state_change_diff_selectors.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/state_change_diff_selectors.py)
- process console builder:
  - [builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py)
- process console render:
  - [render.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/render.py)

## 4. comparison unit

- 기본 diff 단위는 adjacent pair다.
- 기본 open:
  - latest vs previous (`compare_index=0`)
- timeline open:
  - selected history item vs immediate previous (`compare_index=n`)

## 5. canonical-first diff rules

- direct compare:
  - `packet_texture`
  - `grounding_status`
  - `emergence_status`
  - `carryover_risk`
  - `maturation_state`
  - `traceability_status`
- set-like compare:
  - `comparison_memory_reason`
  - `gate_blocker_summary`

### array normalization

- array 순서 차이는 no change로 취급한다.
- added / removed membership만 diff로 본다.

## 6. derived outputs

- `changed_fields`
- `added_items_by_field`
- `removed_items_by_field`
- `unchanged_fields_count`
- `diff_class`
- `provenance_only`

## 7. diff class rules

- `provenance_only`
  - canonical 8필드 변화 없음
- `packet_texture_change`
- `grounding_change`
- `emergence_change`
- `carryover_change`
- `maturation_change`
- `traceability_change`
- `blocker_change`
- `comparison_memory_change`
- `mixed_change`

주의:
- 이 값들은 UI summary용 derived label이다.
- canonical state field로 저장하지 않는다.

## 8. UI attachment points

- state panel:
  - `DiffSummaryStrip`
  - `compare to previous` entry
- history timeline:
  - item별 `compare to previous` link
- right panel:
  - `StateChangeDiffPanel`
  - changed field chips
  - field-level diff rows
  - provenance/evidence summary

## 9. guard rules

- same-record compare 금지
- previous가 없으면 `no_previous_state`
- malformed record가 있어도 panel 전체 crash 금지
- experimental namespace diff는 기본 숨김
- array diff는 set-like normalization 후 계산

## 10. one-line lock

> `state_change_diff_surface_v1`는 adjacent canonical state pair를 기준으로 changed fields, provenance-only 여부, array added/removed, trigger/reason/evidence를 빠르게 읽게 만드는 process console용 변화면 규정이다.
