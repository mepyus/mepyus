# Integrated Engine Current Surface Material Index v0

## 1. Verdict

PASS_WITH_NOTE

This index collects current materials for the next design round. It is an inventory only. It does not redesign, refactor, rename, or propose a new package schema.

## 2. Current UI Source Materials

| path | role | why it matters now | type |
| --- | --- | --- | --- |
| `app/ui/integrated_engine/VectorFLIntegrationShell.tsx` | current integrated-engine shell | Contains User / VectorFL / Engine tabs, slot wrappers, one-handler package constant, current surface projections, and translation-chain display points. | UI source |
| `app/ui/integrated_engine/CliHostControlPanel.tsx` | VectorFL session layer | Contains compact session strip, send/revise/hold/refresh controls, evidence gate, packet formation support, recent turns, latest return details, marks. | UI source |
| `app/ui/integrated_engine/vectorfl_engine_surface_mock.tsx` | Engine inspector/support mock | Contains legacy engine support material, primary processing pipeline mock, asset/watch/trace support grammar. | UI source / support |
| `app/ui/integrated_engine/CommandHeaderPanel.tsx` | User material-context support | Supports User surface context and current goal display. | UI source |
| `app/ui/integrated_engine/ExecutionRoutePanel.tsx` | User route/log inspector | Supports route and assignment history reading. | UI source |
| `app/ui/integrated_engine/OperationLogPanel.tsx` | User log inspector | Supports audit/log reading. | UI source |
| `app/ui/integrated_engine/AssetInspectorPanel.tsx` | support grammar source | Contains warning, link, trace, status-card patterns useful as support grammar. | UI source / grammar source |
| `app/ui/integrated_engine/EventConsolePanel.tsx` | trace/event grammar source | Contains compact event/trace summary cards. | UI source / grammar source |

## 3. Current Slot / Surface Design Docs

| path | role | why it matters now | type |
| --- | --- | --- | --- |
| `docs/specs/integrated_engine_surface_slot_architecture_v0.md` | slot contract | Defines center / support / inspector semantics and first question per surface. | design spec |
| `docs/reports/integrated_engine_surface_slot_mapping_v0.md` | current component mapping | Maps current components into User / VectorFL / Engine slots. | mapping report |
| `docs/reports/integrated_engine_support_grammar_extraction_note_v0.md` | support grammar extraction | Separates reusable support grammar from literal old panel carryover. | report |
| `docs/reports/integrated_engine_surface_slot_validation_note_v0.md` | slot validation | Records what improved and what still feels dense after slot restructuring. | validation doc |
| `docs/reports/integrated_engine_surface_slot_closeout_note_v0.md` | slot closeout | Locks current status and next-safe-action recommendation. | closeout doc |
| `docs/specs/integrated_engine_vectorfl_session_layer_policy_v0.md` | session layer policy | Locks CliHost as session layer, not VectorFL center. | design spec |
| `docs/reports/integrated_engine_vectorfl_session_recenter_closeout_note_v0.md` | VectorFL recenter closeout | Confirms VectorFL now centers selected interpreted package/object. | closeout doc |

## 4. Current Handler Package Artifacts

| path | role | why it matters now | type |
| --- | --- | --- | --- |
| `runtime/contracts/integrated_engine_single_handler_package_instance_v0.json` | live one-handler package artifact | Contains `language_handler_loop_pkg_v0`, surface projections, lifecycle, evidence summary, validation status, authority boundary. | runtime artifact |
| `runtime/contracts/integrated_engine_single_handler_return_record_instance_v0.json` | one-handler return record | Contains attempted flow, surface results, risks, output summary, redeposit boundary, next valid use. | runtime artifact |
| `docs/reports/integrated_engine_single_handler_package_flow_spec_v0.md` | one-handler flow spec | Defines expected flow across User / VectorFL / Engine. | design report |
| `docs/reports/integrated_engine_one_handler_slot_run_note_v0.md` | one-handler slot validation | Confirms same package still flows through slot restructuring. | validation doc |

## 5. Translation / Bridge Context Materials

| path | role | why it matters now | type |
| --- | --- | --- | --- |
| `docs/reports/integrated_engine_lower_to_upper_bridge_maturation_closeout_note_v0.md` | bridge maturity lock | Confirms bridge is usable but dependency-heavy and not automatic. | closeout doc |
| `docs/reports/integrated_engine_lower_to_upper_bridge_stable_vs_dependency_heavy_fields_note_v0.md` | field-origin distinction | Separates stable lower-derived evidence fields from upper-added purpose/action/authority/route fields. | analysis report |

## 6. Validation

- Inventory completeness: enough for the next design round.
- Current relevance: focused on current shell, current slot docs, current package artifacts, and bridge field-origin context.
- Stale side-branch avoidance: no Gemini/external-analysis or older unrelated mock documents were included as core materials.

