# Space Asset Retrieval Manual v0

## Purpose

This manual explains how to pull the right assets out of the space quickly.

## First Retrieval Rule

Retrieve by asset role, not by filename guess alone.

The main retrieval split is:

- source assets
- runtime artifacts
- reports
- specs / contracts / policies
- imported references

## Asset Role Map

### 1. Source Assets

Use when you need original internal guidance or declared intent.

Primary zones:

- `source_assets/declarations/`
- `source_assets/baselines/`
- `source_assets/directives/`
- `source_assets/handoffs/`

Use these for:

- what the space was trying to become
- what was locked as a baseline
- what operators or Codex were told to do

### 2. Runtime Artifacts

Use when you need latest evidence of what the system actually did.

Primary zones:

- `runtime/manifests/`
- `runtime/events/`
- `runtime/receipts/`
- `runtime/views/`

Use these for:

- latest pointer
- registry truth
- receipt trail
- current run/state evidence

### 3. Reports

Use when you need interpreted results or bounded closeout judgment.

Primary zone:

- `docs/reports/`

Use these for:

- what happened
- what was learned
- what remained thin
- what next bounded move was justified

### 4. Specs / Contracts / Policies

Use when you need shape, rules, or boundaries.

Primary zones:

- `docs/specs/`
- `docs/contracts/`
- `docs/policies/`

Use these for:

- allowed shape
- forbidden overreach
- stable operating boundary

### 5. Imported References

Use when the target lives outside our original space but has been copied in.

Primary zone:

- `references/git_search/`

Use these for:

- external tool analysis
- external pattern comparison
- adaptation into our own space

## Retrieval By Question

### “What were we trying to do?”

Read:

- declarations
- baselines
- directives

### “What does the system actually do now?”

Read:

- latest runtime manifests
- latest views
- receipts

### “What is the current judgment?”

Read:

- reports first
- then contracts/specs if the report depends on a boundary

### “What external tool or repo are we comparing?”

Read:

- imported reference repo
- then our own related reports/specs

## What To Avoid

Do not:

- read every report before acting
- treat runtime latest files as source intent
- treat declarations as proof of runtime behavior
- treat imported repos as direct adoption instructions

## One-Line Summary

Pull assets by role: source intent, runtime evidence, interpreted report, stable boundary, or imported reference.
