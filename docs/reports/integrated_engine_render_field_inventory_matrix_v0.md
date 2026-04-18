# Integrated Engine Render Field Inventory Matrix v0

Date: 2026-04-15

## 0. scope

This inventory fixes the minimum render-field language currently implied by the three PASS scaffold files and the v1 candidate interface document.

It is documentation-only.

It does not change scaffold files, manifest shape, panel read mapping, token systems, selected-object behavior, or runtime binding.

Rule:

- `render_fields` lists only field names or field groups directly visible in the current scaffold copy, read-map reasons, or v1 candidate render-contract language.
- Visual rhythm, badge styling, card density, and layout tokens are not treated as render fields.
- Future inspection, selected-object, and trace-density ideas stay in `future_note`.

## 1. inventory matrix

| surface | panel_id | central_or_support | primary_manifest | render_fields | display_purpose | supporting_manifest | secondary_fields | empty_state_message | contract_strength | future_note |
|---|---|---|---|---|---|---|---|---|---|---|
| user | `request_organization_panel` | support | `runtime/manifests/packet_request_axis_enrichment_001.json` | request frame, goal, scope, material context, next surface | Shape the incoming request before review or follow-up routing. | none in current read map | read role, manifest path, read reason | Not defined in scaffold. | implicit | core now; distribution hints remain extension later |
| user | `operating_flow_panel` | central | `runtime/manifests/current_loop_state_axis_enrichment_001.json` | current slot, active packet, route state, open decision | Keep request / return / reflux loop position visible for operating, distribution, and decision. | none in current read map | visual route rhythm: request, vectorfl_review, return, decision_or_reflux | Not defined in scaffold. | implicit | core now; selected route detail remains extension later |
| user | `anchor_support_panel` | support | `runtime/manifests/active_anchor_integrated_engine_3_surface.json` | anchor, boundary, drift watch | Check whether user-side request and decision handling respect the three-surface anchor. | none in current read map | read role, manifest path, read reason | Not defined in scaffold. | implicit | core now |
| user | `return_decision_panel` | support | `runtime/manifests/packet_return_axis_enrichment_001.json` | return material, question, recheck, reflux | Read return material as decision input while keeping recheck, reprocess, and reflux routes open. | none in current read map | read role, manifest path, read reason | Not defined in scaffold. | implicit | core now; deeper return decision inspection remains extension later |
| VectorFL | `anchor_context_panel` | support | `runtime/manifests/active_anchor_integrated_engine_3_surface.json` | anchor ref, boundary, drift risk | Keep anchor criteria and comparison boundaries separate before mediation. | none in current read map | read role, manifest path, read reason | Not defined in scaffold. | implicit | core now |
| VectorFL | `maturation_canvas_panel` | central | `runtime/manifests/maturation_object_axis_candidate_001.json` | origin refs, current position, maturity stage, linked objects, open edges, evidence density | Read the axis candidate as the primary maturation object body. | `runtime/manifests/packet_reflux_axis_pattern_001.json`; `runtime/manifests/packet_return_axis_enrichment_001.json` | reflux route contribution, engine return contribution, read role, manifest path, read reason | Not defined in scaffold. | explicit | core now; selected-object value rendering remains extension later |
| VectorFL | `validation_mediation_panel` | support | `runtime/manifests/packet_request_axis_enrichment_001.json`; `runtime/manifests/packet_return_axis_enrichment_001.json` | request, return, hold, recheck | Compare operating packets before user decision, recheck, reprocess, or reflux routing. | none beyond primary dual-read | request purpose/directionality/validation points, returned result check | Not defined in scaffold. | implicit | core now |
| VectorFL | `routing_reflux_panel` | support | `runtime/manifests/packet_return_axis_enrichment_001.json`; `runtime/manifests/packet_reflux_axis_pattern_001.json` | reflux, target zone, preserve trace | Preserve return-to-reflux route and maturation value without treating reflux as completion. | none beyond primary dual-read | return status, reflux target, maturation value | Not defined in scaffold. | implicit | core now |
| VectorFL | `evidence_history_panel` | support | `runtime/manifests/panel_connection_record_axis_enrichment_001.json` | source, emitted state, target panel | Show compact circulation evidence through the current primary connection record. | broader connection records are supporting context in scenario checks, not current read-map fields | connection record trace, lineage-style row | Not defined in scaffold. | implicit | core now; broader trace density needs promotion gate |
| engine | `work_input_panel` | support | `runtime/manifests/packet_request_axis_enrichment_001.json` | shaped input, panel question, request ready for engine processing | Read the VectorFL-shaped request packet as engine work input. | none in current read map | read role, manifest path, read reason | Not defined in scaffold. | explicit | core now |
| engine | `execution_state_panel` | central | `runtime/manifests/current_loop_state_axis_enrichment_001.json` | central slot, current loop slot, processing state, loop position | Show where engine processing is now without interpreting return meaning. | none in current read map | visual slot rhythm: input, processing, return, trace | Not defined in scaffold. | implicit | core now; worker/process detail remains extension later |
| engine | `result_return_panel` | support | `runtime/manifests/packet_return_axis_enrichment_001.json` | return draft, return material, validation route, follow-up route | Draft return material for VectorFL validation or follow-up routing. | none in current read map | read role, manifest path, read reason | Not defined in scaffold. | implicit | core now; return-material inspection remains extension later |
| engine | `execution_history_panel` | support | `runtime/manifests/panel_connection_record_engine_return_to_vectorfl_validation_001.json` | route trace, panel connection, execution history | Show the minimal route trace that explains the engine return. | none in current read map | read role, manifest path, read reason | Not defined in scaffold. | implicit | core now; denser trace rendering needs promotion gate |

## 2. inventory notes

Explicit contract currently means the scaffold directly names the render field group or panel question in a way that can be inventoried without opening the manifest.

Implicit contract currently means the scaffold names the purpose and visual field labels, but actual manifest value extraction is not specified.

`visual-only-support` is not assigned to current core panel rows because the listed rows are panel contracts. Visual strips, route rhythm, card density, badges, and side-support shells remain support notes, not panel render fields.

## 3. verdict

PASS_WITH_NOTE

The inventory is usable as a current baseline render-field reference, but most fields are still scaffold-level labels rather than actual data-binding fields.
