# Phase 1.28 Flow-Aware Logging Examples v0

## Purpose

These examples show how to write bounded reopen evidence logs.

The examples are not new judgments.
They only show the correct storage and wording discipline.

## Good Example 1: `general_line_vs_flow`

Filename:

- `20260422_general_line_vs_flow_middle_case_pressure_family_recheck_v1.md`

Body:

```md
### Flow-Aware Reopen Evidence Log

- family: general_line_vs_flow
- current_placement: default-sufficient with unresolved pressure
- trigger_type: repeated middle-case evidence
- evidence_summary: three new bounded reread checks show thin flow survival while default repeatedly misses the narrower slice
- repeated_evidence: yes; same pattern appeared across multiple local reread checks
- contradiction_against_current_rule: yes; current default placement may now be too coarse for this family
- carry_forward_class_relevance: stable but low-value, with possible drift toward actual reroute usefulness
- requested_reopen_scope: family only
- requested_reopen_depth: placement recheck only
- why_broad_reopen_is_not_needed: the pressure is bounded to one family and does not challenge the current allow-list or block-list
- reviewer_operator_note: reopen only to test whether this family now deserves a conditional-only slot
```

Why this is good:

- bounded to one family
- bounded reopen depth is explicit
- broad reopen is explicitly denied

## Good Example 2: `input_layer_wrapper`

Filename:

- `20260422_input_layer_wrapper_carry_forward_drift_protection_recheck_v1.md`

Body:

```md
### Flow-Aware Reopen Evidence Log

- family: input_layer_wrapper
- current_placement: protect as default-sufficient
- trigger_type: carry_forward classification drift
- evidence_summary: recent bounded reread checks show carry-forward behaving closer to actual reroute handle than stable low-value handle
- repeated_evidence: yes; same drift appeared across repeated family-local checks
- contradiction_against_current_rule: yes; current protection rule may now be too strong
- carry_forward_class_relevance: possible shift from stable but low-value handle toward actual reroute handle
- requested_reopen_scope: family only
- requested_reopen_depth: protection rule check only
- why_broad_reopen_is_not_needed: this does not affect block-list, allow-list, or global default outside this family
- reviewer_operator_note: confirm whether protection should remain or whether bounded flow-aware eligibility now exists
```

Why this is good:

- stays inside protected-default review
- does not jump straight to allow-list rewrite

## Bad Example: Broad Reopen Framing

Filename:

- `20260422_flow_reopen_master_rethink_v1.md`

Bad body:

```md
### Flow-Aware Reopen Evidence Log

- family: multiple
- current_placement: mixed
- trigger_type: unresolved pressure
- evidence_summary: several families still feel uncertain, so the whole flow-aware rule should be revisited
- repeated_evidence: maybe
- contradiction_against_current_rule: unclear
- carry_forward_class_relevance: mixed
- requested_reopen_scope: global
- requested_reopen_depth: broad tuning restart
- why_broad_reopen_is_not_needed: not applicable
- reviewer_operator_note: reopen the whole heuristic and re-evaluate everything
```

Why this is bad:

- uses unresolved pressure as tuning permission
- asks for global reopen
- does not keep family or bucket scope bounded
- turns the evidence log into a re-argument document

This format is not allowed.
