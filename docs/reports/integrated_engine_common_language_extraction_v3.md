# Integrated Engine Common Language Extraction v3

Date: 2026-04-14

## run metadata

- `run_id`: `harvest_round_3`
- `run_type`: narrow boundary clarification
- `scope`: only the five unresolved clusters carried from round_2.
- `primary_focus`: decide whether round_2 unresolved expressions become body-language, extension-language, future-layer, or remain unresolved.
- `protocol_baseline`: `docs/reports/integrated_engine_exploration_question_set_v1_1.md`
- `comparison_baselines`: `docs/reports/integrated_engine_common_language_extraction_v1.md`, `docs/reports/integrated_engine_common_language_extraction_v2.md`
- `source_priority_used`: priority 1 and 2, with priority 3 latest manifests only as runtime evidence.
- `compared_against_previous_run`: yes
- `new_language_harvest`: intentionally limited
- `stable_body_candidates_added`: 0
- `stable_extension_or_assistant_additions`: 4

## cluster 1. VectorFL surface boundary

- `raw_expression`: `VectorFL surface: reads and translates the request as intermediate formations before execution.`
- `interpreted_meaning`: current body language keeps VectorFL as the required middle reading/translation surface.
- `classification`: body-language candidate, already stable from round_1/round_2.
- `human_rewrite`: 벡터플면은 요청을 바로 실행하지 않고 line/relation/gap/pending/reflux로 읽고 번역하는 면이다.
- `source_refs`: `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:17`, `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:31`, `docs/reports/integrated_engine_common_language_extraction_v2.md:29`
- `comparison_note`: repeated across round_1 and round_2; not reopened.
- `round_3_boundary`: keep as body language.

- `raw_expression`: `VectorFL surface may become the main operating waist`
- `interpreted_meaning`: VectorFL can be a candidate coordination surface after enough language extraction and operating tests.
- `classification`: extension-language candidate, not body-language.
- `human_rewrite`: 벡터플면은 line/axis 판독과 CLI/engine return 해석이 만나는 운영 허리 후보지만, 아직 workflow hub는 아니다.
- `source_refs`: `docs/reports/integrated_engine_vectorfl_surface_elevated_direction_note_v1.md:9`, `docs/reports/integrated_engine_vectorfl_surface_elevated_direction_note_v1.md:24`, `docs/reports/integrated_engine_vectorfl_surface_elevated_direction_note_v1.md:38`
- `comparison_note`: round_2 kept this unresolved; round_3 clarifies it as extension-language, not body-language.
- `round_3_boundary`: allowed as current setup direction language only when paired with `line-first` and `not workflow hub`.

- `raw_expression`: `line-first surface` / `not team board`
- `interpreted_meaning`: operating waist must remain line-first and must not collapse into team/task routing.
- `classification`: stable extension guard / assistant-grammar.
- `human_rewrite`: 벡터플면이 운영 허리처럼 보이더라도 첫 주어는 team/worker가 아니라 line 반응이어야 한다.
- `source_refs`: `app/runtime/vectorfl_integrated_engine_shell.py:1256`, `app/runtime/vectorfl_integrated_engine_shell.py:1258`, `app/runtime/vectorfl_integrated_engine_shell.py:1291`, `docs/reports/integrated_engine_common_language_extraction_v2.md:39`
- `comparison_note`: stronger in round_2; round_3 keeps it as boundary guard.
- `round_3_boundary`: affects current setup now as wording guard.

## cluster 2. handoff / waiting / report placement

- `raw_expression`: `Handoff / Waiting / Report: operating extension layer`
- `interpreted_meaning`: handoff/waiting/report are useful operating concepts but not body skeleton.
- `classification`: extension-language candidate.
- `human_rewrite`: handoff/waiting/report는 현재 본체 3면의 핵심 골격이 아니라, 운영 흐름을 보조하는 확장 언어다.
- `source_refs`: `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:50`, `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:70`, `docs/reports/integrated_engine_exploration_question_set_v1_1.md:27`
- `comparison_note`: round_1/round_2 both avoided body promotion; round_3 confirms extension placement.
- `round_3_boundary`: do not promote to body language.

- `raw_expression`: `Where exactly do handoff/waiting/report live during low-intensity operation?`
- `interpreted_meaning`: exact UI/surface placement is still unresolved.
- `classification`: remain unresolved.
- `human_rewrite`: handoff/waiting/report를 감독 요약으로 둘지, 벡터플 흐름 가까이에 둘지는 아직 더 운영해 봐야 한다.
- `source_refs`: `docs/reports/integrated_engine_vectorfl_surface_elevated_direction_note_v1.md:101`, `docs/reports/integrated_engine_vectorfl_surface_elevated_direction_note_v1.md:102`
- `comparison_note`: round_2 carried this forward; no new body-level evidence found.
- `round_3_boundary`: current setup may show summary, but exact placement stays deferred.

## cluster 3. team / assignment / worker routing fields

- `raw_expression`: `Team Relay Board: operating extension layer` / `automatic team assignment, routing, or queue distribution`
- `interpreted_meaning`: team/assignment/routing fields are not current body skeleton.
- `classification`: extension-language candidate.
- `human_rewrite`: team, assignment, worker, routing은 현재 운용에 필요할 수 있지만 3면 본체를 설명하는 최소 언어는 아니다.
- `source_refs`: `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:52`, `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:53`, `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:59`, `docs/reports/integrated_engine_exploration_question_set_v1_1.md:27`
- `comparison_note`: round_1/round_2 both treated team/routing as extension/future-layer.
- `round_3_boundary`: keep as extension-language.

- `raw_expression`: `routing_fields_first`
- `interpreted_meaning`: supervisor UI should show team/assignee/return_slot before report prose.
- `classification`: future-layer candidate.
- `human_rewrite`: 실제 운영 UI에서는 누가 맡고 어디로 반환되는지 먼저 보이게 할 수 있지만, 이것은 body lock이 아니라 UI/운영 후보다.
- `source_refs`: `runtime/manifests/vectorfl_integrated_engine_internal_read_report_latest_v0.json:37`, `runtime/manifests/vectorfl_integrated_engine_internal_read_report_latest_v0.json:47`, `runtime/manifests/vectorfl_integrated_engine_synthesis_report_latest_v0.json:12`, `runtime/manifests/vectorfl_integrated_engine_synthesis_report_latest_v0.json:20`
- `comparison_note`: round_2 held as future-layer; round_3 confirms.
- `round_3_boundary`: current setup may reference it as future UI guidance, not body language.

- `raw_expression`: `persistent_assignment_gate_inspector`
- `interpreted_meaning`: Paperclip-style right inspector for assignment/gate state.
- `classification`: future-layer candidate / lineage-supported extension.
- `human_rewrite`: 감독자가 책임/worker/return slot/gate를 한눈에 보는 inspector는 유용하지만, 지금은 Paperclip lineage가 강한 UI 후보로 둔다.
- `source_refs`: `runtime/manifests/vectorfl_integrated_engine_internal_read_report_latest_v0.json:89`, `runtime/manifests/vectorfl_integrated_engine_internal_read_report_latest_v0.json:99`, `runtime/manifests/vectorfl_integrated_engine_synthesis_report_latest_v0.json:56`, `runtime/manifests/vectorfl_integrated_engine_synthesis_report_latest_v0.json:64`
- `comparison_note`: round_2 explicitly did not promote it; round_3 confirms future-layer placement.
- `round_3_boundary`: no current body effect.

## cluster 4. line health / current_stage / maturity relation

- `raw_expression`: `LineHealth = strong / growing / thin`
- `interpreted_meaning`: human-friendly surface readability for line thickness.
- `classification`: extension-language candidate / surface readability language.
- `human_rewrite`: line health는 line이 지금 얼마나 두껍게 보이는지 읽는 화면 언어다.
- `source_refs`: `runtime/views/vectorfl_dual_surface.tsx:55`, `runtime/views/vectorfl_dual_surface.tsx:154`, `docs/reports/integrated_engine_common_language_extraction_v2.md:41`
- `comparison_note`: round_2 treated this as useful but not stable body language; round_3 keeps it as surface language.
- `round_3_boundary`: can be used in current setup as UI wording, not final enum.

- `raw_expression`: `stage는 시간축이고, maturity는 숙성축이다.`
- `interpreted_meaning`: current_stage and maturity_level remain separate.
- `classification`: stable assistant-grammar / shared-language.
- `human_rewrite`: 지금 어느 단계인지와 얼마나 익었는지는 다르다.
- `source_refs`: `docs/reports/integrated_engine_common_language_extraction_v1.md:58`, `docs/reports/integrated_engine_common_language_extraction_v1.md:219`, `docs/reports/integrated_engine_common_language_extraction_v2.md:43`
- `comparison_note`: repeated in round_1 and round_2; round_3 confirms it as the boundary sentence.
- `round_3_boundary`: affects current setup now as interpretation rule.

- `raw_expression`: `VectorLineStage = ingress / processing / export / reflux / pending_validation`
- `interpreted_meaning`: current TSX stage strip, not final enum.
- `classification`: extension-language candidate.
- `human_rewrite`: TSX의 stage 값은 화면에서 흐름을 읽는 보조 언어이지 최종 상태 enum이 아니다.
- `source_refs`: `runtime/views/vectorfl_dual_surface.tsx:57`, `runtime/views/vectorfl_dual_surface.tsx:1256`, `runtime/views/vectorfl_dual_surface.tsx:1307`, `runtime/views/vectorfl_dual_surface.tsx:1313`
- `comparison_note`: round_2 made this explicit; round_3 confirms not body/final schema.
- `round_3_boundary`: current setup may use it as current surface language only.

## cluster 5. return artifact minimum language

- `raw_expression`: `must write a return artifact, not chat-only notes`
- `interpreted_meaning`: return must be durable enough to become next-cycle material.
- `classification`: stable assistant-grammar.
- `human_rewrite`: 내부 읽기나 worker 보고는 채팅으로 흘려보내지 말고 return artifact로 남긴다.
- `source_refs`: `app/runtime/vectorfl_integrated_engine_shell.py:2042`, `app/runtime/vectorfl_integrated_engine_shell.py:2044`, `docs/reports/integrated_engine_common_language_extraction_v2.md:51`
- `comparison_note`: stronger rewrite in round_2; round_3 confirms.
- `round_3_boundary`: affects current setup now.

- `raw_expression`: `report return is not product completion` / `Completed means a report returned.`
- `interpreted_meaning`: report returned is not implementation completed or gate closed.
- `classification`: stable assistant-grammar.
- `human_rewrite`: completed는 보고가 돌아왔다는 뜻일 수 있고, 제품 작업 완료나 gate close가 아니다.
- `source_refs`: `app/runtime/vectorfl_integrated_engine_shell.py:1860`, `app/runtime/vectorfl_integrated_engine_shell.py:2012`, `runtime/manifests/vectorfl_integrated_engine_synthesis_report_latest_v0.json:35`, `runtime/manifests/vectorfl_integrated_engine_synthesis_report_latest_v0.json:41`
- `comparison_note`: round_2 stable; round_3 confirms.
- `round_3_boundary`: affects current setup now.

- `raw_expression`: `stable / unclear / next questions / line seeds`
- `interpreted_meaning`: current report artifact grammar for internal read.
- `classification`: extension-language candidate, not final schema.
- `human_rewrite`: 내부 읽기 report는 안정된 것, 불명확한 것, 다음 질문, line seed를 나눠 남길 수 있다.
- `source_refs`: `app/runtime/vectorfl_integrated_engine_shell.py:1750`, `app/runtime/vectorfl_integrated_engine_api.py:1552`, `app/runtime/vectorfl_integrated_engine_api.py:1581`, `runtime/manifests/vectorfl_integrated_engine_internal_read_report_latest_v0.json:9`, `runtime/manifests/vectorfl_integrated_engine_internal_read_report_latest_v0.json:35`
- `comparison_note`: round_2 did not promote as final schema; round_3 keeps it as minimum operational phrasing.
- `round_3_boundary`: usable now as report grammar, not body schema.
