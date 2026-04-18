# main operating set entry and navigation labeling refinement v1

## package status

complete for this turn

## files changed

- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [operating_ui_history.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_history.py)
- [operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)
- [main_operating_set_entry_and_navigation_labeling_refinement_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/main_operating_set_entry_and_navigation_labeling_refinement_v1.md)

## 1. navigation and entry labels changed

- `phase1 shell` -> `main operating set`
- `phase2 history` -> `history companion`
- `operating ui phase1 shell` -> `main operating set`
- `History / Reread / Trace` -> `History / Reread / Trace Companion`
- `open current context in phase1` -> `open in main operating set`

## 2. phase language removed or internalized

Removed from user-facing entry/navigation:

- `phase1 shell`
- `phase2 history`
- `phase1 surface separation`

Kept internal only:

- file/module names
- internal route lineage in code/doc history

## 3. how core / companion / parked now read in UI

- core
  - reads as `main operating set`
  - header now lists `Operating / Explore / Search / Memory / Similar`
- companion
  - reads as `history companion`
  - keeps time-axis reading companion meaning without suggesting a next stage
- parked
  - `saved-path curation` remains absent from active navigation

## 4. remaining naming drift

- internal filenames still contain `phase1` and `phase2`, but this remains implementation-level only
- `history companion` still includes `trace` and `reread` wording, so future label changes should avoid sliding back into phase or replay-engine framing

## 5. next action

main operating set page map labeling 정리
