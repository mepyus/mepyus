# phase1 blank-start and quick-start boundary refinement v1

## package status

complete for this turn

## files changed

- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [phase1_blank_start_and_quick_start_boundary_refinement_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_blank_start_and_quick_start_boundary_refinement_v1.md)

## 1. blank-start implementation

Explore now has a real blank authoring entry.

- `shared_spine` no longer boots with object/lens/position prefilled
- `current_preview_connection` starts as `None`
- Explore now exposes `start blank path` as an explicit action
- blank current path is rendered as:
  - `blank -> blank -> blank`
  - `preview incomplete`
  - `sticker not eligible yet`

This makes the no-selection state real rather than only rhetorical.

## 2. blank entry vs quick-start separation

Quick-start was kept, but moved behind explicit application.

- quick-start is now provided through `quick_start_suggestion`
- Explore shows `apply quick-start path` as an explicit action
- preset chips remain visible as optional scaffold
- preset labels were tightened to say:
  - `optional starter picks`
  - `quick-start scaffold only`
  - `not the full runtime object list`

That keeps quick-start available without making it look like default truth.

## 3. residue vs blank-start distinction

Blank reset and residue restore now read as different actions.

- `start blank path`
  - clears object/lens/position back to blank
- `restore last path`
  - appears only when a residue snapshot exists
- Explore explicitly says:
  - blank start is real empty path
  - quick-start is optional
  - residue is not Memory

This separates:

- blank current path
- optional quick-start preset
- restored residue path
- explicit stickered path

## 4. current path strip state distinctions

The current path strip now distinguishes:

- `blank`
- `quick-start applied`
- `residue restored`
- `manually progressed`
- sticker eligibility through preview readiness

Operating also reflects this minimally through:

- `current path state`
- `current path readiness`
- `quick-start active=true` when relevant
- `resumable path available` when residue exists

## 5. remaining watchpoints

- manual selection currently switches path state to `manually progressed` immediately, even if the user only selected one step; this is acceptable but still coarse
- preset chips still remain highly visible, so future polish should avoid making them visually more authoritative than the full runtime list

## 6. next candidates

- refine path-state wording so partially manual progress and fully manual progress read a bit more distinctly without adding workflow heaviness
- validate the new blank-start flow through another short walkthrough against residue restore and first-sticker save
