# Phase 1.28 Flow-Aware Evidence Log Storage Convention v0

## Purpose

This note fixes the minimal storage convention for trigger-based reopen evidence logs.

The goal is to keep logs:

- easy to find
- bounded in scope
- hard to confuse with broad tuning

## Storage Location

Recommended location:

- `runtime/reopen_evidence_logs/flow_aware/`

Reason:

- close enough to runtime operating use
- separate from reports and trial outputs
- easy for operator and Codex to locate without searching across unrelated folders

## File Unit Rule

Use **one file per incident**.

Current decision:

- one-file-per-incident is the more honest choice

Reason:

- reopen permission is family-level or bucket-level
- each trigger incident should stay bounded
- append-style rolling logs make scope creep easier and blur which request belongs to which trigger

## File Naming Rule

Use the following shape:

- `YYYYMMDD_<family>_<trigger-type>_<reopen-scope>_<short-slug>.md`

Required filename elements:

- date
- family
- trigger type
- reopen scope
- short slug or sequence

Example filenames:

- `20260422_general_line_vs_flow_middle_case_pressure_family_recheck_v1.md`
- `20260422_raw_intake_gap_default_rule_contradiction_placement_recheck_v1.md`
- `20260422_input_layer_wrapper_carry_forward_drift_protection_recheck_v1.md`

## Folder Structure Example

```text
runtime/
  reopen_evidence_logs/
    flow_aware/
      20260422_general_line_vs_flow_middle_case_pressure_family_recheck_v1.md
      20260422_raw_intake_gap_default_rule_contradiction_placement_recheck_v1.md
```

## Append vs One-File-Per-Incident

### Recommended now: one-file-per-incident

Why:

- keeps each reopen request bounded
- matches family-level or bucket-level scope
- makes review simpler
- prevents unresolved pressure from accumulating into an unbounded argument log

### Not recommended now: append-style family log

Why not:

- too easy to turn into a rolling debate
- makes reopen depth harder to see
- weakens the current guardrail against broad reopen

## Writing Rule

Write an evidence log only when:

- a trigger is actually present
- a bounded reopen request is needed

Do not write an evidence log when:

- there is no trigger
- the note is just exploratory
- the goal is to reopen tuning broadly

## Scope Rule

An evidence log is a **bounded reopen request**, not a reopen decision.

It may request only:

- family-level reopen
- bucket-level reopen
- bounded reopen depth

It may not request:

- global heuristic rewrite
- allow-list / block-list reset
- emitter/classifier/schema reopen

## Broad Reopen Guard

Do not create a storage pattern that encourages broad reopen.

Specifically:

- no giant append log
- no multi-family incident bundle by default
- no generic “reopen ideas” file in this folder

Use only bounded incident files.
