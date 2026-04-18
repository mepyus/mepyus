# State Change Attention Queue v1

## Purpose
- Expose which recent state changes deserve operator attention first.
- Keep queue as an operating attention surface, not a task list.

## Source
- Canonical latest state
- Adjacent history diff
- Interpretation badges
- Runtime evidence priority router output

## Queue Item Fields
- `asset_id`
- `latest_updated_at`
- `priority_level`
- `attention_reason`
- `diff_class`
- `interpretation_badges`
- `changed_fields`
- `update_trigger_type`
- `update_reason`
- `evidence_refs_count`
- `queue_status`
- `enqueued_at`

## Queue Status
- `new`
- `seen`
- `deferred`
- `resolved`
- `suppressed`

## Active Queue Rule
- Include `critical`
- Include `high`
- Include meaningful `medium`
- Exclude `low/background provenance_only` from active queue

## Background Summary Rule
- Repeated provenance-only runtime updates are summarized instead of queued one by one.
- Summary node is derived and never treated as canonical history.

## Process Console Link
- Queue item must jump to the selected asset process console.
- Process console then exposes latest state, recent lineage, and adjacent diff.

## Guards
- No raw history deletion
- No canonical field mutation
- No `experimental_namespace`-driven priority promotion
