# Integrated Engine Panel Render Contract v0

Date: 2026-04-15

## 0. purpose

This document is a working draft, not a runtime binding specification.

Panel-to-manifest read mapping says which manifest a panel should read.

Panel render contract says which fields a panel should minimally display from that manifest.

Do not read this document as:

- final component props
- view model layer
- runtime data mapping function
- computed field design
- UI style or layout detail

Read it as:

- v0 minimum display contract
- a guard against panels rendering whole manifests without regard to their own question

Key sentence:

> A panel render contract prevents a panel from swallowing the whole manifest by limiting it to the fields needed to answer its own question.

## 1. common principles

### principle 1 - panels do not render whole manifests

A panel should render only the minimum fields needed for its question.

### principle 2 - the same manifest can be read differently

Example:

- User surface may read `return_summary` and `suggested_next_route`.
- VectorFL surface may read `result_confidence`, `open_questions`, and `validation_points`.
- Engine surface may read `produced_artifacts` and `result_confidence`.

### principle 3 - render contract has three core layers

Each contract should show:

- `primary_manifest`
- `render_fields`
- `display_purpose`

### principle 4 - avoid derived fields in v0

v0 should mostly display existing manifest fields.

Do not add broad computed state, selection sync, or derived view model logic yet.

## 2. render contract unit

Minimum fields:

- `panel_id`
- `primary_manifest`
- `render_fields`
- `display_purpose`

Optional support fields:

- `supporting_manifest`
- `secondary_fields`
- `empty_state_message`

Compressed shape:

```text
panel_id
primary_manifest
supporting_manifest
render_fields
display_purpose
empty_state_message
```

## 3. user surface render contracts v0

User surface is operating-centered.

It should show what was requested, where the loop is, and what decision is needed.

### 3.1 request / organization panel

```text
panel_id: request_organization_panel
primary_manifest: runtime/manifests/packet_request_axis_enrichment_001.json
supporting_manifest: runtime/manifests/active_anchor_integrated_engine_3_surface.json
render_fields:
  - purpose
  - directionality
  - requested_or_next_action
  - external_support_need
  - related_objects
secondary_fields:
  - anchor_refs
display_purpose: Show what the request is trying to do, what direction it has, whether external support is needed, and what objects it touches.
empty_state_message: No active request packet selected.
```

Why:

- User surface does not need the whole request JSON.
- It needs enough to make organization and distribution decisions.

### 3.2 operating flow panel

```text
panel_id: operating_flow_panel
primary_manifest: runtime/manifests/current_loop_state_axis_enrichment_001.json
supporting_manifest:
  - runtime/manifests/packet_request_axis_enrichment_001.json
  - runtime/manifests/packet_return_axis_enrichment_001.json
render_fields:
  - current_slot
  - current_surface
  - loop_status
  - active_request_packet
  - active_return_packet
display_purpose: Show where the current loop is, which surface owns it now, and whether return has arrived.
empty_state_message: No active loop state.
```

Why:

- This is the user surface central panel.
- The first question is where the flow is now.

### 3.3 anchor support panel

```text
panel_id: anchor_support_panel
primary_manifest: runtime/manifests/active_anchor_integrated_engine_3_surface.json
supporting_manifest: runtime/manifests/packet_request_axis_enrichment_001.json
render_fields:
  - anchor_name
  - anchor_scope
  - locked_boundary
  - comparison_rule
secondary_fields:
  - anchor_refs
display_purpose: Show which baseline the current request is standing on and which boundary must not be crossed.
empty_state_message: No active anchor.
```

### 3.4 return / decision panel

```text
panel_id: return_decision_panel
primary_manifest: runtime/manifests/packet_return_axis_enrichment_001.json
supporting_manifest:
  - runtime/manifests/current_loop_state_axis_enrichment_001.json
  - runtime/manifests/packet_reflux_axis_pattern_001.json
render_fields:
  - return_summary
  - result_confidence
  - open_questions
  - suggested_next_route
secondary_fields:
  - produced_artifacts
  - reflux_need
display_purpose: Show what came back, what remains open, and what next decision is suggested.
empty_state_message: No return packet ready for decision.
```

## 4. VectorFL surface render contracts v0

VectorFL surface centers mediation, validation, and maturation.

It needs the most interpretive render contracts.

### 4.1 anchor / context panel

```text
panel_id: anchor_context_panel
primary_manifest: runtime/manifests/active_anchor_integrated_engine_3_surface.json
supporting_manifest:
  - runtime/manifests/packet_request_axis_enrichment_001.json
  - runtime/manifests/packet_return_axis_enrichment_001.json
render_fields:
  - anchor_name
  - anchor_scope
  - governs_what
  - locked_boundary
  - comparison_rule
secondary_fields:
  - anchor_refs
display_purpose: Show which criteria the current request or return should be read against and where drift may appear.
empty_state_message: No active anchor context.
```

### 4.2 maturation canvas panel

```text
panel_id: maturation_canvas_panel
primary_manifest: runtime/manifests/maturation_object_axis_candidate_001.json
supporting_manifest:
  - runtime/manifests/packet_reflux_axis_pattern_001.json
  - runtime/manifests/packet_return_axis_enrichment_001.json
render_fields:
  - object_name
  - object_kind
  - current_position
  - maturity_stage
  - linked_objects
  - evidence_density
  - open_edges
display_purpose: Show what is growing as an axis candidate, where it sits, how mature it is, what it links to, and what remains open.
empty_state_message: No maturation object selected.
```

Note:

- The reflux packet is the maturation entry/evidence route.
- The maturation object is the maturation body.
- The maturation canvas now reads the maturation object as primary.

### 4.3 validation / mediation panel

```text
panel_id: validation_mediation_panel
primary_manifest:
  - runtime/manifests/packet_request_axis_enrichment_001.json
  - runtime/manifests/packet_return_axis_enrichment_001.json
supporting_manifest:
  - runtime/manifests/current_loop_state_axis_enrichment_001.json
  - runtime/manifests/active_anchor_integrated_engine_3_surface.json
render_fields:
  - current_judgment_state
  - validation_points
  - requested_or_next_action
  - result_confidence
  - open_questions
  - suggested_next_route
display_purpose: Show what must be validated, what the current judgment state is, and where the packet should move next.
empty_state_message: No request or return packet under VectorFL validation.
```

Why:

- This is the VectorFL judgment organ in the v0 scaffold.

### 4.4 routing / reflux panel

```text
panel_id: routing_reflux_panel
primary_manifest:
  - runtime/manifests/packet_return_axis_enrichment_001.json
  - runtime/manifests/packet_reflux_axis_pattern_001.json
supporting_manifest: runtime/manifests/panel_connection_record_axis_enrichment_001.json
render_fields:
  - suggested_next_route
  - reflux_need
  - reflux_target_zone
  - maturation_value
secondary_fields:
  - emitted_packet_or_state_change
display_purpose: Show whether the result should go to user decision, engine reprocessing, external support, or space reflux.
empty_state_message: No routing or reflux decision available.
```

### 4.5 evidence / history panel

```text
panel_id: evidence_history_panel
primary_manifest: runtime/manifests/panel_connection_record_axis_enrichment_001.json
supporting_manifest:
  - runtime/manifests/packet_request_axis_enrichment_001.json
  - runtime/manifests/packet_return_axis_enrichment_001.json
  - runtime/manifests/packet_reflux_axis_pattern_001.json
render_fields:
  - trigger_panel
  - trigger_action
  - source_object_or_packet
  - target_surface
  - target_panel
  - record_written
display_purpose: Show where the current flow started, what woke what, and what record remains.
empty_state_message: No connection record available.
```

## 5. engine surface render contracts v0

Engine surface is execution-centered.

It should show input, current loop position, result draft, and minimal route trace.

### 5.1 work input panel

```text
panel_id: work_input_panel
primary_manifest: runtime/manifests/packet_request_axis_enrichment_001.json
supporting_manifest:
  - runtime/manifests/active_anchor_integrated_engine_3_surface.json
  - runtime/manifests/current_loop_state_axis_enrichment_001.json
render_fields:
  - request_type
  - input_materials
  - expected_output_shape
  - validation_points
secondary_fields:
  - anchor_refs
display_purpose: Show what input the engine should process and what output shape is expected.
empty_state_message: No VectorFL-shaped request packet available.
```

### 5.2 execution state panel

```text
panel_id: execution_state_panel
primary_manifest: runtime/manifests/current_loop_state_axis_enrichment_001.json
supporting_manifest: runtime/manifests/packet_request_axis_enrichment_001.json
render_fields:
  - current_slot
  - current_surface
  - loop_status
  - active_request_packet
display_purpose: Show where the loop sits from the engine perspective and what request packet is active.
empty_state_message: No current loop state.
```

### 5.3 result / return panel

```text
panel_id: result_return_panel
primary_manifest: runtime/manifests/packet_return_axis_enrichment_001.json
supporting_manifest: runtime/manifests/packet_request_axis_enrichment_001.json
render_fields:
  - return_summary
  - produced_artifacts
  - result_confidence
  - open_questions
  - suggested_next_route
display_purpose: Show how engine output has been packaged as a return packet.
empty_state_message: No return packet generated.
```

### 5.4 execution history panel

```text
panel_id: execution_history_panel
primary_manifest: runtime/manifests/panel_connection_record_engine_return_to_vectorfl_validation_001.json
supporting_manifest: runtime/manifests/current_loop_state_axis_enrichment_001.json
render_fields:
  - source_object_or_packet
  - emitted_packet_or_state_change
  - target_panel
  - record_written
display_purpose: Show the minimum route trace visible from the engine surface.
empty_state_message: No execution history record available.
```

Note:

- Later this panel may read `logs/runlogs/` as primary.
- In v0, `panel_connection_record_engine_return_to_vectorfl_validation_001.json` is only a temporary history source.

## 6. lock level

### usable now

- Render contract prevents panels from rendering whole manifests.
- User surface reads only fields needed for operating judgment.
- VectorFL surface reads fields needed for validation, maturation, and reflux judgment.
- Engine surface reads fields needed for input, execution state, and return draft.
- The same manifest can have different `render_fields` by surface and panel.

### not locked

- Full props types
- View model layer
- Derived / computed fields
- Selection sync rules
- Runtime data mapping functions
- UI style or layout details

## 7. core sentence

Panel render contract exists so each panel displays only the minimum fields needed to answer its own question instead of exposing a whole manifest.

v0 only needs to fix:

```text
panel_id + primary_manifest + render_fields + display_purpose
```

to separate manifest shape from display shape before runtime binding.
