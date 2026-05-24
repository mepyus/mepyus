# VectorFL Memory & Record Hygiene Rule v0 — 2026-05-08

## 1. Verdict

MEMORY_RECORD_HYGIENE_RULE_CANDIDATE_WITH_WATCH

## 2. Status

STATUS:
VECTORFL_MEMORY_RECORD_HYGIENE_RULE_CANDIDATE_WITH_WATCH

POSITION_VALUE:
PV_RETURN_TO_SPACE_CLOSEOUT

LACL:
CANDIDATE_OPERATING_SETTING_WITH_WATCH

## 3. Problem

Small session-level memories fill the assistant memory too quickly.

The system should not preserve every package/session detail as durable memory.

The durable memory layer should preserve only what changes future judgment, routing, result quality, or user-facing response behavior.

## 4. Core Rule

Do not remember every run.

Remember only reusable operating judgment.

Short form:

기억은 로그 저장소가 아니라, 다음 판단을 바꾸는 압축 운영 상태다.

## 5. What To Preserve In Memory

Preserve:

1. current closeout-level operating state
2. core operating sentence
3. role boundaries
4. user-facing routing triggers
5. Result Usefulness Gate
6. Mission Packet Result Contract
7. durable stop criteria
8. durable user response preferences
9. changed routing rules
10. changed promotion / baseline / candidate rules

## 6. What Not To Preserve In Memory

Do not preserve as long-term memory:

1. every small session result
2. every package file path
3. repeated evidence lists
4. repeated do_not_promote clauses
5. detailed run logs
6. temporary trial outputs
7. per-session execution trace
8. redundant "completed successfully" messages
9. safe but low-value outputs
10. raw trace that does not change future judgment

These should remain in project files / RUNLOG / raw traces, not assistant memory.

## 7. Memory Compression Rule

When a sequence reaches closeout:

Compress:

- many small package details
- into one closeout-level operating memory

Pattern:

Before compression:
Package H detail
Package I detail
Package J detail
Package K detail
Package L detail
Package M detail
...

After compression:
Current operating state
Core principle
Role split
Reusable routing rules
Stop criteria
Next-use rules

## 8. Memory Save Gate

Before saving to assistant memory, ask:

1. Will this change future answers?
2. Will this change routing?
3. Will this change how Codex / Gemini / Hermes / QMD are used?
4. Will this change how the user wants responses?
5. Is this a closeout-level rule rather than a run-level event?
6. Can this be compressed into an existing operating memory?

If no, do not save.

## 9. Record Location Rule

Use different storage layers:

### Assistant Memory

Use for:

- durable operating principles
- user preferences
- role boundaries
- response behavior
- current compressed state

Do not use for:

- detailed logs
- package outputs
- evidence lists
- every generated file

### Project Files

Use for:

- recovery notes
- closeout notes
- candidate rules
- routing cards
- result contracts

### RUNLOG

Use for:

- concise execution trace
- file created / modified
- reason for action

### Raw Trace

Use for:

- low-value safe outputs
- tool stdout
- temporary evidence
- material not worth Return-to-Space recovery

## 10. Response Behavior Rule

When the user says "계속" or "next":

Do not automatically create another package.

First identify:

1. Is this execution?
2. Is this recovery?
3. Is this structure?
4. Is this actual-use routing?
5. Is this memory hygiene?
6. Is this user judgment?

Then choose the smallest sufficient route.

## 11. Result-Oriented Memory Rule

Do not remember that a tool "worked."

Remember what that changes.

Example:

Do not store:
"Hermes successfully read 5 files."

Store:
"Hermes is candidate-bounded to 1-5 explicit active surfaces only; use for small lineage synthesis, not broad repo reading."

Do not store:
"Package N completed."

Store:
"Result Usefulness Gate separates safe/shape-compliant output from actually useful Return-to-Space material."

## 12. Watch Items

- Over-compression may lose useful lineage.
- Under-compression fills memory.
- Repeated package details should remain in project files, not assistant memory.
- User may still need next-chat handoff summaries.
- Closeout-level memories should be updated, not duplicated.
- Avoid saving temporary excitement or one-off results.
- Avoid deleting current operating principles.

## 13. User-Facing Memory Policy

When memory is full or getting noisy, use this policy:

1. Compress to current closeout state.
2. Keep operating principles.
3. Keep role routing.
4. Keep response preferences.
5. Drop session-level detail.
6. Refer to project files for exact history.

User-facing explanation:

"세부 로그는 프로젝트 파일에 두고, 나는 다음 판단에 필요한 운영 원칙만 기억한다."

## 14. Package-Level Movement Record Candidate

movement_record_type:
memory_record_hygiene_structuring

package_id:
VECTORFL_MEMORY_RECORD_HYGIENE_RULE_20260508

input_purpose:
Prevent assistant memory bloat by defining what VectorFL should preserve as durable memory versus project record or raw trace.

activated_space_memory_or_anchors:
Package R result-oriented operating stack closeout; Result Usefulness Gate; Mission Packet Result Contract; user-facing routing card; memory compression request.

external_worker_role:
Codex as structure/closeout worker.

tool_output_summary:
Codex created a candidate memory and record hygiene rule to preserve closeout-level operating principles while avoiding session-level memory bloat.

anchor_usage_trace:
The task applied the Result Usefulness principle to memory itself: remember only what changes future judgment.

evidence_or_gap:
Rule is structurally defined but not yet stress-tested across multiple future conversations.

user_decision_needed:
accept_as_candidate_with_watch

return_to_space_value:
VectorFL memory should preserve compressed operating state, not detailed package logs.

issue_or_watch_item:
Do not over-compress away useful lineage.

future_reuse_note:
Use this rule whenever memory fills or after major closeouts.

do_not_promote:
Candidate hygiene rule only; not baseline or automation.

## 15. Final Codex Output

verdict:
MEMORY_RECORD_HYGIENE_RULE_CANDIDATE_WITH_WATCH

file_created:
app/work/space-skill-sandbox/outputs/vectorfl_memory_record_hygiene_rule_20260508_v0.md

core_memory_rule:
기억은 로그 저장소가 아니라, 다음 판단을 바꾸는 압축 운영 상태다.

what_to_preserve:

- closeout-level operating state
- core operating sentence
- role boundaries
- user-facing routing triggers
- Result Usefulness Gate
- Mission Packet Result Contract
- durable stop criteria
- durable user response preferences
- changed routing rules
- changed promotion / baseline / candidate rules

what_not_to_preserve:

- small session results
- every package file path
- repeated evidence lists
- repeated do_not_promote clauses
- detailed run logs
- temporary trial outputs
- per-session execution trace
- redundant completion messages
- safe but low-value outputs
- raw trace that does not change future judgment

memory_save_gate:
Save only if it changes future answers, routing, tool role use, user response behavior, or closeout-level operating state, and cannot be compressed into existing memory.

record_location_rule:
Assistant Memory stores durable operating principles and current compressed state. Project files store recovery/closeout/rules/cards/contracts. RUNLOG stores concise execution trace. Raw trace stores low-value safe outputs and temporary evidence.

watch_items:

- over-compression
- under-compression
- losing useful lineage
- duplicating closeout memories
- saving one-off results
- deleting current operating principles

do_not_promote:

- do not promote this rule
- do not create schema
- do not create registry
- do not create baseline
- do not create automation
- do not call this validated/proved/stable/standard
