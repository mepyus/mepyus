# Integrated Engine Review Bundle Structuring Schema Augmentation Plan v0

## Status

PASS_WITH_NOTE

Current status:

```text
eligible for provisional camera candidate, not promoted
```

This plan identifies where the structuring record schema should augment the existing review-stage bundle.
It does not patch the existing documents yet.

## Augmentation Principle

Do not add every schema field to every document.
Add only the fields that strengthen the document's current role.
Use companion notes when a document is too role-specific.

## Target Documents

| document | current role | schema fields to add | why these fields matter here | what should not be added | update timing |
|---|---|---|---|---|---|
| `integrated_engine_provisional_camera_candidate_review_note_v0.md` | Slot-by-slot review and whole-frame verdict. | `base_content_trace`, `applied_lens_record`, `structural_principle`, `layer_reapplication_hint`, `what_this_is_not` | The review note should preserve why C0-C6 worked, which lens read it, what principle emerged, and how it may be reread later. | Do not add final camera usage approval or promotion language. | recommended next patch |
| `integrated_engine_provisional_camera_candidate_usage_boundary_v0.md` | Allowed/disallowed target shapes and return boundaries. | `target_shape_assumption`, `what_this_is_not`, `rollback_or_boundary` | Boundary document should show assumptions and prevent review-use from becoming promotion. | Do not add full base content trace; it is not a source evidence doc. | can wait unless boundary confusion appears |
| `integrated_engine_provisional_camera_usage_procedure_v0.md` | Step-by-step review-stage usage procedure. | `action_of_structuring`, `rollback_or_boundary`, `next_valid_use` | Procedure needs verbs and rollback points at each step. | Do not add broad archetype theory. | recommended after review note patch |
| `integrated_engine_lens_slot_compatibility_matrix_v0.md` | Operational lens-to-slot compatibility. | `applied_lens_record`, `false_precedent_or_risk`, `what_this_is_not` | Matrix needs explicit warning that lens fit is not glossary or universal reading. | Do not add full process archetype narrative. | can wait |
| `integrated_engine_provisional_camera_review_bundle_summary_v0.md` | Bundle entry and current status summary. | `structural_principle`, `layer_reapplication_hint`, `next_valid_use` | Summary should tell future readers why the bundle matters beyond one camera review. | Do not repeat all field details. | recommended after core docs patched |
| `integrated_engine_internal_camera_lens_precedent_mining_protocol_v0.md` | Pre-usage mining layer protocol. | `base_content_trace`, `layer_reapplication_hint`, `false_precedent_or_risk`, `record/redeposit` equivalent | Mining needs to keep source traces and false precedents visible. | Do not turn mining log into canonical camera evidence. | recommended if mining is used in next turn |

## Required Field Connections

- review note: `base_content_trace / applied_lens_record / structural_principle / layer_reapplication_hint`
- usage boundary: `target_shape_assumption / what_this_is_not`
- usage procedure: `action_of_structuring / rollback_or_boundary`
- lens-slot matrix: `applied_lens_record / false_precedent_or_risk`
- precedent mining protocol: `base_content_trace / layer_reapplication_hint / false_precedent_or_risk`

## Patch Priority

1. Patch review note first.
2. Patch usage procedure second.
3. Patch bundle summary third.
4. Patch lens-slot matrix and mining protocol only when they are actively used.
5. Keep usage boundary stable unless target-shape confusion reappears.

## Verification

- document roles blurred? no; field selection is role-specific.
- every document forced to carry all fields? no.
- review-stage bundle and precedent-mining layer connected? yes.
- promotion opened? no.

## Pointers

- Schema: `docs/reports/integrated_engine_structuring_record_schema_v0.md`
- Minimal patch policy: `docs/reports/integrated_engine_minimal_structuring_patch_policy_v0.md`
- Integration summary: `docs/reports/integrated_engine_structuring_archetype_integration_summary_v0.md`
