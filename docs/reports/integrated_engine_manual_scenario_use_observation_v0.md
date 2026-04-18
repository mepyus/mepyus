# Integrated Engine Manual Scenario Use Observation v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

The current integrated-engine baseline can be used manually across the three low-intensity scenarios without scaffold, manifest, read-map, token, runtime, or extension changes.

The main limitation is not structure. It is use-time thinness: follow-up and drift scenarios require manual rereading through the same panel-role grammar because the scaffold read maps remain centered on the first sample fixture.

## 1. observation boundary

This observation used:

- current scaffold panel placement and read maps
- v1 candidate lexicon / protocol / interface language
- Round 3 visual closeout
- Round 4 render-contract closeout
- Round 5 render-field inventory closeout
- Round 6 empty-state / trace boundary closeout
- current sample manifests for normal, follow-up, and drift-reprocess loops

It did not:

- change scaffold files
- change manifests
- change `PANEL_MANIFEST_READ_MAP`
- add wording patches
- add selected-object behavior
- add trace UI
- promote any extension

## 2. scenario 1: user-origin normal loop

Scenario:

- user request
- VectorFL review / mediation
- engine processing
- return
- VectorFL validation
- reflux / user decision path remains open

| observation axis | reading |
|---|---|
| entry surface | `user_surface`, through `request_organization_panel` |
| main central panel | `operating_flow_panel` on user surface; `maturation_canvas_panel` for VectorFL validation/reread; `execution_state_panel` for engine processing position |
| route readability | Strong enough. `packet_request_axis_enrichment_001` reads as user -> VectorFL request; `packet_return_axis_enrichment_001` reads as engine -> VectorFL return; `packet_reflux_axis_pattern_001` reads as VectorFL -> space reflux. |
| support layer behavior | User anchor and return panels stay secondary. VectorFL validation/reflux/evidence panels support the maturation canvas. Engine result/history panels support execution state. |
| wording confusion point | The VectorFL review -> engine processing transition still depends on request route intent plus later return packet, not a separate connection record. This is already noted in protocol. |
| what felt stable | Request / return / reflux separation, central panel differences, and active loop state are readable. |
| what felt thin | Full movement history is not reconstructable from `current_loop_state` alone; connection records must be read with it. |

Request / return / reflux reading:

- request is shaped input for VectorFL review, not raw engine command
- return is engine-side material for validation, not completion
- reflux preserves maturation value and trace for reread

Support panel risk:

- low. No support panel becomes the body of the scenario.

Empty state / trace sufficiency:

- sufficient for current manual use because the sample manifests are present and route records can be read directly.
- not sufficient for actual value rendering or missing-data UI.

## 3. scenario 2: VectorFL-origin follow-up / reactivation loop

Scenario:

- VectorFL maturation canvas sees an internal follow-up need
- user surface request organization is awakened
- user organization creates a shaped follow-up request
- engine creates a follow-up return
- user decision or VectorFL recheck remains open

| observation axis | reading |
|---|---|
| entry surface | `vectorfl_surface`, through `maturation_canvas_panel` and `panel_connection_record_vectorfl_maturation_to_user_followup_001` |
| main central panel | `maturation_canvas_panel` remains the cause-reading center; `operating_flow_panel` organizes the follow-up request once user surface is awakened; `execution_state_panel` holds engine processing position. |
| route readability | Good with manual reread. The maturation object is the cause; the connection record wakes user request organization; `packet_request_axis_followup_001` targets engine; `packet_return_axis_followup_001` returns to user with VectorFL recheck still open. |
| support layer behavior | Line/axis support stays smaller than the maturation canvas. User request organization does not become team/role management. Engine return remains return material, not judgment. |
| wording confusion point | User scaffold copy says "incoming request", which can sound user-origin only. The protocol/lexicon already allow VectorFL maturation signal -> user organization -> engine follow-up, so this is wording-only thinness. |
| what felt stable | Maturation object can function as the cause of a new request without making VectorFL an engine executor. |
| what felt thin | Scaffold read maps are still first-fixture centered; follow-up sample is checked manually through panel-role grammar rather than direct scaffold mapping. |

Request / return / reflux reading:

- follow-up request is not raw user bypass because it is reorganized by user surface after a VectorFL maturation signal
- follow-up return is not closure because `suggested_next_route` remains `user_decision_or_vectorfl_recheck`
- reflux remains background maturation context, not the same thing as the follow-up request

Support panel risk:

- low to medium. Support selection and side inspection stay subordinate, but wording around "selected support" should not be read as selected-object behavior.

Empty state / trace sufficiency:

- sufficient for manual use because the explicit maturation-to-user connection record exists.
- trace UI is not needed; a denser trace would be extension work.

## 4. scenario 3: anchor drift -> reprocess / reflux loop

Scenario:

- engine return exists
- VectorFL detects anchor drift
- return does not move directly to user decision
- VectorFL creates or routes an engine reprocess request
- loop stays open in reprocess / rewind state

| observation axis | reading |
|---|---|
| entry surface | `vectorfl_surface`, through `anchor_context_panel` / validation mediation and `panel_connection_record_vectorfl_anchor_drift_to_recheck_001` |
| main central panel | `maturation_canvas_panel` keeps the axis candidate body visible while anchor criteria and validation route explain the drift; engine `execution_state_panel` becomes active after reprocess request. |
| route readability | Strong enough. Drift connection record names anchor mismatch, target engine work input, and recheck route. `packet_request_axis_reprocess_001` states vectorfl_surface -> engine_surface. `current_loop_state_axis_drift_recheck_001` shows `current_slot: reprocess` and records rewind reason. |
| support layer behavior | Anchor context starts the brake, but it remains criteria/support rather than the center body. Engine work input receives the reprocess request without becoming a judgment authority. |
| wording confusion point | Because `anchor_context_panel` is visually support, a reader may need the connection record to see that anchor criteria can stop route progression. This is use-time thinness, not a need to promote anchor panel to center. |
| what felt stable | Anchor drift functions as a real stop/reprocess reason. The loop does not falsely close. |
| what felt thin | Drift connection record is not part of the current VectorFL evidence history read map; it must be manually read as a scenario-specific support record. |

Request / return / reflux reading:

- reprocess request is created by VectorFL validation / anchor check, which the lexicon permits as vectorfl_surface -> engine_surface
- return remains under validation and does not become user-facing completion
- reflux remains available as maturation preservation, not as closure

Support panel risk:

- low. Anchor support is active enough to explain drift but not visually or semantically promoted to central body.

Empty state / trace sufficiency:

- sufficient for manual use because `held_from_closure_reason`, `previous_slot`, and `rewind_reason` make the reprocess state legible.
- denser trace UI is not required to understand the loop.

## 5. cross-scenario observation

Stable across all three:

- central panel gravity remains clear:
  - user: `operating_flow_panel`
  - VectorFL: `maturation_canvas_panel`
  - engine: `execution_state_panel`
- request / return / reflux are separated enough for manual use
- support layers remain subordinate
- no runtime binding or governance authority is needed
- current loop state is enough to locate the loop when read with the relevant packets and connection records

Thin across all three:

- first-fixture scaffold mapping means follow-up and drift samples rely on manual panel-role grammar
- evidence/history trace remains compact and sample-centered
- empty-state messages are not needed for current manual use, but would be needed before actual data rendering
- side inspection wording can hint at future selected-object behavior, but current scaffolds do not implement it

## 6. use sentence

The current baseline is usable for manual scenario reading now. The next safest action is to use it, not build more structure, unless repeated wording confusion appears during further manual runs.
