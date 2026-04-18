# Integrated Engine Common Language Stable Additions Round3 v1

Date: 2026-04-14

Round_3 adds no new stable body-language items.

It adds only boundary-stable extension/assistant grammar.

## stable additions

### 1. line-first operating waist candidate

- `belongs_to`: extension-language / assistant-grammar
- `raw_expression`: `VectorFL surface may become the main operating waist` + `line-first surface` + `not team board`
- `human_rewrite`: 벡터플면은 운영 허리 후보로 읽을 수 있지만, 현재 setup에서는 반드시 line-first이고 workflow hub가 아니다.
- `reason_for_promotion`: This clarifies the round_2 unresolved boundary without promoting workflow hub. It is backed by the direction note and current shell wording.
- `source_refs`: `docs/reports/integrated_engine_vectorfl_surface_elevated_direction_note_v1.md:24`, `docs/reports/integrated_engine_vectorfl_surface_elevated_direction_note_v1.md:38`, `app/runtime/vectorfl_integrated_engine_shell.py:1258`, `app/runtime/vectorfl_integrated_engine_shell.py:1291`
- `current_setup_effect`: use as wording guard now.

### 2. handoff/waiting/report as extension-language

- `belongs_to`: extension-language
- `raw_expression`: `Handoff / Waiting / Report: operating extension layer`
- `human_rewrite`: handoff/waiting/report는 본체 골격이 아니라 운영 흐름을 요약하고 연결하는 확장 언어다.
- `reason_for_promotion`: The current lock explicitly classifies it as extension layer, and round_3 found no contrary body-level evidence.
- `source_refs`: `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:69`, `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:70`, `docs/reports/integrated_engine_exploration_question_set_v1_1.md:27`
- `current_setup_effect`: use it in operating summaries, not body definitions.

### 3. health/stage/maturity separation

- `belongs_to`: assistant-grammar
- `raw_expression`: `LineHealth = strong/growing/thin`, `VectorLineStage = ingress/processing/export/reflux/pending_validation`, `stage는 시간축이고 maturity는 숙성축이다`
- `human_rewrite`: health는 line 두께의 화면 언어, current_stage는 흐름의 시간축, maturity는 숙성 판단이다.
- `reason_for_promotion`: Round_1 and round_2 already stabilized stage/maturity separation; round_3 clarifies TSX health/stage as surface language only.
- `source_refs`: `docs/reports/integrated_engine_common_language_extraction_v1.md:58`, `docs/reports/integrated_engine_common_language_extraction_v1.md:219`, `runtime/views/vectorfl_dual_surface.tsx:55`, `runtime/views/vectorfl_dual_surface.tsx:57`, `runtime/views/vectorfl_dual_surface.tsx:1256`
- `current_setup_effect`: use this as an interpretation guard now.

### 4. minimum return artifact phrasing

- `belongs_to`: assistant-grammar / extension-language
- `raw_expression`: `must write a return artifact, not chat-only notes`; `report return is not product completion`; `stable / unclear / next questions / line seeds`
- `human_rewrite`: 반환은 채팅 메모가 아니라 다음 순환에 쓰일 artifact여야 하며, 보고가 돌아온 것은 제품 완료가 아니다. 내부 읽기 report는 stable/unclear/next questions/line seeds로 나눠 남길 수 있다.
- `reason_for_promotion`: Round_2 had strong shell/API evidence; round_3 confirms it as minimum operational phrasing while still rejecting final schema promotion.
- `source_refs`: `app/runtime/vectorfl_integrated_engine_shell.py:2044`, `app/runtime/vectorfl_integrated_engine_shell.py:1860`, `runtime/manifests/vectorfl_integrated_engine_synthesis_report_latest_v0.json:41`, `app/runtime/vectorfl_integrated_engine_api.py:1552`, `app/runtime/vectorfl_integrated_engine_api.py:1581`
- `current_setup_effect`: use now for assistant/CLI report interpretation.
