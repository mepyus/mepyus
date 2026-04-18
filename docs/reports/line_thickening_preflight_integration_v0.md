# line thickening preflight integration v0

## Verdict

**PASS**

## What was integrated

The existing runtime preflight path now has an opt-in hook into `line_thickening`.

The hook is bounded and does not change default reread behavior.

## Files changed

- `app/core/runtime/line_thickening.py`
- `scripts/run_runtime_preflight.py`
- `docs/notes/line_thickening_preflight_hook_note_v0.md`
- `docs/reports/line_thickening_preflight_integration_v0.md`

## Hook decision

The hook was attached to `scripts/run_runtime_preflight.py` because that is the actual entrypoint that already:

- builds the preflight decision
- appends the breadcrumb
- writes the phase decision
- optionally appends pipeline observations

That makes it the least destructive place to attach line thickening as a sink.

## Opt-in behavior

The new flag is:

- `--record-line-thickening`

When the flag is off, the existing preflight path is unchanged.

When the flag is on, the hook emits line-centered reread observations for the active latent lines selected by the preflight gate.

## Observation mapping

The hook maps the preflight output into `RereadObservation` packets using:

- `line_name` from active latent lines
- `asset_or_surface` from the first read target or the reread surface
- `view_type` from selected mode
- `evidence` from the preflight decision
- `grounding_type` as direct
- `support_points`, `weakness_points`, `resistance_or_counterexample`
- `next_probe_surface`
- `thickness_before`
- `thickness_after`

## Verification

Verified with an actual runtime preflight run:

```bash
python3 scripts/run_runtime_preflight.py runtime --mode space_reading --ref inputs/external_cases/enterprise.txt --record-observation --record-line-thickening
```

Result:

- `pre_read_eye` produced a line-thickening observation packet
- `raw_return_preservation` produced a line-thickening observation packet
- both were appended to `runtime/logs/reread_observation_log.jsonl`
- both updated `runtime/manifests/line_registry.json`
- both wrote promotion records to `runtime/logs/line_promotion_log.jsonl`
- both remained conservatively at `candidate / thin`

The existing preflight breadcrumb and phase flow stayed intact.

## Behavior preserved

- The original preflight decision still drives mode selection.
- The breadcrumb still records judgment movement.
- The pipeline observation registry still remains separate from line thickening.
- The line registry remains a derived summary surface, not the truth archive.
- The new hook did not change the default preflight decision or its output shape.

## Remaining risks

- Exact-duplicate suppression is implemented; fuzzy dedupe is not.
- The current mapping is only as good as the active latent lines selected by preflight.
- The hook is intentionally narrow and not yet wired into every possible reread entrypoint.
- The current mapping is conservative and can stay thin until more real reread runs accumulate.

## Deferred

- no UI
- no ontology lift
- no broad refactor
- no full automation of line promotion
- no move of line thickening into the candidate / phase / hold subsystems
