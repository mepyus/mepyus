# phase1 cross-surface jump contract refinement v1

## package status

complete for this turn

## files changed

- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [phase1_cross_surface_jump_contract_refinement_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_cross_surface_jump_contract_refinement_v1.md)

## 1. surface ownership definition

Ownership is now reinforced as:

- Explore:
  - owns current path authoring
- Memory:
  - owns explicit saved sticker selection
- Similar:
  - owns active seed context and local re-query view
- Search:
  - does not own long interpretation flow
  - only offers explicit jump/import actions
- Operating:
  - remains observation only

This is now visible in the shared spine wording and in surface-local helper text.

## 2. jump action import rules

Current explicit import behavior:

- `open in Explore`
  - imports only path-relevant fields
  - no memory creation
  - no seed activation
- `open in Memory`
  - imports only `selected_memory_sticker_id`
  - does not activate Similar seed
- `use in Similar`
  - imports only `similar_seed_ref`
  - does not auto-create memory
  - does not require Search to own sticker selection
- `restore last path`
  - imports residue back into Explore only

## 3. automatic mutation now prevented

The main hidden mutations reduced in this turn are:

- no automatic selected sticker or active seed on initial page load
- Memory selection no longer auto-jumps to Similar
- Memory selection no longer auto-activates seed
- Search result row itself is not a jump; explicit button action is required
- Similar seed activation is now explicit from Memory or Search

## 4. imported-from context visibility

Thin imported context visibility was added through:

- Explore preview:
  - `imported from=...`
- Memory selected sticker panel:
  - `imported from=...`
- Similar seed panel:
  - `imported from=...`
- Operating:
  - `current jump target`
  - `import source`

This stays subtle but readable and avoids a large activity log.

## 5. clear / detach affordance

Explicit detach controls now exist:

- Explore:
  - `clear imported context`
- Memory:
  - `clear imported context`
- Similar:
  - `clear active seed`
  - `clear imported context`

These do not delete stickers or memory assets. They only remove current imported linkage or active seed state.

## 6. remaining ambiguity or watchpoints

- Explore imports and quick-start application both currently read as imported context; this is workable but still semantically close
- Similar seed switching inside Similar currently marks itself as a new import context, which is readable but still fairly lightweight
- direct jump hints in Operating are intentionally minimal, so they help trace state ownership but are not a full debugging surface

## 7. next candidates

- run a short scenario validation specifically for Search -> Memory, Memory -> Similar, and Search -> Similar after this contract change
- tighten wording around self-originated Similar seed switching if it starts to feel too much like import rather than local control
