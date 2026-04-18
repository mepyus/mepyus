# Integrated Engine Working Protocol v1 Candidate

Date: 2026-04-15

## 0. purpose

This document gathers the current PASS-level operating protocol for integrated-engine v0.

It is a v1 candidate, not a final state machine.

Do not read this as:

- final workflow engine
- full routing automation
- DB schema
- complete event system
- permission model

Read it as:

- the minimum operating protocol that currently keeps request, return, reflux, loop state, and panel connection legible

## 1. operating object slot loop

Default movement loop:

```text
inbox
-> vectorfl_review
-> engine_processing / external_support
-> validation
-> return_ready
-> closed
```

Core rules:

- `inbox` does not go directly to `engine_processing`.
- Engine result does not go directly to `closed`.
- `external_support` returns to `validation`.
- `closed` means current-loop closure, not permanent deletion.

Working sentence:

- Operating objects move through explicit slots so processing state and next action do not dissolve into conversation.

## 2. transfer packet minimum

Common packet slots:

- `packet_kind`
- `source_surface`
- `target_surface`
- `purpose`
- `directionality`
- `anchor_refs`
- `requested_or_next_action`
- `packet_status`

Type-specific minimum:

- request: `input_materials`, `expected_output_shape`
- return: `return_summary`, `suggested_next_route`
- reflux: `reflux_target_zone`, `maturation_value`

Working sentence:

- Transfer packets carry purpose, direction, anchor, judgment, next action, validation, and reflux context between surfaces.

## 3. request / return / reflux role separation

### request

Direction:

- `user_surface -> vectorfl_surface`

Role:

- Start review and mediation.

### return

Direction:

- `engine_surface -> vectorfl_surface`

Role:

- Bring processing output back for validation.

### reflux

Direction:

- `vectorfl_surface -> space`

Role:

- Preserve maturation-worthy material for reread and line/axis growth.

## 4. panel connection flow unit

Each representative panel connection is recorded with:

- `trigger_panel`
- `trigger_action`
- `source_object_or_packet`
- `emitted_packet_or_state_change`
- `target_surface`
- `target_panel`
- `expected_effect`
- `record_written`

Current essential flows:

1. user request -> VectorFL review
2. VectorFL review -> engine processing / external support
3. engine result -> VectorFL validation
4. VectorFL judgment -> user decision / space reflux

Current low-intensity bundle note:

- `VectorFL review -> engine processing / external support` is not yet represented as a separate panel connection record in the current low-intensity bundle.
- For this bundle, that transition is confirmed after the fact by reading the request packet route intent (`requested_or_next_action`, `external_support_need`) together with the later return packet.

Working sentence:

- Panel connections make the three-surface circulation explicit in packet and log units.

## 5. current loop state minimum

`current_loop_state` should show at least:

- `active_request_packet`
- `active_return_packet`
- `active_reflux_packet`
- `current_slot`
- `current_surface`
- `current_focus_object`
- `loop_status`

Working sentence:

- Current loop state should let the operator understand where the loop is without reading every packet.
- It is a minimum current-position state, not a full movement history; read panel connection records together with it when reconstructing the whole loop progression.

## 6. anti-bypass principle

User request must not go directly to engine processing.

Required path:

```text
user request -> VectorFL review -> engine processing / external support
```

Reason:

- VectorFL review attaches directionality, anchors, related objects, validation points, and route judgment before execution.

Current follow-up note:

- A follow-up that starts after a recorded VectorFL maturation-canvas signal is not raw user-intent bypass.
- Read it as user organization turning that maturation signal into an engine follow-up request.

## 7. return validation principle

Engine output is not final completion.

Required path:

```text
engine result -> VectorFL validation -> user decision / reflux / reprocess
```

Reason:

- Return is processing output, not validated meaning or product completion.

Current reprocess note:

- When anchor drift is detected, return validation may rewind to a reprocess route instead of moving to user decision.

## 8. reflux principle

Maturation-worthy output creates a reflux path even when operating work can close.

Required separation:

- return packet = processing output for validation
- reflux packet = route/reason for preserving maturation value
- maturation object = body that grows after reflux

## 9. held out of this candidate

Not included in this v1 candidate:

- full status enum
- automatic routing
- standing team assignment
- permission / lock policy
- runtime watchers
- actual engine execution
- complete panel event inventory
