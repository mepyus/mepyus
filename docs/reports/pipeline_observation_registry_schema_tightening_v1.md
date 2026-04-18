# pipeline observation registry schema tightening v1

## 0. Verdict

**PASS**

## 1. Schema change summary

The registry was kept observation-only, but the observation surface was made thinner and more structured for future promotion judgment.

New fields for future entries:

- `candidate_name`
- `family`
- `mode`
- `first_read_ref`
- `selected_artifact_group`
- `next_hop`
- `drift_risk_present`
- `guard_action_present`
- `observation_source`
- `observation_timestamp`
- `promotion_status`
- `not_promoted_reason`

What changed operationally:

- legacy rows remain in place
- new entries are written from the preflight decision itself
- `family`, `mode`, `first_read_ref`, `selected_artifact_group`, and `next_hop` are now explicit enough to inspect repeatability without promoting the path

## 2. Sample observation entries

### 2.1 Legacy observation row

- `candidate_name=raw_to_first_pass_to_report`
- `mode=reflection`
- `observation_count=6`
- `repeated_on=[saltlux_ai, ontology_youtube, choi_ai_classroom_vlm, enterprise]`
- `not_promoted_reason=observation only; raw -> first-pass -> report remains a candidate rather than a locked pipeline`

This row is still useful as count evidence, but it lacks the newly desired family/first-read structure.

### 2.2 Structured observation row

- `candidate_name=raw_to_first_pass_to_report`
- `family=andrej_karpathy_youtube`
- `mode=space_reading`
- `first_read_ref=inputs/external_cases/andrej_karpathy_youtube.txt`
- `selected_artifact_group=raw_external_cases`
- `next_hop=inputs/external_cases/andrej_karpathy_youtube.txt`
- `drift_risk_present=true`
- `guard_action_present=true`
- `promotion_status=observation`

This row is the new minimal observation shape. It makes future promotion review easier without changing status.

## 3. Why this is still observation-only

- The registry now shows *what repeats* and *under which gate conditions*, but it still does not claim the path is stable enough to lock.
- The candidate remains observation-only because:
  - no failure-family pass has been added yet
  - no divergent mode set has been promoted
  - no explicit promotion threshold has been met

## 4. Next minimal step

- Keep appending structured observation rows from the same runtime preflight entrypoint.
- If a future family demonstrates the same path under different mode conditions without drift failures, then revisit promotion.

