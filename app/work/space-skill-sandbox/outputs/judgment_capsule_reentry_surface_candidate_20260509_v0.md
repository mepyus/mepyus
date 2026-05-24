# Judgment Capsule & Re-entry Surface Candidate — 2026-05-09

## 0. Status

- candidate only
- live-use with watch
- not baseline
- not schema
- not registry
- not wiki system
- not automation
- not final memory structure
- not replacement for user judgment

## 1. Purpose

This document defines a minimal candidate shape for judgment capsules and user re-entry surfaces.

It exists to prevent the small file trap: small files can reduce token cost, but they can also kill context if they lose parent context, neighbor context, provenance, return placement, user language, and watch conditions.

The goal is to turn recovered judgment into reusable, low-token surfaces without turning those surfaces into final truth, wiki authority, registry, or automation.

## 2. Judgment Capsule Definition

A judgment capsule is a compact, reusable judgment unit recovered from trace, package, session, or tool output after usefulness and provenance review.

It is not:

- raw trace
- full summary
- final truth
- baseline
- memory by default
- standalone authority

## 3. Minimal Judgment Capsule Fields

Use this compact candidate template when a recovered judgment needs to be reused without rereading the full source.

```text
capsule_id:
title:
judgment:
layer:
source_trace_or_package:
provenance:
parent_context:
neighbor_context:
use_when:
do_not_use_when:
return_placement:
watch:
linked_policy_mutation:
linked_tool_profile:
user_reentry_phrase:
```

Keep it minimal. This is a candidate shape, not a schema.

## 4. User Re-entry Surface Definition

A user re-entry surface is a human-readable entry point that lets the user later remember why a judgment mattered and how to reuse it.

It is not:

- machine-only index
- polished encyclopedia page
- final wiki
- registry
- static truth

## 5. Minimal Re-entry Surface Fields

Use this compact candidate template when a future user or worker needs to reopen a judgment area.

```text
surface_id:
user_facing_title:
why_this_mattered:
when_to_reopen:
what_to_read_first:
related_capsules:
related_trace:
current_status:
watch:
next_possible_action:
```

Keep it simple and readable.

## 6. Parent / Neighbor Context Rule

Candidate rule:

No capsule should be treated as reusable unless it names:

- parent context
- mandatory neighbor context
- provenance
- return placement
- do-not-use condition

This is candidate with watch, not baseline.

The point is not to create a heavy wiki system. The point is to keep small surfaces from becoming contextless fragments.

## 7. Trace-to-Capsule Transition

Candidate transition:

```text
Raw Trace
-> Micro-Run Trace Record
-> Boundary / Shape / Usefulness Check
-> Provenance Tagging
-> Judgment Capsule or Watch
-> Re-entry Surface / Active Bundle
-> Policy Mutation if future behavior changes
```

User judgment remains required at recovery, expansion, and promotion points.

The transition should not imply that every trace becomes a capsule. Many traces should remain Raw Trace Only or Watch.

## 8. Sample Capsule A — Package R Core Sentence

```text
capsule_id:
JC_PACKAGE_R_CORE_SENTENCE_20260509_A

title:
Result-Oriented Recovery Core Sentence

judgment:
공간은 원칙을 지킨 결과가 아니라, 쓸 수 있는 판단을 회수한다.

layer:
result-oriented operating stack / recovery principle / live-use candidate with watch

source_trace_or_package:
- app/work/space-skill-sandbox/outputs/result_oriented_operating_stack_closeout_20260508_v0.md
- current_anchor_map_candidate_20260509_v0.md as first-read reference

provenance:
OBSERVED_FILE_EVIDENCE when Package R file is read; USER_LONG_TERM_CONTEXT for repeated user direction; CHATGPT_SUPERVISOR_INFERENCE for application to future routing.

parent_context:
Package M-Q result-oriented sequence; Package R closeout.

neighbor_context:
- result_usefulness_gate_v0_candidate_20260508.md
- mission_packet_result_contract_v0_candidate_20260508.md
- user_facing_routing_card_v0_candidate_20260508.md
- policy_mutation_record_candidate_20260509_v0.md

use_when:
Use when deciding whether an external result should be recovered, watched, held, discarded, or kept as raw trace.

do_not_use_when:
Do not use as proof that any tool result is useful. Do not use to bypass file observation, provenance review, LACL placement, or user judgment.

return_placement:
RETURN_TO_SPACE_VALUE_WITH_WATCH

watch:
This sentence can become slogan-like if repeated without concrete recovery decision.

linked_policy_mutation:
PMR_RESULT_CONTRACT_SHIFT_20260509_A

linked_tool_profile:
ChatGPT/Supervisor for routing; Codex for recovery; Gemini for broad audit; Hermes/QMD only within their bounded roles.

user_reentry_phrase:
요약 말고 쓸 값만 뽑아줘.
```

## 9. Sample Re-entry Surface A — Result-Oriented Stack

```text
surface_id:
URS_RESULT_ORIENTED_STACK_20260509_A

user_facing_title:
결과 중심 운영 스택을 다시 열어야 할 때

why_this_mattered:
This surface helps reopen the current operating stack without rereading every Package M-Q note. It reminds future workers that safe/shape-compliant output is not enough; recovered material must help a user decision, action, route, watch, or stop condition.

when_to_reopen:
- when routing a new user request
- when deciding whether a tool result should be recovered
- when writing a mission packet
- when a result is safe but possibly low-value
- when a worker starts explaining instead of observing

what_to_read_first:
- current_anchor_map_candidate_20260509_v0.md
- result_oriented_operating_stack_closeout_20260508_v0.md
- result_usefulness_gate_v0_candidate_20260508.md
- mission_packet_result_contract_v0_candidate_20260508.md
- user_facing_routing_card_v0_candidate_20260508.md

related_capsules:
- JC_PACKAGE_R_CORE_SENTENCE_20260509_A

related_trace:
- Package M-Q sequence as represented by Package R closeout
- policy_mutation_record_candidate_20260509_v0.md

current_status:
live-use candidate with watch

watch:
Do not treat this surface as wiki homepage, baseline, registry, or final operating manual. Trial 002's wiki analogy remains metaphorical until tested.

next_possible_action:
Use this surface to select a small active bundle, then decide whether the next task is Codex-light setup, Gemini-heavy analysis, Hermes bounded reading, QMD evidence pointer access, or user judgment.
```

## 10. Watch Items

- capsule becoming final truth
- re-entry surface becoming registry
- polished summary replacing provenance
- user language disappearing
- too many links causing burden
- every trace becoming capsule
- parent/neighbor links becoming ceremony
- candidate becoming baseline
- Codex over-structuring
- Gemini over-abstracting
- ChatGPT explaining instead of observing
- current_anchor_map being treated as "Wiki Homepage" rather than first-read candidate map
- mandatory interlinking becoming policy before real use

## Optional Compounding Check — Candidate

This check asks:

```text
What does this recovered judgment make easier next time?
```

evidence_type:
USER_PROVIDED_SUMMARY / GEMINI_TRIAL_EVIDENCE. A saved Trial 011 / Compound Engineering file was not found in the narrow check for this patch.

Trial 011 / Compound Engineering was useful as an external-reference lens, but it is not a VectorFL workflow or product template.

### Candidate Use

Use this check when deciding whether a result should become:

- judgment capsule
- re-entry surface
- policy mutation
- tool profile update
- watch item
- active bundle adjustment

### Not Mandatory

- not every result needs to compound
- if no next-work condition improved, keep it as raw trace / watch / hold
- do not invent a lesson just to fill the check
- this is not a required schema field
- this is not a workflow step
- this is not automation

### Example Questions

```text
Did this reduce future rediscovery cost?
Did this improve next active bundle selection?
Did this update a tool profile?
Did this create or refine a policy mutation?
Did this clarify a watch item?
Did this make future routing easier?
Did this only produce output without changing future conditions?
```

### Compounding Watch

- compounding becoming ceremony
- workers inventing lessons
- every trace becoming capsule
- documentation bloat
- review becoming approval instead of calibration
- user judgment bypassed

This addendum is a language/check refinement only.

It should be tested in 1-2 real closeouts before becoming a recurring field.

## 11. Relation to Existing Setup

### current_anchor_map

- identifies what to read first
- can point to re-entry surfaces later, but is not a wiki homepage or registry

### judgment_provenance_record

- labels where capsule judgments came from
- prevents synthesis from being treated as file evidence

### micro_run_trace_record

- supplies trace material that may later become capsule, watch, raw trace, hold, or discard
- prevents execution trace from becoming memory by default

### policy_mutation_record

- records when a capsule changes future operating conditions
- prevents lessons from being buried in summaries

### structural_setup_pack

- provides active bundle, telemetry, external reference translation, and degradation watch setup
- keeps this document as setup material rather than architecture

### Package R flow

- supplies the result-oriented path from User Purpose through Usefulness Gate, LACL placement, Return-to-Space, and User Judgment
- anchors the sample core sentence

## 12. Known Limits

- not tested
- not a wiki implementation
- not a final memory model
- sample may be too narrow
- Trial 002 standalone file was not found in this narrow pass
- external LLM Wiki source was not directly verified by Codex in this task
- should be revised after 2-3 real uses

## 13. Final Note

This document is a judgment capsule and re-entry surface candidate only.

It should be tested manually before any wiki, graph, or script implementation.

It should not be treated as final architecture.
