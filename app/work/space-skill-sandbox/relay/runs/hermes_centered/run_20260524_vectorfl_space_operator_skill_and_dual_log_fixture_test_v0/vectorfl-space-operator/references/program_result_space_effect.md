# Program Result Space Effect

Use this reference when checking a function, script, fixture, or program result. A local pass/fail result is not enough. Codex must inspect how the result behaves inside the VectorFL space.

## Core Question

Ask:

What does this program result do to the space?

Separate:

1. `PROGRAM_BEHAVIOR`
2. `EXECUTION_TRACE`
3. `SPACE_CONTACT`
4. `SPACE_EFFECT`
5. `MATURATION_DECISION`

## Effect Types

Choose one primary `space_effect_type`:

- `NO_SPACE_EFFECT`
- `REFERENCE_EVIDENCE`
- `PATTERN_CONFIRMED`
- `PATTERN_STRENGTHENED`
- `PATTERN_CHANGED`
- `NEW_PATTERN_CANDIDATE`
- `MISSING_HANDLE_EXPOSED`
- `STALE_OR_SUPERSEDED_EFFECT`
- `DUPLICATE_PRESSURE`
- `BOUNDARY_RISK`
- `REENTRY_REPAIR_NEEDED`

## Inspection Checklist

Answer these before considering the function check complete:

- Which input triggered the program result?
- Which space baseline was active before the result?
- Which existing pattern did the result touch?
- Which files or handles did the result read?
- Which files or handles did the result write?
- Did it write only to the owner namespace?
- What is the local pass/fail result?
- What is the space effect type?
- Did it create a missing handle?
- Did it create stale or duplicate pressure?
- Is Gemini needed to inspect wider space effects?
- What should be remembered as HOLD-only?
- What must not be promoted?

## Minimum Return Fields

- `packet_id`
- `role`
- `program_result_under_test`
- `space_baseline_before`
- `space_contacts`
- `local_execution_result`
- `space_effect_type`
- `space_effect_reasoning`
- `touched_patterns`
- `missing_handles`
- `stale_or_duplicate_pressure`
- `gemini_exploration_decision`
- `maturation_decision`
- `proposed_space_changes_hold_only`
- `boundary`
- `validation`
- `next_safe_lane`
- `promotion_status`

## Boundary

A passing test does not become authority. Keep source, authority, current-position, registry, and folder tree unchanged unless a separate explicit approved lane exists.
