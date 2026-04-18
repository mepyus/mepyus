# line thickening grounding hardening v0

## Verdict

**PASS**

## What changed

The existing preflight-connected line thickening slice now records provenance-like anchor fields and treats `summary_echo` observations conservatively.

## Files changed

- `app/core/runtime/line_thickening.py`
- `docs/notes/line_thickening_grounding_hardening_v0.md`
- `docs/reports/line_thickening_grounding_hardening_v0.md`
- `docs/reports/today_handoff_index_v1.md`

## Grounding decision

The new observation anchor shape is:

- `source_kind`
- `source_path_or_ref`
- `source_run_id_or_event_id`
- `source_pointer`
- `evidence_mode`

The current preflight hook classifies its own packets as `summary_echo`, because they are derived from the preflight decision / phase summary rather than a direct span.

That is the correct classification for this entrypoint.

## Behavior summary

- `summary_echo` observations remain at `candidate / thin`
- `medium` requires a `source_linked` or `direct_span` packet
- `thick` requires at least one `direct_span` and recurrence across distinct runs or distinct asset/surface families

The registry remains a derived current-state surface.
The logs remain the truth archive.

## Verification

Verified with the actual preflight path:

```bash
python3 scripts/run_runtime_preflight.py runtime --mode space_reading --ref inputs/external_cases/enterprise.txt --record-observation --record-line-thickening
```

Observed result:

- `pre_read_eye` carried anchor fields and remained `candidate / thin`
- `raw_return_preservation` carried anchor fields and remained `candidate / thin`
- both observations were written to `runtime/logs/reread_observation_log.jsonl`
- both registry rows were updated in `runtime/manifests/line_registry.json`
- both promotion entries remained conservative in `runtime/logs/line_promotion_log.jsonl`

## Why this was needed before widening

Without anchor classification, summary-level control-plane output could be mistaken for strong reread evidence.
This hardening keeps the line-thickening slice honest and prevents accidental inflation from preflight echo.

## Deferred

- no other reread entrypoints
- no UI
- no graph / ontology lift
- no fuzzy dedupe
- no broad refactor
- no phase / hold / candidate integration
