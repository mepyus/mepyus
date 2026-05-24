# Space Observation Structural Setup Pack — 2026-05-09

## 0. Status

- candidate only
- setup pack only
- live-use with watch
- not baseline
- not schema
- not registry
- not automation
- not production workflow
- not final authority

## 1. Purpose

This setup pack exists to prepare the next layer of space observation work without performing the heavy work itself.

It provides compact candidate templates for low-token active reads, judgment provenance, tool behavior tracking, and degradation watch. The goal is to reduce rediscovery cost, make future Gemini execution/testing easier, and keep Codex focused on structural setup rather than broad synthesis.

This pack should help future workers ask:

- what active surfaces should be read
- where a judgment came from
- what tool behavior was observed
- what changed future operating conditions
- what should remain watch, raw trace, or candidate-only

## 2. Existing Setup Inputs

### A. current_anchor_map

Provides:
- a first-read candidate map of current anchors
- anchor roles, statuses, read conditions, and neighbor context
- minimal active bundles for current result-oriented operation

Must not become:
- baseline
- registry
- schema
- authority index
- final space map

### B. judgment_provenance_record

Provides:
- minimal provenance labels
- compact record fields for source-of-judgment tracking
- trial records separating observed file evidence, user judgment, missing evidence, and supervisor inference

Must not become:
- truth engine
- final provenance system
- schema
- replacement for user judgment

### C. tool_profile_record

Provides:
- candidate profiles for ChatGPT/Supervisor, Codex, Gemini, Hermes, QMD, and future tools
- observed strengths, drift risks, safe scopes, stop conditions, and next-use corrections
- optional telemetry fields for future trials

Must not become:
- routing authority
- doctrine
- registry
- permanent tool identity map

## 3. Candidate Template — Active Surface Bundle

Use this when a future worker needs a small, explicit reading set.

```text
bundle_id:
purpose:
route:
recommended_tool:
max_surfaces:
files_or_surfaces:
parent_context:
neighbor_context:
not_included:
required_provenance:
expected_useful_result:
return_placement_options:
watch:
```

### Sample: Result-Oriented Core Bundle

```text
bundle_id:
ASB_RESULT_ORIENTED_CORE_20260509_SAMPLE

purpose:
Understand the current live-use candidate operating stack before routing, packet drafting, or recovery.

route:
first-read / route selection / recovery framing

recommended_tool:
ChatGPT/Supervisor for routing; Codex for structural recovery; Gemini only if broader audit or testing is needed.

max_surfaces:
5

files_or_surfaces:
- app/work/space-skill-sandbox/outputs/result_oriented_operating_stack_closeout_20260508_v0.md
- app/work/space-skill-sandbox/outputs/user_facing_routing_card_v0_candidate_20260508.md
- app/work/space-skill-sandbox/outputs/mission_packet_result_contract_v0_candidate_20260508.md
- app/work/space-skill-sandbox/outputs/result_usefulness_gate_v0_candidate_20260508.md
- app/work/space-skill-sandbox/outputs/package_l_hermes_carrier_sizing_boundary_closeout_20260508_v0.md

parent_context:
Package M-Q result-oriented sequence and Package L Hermes sizing boundary.

neighbor_context:
current_anchor_map_candidate_20260509_v0.md; judgment_provenance_record_template_and_trial_20260509_v0.md; tool_profile_record_candidate_20260509_v0.md.

not_included:
Full RUNLOG; Package S standalone note; full Hermes/Gemini raw outputs.

required_provenance:
Separate observed file evidence from supervisor inference and user judgment.

expected_useful_result:
Recover the current flow, role split, Expected Useful Result discipline, and stop criteria without promoting them to baseline.

return_placement_options:
RETURN_TO_SPACE_VALUE_WITH_WATCH; WATCH; RAW_TRACE_ONLY if only restating file contents.

watch:
Do not treat the bundle as complete authority. Add parent or neighbor context when LACL, provenance, or record structure is the main task.
```

## 4. Candidate Template — Policy Mutation Record

Use this when an observed result changes a future operating condition.

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
```

### Sample: Read X -> Synthesize X to Enable Decision Y

```text
mutation_id:
PMR_RESULT_CONTRACT_SHIFT_20260509_SAMPLE

trigger:
Package N usefulness audit and Package O Result Contract patch.

observed_problem:
Packets that ask only "Read X" or "summarize X" can produce safe, shaped, low-value output.

source_run_or_package:
Package M Result Usefulness Gate; Package N audit; Package O Mission Packet Result Contract.

affected_tool_or_route:
Gemini mission packets, Hermes active-surface packets, Codex recovery checks, Supervisor routing.

old_condition:
Boundary and return-shape instructions were emphasized more than the decision/action value of the result.

new_condition:
Mission packets should define Expected Useful Result before execution: synthesize X to enable decision Y.

required_companion_context:
Result Usefulness Gate; Mission Packet Result Contract; user purpose; active surfaces.

provenance:
GEMINI_SYNTHESIS + CHATGPT_SUPERVISOR_INFERENCE + OBSERVED_FILE_EVIDENCE, depending on which recovery note is read.

status:
candidate with watch

watch:
Decision language must not become authority claim, validation, or promotion.
```

## 5. Candidate Template — External Reference Translation Record

Use this for future external materials such as mini-swe-agent, LLM Wiki, Graphiti, GMD, or GraphRAG. Do not analyze those sources in this setup pack.

```text
external_reference:
source_type:
original_problem:
core_mechanism:
what_to_borrow:
what_not_to_borrow:
fit_to_current_space:
small_experiment_candidate:
required_active_surfaces:
expected_recovered_judgment:
token_efficiency_question:
risk:
return_placement:
provenance:
```

Future Gemini should perform token-heavy external reference analysis using this record.

The expected output should not be a generic summary. It should identify what problem the external mechanism solves, what VectorFL should borrow, what should not be imported, and what small experiment or recovered judgment could change future execution conditions.

## 6. Candidate Template — Tool Telemetry Record

Use this only when a future trial needs lightweight tool behavior tracking.

```text
telemetry_id:
tool:
task_id:
input_active_surfaces:
input_size_estimate:
output_size_estimate:
result_type:
strength_observed:
drift_observed:
user_correction_needed:
recovered_judgment:
return_placement:
next_policy_change:
provenance:
watch:
```

This is optional trial telemetry, not mandatory scoring.

Do not turn token estimates or output sizes into fake precision. The purpose is to notice useful behavior and drift patterns, not to rank tools mechanically.

## 7. Candidate Template — Degradation Watch

Use this when a repeated drift or failure mode should affect future routing, packet design, or recovery.

```text
watch_id:
degradation_type:
trigger_condition:
observed_in:
affected_route_or_tool:
symptom:
correction:
status:
provenance:
```

Initial watch candidates:

- ChatGPT explaining instead of observing
- Codex over-structuring
- Gemini over-abstracting
- Hermes 1-5 success overgeneralized
- QMD pointer/score/body mistaken for memory
- small active surface losing parent context
- model inference treated as observed file evidence
- candidate map becoming baseline/registry/schema
- telemetry becoming fake precision

## 8. Codex vs Gemini Work Split

### Codex should be used for:

- structure setup
- file-grounded inspection
- anchor map
- templates
- lightweight candidate docs
- downshift / closeout / packet design

### Gemini should be used for:

- token-heavy analysis
- broad external reference reading
- execution/testing
- synthesis across many materials
- usefulness audit
- comparison rounds

### Supervisor / ChatGPT should:

- decide route
- check provenance
- prevent overpromotion
- translate results into user-facing judgment
- create next worklist

## 9. Recommended Next Tasks

Do not execute these from this setup pack.

### Codex-light tasks

- draft one active_surface_bundle trial
- draft one policy_mutation_record trial
- draft one external_reference_translation blank card
- draft one tool_telemetry sample from the recent Codex/Gemini comparison

### Gemini-heavy tasks

- analyze mini-swe-agent through external_reference_translation_record
- analyze LLM Wiki through external_reference_translation_record
- analyze Graphiti / GraphRAG through external_reference_translation_record
- compare which external mechanism best supports space maturation

### Supervisor tasks

- turn results into prioritized worklist
- decide which structure is useful after 2-3 real uses
- keep all outputs candidate-with-watch

## 10. Known Limits

- setup pack is not tested
- templates may be too many
- risk of ceremony bloat
- risk of structure replacing judgment
- Gemini still needs actual external-source reading
- Codex should not spend tokens on broad synthesis
- user judgment remains final

## 11. Final Note

This document is a structural setup pack only.

It should be revised after 2-3 real uses.

It should not be treated as final architecture, schema, registry, or automation.
