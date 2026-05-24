# Codex Recovery Over Gemini Lite Return

## verdict

```text
CODEX_RECOVERY_OVER_REAL_GEMINI_LITE_RETURNED_WITH_WATCH_NO_PROMOTION
```

## output_shape_validity

```text
shape_validity: valid_with_watch
format: GEMINI_BULK_REVIEW_LITE_V0
status: returned_with_watch
required_sections_present: yes
negative_evidence_present: yes
receipt_conflict_check_present: yes
raw_audit_trigger_present: yes
stop_flags_present: yes
stop_flags: none
promotion_status: no promotion
```

The Gemini lite output is valid as bounded recovery evidence. It is not truth, approval, a component, a workflow/schema/registry/ontology/baseline, or promotion authority.

## normalized_watch

```text
1. Gemini uncertainty "Real Gemini execution remains unverified in all observed receipts" is normalized as prior-receipt-scoped. The Option 2 Hermes receipt records real_gemini_executed: true for the Gemini-only run, while the observed earlier receipts did not.
2. Gemini raw_limits phrase "model_api_transport_only for Codex CLI" is normalized to "model_api_transport_only for Gemini CLI" for the Option 2 context.
3. Option 1 success proves bounded real Codex-only recovery execution, not Gemini bridge validation.
4. Option 2 success proves bounded real Gemini-only lite output execution, not combined Codex+Gemini bridge validation.
5. Gemini lite output remains evidence for Codex recovery only and must not be promoted or treated as truth.
```

## bridge_readiness

```text
separate_option1_codex_only_success: yes
separate_option2_gemini_only_success: yes
codex_recovery_over_option2_completed: yes
ready_for_bounded_combined_bridge_rehearsal_attempt: yes_with_holds
ready_for_promotion: no
```

The separate Option 1 and Option 2 runs are sufficient to attempt one bounded combined bridge rehearsal, provided the rehearsal has a concrete approved request, exact declared inputs and outputs, explicit model API transport scope, no live web/source lookup, no external connector, no authority mutation, and no promotion.

## recovery_class_hint

```text
candidate
```

## HOLD

```text
new Gemini execution unless separately approved
combined bridge execution unless separately approved
live web/source lookup
external connector
memory/skill/cron/config mutation
VectorFL authority mutation
AGENTS.md / SKILL.md / current-position / output_manifest update
baseline / workflow / schema / registry / ontology / component promotion
```

## next_smallest_action

```text
Prepare one concrete bounded combined bridge rehearsal request that names exact declared inputs, exact output path, Codex and Gemini CLI/model transport scope, receipt requirements, recovery requirements, HOLD items, and promotion=no; then run only that approved rehearsal lane if separately authorized.
```
