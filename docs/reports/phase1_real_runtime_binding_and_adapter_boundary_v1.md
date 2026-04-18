# phase1 real-runtime binding and adapter boundary v1

## package status

complete for this turn

## files changed

- [operating_ui_phase1_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1_adapter.py)
- [operating_ui_phase1.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1.py)
- [run_phase1_interaction_invariant_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_phase1_interaction_invariant_probe.py)
- [phase1_real_runtime_binding_and_adapter_boundary_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_real_runtime_binding_and_adapter_boundary_v1.md)

## 1. runtime sources connected

The phase1 surface is now bound to existing runtime sources through a thin adapter.

Connected sources:

- Operating current run:
  - `live.process_console_summary`
- Operating detail / activity / compare hint:
  - `live.debug_text.detail_summary`
  - `live.debug_text.activity`
  - `live.debug_text.compare_panel`
- Explore object options:
  - `live.available_assets`
- Search candidate base:
  - adapted Explore object options
  - explicit saved paths from sticker store
- Memory:
  - `runtime/manifests/operating_ui_phase1/phase1_memory_stickers.jsonl`
- Residue:
  - `runtime/manifests/operating_ui_phase1/phase1_current_path_residue.json`

## 2. adapter boundary

The adapter lives in:

- [operating_ui_phase1_adapter.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operating_ui_phase1_adapter.py)

It exposes phase1-facing view-model fields rather than raw live naming:

- `operating_observation`
- `explore_binding`
- `search_binding`
- `memory_binding`
- `similar_binding`
- `source_map`

This keeps phase1 semantics from being directly defined by live runtime field names like `available_assets` or `debug_text`.

## 3. how raw runtime naming is prevented from overriding phase1 semantics

The main protections added are:

- raw `live_data` is no longer the primary source for Operating rendering
- object options now come through `explore_binding.objects`
- Search reads adapter source state and note instead of implying a fully independent search source
- source availability is shown as `runtime adapter=...` rather than leaking raw payload structure into surface copy

Phase1 still keeps its own terms:

- current path
- explicit saved path
- active seed context
- local re-query

## 4. fallback / degraded mode

Fallback behavior now stays explicit and thin:

- missing live current run:
  - `current run source unavailable`
- missing detail summary:
  - `detail summary source unavailable`
- missing activity:
  - `recent activity source unavailable`
- missing object options:
  - `runtime object source missing / degraded fallback mode`
- sparse search source:
  - `search candidate source sparse / degraded fallback mode`

This keeps `missing data` separate from `broken feature`.

## 5. probe update

The invariant probe now checks one more runtime-bound case:

- runtime unavailable mode still exposes blank start
- no auto selected memory on load
- no auto active seed on load
- degraded search note remains available

Probe script:

- [run_phase1_interaction_invariant_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_phase1_interaction_invariant_probe.py)

## 6. still not connected and why

Not directly connected yet:

- raw board/view structures as first-class phase1 Explore taxonomy
  - avoided because this would let runtime board naming bleed into phase1 semantics
- broader runtime manifests as Similar source
  - avoided because Similar still owns only seed-based local re-query semantics
- compare candidate data as phase1 source
  - avoided because compare track remains parked

## 7. next candidates

- run one short walkthrough in `live_ready` and `live_unavailable` modes to confirm the adapter wording still reads cleanly in the UI
- tighten object fallback behavior only if runtime sparse mode proves too thin for practical Explore use
