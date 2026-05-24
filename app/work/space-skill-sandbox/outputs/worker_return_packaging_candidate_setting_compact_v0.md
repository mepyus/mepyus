# Worker Return Packaging Candidate Setting Compact v0

## Status

```yaml
status: candidate_operating_setting
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
current_position_update: false
```

## Setting

Use this when receiving a broad-bounded external worker return that must be recovered into VectorFL space.

## Candidate Return Shape

```yaml
worker_role:
input_purpose:
anchors_used:
how_anchors_changed_behavior:
tool_output_summary:
evidence_pointers:
not_inspected_scope:
issues_or_watch_items:
return_to_space_value_candidate:
do_not_promote:
```

## Raw Trace Boundary

```text
worker prose
tool logs
QMD score / docid / URI / snippet
model confidence
unread source claims
body bundle text
```

## Codex Recovery

```text
downshift claims
separate evidence / not-inspected / gap
extract reusable judgment
classify HOLD vs WATCH
write one package-level Movement Record only if reusable judgment exists
```

## Micro-Run Prevention

```text
Gemini / external carrier handles internal small execution.
Codex does not create a run for each search/read/review step.
Codex recovers only the packaged result.
```

## Do Not Promote

```text
not schema
not automation
not registry
not baseline
not current-position update
not interpreted memory before Codex recovery
```

`STATUS: WORKER_RETURN_PACKAGING_CANDIDATE_SETTING_COMPACT_PREPARED`
