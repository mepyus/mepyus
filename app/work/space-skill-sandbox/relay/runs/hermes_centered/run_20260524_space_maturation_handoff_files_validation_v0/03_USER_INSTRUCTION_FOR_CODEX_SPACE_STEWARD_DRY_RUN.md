VectorFL 공간 담당 Codex dry-run 지시문

목표:
너는 CODEX_SPACE_STEWARD다. Hermes가 만든 공간 숙성 handoff 파일을 읽고, 실제 폴더 이동 없이 공간 자산의 primary layer / secondary links / 재투입 위치를 검토해라.

절대 금지:
- 폴더 이동 금지
- 파일 수정 금지
- source/authority/current-position/registry mutation 금지
- API/direct/server/replay 실행 금지
- 후보/제안/receipt를 authority로 승격 금지
- 네트워크/패키지 설치 금지

읽을 파일, 순서 고정:
1. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/03_VECTORFL_CURRENT_SPACE_HANDOFF_DRAFT.md
2. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/09_VECTORFL_NO_MUTATION_BOUNDARY_DRAFT.md
3. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/06_VECTORFL_CODEX_SPACE_STEWARD_GUIDE_DRAFT.md
4. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_space_maturation_handoff_files_validation_v0/06_VECTORFL_SPACE_LAYER_MAP_COMPACT.json
5. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_space_maturation_handoff_files_validation_v0/07_VECTORFL_ASSET_INDEX_COMPACT.json
6. /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/08_VECTORFL_SPACE_MATURATION_PACKET_SCHEMA_DRAFT.json

해야 할 일:
1. 위 6개 파일만 먼저 읽어라.
2. 현재 위치와 금지 경계를 요약해라.
3. asset index의 각 항목이 primary_layer + secondary_links를 갖는지 확인해라.
4. multi-layer 자산이 단일 폴더 이동으로 손실될 위험이 있는지 판단해라.
5. referenced_material / reinserted_material 구분이 충분한지 평가해라.
6. Gemini에게 넘길 질문 3~5개를 만들어라.
7. 아래 JSON 형태로만 결과를 작성해라.

출력 형식:
{
  "packet_id": "CODEX_SPACE_STEWARD_DRY_RUN_RETURN_V0",
  "role": "CODEX_SPACE_STEWARD",
  "read_files": [],
  "boundary_confirmed": {
    "folder_tree_mutation": "NO",
    "authority_mutation": "NO",
    "current_position_apply": "NO",
    "api_direct_server_replay": "NO"
  },
  "referenced_material_findings": [],
  "reinserted_material_findings": [],
  "primary_layer_assignments_review": [],
  "secondary_links_review": [],
  "spatial_risks": [],
  "missing_material": [],
  "changed_judgment": "",
  "gemini_questions": [],
  "next_safe_lane": "GEMINI_LAYER_READER_DRY_RUN_FROM_CODEX_PACKET_OR_HOLD_V0",
  "promotion_status": "HOLD"
}

검토만 하고 수정하지 마라.

참고: full draft는 필요할 때만 열고, 첫 pass는 compact layer/index로 처리해라.
