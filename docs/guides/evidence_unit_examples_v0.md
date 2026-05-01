# Evidence Unit Examples v0

## Purpose

Examples for reading grounded evidence units produced by Phase 1.6.

## Example: Pointer Only

```json
{
  "source_ref": "runtime/views/example_latest.md",
  "pointer": "runtime/views/example_latest.md",
  "excerpt_window": "",
  "excerpt_mode": "pointer_only",
  "why_it_matters": "Generated view may contain current state but was not read deeply.",
  "relation_type": "weak_candidate",
  "local_confidence": "low",
  "grounding_status": "pointer_only"
}
```

Use when the file exists as a possible source but no bounded local excerpt was extracted.

## Example: Weak Grounded

```json
{
  "source_ref": "docs/guides/question_type_to_search_path_map_v0.md",
  "pointer": "docs/guides/question_type_to_search_path_map_v0.md:L1-L20",
  "excerpt_window": "Question Type To Search Path Map v0 ...",
  "excerpt_mode": "heading_plus_block",
  "why_it_matters": "The excerpt identifies this as a search path guide.",
  "relation_type": "contextual_support",
  "local_confidence": "medium",
  "grounding_status": "weak_grounded"
}
```

Use when the excerpt is useful context but not enough for strong merge.

## Example: Direct Grounded

```json
{
  "source_ref": "docs/specs/source_authority_ladder_v0.md",
  "pointer": "docs/specs/source_authority_ladder_v0.md:L24-L36",
  "excerpt_window": "Conflict handling ... If two high-authority sources conflict, mark HOLD ...",
  "excerpt_mode": "heading_plus_block",
  "why_it_matters": "The excerpt directly defines hold behavior for authority conflict.",
  "relation_type": "direct_support",
  "local_confidence": "high",
  "grounding_status": "direct_grounded"
}
```

Use when the excerpt directly supports the claim.

## Example: Cross Supported

```json
{
  "source_ref": "docs/specs/evidence_merge_diff_hold_contract_v0.md",
  "pointer": "docs/specs/evidence_merge_diff_hold_contract_v0.md:L20-L36",
  "excerpt_window": "Allowed chosen_mode values ... merge diff hold ...",
  "excerpt_mode": "heading_plus_block",
  "why_it_matters": "The excerpt defines mode vocabulary and is reinforced by decision gate rules.",
  "relation_type": "direct_support",
  "local_confidence": "high",
  "cross_support_refs": ["docs/specs/phase1_5_decision_gate_rules_v0.md"],
  "grounding_status": "cross_supported"
}
```

Use when multiple bounded excerpts support the same operating decision.

## Validation

Evidence examples remain small, inspectable, and compatible with v0 fields.
