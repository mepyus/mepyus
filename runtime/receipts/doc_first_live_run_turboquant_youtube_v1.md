# doc_first_live_run_turboquant_youtube_v1.md

- operation_date: 2026-03-29
- operation_scope: first end-to-end live run on `turboquant_youtube`
- prepared_by: Codex

## changed assets

- `app/work/dialogue_loop_test/generated/turboquant_youtube_live_run_v1_w6_s3_20260328T212851Z.json`
- `runtime/state/engine_state_history/turboquant_youtube.jsonl`
- `runtime/views/engine_state_latest/turboquant_youtube.json`
- `runtime/views/engine_state_latest/index.json`
- `runtime/views/state_change_attention_queue/index.json`
- `runtime/views/state_attention_memory/turboquant_youtube.json`
- `runtime/views/state_attention_memory/index.json`
- `docs/reports/first_live_run_turboquant_youtube_v1.md`

## validation

- located source file: `inputs/external_cases/TurboQuant_youtube.txt`
- executed probe:
  - `python3 scripts/run_dialogue_asset_probe.py --input inputs/external_cases/TurboQuant_youtube.txt --label turboquant_youtube_live_run_v1 --window-size 6 --stride 3`
- appended first canonical state via `EngineStateStore.append_state(...)`
- refreshed derived queue + memory surfaces
- built process console payload for `asset_id=turboquant_youtube`

## result

- first live input passed through source -> probe packet -> canonical state -> latest/history -> diff/attention/memory
- packet was read conservatively as `overcompressed_closure_heavy`
- process console reads:
  - latest: loaded
  - history: loaded
  - diff: `no_previous_state`
  - attention: `no_previous_state_anchor`
  - memory: `insufficient_attention_history`
