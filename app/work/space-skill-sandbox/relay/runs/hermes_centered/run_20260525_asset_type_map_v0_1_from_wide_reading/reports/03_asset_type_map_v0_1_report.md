DONE: VectorFL asset type map v0.1

verdict: PASS_ASSET_TYPE_MAP_AND_ROUTE_BATCH_WITH_HOLD

sample_count: 18
type_distribution: {"index_or_map": 10, "guard_or_gate": 1, "phase_closeout": 2, "evidence_classifier": 1, "report_or_candidate": 1, "audit_or_position_check": 3}
route_distribution: {"Codex_mature": 10, "Hermes_execute_as_check_then_Codex_mature": 2, "Gemini_explore_then_Codex_mature": 6}

핵심:
- 문서를 내용보다 먼저 공간 기능으로 읽는다.
- route surface / execution gate / provenance boundary / anchor-sensitive observation / closeout residue로 분리한다.
- Hermes→Codex→Gemini 순서가 아니라, gate는 Hermes, map은 Codex, 넓은 잠재관계는 Gemini로 라우팅한다.
