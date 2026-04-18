# Integrated Engine Execution Packet Schema v0

## 1. Purpose

An execution packet is the compact unit a CLI, sub-agent, or worker can consume.

It must let a worker act without rereading the full conversation history.
It must preserve scope, lens, evidence, validation criteria, allowed actions, forbidden actions, and authority boundary.

This schema is process-camera compatible.
It is not an automation system.

## 2. Required Fields

| field | purpose |
|---|---|
| `packet_id` | unique packet identifier |
| `process_camera_id` | process camera used to shape the work |
| `target_type` | kind of target object being handled |
| `current_purpose` | why this packet exists |
| `scope_boundary` | included / excluded scope |
| `candidate_source_zone` | where candidates/evidence come from |
| `selected_lens_set` | primary and supporting lenses |
| `candidate_list` | selected and rejected candidates |
| `evidence_bundle` | evidence items with support reasons |
| `validation_criteria` | gates to check |
| `allowed_actions` | what worker may do |
| `forbidden_actions` | what worker must not do |
| `expected_output_shape` | required return form |
| `authority_boundary` | status and promotion/rollout limits |
| `why_this_path_was_chosen` | reason this route was selected |

## 3. Worker Readiness Rule

A packet is worker-ready only if:

- target type is clear
- scope boundary is explicit
- selected lens set is named
- evidence bundle is enough for bounded action
- allowed and forbidden actions are explicit
- expected output shape is concrete
- authority boundary prevents promotion/rollout drift

If these are not present, the packet is not worker-ready.

## 4. Bounded Outputs From A Packet

Allowed worker outputs:

- inspection result
- validation result
- candidate comparison
- evidence gap note
- bounded implementation note if allowed
- return record

Forbidden worker outputs unless separately authorized:

- promotion
- rollout
- canonical ingestion
- global protocol
- UI implementation
- automation

## 5. Phase 3 Validation

CLI/sub-agent readiness check:

- schema includes enough context for bounded work without full chat reread

Non-promotional check:

- forbidden actions and authority boundary are required fields

