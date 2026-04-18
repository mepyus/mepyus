# phase2 translated reading-unit refinement v1

## package status

complete for this turn

## files changed

- [operating_ui_history.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_history.py)
- [phase2_translated_reading_unit_refinement_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase2_translated_reading_unit_refinement_v1.md)

## 1. how each reading unit became more operator-facing

### run snapshot

- title now reads as `read checkpoint`
- summary now reads as a brief state read instead of raw key-style text
- context hint is shown separately
- time hint now includes `most recent / recent / older`, readable UTC time, and relative age

### activity cluster

- titles now read as `state change group`, `grounding shift group`, `traceability shift group`, or `provenance-only reading group`
- grouping note explains why the cluster is one reading unit
- summary now reads as `reason + visible field-shift count`

### trace entry

- raw-ish labels were replaced with operator-facing prompts:
  - `what started this shift`
  - `what changed in this reading slice`
  - `supporting evidence read`
  - `operator note carried with the slice`
- changed fields are humanized into readable phrases
- honesty notes appear where source depth is limited

### replayable state

- wording now consistently uses `reread` and `prior state slice`
- summary explains why the state is readable again and what is limited
- rerun/simulate implication was reduced further

## 2. raw-like wording reduced

Reduced or replaced:

- `view-level replay only` -> `view-level reread only`
- `translated recent lineage clusters` -> `grouped activity flows`
- `trigger and reason` -> `what started this shift`
- `state change read` -> `what changed in this reading slice`
- `evidence link count` -> `supporting evidence read`
- `state note` -> `operator note carried with the slice`
- replay preview copy now centers `reread preview`

## 3. time-axis legibility improvements

- snapshots now show `most recent / recent / older`
- clusters carry ordering hints tied to the selected read checkpoint
- trace cards inherit the same ordering hint so the selected slice still reads temporally
- reread preview is explicitly anchored to the selected activity group or latest-linked slice

## 4. source sparsity honesty

Still shown explicitly where needed:

- `history sparse / latest-linked reread only`
- `partial trace only`
- `source is limited, so this reading stays partial`
- `available as a prior-state read checkpoint, limited by current history depth`

The surface still avoids fake completeness.

## 5. still-weak units

- activity cluster remains thin when history depth is only one row
- trace entry quality is still bounded by current lineage depth
- context hint is still asset-centered rather than a richer operating-context phrase

## 6. next candidates

- add one very thin sequence label for trace cards if history depth grows beyond one or two rows
- evaluate whether update-event helper data can improve cluster summary wording without surfacing raw runtime names
