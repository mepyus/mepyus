# User-Facing Routing Card v0 Candidate — 2026-05-08

## 1. Verdict

USER_FACING_ROUTING_CARD_CANDIDATE_WITH_WATCH

## 2. Corrected Status

STATUS:
PACKAGE_Q_USER_FACING_ROUTING_CARD_STRUCTURED_WITH_WATCH

POSITION_VALUE:
PV_RETURN_TO_SPACE_CLOSEOUT

LACL:
CANDIDATE_OPERATING_SETTING_WITH_WATCH

## 3. Purpose

This card helps translate natural user phrases into internal VectorFL operating routes.

It is not:

- a command registry
- automation
- baseline
- final UI
- strict syntax
- tool dispatcher

It is:

- a candidate interpretation guide
- a low-friction user surface
- a routing helper
- a way to preserve Result Contract discipline without exposing internal jargon

Core sentence:

사용자는 내부 운영어를 말하지 않아도 된다.
사용자 말은 공간 목적에 따라 Codex / Gemini / Hermes / QMD / User judgment로 라우팅된다.

## 4. Routing Principles

1. User phrases are intents, not rigid commands.
2. ChatGPT/Supervisor reads the purpose first.
3. Tools are routed by task nature, not by keyword alone.
4. Hermes is only for explicit 1-5 active-surface reading/synthesis.
5. Gemini is for broad-bounded execution, testing, and larger synthesis.
6. Codex is for recovery, structure, downshift, closeout, and packet design.
7. QMD is for bounded evidence access only.
8. User remains final direction / expansion / promotion judge.
9. Expected Useful Result must be identified before external execution.
10. Safe but low-value output should not become full recovery material.

## 5. Routing Cards

### Card 1 — “이거 공간에 넣어봐”

when_to_use:

- User provides a material, result, note, or external output and wants to know how it fits into VectorFL space.

internal_meaning:

- Material Intake / Preparation for Recovery

default_route:

- Codex

assigned_role:

- Codex as structure/recovery worker

expected_useful_result:

- A downshifted candidate placement:
  - what this material is
  - where it fits
  - what value it may have
  - what should be watched
  - whether it should be recovered, held, or kept as raw trace

allowed_scope:

- one package-level result
- one external tool output
- one bounded material

do_not_do:

- do not promote to baseline
- do not modify SSOT files
- do not create automation
- do not over-document low-value material

stop_condition:

- material is too large
- no clear purpose
- no clear LACL / route / material placement
- result fails Usefulness Gate

recovery_decision_default:

- RECOVER_AS_WATCH_ITEM
- or RECOVER_AS_RETURN_TO_SPACE_VALUE if usefulness is clear

user_facing_return:

- 쓸 수 있나?
- 왜?
- 어디에 놓이나?
- 조심할 점은?
- 다음 행동은?

---

### Card 2 — “이 파일들만 보고 정리해줘”

when_to_use:

- User explicitly gives files or surfaces and wants synthesis limited to those materials.

internal_meaning:

- Bounded Active-Surface Synthesis

default_route:

- Hermes if 1-5 explicit non-sensitive files
- Gemini if more than 5 files or context is complex

assigned_role:

- Hermes as bounded active-surface carrier candidate
- Supervisor decides if Gemini is safer

expected_useful_result:

- A bounded synthesis that helps stay / go / change / hold decision.
- It must include:
  - what the selected surfaces collectively show
  - what was not inspected
  - what gap matters
  - whether the result is useful, watch, or raw trace

allowed_scope:

- 1-5 explicitly listed non-sensitive files for Hermes
- no broad search
- no secret/log/state/session files

do_not_do:

- no repo-wide reading
- no file modification
- no skill creation
- no memory/config edits
- no baseline/promotion claims

stop_condition:

- more than 5 files
- unclear surfaces
- sensitive files
- broad repo context needed
- active-surface incompleteness becomes material

recovery_decision_default:

- RECOVER_AS_RETURN_TO_SPACE_VALUE if synthesis is useful
- RAW_TRACE_ONLY if it is only summary

user_facing_return:

- 이 파일들 기준으로만 보면...
- 읽지 않은 범위는...
- 쓸 수 있는 값은...
- 조심할 점은...

---

### Card 3 — “이걸 실제로 검증해봐”

when_to_use:

- User wants execution, verification, testing, comparison, or real trial.

internal_meaning:

- Broad-Bounded Execution / Verification

default_route:

- Gemini

assigned_role:

- Gemini as execution / verification / testing worker

expected_useful_result:

- Evidence-backed finding that supports continue / hold / revise / discard.
- Must include:
  - what was actually tested
  - what passed / failed / remained uncertain
  - what should change next
  - what must not be promoted

allowed_scope:

- one broad-bounded package-level trial
- internal sessions allowed
- one package-level result only

do_not_do:

- no session-by-session relay
- no proof/validation/stable claims
- no baseline promotion
- no unauthorized mutation

stop_condition:

- task requires unsafe mutation
- scope becomes too broad
- evidence cannot be collected
- result would be generic

recovery_decision_default:

- RECOVER_AS_WATCH_ITEM
- or RECOVER_AS_RETURN_TO_SPACE_VALUE if it changes next operation

user_facing_return:

- 실제로 확인된 것
- 안 된 것
- 다음에 바꿀 것
- 조심할 점

---

### Card 4 — “이 결과 회수해줘”

when_to_use:

- User provides an external tool result and wants it brought back into VectorFL space.

internal_meaning:

- Return-to-Space Recovery

default_route:

- Codex

assigned_role:

- Codex as recovery/downshift worker

expected_useful_result:

- A recovery decision:
  - Return-to-Space Value
  - Watch Item
  - Routing Hint
  - Raw Trace Only
  - Hold
  - Discard

allowed_scope:

- one package-level result
- one external result
- one candidate material

do_not_do:

- do not recover safe-but-low-value output as full note
- do not baseline
- do not over-document
- do not trust external result as authority

stop_condition:

- result fails Usefulness Gate
- result is only pipe/shape evidence
- result lacks purpose match
- result contains unsafe/overclaiming content

recovery_decision_default:

- RECOVER_AS_RETURN_TO_SPACE_VALUE only if useful
- RAW_TRACE_ONLY if merely safe/shaped

user_facing_return:

- 회수할 값
- watch로 둘 값
- 버릴 값
- 다음 행동

---

### Card 5 — “근거만 찾아줘”

when_to_use:

- User wants exact evidence pointers, not synthesis.

internal_meaning:

- Bounded Evidence Access

default_route:

- QMD if available and explicitly needed
- Otherwise Hermes/Codex may only work from provided surfaces

assigned_role:

- QMD as bounded evidence access carrier candidate

expected_useful_result:

- Exact evidence pointers:
  - file paths
  - line numbers if available
  - short evidence label
- No broad interpretation.

allowed_scope:

- known material family
- bounded folder/surface
- 3-7 active surfaces if applicable

do_not_do:

- do not synthesize
- do not interpret broadly
- do not become memory
- do not become authority
- do not do full corpus indexing

stop_condition:

- query is too vague
- material family unknown
- full repo search required
- evidence source unclear

recovery_decision_default:

- RAW_TRACE_ONLY
- or RECOVER_AS_ROUTING_HINT if it helps next package

user_facing_return:

- 근거 위치
- 어떤 주장에 대한 근거인지
- 찾지 못한 범위

---

### Card 6 — “이제 기준으로 삼아도 돼?”

when_to_use:

- User asks whether a candidate can become a standard, baseline, or operating rule.

internal_meaning:

- Promotion / Baseline Judgment

default_route:

- User judgment with Supervisor framing

assigned_role:

- User as final judge
- ChatGPT/Supervisor as reality-check framer
- Codex only if a formal closeout is needed

expected_useful_result:

- A promotion readiness frame:
  - what supports promotion
  - what remains untested
  - what risks exist
  - recommended decision: promote / hold / continue as candidate

allowed_scope:

- one recovered candidate
- one operating rule candidate
- one closeout set

do_not_do:

- tools must not answer "yes" autonomously
- no baseline change without explicit user approval
- no Gemini/Hermes self-promotion

stop_condition:

- evidence missing
- candidate not recovered
- unclear authority
- user has not explicitly approved

recovery_decision_default:

- USER_JUDGMENT_GATE

user_facing_return:

- 기준으로 삼을 수 있는 부분
- 아직 안 되는 부분
- 승격하면 위험한 점
- 내 추천 판단

---

### Card 7 — “요약 말고 쓸 값만 뽑아줘”

when_to_use:

- User wants practical value, not summary.

internal_meaning:

- Result Usefulness Extraction

default_route:

- Codex / Supervisor

assigned_role:

- Codex if structure/recovery output is needed
- ChatGPT/Supervisor if conversational filtering is enough

expected_useful_result:

- Extract only:
  - decision value
  - action value
  - routing hint
  - watch item
  - reusable Return-to-Space candidate
- Mark low-value summary as raw trace.

allowed_scope:

- one tool output
- one draft package
- one bounded result set

do_not_do:

- no generic summaries
- no repeating slogans
- no full recovery note for low-value output
- no promotion

stop_condition:

- result is empty
- result is only safe filler
- no decision/action/recovery value exists

recovery_decision_default:

- RECOVER_AS_ROUTING_HINT
- RECOVER_AS_WATCH_ITEM
- RAW_TRACE_ONLY if no practical value

user_facing_return:

- 쓸 값
- 안 쓸 값
- 다음 행동에 반영할 값
- 그냥 기록으로 둘 값

## 6. Deferred / Ambiguous Triggers

### “다음 패키지 만들어줘”

why_deferred:

- Could mean frame only, instruction writing, or execution start.

risk:

- package proliferation
- micro-run gravitation
- premature execution

recommended_handling:

- Supervisor first decides:
  - frame only?
  - Codex instruction?
  - Gemini execution?
  - hold?

### “여기서 닫자”

why_deferred:

- Could mean stop conversation, create closeout, or preserve state.

risk:

- premature closeout without recovery
- missing Return-to-Space value

recommended_handling:

- Ask or infer whether user wants:
  - short conversation summary
  - package closeout
  - Codex recovery
  - next-chat handoff

### “이걸 보고 내가 뭘 결정해야 하는지 나오게 해줘”

why_deferred:

- High-level decision support may require broader context.

risk:

- worker claiming project authority
- over-broad synthesis
- Gemini overclaim

recommended_handling:

- Supervisor frames scope first.
- Gemini may audit if broad.
- Codex may structure if result already exists.

## 6.1 Overloaded Term Resolution — “정리해줘”

### Why this is needed

“정리해줘” is the most common and most ambiguous Korean trigger in current VectorFL use.

It can mean:

1. normal conversation summary
2. Obsidian-ready summary
3. next-chat handoff
4. package closeout
5. Codex recovery note
6. value extraction
7. simple explanation cleanup

Therefore it must not be routed by keyword alone.

### Resolution Rule

When the user says:

- “정리해줘”
- “정리해”
- “정리하자”
- “이번 채팅 정리”
- “다음 채팅으로 넘어가자”

First read the conversation position and user purpose.

### Default Interpretations

#### Case A — End of long chat / next chat handoff

If the user says:

- “채팅창 정리하고 다음으로 가자”
- “다음 채팅으로 넘어가자”
- “맥락 놓치지 않게 정리해줘”

Route:

- ChatGPT / Supervisor

Output:

- concise handoff summary
- usually in a single code block if intended for copy/paste
- include current status, role split, next step, watch items

Do not:

- create new package
- run external tools
- over-document

#### Case B — Package / result closeout

If the user provides a package result and says:

- “정리해줘”
- “회수해줘”
- “닫자”

Route:

- Codex if structured recovery/closeout is needed
- ChatGPT/Supervisor if lightweight judgment is enough

Expected Useful Result:

- recovery decision
- Return-to-Space / Watch / Raw Trace / Hold / Discard
- downshifted status
- next route

Do not:

- recover safe-but-low-value output as full note
- promote to baseline

#### Case C — Obsidian / copyable summary

If the user clearly wants a note:

- “Obsidian에 넣게 정리”
- “붙여넣기 좋게 정리”
- “정리문으로 줘”

Route:

- ChatGPT / Supervisor

Output:

- one copyable code block
- structured but not over-expanded

Do not:

- make unnecessary package
- call Codex unless project file update is needed

#### Case D — Early-stage reading / synthesis

If the user says “정리해줘” after giving files or materials at the start of a task:

Route:

- Hermes if 1-5 explicit active surfaces and bounded
- Gemini if broader / complex / verification needed
- ChatGPT/Supervisor if simple conversational summary is enough

Expected Useful Result:

- not just summary
- identify decision/action/recovery value if relevant

#### Case E — Value extraction

If the user says:

- “요약 말고 쓸 값만”
- “핵심 판단만”
- “다음 행동에 쓸 것만”

Route:

- Codex / Supervisor

Expected Useful Result:

- decision value
- action value
- routing hint
- watch item
- raw trace separation

### Clarification Rule

If unclear, ask or infer minimally:

“회수 기록으로 남길까요, 아니면 대화 요약만 할까요?”

But if context is obvious, do not ask. Use the smallest sufficient route.

### Watch Items

- Do not treat “정리해줘” as one fixed command.
- Do not automatically create packages.
- Do not overuse Codex for simple summaries.
- Do not use Hermes/Gemini unless external reading/testing adds value.
- Keep user-facing output short unless the user asks for a full handoff.

## 7. How ChatGPT / Supervisor Should Use This Card

When the user gives a trigger:

1. Read the user's actual purpose.
2. Do not route by keyword alone.
3. Check whether the trigger implies:
   - recovery
   - execution
   - explicit surface reading
   - evidence access
   - promotion judgment
   - usefulness extraction
4. Apply the smallest sufficient route.
5. Define Expected Useful Result before external execution.
6. Prevent tool overuse.
7. Keep result candidate-with-watch unless user explicitly promotes.
8. Return in user-facing language, not internal jargon.

## 8. Minimal Internal Routing Spine

- structure / recovery / downshift / closeout / packet design
  -> Codex

- broad-bounded execution / verification / testing / usefulness audit
  -> Gemini

- explicit 1-5 active-surface reading / lineage synthesis
  -> Hermes

- bounded evidence pointer access
  -> QMD

- direction / expansion / promotion
  -> User

- ambiguous route / principle alignment
  -> ChatGPT / Supervisor

## 9. Watch Items

- Trigger phrases may become rigid commands.
- User-facing language may drift into internal jargon.
- Hermes may be overused for tasks needing Gemini.
- Gemini may overclaim when asked for decision support.
- Codex may over-document low-value outputs.
- QMD may be mistaken for memory.
- Routing card may be prematurely treated as baseline.
- "정리해줘" is overloaded and must be resolved by context, not keyword alone.

## 10. Package-Level Movement Record Candidate

movement_record_type:
user_facing_routing_card_structuring

package_id:
PACKAGE_Q_USER_FACING_ROUTING_CARD_20260508

input_purpose:
Convert Package P user-facing routing trial into a candidate routing card for low-friction VectorFL operation.

activated_space_memory_or_anchors:
Package L sizing boundary; Package M Result Usefulness Gate; Package N audit; Package O Result Contract; Package P trigger map.

external_worker_role:
Codex as structure/routing-card worker.

tool_output_summary:
Codex structured seven user-facing routing cards and three deferred ambiguous triggers.

anchor_usage_trace:
The work lowered internal operating roles into user-facing Korean trigger language while preserving Expected Useful Result discipline.

evidence_or_gap:
The card is grounded in Package P but not yet tested in live use across many real user prompts.

user_decision_needed:
accept_as_candidate_with_watch

return_to_space_value:
User can speak in natural trigger phrases while the system internally routes by purpose and expected useful result.

issue_or_watch_item:
Do not treat the routing card as command registry or baseline.

future_reuse_note:
Use this card as the candidate surface for future real conversations and Package R closeout.

do_not_promote:
Candidate only; not baseline, schema, automation, or standard UI.

## 11. Final Codex Output

verdict:
USER_FACING_ROUTING_CARD_CANDIDATE_WITH_WATCH

file_created:
app/work/space-skill-sandbox/outputs/user_facing_routing_card_v0_candidate_20260508.md

key_routing_card_summary:
The card maps natural Korean user trigger phrases to internal VectorFL routes while preserving Result Contract discipline. Triggers are interpreted as intents, not rigid commands, and routing is based on user purpose, expected useful result, allowed scope, and stop conditions.

included_triggers:

- “이거 공간에 넣어봐”
- “이 파일들만 보고 정리해줘”
- “이걸 실제로 검증해봐”
- “이 결과 회수해줘”
- “근거만 찾아줘”
- “이제 기준으로 삼아도 돼?”
- “요약 말고 쓸 값만 뽑아줘”

deferred_triggers:

- “다음 패키지 만들어줘”
- “여기서 닫자”
- “이걸 보고 내가 뭘 결정해야 하는지 나오게 해줘”

routing_spine:

- Codex: structure / recovery / downshift / closeout / packet design
- Gemini: broad-bounded execution / verification / testing / usefulness audit
- Hermes: explicit 1-5 active-surface reading / lineage synthesis
- QMD: bounded evidence pointer access
- User: direction / expansion / promotion
- ChatGPT/Supervisor: ambiguous route / principle alignment

watch_items:

- trigger phrases becoming rigid commands
- user-facing language drifting into internal jargon
- Hermes overuse
- Gemini overclaim under decision support
- Codex over-documenting low-value outputs
- QMD mistaken for memory
- routing card treated as baseline
- ambiguous "정리해줘" overload

do_not_promote:

- do not promote this card
- do not create schema
- do not create registry
- do not create baseline
- do not create automation
- do not call this validated/proved/stable/standard
