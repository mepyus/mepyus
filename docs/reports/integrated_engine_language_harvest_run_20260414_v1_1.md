# Integrated Engine Language Harvest Run 20260414 v1.1

Date: 2026-04-14

## run metadata

- `run_id`: `integrated_engine_language_harvest_20260414_v1_1`
- `date`: `2026-04-14`
- `scope`: priority 1 current reading/language documents plus priority 2 current user/VectorFL React surface and Python engine surface code.
- `primary_focus`: compare `harvest_round_1` against current priority 1/2 assets, add source priority / freshness / overlap fields, and extract stronger operating language for surface boundaries, line reading, return artifacts, and assistant input grammar.
- `source_priority_used`: priority 1 and 2. Priority 3 was used only through the current freshness logic and latest-manifest boundary language in priority 2. Priority 4 was not reopened in this run because `integrated_engine_common_language_extraction_v1.md` already captured the first lineage harvest.
- `compared_against_previous_run`: yes. Comparison baseline is `docs/reports/integrated_engine_common_language_extraction_v1.md`.
- `new_expressions_found`: React/Vite shell is user/VectorFL surface, not Python engine surface; engine surface remains Python-rendered; real operating execution belongs to engine runtime and latest manifests; VectorFL surface is `line-first surface`; this face is not an operating panel; team/worker are provenance only; return must be artifact, not chat-only notes; completed history is not necessarily current execution.
- `stronger_rewrites_found`: the VectorFL surface may rise as operating waist, but current shell wording still protects the body reading by saying it is not an operating panel; CLI/session settings record context and role before execution; report return is not product completion.
- `stable_candidates_promoted`: 8
- `unresolved_carried_forward`: workflow-hub boundary, handoff/waiting/report placement, CLI control placement, TSX type values vs final schema, runtime manifest freshness gate details, team-role UI as extension layer.

## extracted dataset

Fields: `raw_expression`, `interpreted_meaning`, `bucket_or_grammar_type`, `related_surface`, `related_line_or_axis`, `human_rewrite`, `why_useful_now`, `unresolved`, `source_refs`, `repetition_signal`, `source_priority`, `freshness_note`, `overlap_with_previous_run`

### Track A. three-surface language

| raw_expression | interpreted_meaning | bucket_or_grammar_type | related_surface | related_line_or_axis | human_rewrite | why_useful_now | unresolved | source_refs | repetition_signal | source_priority | freshness_note | overlap_with_previous_run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `User surface: sets request, goal, scope, and material context.` | 사용자면의 본체는 요청/목적/범위/재료 문맥이다. | A / three-surface | 사용자면 | goal / scope / material context | 사용자면은 무엇을 왜 어디까지 할지와 어떤 재료 위에서 할지를 세우는 면이다. | 사용자면이 team board로 납작해지는 것을 막는 기준 문장이다. | 팀/담당 배치는 현재 확장층으로 유지한다. | `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:16`, `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:22` | high | priority 1 | current lock 문서. | yes |
| `VectorFL surface: reads and translates the request as intermediate formations before execution.` | 벡터플면은 실행 전 중간 형성체 판독/번역 면이다. | A / three-surface | 벡터플면 | line / relation / gap / pending / reflux | 요청을 바로 실행하지 않고 line, relation, gap, pending으로 읽고 번역하는 면이다. | 사용자면과 엔진면의 직접 연결을 막는 핵심 문장이다. | 운영 허리 방향과 workflow hub 확정 사이 경계는 보류. | `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:17`, `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:31` | high | priority 1 | current lock 문서. | yes |
| `Engine surface: ingests, processes, validates, records trace/memory, and returns output.` | 엔진면은 처리와 반환뿐 아니라 trace/memory를 포함한다. | A / three-surface | 엔진면 | ingest / process / validate / trace / memory / return | 엔진면은 재료를 받고 처리/검증한 뒤 흔적과 기억을 남겨 반환하는 면이다. | 엔진면을 단순 결과 생성기로 축소하지 않게 한다. | 실제 실행 freshness는 runtime evidence로 별도 확인해야 한다. | `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:18`, `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:24` | high | priority 1 | current lock 문서. | yes |
| `This is the current React/Vite program shell for the VectorFL user surface and VectorFL surface. It is not the Python engine surface.` | 현재 React 앱과 Python 엔진면의 소유 경계를 분명히 한다. | A / boundary | 사용자면 / 벡터플면 / 엔진면 | surface ownership | React 앱은 사용자면/벡터플면 shell이고, Python 쪽이 엔진면이다. | 현재 자산 지도를 셋업 언어에 붙이는 가장 직접적인 코드 근거다. | React의 팀/역할 mock 값은 final schema가 아니다. | `runtime/views/vectorfl_dual_surface_app/README.md:5`, `runtime/views/vectorfl_dual_surface_app/README.md:7`, `runtime/views/vectorfl_dual_surface_app/README.md:11`, `runtime/views/vectorfl_dual_surface_app/README.md:13` | high | priority 2 | current app README. | new |
| `The engine surface remains Python-rendered. Real operating execution still belongs to the engine runtime and latest manifests, not this app alone.` | 화면 shell과 실제 실행 증거를 분리한다. | A / boundary | 엔진면 / runtime evidence | execution / manifests | 엔진면은 Python으로 남고, 실제 실행 여부는 앱 화면만이 아니라 runtime/latest manifest까지 봐야 한다. | generated/test surface를 canonical truth로 오인하지 않게 한다. | priority 3 manifest 자체는 이번에 깊게 재검증하지 않았다. | `runtime/views/vectorfl_dual_surface_app/README.md:107`, `runtime/views/vectorfl_dual_surface_app/README.md:109`, `runtime/views/vectorfl_dual_surface_app/README.md:110` | high | priority 2 | current app README; runtime evidence requires separate freshness gate. | new |
| `The integrated engine sets goal and scope ... uses that return as material for the next cycle.` | 3면 전체 순환 압축문. | A / cycle | cross-surface | return as next material | 목적과 범위를 세우고, 중간 형성체를 읽고, 처리/검증/기억/반환한 뒤, 그 반환을 다음 판독 재료로 삼는다. | 최소 공통 언어 초안의 순환 문장으로 바로 쓸 수 있다. | 자동 reingest 공식은 아직 잠그지 않는다. | `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:34`, `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:46` | high | priority 1 | current lock 문서. | yes |

### Track B. line / axis language

| raw_expression | interpreted_meaning | bucket_or_grammar_type | related_surface | related_line_or_axis | human_rewrite | why_useful_now | unresolved | source_refs | repetition_signal | source_priority | freshness_note | overlap_with_previous_run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `line, relation, gap, genealogy, export/reflux` | 현재 VectorFL surface가 읽는 핵심 중간 표면 언어. | B / line-axis | 벡터플면 | line / relation / gap / genealogy / export / reflux | 벡터플면은 팀/worker보다 먼저 라인, 연결, 빈칸, 계보, 내보냄과 되돌아옴을 읽는다. | priority 2 코드가 harvest_round_1의 line/relation/gap/reflux 언어를 강화한다. | genealogy가 최소 공통 언어에 계속 들어갈지는 보류. | `app/runtime/vectorfl_integrated_engine_shell.py:1255`, `app/runtime/vectorfl_integrated_engine_shell.py:1256`, `app/runtime/vectorfl_integrated_engine_shell.py:1260` | high | priority 2 | current Python shell wording. | yes |
| `line-first surface` / `not team board` | 벡터플면은 팀 보드보다 line 반응을 먼저 읽는 면이다. | B / surface emphasis | 벡터플면 | line-first | 벡터플면은 담당자 보드가 아니라 먼저 공간 표면의 라인 반응을 읽는 곳이다. | 벡터플면을 workflow board로 오해하지 않게 하는 강한 UI 언어다. | 운영 허리 후보와 `not team board` 사이 장력은 future-layer로 남김. | `app/runtime/vectorfl_integrated_engine_shell.py:1256`, `app/runtime/vectorfl_integrated_engine_shell.py:1258`, `app/runtime/vectorfl_integrated_engine_shell.py:1291` | high | priority 2 | current Python shell wording. | stronger |
| `weak points / gaps` / `expected reflux` | line inspector가 결핍과 환류 예상을 함께 보여준다. | B / relation-gap-reflux | 벡터플면 | gap / reflux | 라인은 강한 연결만이 아니라 약한 지점과 돌아올 재료까지 함께 읽는다. | gap/reflux를 line의 일부로 다루는 실무 화면 언어다. | weak point와 blocker의 차이는 계속 unresolved. | `app/runtime/vectorfl_integrated_engine_shell.py:1308`, `app/runtime/vectorfl_integrated_engine_shell.py:1318` | high | priority 2 | current Python shell wording. | yes |
| `LineHealth = "strong" | "growing" | "thin"` | line은 단순 존재/부재가 아니라 두께/성장/얇음으로 읽힌다. | B / line-axis | 벡터플면 | line health | 라인은 있는지 없는지만 보는 게 아니라 지금 두꺼운지, 자라는지, 얇은지 본다. | line이 왜 중요한지 사람 언어로 설명하기 좋다. | `LineHealth`는 TSX mock/type 언어이며 final enum이 아니다. | `runtime/views/vectorfl_dual_surface.tsx:55`, `runtime/views/vectorfl_dual_surface.tsx:154` | medium | priority 2 | current TSX source; not schema lock. | new |
| `VectorLineStage = "ingress" | "processing" | "export" | "reflux" | "pending_validation"` | line stage 후보가 실제 화면 코드에 있다. | B / stage | 벡터플면 | current_stage / reflux / pending_validation | 라인이 들어오고, 처리되고, 내보내지고, 되돌아오고, 검증 대기하는 흐름으로 읽힐 수 있다. | stage 언어를 화면 seed와 harvest_round_1 사이에 연결한다. | final enum 금지. maturity_level과의 분리는 아직 이 코드에서 보이지 않는다. | `runtime/views/vectorfl_dual_surface.tsx:57`, `docs/reports/integrated_engine_common_language_extraction_v1.md:58` | medium | priority 2 + priority 1 | TSX source plus previous harvest; not final schema. | stronger |
| `stage는 시간축이고, maturity는 숙성축이다. 둘은 같이 움직일 수 있지만 동일하지 않다.` | stage/maturity 분리의 핵심 문장. | B / axis | 벡터플면 | current_stage / maturity_level | 지금 어느 단계인지와 얼마나 익었는지는 다르다. | TSX의 stage 후보값을 final maturity 판단으로 오해하지 않게 한다. | maturity 표현의 current surface 위치는 더 탐색 필요. | `docs/reports/integrated_engine_common_language_extraction_v1.md:58`, `runtime/views/vectorfl_dual_surface.tsx:57` | high | priority 1 + priority 2 | harvest_round_1 stable; code only partially supports stage. | yes |

### Track C. return / reflux language

| raw_expression | interpreted_meaning | bucket_or_grammar_type | related_surface | related_line_or_axis | human_rewrite | why_useful_now | unresolved | source_refs | repetition_signal | source_priority | freshness_note | overlap_with_previous_run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `Return comes back with trace and memory, not only result text.` | 반환은 텍스트 결과가 아니라 trace/memory 포함 패킷이다. | C / return | 엔진면 / cross-surface | return / trace / memory | 돌아오는 것은 답 한 줄이 아니라 판단 흔적과 기억을 포함한 다음 재료다. | 반환/환류 공통 언어의 가장 안정적인 문장이다. | return packet schema는 확정하지 않는다. | `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:41`, `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:42` | high | priority 1 | current lock 문서. | yes |
| `얇은 라인을 사용자면 지시 또는 내부 탐색으로 되돌린다` | 약한 line은 실패가 아니라 보강/환류 대상으로 돌아간다. | C / reflux | 벡터플면 | thin line / reflux / internal read | 얇은 라인은 버리는 게 아니라 사용자 지시나 내부 탐색으로 되돌려 더 두껍게 만든다. | gap/reflux를 운영 문장으로 바꾸는 좋은 표현이다. | 자동 재지시/자동 routing은 잠그지 않는다. | `app/runtime/vectorfl_integrated_engine_shell.py:1277`, `app/runtime/vectorfl_integrated_engine_shell.py:1280` | high | priority 2 | current Python shell wording. | stronger |
| `report return is not product completion` | 보고 반환과 제품 완료를 분리한다. | C / return judgment | 엔진면 / 도구층 | report return / gate | 보고가 돌아왔다는 것은 제품 구현이 끝났다는 뜻이 아니다. | CLI 결과를 gate close로 오해하지 않게 하는 즉시 사용 문장이다. | 제품 완료 판정 조건은 별도 gate가 필요하다. | `app/runtime/vectorfl_integrated_engine_shell.py:1855`, `app/runtime/vectorfl_integrated_engine_shell.py:1860`, `app/runtime/vectorfl_integrated_engine_api.py:2071` | high | priority 2 | current shell/API guardrail. | new |
| `must write a return artifact, not chat-only notes` | 반환은 채팅 메모가 아니라 재사용 가능한 artifact여야 한다. | C / return artifact | 엔진면 / 도구층 | return artifact / trace | 내부 읽기나 작업자 보고는 채팅으로 흘려보내지 말고 반환 artifact로 남겨야 한다. | CLI/assistant 산출이 공간 재료로 남는 기준을 준다. | artifact 최소 필드는 아직 final schema가 아니다. | `app/runtime/vectorfl_integrated_engine_shell.py:2042`, `app/runtime/vectorfl_integrated_engine_shell.py:2044` | high | priority 2 | current Python shell wording. | new |
| `stable / unclear / next questions / line seeds` | 내부 읽기 반환을 stable/unclear/question/seed로 나눈다. | C / internal-read return | 벡터플면 / 엔진면 | stable / unclear / line_seed | 내부 탐색 결과는 안정된 것, 불명확한 것, 다음 질문, 라인 씨앗으로 나눠 보고한다. | return을 단순 요약이 아니라 다음 cycle 재료로 구조화한다. | outputs는 current operating language이지 final schema가 아니다. | `app/runtime/vectorfl_integrated_engine_shell.py:1750`, `app/runtime/vectorfl_integrated_engine_shell.py:1773`, `app/runtime/vectorfl_integrated_engine_api.py:211`, `app/runtime/vectorfl_integrated_engine_api.py:217` | high | priority 2 | current shell/API wording. | stronger |

### Track D. assistant input grammar

| raw_expression | interpreted_meaning | bucket_or_grammar_type | related_surface | related_line_or_axis | human_rewrite | why_useful_now | unresolved | source_refs | repetition_signal | source_priority | freshness_note | overlap_with_previous_run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `Do not mix the body three-surface structure with the optional tool layer.` | 본체와 도구층 경계를 섞지 말라는 입력 문법. | D / boundary grammar | 본체 / 도구층 | CLI / agent boundary | 3면 본체와 CLI/agent 도구층을 같은 층으로 섞지 않는다. | assistant가 팀/CLI/automation을 본체로 승격하지 않게 한다. | 운영 허리 후보에서 CLI control을 어디까지 표면에 둘지는 unresolved. | `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md:88`, `docs/reports/integrated_engine_vectorfl_surface_elevated_direction_note_v1.md:44`, `docs/reports/integrated_engine_vectorfl_surface_elevated_direction_note_v1.md:48` | high | priority 1 | current lock + direction note. | yes |
| `The next correct move is not more locking.` / `Locking is not the starting point.` | 현재 단계는 잠금이 아니라 언어 적립/반복 운용이다. | D / stage grammar | 운영층 | language harvest / later lock | 지금 할 일은 더 잠그는 게 아니라 언어를 수확하고 반복해 본 뒤 나중에 잠그는 것이다. | v1.1을 language harvest protocol로 읽게 한다. | 잠금 재개 조건은 추후 운영 반복 뒤 판단. | `docs/reports/integrated_engine_vectorfl_surface_elevated_direction_note_v1.md:50`, `docs/reports/integrated_engine_vectorfl_surface_elevated_direction_note_v1.md:69`, `docs/reports/integrated_engine_exploration_question_set_v1_1.md:19` | high | priority 1 | direction note + current protocol. | yes |
| `Return conservative posture for whether the latest execution proves the current draft.` | latest 실행도 현재 draft를 증명하는지 보수적으로 봐야 한다. | D / freshness grammar | 엔진면 / runtime evidence | freshness / execution proof | latest가 있다고 바로 현재 실행 증거로 보지 말고 object/draft/worker가 맞는지 확인한다. | v1.1의 freshness_note 필드를 실제 코드 기준과 연결한다. | priority 3 manifest deep-read는 다음 실행에서 보강. | `app/runtime/vectorfl_integrated_engine_shell.py:33`, `app/runtime/vectorfl_integrated_engine_shell.py:39`, `app/runtime/vectorfl_integrated_engine_shell.py:56`, `app/runtime/vectorfl_integrated_engine_shell.py:67` | high | priority 2 | current Python freshness function. | new |
| `이 슬롯은 Gemini를 실행하지 않습니다.` / `records config only` | CLI 설정은 실행이 아니라 맥락/역할 기록일 수 있다. | D / tool boundary | 도구층 / 벡터플면 후보 | CLI session | CLI 슬롯은 모델/역할/스크립트 후보를 기록할 뿐, 그 자체가 실행 권위는 아니다. | 선택 호출형 저강도 운용과 잘 맞는다. | VectorFL surface에 붙일지 별도 도구층으로 둘지는 unresolved. | `app/runtime/vectorfl_integrated_engine_shell.py:1453`, `app/runtime/vectorfl_integrated_engine_shell.py:1456`, `app/runtime/vectorfl_integrated_engine_shell.py:1458`, `app/runtime/vectorfl_integrated_engine_shell.py:1497`, `app/runtime/vectorfl_integrated_engine_shell.py:1501` | high | priority 2 | current Python shell wording. | new |
| `do not jump to external search before internal line is shaped` | 외부 리서치 전 내부 line 형성이 먼저다. | D / purpose-boundary grammar | 벡터플면 / 도구층 | internal-first / external search | 내부 line이 잡히기 전에는 외부 검색으로 점프하지 않는다. | 외부 리서치를 선택적 도구층으로 유지하게 한다. | 외부 검색 개시 조건은 추가 evidence 필요. | `app/runtime/vectorfl_integrated_engine_shell.py:1437`, `app/runtime/vectorfl_integrated_engine_shell.py:1441`, `app/runtime/vectorfl_integrated_engine_shell.py:1745`, `app/runtime/vectorfl_integrated_engine_shell.py:1750`, `app/runtime/vectorfl_integrated_engine_shell.py:1791` | high | priority 2 | current shell workflow guardrail. | stronger |
| `Split user and VectorFL surface data into explicit view models only after the UI role boundary is stable.` | view model 분리는 UI 역할 경계가 안정된 뒤에 한다. | D / judgment grammar | 사용자면 / 벡터플면 | view model / role boundary | user/VectorFL 데이터를 나누는 모델화는 역할 경계가 안정된 뒤에 한다. | final schema/model 조기 잠금을 막는다. | explicit view model 전환 조건은 추후 UI 안정화 뒤 판단. | `runtime/views/vectorfl_dual_surface_app/README.md:112`, `runtime/views/vectorfl_dual_surface_app/README.md:116` | high | priority 2 | current app README. | new |

## short synthesis report

### repeated core expressions

- `goal / scope / material context` remains the user-surface body language.
- `intermediate formations`, `line / relation / gap / pending / reflux` remain the VectorFL-surface body language.
- `ingest / process / validate / trace-memory / return` remains the engine-surface body language.
- Priority 2 adds a stronger implementation boundary: React/Vite carries user/VectorFL surfaces, while the Python shell remains the engine surface.
- Priority 2 also strengthens return language: report return is not product completion, and return must become artifact rather than chat-only notes.
- Freshness is now a first-class assistant grammar: latest execution needs current object/draft/worker match before it proves the current run.

### setup sentences usable now

- 사용자면은 목적, 범위, 재료 문맥을 세우는 시작면이다.
- 벡터플면은 사용자 목적이 바로 실행으로 떨어지기 전 line, relation, gap, pending, reflux를 읽고 번역하는 중간 형성체 판독면이다.
- 엔진면은 ingest, process, validate를 수행하고 trace/memory와 함께 return을 남기는 처리/환류면이다.
- React/Vite 앱은 현재 사용자면/벡터플면 shell이고, Python `/vectorfl-engine/operate`는 engine-facing surface다.
- 실제 실행 증거는 화면 문구만이 아니라 runtime/latest manifest와 freshness gate까지 함께 봐야 한다.
- 작업자/CLI return은 제품 완료가 아니라 다음 판단을 위한 report artifact다.

### assistant input grammar candidates

- 이번 표현은 사용자면 / 벡터플면 / 엔진면 / 도구층 중 어디에 속하는가?
- 이 산출은 language material인가, current lock인가, future-layer candidate인가?
- 이 latest 실행은 current object, draft fingerprint, worker가 맞는 current run인가?
- 이 CLI 슬롯은 실행인가, 설정/역할 기록인가, report return인가?
- 이 line은 strong / growing / thin 중 무엇으로 보이며, 그 판단이 maturity와 같은 뜻으로 오해되고 있지 않은가?
- 외부 검색 전에 내부 line이 충분히 shaped 되었는가?

### not to lock yet

- VectorFL surface를 final workflow manager로 확정하는 표현.
- Team/assignment/worker UI를 본체 골격으로 승격하는 표현.
- TSX의 `LineHealth`, `VectorLineStage`, team/role union 값을 final enum으로 쓰는 것.
- `stable / unclear / next_questions / line_seeds`를 final return schema로 고정하는 것.
- Gemini/Codex model/session controls를 본체 실행 권위로 읽는 것.
- Latest manifest 이름만으로 current proof를 인정하는 것.

### additional blanks

- VectorFL surface가 운영 허리로 올라갈 때 `not operating panel` 기준과 어떻게 공존하는가.
- handoff / waiting / report가 low-intensity operation에서 어느 표면에 어느 강도로 보이는가.
- `line health`와 `maturity_level`의 차이를 현재 surface에 어떻게 표시할 것인가.
- freshness gate를 runtime manifest 자체와 연결한 다음 실행의 priority 3 deep-read.
- return artifact 최소 필드와 trace/memory field의 경계.

## stable candidates

| stable_candidate | reason |
|---|---|
| 사용자면 = goal / scope / material context start surface | current lock, asset index, previous harvest가 모두 반복한다. 팀/담당을 본체로 승격하지 않는 데 직접 유용하다. |
| 벡터플면 = intermediate-formation reading / translation surface | current lock, previous harvest, current shell line-first wording이 서로 강화한다. |
| 엔진면 = ingest / process / validate / trace-memory / return surface | current lock과 app README의 Python engine boundary가 함께 지지한다. |
| React/Vite app = user/VectorFL shell, Python shell = engine surface | priority 2 README와 asset index가 현재 구현 경계를 직접 말한다. |
| VectorFL surface = line-first, not team board | current shell에서 `line-first surface`, `not team board`, line/relation/gap/export/reflux가 반복된다. |
| report return is not product completion | current shell/API guardrail이며 CLI/worker 결과를 gate close로 오해하지 않게 한다. |
| return artifact, not chat-only notes | current shell command slot 문구이며 환류/trace/memory 언어와 직접 연결된다. |
| freshness gate before treating latest as current truth | `_current_run_freshness` 코드가 object/draft/worker match를 요구한다. v1.1 `freshness_note` 필드와 직접 연결된다. |

## unresolved / future-layer list

### hold as unresolved

- VectorFL surface operating waist: 방향 후보는 강하지만 final workflow hub로 잠그면 안 된다.
- handoff / waiting / report: current code에 존재하지만 body skeleton으로 승격하지 않는다.
- CLI model/version controls: VectorFL surface 가까이에 두는 방향은 강하지만, 본체 실행 권위로 읽지 않는다.
- line health vs maturity_level: health는 TSX에 있고 maturity는 harvest language에 강하나 둘의 관계는 더 봐야 한다.
- return artifact minimum fields: stable/unclear/next_questions/line_seeds는 현재 운영어이지 final schema가 아니다.

### future-layer candidate

- internal operations team as language-harvest maintainer.
- VectorFL surface as selective low-intensity CLI coordination waist.
- explicit user/VectorFL view-model split after UI role boundary stabilizes.

### lineage-only / contrast material for this run

- full workflow hub language.
- automatic routing / queue distribution.
- standing multi-agent team operation.
- broad external research automation.

### additional evidence needed

- priority 3 latest manifests should be deep-read in the next run to test freshness language against actual current runtime records.
- priority 4 lineage reports should be reopened only when comparing whether a repeated expression survived into current priority 1/2 assets.
