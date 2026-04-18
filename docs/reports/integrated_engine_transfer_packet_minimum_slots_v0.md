# Integrated Engine Transfer Packet Minimum Slots v0

Date: 2026-04-15

## 0. purpose

This document is a working draft, not a final schema.

The goal is to reduce communication friction between:

- User surface
- VectorFL surface
- Engine surface

It defines a minimum shared carrier for request, return, and reflux movement.

Do not read this document as:

- final DB schema
- final enum set
- canonical state machine
- automatic routing design
- team assignment lock

Read it as:

- setup language for low-intensity operating tests
- a common packet grammar for moving purpose, anchor, judgment, action, validation, and reflux context between surfaces

## 1. why transfer packets exist

Current problem:

- Requests exist.
- But purpose, direction, reference criteria, judgment state, next action, and reflux target can dissolve inside free conversation.

Transfer packets exist because the surfaces need a common carrier that preserves:

- why the request exists
- what direction it has
- what anchors it uses
- how far judgment has progressed
- what should happen next
- where results or traces should return

Key sentence:

> A transfer packet is not only a message. It is a common carrier that moves purpose, criteria, state, and next action together.

## 2. packet kinds v0

v0 uses only three packet kinds:

- `request`
- `return`
- `reflux`

### request packet

Used when asking for work, verification, search, reread, processing, or extraction.

### return packet

Used when engine-side or external processing sends a result back upward.

### reflux packet

Used when lines, axes, interpretations, traces, or process memory produced during work must be returned to the space as maturation material.

Important boundary:

- These three kinds are enough for v0 operating tests.
- Do not split into detailed team-specific packet families yet.

## 3. common slots v0

All packet kinds share these slots:

| slot | meaning | note |
| --- | --- | --- |
| `packet_id` | Packet identifier | Needed for trace and reflux. |
| `packet_kind` | Packet kind | `request`, `return`, or `reflux` in v0. |
| `source_surface` | Where the packet comes from | Example: `user_surface`, `vectorfl_surface`, `engine_surface`. |
| `target_surface` | Where the packet should move | Surface or space target. |
| `purpose` | Why this packet exists | The operating reason. |
| `directionality` | What direction the action has | Example directions are illustrative, not final enums. |
| `anchor_refs` | Reference anchors used for judgment | Keeps packets attached to baseline criteria. |
| `related_objects` | Objects related to this packet | Lines, axes, harvests, briefs, manifests, etc. |
| `current_judgment_state` | How far judgment has progressed | Example values are illustrative. |
| `requested_or_next_action` | What should happen next | Search, inspect, compare, validate, return, reflux, etc. |
| `validation_points` | What must be checked | Anchor fit, evidence density, duplicate risk, reflux value, etc. |
| `reflux_need` | Whether the result should return to space | `yes`, `no`, or `maybe` as working labels. |
| `packet_status` | Current packet movement status | Example values are illustrative, not final state machine. |

## 4. minimum required slots

For low-intensity v0 operation, the true minimum shared slots are:

- `packet_kind`
- `source_surface`
- `target_surface`
- `purpose`
- `directionality`
- `anchor_refs`
- `requested_or_next_action`
- `packet_status`

Type-specific minimum slots:

### request minimum

- `input_materials`
- `expected_output_shape`

### return minimum

- `return_summary`
- `suggested_next_route`

### reflux minimum

- `reflux_target_zone`
- `maturation_value`

## 5. request packet additional slots

Request packets may add:

| slot | meaning |
| --- | --- |
| `request_type` | Kind of request, such as engine job, external search, validation, reread, or extraction. |
| `requested_team_or_executor` | Executor candidate. This remains extension language unless relocked. |
| `input_materials` | Materials used as input. |
| `expected_output_shape` | Shape expected from the return. |
| `external_support_need` | Whether external support is needed. |
| `urgency_level` | Low / medium / high as working labels, not final enum. |

Boundary:

- `requested_team_or_executor` is an operating-extension field.
- It must not promote team routing or standing assignment into body skeleton.

## 6. return packet additional slots

Return packets may add:

| slot | meaning |
| --- | --- |
| `return_summary` | Short result summary. |
| `produced_artifacts` | Produced or confirmed artifacts. |
| `result_confidence` | How far the result can be trusted. |
| `open_questions` | Questions not resolved by the return. |
| `needs_followup` | Whether more action is needed. |
| `suggested_next_route` | Where the packet should move next. |

Important return language:

- `report return != product completion`
- `return artifact != chat-only note`
- `return includes trace-memory`
- `latest completed != current truth without freshness gate`

## 7. reflux packet additional slots

Reflux packets may add:

| slot | meaning |
| --- | --- |
| `reflux_target_zone` | Where the material should return. |
| `reflux_reason` | Why the material should return. |
| `maturation_value` | What maturation value this material has. |
| `linked_lines_or_axes` | Related lines or axes. |
| `preserve_trace_items` | Trace items that must not be lost. |

Reflux packet principle:

- Reflux is not completion.
- Reflux is preserving returned material so it can become future reread, comparison, line, axis, or process-memory material.

## 8. example flow 1 - user surface to VectorFL surface

User utterance:

> 이 축 후보를 보강할 외부 자료가 있는지 찾아보자.

Working packet:

```text
packet_kind: request
source_surface: user_surface
target_surface: vectorfl_surface
purpose: axis candidate enrichment
directionality: enrichment
anchor_refs: [integrated_engine_3_surface_baseline]
related_objects: [axis_candidate_alpha]
current_judgment_state: candidate
requested_or_next_action: inspect_and_route
validation_points: [axis evidence density, external enrichment need]
reflux_need: maybe
packet_status: created

request_type: external_search
requested_team_or_executor: vectorfl_surface
input_materials: [axis_candidate_alpha, related_line_bundle_02]
expected_output_shape: evidence note + relevant sources
external_support_need: yes
urgency_level: medium
```

Reading:

- The user surface gives purpose and direction.
- The VectorFL surface should not bypass intermediate reading.
- The VectorFL surface inspects, adds validation points, and only then routes or asks the engine/tool layer.

## 9. example flow 2 - engine surface to VectorFL surface

Working packet:

```text
packet_kind: return
source_surface: engine_surface
target_surface: vectorfl_surface
purpose: external enrichment result
directionality: enrichment
anchor_refs: [integrated_engine_3_surface_baseline]
related_objects: [axis_candidate_alpha, search_result_bundle_07]
current_judgment_state: under_review
requested_or_next_action: validate_and_decide
validation_points: [relevance, axis value, duplicate risk]
reflux_need: maybe
packet_status: returned

return_summary: external materials show medium/high relation to axis_candidate_alpha
produced_artifacts: [search_result_bundle_07, comparison_note_03]
result_confidence: medium
open_questions: [unclear whether this is enough for axis promotion]
needs_followup: yes
suggested_next_route: vectorfl_validation
```

Reading:

- The engine returns result and trace.
- VectorFL validates and decides the next route.
- Return does not equal completion.

## 10. example flow 3 - VectorFL surface to space reflux

Working packet:

```text
packet_kind: reflux
source_surface: vectorfl_surface
target_surface: space
purpose: preserve emerging axis pattern
directionality: reflux
anchor_refs: [integrated_engine_3_surface_baseline]
related_objects: [axis_candidate_alpha, comparison_note_03]
current_judgment_state: candidate_enriched
requested_or_next_action: preserve_for_reread
validation_points: [reread value, axis emergence potential]
reflux_need: yes
packet_status: refluxed

reflux_target_zone: axis_candidate_zone
reflux_reason: future reread and maturation
maturation_value: external enrichment made the axis pattern more explicit
linked_lines_or_axes: [line_bundle_02, line_bundle_05]
preserve_trace_items: [origin, comparison_reason, search_route]
```

Reading:

- The packet is not closing the object as final.
- It preserves the trace and maturation value for future reread.

## 11. VectorFL surface implication

Packet language clarifies why the VectorFL surface matters.

VectorFL surface is not only a relay point. It is the packet mediation organ that:

- reads user purpose before engine execution
- attaches directionality
- checks anchor references
- adds validation points
- decides whether execution, tool support, return, or reflux is appropriate
- reads returned material
- decides whether the result should become space maturation material

Stable working sentence:

> The VectorFL surface is the packet mediation organ that reads purpose and direction, attaches anchor and validation context, routes only after intermediate formation reading, validates returns, and sends reflux-worthy material back to the space.

Boundary:

- This does not lock VectorFL as a full workflow hub.
- Team routing, automatic assignment, and standing workers remain operating extension / future-layer language.

## 12. lock level

### usable now

- Use `request / return / reflux` as the three packet kinds for v0.
- Use common slots + type-specific minimum slots.
- Treat packets as shared carriers, not chat-only messages.
- Treat VectorFL as packet mediation surface between user purpose and engine execution.

### not locked

- Full enum values
- DB schema
- Final status machine
- Automatic routing rules
- Team-specific packet variants
- Persistent executor assignment

## 13. core sentence

Transfer packets are not simple request text. They are common carriers that move purpose, directionality, anchor criteria, judgment state, next action, validation points, and reflux need between the user surface, VectorFL surface, and engine surface.

v0 should only test whether `request / return / reflux` plus common slots and type-specific minimum slots are enough to support repeated low-intensity operation.

