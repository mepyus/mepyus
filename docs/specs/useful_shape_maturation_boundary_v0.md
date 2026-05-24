# Useful Shape Maturation Boundary v0

## Status

```yaml
status: maturation_boundary_candidate
date: 2026-05-06
baseline_lock: false
automation: false
schema: false
registry: false
scope: anchor_stack_maturation
```

## Purpose

Prevent every useful structure from becoming an anchor, rule, workflow, or baseline.

This boundary defines a light maturation path for Anchor Stack setup artifacts.

## Maturation Path

```text
useful_shape
-> candidate_signal
-> reusable_setting_candidate
-> operating_anchor_candidate
```

## Markers

### useful_shape

Use when a structure helps one local task but has not yet shown reusable decision value.

Required evidence:

- local purpose
- one output or trial where it helped

Do not infer:

- no reuse claim
- no route/PV update

### candidate_signal

Use when the same shape appears relevant across more than one record or worker return.

Required evidence:

- at least two pointers or one strong worker return plus Codex packaging
- watch item stated

Do not infer:

- no baseline
- no automatic inclusion in small anchors

### reusable_setting_candidate

Use when the shape changes actual task behavior.

Required evidence:

- changes package sizing, stop/continue, route selection, or Return-to-Space shape
- has a canonical PV or route link

Do not infer:

- no schema
- no registry
- no automation

### operating_anchor_candidate

Use when the setting is stable enough to guide bounded work within a named line.

Required evidence:

- repeated use across sessions or trials
- clear do-not-infer boundary
- Movement Record support

Do not infer:

- no global line baseline
- no permanent authority

## Current Examples

| artifact | current marker | reason |
| --- | --- | --- |
| `ROUTE_EXTERNAL_TOOL_PLANNING` | reusable_setting_candidate | changes external worker plan shape. |
| `ROUTE_INPUT_CLASSIFICATION` | candidate_signal | useful but may merge with planning or session re-entry route. |
| `ROUTE_SPACE_RESIDUE_SAMPLING` | candidate_signal | proposed by Gemini; needs bounded residue sampling. |
| four-gate plan-mode sequence | reusable_setting_candidate | changed Set A worker behavior and has self-application trial. |
| Position Value Layer | reusable_setting_candidate | compresses small anchor handoff; still not ontology/schema. |

## Promotion Rule

Promotion requires a Movement Record note that states:

- what behavior changed
- what evidence supports reuse
- what watch remains
- what must not be inferred

## Do Not

- Do not promote based on clean wording alone.
- Do not treat repeated terminology as maturity.
- Do not make this boundary a database schema.
- Do not use this as an automatic classifier.
