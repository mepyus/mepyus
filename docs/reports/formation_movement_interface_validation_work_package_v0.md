# Formation-Movement Interface Validation Work Package v0

## 0. package status

```yaml
package_name: formation_movement_interface_validation_work_package_v0
status: package_candidate
verdict: PASS_WITH_NOTE-ready
purpose: validate whether the formation-movement interface package stays lightweight and usable across real cases
lock_status: no_baseline_lock
implementation_status: no_implementation
schema_status: no_schema_enforcement
```

## 1. purpose of this package

This package records the validation checklist used to confirm that `docs/reports/formation_movement_interface_package_draft_v0.md` works in actual operating cases.

Core validation goals:

1. The package must not impose excessive input burden on the user.
2. Sidecar must behave as lifecycle-coupled support material, not enforced schema.
3. Prepare and execute must remain separate.
4. Validation return must not be misread as final result.
5. External reference, Codex one-shot, and user-surface explanation cases must all resist premature promotion.
6. Repeated validation must not silently upgrade the package into baseline lock.

## 2. full validation task list

### validation task 1. package document state check

Target:

`docs/reports/formation_movement_interface_package_draft_v0.md`

Checklist:

- [ ] status remains `package_candidate / PASS_WITH_NOTE-ready`
- [ ] no-lock warning remains
- [ ] baseline lock prohibition remains
- [ ] schema enforcement prohibition remains
- [ ] implementation / runtime manifest / validator creation prohibition remains
- [ ] Core 7 remains unchanged
- [ ] object family 5 remains unchanged
- [ ] addendum sections 21-24 exist

Validation criteria:

```yaml
PASS:
  - package_candidate status remains
  - no Core 7 change
  - no object family 5 change
  - no-lock / no-schema / no-implementation guardrails remain

PASS_WITH_NOTE:
  - structure remains but some wording risks reading like lock
  - addendum exists but operator-cost language is weak

HOLD:
  - package_candidate contains wording that reads like baseline
  - Core 7 is treated like enforced schema

FAIL:
  - baseline lock or schema enforcement is introduced
  - implementation / validator / runtime manifest is created
```

### validation task 2. Core 7 check

Target:

Core sidecar metadata 7 fields:

```yaml
object_type
current_purpose
boundary
provisional_status
next_allowed_move
reread_return_hook
source_trace
```

Checklist:

- [ ] Core 7 remains unchanged
- [ ] no new field is added to Core 7
- [ ] `unclassified`, `allowed_to_prepare`, `allowed_to_execute`, and `trust_scope_note` are not promoted into Core 7
- [ ] Core 7 is described as lifecycle-complete target, not creation-time required input
- [ ] seed sidecar does not require full Core 7

Validation criteria:

```yaml
PASS:
  - Core 7 remains
  - Core 7 is treated as lifecycle-complete target
  - seed stage requires only operational minimum

PASS_WITH_NOTE:
  - Core 7 remains but some wording reads like creation-time requirement

HOLD:
  - user is asked to fill full Core 7

FAIL:
  - Core 7 is expanded
  - Core 7 is used as enforced schema
```

### validation task 3. operational minimum check

Target:

Seed sidecar creation stage

Checklist:

- [ ] user fills about three fields at seed stage
- [ ] `current_purpose` exists
- [ ] `source_trace` exists
- [ ] `initial_boundary` or `why_now` exists
- [ ] `object_type` may be omitted or `unclassified`
- [ ] user does not choose `object_type`

Validation criteria:

```yaml
PASS:
  - user input stays near three fields
  - object_type is not user-selected
  - unclassified seed is allowed

PASS_WITH_NOTE:
  - user input remains light but object_type pressure still exists

HOLD:
  - seed stage pushes object_type confirmation

FAIL:
  - seed stage requires full Core 7
```

### validation task 4. sidecar maturity check

Target:

Sidecar lifecycle:

```yaml
seed_sidecar
formed_sidecar
motion_sidecar
return_sidecar
refined_sidecar
```

Checklist:

- [ ] sidecar is not treated as complete schema from the start
- [ ] seed sidecar centers on why the object exists and where it came from
- [ ] formed sidecar attaches `object_type` and `provisional_status` on VectorFL surface
- [ ] motion sidecar centers on `action_shape`, `guardrail`, and `expected_return_form`
- [ ] return sidecar centers on `observed_result`, `reread_trigger`, and `refinement_target`
- [ ] refined sidecar updates status, next move, and trust scope

Validation criteria:

```yaml
PASS:
  - sidecar matures with the object
  - each maturity stage has a distinct role

PASS_WITH_NOTE:
  - maturity stages exist but some stages blur together

HOLD:
  - seed stage asks for formed/motion fields

FAIL:
  - sidecar is treated as static schema
```

### validation task 5. surface-specific visibility check

Target:

User / VectorFL / Engine / Return surface visibility split

Checklist:

User Surface:

- [ ] only a 3-4 line judgment card is shown
- [ ] card follows this shape:

```text
current judgment:
reason:
next move:
guardrail:
```

VectorFL Surface:

- [ ] full formation sidecar is visible
- [ ] `object_type`, `provisional_status`, `boundary`, `candidate_role`, and `promotion_barrier` appear

Engine Surface:

- [ ] execution-oriented fields are centered
- [ ] `action_shape`, `execution_constraint`, `guardrail`, `expected_return_form`, `fallback_policy`, and `trust_scope` are central

Return / Validation Surface:

- [ ] next-branch orientation is shown instead of full result prose
- [ ] `observed_result`, `reread_trigger`, `recommended_branch`, and `refinement_target` appear

Validation criteria:

```yaml
PASS:
  - visibility is split by surface
  - user neither sees nor fills full sidecar

PASS_WITH_NOTE:
  - visibility is split but user summary is still slightly heavy

HOLD:
  - full sidecar is exposed to the user

FAIL:
  - every surface shows the same sidecar information
```

### validation task 6. prepare vs execute check

Target:

`next_allowed_move` interpretation

Checklist:

- [ ] `allowed_to_prepare` and `allowed_to_execute` remain distinct
- [ ] `prepare_worker_packet` is not misread as execution
- [ ] `allowed_to_execute` requires:

```yaml
execution_constraint
guardrail
fallback_policy
trust_scope
expected_return_form
reread_return_hook
```

- [ ] one-shot draft remains `bounded_action_candidate` by default
- [ ] guarded execution promotion conditions are explicit

Validation criteria:

```yaml
PASS:
  - prepare and execute are clearly separated
  - no execution happens from prepare state

PASS_WITH_NOTE:
  - separation exists but some wording still sounds executable

HOLD:
  - prepare_worker_packet is over-read as execution-ready

FAIL:
  - prepare state jumps directly to guarded_execution
```

### validation task 7. short / full validation return check

Target:

Validation return strength

Checklist:

- [ ] low-risk dry-runs can use short validation return
- [ ] short validation return contains:

```yaml
observed_result
reread_trigger
next_recommended_state
```

- [ ] full validation return triggers are explicit

Full triggers:

- [ ] promotion risk
- [ ] baseline risk
- [ ] schema enforcement risk
- [ ] runtime coupling risk
- [ ] boundary drift
- [ ] trust scope change
- [ ] object_type change
- [ ] R loss / flattening
- [ ] large gap between expected and actual return

Validation criteria:

```yaml
PASS:
  - short/full criteria are explicit
  - observed_result-only return is not treated as complete

PASS_WITH_NOTE:
  - criteria exist but some full-return triggers remain fuzzy

HOLD:
  - high-risk case still uses short return only

FAIL:
  - validation return is treated as final result
```

## 3. case-specific validation list

### case 1. Codex one-shot prepare validation

Target:

`docs/reports/formation_movement_interface_codex_oneshot_validation_case_v0.md`

Checklist:

- [ ] Codex one-shot is not executed directly
- [ ] it stays at `prepare_worker_packet`
- [ ] seed sidecar uses only operational minimum
- [ ] VectorFL assigns `object_type` at formed stage
- [ ] `allowed_to_prepare -> allowed_to_execute` is judged as HOLD
- [ ] user-filled fields stay near three
- [ ] User Surface remains a four-line judgment card

Validation criteria:

```yaml
PASS:
  - prepare and execute are fully separated
  - user burden stays near three fields

PASS_WITH_NOTE:
  - separation works but guarded_execution promotion needs sharper criteria

HOLD:
  - one-shot draft starts looking executable

FAIL:
  - task becomes direct Codex execution
```

### case 2. external reference ingest validation

Target:

`docs/reports/formation_movement_interface_external_reference_ingest_validation_case_v0.md`

Checklist:

- [ ] external reference is captured as unclassified seed
- [ ] user does not choose `object_type`
- [ ] VectorFL assigns `framing_candidate` at formed stage
- [ ] B-adjacent reference is not used as B promotion evidence
- [ ] direct evidence / defensive logic / comparison frame distinction is considered
- [ ] bounded_action_candidate remains only a prepare possibility
- [ ] guarded_execution remains HOLD
- [ ] short validation return is justified

Validation criteria:

```yaml
PASS:
  - reference is not over-promoted
  - user burden stays low
  - B promotion prohibition remains

PASS_WITH_NOTE:
  - flow is safe but direct evidence / defensive logic / comparison frame examples still need strengthening

HOLD:
  - B-adjacent reference is elevated to framing too aggressively

FAIL:
  - external reference becomes B evidence or operating rule
```

### case 3. user surface explanation validation

Target:

`docs/reports/formation_movement_interface_user_surface_explanation_validation_case_v0.md`

Checklist:

- [ ] explanation is not promoted to final definition
- [ ] it is handled as `unclassified seed -> explanation draft -> validation_return`
- [ ] internal-language-heavy explanation is judged as L failure
- [ ] over-easy explanation is judged as R loss / flattening
- [ ] balanced explanation remains provisional user-surface draft candidate
- [ ] explanation comparison is handled on VectorFL surface
- [ ] user does not choose `object_type`
- [ ] User Surface remains a four-line judgment card
- [ ] promotion remains forbidden

Validation criteria:

```yaml
PASS:
  - L failure and R loss are separated
  - balanced explanation stays provisional
  - user burden stays low

PASS_WITH_NOTE:
  - draft quality is good but acceptable simplification vs R loss still needs sharpening

HOLD:
  - explanation risks reading like final definition

FAIL:
  - user-surface explanation is promoted to baseline wording
```

## 4. shared operator-cost check

Checklist:

- [ ] user-filled fields stay near three
- [ ] user does not choose `object_type`
- [ ] user does not fill full Core 7
- [ ] User Surface stays to 3-4 line judgment card
- [ ] detailed interpretation stays on VectorFL surface
- [ ] execution conditions stay on Engine surface
- [ ] return branching stays on validation surface

Validation criteria:

```yaml
PASS:
  - user burden stays low and surface responsibilities remain separated

PASS_WITH_NOTE:
  - user burden stays low but some judgment language leaks outward

HOLD:
  - user must choose object_type or next_allowed_move

FAIL:
  - package behaves like a user input form
```

## 5. shared promotion-risk check

Checklist:

- [ ] promote is not the default after validation return
- [ ] refine / hold / downgrade / archive_as_residue remain normal branches
- [ ] external reference is not over-promoted to evidence
- [ ] user-surface explanation is not over-promoted to final definition
- [ ] Codex output is not over-promoted to implementation success

Validation criteria:

```yaml
PASS:
  - promotion remains an exceptional route

PASS_WITH_NOTE:
  - promotion prohibition remains but some phrasing sounds too certain

HOLD:
  - package candidate begins to read like baseline candidate

FAIL:
  - promote / lock / baseline reflection happens
```

## 6. shared return-loop check

Checklist:

- [ ] result does not stop as final output
- [ ] result returns as validation_return
- [ ] `reread_trigger` exists beyond `observed_result`
- [ ] `next_recommended_state` or `refinement_target` exists
- [ ] full validation return can be triggered when needed

Validation criteria:

```yaml
PASS:
  - formation -> movement -> formation loop remains

PASS_WITH_NOTE:
  - return exists but refinement target is weak

HOLD:
  - result returns but next branch remains unclear

FAIL:
  - result is treated as final endpoint
```

## 7. current synthesis across the three validated cases

```yaml
codex_one_shot_prepare_case:
  verdict: PASS_WITH_NOTE
  key_success:
    - prepare and execute remain separated
    - user input stays near three fields
    - object_type is not user-selected
  remaining_note:
    - guarded_execution promotion threshold needs refinement

external_reference_ingest_case:
  verdict: PASS_WITH_NOTE
  key_success:
    - unclassified seed works
    - B promotion is blocked
    - framing_candidate elevation remains safe
  remaining_note:
    - direct evidence / defensive logic / comparison frame boundaries need stronger examples

user_surface_explanation_case:
  verdict: PASS_WITH_NOTE
  key_success:
    - L failure and R loss are separated
    - explanation draft is not promoted to final definition
    - user burden stays low
  remaining_note:
    - acceptable simplification vs R loss still needs sharpening
```

## 8. next package reinforcement candidates

### candidate 1. user surface explanation clarification

Why:

User-surface explanation still leaves open:

- acceptable simplification vs R loss boundary
- when L/T/X ambiguity requires full validation return
- when a strong explanation draft outgrows short validation return
- how much intermediate layer / reread / provisionality must survive in user language

Validation needs:

- [ ] when easy explanation remains acceptable simplification
- [ ] when it becomes R loss / flattening
- [ ] when explanation starts looking like final definition
- [ ] when user-surface draft should default to full validation return

### candidate 2. direct evidence / defensive logic / comparison frame examples

Why:

External reference ingest now has the distinction, but still needs clearer examples.

Validation needs:

- [ ] one direct evidence example
- [ ] one defensive logic example
- [ ] one comparison frame example
- [ ] whether B-adjacent default should be `reread_priority` or `framing_candidate`

### candidate 3. guarded execution promotion refinement

Why:

Codex one-shot still leaves `allowed_to_prepare -> allowed_to_execute` at HOLD.

Validation needs:

- [ ] when one-shot draft becomes `guarded_execution`
- [ ] whether user approval, supervisor judgment, or both are needed
- [ ] whether `trust_scope` optional note is enough at prepare stage
- [ ] what the minimum execution constraint is

## 9. recommended next validation order

```text
1. reinforce user-surface explanation case
   - sharpen acceptable simplification vs R loss

2. reinforce external reference ingest case
   - add direct evidence / defensive logic / comparison frame examples

3. reinforce Codex one-shot case
   - sharpen guarded_execution promotion threshold

4. revalidate the three cases
   - confirm operator cost stays low

5. reassess package v0 status
   - keep PASS_WITH_NOTE / move to HOLD / judge limited promote-candidate possibility
```

## 10. final summary

At the current checkpoint, the formation-movement interface package has received `PASS_WITH_NOTE` in all three representative cases.

The package has successfully protected against:

- excessive user input burden
- premature `object_type` forcing
- Core 7 turning into mandatory input
- prepare / execute confusion
- over-promotion of external references
- user-surface explanation being treated as final definition
- validation return being treated as final result

Remaining reinforcement areas:

- acceptable simplification vs R loss boundary
- direct evidence / defensive logic / comparison frame examples
- guarded_execution promotion threshold
- short/full validation return trigger boundary
- conditions where A/C/T/X/R/L overlap should force hold

Current package state:

```yaml
package_status: package_candidate
overall_verdict: PASS_WITH_NOTE
next_allowed_move: targeted_clarification_patch_or_additional_validation
do_not:
  - baseline_lock
  - schema_enforcement
  - implementation
  - runtime_manifest_creation
  - validator_creation
```
