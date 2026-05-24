# Gemini Instruction - Package A: Worker Return Intake Hardening v0

## Mission

You are acting as an external execution carrier for VectorFL.

Do not create micro-runs.
Do not return result per session.
Perform 10 internal sessions (A01-A10) in one broad-but-bounded pass and return one packaged result.

## Operating Principle

```text
Plan from Space, not from Model Default.
```

VectorFL Space is the memory / judgment / recovery body.
The goal of this package is to harden the intake shape for worker returns.

## Current Operating Setting

- External carrier: broad-but-bounded synthesis
- Codex: anchor broker / recovery editor
- User: direction judge

## Space Anchors To Use

Primary anchors:

- `docs/specs/integrated_engine_worker_return_contract_v0.md`
- `docs/specs/integrated_engine_worker_return_normalization_policy_v0.md`
- `docs/specs/package_record_minimum_v0.md`
- `app/work/space-skill-sandbox/outputs/movement_record_worker_return_shape_application_recovery_v0.md`
- `app/work/space-skill-sandbox/outputs/movement_record_worker_return_shape_weak_failure_application_recovery_v0.md`
- `app/work/space-skill-sandbox/outputs/worker_return_packaging_candidate_setting_compact_v0.md`

## Package A - Session List

Execute these 10 sessions internally:

- **A01 - Intake Shape Regrounding**: Restate the 10-field shape from space anchors. Verify no schema/baseline wording.
- **A02 - Success Case Mapping**: Apply shape to a successful external return. Confirm anchors_used and Return-to-Space candidate presence.
- **A03 - Empty Failure HOLD**: Apply shape to an empty/silent return. Classify HOLD without inferring meaning.
- **A04 - Partial Non-Empty WATCH**: Apply shape to a partial but usable return. Identify thin anchor trace. Classify WATCH with downshift.
- **A05 - Mixed Claim Priority**: Evaluate a return with useful content plus overclaim wording. Apply HOLD/WATCH priority rule.
- **A06 - Not-Inspected Disclosure Drill**: Separate disclosed gap vs hidden critical gap. Classify examples.
- **A07 - Anchor Usage Trace Drill**: Require `how_anchors_changed_behavior`. Compare mention-only vs behavior-changing trace.
- **A08 - Return-to-Space Extraction**: Produce 3-7 reusable judgment bullets. Reject raw prose/logs as memory.
- **A09 - Micro-Run Prevention Gate**: Enforce one package-level record. Convert any internal micro-run thoughts into one package return.
- **A10 - Package Closeout**: Synthesize A01-A09. Confirm candidate-only status.

## Required Return Shape

Return exactly one package-level result with these sections:

```text
PLAN_BASIS
PACKAGE_A_SESSION_SUMMARY
WORKER_RETURN_INTAKE_PACKAGE_RETURN
HOLD_WATCH_PRIORITY_TABLE
RETURN_TO_SPACE_VALUE
MOVEMENT_RECORD_CANDIDATE
DO_NOT_PROMOTE
NEXT_USE
```

### WORKER_RETURN_INTAKE_PACKAGE_RETURN

This section must include the final hardened 10-field candidate shape:

```yaml
worker_role:
input_purpose:
anchors_used:
how_anchors_changed_behavior:
tool_output_summary:
evidence_pointers:
not_inspected_scope:
issues_or_watch_items:
return_to_space_value_candidate:
do_not_promote:
```

## Stop Conditions

Stop and return HOLD if:
- authority/baseline/schema/automation claims appear.
- Return-to-Space Value is absent.
- full corpus indexing is requested.
- micro-run splitting begins.

## Style Constraints

Be concise.
Do not expand into philosophy.
Do not call the result final or baseline.

`STATUS: GEMINI_PACKAGE_A_WORKER_RETURN_INTAKE_HARDENING_INSTRUCTION_PREPARED`
