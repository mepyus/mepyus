# line thickening runtime insertion report v0

## What was added

Added a thin runtime slice for line thickening:

- `line_registry`
- `reread_observation_log`
- `promotion_rule`

## Files added

- `docs/specs/line_thickening_runtime_insertion_v0.md`
- `app/core/runtime/line_thickening.py`
- `app/runtime/line_thickening.py`
- `scripts/run_line_thickening_sample.py`
- generated demo artifacts under `runtime/line_thickening_demo_v2/`

## Why this placement

- `docs/specs` holds the behavioral contract.
- `app/core/runtime` holds the reusable helper/service logic.
- `app/runtime` re-exports the runtime-facing entrypoint, matching the existing wrapper pattern.
- `scripts/` holds the runnable sample fixture instead of inflating the runtime itself.

## What the runtime surfaces are

### `runtime/line_thickening_demo_v2/manifests/line_registry.json`

- current line summary
- derived from observation packets
- keeps line status, thickness, support/resistance counts, and seen surfaces

### `runtime/line_thickening_demo_v2/logs/reread_observation_log.jsonl`

- append-only reread packets
- contains support, weakness, resistance, and next probe
- exact duplicate observations are suppressed

### `runtime/line_thickening_demo_v2/logs/line_promotion_log.jsonl`

- append-only promotion evaluator records
- shows why a line stayed thin, moved to medium, or became thick/operating

## What the sample showed

The sample run used a small line set to confirm:

- one line-centered observation packet appends cleanly
- the registry updates from that packet
- promotion stays conservative
- exact duplicate observations are not re-appended

## What is intentionally not implemented

- no graph or ontology lift
- no UI work
- no full automation pipeline
- no hard promotion rules
- no broad refactor of existing phase / hold / candidate infrastructure

## Why this is useful

This gives the space a minimal record base where rereading itself thickens lines over time without turning every observation into a locked structure.
