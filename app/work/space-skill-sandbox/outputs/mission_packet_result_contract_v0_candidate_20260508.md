# Mission Packet Result Contract v0 Candidate — 2026-05-08

## 1. Verdict

MISSION_PACKET_RESULT_CONTRACT_CANDIDATE_WITH_WATCH

## 2. Corrected Status

STATUS:
PACKAGE_O_RESULT_CONTRACT_PATCH_STRUCTURED_WITH_WATCH

POSITION_VALUE:
PV_RETURN_TO_SPACE_CLOSEOUT

LACL:
CANDIDATE_OPERATING_SETTING_WITH_WATCH

## 3. Problem Statement

Previous mission packets were strong on:

- hard boundaries
- do_not_promote
- no broad search
- no memory/config/skill edits
- Worker Return Intake shape
- not_inspected_scope

But weak on:

- what decision the result should support
- what action the result should enable
- what would count as concrete value
- what would be too generic
- what should become Return-to-Space
- what should remain raw trace only

Core correction:

A mission packet should not only define safe behavior. It should define useful output.

## 4. Result Contract Definition

Result Contract is a mission packet section that tells the worker what kind of result would be useful for the user's current purpose.

It answers:

- What decision should this result help with?
- What action should this result enable?
- What concrete findings are expected?
- What would be too generic?
- What should be returned as watch?
- What should be raw trace only?
- What should not be promoted?

It is not:

- a scoring system
- a schema
- a baseline
- an automation
- a replacement for user judgment

It is:

- a practical output-quality contract
- a guard against safe-but-useless output
- a bridge between Mission Packet and Result Usefulness Gate

## 5. Result Contract Placement

Add this section to future mission packets after Purpose and before Task.

Recommended placement:

1. Role
2. Purpose
3. Active Surfaces / Target
4. Boundaries
5. Expected Useful Result
6. Task
7. Return Shape
8. Do Not Promote

## 6. Generic Result Contract Template

Add:

```markdown
## Expected Useful Result

This result is useful only if it helps with:

decision_to_support:
- [what the user needs to decide]

action_to_enable:
- [what the next instruction / operation should be able to do]

concrete_outputs_required:
- [specific finding 1]
- [specific finding 2]
- [specific finding 3]

watch_outputs_required:
- [risk / gap / uncertainty to expose]

raw_trace_only_if:
- [condition where result is only a trace]

hold_if:
- [condition where output should stop and request rework]

too_generic_if:
- repeats operating slogans without task-specific findings
- summarizes surfaces without connecting them to the current decision
- says "candidate" but provides no usable judgment
- only says constraints were obeyed
- produces volume without decision value

do_not_promote:
- this result is not proof, validation, standard, baseline, or integration completion
```

## 7. Hermes Variant

Hermes Result Contract should be small and bounded.

Use when:

- 1-5 explicit active surfaces
- no-write
- no-memory
- no-skill
- no-config
- one-shot `hermes -z`
- Worker Return Intake return

Hermes should produce:

- concise synthesis across explicit surfaces
- what changed in current state understanding
- what gap/watch item matters
- what next routing hint exists, if any
- what remains not inspected
- why result is candidate-only

Hermes should not produce:

- broad strategic judgment
- baseline decision
- promotion recommendation
- full repo interpretation
- generic summary only
- follow-on execution plan unless asked

Example Hermes Expected Useful Result:

```markdown
decision_to_support:
- Should these active surfaces be recovered as useful lineage synthesis, or only kept as raw trace/watch?

action_to_enable:
- Decide whether to route next step to Codex recovery, Gemini broad execution, or stop.

concrete_outputs_required:
- one synthesis of what the selected surfaces collectively show
- one specific gap that affects the current decision
- one routing hint
- one reason this should not be promoted

too_generic_if:
- it only summarizes each file separately
- it only says "everything remains candidate"
- it does not identify any decision or next-use value
```

## 8. Gemini Variant

Gemini Result Contract should support broader execution/testing.

Use when:

- task requires verification
- task requires comparison
- task requires multi-session internal reasoning
- task requires real target trial
- task requires broader synthesis than Hermes should handle

Gemini should produce:

- actual execution/test findings
- comparison of alternatives
- failure cases
- concrete decision support
- reusable lessons
- what to change in next packet or route

Gemini should not produce:

- proof/validation/stable claims
- baseline declarations
- generic high-confidence summaries
- session-by-session relay output
- self-promotion of its own result

Example Gemini Expected Useful Result:

```markdown
decision_to_support:
- Should the current operating pattern be reused, revised, held, or discarded?

action_to_enable:
- Produce concrete changes for the next mission packet or routing rule.

concrete_outputs_required:
- evidence-backed finding
- failed/weak part
- recommended route change
- one watch item
- one do-not-promote warning

too_generic_if:
- it only says the protocol worked
- it does not identify what should change
- it does not separate evidence from inference
- it does not help decide next action
```

## 9. Codex Recovery Variant

Codex should use Result Contract during recovery.

Codex should ask:

- Did the worker answer the expected useful result?
- Which part is actual value?
- Which part is watch?
- Which part is raw trace?
- Did the result change routing, packet design, or operating limit?
- Should a recovery note be created, or is a short log enough?

Codex should not:

- recover every safe output
- create recovery notes for raw trace only
- turn every useful observation into baseline
- over-document small results

## 10. Recovery Decision Mapping

If useful output is strong:

- RECOVER_AS_RETURN_TO_SPACE_VALUE

If useful but risky:

- RECOVER_AS_WATCH_ITEM

If mainly helps route future tasks:

- RECOVER_AS_ROUTING_HINT

If safe and shaped but low-value:

- RAW_TRACE_ONLY

If too vague or misses purpose:

- HOLD_FOR_REWORK

If unsafe or misleading:

- DISCARD

## 11. Weak vs Improved Mission Packet Examples

### Weak Example 1

Read these files and summarize.

Problem:

- no decision target
- no action target
- encourages generic summary

Improved:

Read these three active surfaces and synthesize what they collectively imply for the next routing decision.
Return:
1. one decision-relevant synthesis,
2. one gap that matters,
3. one routing hint,
4. one not-inspected limitation,
5. one do-not-promote warning.

### Weak Example 2

Check whether this worked.

Problem:

- unclear success criteria
- invites self-congratulation

Improved:

Evaluate whether this result should be recovered, watched, held, or discarded.
Use:

- purpose match
- concrete output
- decision value
- action value
- space value

Return the recovery decision and reason.

### Weak Example 3

Verify the protocol.

Problem:

- invites validation/proof language

Improved:

Test one bounded case and identify:
1. what was observed,
2. what remains untested,
3. whether the result changes the next instruction,
4. why this does not prove the protocol.

## 12. Package N Lessons Embedded

- A result that only proves the carrier is behaving is a log, not memory.
- Usefulness is highest when the carrier connects active surfaces into decision-enabling synthesis.
- Expected Useful Result must be part of the contract.
- Summary volume is not the same as decision value.
- Synthesis must not become authority.
- Codex should not recover safe but low-value outputs as full notes.

## 13. User-Facing Simplification

User does not need to say "Result Contract."

User can say:

- "이걸 보고 내가 뭘 결정해야 하는지 나오게 해줘."
- "요약 말고 다음 행동에 쓸 값만 뽑아줘."
- "이 파일들을 보고 지금 멈출지 계속할지 판단할 수 있게 정리해줘."
- "쓸 수 있는 값과 그냥 기록으로 둘 값을 나눠줘."
- "공간에 넣을 값만 골라줘."

Internal interpretation:
Use Result Contract.

## 14. Watch Items

- Contract could become too verbose.
- Workers may fill contract fields mechanically.
- "Decision value" can drift into authority claim.
- Hermes should not be asked for broad strategic decisions.
- Gemini may overclaim if decision language is too strong.
- Codex may over-document low-value outputs.
- User purpose must remain primary.

## Context Budget / Progressive Loading Check — Candidate

This check asks:

```text
What is the smallest sufficient context this mission should start with?
```

evidence_type:
USER_PROVIDED_SUMMARY / GEMINI_TRIAL_EVIDENCE. A saved Trial 013 file was not found in the narrow check for this patch.

Trial 013 showed that "Lazy Loading Context" supports VectorFL's progressive lens loading rule, but the external source is not VectorFL authority.

### Candidate Use

Use this check when drafting a mission packet for:

- Gemini-heavy analysis
- Codex-light setup
- Hermes bounded reading
- QMD evidence retrieval
- external reference translation
- active-bundle trials

### Starting Context

A mission packet should name the initial active surfaces.

Prefer:

- 2-3 high-signal anchors for ordinary judgment tasks
- 4-file asset bundle when provenance/capsule/policy mutation is needed
- 5-file calibration bundle when tool behavior is the question
- 6-file routing bundle only when user trigger/routing drift is the question
- bounded RUNLOG slice only when causality is the question

### Neighbor Request Rule

The worker should not silently broaden context.

If current context is insufficient, the worker must state:

```text
missing_layer:
why_current_context_is_insufficient:
requested_neighbor:
expected_useful_result_from_neighbor:
```

Only one neighbor should be requested at a time unless the user explicitly approves broader reading.

### Not Mandatory Schema

- this is not a required schema field
- this is not a routing authority
- this is not an automatic file selector
- this is not a reason to under-context a task
- if the task genuinely needs broader context, mark the need rather than forcing a small bundle

### Context Budget Watch

- under-context from too-small initial bundle
- over-context from loading all lenses
- worker requesting wrong neighbor
- context budget becoming rigid schema
- "lazy loading" becoming excuse for shallow reading
- user judgment bypassed

This addendum is a mission-packet drafting check only.

It should be tested in 1-2 real packets before becoming a recurring field.

## 15. Package-Level Movement Record Candidate

movement_record_type:
mission_packet_result_contract_patch

package_id:
PACKAGE_O_MISSION_PACKET_RESULT_CONTRACT_PATCH_20260508

input_purpose:
Patch future mission packets so external workers produce useful decision/action/recovery value, not only safe and well-shaped output.

activated_space_memory_or_anchors:
Package M Result Usefulness Gate; Package N Usefulness Audit; Package L Hermes sizing boundary; Worker Return Intake; Return-to-Space; CANDIDATE_OPERATING_SETTING_WITH_WATCH.

external_worker_role:
Codex as structure/contract patch worker.

tool_output_summary:
Codex structured the Result Contract candidate and embedded it into Hermes, Gemini, and Codex recovery variants.

anchor_usage_trace:
The task shifted mission packet design from boundary/shape-only to useful-result-oriented output.

evidence_or_gap:
Contract is structurally defined but not yet tested on a new real task. Package P should trial it.

user_decision_needed:
accept_as_candidate_with_watch

return_to_space_value:
Future mission packets should specify Expected Useful Result to prevent safe but useless output.

issue_or_watch_item:
Keep the contract lightweight and do not turn it into schema/automation.

future_reuse_note:
Use in Package P Real Result Contract Trial.

do_not_promote:
Candidate patch only; not baseline, schema, standard, or automation.

## 16. Next Package Frame

Prepare Package P frame only. Do not execute it.

PACKAGE_P_REAL_RESULT_CONTRACT_TRIAL

Purpose:
Use the Result Contract on one real task and test whether the worker returns decision/action/recovery value, not just safe formatted output.

Owner:
Gemini execution, Codex later recovery.

## 17. Final Codex Output

verdict:
MISSION_PACKET_RESULT_CONTRACT_CANDIDATE_WITH_WATCH

file_created:
app/work/space-skill-sandbox/outputs/mission_packet_result_contract_v0_candidate_20260508.md

key_contract_summary:
Future Mission Packets should specify Expected Useful Result before execution. The contract tells the worker what decision the result should support, what action it should enable, what concrete outputs are required, what is too generic, and what should become watch, raw trace, hold, discard, or Return-to-Space material.

hermes_variant_summary:
Hermes should receive small bounded Result Contracts for 1-5 explicit active surfaces, no-write/no-memory/no-skill/no-config, one-shot `hermes -z`, and Worker Return Intake return. It should synthesize explicit surfaces into decision-useful lineage or routing value, not broad strategic judgment.

gemini_variant_summary:
Gemini Result Contracts should support broader execution/testing, evidence-backed findings, weak/failure cases, route changes, watch items, and do-not-promote warnings without proof/validation/stable claims.

codex_recovery_variant_summary:
Codex uses the contract to decide what is actual value, watch, raw trace, routing hint, hold, or discard, and should avoid full recovery notes for safe but low-value outputs.

weak_vs_improved_example_summary:
Replace "Read X and summarize" with "Synthesize X to enable decision Y." Replace "Check whether this worked" with recovery-decision criteria. Replace "Verify the protocol" with bounded observation, untested scope, next-instruction impact, and do-not-prove framing.

package_p_frame_prepared:
yes, as a future real Result Contract trial only; not executed

watch_items:

- contract verbosity
- mechanical field filling
- decision value drifting into authority claim
- Hermes broad-strategy overreach
- Gemini overclaim under decision language
- Codex over-documenting low-value outputs
- user purpose drift

do_not_promote:

- do not promote this contract
- do not create schema
- do not create registry
- do not create baseline
- do not create automation
- do not call this validated/proved/stable/standard
