# External Tool Plan Return Review Template v0

## Status

```yaml
status: review_template_candidate
date: 2026-05-06
baseline_lock: false
automation: false
schema: false
registry: false
```

## Purpose

Review a worker's Set A external-tool planning trial result.

This is a manual Codex/User review template, not an automated parser.

## Source

```text
worker:
prompt_packet:
delivery_route:
review_date:
```

## Gate Review

| gate | pass / hold | evidence |
| --- | --- | --- |
| Pre-Plan Gate |  |  |
| Plan Sizing Gate |  |  |
| Runtime Re-Entry Gate |  |  |
| Closeout / Return-to-Space Gate |  |  |

## Required Checks

```yaml
plan_basis_before_plan:
route_used:
canonical_pvs_used:
broad_bounded_default:
blocking_split_reason_if_any:
non_inspected_scope_stated:
hard_boundary_vs_watch_separated:
return_to_space_value_present:
authority_claim_absent:
```

## Review Label

Choose one:

- `PASS_AS_SPACE_GROUNDED_PLAN`
- `PASS_WITH_WATCH`
- `HOLD_FOR_PLAN_BASIS`
- `HOLD_FOR_BOUNDARY`
- `HOLD_FOR_USER_DECISION`
- `REJECT_MODEL_DEFAULT_PLAN`

## Codex Packaging Decision

```yaml
accepted_values:
corrections_needed:
watch_items:
route_updates:
pv_updates:
movement_record_update:
```

## Do Not

- Do not accept worker output as memory without packaging.
- Do not accept shortened PV aliases in final maps.
- Do not accept authority, baseline, registry, schema, or automation claims.
