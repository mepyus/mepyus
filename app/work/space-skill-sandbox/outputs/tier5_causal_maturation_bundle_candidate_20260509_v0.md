# Tier 5 Causal Maturation Bundle Candidate — 2026-05-09

## 0. Status

- candidate only
- Tier 5 causal maturation candidate only
- live-use with watch
- not baseline
- not schema
- not registry
- not automation
- not RUNLOG parser
- not final causality engine
- not replacement for user judgment

## 1. Purpose

This file preserves the Trial 009 finding as a practical rule for when and how to add RUNLOG.

It exists to add RUNLOG only when causality is the question, prevent full RUNLOG reads, preserve event-level sequence, distinguish semantic change from process trace, and prevent RUNLOG `reason` fields from becoming truth claims.

## 2. Tier 5 Definition

Tier 5 means:

```text
Relevant semantic bundle + bounded RUNLOG slice
```

Use for:

- event-level causality
- why a policy changed
- actual drift sequence
- success/fail sequence
- package lineage audit
- root-cause depth check

Do not use for:

- normal summary
- ordinary judgment capsule production
- tool calibration without causal question
- routing drift without event question
- broad history reading

Tier 5 is still bounded process causality, not full causality.

## 3. Bounded RUNLOG Slice Rule

Candidate rule:

```text
Start with a focused semantic question.
Identify relevant package IDs / keywords.
Search only matching RUNLOG entries.
Prefer small grep/tail slices.
Do not read full RUNLOG.
Record slice method.
Record approximate slice size.
Record missing raw trace.
```

Candidate example, not universal command:

```bash
grep -E "Package M|Package N|Package O|Package Q|Package R|result_usefulness|result contract|active bundle|Trial 004|Trial 005|Package U|Trial 006|Trial 007|Trial 008|space_observation" RUNLOG.jsonl | tail -n 80
```

The slice should be treated as process trace, not semantic proof.

## 4. What RUNLOG Can Provide

- timestamps
- action sequence
- package linkage
- input_refs
- output_refs
- worker-stated reason
- process trace
- sequence causality

## 5. What RUNLOG Cannot Provide Alone

- full semantic meaning
- user final judgment
- raw behavioral detail if not linked
- proof of root cause
- truth of worker reason field
- replacement for source files
- replacement for raw trace or session logs

## 6. Causality Strength Levels

```text
SEMANTIC_ONLY:
Meaning inferred from docs, no process trace.

SEQUENCE_CAUSALITY:
RUNLOG shows order and input/output references.

SUMMARY_CAUSALITY:
RUNLOG reason field explains why, but raw evidence is not present.

RAW_TRACE_CAUSALITY:
Underlying raw trace or session log confirms the behavior.

USER_CONFIRMED_CAUSALITY:
User confirms the causal interpretation.
```

These levels are candidate-only. They should not become a scoring system.

## 7. Trial 009 Summary

evidence_type:
USER_PROVIDED_SUMMARY / GEMINI_TRIAL_EVIDENCE. Trial 009 standalone file was not found in the narrow saved-file check for this task.

summary:
- A 4-file semantic bundle was used.
- A bounded RUNLOG slice was used.
- Approximately 5 JSONL entries were reportedly enough to recover sequence-level causality.
- Package O linked to Package N via `input_refs`.
- The recovered sequence included Package M -> Package O -> Package Q -> Package R -> Package Q patch.
- Causality remained partial because raw Package N failure / behavior logs were absent.

verdict:
GOOD_FOR_RUNLOG_NEIGHBOR_WITH_PARTIAL_PROCESS_CAUSALITY

downshift:
Trial 009 supports bounded sequence causality, not full root-cause proof.

## 8. Tier 5 Causal Record Template

Use this compact candidate template when RUNLOG is added to a semantic bundle for causality.

```text
causal_record_id:
semantic_change:
suspected_trigger:
runlog_slice_method:
runlog_entries_used:
observed_process_evidence:
causality_strength:
source_bundle:
provenance:
evidence_level:
inference_level:
missing_raw_trace:
return_placement_candidate:
watch:
```

This is a candidate shape, not a schema.

## 9. Relation to Existing Setup

### active_bundle_tier_map

- defines Tier 5 as relevant semantic bundle plus bounded RUNLOG slice
- keeps lower tiers available when causality is not the question

### judgment_provenance_record

- labels RUNLOG as PROCESS_TRACE
- prevents process trace from being treated as semantic validation

### policy_mutation_record

- uses Tier 5 when the question is why a policy changed
- keeps future-condition changes tied to observed or reported process evidence

### judgment_lineage_map

- uses RUNLOG slice to strengthen relationship chains from inferred lineage toward sequence causality
- does not convert relationships into proof

### micro_run_trace_record

- separates raw/process trace from recovered judgment
- reminds workers that missing raw trace limits causality depth

### Package R result-oriented flow

- RUNLOG enters after a focused question and before recovery placement
- result still needs Usefulness Gate, LACL placement, and User Judgment

## 10. Watch Items

- full RUNLOG read by habit
- RUNLOG reason treated as truth
- sequence mistaken for root cause
- bounded slice missing key event
- process trace overriding semantic judgment
- raw trace ignored when needed
- old traces reviving deprecated conditions
- token explosion through log reading
- user judgment bypassed
- Trial 009 summary treated as observed file evidence without saved report

## 11. Recommended Next Trial

Trial 010 — Bounded RUNLOG Slice Prepared by Codex

Purpose:

Test whether Codex-light can prepare a cleaner RUNLOG causal slice for Gemini-heavy analysis.

Candidate prompt fragment:

```text
Prepare one bounded RUNLOG slice for a named causality question. Record keywords, slice size, omitted scope, and missing raw trace. Do not interpret beyond process trace.
```

Do not execute Trial 010 from this document.

## 12. Final Note

This document is a Tier 5 causal maturation candidate only.

It should be revised after 1-2 more bounded RUNLOG trials.

It should not be treated as final causality policy.
