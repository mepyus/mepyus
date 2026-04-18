# browser level manual smoke check v1

## verdict

pass_with_micro_note

## manual click path

1. Open `http://127.0.0.1:8532/operating-ui-phase1` in Safari
2. Confirm Main Operating Set tab title and core page map
3. Open `http://127.0.0.1:8532/operating-ui-history` in Safari
4. Confirm History Companion title and `Open in Main Operating Set` presence
5. Reconfirm reachable HTML labels and phase-language absence on the same server instance

## page-by-page observation

- `Main Operating Set`
  - browser URL opened correctly
  - Safari tab title now reads `main operating set`
  - core page map reads clearly:
    - `Operating: observe now`
    - `Explore: build path`
    - `Search: direct access`
    - `Memory: saved paths`
    - `Similar: local re-query`
  - `History Companion: time-axis read` remains visible as companion, not core progression
- `History Companion`
  - browser URL opened correctly
  - Safari tab title reads `history / reread / trace companion`
  - `Open in Main Operating Set` is present
  - no `Open in Phase`, `Restore State`, or execution-like wording was found

## misleading label check

- no misleading core/companion label was observed in the reachable browser instance
- no user-facing phase language remained after the tab-title trim
- no replay/restore/load wording was observed in the tested surface entry points

## modified files

- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [browser_level_manual_smoke_check_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/browser_level_manual_smoke_check_v1.md)

## micro note

- the only issue found in this smoke pass was the old browser tab title `Operating UI Phase1 Shell`
- this was a wording-level issue, not a composition issue, and it is now trimmed to `main operating set`

## next smallest action

leave the reachable viewer instance on `http://127.0.0.1:8532` for optional human spot-check only
