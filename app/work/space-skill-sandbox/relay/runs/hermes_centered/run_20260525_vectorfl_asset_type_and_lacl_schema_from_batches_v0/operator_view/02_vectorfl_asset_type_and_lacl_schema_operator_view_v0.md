# VectorFL Asset Type + LACL Schema from Batches v0

status: WORKSPACE_INTERNAL_CANDIDATE / NOT_AUTHORITY / HOLD

## Asset types

### T01_SOURCE_ORIENTATION_HANDLE
- definition: 원본 경로/원본 sha가 판단과 연결의 기준점이 되는 자산. source of truth 자체로 승격하는 것이 아니라 방향/위치 핸들로 유지한다.
- modules: M1_intake_provenance, M2_asset_graph_router
- LACL role: claim/source/context anchor
- move_policy: NO_MOVE_UNTIL_MANIFEST_ROLLBACK_APPROVAL
- authority_boundary: orientation handle != authority registry
- evidence examples:
  - batch03_space_governed_lacl / BATCH03_ITEM_02 / docs/reports/external_thought_asset_research_round_005_manual_stage_0_event_dry_run_batch_v0.md / sha 74e62e6f113f
  - batch02_module_spread / BATCH02_ITEM_03 / app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_ASSET_FUNCTION_FAMILY_MAP_FROM_05_15_V0.md / sha e92fe2f9666e
  - batch03_space_governed_lacl / BATCH03_ITEM_01 / docs/reports/external_candidate_four_source_cross_synthesis_v0.md / sha a8bf757b3b50

### T02_POINTER_VIEW
- definition: 원본을 옮기지 않고 workspace/module lane에서 원본·copy·검토 산출물을 가리키는 pointer/index 자산.
- modules: M2_asset_graph_router
- LACL role: relation/context routing layer
- move_policy: POINTER_ONLY_CAN_UPDATE_IN_WORKSPACE
- authority_boundary: not registry; not current-position mutation
- evidence examples:
  - batch03_space_governed_lacl / BATCH03_ITEM_03 / docs/indexes/anchor_stack_manifest_v0.md / sha 93f1d8624c69
  - batch02_module_spread / BATCH02_ITEM_03 / app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_ASSET_FUNCTION_FAMILY_MAP_FROM_05_15_V0.md / sha e92fe2f9666e
  - batch03_space_governed_lacl / BATCH03_ITEM_08 / docs/reports/integrated_engine_language_amplification_harvest_v0.md / sha 56cd3704d80c

### T03_READONLY_COPY_VIEW
- definition: 검토·Codex handoff·operator reading을 위한 copy surface. 원본 대체 금지.
- modules: M5_space_inbox_review, M2_asset_graph_router
- LACL role: review surface / context copy
- move_policy: COPY_ALLOWED_SMALL_BATCH_WITH_MANIFEST_SHA
- authority_boundary: copy path must not replace original path
- evidence examples:
  - batch03_space_governed_lacl / BATCH03_ITEM_03 / docs/indexes/anchor_stack_manifest_v0.md / sha 93f1d8624c69
  - batch02_module_spread / BATCH02_ITEM_03 / app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_ASSET_FUNCTION_FAMILY_MAP_FROM_05_15_V0.md / sha e92fe2f9666e
  - batch03_space_governed_lacl / BATCH03_ITEM_08 / docs/reports/integrated_engine_language_amplification_harvest_v0.md / sha 56cd3704d80c

### T04_CONTROL_SURFACE
- definition: workspace README/MANIFEST/operator card처럼 작업 흐름을 통제하지만 authority registry는 아닌 자산.
- modules: M3_guard_precheck, M7_hygiene_operator_dashboard
- LACL role: control/guard layer
- move_policy: WORKSPACE_INTERNAL_EDIT_ALLOWED_WITH_VALIDATION
- authority_boundary: control surface != approval authority
- evidence examples:
  - batch03_space_governed_lacl / BATCH03_ITEM_02 / docs/reports/external_thought_asset_research_round_005_manual_stage_0_event_dry_run_batch_v0.md / sha 74e62e6f113f
  - batch03_space_governed_lacl / BATCH03_ITEM_04 / docs/reports/formation_layer_provisional_object_metadata_note_v0.md / sha eac37cd5e636
  - batch02_module_spread / BATCH02_ITEM_03 / app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_ASSET_FUNCTION_FAMILY_MAP_FROM_05_15_V0.md / sha e92fe2f9666e

### T05_AUTHORITY_SENSITIVE_SURFACE
- definition: authority/current-position/registry/promotion과 혼동될 수 있어 freeze/HOLD가 필요한 자산.
- modules: M4_maturation_governance
- LACL role: authority boundary layer
- move_policy: FREEZE_NO_MOVE_NO_ARCHIVE
- authority_boundary: requires explicit authority approval to mutate
- evidence examples:
  - batch03_space_governed_lacl / BATCH03_ITEM_02 / docs/reports/external_thought_asset_research_round_005_manual_stage_0_event_dry_run_batch_v0.md / sha 74e62e6f113f
  - batch02_module_spread / BATCH02_ITEM_03 / app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_ASSET_FUNCTION_FAMILY_MAP_FROM_05_15_V0.md / sha e92fe2f9666e
  - batch02_module_spread / BATCH02_ITEM_02 / app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0.md / sha 9d3fb452241a

### T06_LACL_LAYER_CARD
- definition: 논지/맥락/권위/감정/실행조건/반론/불확실성 등 층위를 읽어 구조화하는 카드형 자산.
- modules: M1_intake_provenance, M4_maturation_governance, M8_evaluation_trace_observability
- LACL role: LACL/layer classification
- move_policy: READONLY_DERIVATION_ONLY
- authority_boundary: classification candidate not source mutation
- evidence examples:
  - batch03_space_governed_lacl / BATCH03_ITEM_01 / docs/reports/external_candidate_four_source_cross_synthesis_v0.md / sha a8bf757b3b50
  - batch02_module_spread / BATCH02_ITEM_03 / app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_ASSET_FUNCTION_FAMILY_MAP_FROM_05_15_V0.md / sha e92fe2f9666e
  - batch03_space_governed_lacl / BATCH03_ITEM_02 / docs/reports/external_thought_asset_research_round_005_manual_stage_0_event_dry_run_batch_v0.md / sha 74e62e6f113f

### T07_MATURATION_EVIDENCE
- definition: 정밀 독해, risk rollup, closeout, coverage처럼 성숙 판단에 쓰는 evidence.
- modules: M4_maturation_governance, M8_evaluation_trace_observability
- LACL role: maturation evidence layer
- move_policy: EVIDENCE_ONLY_NO_PROMOTION
- authority_boundary: evidence != promotion/authority
- evidence examples:
  - batch03_space_governed_lacl / BATCH03_ITEM_02 / docs/reports/external_thought_asset_research_round_005_manual_stage_0_event_dry_run_batch_v0.md / sha 74e62e6f113f
  - batch02_module_spread / BATCH02_ITEM_03 / app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/VECTORFL_ASSET_FUNCTION_FAMILY_MAP_FROM_05_15_V0.md / sha e92fe2f9666e
  - batch03_space_governed_lacl / BATCH03_ITEM_01 / docs/reports/external_candidate_four_source_cross_synthesis_v0.md / sha a8bf757b3b50

### T08_OPERATOR_DASHBOARD_ITEM
- definition: operator가 부담/위험/다음 행동을 볼 수 있게 압축된 카드/대시보드 자산.
- modules: M7_hygiene_operator_dashboard
- LACL role: operator attention layer
- move_policy: NO_APPLY_FROM_DASHBOARD_ONLY
- authority_boundary: dashboard != apply approval
- evidence examples:
  - batch03_space_governed_lacl / BATCH03_ITEM_04 / docs/reports/formation_layer_provisional_object_metadata_note_v0.md / sha eac37cd5e636
  - batch02_module_spread / BATCH02_ITEM_07 / app/work/VECTORFL_NO_CALL_CURRENT_POSITION_PROPOSAL_FOR_REUSE_CHAIN_20260524_V0.json / sha 39d5b1f3843b
  - batch03_space_governed_lacl / BATCH03_ITEM_08 / docs/reports/integrated_engine_language_amplification_harvest_v0.md / sha 56cd3704d80c

### T09_TRACE_RECEIPT_EVIDENCE
- definition: sha, validation, rollback, receipt처럼 실행 검증과 회수를 증명하지만 authority는 아닌 자산.
- modules: M8_evaluation_trace_observability
- LACL role: trace/observability layer
- move_policy: REQUIRED_BEFORE_APPLY_BUT_NOT_APPROVAL
- authority_boundary: receipt is evidence only
- evidence examples:
  - batch02_module_spread / BATCH02_ITEM_06 / docs/reports/space_operating_organ_applied_validation_v0.md / sha 29587c6c2d48
  - batch03_space_governed_lacl / BATCH03_ITEM_01 / docs/reports/external_candidate_four_source_cross_synthesis_v0.md / sha a8bf757b3b50
  - batch03_space_governed_lacl / BATCH03_ITEM_08 / docs/reports/integrated_engine_language_amplification_harvest_v0.md / sha 56cd3704d80c

### T10_ADAPTER_SHELL
- definition: 외부 도구/내부 기능과 연결되는 adapter/bridge/shell 성격의 자산.
- modules: M6_adapter_factory
- LACL role: tool boundary/adapter layer
- move_policy: NO_LIVE_CALL_OR_API_WITHOUT_SCOPE
- authority_boundary: adapter proposal != external action approval
- evidence examples:
  - batch03_space_governed_lacl / BATCH03_ITEM_01 / docs/reports/external_candidate_four_source_cross_synthesis_v0.md / sha a8bf757b3b50
  - batch03_space_governed_lacl / BATCH03_ITEM_05 / docs/notes/git_search_deep_structure_reading_v0.md / sha 4f4069aebbc2
  - batch02_module_spread / BATCH02_ITEM_02 / app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0.md / sha 9d3fb452241a

## Return plan
- next: INTERNAL_ASSET_FIELD_CLEANUP_SPACE_GOVERNED_PASS_V0
- no move / no archive / no source edit / HOLD
