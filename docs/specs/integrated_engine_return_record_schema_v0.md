# Integrated Engine Return Record Schema v0

## 1. Purpose

A return record is the structured result that comes back into the integrated engine after a process-camera-shaped execution packet is handled.

It is not a free-form answer.
It is a redeposit-ready record of what was attempted, what evidence was used, which gates passed or failed, what decision was made, and what should happen next.

## 2. Required Fields

| field | purpose |
|---|---|
| `return_id` | unique return record identifier |
| `source_packet_id` | execution packet that produced the return |
| `process_camera_id` | process camera used |
| `target_type` | target type handled |
| `attempted_actions` | what the worker actually did |
| `evidence_used` | evidence actually used |
| `gate_results` | validation gates and outcomes |
| `insufficiency_or_risk` | weak evidence, drift, or blocked conditions |
| `final_decision` | usable / weakly / hold / supplement / insufficient / blocked |
| `action_output_or_reference` | output artifact or reference |
| `what_was_not_done` | explicit non-actions |
| `redeposit_payload` | what returns to the space/engine |
| `next_valid_use` | next bounded use |
| `authority_boundary_confirmation` | confirmation that status and guardrails stayed intact |

## 3. Return Strength Rule

A return record is strong enough for redeposit when:

- it names the source packet
- it states what was attempted
- it maps evidence to gate results
- it distinguishes direct / weak / not yet / blocked
- it names what was not done
- it keeps authority boundary intact

If those are missing, return should be held as incomplete.

## 4. Allowed Final Decisions

Use only bounded decisions:

- `directly`
- `weakly`
- `not_yet`
- `usable_for_bounded_action`
- `usable_for_inspection_only`
- `supplement_needed`
- `hold`
- `insufficient`
- `blocked`

Do not use:

- `promoted`
- `canonical`
- `rollout_ready`
- `global_standard`

## 5. Phase 3 Validation

Redeposit readiness check:

- schema records evidence, gates, risk, decision, and next use

Non-promotional check:

- schema requires `what_was_not_done` and `authority_boundary_confirmation`

