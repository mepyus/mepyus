# second candidate emergence watch rule v1

## 0. Verdict

**PASS**

## 1. Watch rule surface created

Created:
- `runtime/manifests/second_candidate_watch_rules.json`

Purpose:
- define when a second reading-path candidate may be named
- keep the current observation state from drifting into premature candidate creation

## 2. Key criteria

- `current_clear_candidates = [raw_to_first_pass_to_report]`
- `must_not_be_explained_by = [family_variation, divergent_mode_boundary, existing_scope_extension]`
- `minimum_repeat_requirement = 2`
- `minimum_context_diversity = 2`
- `disqualifiers = [same_candidate_new_family, same_candidate_boundary_note_only]`
- `trigger_for_seed_found = distinct repeated path not collapsible to existing candidate`

## 3. Why current evidence still does not trigger second seed

- Current observations can still be explained as:
  - the same candidate across different families, or
  - the same candidate across divergent mode boundaries
- The boundary notes already explain the variation.
- There is still no distinct repeated path that cannot be collapsed back into `raw_to_first_pass_to_report`.
- Therefore the watch rule remains inactive.

## 4. Next minimal fix

- Keep observing.
- Only name a second candidate when a path repeats twice across at least two contexts and cannot be explained by the current candidate plus boundary notes.

