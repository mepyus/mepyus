# phase2 semantic boundary and invariant probe lock v1

## package status

complete for this turn

## wording audit and cleanup

- kept `history`, `trace`, `reread preview`, `prior state slice`, and `open in phase1 with reread context`
- reduced replay drift by shifting the visible page title from `history / replay / trace` to `history / reread / trace`
- renamed `Replayable State Preview` to `Rereadable State Preview`
- kept degraded/unavailable wording honest without making it sound like execution failure

## invariants checked in probe

### history_surface_invariants

- `history surface is readable with available runtime data`
- `reread preview stays available as view-level slice when source exists`
- `trace entries remain translated/operator-facing units`
- `sparse root resolves to source_unavailable rather than execution failure`
- `sparse mode shows honest unavailable wording`
- `sparse mode keeps reread preview honesty wording`

### cross_surface_handoff_invariants

- `open from history attaches reread context only`
- `history handoff does not create saved path selection`
- `history handoff does not activate seed`
- `history handoff does not overwrite current path authoring`
- `history handoff carries summary reference only`

### wording_presence_sanity

- `history surface title uses reread wording`
- `phase1 handoff wording uses reread context`
- `reread preview wording keeps execution boundary explicit`
- `trace wording stays translated rather than raw`
- `forbidden replay-in-phase1 wording is absent`
- `forbidden restore-state wording is absent`
- `forbidden load-state wording is absent`

## still governance-level only

- cluster quality still needs periodic manual reading because grouping quality cannot be fully asserted from tokens alone
- translated trace readability is only partially assertable in shell data; final operator-facing nuance still needs manual walkthrough
- degraded honesty tone can still drift visually without failing these token checks

## freeze-candidate note

### already locked

- read-oriented time-axis companion
- replay means view-level reread only
- trace means translated operator-facing reading unit
- phase1 handoff remains explicit contextual reference only

### still open

- richer clustering quality
- source sparsity handling polish
- readability and wording trim

## anti-drift rules

- history surface must not become command center
- replay must not drift into execution
- trace must not drift into raw audit console
- phase1 handoff must remain contextual reference only
- saved-path curation is still outside this surface

## watchpoints

- `replay` still exists in internal naming, so visible wording must keep favoring `reread`
- sparse history can still make cluster quality feel thinner than the labels imply
- token probes do not fully guarantee visual tone or operator trust
