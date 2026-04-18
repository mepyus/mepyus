# history companion return-link labeling consistency check v1

## package status

complete for this turn

## files changed

- [operating_ui_history.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_history.py)
- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [history_companion_return_link_labeling_consistency_check_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/history/history_companion_return_link_labeling_consistency_check_v1.md)

## 1. wording kept or changed

Kept:

- `Main Operating Set`
- `Reread Context`
- `Historical Reference`
- `Clear History Context`

Changed:

- `Return / Open in Phase1` -> `Main Operating Set Link`
- `open in phase1 with reread context` -> `Open in Main Operating Set`
- `opened from history / reread context attached` -> `Historical Reference Attached`
- `historical reread context=...` -> `historical reference attached=...`
- `historical reread context remains separate from Memory` -> `historical reference remains separate from Memory`

## 2. inconsistent phrases removed

Removed or reduced:

- explicit `Phase1` wording in history return/open area
- mixed `open` and `return` phrasing for the same navigation action
- `opened from history` phrasing where the important meaning was really `reference attached`

## 3. meaning split now

- `Open in Main Operating Set`
  - navigation action
- `Historical Reference Attached`
  - attached contextual reference
- `Clear History Context`
  - detach the attached reference only

This keeps navigation, attachment, and detach as separate meanings.

## 4. remaining drift risk

- `Open in Main Operating Set` is now consistent, but future micro-copy could still over-explain the attachment if not trimmed
- some internal code/query names still use `history_*` and `phase1`, though these are no longer user-facing

## 5. next action

history companion header micro-copy trim check
