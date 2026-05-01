# External Reference Subtype Contract v0

## Purpose

This contract defines a small subtype layer for external references.

The goal is not promotion.
The goal is to reduce retrieval cost and merge ambiguity as more external inputs accumulate.

## Core Rule

Do not store every external reference as one undifferentiated `external article`.

Assign one bounded subtype at ingest time.

## Allowed Subtypes

### 1. `broad_reference`

Use when the source is mostly:

- summary-shaped
- principle-heavy
- broad engineering or product reflection
- weak on concrete runtime surface

Typical use:

- background rationale
- boundary reminder
- anti-overbuild reminder

### 2. `operating_reference`

Use when the source is mostly:

- concrete operating guidance
- workflow or process behavior
- role, boundary, or mode discipline
- practical but not API-shaped

Typical use:

- run-mode judgment
- boundary-aware operation
- worker vs interactive separation

### 3. `api_surface_reference`

Use when the source is mostly:

- product or API surface
- explicit execution model
- tool surface
- request/response or plan/run boundary

Typical use:

- orchestration comparison
- planning/execution boundary comparison
- tool-boundary comparison

### 4. `raw_capture`

Use when the preserved artifact is still mainly:

- transcript
- copied raw text
- loose capture
- probe input, not yet stable ingest surface

Typical use:

- provenance preservation
- script-first gate/probe
- pre-memo holding state

## Assignment Rule

Pick the subtype by dominant operating use, not by publication brand.

Examples:

- GeekNews law summary -> `broad_reference`
- token efficiency tuning article -> `operating_reference`
- Gemini Deep Research API guide -> `api_surface_reference`
- pasted X thread text -> `raw_capture`

## Storage Rule

Subtype does not replace current storage rules.

Keep using:

- `inputs/external_cases/`
- `[[DOCROLE:memo]]`
- `[[RUNMODE:ingest_only]]`
- `[[PRIORITY:normal]]`

Subtype should be recorded inside the memo body under source metadata or source note fields.

## Retrieval Rule

When comparing or merging external references:

- prefer same-subtype comparison first
- allow cross-subtype merge only when the sources are complementary

Cross-subtype merge is strongest when it combines:

- broad rationale
- concrete runtime surface
- concrete operator control

## Promotion Guard

Subtype is a retrieval aid, not a promotion signal.

Subtype assignment does not justify:

- axis naming
- operating rule promotion
- direct adoption
- architecture replacement

## Summary

External reference subtype exists to keep external ingest legible:

- `broad_reference`
- `operating_reference`
- `api_surface_reference`
- `raw_capture`
