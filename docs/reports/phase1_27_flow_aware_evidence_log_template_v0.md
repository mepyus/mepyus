# Phase 1.27 Flow-Aware Evidence Log Template v0

## Purpose

This template is for bounded reopen requests only.

It is not a re-argument document.
It is not a broad tuning request.

Write it only when trigger evidence exists.

## When To Use

Use this template only when:

- a trigger in the current checklist is actually met
- the reopen target is bounded to a family or bucket
- the current placement may no longer be honest enough

Do not use it when:

- no trigger exists
- the request is just exploratory
- broad tuning is being proposed

## Required Fields

| Field | Required meaning |
| --- | --- |
| `family` | affected family or bucket |
| `current_placement` | current operating placement |
| `trigger_type` | specific trigger type that fired |
| `evidence_summary` | short factual summary of the new evidence |
| `repeated_evidence` | yes/no plus short note |
| `contradiction_against_current_rule` | yes/no plus short note |
| `carry_forward_class_relevance` | actual reroute / stable low-value / mostly formal / none |
| `requested_reopen_scope` | family only / bucket only |
| `requested_reopen_depth` | placement recheck only / family-local reread only / conditional bucket check only |
| `why_broad_reopen_is_not_needed` | short statement limiting scope |
| `reviewer_operator_note` | bounded note from operator or reviewer |

## Template Block

```md
### Flow-Aware Reopen Evidence Log

- family:
- current_placement:
- trigger_type:
- evidence_summary:
- repeated_evidence:
- contradiction_against_current_rule:
- carry_forward_class_relevance:
- requested_reopen_scope:
- requested_reopen_depth:
- why_broad_reopen_is_not_needed:
- reviewer_operator_note:
```

## Example 1: `general_line_vs_flow`

```md
### Flow-Aware Reopen Evidence Log

- family: general_line_vs_flow
- current_placement: default-sufficient with unresolved pressure
- trigger_type: repeated middle-case evidence
- evidence_summary: three new local samples show thin flow surviving while default repeatedly misses the narrower slice
- repeated_evidence: yes; same pattern appeared across three bounded reread notes
- contradiction_against_current_rule: yes; current default placement may be too coarse for this family
- carry_forward_class_relevance: stable but low-value, with possible drift toward actual reroute usefulness
- requested_reopen_scope: family only
- requested_reopen_depth: placement recheck only
- why_broad_reopen_is_not_needed: the issue is bounded to one family and does not challenge the current allow-list or block-list
- reviewer_operator_note: reopen only to test whether this family now justifies a conditional-only slot
```

## Example 2: `raw_intake_gap`

```md
### Flow-Aware Reopen Evidence Log

- family: raw_intake_gap
- current_placement: keep default-sufficient
- trigger_type: repeated contradiction against current default rule
- evidence_summary: new reread outputs show boundary remains weak while flow-aware adds repeated noise pressure toward a more restrictive placement
- repeated_evidence: yes; same overreach shape appeared across multiple bounded reread checks
- contradiction_against_current_rule: yes; current default may no longer be the most honest description
- carry_forward_class_relevance: mostly formal ref
- requested_reopen_scope: family only
- requested_reopen_depth: placement recheck only
- why_broad_reopen_is_not_needed: no other family is affected and current global rule does not need revision
- reviewer_operator_note: only check whether this family should move closer to block-list
```

## Evidence Log Guard

This template permits only bounded reopen requests.

It must not be used to request:

- global heuristic rewrite
- allow-list / block-list overhaul
- emitter rewrite
- classifier rewrite
- broad tuning restart
