# middle layer role resolution refinement result

## 1. refined scope
- layer 3: YES
- layer 4: YES

## 2. what changed
- refined the read-only interview probe to resolve case blocks into a bounded working-set of frame roles instead of broad topic buckets
- added packet v1 fields for:
  - dominant roles
  - secondary roles
  - observer-only roles
  - role evidence terms
  - case-specific signals
- kept `observer_or_transition_role` visible but out of dominant role competition so case-bearing roles could separate more clearly
- generated a refined packet example:
  - [middle_layer_interview_probe_20260327T223511Z.json](/Users/sungsookim/universe/vectorfl_replica/app/work/archive_review/interview_support/middle_layer_experiments/generated/middle_layer_interview_probe_20260327T223511Z.json)

## 3. verification
- discourse anchor dominance still reduced: YES
- topic-bearing anchor uplift retained: YES
- case-specific dominant roles more visible: YES
- defer/observer-only roles clearer: YES
- compare-ready packet v1 produced: YES

## 4. untouched
- promotion logic: YES
- current asset map: YES
- shared reality/baseline: YES
- core engine: YES

## 5. optional note
- later promotion still premature: YES
- one more refinement useful: YES

### case-level read
- Dario:
  - dominant roles:
    - `mechanism_role`
    - `verification_or_evaluation_role`
- Andrej:
  - dominant roles:
    - `reflection_or_gap_role`
    - `problem_or_constraint_role`
- Alex:
  - dominant roles:
    - `problem_or_constraint_role`
    - `control_or_deployment_role`

### why this is better than v0
- v0 proved the middle layer could emit packets, but role mix still collapsed toward broad constraint language
- v1 keeps the same read-only scaffold while making the three interview cases diverge into more compare-meaningful dominant role combinations

## 6. result
- status: PASS_WITH_NOTE

## 7. one-line summary
- layer 3/4 refinement made the interview packets more compare-meaningful by separating dominant role mixes across Dario, Andrej, and Alex without touching promotion logic or core paths.
