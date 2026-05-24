# Policy Mutation Record Candidate — 2026-05-09

## 0. Status

- candidate only
- policy mutation record candidate only
- live-use with watch
- not baseline
- not schema
- not registry
- not automation
- not governance system
- not replacement for user judgment

## 1. Purpose

This document defines how the space records changes to future operating conditions.

A policy mutation record exists to keep useful lessons from being buried inside closeouts, traces, tool reports, or user corrections. It connects trace, tool behavior, provenance, and result usefulness to the next operating condition while keeping every change candidate-with-watch.

Short form:

```text
Because we observed X, future work should change condition Y, with watch Z.
```

This is how the space matures instead of merely storing records.

## 2. Minimal Policy Mutation Fields

Use this compact candidate template when an observed result changes a future operating condition.

```text
mutation_id:
trigger:
observed_problem:
source_run_or_package:
affected_tool_or_route:
old_condition:
new_condition:
required_companion_context:
provenance:
status:
watch:
next_review_condition:
```

Keep it minimal. This is a candidate record shape, not a schema.

## 3. Mutation Record A — Read X -> Synthesize X to Enable Decision Y

```text
mutation_id:
PMR_RESULT_CONTRACT_SHIFT_20260509_A

trigger:
Package M/N/O/R result-oriented stack and usefulness audit sequence.

observed_problem:
Mission packets that ask only "Read X" or "summarize X" can produce safe, shaped, low-value output that does not help the user decide, act, revise, stop, or recover.

source_run_or_package:
- Package M Result Usefulness Gate
- Package N usefulness audit, as represented in later recovery context
- Package O Mission Packet Result Contract
- Package R result-oriented operating stack closeout

affected_tool_or_route:
Gemini mission packets; Hermes active-surface packets; Codex recovery checks; ChatGPT/Supervisor route framing.

old_condition:
Boundary and return-shape instructions were sufficient to launch external work.

new_condition:
Future mission packets should define Expected Useful Result before execution: synthesize X to enable decision Y.

required_companion_context:
Result Usefulness Gate; Mission Packet Result Contract; user purpose; active surfaces; do-not-promote boundary.

provenance:
OBSERVED_FILE_EVIDENCE where Package O/R files are read; GEMINI_SYNTHESIS for Package N audit lesson; CHATGPT_SUPERVISOR_INFERENCE for routing interpretation.

status:
candidate with watch

watch:
Decision language must not become authority claim, proof, validation, promotion, or baseline.

next_review_condition:
Review after 2-3 future mission packets use Expected Useful Result and produce visibly better recovery decisions.
```

## 4. Mutation Record B — First-Read Anchor Before Space Reasoning

```text
mutation_id:
PMR_FIRST_READ_ANCHOR_BEFORE_SPACE_REASONING_20260509_B

trigger:
Current anchor map candidate and repeated user correction that future workers should observe the space before explaining it.

observed_problem:
Space-related answers can drift into conceptual explanation if the current anchors are not read or referenced first.

source_run_or_package:
- current_anchor_map_candidate_20260509_v0.md
- user instruction to inspect or observe the current space rather than infer from memory alone
- judgment_provenance_record trial watch on ChatGPT/Supervisor explaining instead of observing

affected_tool_or_route:
ChatGPT/Supervisor; Codex; Gemini.

old_condition:
Workers could answer from remembered/project context or general conceptual understanding before checking current anchors.

new_condition:
Before space-related reasoning, read or reference the current anchor map when available, then state whether the answer is based on observed files, user input, process trace, or inference.

required_companion_context:
current_anchor_map candidate; judgment provenance record; user purpose; task scope.

provenance:
OBSERVED_FILE_EVIDENCE for current anchor map and provenance trial; USER_CURRENT_INPUT / USER_LONG_TERM_CONTEXT for the correction; CHATGPT_SUPERVISOR_INFERENCE for application.

status:
candidate with watch

watch:
The anchor map must not become baseline, registry, schema, authority index, or a substitute for reading the actual needed files.

next_review_condition:
Review after several future answers start from the anchor map and reduce rediscovery or conceptual drift.
```

## 5. Mutation Record C — Judgment Provenance Required

```text
mutation_id:
PMR_JUDGMENT_PROVENANCE_REQUIRED_20260509_C

trigger:
Judgment Provenance Record Template and Trial.

observed_problem:
Future workers may silently blend user input, observed file evidence, process trace, model inference, Gemini synthesis, external source claims, and experiment results.

source_run_or_package:
- judgment_provenance_record_template_and_trial_20260509_v0.md
- evidence provenance classification candidate, when used as neighbor context

affected_tool_or_route:
ChatGPT/Supervisor; Codex; Gemini; Hermes; QMD; future external tools.

old_condition:
Judgments could be returned without explicit source type or evidence level.

new_condition:
Space-related judgments should identify their source type when the distinction affects recovery, routing, promotion, or watch status.

required_companion_context:
provenance labels; evidence level guidance; return placement vocabulary.

provenance:
OBSERVED_FILE_EVIDENCE for the provenance template; USER_CURRENT_INPUT / USER_LONG_TERM_CONTEXT for the user's requested discipline.

status:
candidate with watch

watch:
Provenance labels must not become a truth engine, ceremony bloat, or fake precision.

next_review_condition:
Review after 2-3 real records use source labels and show whether the labels clarified or slowed recovery.
```

## 6. Mutation Record D — Codex-Light / Gemini-Heavy Work Split

```text
mutation_id:
PMR_CODEX_LIGHT_GEMINI_HEAVY_SPLIT_20260509_D

trigger:
User instruction after tool profile setup and structural setup pack.

observed_problem:
Codex can spend too many tokens on broad reading or analysis when the current need is structural setup; Gemini is better suited for token-heavy external reference reading, testing, comparison, and audit.

source_run_or_package:
- current user instruction
- tool_profile_record_candidate_20260509_v0.md
- space_observation_structural_setup_pack_20260509_v0.md

affected_tool_or_route:
Supervisor task routing; Codex structural setup; Gemini-heavy execution/analysis packages.

old_condition:
Codex could be asked to deeply inspect, analyze, and structure in the same pass.

new_condition:
Use Codex for structural setup, anchor/template/candidate docs, file-grounded inspection, downshift, and closeout. Use Gemini for token-heavy analysis, external reference reading, execution/testing, comparison, synthesis, and audit.

required_companion_context:
tool profile record; structural setup pack; current user purpose; no-promotion boundary.

provenance:
USER_CURRENT_INPUT + OBSERVED_FILE_EVIDENCE from tool profile and setup pack.

status:
candidate with watch

watch:
Do not freeze tool identities. Model versions, context, task type, and user intent may change the route.

next_review_condition:
Review after Gemini handles 1-2 external reference analyses using Codex-created templates.
```

## 7. Mutation Record E — Micro-Run Trace Separation Rule

```text
mutation_id:
PMR_MICRO_RUN_TRACE_SEPARATION_20260509_E

trigger:
Micro-Run Trace Record Candidate and Gemini mini-swe-agent translation as reported by the user.

observed_problem:
Future micro-run scripts or mini-agent experiments could produce unclassified logs that are mistaken for memory, proof, or useful judgment.

source_run_or_package:
- micro_run_trace_record_candidate_20260509_v0.md
- user-provided Gemini mini-swe-agent / swe-mini-agent translation summary
- space_observation_structural_setup_pack_20260509_v0.md

affected_tool_or_route:
future micro-run / script / mini-agent experiments; Codex structural recovery; Gemini external reference analysis; Supervisor worklist.

old_condition:
A future small runner could be evaluated by whether it executed or produced a log.

new_condition:
Every future micro-run should return trace + recovered judgment candidate + provenance + return placement candidate before any recovery or reuse.

required_companion_context:
micro-run trace record; judgment provenance record; tool telemetry fields; Result Usefulness Gate; user judgment.

provenance:
OBSERVED_FILE_EVIDENCE for micro-run trace candidate; GEMINI_SYNTHESIS + EXTERNAL_REFERENCE_KNOWLEDGE for mini-swe-agent translation; MISSING_EVIDENCE where original source structure/code was not inspected by Codex in the micro-run task.

status:
candidate with watch

watch:
Trace is not memory. Micro-run is not automation. User judgment remains final. Bash-only is candidate inspiration, not doctrine.

next_review_condition:
Review after one manual micro-run-style trial returns trace, provenance, recovered judgment candidate, and return placement.
```

## 8. Relation to Existing Setup

### current_anchor_map

- supplies first-read anchors and minimal active bundles
- prevents policy mutation records from being written from memory alone
- must not become policy authority

### judgment_provenance_record

- supplies labels for where each mutation came from
- separates observed evidence, user judgment, Gemini synthesis, external source knowledge, process trace, and missing evidence
- prevents one trial from being treated as proof

### tool_profile_record

- identifies which tool or route is affected by each mutation
- records observed drift and next-use correction
- prevents role split from becoming permanent tool identity

### structural_setup_pack

- provides the initial policy mutation template and connects it to active bundles, telemetry, external reference translation, and degradation watch
- keeps mutation records as setup material, not governance

### micro_run_trace_record

- supplies the trace separation rule and fields that future micro-runs should return before recovery
- prevents logs from being mistaken for memory or recovered judgment

### Package R result-oriented flow

- policy mutation happens after Result Usefulness Gate and LACL placement
- mutation records should influence future route/packet conditions without bypassing user judgment

## 9. Usage Note

Future workers should use this document when:

- a trial result changes next instructions
- a tool drift changes future packet design
- a trace changes recovery rules
- external reference analysis changes what to borrow or avoid
- a user correction changes Supervisor behavior

Future workers should not use this document to:

- enforce rules automatically
- promote candidates
- bypass user judgment
- treat one trial as proof
- create governance system

## 10. Known Limits

- first mutation set only
- not tested across many runs
- some mutations are based on user/supervisor judgment, not repeated experiment
- may be too many fields
- should be revised after 2-3 real uses
- risk of governance overbuild

## 11. Watch Items

- policy mutation becoming baseline
- policy mutation becoming hidden automation
- one trial overgeneralized
- user judgment bypassed
- Codex over-structuring
- Gemini over-abstracting
- provenance labels becoming ceremony
- tool split becoming rigid doctrine
- micro-run trace mistaken for memory
- anchor map treated as authority

## 12. Final Note

This is a policy mutation record candidate only.

It should be revised after 2-3 real uses.

It should not be treated as final policy, governance, schema, registry, or automation.
