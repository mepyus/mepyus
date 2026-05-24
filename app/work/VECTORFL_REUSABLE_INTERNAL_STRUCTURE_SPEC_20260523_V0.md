# VECTORFL_REUSABLE_INTERNAL_STRUCTURE_SPEC_20260523_V0

status: REUSABLE_INTERNAL_STRUCTURE_SPEC_CANDIDATE_WITH_HOLD
created_at: 2026-05-23 10:34:42 KST

## 0. Use this when

Use this as a pocket reference when creating future VectorFL personal-program artifacts.

It tells future work:

```text
which layer an artifact belongs to
which guard label it needs
which receipt/evidence link it must carry
what it must NOT claim
```

## 1. Reusable layer spec

| layer | allowed purpose | required evidence | default guard | forbidden claim |
|---|---|---|---|---|
| input_layer | locate declared input/local fixture/personal intake boundary | input_ref + output_ref + receipt_ref | PASS_WITH_HOLD or STOP | live DB intake enabled |
| evidence_layer | preserve receipt/evidence lineage | receipt_ref + source_artifact + trace_id | PASS_WITH_HOLD or HOLD_STOP_REVIEW | receipt is authority |
| review_guard_layer | block promotion/authority/live drift | guard_status + negative-case reason | HOLD_STOP_REVIEW or STOP | M4/Program Alpha approved |
| surface_layer | expose read-only status to user | surface_label + receipt_ref + guard_status | WATCH or PASS_WITH_HOLD | approval/readiness badge |
| tool_reentry_layer | receive approved model/tool output only through raw/lite/receipt/re-entry | packet/ref + raw/lite/receipt if approved | HOLD_UNTIL_APPROVED_MODEL_OUTPUT or STOP | packet equals model result |
| operator_recovery_layer | help next session/tool recover context | handoff/index/checksum/receipt | WATCH | baseline freeze/v1 snapshot |

## 2. Reusable trace row minimum

```yaml
trace_id: TRACE-YYYYMMDD-LAYER-0001
source_layer: <one of six layers>
source_artifact: <local path>
input_ref: <local path or null>
output_ref: <local path or null>
receipt_ref: <local path>
guard_status: <PASS_WITH_HOLD|WATCH|HOLD_STOP_REVIEW|STOP|HOLD_UNTIL_APPROVED_MODEL_OUTPUT>
surface_label: <label preserving guard_status>
reentry_ref: <local path or null>
authority_effect: NO_AUTHORITY_MUTATION
promotion_status: HOLD
next_action: <bounded next action>
watch_notes:
  - candidate material only
```

## 3. Reusable guard status rules

```text
PASS_WITH_HOLD: validator/evidence passed but not approved/promoted
WATCH: safe to continue locally, but risk/incompleteness remains visible
HOLD_STOP_REVIEW: boundary pressure; review before continuing or surfacing
STOP: forbidden action/claim/mutation; isolate before any continuation
HOLD_UNTIL_APPROVED_MODEL_OUTPUT: packet/template exists but real model output is absent or unapproved
```

## 4. Reusable surface label rule

Every user-facing card/dashboard/handoff line must answer:

```text
What evidence supports this?
What receipt supports this?
What guard_status controls this?
What must this NOT be interpreted as?
```

## 5. Reusable model re-entry contract

If a future explicit model lane is approved, capture only as:

```text
RAW_OUTPUT
LITE_SUMMARY
MODEL_RUN_RECEIPT
HOLD_REVIEW
REENTRY_COMPRESSION
USER_SURFACE_CARD
```

Never as:

```text
authority
permission
promotion
truth source
registry mutation
implementation patch
```

## 6. Current reusable-but-not-promoted components

| component | reusable as | not yet |
|---|---|---|
| 12-candidate chain | evidence map | M4 modules |
| six-layer structure | internal architecture lens | runtime architecture |
| trace ledger schema | candidate row shape | DB schema |
| guard matrix | label/status rule | enforcement engine |
| surface-to-evidence map | interpretation guard | UI framework |
| model packet templates | approved future capture shape | model execution result |
| operator recovery index | handoff/navigation | baseline/v1 snapshot |

## 7. HOLD

promotion_status: HOLD
program_alpha_status: NOT_READY
vectorfl_authority_mutation: no
model_execution: no
real_gemini_execution: no
real_codex_execution: no
approval_applied: no
live_db_intake: HOLD
schema_mutation: no
snapshot_mutation: no
router_runner_claim: no
write_ui: no
authority_database: no
shared_db_mutation: no
v1_snapshot_creation: no
m4_reusable_module: no
module_promotion: no
program_alpha_ready: no
