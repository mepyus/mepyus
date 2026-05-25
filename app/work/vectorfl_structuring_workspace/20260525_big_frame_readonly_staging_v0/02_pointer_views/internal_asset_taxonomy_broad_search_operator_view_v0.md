# Internal Asset Taxonomy Broad Search Safe-Line Map v0

status: POINTER_ONLY / NOT_AUTHORITY / NO_MOVE / HOLD

search_file_count: 7847
family_count: 12

## Families

### P_PACKET_HANDOFF_ASSET
- count: 9846
- definition: Codex/Gemini/Hermes handoff, read-only review packet, task packet 계열
- safe_line: pointer-only; no live call; no external action
- surfaces: {'work_control': 5067, 'workspace_control': 53, 'run_generated': 2531, 'source_docs': 2195}
- examples:
  - app/work/space-skill-sandbox/packages/package_050_inventory/report_files.txt / sha b66092948831 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/01_principles/VECTORFL_ASSET_TYPE_AND_LACL_SCHEMA_FROM_BATCHES_V0.json / sha 0c0664e69f79 / workspace_control
  - app/work/MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0.md / sha 14b0a334cbd4 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/batch02_pointer_only_precheck_v0.json / sha 50a4aed0eb59 / workspace_control

### R_RECEIPT_TRACE_ASSET
- count: 4606
- definition: receipt/trace/validation/rollback/sha evidence 계열
- safe_line: evidence only; not authority/approval
- surfaces: {'work_control': 2195, 'workspace_control': 42, 'run_generated': 1021, 'source_docs': 1348}
- examples:
  - app/work/space-skill-sandbox/packages/package_050_inventory/report_files.txt / sha b66092948831 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/01_principles/VECTORFL_ASSET_TYPE_AND_LACL_SCHEMA_FROM_BATCHES_V0.json / sha 0c0664e69f79 / workspace_control
  - app/work/MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0.md / sha 14b0a334cbd4 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/batch02_pointer_only_precheck_v0.json / sha 50a4aed0eb59 / workspace_control

### G_GATE_GUARD_ASSET
- count: 5103
- definition: guard/precheck/negative test/STOP/HOLD 계열
- safe_line: can strengthen workspace rule; not apply approval
- surfaces: {'work_control': 2365, 'workspace_control': 37, 'run_generated': 1340, 'source_docs': 1361}
- examples:
  - app/work/space-skill-sandbox/packages/package_050_inventory/report_files.txt / sha b66092948831 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/01_principles/VECTORFL_ASSET_TYPE_AND_LACL_SCHEMA_FROM_BATCHES_V0.json / sha 0c0664e69f79 / workspace_control
  - app/work/MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0.md / sha 14b0a334cbd4 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/batch02_pointer_only_precheck_v0.json / sha 50a4aed0eb59 / workspace_control

### S_STATE_PROMOTION_ASSET
- count: 5642
- definition: INBOX/CANDIDATE/MATURED/AUTHORITY/freeze 상태 계열
- safe_line: authority-sensitive; freeze; no promotion mutation
- surfaces: {'work_control': 2845, 'workspace_control': 55, 'run_generated': 1313, 'source_docs': 1429}
- examples:
  - app/work/space-skill-sandbox/packages/package_050_inventory/report_files.txt / sha b66092948831 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/01_principles/VECTORFL_ASSET_TYPE_AND_LACL_SCHEMA_FROM_BATCHES_V0.json / sha 0c0664e69f79 / workspace_control
  - app/work/MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0.md / sha 14b0a334cbd4 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/batch02_pointer_only_precheck_v0.json / sha 50a4aed0eb59 / workspace_control

### X_POINTER_GRAPH_ASSET
- count: 4213
- definition: pointer/index/route/dedupe/conflict map 계열
- safe_line: workspace pointer allowed; authoritative registry not allowed
- surfaces: {'work_control': 1963, 'workspace_control': 56, 'run_generated': 933, 'source_docs': 1261}
- examples:
  - app/work/space-skill-sandbox/packages/package_050_inventory/report_files.txt / sha b66092948831 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/01_principles/VECTORFL_ASSET_TYPE_AND_LACL_SCHEMA_FROM_BATCHES_V0.json / sha 0c0664e69f79 / workspace_control
  - app/work/MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0.md / sha 14b0a334cbd4 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/batch02_pointer_only_precheck_v0.json / sha 50a4aed0eb59 / workspace_control

### Q_QUEUE_INBOX_ASSET
- count: 664
- definition: queue/inbox/review/quarantine 계열
- safe_line: small batch review; no bulk apply
- surfaces: {'work_control': 269, 'workspace_control': 25, 'run_generated': 147, 'source_docs': 223}
- examples:
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/01_principles/VECTORFL_ASSET_TYPE_AND_LACL_SCHEMA_FROM_BATCHES_V0.json / sha 0c0664e69f79 / workspace_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/batch02_pointer_only_precheck_v0.json / sha 50a4aed0eb59 / workspace_control
  - docs/reports/function_process_formation_prework_first_application_tools_leave_their_maker_v0.md / sha bb085260a297 / source_docs
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/high_risk_6_reference_map_batch01_v0.json / sha 1577e62bb9df / workspace_control

### O_OPERATOR_SURFACE_ASSET
- count: 1791
- definition: operator dashboard/compact view/risk distribution 계열
- safe_line: operator attention only; not patch plan
- surfaces: {'work_control': 742, 'workspace_control': 39, 'run_generated': 540, 'source_docs': 470}
- examples:
  - app/work/space-skill-sandbox/packages/package_050_inventory/report_files.txt / sha b66092948831 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/01_principles/VECTORFL_ASSET_TYPE_AND_LACL_SCHEMA_FROM_BATCHES_V0.json / sha 0c0664e69f79 / workspace_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/batch02_pointer_only_precheck_v0.json / sha 50a4aed0eb59 / workspace_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/high_risk_6_reference_map_batch01_v0.json / sha 1577e62bb9df / workspace_control

### B_BRIDGE_ADAPTER_ASSET
- count: 5462
- definition: tool bridge/adapter/channel/shell 계열
- safe_line: no live API/Codex/Gemini unless scoped
- surfaces: {'work_control': 2850, 'workspace_control': 33, 'run_generated': 1457, 'source_docs': 1122}
- examples:
  - app/work/space-skill-sandbox/packages/package_050_inventory/report_files.txt / sha b66092948831 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/01_principles/VECTORFL_ASSET_TYPE_AND_LACL_SCHEMA_FROM_BATCHES_V0.json / sha 0c0664e69f79 / workspace_control
  - app/work/MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0.md / sha 14b0a334cbd4 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/batch02_pointer_only_precheck_v0.json / sha 50a4aed0eb59 / workspace_control

### M_MODULE_SKELETON_ASSET
- count: 887
- definition: M1~M8 module/skeleton/lane 계열
- safe_line: workspace design candidate; not architecture authority
- surfaces: {'work_control': 249, 'workspace_control': 45, 'run_generated': 484, 'source_docs': 109}
- examples:
  - app/work/space-skill-sandbox/packages/package_050_inventory/report_files.txt / sha b66092948831 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/01_principles/VECTORFL_ASSET_TYPE_AND_LACL_SCHEMA_FROM_BATCHES_V0.json / sha 0c0664e69f79 / workspace_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/batch02_pointer_only_precheck_v0.json / sha 50a4aed0eb59 / workspace_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/high_risk_6_reference_map_batch01_v0.json / sha 1577e62bb9df / workspace_control

### C_CONTEXT_LAYER_ASSET
- count: 4197
- definition: context/layer/LACL/claim/authority-boundary 계열
- safe_line: classification candidate; no source mutation
- surfaces: {'work_control': 1982, 'workspace_control': 24, 'run_generated': 894, 'source_docs': 1297}
- examples:
  - app/work/space-skill-sandbox/packages/package_050_inventory/report_files.txt / sha b66092948831 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/01_principles/VECTORFL_ASSET_TYPE_AND_LACL_SCHEMA_FROM_BATCHES_V0.json / sha 0c0664e69f79 / workspace_control
  - app/work/MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0.md / sha 14b0a334cbd4 / work_control
  - docs/reports/function_process_formation_prework_first_application_tools_leave_their_maker_v0.md / sha bb085260a297 / source_docs

### U_RUN_BUNDLE_ASSET
- count: 6820
- definition: run/bundle/report/closeout/rollup 실행 산출물 계열
- safe_line: receipt/evidence; may be compacted but not source of truth
- surfaces: {'work_control': 3613, 'workspace_control': 28, 'run_generated': 1457, 'source_docs': 1722}
- examples:
  - app/work/space-skill-sandbox/packages/package_050_inventory/report_files.txt / sha b66092948831 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/01_principles/VECTORFL_ASSET_TYPE_AND_LACL_SCHEMA_FROM_BATCHES_V0.json / sha 0c0664e69f79 / workspace_control
  - app/work/MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0.md / sha 14b0a334cbd4 / work_control
  - app/work/vectorfl_structuring_workspace/20260525_big_frame_readonly_staging_v0/02_pointer_views/batch02_pointer_only_precheck_v0.json / sha 50a4aed0eb59 / workspace_control

### SEC_SECRET_SURFACE_RISK
- count: 676
- definition: token/password/secret/API-key 등 보안 민감 표면 가능성
- safe_line: do not copy lines; redact; manual/security review before any preservation
- surfaces: {'work_control': 407, 'workspace_control': 6, 'run_generated': 111, 'source_docs': 152}
- examples:
  - app/work/space-skill-sandbox/packages/package_050_inventory/report_files.txt / sha b66092948831 / work_control
  - app/work/MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0.md / sha 14b0a334cbd4 / work_control
  - docs/reports/function_process_formation_prework_first_application_tools_leave_their_maker_v0.md / sha bb085260a297 / source_docs
  - app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/FLOW_NETWORK_CURRENT_EXECUTION_TOPOLOGY_STATE_V0.md / sha 072ac5d3f2d6 / work_control
