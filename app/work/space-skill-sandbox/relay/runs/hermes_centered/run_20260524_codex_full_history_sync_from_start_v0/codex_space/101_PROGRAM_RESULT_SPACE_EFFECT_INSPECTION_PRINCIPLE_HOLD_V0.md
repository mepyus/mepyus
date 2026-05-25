# PROGRAM_RESULT_SPACE_EFFECT_INSPECTION_PRINCIPLE_HOLD_V0

status: HOLD / inspection principle

purpose:
Extend Codex space maturation testing beyond the operating loop. A program can pass its local execution test while still producing unclear, stale, duplicated, or unsafe effects in the VectorFL space. Codex must inspect how program results behave as space material.

## 1. Core Question

For every program result, Codex asks:

What does this result do to the space?

The answer must be more specific than "the program passed" or "the program failed."

Codex should decide whether the result:
- confirms an existing pattern
- changes an existing pattern
- creates a new pattern candidate
- exposes a missing handle
- produces stale or superseded language
- creates duplicate artifacts
- creates authority/HOLD confusion
- needs reentry repair before maturation
- should remain reference-only
- has no meaningful space delta

## 2. Program Result Space Effect Model

Every functional check should separate five layers:

1. Program behavior
   What ran, what output was produced, and whether local validation passed.

2. Execution trace
   What Hermes or the local fixture says was selected, merged, executed, held, or returned.

3. Space contact
   Which space references, patterns, indexes, schemas, handles, or boundaries the result touched.

4. Space effect
   What changed in the interpretation of the space after the result.

5. Maturation decision
   What Codex proposes to remember, ignore, repair, or hold.

## 3. Result Effect Types

Codex should classify the result effect as one primary type:

- `NO_SPACE_EFFECT`
  The result is local-only and does not change reusable space understanding.

- `REFERENCE_EVIDENCE`
  The result should be kept as evidence but not indexed as a pattern.

- `PATTERN_CONFIRMED`
  The result confirms an existing pattern without changing it.

- `PATTERN_STRENGTHENED`
  The result adds useful evidence to an existing pattern.

- `PATTERN_CHANGED`
  The result changes how an existing pattern should be read.

- `NEW_PATTERN_CANDIDATE`
  The result creates a reusable operating structure not covered by the current index.

- `MISSING_HANDLE_EXPOSED`
  The result needs a new named handle, schema, pointer, or route.

- `STALE_OR_SUPERSEDED_EFFECT`
  The result makes older language historically valid but operationally stale.

- `DUPLICATE_PRESSURE`
  The result creates multiple artifacts with overlapping meaning.

- `BOUNDARY_RISK`
  The result risks treating HOLD/proposal/test output as authority.

- `REENTRY_REPAIR_NEEDED`
  The result cannot be matured because trace, receipt, source reference, or reentry fields are missing.

## 4. Functional Test Inspection Checklist

A function test is incomplete until these questions are answered:

- Which input triggered the program result?
- Which space baseline was active before the result?
- Which existing pattern did the result touch?
- Which files or handles did the result read?
- Which files or handles did the result write?
- Did it write only to the owner namespace?
- What is the local pass/fail result?
- What is the space effect type?
- Did it create a new missing handle?
- Did it create stale or duplicate pressure?
- Is Gemini needed to inspect wider space effects?
- What should be remembered as HOLD-only?
- What must not be promoted?

## 5. Gemini In This Inspection

Gemini is not needed for ordinary local pass/fail verification.

Gemini may be useful when the program result touches several patterns or when Codex cannot tell whether the result is:
- a new pattern
- a strengthened existing pattern
- duplicate pressure
- stale/superseded effect
- boundary risk

Gemini remains Codex-side evidence only.

## 6. Minimum Return Shape

Every program-result space-effect inspection should return:

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

## 7. Non-Negotiable Boundary

This inspection does not authorize:
- applying a result to authority
- mutating current-position
- mutating registry
- moving folders
- mutating source
- promoting a passing test into a space rule without approval

promotion_status: HOLD
