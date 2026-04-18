# history companion item-level label compression check v1

## package status

complete for this turn

## files changed

- [operating_ui_history.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_history.py)
- [history_companion_item_level_label_compression_check_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/history/history_companion_item_level_label_compression_check_v1.md)

## 1. which item-level labels were shortened

- snapshot title
  - `read checkpoint` -> `checkpoint`
- snapshot meta
  - `context=...` -> `asset=...`
- snapshot summary
  - `grounding ...` -> `grounded ...`
- cluster title
  - `runtime evidence / grounding shift group` style
  - -> `runtime evidence / grounding shift` style
- cluster meta
  - raw-like `cluster_kind` exposure removed from the visible item meta
  - replaced by shorter human tag such as `grounding shift` or `partial trace`
- cluster grouping note
  - compressed to shorter grouped-slice phrasing
- trace entry labels
  - `limited trace visibility` -> `limited trace view`
  - `what started this shift` -> `what started it`
  - `what changed in this reading slice` -> `what changed`
  - `supporting evidence read` -> `supporting evidence`
  - `operator note carried with the slice` -> `operator note`
- reread title/summary
  - `reread the state slice around ...` -> `reread around ...`
  - prior-state summaries shortened

## 2. what meaning was preserved

Still preserved:

- snapshot remains a checkpoint
- cluster remains a grouped activity/state slice
- trace remains a translated reading unit
- reread preview remains prior-state only
- sparse/degraded honesty remains in limited-trace and sparse-history wording

## 3. repetition removed

- removed repeated `reading slice` wording from multiple trace labels
- removed repeated `group` suffix where the cluster title already reads as a grouped slice
- removed repeated `translated trace read` phrasing from item meta by compressing it to `translated read`
- shortened reread titles that restated `state slice` too often

## 4. honesty wording kept

These remained on purpose:

- `partial trace only`
- `source limited / partial read only`
- `history sparse / latest-linked reread only`
- `prior state slice / limited by current history depth`

## 5. remaining compression risk

- cluster summary plus grouping note can still overlap when there is only one visible history row
- some trace summaries remain long when changed fields are numerous, because honesty is more important than over-compression there
- raw source labels can still exist in embedded shell data for adapter/probe use, even though the visible item labels are compressed

## 6. next action

history companion sparse/degraded honesty wording balance check
