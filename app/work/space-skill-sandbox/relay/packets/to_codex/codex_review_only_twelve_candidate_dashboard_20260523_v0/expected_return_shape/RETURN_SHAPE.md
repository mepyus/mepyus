# Expected Codex Review-only Return Shape

status: RETURN_SHAPE_CONTRACT_WITH_HOLD
real_codex_execution: NO
approval_applied: no
promotion_status: HOLD

Codex must return:

```text
verdict:
read_before_work:
files_touched:
commands_run:
receipts_created_or_updated:
state_mutations_observed:
WATCH:
HOLD:
overclaim_findings:
missing_evidence:
next_smallest_action:
```

Expected safe verdict examples:

```text
PASS_REVIEW_ONLY_WITH_HOLD
HOLD_STOP_REVIEW_FOR_OVERCLAIM_LANGUAGE
STOP_FOR_AUTHORITY_OR_PROMOTION_DRIFT
```

Not allowed:

```text
PROMOTED
APPROVED
M4_CONFIRMED
PROGRAM_ALPHA_READY
AUTHORITY_UPDATED
```
