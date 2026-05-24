# Gemini Worker Return / Packaging Records Return Packaging v0

## Status

```yaml
status: gemini_return_packaging
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
current_position_update: false
source_return: user_pasted_gemini_result
verdict: PASS_WITH_DOWNSHIFT_AS_CANDIDATE_PACKAGING_SETTING_MATERIAL
```

## Source

Gemini returned:

```text
PLAN_BASIS
WORKER_RETURN_SHAPE_CANDIDATE
RAW_TRACE_BOUNDARY
RECOVERY_RULES
HOLD_AND_WATCH
MICRO_RUN_PREVENTION
ROLE_SPLIT
RETURN_TO_SPACE_VALUE
MOVEMENT_RECORD_CANDIDATE
DO_NOT_PROMOTE
NEXT_USE
```

Declared:

```text
STATUS: GEMINI_WORKER_RETURN_PACKAGING_RECORDS_SYNTHESIS_COMPLETE
POSITION_VALUE: PV_RETURN_TO_SPACE_CLOSEOUT
LACL: CANDIDATE_OPERATING_SETTING
```

## File Presence Check

Gemini cited these files. Codex verified only presence, not full content in this recovery pass:

```text
docs/specs/integrated_engine_worker_return_contract_v0.md: present
docs/specs/integrated_engine_worker_return_normalization_policy_v0.md: present
docs/specs/package_record_minimum_v0.md: present
```

## Accepted Values

Accepted as candidate packaging-setting material:

```text
worker return must expose worker role, input purpose, anchors used, behavior change, tool output summary, evidence pointers, not-inspected scope, watch items, Return-to-Space candidate, and do-not-promote boundaries.
raw worker prose / logs / QMD metadata / snippets / unread claims remain raw trace.
Codex recovery should downshift claims, separate evidence/gap, extract reusable judgment, classify HOLD vs WATCH, and write one package-level Movement Record only when useful.
micro-run proliferation should be prevented by one broad-bounded external carrier return and one Codex recovery pass.
```

## Downshift Corrections

Gemini wording:

```text
Normalization policies are confirmed as the correct foundation.
```

Downshift:

```text
Normalization policies are candidate source anchors for future worker-return handling; this pass did not revalidate them as the correct foundation.
```

Gemini wording:

```text
package_record_minimum_v0 is a sufficient handle for cross-phase continuity.
```

Downshift:

```text
package_record_minimum_v0 is a candidate handle for cross-phase continuity; sufficiency remains watch until applied in a real package.
```

Gemini wording:

```text
The candidate shape effectively separates raw trace from candidate judgment.
```

Downshift:

```text
The candidate shape is useful for separating raw trace from candidate judgment, but it is not a schema or mandatory contract.
```

## Candidate Worker Return Shape

Use as a candidate shape only:

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

## Recovery Rule

```text
Worker return enters VectorFL only after Codex recovery.
Codex recovery must produce reusable judgment or leave the return as raw trace.
One broad-bounded package should produce at most one package-level Movement Record.
```

## Hold / Watch

Hold:

```text
authority_claim_hold
schema_or_automation_hold
full_corpus_indexing_hold
baseline_or_registry_claim_hold
```

Watch:

```text
thin_anchor_usage_trace_watch
missing_not_inspected_scope_watch
micro_run_proliferation_watch
raw_trace_memory_promotion_watch
package_record_sufficiency_watch
```

## Return-to-Space Value

Recoverable material:

```text
Gemini compressed Worker Return / Packaging Records into a candidate return shape and recovery rule set.
```

Reusable judgment:

```text
Future external worker returns should be broad-bounded, expose anchor usage and not-inspected scope, and be recovered by Codex in one package-level pass.
```

Operational correction:

```text
Do not turn the worker return shape into schema or automation; keep it as a packaging discipline.
```

Future reuse note:

```text
Use this candidate shape when preparing the next Gemini instruction or reviewing a user-pasted external worker return.
```

## Do Not

```text
do not promote to baseline
do not create schema/parser/automation
do not update current position
do not treat worker output as memory
do not treat Gemini synthesis as authority
```

`STATUS: GEMINI_WORKER_RETURN_PACKAGING_RECORDS_RETURN_PACKAGED_WITH_DOWNSHIFT`
