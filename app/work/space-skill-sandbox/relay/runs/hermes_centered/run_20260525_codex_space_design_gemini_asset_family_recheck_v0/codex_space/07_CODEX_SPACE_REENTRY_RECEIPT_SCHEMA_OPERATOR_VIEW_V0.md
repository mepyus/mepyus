# Codex space reentry receipt schema operator view v0

Status: SCHEMA_CANDIDATE_HOLD_NOT_AUTHORITY

## Why This Exists

Hermes and Codex must not read the same artifact in the same way.

Hermes closeout answers:

```text
What was executed or withheld?
What files were produced?
What validation passed?
Where did execution stop?
```

Codex reentry receipt answers:

```text
What did that execution touch in space?
Which asset families did it connect?
Which pointer graph edges did it use or risk?
What should be remembered as HOLD-only?
What must not become authority?
```

## Required Split

Every future Hermes result received by Codex should separate:

```text
execution result
from
space effect
```

This prevents a run pass, validation pass, or closeout from becoming false authority.

## Minimum Receipt Sections

```text
input_reentry
  where the Hermes result came from

cross_read_records
  exact handles read, sha, owner namespace, read-only assertion

space_baseline_before
  current pointer graph and active hard HOLD

space_contact
  families touched, pointer edges touched, refs used

execution_to_space_split
  Hermes execution summary vs Codex space reading

space_effect_classification
  no effect, evidence, strengthened pattern, new candidate, risk, etc.

risk_hold_map
  what remains blocked

gap_map
  missing handles for future operation

stale_or_duplicate_pressure
  duplicate/stale/confusion pressure

maturation_decision
  HOLD-only memory proposal

next_actions
  who can do what next, with side-effect level

validation
  required fields, blocked edge checks, negative tests

mutation_statement
  all false unless separately approved
```

## Fields Codex Must Always Ask For

```text
source_execution_id
hermes_run_dir
hermes_reentry_handle
hermes_reentry_sha256
original_input_handle
space_refs_used_by_hermes
families_touched
pointer_graph_edges_touched
hermes_execution_summary
codex_space_reading_summary
what_is_execution_result
what_is_space_effect
what_must_not_be_promoted
primary_effect_type
risk_hold_map
gap_map
mutation_statement
promotion_status
```

## Effect Types

Codex should classify space effect as one of:

```text
NO_SPACE_EFFECT
REFERENCE_EVIDENCE
PATTERN_CONFIRMED
PATTERN_STRENGTHENED
PATTERN_CHANGED
NEW_PATTERN_CANDIDATE
MISSING_HANDLE_EXPOSED
STALE_OR_SUPERSEDED_EFFECT
DUPLICATE_PRESSURE
BOUNDARY_RISK
REENTRY_REPAIR_NEEDED
```

## Mandatory Negative Tests

```text
NEG_EXECUTION_RESULT_AS_AUTHORITY
NEG_PACKET_EDGE_AS_LIVE_CALL_SCOPE
NEG_RUN_BUNDLE_AS_CLEANUP_APPROVAL
NEG_POINTER_GRAPH_AS_SOURCE_OF_TRUTH
NEG_MATURED_AS_AUTHORITY
```

## What This Schema Does Not Do

```text
It does not approve execution.
It does not approve live Codex/Gemini/API call.
It does not move files.
It does not delete files.
It does not archive files.
It does not edit source.
It does not change registry/current-position.
It does not promote anything.
```

## Next Safe Lane

```text
USE_THIS_SCHEMA_ON_NEXT_HERMES_REENTRY_DRY_RUN_HOLD_ONLY
```

That means: when a future Hermes closeout appears, Codex can test this schema on it in read-only mode.

Final status:

```text
HOLD_NOT_AUTHORITY
```
