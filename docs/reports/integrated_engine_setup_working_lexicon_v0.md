# Codex Handoff - Integrated Engine Setup Language / Working Lexicon v0

Date: 2026-04-14

## 0. purpose

This document is not for locking the integrated engine further.

It is a handoff for using the current three-surface structure and language-harvest results without mixing:

- body language
- extension-layer language
- future-layer language

Current stage:

- Do not lock final schema / final enum / canonical state machine.
- Use stable body language as provisional working language.
- Keep unresolved / extension / future-layer language separated.
- Move through setup -> CLI attachment -> low-intensity operating test -> correction -> repeated runs -> later lock.

## 1. top-level baseline

### three surfaces are the body

- User surface = the surface that sets request, goal, and scope.
- VectorFL surface = the surface that reads, organizes, and translates the request.
- Engine surface = the surface that processes, executes, outputs, and returns.

### tool layer is not the body

- CLI/agents do not replace the body.
- When needed, they support team division, external research, auxiliary execution, or mechanical cleanup as optional tool layers.

### current direction

- User surface becomes clearer as supervision / organization / purpose surface.
- VectorFL surface becomes clearer as the operating waist and main work surface.
- Engine surface becomes clearer as the processing / return / trace-memory organ.

## 2. locked language-harvest baseline

### protocol baseline

- `docs/reports/integrated_engine_exploration_question_set_v1_1.md`
- Treat this as the reusable `language harvest protocol baseline`.

### harvest history

- `docs/reports/integrated_engine_common_language_extraction_v1.md` = `harvest_round_1`
- `docs/reports/integrated_engine_common_language_extraction_v2.md` = `harvest_round_2`
- `docs/reports/integrated_engine_common_language_extraction_v3.md` = `harvest_round_3`
- `docs/reports/integrated_engine_common_language_round3_boundary_report_v1.md` = round_3 boundary clarification
- `docs/reports/integrated_engine_common_language_unresolved_round3_v1.md` = round_3 unresolved/future-layer carry-forward

### current judgment

- Round_2 produced stable candidates.
- Round_3 clarified unresolved / extension / future-layer boundaries.
- The next move is not to keep polishing documents indefinitely.
- The next move is to use stable body language as provisional working language and move into setup / low-intensity operation tests.

## 3. Working Lexicon v0 - body language usable now

### 3.1 three-surface body language

#### User surface

Definition:

- The starting surface that sets request, goal, scope, and material context.

Human rewrite:

- 무엇을 왜 어디까지 할지, 어떤 재료 위에서 시작할지를 정하는 면.

#### VectorFL surface

Definition:

- The surface that does not drop a request directly into execution.
- It first reads and translates the request as intermediate formations.

Human rewrite:

- line, relation, gap, pending, reflux 같은 형태로 먼저 읽고 정리하는 면.

#### Engine surface

Definition:

- The surface that ingests material, processes, validates, leaves trace/memory, and returns.

Human rewrite:

- 처리하고 결과와 흔적을 함께 돌려주는 본체 기관.

## 3.2 current asset boundary language

### React/Vite app = user surface / VectorFL surface shell

The current React/Vite app is the user-surface / VectorFL-surface shell.

Primary files:

- `runtime/views/vectorfl_dual_surface.tsx`
- `runtime/views/vectorfl_dual_surface_app/`

### Python route = engine surface

`/vectorfl-engine/operate` is the engine-facing operating shell.

Primary files:

- `app/runtime/vectorfl_integrated_engine_shell.py`
- `app/runtime/vectorfl_integrated_engine_api.py`
- `app/core/runtime/viewer_server.py`

### UI shell is not runtime evidence

What appears on screen is not automatically current truth.

Execution evidence must be checked through runtime/latest manifests and the freshness gate.

## 3.3 line / axis body language

### line

Definition:

- A line is a middle operating formation between raw material and final output.

Human rewrite:

- 아직 최종 답은 아니지만 관계, 공백, 압력, 방향을 묶어 다음 작업을 유발하는 중간 단위.

### line-first

Definition:

- VectorFL surface reads line reactions before team-board or task-routing structure.

Human rewrite:

- 벡터플면은 team board보다 먼저 line 반응을 읽는 곳이다.

### relation / gap / reflux

Definition:

- A line includes not only what is connected but also weak points, gaps, and material likely to return.

Human rewrite:

- gap과 reflux는 실패가 아니라 판독 재료다.

### stage != maturity

Definition:

- `stage` = time/movement axis.
- `maturity` = maturation axis.

Human rewrite:

- 지금 어느 단계에 와 있는가와 얼마나 익었는가는 다른 문제다.

## 3.4 return / reflux body language

### return is not only result text

Definition:

- Return is next-cycle material with trace and memory.

Human rewrite:

- 답 한 줄이 아니라 다음 순환에 다시 먹일 판단 흔적이다.

### report return != product completion

Definition:

- A report being returned does not mean product work is complete.

Human rewrite:

- 보고가 돌아왔다는 것과 제품 작업이 끝났다는 것은 다르다.

### return artifact, not chat-only notes

Definition:

- Return must remain as a reusable artifact, not evaporate as chat-only notes.

Human rewrite:

- 반환은 채팅 메모처럼 흘리면 안 되고, 다시 읽고 재사용할 수 있는 artifact로 남아야 한다.

## 3.5 assistant / operation input grammar

### Do not mix the body and the tool layer

- The three surfaces are the body.
- CLI/agent/automation is the optional tool layer.

### latest completed != current truth

- Latest execution record is not automatically current proof.
- Check whether object / draft / worker belongs to the current chain through the freshness gate.

### record / draft / execute / gate close are different strengths

- Recording does not mean executing.
- Executing does not mean locking.
- Report return does not mean gate close.

### internal line shaping first

- External search is attached only after internal line is shaped enough.

## 4. Do not put these into current body language

### extension-language

These may be useful in setup/operation, but are not body language now:

- `handoff / waiting / report`
- `team / assignment / worker routing fields`
- `LineHealth = strong/growing/thin`
- `VectorLineStage = ingress/processing/export/reflux/pending_validation`
- `stable / unclear / next questions / line seeds`

### future-layer

These are future-layer candidates:

- `persistent_assignment_gate_inspector`
- `routing_fields_first`
- `packet_to_gate_sequence`
- automatic routing / queue distribution
- standing worker assignment

Do not treat these as current setup requirements unless explicitly approved later.

## 5. unresolved after round_3

Keep these open for setup/low-intensity tests:

- VectorFL surface workflow capacity
- exact placement of handoff / waiting / report
- maturity display
- return artifact minimum fields

Current judgment:

- These are better answered through setup and low-intensity operating tests than by more document reading right now.

## 6. what Codex should do now

Do:

1. Use this Working Lexicon v0 as current setup body language.
2. Align user / VectorFL / engine surface wording to this language.
3. Keep CLI as optional tool layer, not body.
4. Keep VectorFL as line-first intermediate reading/translation surface.
5. Prepare setup and low-intensity operating tests.
6. Keep test-only unresolved items deferred instead of locking them through more wording.

Do not:

- lock final schema
- lock final enum
- lock DB model
- promote workflow hub into body
- place team routing / auto assignment into the body
- mistake extension-language for body-language
- treat future-layer as current setup demand

## 7. setup one-line sentence group

### three surfaces

- User surface is the start surface that sets request / goal / scope and material context.
- VectorFL surface is the line-first intermediate formation reading / organizing / translation surface.
- Engine surface is the body organ that performs ingest / process / validate / trace-memory / return.

### line / axis

- A line is a middle operating formation, neither raw nor final.
- relation / gap / reflux are not failures; they are line-reading material.
- current stage and maturity must be read separately.

### return / reflux

- Return is not only result text; it is next material with trace/memory.
- Report return and product completion are different.
- Return must remain as an artifact, not chat-only notes.

### assistant / operation

- Do not mix the three-surface body with the tool layer.
- Check freshness before treating latest completed as current truth.
- Do not treat record / draft / execution / gate close as the same strength.
- Attach external search only after internal line shaping.

## 8. next sequence

1. Use Working Lexicon v0 to clean up surface wording, setup wording, and CLI placement wording.
2. Proceed with integrated-engine setup.
3. Attach CLI for low-intensity operating tests.
4. Re-check unresolved items after tests:
   - VectorFL workflow capacity
   - handoff / waiting / report placement
   - maturity display
   - return artifact minimum language
5. Lock only what survives actual operation.

## 9. final one-line

Use stable body language as provisional working language now, keep extension-language / future-layer / unresolved separate, and move into integrated-engine setup plus low-intensity CLI operation tests.
