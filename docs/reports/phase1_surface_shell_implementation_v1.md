# phase1 surface shell implementation v1

## 1. status

- package status:
  **complete for structure-first phase1 shell**

중요:
- 이 구현은 phase1의 다섯 면을 구분하고 shared interaction spine을 얇게 붙이는 데 초점을 둔다
- 깊은 엔진 로직, recommendation semantics, whole-space view, compare track 재개는 이번 턴 범위 밖에 뒀다

## 2. files changed

### created

- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [phase1_surface_shell_implementation_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_surface_shell_implementation_v1.md)

### modified

- [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)
- [operating_ui_live.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_live.py)

## 3. what was implemented

### new phase1 shell route

- added `/operating-ui-phase1` and `/api/operating-ui-phase1`
- the new route wraps the existing operating live data instead of replacing the old live surface
- existing `/operating-ui-live` remains intact

### five-surface shell

the phase1 shell now exposes:
- `Operating`
- `Explore`
- `Search`
- `Memory`
- `Similar`

### thin shared interaction spine

the client-side shared spine now carries:
- `selected_object_id`
- `selected_lens_id`
- `selected_position_value`
- `current_preview_connection`
- `selected_memory_sticker_id`
- `similar_seed_ref`

중요:
- this is a thin interpretation path spine only
- it does not attempt to finalize ontology schema or back-end state contracts

## 4. how phase1 boundaries show up in UI

### Operating

- keeps the current operating read thin
- shows current run summary, selected asset/state, recent activity, and compare hint only
- compare is explicitly kept as a hint and not resumed as a working track

### Explore

- makes the path visible as
  `object -> lens -> position -> preview -> optional sticker -> optional detail`
- treats connection preview as something that wakes up after lens + position selection
- adds an explicit `promote to memory sticker` action instead of any automatic memory behavior

### Search

- uses one search input and grouped result buckets
- does not force the user to predeclare object vs lens vs position vs connection vs memory
- does not reuse the explore path slots

### Memory

- only shows stickered items
- preserves a thin `why stickered` slot
- keeps click history out of memory

### Similar

- works from sticker seeds only
- frames results as local similar structures, not recommendations
- allows optional restickering explicitly, never automatically

## 5. placeholder / thin-functional areas

the following are intentionally thin or placeholder-grade in this turn:

- lens options are phase1 shell presets, not deep engine-derived lens logic
- position values are limited shell placeholders to make the explore flow legible
- similar results are local re-query placeholders driven by sticker seeds and current object context
- memory stickers are only lightly seeded from the current operating selection and explicit promote actions
- detail/modal content is still thin JSON-backed detail, not a rich dedicated detail surface

## 6. preservation of existing operating live surface

- existing operating live composition was preserved
- only a navigation link to `/operating-ui-phase1` was added in the live top nav
- the phase1 shell reuses live composition data rather than replacing the live route

## 7. verification

verified with:
- `python3 -m py_compile app/runtime/operating_ui_phase1.py app/runtime/operating_ui_live.py app/core/runtime/viewer_server.py`
- a direct render check that confirmed:
  - phase1 shell data builds successfully from `runtime/`
  - all five surfaces render into HTML
  - the shared interaction spine and new route are present

## 8. next natural candidates

1. thin explore surface refinement
- replace placeholder lens/position presets with more runtime-informed but still bounded interpretation inputs

2. similar surface seed refinement
- improve how sticker-seeded local re-query results are derived while keeping recommendation/whole-space drift out
