# main operating set page map labeling refinement v1

## package status

complete for this turn

## files changed

- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [operating_ui_history.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_history.py)
- [main_operating_set_page_map_labeling_refinement_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/main_operating_set_page_map_labeling_refinement_v1.md)

## 1. page map labels added

Added a thin page-map strip near the main entry/header area.

Core page labels:

- `Operating: observe now`
- `Explore: build path`
- `Search: direct access`
- `Memory: saved paths`
- `Similar: local re-query`

Companion label:

- `History Companion: time-axis read`

## 2. how page differences now read faster

- `Operating / Explore / Search / Similar` no longer rely only on page names; each now has a one-line role verb
- the most confusable trio, `Explore / Search / Similar`, is now distinguished by:
  - `build path`
  - `direct access`
  - `local re-query`
- `Memory` stays tied to `saved paths`, so explicit saved-path meaning remains visible

## 3. companion distinction

History remains visibly separate:

- labeled as `History Companion`
- described as `time-axis read`
- shown on its own companion row rather than mixed into the core page row

That keeps it from reading like the next step in a progression.

## 4. where explanation was kept short

- used one-line chips instead of long onboarding text
- kept page map at the header level only
- avoided new explanatory paragraphs inside each page body

## 5. remaining naming drift

- internal code/file names still contain `phase1` and `phase2`
- `Similar: local re-query` is clear enough now, but if future labels get longer it could start collapsing back toward generic similarity wording

## 6. next action

history companion return-link labeling consistency check
