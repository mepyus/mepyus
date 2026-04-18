# Integrated Engine Gemini CLI Orientation v1

Date: 2026-04-14

## purpose

This note is for Gemini CLI or any external CLI worker editing the integrated-engine surface.

Do not treat this as a new product brief, final schema, final UI spec, database model, or orchestration plan. It is an orientation note that explains what the integrated engine is, why it is being built, and how to avoid damaging the current reading while making surface changes.

## one-line reading

The integrated engine is a three-surface translation of existing VectorFL/engine internals: the user surface sets goal/scope/material context, the VectorFL surface reads intermediate formations such as line/relation/gap/pending/reflux, and the engine surface ingests/processes/validates/records trace-memory/returns; CLI/agents are optional tool layers, not the body.

## why we are building it

The goal is not just to make one UI screen.

The larger goal is to build a personal operating frame that can absorb changing goals, tools, AI models, and work domains without losing its center. The engine should help turn raw material, user intent, internal documents, external references, code work, validation, and later returns into a reusable space of lines, traces, and memory.

This requires a shared language layer:

- space language: how the accumulated material is read
- engine language: how ingest/process/validate/return are handled
- human language: how the user can understand and steer the work
- tool language: how CLI/agents can assist without replacing the body

The current work is therefore not automation-first. It is language-first and boundary-first.

## current body: three surfaces

### User surface

Body role:

- set request, goal, scope, and material context
- make the user's purpose legible before work expands
- preserve the connection between the goal and source material

Human rewrite:

- 사용자면은 무엇을 왜 어디까지 할지와 어떤 재료 위에서 시작할지를 세우는 면이다.

Guard:

- Do not turn the user surface into a task board or team-management dashboard.
- Team/assignment/handoff elements may appear as operating extensions, but they are not the body skeleton.

### VectorFL surface

Body role:

- read and translate the request before execution
- show intermediate formations: active line, relation/gap, pending/reflux traces
- keep the middle layer between user intent and engine processing

Human rewrite:

- 벡터플면은 요청을 바로 실행으로 떨어뜨리지 않고 line, relation, gap, pending, reflux로 읽고 번역하는 중간 형성체 판독면이다.

Current direction:

- VectorFL may become a `line-first operating waist candidate`, where line/axis reading, CLI contact, engine request/return interpretation, and space-change signals meet.

Guard:

- `operating waist` does not mean final workflow hub.
- Keep VectorFL `line-first`.
- Do not redesign it around team/task routing.
- Do not make it a generic workflow board.

### Engine surface

Body role:

- ingest material
- process and validate
- record trace/memory
- return output and residue as next-cycle material

Human rewrite:

- 엔진면은 재료를 받고 처리/검증한 뒤 trace/memory와 함께 반환하는 면이다.

Guard:

- Do not collapse the engine surface into result output only.
- Do not expose engine inventory so heavily that it dominates user/VectorFL surfaces.
- Runtime manifests are evidence, not permanent design specs.

## current asset boundary

Current implementation is transitional:

- `runtime/views/vectorfl_dual_surface.tsx` and `runtime/views/vectorfl_dual_surface_app/` carry the current React/Vite user surface and VectorFL surface shell.
- `/vectorfl-engine/operate` is the Python-rendered engine-facing operating shell.
- `runtime/views/vectorfl_dual_surface_app/dist/` is generated output. Do not edit it directly.
- Latest manifests under `runtime/manifests/vectorfl_integrated_engine_*_latest_v0.json` are runtime evidence, not canonical UI structure.

Do not read `/vectorfl-engine/operate` as a direct user-to-engine bypass. The current body interpretation still requires the VectorFL intermediate reading surface.

## line / axis language

Core reading:

- line is not just a card, sentence fragment, ticket, or fixed DB object.
- line is a middle operating formation between raw material and final concept.
- line gathers relation, gap, pressure, direction, trace, and possible reflux.

Human rewrite:

- line은 날것도 최종 답도 아닌 사이에서 관계, 공백, 압력, 방향을 묶는 중간 운용 형성체다.

Important distinctions:

- `current_stage` is the time/movement axis.
- `maturity_level` is the maturation axis.
- They are not the same.
- `LineHealth = strong/growing/thin` is surface readability language, not final enum.
- `VectorLineStage = ingress/processing/export/reflux/pending_validation` is current surface stage language, not final schema.

Guard:

- Do not turn TSX type values into final enums.
- Do not treat stage movement as success by itself.
- Do not treat a thin line as failure; it may be a candidate for hold, reflux, or internal reread.

## return / reflux language

Core reading:

- return is not only result text.
- return carries trace/memory/residue for the next cycle.
- report return is not product completion.
- return artifact is required when the output must feed the next loop.

Human rewrite:

- 반환은 답 한 줄이 아니라 다음 판단에 쓰일 trace/memory 재료다.
- completed는 보고가 돌아왔다는 뜻일 수 있고, 제품 작업 완료나 gate close가 아니다.
- 내부 읽기나 worker 보고는 채팅으로 흘려보내지 말고 return artifact로 남긴다.

Current operational phrasing:

- Internal-read reports may use `stable / unclear / next questions / line seeds`.
- This is current report grammar, not final return schema.

Guard:

- Do not interpret worker report completion as implementation completion.
- Do not declare gate close from a report return.
- Do not treat `stable / unclear / line_seeds` as permanent schema.

## CLI / agent role

CLI/agents are optional tool layers.

They may assist with:

- internal reading
- language harvest
- external comparison when explicitly allowed
- code edits after scoped approval
- mechanical cleanup
- report artifact generation

They must not:

- replace the three-surface body
- redefine the engine
- promote themselves into the main operating authority
- trigger broad automation by default
- convert language material into final schema

Preferred current operation:

- selective low-intensity CLI use
- internal-first before external search
- read-only/report-only unless supervisor explicitly approves implementation
- record return artifacts rather than chat-only notes

## current setup rules for surface editing

When editing the integrated-engine screen:

1. Preserve the three-surface body.
2. Keep user surface centered on goal/scope/material context.
3. Keep VectorFL surface line-first: active lines, relation/gap, ingress/reflux/pending trace.
4. Keep engine surface centered on processing, runtime evidence, validation, trace/memory, return.
5. Treat team/assignment/worker routing fields as operating extension language.
6. Treat handoff/waiting/report as operating extension language.
7. Treat persistent assignment/gate inspector as future-layer unless explicitly approved.
8. Treat latest manifests as evidence with freshness checks, not permanent truth.
9. Do not edit generated `dist/` directly.
10. Do not turn current TSX mock/type values into final schema or enums.

## strong do-not-do list

- Do not redesign the integrated engine from scratch.
- Do not make VectorFL a generic workflow hub.
- Do not make user surface a team board.
- Do not make engine surface a result-only page.
- Do not promote Team Relay Board, automatic routing, or standing worker assignment into body language.
- Do not jump to external search before internal line is shaped.
- Do not treat report returned as product complete.
- Do not treat language harvest output as final schema.
- Do not overwrite current body language with Paperclip lineage language.

## working sentence for Gemini

Use this sentence as the default interpretation while editing:

The integrated engine keeps a three-surface body: user surface sets goal/scope/material context, VectorFL surface reads line/relation/gap/pending/reflux as a line-first middle layer, and engine surface processes/validates/records trace-memory/returns; team, handoff, worker, CLI, routing, and automation are operating extensions unless explicitly relocked.

## first files to read before editing

1. `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md`
2. `docs/reports/integrated_engine_common_language_round3_boundary_report_v1.md`
3. `docs/reports/vectorfl_integrated_engine_asset_index_v0.md`
4. `runtime/views/vectorfl_dual_surface_app/README.md`
5. `runtime/views/vectorfl_dual_surface.tsx`
6. `app/runtime/vectorfl_integrated_engine_shell.py`
