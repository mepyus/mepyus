# Whole-Space Handoff Checklist v1 Light Revision Design v0

## Status

- status: design candidate
- baseline: false
- official_workflow: false
- source_space_promotion: false
- automation: false
- schema: false
- controller: false

## Purpose

Design the light revision needed before Gemini calibration of:

```text
app/work/space-skill-sandbox/outputs/whole_space_handoff_checklist_v1_candidate.md
```

This is not a rewrite. It is a narrow safety design to prevent Gemini or future workers from overreading v1 as official workflow, schema, or execution permission.

## Design Judgment

The v1 candidate is structurally sound. The problem is not missing structure. The problem is over-structure risk.

Therefore the revision should add only four small guards:

```text
Usage Mode
Anti-Schema Warning
Gemini Calibration Warning
Example Non-Instruction Warning
```

## 1. Usage Mode Guard

Add near the top:

```text
Usage Mode:

Full mode is for cross-agent, cross-session, approval-gated, high-risk, or whole-space handoffs.

Compact mode is for ordinary handoffs:
identity / context / authority_status / source_refs / next / forbidden_actions.

Do not apply this checklist to trivial single-turn requests.
```

Purpose:

Prevent the checklist from becoming ceremony for every small request.

## 2. Anti-Schema Warning

Add near the status or field-layers section:

```text
These fields are judgment prompts, not required schema fields.
Missing fields may be acceptable when the handoff is low-risk and current position is clear.
Do not turn this checklist into a parser, ledger, ontology, controller, router, or enforcement mechanism.
```

Purpose:

Prevent schema hardening.

## 3. Gemini Calibration Warning

Add before any Gemini-facing use:

```text
Gemini should read this as boundary training and return-format guidance.
It is not permission to execute, approve, promote, modify files, or open new package work.
Gemini output remains worker evidence for Codex/User review.
```

Purpose:

Prevent Gemini from reading v1 as execution authority.

## 4. Example Non-Instruction Warning

Strengthen the example note:

```text
The example is historical-pattern illustration only.
Do not follow it as a live package instruction.
Do not analyze package targets from the example.
```

Purpose:

Prevent example package references from becoming live work.

## What Must Stay Unchanged

- candidate-only status
- run identity correction note
- `source_refs`
- `memory_layer`
- `authority_status`
- sandbox 15 principles as audit lens
- external lenses as `connection_candidate`
- User approval authority

## Gemini Calibration Scope

Gemini should not revise the checklist.

Gemini should return a calibration note answering:

```text
Can I read v1 without treating it as official workflow?
What should I learn?
What might I overread?
How should I use full mode vs compact mode?
What must I never infer from this checklist?
```

## Boundary

- no Gemini execution
- no package work
- no baseline
- no official workflow
- no automation / policy / schema / router / controller / graph / ontology

