# Expected Gemini Gap-scan Return Shape

status: RETURN_SHAPE_CONTRACT_WITH_HOLD
real_gemini_execution: NO
approval_applied: no
promotion_status: HOLD

Gemini must return:

```text
verdict:
assets_read:
finding_table:
best_mappings:
missing_guards:
weak_boundaries:
user_surface_suggestions:
candidate_only_material:
STOP:
WATCH:
HOLD:
recommended_next_smallest_action:
```

Allowed verdict examples:

```text
GEMINI_GAP_SCAN_RETURNED_CANDIDATE_MATERIAL_WITH_HOLD
GEMINI_GAP_SCAN_RETURNED_WATCH_ITEMS_WITH_HOLD
GEMINI_GAP_SCAN_OUTPUT_REQUIRES_HOLD_STOP_REVIEW
```

Not allowed:

```text
IMPLEMENTED
APPROVED
PROMOTED
M4_CONFIRMED
PROGRAM_ALPHA_READY
AUTHORITY_UPDATED
```
