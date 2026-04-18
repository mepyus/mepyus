# Integrated Engine Wording Patch Promotion Gate v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This gate defines when a wording-only patch may be promoted from use observation.

It does not define patch text. It does not approve implementation. It does not authorize scaffold restructuring, manifest changes, read-map changes, runtime binding, trace UI, selected-object behavior, or extension promotion.

## 1. purpose

The purpose is to prevent premature wording churn while still allowing repeated use-time confusion to be corrected.

Patch only when:

- the baseline structure works
- the confusion is repeated
- the fix is wording-only
- the fix protects an existing boundary
- no held extension is required

## 2. eligibility criteria

A wording candidate is eligible for promotion review only if all are true:

1. It has been logged in the wording confusion log.
2. It appears in at least two use observations, or appears once and blocks scenario reading.
3. It is tied to a specific surface and panel.
4. It has a clearly stated intended reading from current baseline docs.
5. It can be clarified without changing:
   - panel identity
   - central panel gravity
   - manifest shape
   - read map
   - runtime behavior
   - selected-object behavior
   - trace UI
   - extension status
6. It does not hide fixture scope or trace boundary under wording.

## 3. non-eligibility criteria

Do not promote a wording patch if the issue is actually:

- first-fixture scaffold scope
- current core-support trace boundary
- absence of selected-object behavior
- absence of trace UI
- absence of runtime binding
- desire for denser evidence/history
- desire for team/ownership/approval extension
- desire for worker/process telemetry
- old mock/lineage wording preference

These remain hold or promotion-gate material, not wording-only patch material.

## 4. patch class

If eligible, classify the patch:

| patch class | meaning | allowed scope |
|---|---|---|
| boundary clarification | clarifies what the panel is not | support note or label wording only |
| scenario inclusion clarification | clarifies that a panel covers follow-up or reprocess as already allowed by baseline | title, summary, or support note wording only |
| visual-only disclaimer strengthening | clarifies that a strip, selector, or trace hint is not runtime behavior | local copy only |
| role separation strengthening | clarifies request / return / reflux or surface role | local copy only |

No class may add new behavior.

## 5. review checklist

Before applying a wording-only patch, answer:

- Does this preserve the current central panel?
- Does this preserve request / return / reflux separation?
- Does this preserve user / VectorFL / engine role separation?
- Does this avoid selected-object behavior?
- Does this avoid trace UI?
- Does this avoid runtime truth?
- Does this avoid extension promotion?
- Does this avoid read-map or manifest changes?
- Is this based on repeated observation rather than speculation?

If any answer is no, do not patch.

## 6. approval threshold

Default threshold:

- two observations of the same confusion in the same scenario family

Stronger threshold:

- one observation in two different scenario families

Emergency threshold:

- one observation that blocks scenario reading while structure otherwise remains correct

Current status:

- no wording candidate is promoted yet
- all known candidates remain observation candidates

## 7. allowed output after gate passes

If the gate passes, the next package may produce:

- a wording-only patch plan
- affected file list
- before/after copy candidates
- self-check against baseline

The next package still must not automatically apply the patch unless the user asks for implementation.

## 8. disallowed output

The gate must not produce:

- new panel design
- new manifest fields
- read-map changes
- selected-object model
- trace UI
- runtime binding
- extension promotion
- broad copy rewrite across all surfaces

## 9. closeout sentence

Wording patches are allowed only after repeated use observation proves that phrasing, not structure, is causing confusion.
