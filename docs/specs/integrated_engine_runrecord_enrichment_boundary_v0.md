# Integrated Engine RunRecord Enrichment Boundary v0

## 1. Purpose

This note defines the bounded enrichment layer for RunRecord.

The operating spine already supports basic package continuity. The weak point is that each run still reads like a coarse summary blob. This enrichment projects each run into continuation-friendly fields without replacing the existing session, event, or notebook storage.

## 2. Boundary

This is an adapter/projection layer.

It does not implement:

- full artifact viewer
- streaming terminal
- multi-agent orchestration
- worker switching UX
- cross-package automation
- automatic line / axis detection
- broad UI redesign

## 3. Preferred RunRecord Read Shape

Each run should expose:

- `run_id`
- `package_id`
- `worker`
- `input_packet_id`
- `start_time`
- `end_time`
- `execution_status`
- `route_mark`
- `result_summary`
- `answer`
- `findings[]`
- `files_artifacts[]`
- `next_continue_hint`
- `open_questions[]`
- `risks_or_limits[]`
- `source_refs[]`

`result_summary` remains for compatibility, but notebook reading should prefer the enriched fields.

## 4. Parsing Discipline

The parser must not fake semantic precision.

Current enrichment is intentionally conservative:

- `answer` is the first useful block, falling back to the raw summary.
- `findings[]` are extracted from bullet/numbered lines when possible.
- `files_artifacts[]` combines known session artifact paths with path-like refs extracted from the return text.
- `next_continue_hint` is derived from `suggested_next_use` / route.
- `risks_or_limits[]` explicitly records dry-run and reread-target weakness.
- `source_refs[]` preserves bounded context refs used by the run.

## 5. Known Weakness

The parser is format-sensitive.

Dry-run outputs currently contain fairly regular profile text, so enrichment works, but real worker outputs may vary. If extraction is weak, the enriched record must show partial fields and preserve `result_summary` as fallback.

## 6. UI Use

The package notebook should show:

- latest answer
- findings list
- files/artifacts list
- next continue hint
- open questions / limits

It should not add a new dashboard layer.

## 7. Next Safe Improvement

After this boundary, the next improvement should be to make worker returns emit a more stable structured return shape, not to widen the UI.
