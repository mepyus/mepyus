# history companion sparse-degraded honesty wording balance check v1

## package status

complete for this turn

## files changed

- [operating_ui_history.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_history.py)
- [history_companion_sparse_degraded_honesty_wording_balance_check_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/history/history_companion_sparse_degraded_honesty_wording_balance_check_v1.md)

## 1. which honesty wording was kept or reduced

- kept
  - `partial trace only`
  - `reread preview unavailable`
  - `source unavailable`
  - `source too sparse`
- reduced
  - `latest snapshot source unavailable` -> `source unavailable`
  - `partial trace only / no activity clusters loaded for this snapshot yet` -> `partial trace only / no clusters for this snapshot yet`
  - `trace reading unavailable / partial source only` -> `trace read unavailable / partial source`
  - `reread preview unavailable / current source is too sparse` -> `reread preview unavailable / source too sparse`
  - `history sparse / latest-linked reread only` -> `history sparse / latest-linked read only`
  - `source limited / partial read only` -> `partial source / partial read`
  - `prior state slice / limited by current history depth` -> `prior state slice / history depth limited`

## 2. which duplication was removed

- removed repeated `source` wording where the same section already showed availability state
- reduced `latest-linked reread only` to `latest-linked read only` because `reread` meaning already remains in the page and section labels
- shortened empty-state lines that repeated both the missing unit and the missing source in long form

## 3. wording that had to stay

These still needed to remain:

- `partial trace only`
- `reread preview unavailable`
- `history sparse`
- `prior state slice`

Without these, sparse/degraded honesty would weaken too much or the reread unit could start to look like a general failure state.

## 4. what improved after the balance pass

- empty-state honesty now reads more like availability truth and less like a warning block
- item-level honesty and section-level honesty overlap less
- sparse/degraded/unavailable wording now uses a smaller shared vocabulary across sections

## 5. remaining wording watchpoint

- `partial trace only` still appears both as a badge and inside some empty/sparse states, which is acceptable now but could become repetitive again if more helper text is added later

## 6. next action

history companion freeze-readiness spot check
