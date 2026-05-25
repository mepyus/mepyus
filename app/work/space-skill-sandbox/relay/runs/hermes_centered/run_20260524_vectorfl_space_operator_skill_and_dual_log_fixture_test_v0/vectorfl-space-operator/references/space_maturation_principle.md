# Space Maturation Principle

Use this reference when Codex is asked to judge how a Hermes execution, reentry record, new input, or space check should be remembered by the VectorFL space.

## Role Boundary

Hermes owns execution operation:
- preserve original input
- request space when needed
- merge original + space + model reasoning
- execute or hold
- write trace, receipt, and reentry

Codex owns space operation:
- observe current space
- classify input/reentry
- compare against current patterns and boundaries
- judge space delta
- decide whether Gemini is needed
- write HOLD-only maturation proposal and validation

Execution produces results. Space operation decides how results should be remembered.

## Maturation Loop

Follow this loop for every maturation pass:

1. `OBSERVE`
2. `CLASSIFY`
3. `COMPARE`
4. `JUDGE_SPACE_DELTA`
5. `DECIDE_GEMINI`
6. `PROPOSE_MATURATION`
7. `VERIFY`
8. `RETURN`

## Judgment Types

Choose one primary judgment:

- `NO_SPACE_DELTA`
- `REFERENCE_ONLY`
- `STRENGTHEN_EXISTING_PATTERN`
- `NEW_PATTERN_CANDIDATE`
- `LAYER_REASSIGNMENT_CANDIDATE`
- `STALE_OR_SUPERSEDED_HANDLE`
- `MISSING_HANDLE`
- `BOUNDARY_RISK`

## Gemini Rule

Default: do not call Gemini.

Use Gemini only when bounded files are insufficient and layer ambiguity, semantic flattening, stale/current separation, or multi-arc impact remains unresolved.

Gemini output is evidence only. Codex remains responsible for judgment.

## Minimum Return Fields

- `packet_id`
- `role`
- `read_files`
- `input_classification`
- `space_state_before`
- `comparison_basis`
- `space_delta_judgment`
- `maturation_decision`
- `gemini_exploration_decision`
- `proposed_space_changes_hold_only`
- `stale_or_superseded_handles_hold_only`
- `missing_handles`
- `boundary`
- `validation`
- `next_safe_lane`
- `promotion_status`

## Current Baseline

When available, read the full-history pattern index first. Current baseline patterns are:

1. no-call recovery and current-position surface
2. prototype behavior loop
3. Phase2 function position stack
4. Phase3 structure relayering
5. Hermes-centered Codex space loop
6. provider-call budget governance
7. external space lens stack
8. space-operator governance and channel

## Boundary

Do not mutate source, authority, current-position, registry, folder tree, or promotion state. Default promotion status is `HOLD`.
