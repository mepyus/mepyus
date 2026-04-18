# Integrated Engine Current Language Handler Field Inventory v0

## 1. Verdict

PASS_WITH_NOTE

This inventory is grounded in:

- `runtime/contracts/integrated_engine_single_handler_package_instance_v0.json`
- `runtime/contracts/integrated_engine_single_handler_return_record_instance_v0.json`

It interprets current fields conservatively and does not propose a new schema.

## 2. Package Artifact Field Inventory

| field | current value / shape | meaning | current visibility | surface fit |
| --- | --- | --- | --- | --- |
| `package_id` | `language_handler_loop_pkg_v0` | package identity | visible in package panel / support detail | support / lightweight reference |
| `package_kind` | `single_handler_package` | confirms one-handler mode | mostly artifact-level | support-only |
| `handler.handler_id` | `language-owner` | internal handler id | visible in package panel small text | support-only |
| `handler.handler_label` | `언어담당` | human-readable handler label | visible in package panel | user-facing / vectorfl-facing |
| `handler.surface_home` | `user` | home surface for assignment | artifact-level | support-only |
| `handler.automation_status` | `not_automatic` | blocks automation overread | artifact-level, echoed in docs | inspector/support boundary |
| `purpose` | Korean operating purpose | why the package exists | User center / package panel | user-facing |
| `scope.included` | one-handler flow, projections, bounded status, declutter validation | what the package includes | support detail / artifact | support-only |
| `scope.excluded` | no multi-agent, no automation, no unification, etc. | authority boundary | support / docs | support / inspector |
| `current_target` | external_analysis lens fragments + lower-input / bridge wording residues | object/material under handling | package panel across surfaces | all surfaces, projected differently |
| `current_stage` | `VectorFL return review` | current lifecycle stage | Engine/VectorFL package projection | vectorfl-facing / engine-facing |
| `current_status` | `usable_with_hold` | current judgment state | package panel | all surfaces |
| `surface_projection.user.active` | purpose/scope/target/status/next action | User projection contract | artifact and implemented via package panel | user-facing |
| `surface_projection.vectorfl.active` | package/state/evidence/blocker/next route | VectorFL projection contract | artifact and implemented via package panel | vectorfl-facing |
| `surface_projection.engine.active` | ingest/process/validation/return/output | Engine projection contract | artifact and implemented via package panel | engine-facing |
| `surface_projection.*.support` | support field sets | support placement hints | partially visible | support-only |
| `surface_projection.*.hold` | hold/detail field sets | not-front boundary | mostly artifact/doc-level | inspector-only |
| `lifecycle` | five steps from User purpose to User next action | flow skeleton | lifecycle cards in package panel | all surfaces |
| `evidence_summary` | external_analysis lens fragments + dependency-heavy bridge finding | compact material basis | VectorFL package panel | vectorfl-facing |
| `validation_status` | bounded flow visible; no automatic bridge/final translation | validation and authority boundary | Engine package projection | engine-facing / support |
| `next_valid_action` | keep one-handler supervisory mode and demote internals | current next action | User package panel | user-facing |
| `authority_boundary` | booleans false for multi-agent, automation, glossary, canonical bridge | hard boundary | artifact-level, docs, support badges | support / inspector |

## 3. Return Record Field Inventory

| field | current value / shape | meaning | current visibility | surface fit |
| --- | --- | --- | --- | --- |
| `return_record_id` | `language_handler_loop_return_record_v0` | return identity | artifact-level | inspector-only |
| `source_package_id` | `language_handler_loop_pkg_v0` | links return to package | artifact-level | support / inspector |
| `handler_id` | `language-owner` | handler reference | artifact-level | support-only |
| `attempted_flow` | five-step flow | what the run attempted | summarized in run docs | support |
| `surface_results.user.result` | purpose-first projection visible | user result | not directly front as field | user-facing if translated |
| `surface_results.user.remaining_risk` | team/role support can become too loud | user risk | validation docs | support / inspector |
| `surface_results.vectorfl.result` | mediation/evidence front; line/bridge moved to support | VectorFL result | validation docs | vectorfl-facing if translated |
| `surface_results.vectorfl.remaining_risk` | CliHost dense packet controls | VectorFL risk | validation docs | support / gap material |
| `surface_results.engine.result` | processing/return before legacy mock | Engine result | validation docs | engine-facing if translated |
| `surface_results.engine.remaining_risk` | legacy mock remains large | Engine risk | validation docs | support / gap material |
| `validation_state` | `PASS_WITH_NOTE` | overall result | docs / artifact | support |
| `output_summary` | one package can display across surfaces with different density | return summary | closeout docs | user-facing after translation |
| `return_redeposit_summary` | candidate only; no automatic redeposit/canonical ingestion | authority boundary | Engine package projection / docs | engine-facing / vectorfl-facing |
| `what_was_not_done` | no orchestration, bridge, unification, polish, glossary | blocked actions | artifact-level | inspector/support boundary |
| `next_valid_use` | use as one-handler supervisory mode before second-handler | next use | closeout docs | user-facing if translated |
| `authority_boundary_confirmation` | bounded pilot only, no automation/team/canonical | confirmation | artifact-level | support/inspector |

## 4. What The Package Already Contains

- identity
- purpose
- scope include/exclude
- current target
- current stage
- current status
- surface projection hints
- lifecycle
- evidence summary
- validation status
- next valid action
- authority boundaries

## 5. What Feels Missing As A Translated Operating Object

Missing or thin:

- plain-language meaning summary for the current target
- clear “why this matters now” sentence for User
- explicit Engine-produced output field separate from UI output summary
- VectorFL reread/translation result field
- blocker rewritten in user-action language
- next route reason, not just next route label
- field-origin marker for lower-derived vs upper-added content
- confidence / readiness level for translation

## 6. Validation

- Grounding: field list matches current JSON artifacts.
- Field meaning: interpreted conservatively.
- Visibility vs hiddenness: captured per field or field group.

