# phase1 memory-seed loop activation v1

## 1. status

- package status:
  **complete for thin phase1 loop closure**

중요:
- 이번 구현의 목표는 정교한 semantic intelligence가 아니라
  `Explore -> Memory -> Similar` 최소 loop를 실제로 닫는 것이었다
- recommendation semantics, compare 재개, whole-space derivation, automatic memory는 넣지 않았다

## 2. files created / modified

### created

- [phase1_memory_seed_loop_activation_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_memory_seed_loop_activation_v1.md)

### modified

- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)

## 3. sticker storage path

sticker persistence is now stored through:
- `runtime/manifests/operating_ui_phase1/phase1_memory_stickers.jsonl`

storage style:
- thin JSONL
- append-only through `JsonlEventStore`
- no DB migration
- no schema finalization

minimum stored shape:
- `sticker_id`
- `created_at`
- `object_id`
- `lens_id`
- `position_value`
- `preview_connection_summary`
- `why_selected`
- `seed_ref`

중요:
- this is only a phase1 interaction record shape
- it is not treated as final ontology schema

## 4. how the loop now closes

### Explore

- a sticker can be saved only when `object / lens / position / preview` are all present
- the save action is explicit
- `why selected` is collected through a thin prompt with a default sentence

### Memory

- saved stickers are loaded from runtime persistence
- the Memory surface shows sticker-only rows with
  - object
  - lens
  - position
  - preview summary
  - why_selected
  - created_at
- selecting a sticker also activates the similar seed path

### Similar

- Similar now uses the selected sticker or `seed_ref`
- results are shown as thin local re-query matches
- each result shows a thin `why it touches seed` explanation and a confidence label like `thin-match` or `low-confidence`
- result cards do not auto-save; explicit sticker save remains required

### Operating linkage

- Operating was kept thin
- only a minimal sticker hint block was added:
  - recent sticker created
  - selected seed active

## 5. derivation rule and current weakness

current similar derivation is intentionally weak.

what it does:
- derives local matches from saved sticker seed fields
- reuses `object_id`, `lens_id`, `position_value`, and `preview_connection_summary`
- produces thin local match reasons instead of pretending to be recommendation intelligence

what is still weak:
- similar results are still heuristic placeholders
- match reasoning is token-level and shallow
- no richer runtime-informed local structure engine exists yet

이 약함은 이번 턴에서 허용된 범위다.
이번 목표는 derived intelligence가 아니라 seed-based local re-query structure였다.

## 6. package completeness

- package completeness:
  **complete for the intended thin loop**

무엇이 아직 intentionally thin한가:
- `why_selected` 입력은 prompt 기반
- detail/modal은 여전히 thin JSON-backed detail
- similar derivation은 local heuristic 수준

## 7. next natural candidates

1. memory authoring refinement
- replace prompt-based `why_selected` capture with a slightly cleaner in-surface thin input

2. similar derivation refinement
- improve seed-to-result touch logic while still keeping it local, sparse, and non-recommendation
