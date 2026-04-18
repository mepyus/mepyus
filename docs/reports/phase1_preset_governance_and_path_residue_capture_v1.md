# phase1 preset governance and path residue capture v1

## package status

complete for this turn

## files changed

- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)
- [phase1_preset_governance_and_path_residue_capture_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_preset_governance_and_path_residue_capture_v1.md)

## 1. preset governance visibility

Preset governance was made explicit in both UI language and code shape.

- object starter area now says `starter picks / quick start only / not the full runtime object list`
- lens area now says `phase1 presets / quick start scaffold / runtime list remains below`
- position area now says `quick position presets for the current lens / not locked field taxonomy`
- Explore boundary repeats that preset support is scaffold only, not final taxonomy or ontology

This keeps preset-first convenience without letting presets read like a hidden source of truth.

## 2. residue vs sticker distinction

The UI now distinguishes three different things:

- preset:
  - quick-start scaffold
- current path residue:
  - in-progress path snapshot
- sticker:
  - explicit saved interpretation path

Residue is shown only inside Explore and as a very small Operating hint. It does not appear in Memory and does not activate Similar as a seed by itself.

## 3. residue storage location and shape

Residue is stored as a latest-snapshot JSON file:

- `runtime/manifests/operating_ui_phase1/phase1_current_path_residue.json`

Current minimum shape:

- `object_id`
- `lens_id`
- `position_value`
- `preview_ready`
- `updated_at`

This is intentionally lighter than sticker persistence and does not use the sticker JSONL path.

## 4. restore flow

Restore was kept thin and explicit.

- selecting object/lens/position updates the in-progress residue snapshot
- Explore shows `current path residue` when a resumable snapshot exists
- Explore exposes a `restore last path` button
- Operating only shows `resumable path available` as a thin hint

No wizard, heavy autosave UX, or Memory promotion was added.

## 5. still-thin or placeholder parts

- residue is a single latest snapshot, not a path history
- restore is manual and local to Explore
- residue does not capture `why_mode` or free-form authoring state, only the structural path

## 6. next candidates

- add a thinner visual contrast between active current path and restored residue state
- decide whether first successful sticker save should clear or retain residue while keeping the boundary explicit
