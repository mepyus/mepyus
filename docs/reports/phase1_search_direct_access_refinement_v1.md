# phase1 search direct-access refinement v1

## package status

complete for this turn

## files changed

- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [phase1_search_direct_access_refinement_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_search_direct_access_refinement_v1.md)

## 1. search result grouping

Search is now grouped as direct-access result groups rather than a flat list.

Current groups:

- objects
- lenses
- positions
- stickers / memory
- seed-relevant traces

These groups stay thin and local to current phase1 runtime assets.

## 2. match_reason / matched_in visibility

Search now surfaces thin match context through:

- `direct match` or `partial match`
- `matched in ...` badge

Current `matched_in` examples include:

- `object id`
- `object label`
- `lens id`
- `lens label`
- `position id`
- `position label`
- `sticker summary`
- `why_selected_short`
- `why_mode`
- `saved path summary`

This keeps Search readable without turning it into a heavy ranking system.

## 3. search-to-surface jump contract

Each result now exposes an explicit jump action.

- object result:
  - `open in Explore`
- lens result:
  - `open in Explore`
- position result:
  - `open in Explore`
- sticker result:
  - `open in Memory`
- seed-relevant trace:
  - `use in Similar`

The jump stays explicit through button actions. Search does not auto-trigger memory creation or hidden seed activation.

## 4. no query / no direct match / partial match handling

Search now distinguishes:

- no query:
  - `search is idle until you ask for direct access`
- direct hits present:
  - summary shows direct and partial hit counts
- no direct hits but partial hits exist:
  - summary shows `partial matches only`
- no direct and no partial hits:
  - summary shows `no direct matches / no partial matches`

Group-level empty states also reflect whether the issue is:

- no query yet
- no direct hit in that group
- only partial or no local hit in that group

## 5. operating linkage

Operating now keeps only minimal Search linkage:

- `last search query`
- `direct hits`
- `current jump target`

This keeps Search visible without expanding Operating into a search workspace.

## 6. still-thin or placeholder parts

- search matching remains simple substring matching over local phase1 fields
- seed-relevant traces are derived from saved stickers, not a separate trace index
- Search does not yet distinguish richer ambiguity classes beyond direct vs partial

## 7. next candidates

- validate search jump behavior through a short surface-to-surface walkthrough after first sticker exists
- tighten wording on seed-relevant trace cards if they begin to feel too close to Similar result semantics
