# VECTORFL_CROSS_LAYER_GUARD_MATRIX_CANDIDATE_20260523_V0

status: CROSS_LAYER_GUARD_MATRIX_CANDIDATE_WITH_HOLD
created_at: 2026-05-23 10:13:27 KST

## 0. Purpose

Normalize guard statuses across all six program-unit layers so user surfaces and dashboards cannot soften STOP/HOLD.

This is no-model candidate material. It is not implementation, authority, promotion, workflow schema, or registry mutation.

## 1. Guard status meanings

| guard_status | when to use | surface label rule | forbidden drift |
|---|---|---|---|
| PASS_WITH_HOLD | local evidence exists, validator passed, no authority/promotion implied | label must include HOLD or candidate/evidence language | never call READY/APPROVED/PROMOTED |
| WATCH | structural risk or incomplete coupling exists, but no immediate STOP | label must preserve WATCH and risk note | never show green-ready language |
| HOLD_STOP_REVIEW | boundary pressure exists: label/authority/promotion could drift | label must include exact HOLD_STOP_REVIEW | do not soften to warning only |
| STOP | forbidden action or contamination detected | label must include exact STOP | do not continue until isolated |
| HOLD_UNTIL_APPROVED_MODEL_OUTPUT | model/tool output would be needed but explicit approval/output is absent | label must include exact HOLD_UNTIL_APPROVED_MODEL_OUTPUT | do not imply packet prepared equals model result |

## 2. Cross-layer matrix cases

| case_id | layer | trigger | guard_status | surface_label_rule | stop_condition |
|---|---|---|---|---|---|
| GM-INPUT-PASS-001 | input_layer | fixture input localized with declared path and receipt | PASS_WITH_HOLD | input accepted as candidate evidence with HOLD | live DB intake or undeclared input path |
| GM-INPUT-STOP-001 | input_layer | secret/live connector/API key or live DB intake requested | STOP | STOP: live intake/secret/connector blocked | any credential, connector, network, or live DB write |
| GM-EVIDENCE-PASS-001 | evidence_layer | receipt_ref exists and links local output | PASS_WITH_HOLD | receipt evidence with HOLD, not authority | receipt described as authority |
| GM-EVIDENCE-HOLD-001 | evidence_layer | receipt exists but lineage input->output->review is incomplete | HOLD_STOP_REVIEW | HOLD_STOP_REVIEW: lineage incomplete | dashboard hides incomplete lineage |
| GM-GUARD-HOLD-001 | review_guard_layer | promotion/Program Alpha/M4 language appears near candidate evidence | HOLD_STOP_REVIEW | HOLD_STOP_REVIEW: promotion language must be reviewed | promotion claim applied |
| GM-GUARD-STOP-001 | review_guard_layer | authority mutation/schema mutation/router-runner instruction detected | STOP | STOP: authority/schema/router mutation blocked | mutation instruction or execution |
| GM-SURFACE-WATCH-001 | surface_layer | dashboard/status card exists but evidence coupling is weak | WATCH | WATCH: label evidence coupling incomplete | green approval badge or readiness language |
| GM-SURFACE-HOLD-001 | surface_layer | surface label softens HOLD_STOP_REVIEW/STOP | HOLD_STOP_REVIEW | HOLD_STOP_REVIEW: surface label softened guard state | softened label published |
| GM-REENTRY-HOLD-001 | tool_reentry_layer | Codex/Gemini packet prepared but no approved raw output exists | HOLD_UNTIL_APPROVED_MODEL_OUTPUT | HOLD_UNTIL_APPROVED_MODEL_OUTPUT: packet prepared, not executed | packet treated as model result |
| GM-REENTRY-STOP-001 | tool_reentry_layer | model output claims truth/authority/edit permission/promotion | STOP | STOP: model output authority/promotion claim blocked | claim enters shared surface as authority |
| GM-RECOVERY-WATCH-001 | operator_recovery_layer | artifact index/checksum/recovery card helps navigation | WATCH | WATCH: recovery aid only, not baseline freeze | checksum called v1 snapshot/baseline authority |
| GM-RECOVERY-HOLD-001 | operator_recovery_layer | artifact growth creates navigation ambiguity | HOLD_STOP_REVIEW | HOLD_STOP_REVIEW: recovery bundle grouping needed | old/new artifacts treated as authority without receipt |

## 3. Fixture source

```text
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_cross_layer_guard_matrix_candidate_v0/fixtures/cross_layer_guard_matrix_fixture.json
```

## 4. Matrix rules

```text
1. PASS_WITH_HOLD must never become APPROVED or READY.
2. WATCH must stay visible as WATCH in user surfaces.
3. HOLD_STOP_REVIEW must appear exactly when boundary pressure exists.
4. STOP must block continuation until isolated.
5. HOLD_UNTIL_APPROVED_MODEL_OUTPUT must be used for prepared-but-not-executed model/tool lanes.
6. No surface label may soften STOP/HOLD_STOP_REVIEW/HOLD_UNTIL_APPROVED_MODEL_OUTPUT.
7. No guard status creates authority mutation or promotion.
```

## 5. Next smallest action

```text
VECTORFL_SURFACE_TO_EVIDENCE_TRACE_MAP_CANDIDATE_20260523_V0.md
```

Reason:

```text
The guard matrix defines labels. Next, map each user surface/dashboard label back to evidence/receipt/guard_status so labels cannot drift.
```

## 6. HOLD

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
