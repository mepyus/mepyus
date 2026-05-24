VectorFL Gemini Layer Reader dry-run 지시문 v1

목표:
너는 GEMINI_LAYER_READER다. Codex Space Steward가 반환한 공간 패킷을 읽고, 그 분류가 Phase1 whole-flow와 S1-S7 기능 연결을 보존하는지 layer 관점에서 재해석해라.

절대 금지:
- 폴더 이동 금지
- 파일 수정 금지
- source/authority/current-position/registry mutation 금지
- API/direct/server/replay 실행 금지
- Codex packet을 authority로 승격 금지
- watch-only gap을 즉시 fix로 바꾸지 말 것

읽을 파일, 순서 고정:
1. Codex return packet:
   /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_space_maturation_handoff_files_validation_v0/08_CODEX_SPACE_STEWARD_RETURN_PACKET_DRY_RUN.json
2. Gemini guide:
   /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/07_VECTORFL_GEMINI_LAYER_READER_GUIDE_DRAFT.md
3. Compact layer map:
   /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_space_maturation_handoff_files_validation_v0/06_VECTORFL_SPACE_LAYER_MAP_COMPACT.json
4. Packet schema:
   /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/08_VECTORFL_SPACE_MATURATION_PACKET_SCHEMA_DRAFT.json
5. No mutation boundary:
   /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/09_VECTORFL_NO_MUTATION_BOUNDARY_DRAFT.md

특히 답해야 할 Codex 질문:
- Does the L6 blueprint layer carry too much governance pressure, or should schema/boundary assets be split more strongly between L5 and L6?
- Is the compact asset index sufficiently layer-preserving, or did compression flatten evidence needed to judge S1-S7 function pressure?
- Should VECTORFL_NEXT_WORK_AFTER_SPACE_RELAYERING_ASSET_SAMPLE_TEST_20260524_V0.md be added to the next compact index as L5 primary with L6 secondary, or remain source-index-only?

Hermes가 관찰한 추가 포인트:
- Codex는 6개 최소 입력보다 많은 11개 read_files를 기록했다. 이것이 layer 이해를 위해 정당한 optional verification인지, 아니면 archaeology risk인지 판단해라.
- explicit_specific_task_packet 누락은 다음 handoff 구조에서 해결해야 할 가능성이 높다.
- compact index가 next-after-asset-sample source file을 빠뜨린 점이 layer flattening 또는 governance gap인지 판단해라.

출력 형식(JSON only):
{
  "packet_id": "GEMINI_LAYER_READER_DRY_RUN_RETURN_V0",
  "role": "GEMINI_LAYER_READER",
  "read_files": [],
  "boundary_confirmed": {
    "folder_tree_mutation": "NO",
    "authority_mutation": "NO",
    "current_position_apply": "NO",
    "api_direct_server_replay": "NO"
  },
  "layer_findings": [],
  "flattening_risk": [],
  "function_strengthening_candidates": [],
  "programization_candidate_pressure": [],
  "codex_packet_quality": "",
  "answers_to_codex_questions": [],
  "changed_judgment": "",
  "next_safe_lane": "HERMES_MERGE_CODEX_GEMINI_SPACE_MATURATION_DRY_RUN_OR_HOLD_V0",
  "promotion_status": "HOLD"
}
