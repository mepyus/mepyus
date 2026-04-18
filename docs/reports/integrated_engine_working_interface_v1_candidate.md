# Integrated Engine Working Interface v1 Candidate

Date: 2026-04-15

## 0. purpose

This document gathers the current PASS-level interface language for integrated-engine v0.

It is a v1 candidate, not a final UI design.

Do not read this as:

- visual design system
- final component architecture
- runtime binding
- file watcher
- automatic dashboard generator

Read it as:

- the minimum interface contract that keeps panels, manifests, and render fields aligned

## 1. panel classification

Panels are classified by what they express:

- anchor expression
- maturation expression
- operating expression

Rule:

- Panels should answer operating questions, not expose whole manifests or generic feature lists.

## 2. representative panel placement

### user surface

Center:

- `operating_flow_panel`

Representative panels:

- `request_organization_panel`
- `operating_flow_panel`
- `anchor_support_panel`
- `return_decision_panel`

### VectorFL surface

Center:

- `maturation_canvas_panel`

Representative panels:

- `anchor_context_panel`
- `maturation_canvas_panel`
- `validation_mediation_panel`
- `routing_reflux_panel`
- `evidence_history_panel`

### engine surface

Center:

- `execution_state_panel`

Representative panels:

- `work_input_panel`
- `execution_state_panel`
- `result_return_panel`
- `execution_history_panel`

## 3. panel-to-manifest read mapping

### user surface

- `request_organization_panel` -> `packet_request_axis_enrichment_001.json`
- `operating_flow_panel` -> `current_loop_state_axis_enrichment_001.json`
- `anchor_support_panel` -> `active_anchor_integrated_engine_3_surface.json`
- `return_decision_panel` -> `packet_return_axis_enrichment_001.json`

### VectorFL surface

- `anchor_context_panel` -> `active_anchor_integrated_engine_3_surface.json`
- `maturation_canvas_panel` -> `maturation_object_axis_candidate_001.json`
- `validation_mediation_panel` -> `packet_request_axis_enrichment_001.json` + `packet_return_axis_enrichment_001.json`
- `routing_reflux_panel` -> `packet_return_axis_enrichment_001.json` + `packet_reflux_axis_pattern_001.json`
- `evidence_history_panel` -> `panel_connection_record_axis_enrichment_001.json`

Current low-intensity bundle note:

- `evidence_history_panel` keeps `panel_connection_record_axis_enrichment_001.json` as the first primary record for request creation.
- Engine return and reflux connection records are read as supporting trace records when checking the broader flow, without changing the read mapping above.

### engine surface

- `work_input_panel` -> `packet_request_axis_enrichment_001.json`
- `execution_state_panel` -> `current_loop_state_axis_enrichment_001.json`
- `result_return_panel` -> `packet_return_axis_enrichment_001.json`
- `execution_history_panel` -> `panel_connection_record_engine_return_to_vectorfl_validation_001.json`

Fixture scope note:

- The direct mapping examples above are centered on the first sample fixture.
- Follow-up and drift-reprocess samples are checked manually through the same panel-role grammar, without changing scaffold read mappings.

## 4. render contract principle

Each panel renders only fields needed for its question.

Minimum render contract unit:

- `panel_id`
- `primary_manifest`
- `render_fields`
- `display_purpose`

Optional support:

- `supporting_manifest`
- `secondary_fields`
- `empty_state_message`

Working sentence:

- Render contract separates manifest shape from display shape.

## 5. current PASS rule for VectorFL maturation canvas

Current primary manifest:

- `runtime/manifests/maturation_object_axis_candidate_001.json`

Supporting manifests:

- `runtime/manifests/packet_reflux_axis_pattern_001.json`
- `runtime/manifests/packet_return_axis_enrichment_001.json`

Role separation:

- reflux packet = maturation entry / evidence route
- maturation object = maturation body

Working sentence:

- VectorFL maturation canvas now reads the axis candidate body directly, not only the reflux event that created it.

## 6. current scaffold files

The current v0 scaffold files are:

- `runtime/views/user_surface_scaffold_v0.tsx`
- `runtime/views/vectorfl_surface_scaffold_v0.tsx`
- `runtime/views/engine_surface_scaffold_v0.tsx`

Role:

- These files are read-mapping scaffolds, not runtime data binding implementations.

## 7. held out of this candidate

Not included in this v1 candidate:

- final CSS/design system
- component props
- view model layer
- computed fields
- selection sync
- actual file reads
- live runtime binding
- automatic panel generation
