# Micro-Run Trace Record Candidate — 2026-05-09

## 0. Status

- candidate only
- trace record candidate only
- live-use with watch
- not baseline
- not schema
- not registry
- not automation
- not mini-agent implementation
- not proof of usefulness
- not replacement for user judgment

## 1. Purpose

This document defines how a future micro-run should leave a trace that VectorFL can later read, evaluate, and recover.

The purpose is to preserve small execution traces without mistaking trace for memory, proof, or useful judgment. A micro-run trace should support tool telemetry, policy mutation, Result Usefulness Gate review, and future script or mini-agent experiments only after the trace is recoverable and provenance-aware.

The main operating point:

```text
Build the readable trace shape before building the runner.
```

## 2. Micro-Run Definition

A micro-run is a bounded, explicitly scoped action sequence that reads selected active surfaces, performs a small action or check, records what happened, and returns enough trace for later recovery.

A micro-run is not:

- autonomous agent run
- full task automation
- baseline operation
- broad repo exploration
- memory by default
- proof that a result is useful
- replacement for user judgment

## 3. Minimal Micro-Run Trace Fields

Use this compact candidate template when a future micro-run needs to leave recoverable process material.

```text
micro_run_id:
purpose:
trigger:
route:
recommended_tool:
input_active_surfaces:
allowed_actions:
blocked_actions:
action_trace:
output_summary:
observed_drift:
boundary_check:
shape_check:
usefulness_check:
provenance:
return_placement_candidate:
recovered_judgment_candidate:
policy_mutation_candidate:
tool_telemetry_link:
raw_trace_location:
watch:
```

Keep this minimal. It is a candidate record shape, not a schema.

## 4. Action Trace Shape

Smallest useful action trace candidate:

```text
step:
action:
input_ref:
result:
error_or_warning:
next_action_reason:
```

The action trace can be shell-like, file-read-like, or worker-action-like.

Do not require Bash. Bash-only is an external-reference-inspired candidate principle, not a fixed VectorFL rule.

## 5. Boundary Rules

Candidate boundaries:

- read only unless user explicitly approves write
- no broad repo scan unless route requires it
- no baseline/schema/registry promotion
- no hidden automation
- no destructive commands
- no treating trace as memory
- no user judgment bypass
- active surfaces should be explicit
- not-inspected scope should be stated

## 6. Relation to Existing Structures

### current_anchor_map

- selects first-read anchors
- prevents broad rediscovery before the micro-run
- supplies parent and neighbor context for small active surfaces

### judgment_provenance_record

- labels where trace-derived judgments came from
- separates observed file evidence, user judgment, process trace, Gemini synthesis, and missing evidence
- prevents model inference from being treated as file evidence

### tool_profile_record

- records observed tool behavior
- links micro-run results to strengths, drifts, safe scopes, and next-use corrections
- prevents a successful run from becoming a permanent tool identity

### structural_setup_pack

- connects active bundle, policy mutation, tool telemetry, degradation watch, and external reference translation
- keeps this record as setup material, not automation

### Package R result-oriented flow

- micro-run fits between External Execution and Worker Return Intake
- recovery happens only after Boundary Check, Shape Check, Result Usefulness Gate, LACL Placement, and User Judgment

## 7. Sample Record — External Reference Translation Trial 001

This is not an execution trace.

It is a conceptual translation trace sample based on the user-provided Gemini mini-swe-agent / swe-mini-agent external-reference trial summary. A standalone local Trial 001 file was not confirmed in this pass.

```text
micro_run_id:
MRT_EXTERNAL_REFERENCE_TRIAL_001_MINI_SWE_AGENT_SAMPLE_20260509

purpose:
Translate the mini-swe-agent / swe-mini-agent reference into a VectorFL micro-run trace candidate without adopting it as automation.

trigger:
Gemini external-reference translation trial reported by the user.

route:
Gemini-heavy external reference translation -> Codex-light structural recovery.

recommended_tool:
Gemini for token-heavy external reference comparison; Codex for downshifted trace record structure.

input_active_surfaces:
- user-provided Gemini Trial 001 summary in current context
- current_anchor_map_candidate_20260509_v0.md
- judgment_provenance_record_template_and_trial_20260509_v0.md
- tool_profile_record_candidate_20260509_v0.md
- space_observation_structural_setup_pack_20260509_v0.md

allowed_actions:
- translate external mechanism into VectorFL candidate principle
- define trace shape before runner shape
- separate trace from memory
- mark missing source inspection

blocked_actions:
- no script implementation
- no Bash loop creation
- no mini-agent clone
- no baseline/schema/registry promotion
- no treating external reference as VectorFL authority

action_trace:
1.
  action:
  Read current setup anchors.
  input_ref:
  current anchor map, provenance record, tool profile, structural setup pack.
  result:
  Existing setup supports active bundles, provenance labels, tool profiles, policy mutation, telemetry, and degradation watch.
  error_or_warning:
  none for required setup reads.
  next_action_reason:
  Use existing setup to place micro-run trace as a candidate record.

2.
  action:
  Apply user-provided Gemini Trial 001 summary.
  input_ref:
  current user input summarizing mini-swe-agent translation.
  result:
  mini-swe-agent-like simplicity is useful as a thin trace/reproducibility inspiration, not as an automation import.
  error_or_warning:
  external source code/original structure was not inspected by Codex in this task.
  next_action_reason:
  Downshift into trace record candidate with missing-evidence watch.

output_summary:
mini-swe-agent-like simplicity may help VectorFL design bounded micro-run traces, but should not be copied as automation or treated as a full operating model.

observed_drift:
- "perfectly aligned" and "High confidence" language should be downshifted.
- Bash-only can become doctrine if not marked candidate.
- trace file + link can be mistaken for approved implementation direction.

boundary_check:
PASS_WITH_WATCH as structural recovery only. No script, runner, automation, schema, registry, or baseline created.

shape_check:
Candidate trace fields are defined and linked to provenance, usefulness, telemetry, policy mutation, and watch placement.

usefulness_check:
Useful as a micro-run trace structure candidate. Not useful as implementation approval.

provenance:
- GEMINI_SYNTHESIS
- EXTERNAL_REFERENCE_KNOWLEDGE
- USER_LONG_TERM_CONTEXT
- MISSING_EVIDENCE for external source structure/source code not inspected by Codex in this task

return_placement_candidate:
WATCH + RETURN_TO_SPACE_VALUE_WITH_WATCH

recovered_judgment_candidate:
micro-run is not automation; it is an observation unit whose trace must be read by the space before becoming judgment.

policy_mutation_candidate:
Before any future micro-run script or mini-agent, define required trace, provenance, usefulness check, and return placement.

tool_telemetry_link:
Future telemetry should record tool, active surfaces, result type, drift, recovered judgment, return placement, and next policy change.

raw_trace_location:
not applicable for this conceptual sample; no local standalone Trial 001 file confirmed in this pass.

watch:
- over-automation
- Bash-only becoming doctrine
- trace mistaken for memory
- token efficiency reducing judgment quality
- external reference treated as direct template
```

## 8. Degradation Watch Candidates

- micro-run becoming automation
- trace mistaken for memory
- Bash-only interface becoming doctrine
- script execution bypassing user judgment
- token efficiency reducing judgment quality
- active surface too small
- Codex over-structuring micro-run into framework
- Gemini over-abstracting without experiment candidate
- raw trace filling chat instead of being compressed
- recovered judgment missing

## 9. Recommended Next Uses

Do not execute these from this document.

### Codex-light

- draft active_bundle trial for one micro-run
- draft policy_mutation record for micro-run trace separation rule
- draft tool_telemetry sample for one future micro-run

### Gemini-heavy

- compare mini-swe-agent with Graphiti / LLM Wiki for trace-to-lineage transition
- analyze when linear trace is enough and when graph/wiki relation is needed

### Supervisor

- decide whether micro-run trace candidate is useful after 2-3 trials
- prevent early automation
- convert useful traces into worklist / watch / policy mutation

## 10. Known Limits

- not tested
- no script implemented
- no mini-agent created
- external reference source structure not inspected by Codex in this task
- field names may change
- too much trace can still create token bloat
- too little trace can destroy provenance
- standalone local Gemini Trial 001 file was not confirmed in this pass

## 11. Final Note

This is a micro-run trace record candidate only.

It should be tested manually before any script or mini-agent implementation.

It should be revised after 2-3 real uses.

It should not be treated as automation or final architecture.
