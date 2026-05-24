# QMD Gate Anchor Application to Gemini Anchor Request Review v0

## Status

```yaml
status: codex_review_using_qmd_retrieved_gate_anchors
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
qmd_runtime_executed_for_this_review: false
verdict: PASS_WITH_WATCH_AS_GATE_ANCHOR_APPLICATION_TRIAL
```

## Purpose

Apply the gate-spec anchors surfaced by QMD subset 002 to a real Gemini external-tool return, without treating QMD as reviewer, authority, schema, or automation.

## Reviewed External Return

```text
app/work/space-skill-sandbox/relay/outbox/space_loop_test_001_anchor_request_20260507_gemini_outbox_20260507_180852.md
```

Return type:

```text
EXTERNAL_TOOL_INTERPRETATION
ANCHOR_REQUEST
STOP_BEFORE_EXECUTION
```

## Gate Anchors Used

Retrieved in QMD subset 002:

```text
qmd://vectorfl_subset002_gate_specs/external-tool-plan-prompt-wrapper-v0.md
qmd://vectorfl_subset002_gate_specs/anchor-stack-gate-checklist-v0.md
```

Actual source paths:

```text
docs/specs/external_tool_plan_prompt_wrapper_v0.md
docs/specs/anchor_stack_gate_checklist_v0.md
```

Use boundary:

```text
QMD surfaced the candidate pointers.
Codex applied the judgment.
```

## Gate Review

| gate | pass / hold | evidence |
| --- | --- | --- |
| Pre-Plan Gate | PASS_WITH_WATCH | Gemini stated user purpose, work type, needed material families, PVs, LACL signals, expected surfaces, and unsafe inferences. |
| Plan Sizing Gate | HOLD_NOT_YET_APPLICABLE | Gemini stopped before plan; package sizing was not required yet. |
| Boundary Gate | PASS | Gemini explicitly stopped before execution and named unsafe inferences. |
| Runtime Re-Entry Gate | PASS_WITH_WATCH | Gemini requested Codex Anchor Packet before proceeding, which preserves space re-entry, but expected a Session Space Anchor and possible Line Asset Map updates that Codex must downshift. |
| Return-to-Space Gate | PASS_WITH_WATCH | Gemini named Movement Record compatibility and Return-to-Space Value, but no Movement Record was produced by Gemini itself because this was an Anchor Request phase. |

## Required Checks

```yaml
plan_basis_before_plan: pass_by_stop_before_plan
route_used: partial
canonical_pvs_used: pass_with_watch
broad_bounded_default: not_yet_applicable
blocking_split_reason_if_any: not_applicable
non_inspected_scope_stated: partial
hard_boundary_vs_watch_separated: pass
return_to_space_value_present: partial
authority_claim_absent: pass
```

## Review Notes

Pass signals:

```text
Gemini did not jump into design execution.
Gemini asked for anchors before planning.
Gemini identified PV_PLAN_BASIS_GATE and PV_RETURN_TO_SPACE_CLOSEOUT.
Gemini named unsafe authority inferences.
Gemini stopped before execution.
```

Watch signals:

```text
Gemini requested possible Line Asset Map updates; this must not imply source map mutation.
Gemini used "baseline movement rules" wording for stable operating anchors; this should be downshifted unless the source is actually baseline-locked.
Gemini expected a Session Space Anchor; Codex should provide an Anchor Packet rather than create or promote a new session anchor by default.
Non-inspected scope was implicit but not fully enumerated.
```

## Codex Packaging Decision

```yaml
accepted_values:
  - external tool can detect that anchors are needed before planning
  - anchor request can include material family / PV / LACL / expected return shape
  - stop-before-execution behavior is valid at pre-plan gate
corrections_needed:
  - downshift baseline wording
  - avoid automatic Line Asset Map updates
  - use Anchor Packet rather than creating a new Session Space Anchor by default
watch_items:
  - baseline_wording_watch
  - map_update_pressure_watch
  - anchor_packet_vs_session_anchor_watch
  - non_inspected_scope_thin_watch
route_updates: []
pv_updates: []
movement_record_update:
  - capture this as gate anchor application trial
```

## Return-to-Space Value

Recoverable material:

```text
The QMD-retrieved gate anchors are usable for reviewing a real external-tool Anchor Request.
```

Reusable judgment:

```text
A good external-tool pre-plan return may stop at ANCHOR_REQUEST rather than forcing PLAN_BASIS or PLAN. The gate check should distinguish "stopped before plan" from "missing plan basis after planning."
```

Issue / watch:

```text
External tool anchor requests may over-ask for new session anchors or map updates. Codex should downshift those into bounded Anchor Packet delivery unless explicit update work is approved.
```

Future reuse note:

```text
Use this review as a candidate example when checking whether an external tool requested space anchors instead of default-planning.
```

## Do Not

```text
do not treat QMD as reviewer
do not treat Gemini output as authority
do not create or update Line Asset Maps from this review
do not create a Session Space Anchor by default
do not promote this review to baseline
do not create parser/schema/automation
```

`STATUS: QMD_GATE_ANCHOR_APPLICATION_TO_GEMINI_ANCHOR_REQUEST_REVIEW_PREPARED`
