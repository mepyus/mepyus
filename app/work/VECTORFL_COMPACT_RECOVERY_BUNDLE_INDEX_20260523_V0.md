# VECTORFL_COMPACT_RECOVERY_BUNDLE_INDEX_20260523_V0
status: COMPACT_RECOVERY_BUNDLE_INDEX_WITH_HOLD
created_at: 2026-05-23 10:44:16 KST
updated_at: 2026-05-23 11:29:09 KST

## 0. Purpose

Group the many artifacts into reusable bundles so future sessions can retrieve the right spec/evidence quickly without treating any artifact as authority.

This is a recovery/navigation index only.
It is not baseline freeze, not v1 snapshot, not registry, not workflow authority, not module promotion.

## 0.1 Maintenance reflection

```text
diagnosis: S1-S8 hardening artifacts existed outside compact recovery index
verification: reviewed review_guard receipt and prior compact index
test_run: local bundle index validator with checksum verification
actual_result: added BUNDLE-09 for operator_recovery/surface/review_guard hardening artifacts
applied_change: compact recovery index MD/JSON now retrieve S1-S8 layer hardening artifacts
not_applied: no authority mutation, no promotion, no schema/baseline/workflow mutation
```

## 1. Start here rule

If a future session asks “where were we?” read in this order:

```text
1. VECTORFL_COMPACT_RECOVERY_QUICKSTART_20260523_V0.md
2. VECTORFL_DIAGNOSE_VERIFY_TEST_REFLECT_QUICKSTART_20260523_V0.md
3. VECTORFL_S1_S8_LOOP_CHECKLIST_TEMPLATE_20260523_V0.md
4. VECTORFL_REUSABLE_INTERNAL_STRUCTURE_SPEC_20260523_V0.md
5. VECTORFL_PROGRAM_UNIT_STRUCTURE_PROGRESS_REVIEW_20260523_V0.md
6. VECTORFL_COMPACT_RECOVERY_BUNDLE_INDEX_20260523_V0.md
```

## 2. Bundles

| bundle_id | name | purpose | boundary_note |
|---|---|---|---|
| BUNDLE-00-START-HERE | start_here | where to begin next session | read first; navigation only |
| BUNDLE-01-DIRECTION | direction_review | direction fit and progress review | direction YES_WITH_HOLD, not readiness |
| BUNDLE-02-STRUCTURE-SPEC | internal_structure | six-layer program-unit spec | pocket spec, not runtime architecture |
| BUNDLE-03-CANDIDATE-CHAIN | candidate_chain | 12 candidate local/synthetic evidence | candidate evidence, not M4 modules |
| BUNDLE-04-TRACE | traceability | trace ledger schema/fixture/surface map | trace candidate only, not DB schema |
| BUNDLE-05-GUARD | guard_matrix | guard statuses and negative cases | status rule, not enforcement engine |
| BUNDLE-06-MODEL-REENTRY | model_reentry | Codex/Gemini packets and future capture contract | prepared, not executed |
| BUNDLE-07-OPERATOR-RECOVERY | operator_recovery | handoff/checksum/recovery surfaces | navigation, not baseline freeze |
| BUNDLE-08-DIAGNOSE-VERIFY-TEST-REFLECT | diagnose_verify_test_reflect | mandatory diagnosis/verification/test/reflection loop and real bounded test evidence | diagnostic loop, not promotion or authority |
| BUNDLE-09-S1-S8-LAYER-HARDENING | s1_s8_layer_hardening | retrieve concrete S1-S8 hardening artifacts for operator_recovery_layer, surface_layer, and review_guard_layer | layer hardening evidence only, not enforcement engine, authority, promotion, or readiness |

## 3. Bundle file map

### BUNDLE-00-START-HERE — start_here

- `app/work/VECTORFL_COMPACT_RECOVERY_QUICKSTART_20260523_V0.md` — exists=TRUE sha256=fec5029d62cdf201289417d1746f191338740ac9a4f8ff7d53c8fccbb44f6d74
- `app/work/VECTORFL_PROGRAM_UNIT_PROGRESS_REVIEW_USER_STATUS_CARD_20260523_V0.md` — exists=TRUE sha256=249111a086b5c09d7f114a70692fa59378150e3385543e6f40ec3aad94370937
- `app/work/VECTORFL_REUSABLE_INTERNAL_STRUCTURE_SPEC_20260523_V0.md` — exists=TRUE sha256=66a9488250929ca6bd86963e91eb33289a11f1447fe5d9ef398b7ef45b6309d0

### BUNDLE-01-DIRECTION — direction_review

- `app/work/VECTORFL_PROGRAM_UNIT_STRUCTURE_PROGRESS_REVIEW_20260523_V0.md` — exists=TRUE sha256=c179885311c9860f5df36f6cde92bd568dfc76c260ee08189c64cc3d001e0c32
- `app/work/VECTORFL_PROGRAM_UNIT_STRUCTURE_PROGRESS_DASHBOARD_20260523_V0.json` — exists=TRUE sha256=44e89f4d2089db0525002dbbbb3728219a9d2bd3cc8d581a9a631cc0c3c279a1
- `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_program_unit_structure_progress_review_v0/receipt.md` — exists=TRUE sha256=ef69610b90a1e5e26e1baada38b6c710ddf4ada3222248c71d7eeb55de75827f

### BUNDLE-02-STRUCTURE-SPEC — internal_structure

- `app/work/VECTORFL_PROGRAM_UNIT_INTERNAL_STRUCTURE_SPEC_20260523_V0.md` — exists=TRUE sha256=fd8aee5af7f52140902ef685da410c4f75b9abe9f88cb397a501d94a319961ea
- `app/work/VECTORFL_REUSABLE_INTERNAL_STRUCTURE_SPEC_20260523_V0.md` — exists=TRUE sha256=66a9488250929ca6bd86963e91eb33289a11f1447fe5d9ef398b7ef45b6309d0
- `app/work/VECTORFL_PROGRAM_UNIT_INTERNAL_STRUCTURE_DASHBOARD_20260523_V0.json` — exists=TRUE sha256=4323c6eda1aef72e5bdbd7098dde30f4c244e77350eef0a7749e052d3eeed3c7

### BUNDLE-03-CANDIDATE-CHAIN — candidate_chain

- `app/work/VECTORFL_TWELVE_CANDIDATE_PERSONAL_PROGRAM_COMPLETE_CHAIN_RECEIPT_20260523_V0.md` — exists=TRUE sha256=3d5cd5e27db7644b116d9882d08df60455db1208f7f0272a37bc107880dd1295
- `app/work/VECTORFL_TWELVE_CANDIDATE_CONSOLIDATION_DASHBOARD_20260523_V0.json` — exists=TRUE sha256=60e4f8750f7cedff9dfb32b80a4af6fd11b31806a58809a9f995445eb5cf91aa
- `app/work/VECTORFL_TWELVE_CANDIDATE_HOLD_STOP_COVERAGE_MAP_20260523_V0.md` — exists=TRUE sha256=ed53ed6bb3d7753e1c1cbca0eaeff197e76a98a14e9ea91d8ff1a3baadae10b5

### BUNDLE-04-TRACE — traceability

- `app/work/VECTORFL_PROGRAM_UNIT_TRACE_LEDGER_SCHEMA_CANDIDATE_20260523_V0.md` — exists=TRUE sha256=a1bcd8acb7621f2c05a82c579828e0628adc9b64c17a8cb18cf7f6102be2312d
- `app/work/VECTORFL_PROGRAM_UNIT_TRACE_LEDGER_FIXTURE_REHEARSAL_20260523_V0.md` — exists=TRUE sha256=d0d8a107ac200fe1caf2f5dd77a6fcc5668f3022e054e27a646fcdb5ff91ad76
- `app/work/VECTORFL_SURFACE_TO_EVIDENCE_TRACE_MAP_CANDIDATE_20260523_V0.md` — exists=TRUE sha256=2505d0fa83d52fd4969bb73a4bfc6901cb12cf7672f97668420c2e236b4364e4

### BUNDLE-05-GUARD — guard_matrix

- `app/work/VECTORFL_CROSS_LAYER_GUARD_MATRIX_CANDIDATE_20260523_V0.md` — exists=TRUE sha256=3b39d174e4f9e5e4f2295f9df739bd8fdd09f8332aded08434a6b11296a5be32
- `app/work/VECTORFL_CROSS_LAYER_GUARD_MATRIX_CANDIDATE_20260523_V0.json` — exists=TRUE sha256=e1e148b51fa3f88a19d554ec898e623ad40265f6350409591f267ca291846c63
- `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_cross_layer_guard_matrix_candidate_v0/receipt.md` — exists=TRUE sha256=55c9b3e6c05bce53c98c9153c4e9bd43dfa241e7ece0c1ba069c8a30c8286fad

### BUNDLE-06-MODEL-REENTRY — model_reentry

- `app/work/VECTORFL_MODEL_EXECUTION_DECISION_CARD_20260523_V0.md` — exists=TRUE sha256=4e3c2329f1e6d130284ce12f94cbb5cc762bfc54953502300a10e2ca22b5b71f
- `app/work/space-skill-sandbox/relay/packets/to_codex/codex_review_only_twelve_candidate_dashboard_20260523_v0/PACKET.md` — exists=TRUE sha256=58b93c0f5d0c85458e63989fac76bdadbbdd2a4ea3f43aaa051d9861a93779cb
- `app/work/space-skill-sandbox/relay/packets/to_gemini/gemini_gap_scan_twelve_candidate_dashboard_20260523_v0/PACKET.md` — exists=TRUE sha256=5e52326115883d1eeda7b35d8a3de2c90db8085a02c215d2f85bf41a5a5bdebb
- `app/work/space-skill-sandbox/relay/templates/post_model_run_receipt_pack_20260523_v0/README.md` — exists=TRUE sha256=8f2ee676e608837c687361cccec017a55301b32686886e9b104f30eea41c0a29

### BUNDLE-07-OPERATOR-RECOVERY — operator_recovery

- `app/work/CHATGPT_CODEX_GEMINI_SAME_DAY_FINAL_HANDOFF_UPDATE_20260523_V0.md` — exists=TRUE sha256=803aec443d73ee431d54477b290e3da1901db99661ff0e574f2cbb984ec1d526
- `app/work/VECTORFL_END_OF_DAY_OPERATOR_RECOVERY_INDEX_20260523_V0.md` — exists=TRUE sha256=44bd0033c7d1428daaa45beb9a50bba007ef49386c9d3dde790c8a0120291344
- `app/work/VECTORFL_HANDOFF_RECOVERY_INTEGRITY_CHECKSUM_INDEX_20260523_V0.md` — exists=TRUE sha256=008e266bda59b0049f1b6fc8c0ec586b0fb4c7ab46c1c1ef5cfd27445abad2b4

### BUNDLE-08-DIAGNOSE-VERIFY-TEST-REFLECT — diagnose_verify_test_reflect

- `app/work/VECTORFL_DIAGNOSE_VERIFY_TEST_REFLECT_LOOP_SPEC_20260523_V0.md` — exists=TRUE sha256=65a26301c3884a5d19ce2a090b7f58f03cebb4a67ad29e31fc889d370a596f07
- `app/work/VECTORFL_DIAGNOSE_VERIFY_TEST_REFLECT_QUICKSTART_20260523_V0.md` — exists=TRUE sha256=4e1d10f6bdb6080364ad807c394d49cf3b655d845f97ef52c3f39ad286289198
- `app/work/VECTORFL_REAL_CODEX_REVIEW_ONLY_BUNDLE_AUDIT_SUMMARY_20260523_V0.md` — exists=TRUE sha256=f7851876168edda855ec12adc85dae5d94852d89b8273dc998a2b117c5f98a07
- `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_real_codex_review_only_bundle_audit_v0/codex_output/codex_recovery_return.md` — exists=TRUE sha256=fe9748207c77f57cfb1f372b64c6540e489e44f2c9a5059810e95ced6dfa417a

### BUNDLE-09-S1-S8-LAYER-HARDENING — s1_s8_layer_hardening

- `app/work/VECTORFL_S1_S8_LOOP_CHECKLIST_TEMPLATE_20260523_V0.md` — exists=TRUE sha256=dc30734acd0689755e28ce3ac1f9cd47807f36690f19405656646de07c95534e
- `app/work/VECTORFL_OPERATOR_RECOVERY_LAYER_S1_S8_HARDENING_20260523_V0.md` — exists=TRUE sha256=b91806bc3feaca798419cadb83f3bbe427bd322473d13ae1460404778b1c779b
- `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_operator_recovery_s1_s8_loop_hardening_v0/receipt.md` — exists=TRUE sha256=b6050b3edef524f1ed6c3af809246f70136431c9f02b50fe8ffbbe27c950f770
- `app/work/VECTORFL_SURFACE_LAYER_S1_S8_LABEL_PRESSURE_HARDENING_20260523_V0.md` — exists=TRUE sha256=99cbba77710ab089ce4d91da654b804854e3ed72f5d92a48cc2cdaad04113175
- `app/work/VECTORFL_SURFACE_LABEL_PRESSURE_RULES_20260523_V0.md` — exists=TRUE sha256=a3f16a75c8071490efd0f15dc76e1d70d49e25cf10a491e69ff1f91929a67c1d
- `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_surface_layer_s1_s8_label_pressure_hardening_v0/receipt.md` — exists=TRUE sha256=2982d3ccce7a494931edd2e6142d4a4aad179e46fe90caa700cfd205a72495bc
- `app/work/VECTORFL_REVIEW_GUARD_LAYER_S1_S8_NEGATIVE_CASE_EXPANSION_20260523_V0.md` — exists=TRUE sha256=211aea8715e47f7d8b3a8898bccbb8d30f721b9094134b43b8841e4f56f2f28a
- `app/work/VECTORFL_REVIEW_GUARD_NEGATIVE_CASE_RULES_20260523_V0.md` — exists=TRUE sha256=14280c468b0dd5074c9e226059d536496e69c1d2891d74ccc34f0ab490c3cb48
- `app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260523_review_guard_s1_s8_negative_case_expansion_v0/receipt.md` — exists=TRUE sha256=6c3e0f39414b9003e5895a51e602e2e4a0aac375a45d09c5ccbab27326fc5fe2

## 4. Reuse lookup

Use:

```text
VECTORFL_REUSE_LOOKUP_SPEC_20260523_V0.md
VECTORFL_DIAGNOSE_VERIFY_TEST_REFLECT_LOOP_SPEC_20260523_V0.md
VECTORFL_S1_S8_LOOP_CHECKLIST_TEMPLATE_20260523_V0.md
```

for “what do I copy/reuse for X?” and “what must be tested/reflected?” questions.

## 5. HOLD

promotion_status: HOLD
program_alpha_status: NOT_READY
vectorfl_authority_mutation: no
real_codex_execution: YES_BOUNDED_REVIEW_ONLY_FOR_AUDIT_PACKET
real_gemini_execution: no
approval_applied_to_promotion: no
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
