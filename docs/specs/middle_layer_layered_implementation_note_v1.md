# middle layer layered implementation note v1

## 1. implementation stance
- experimental
- read-only
- no `inputter.py` patch
- no `labeler.py` patch
- no promotion logic touch

## 2. implemented helper
- script:
  - [run_middle_layer_interview_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_middle_layer_interview_probe.py)

## 3. implemented layer mapping

### layer 1. transcript pre-normalization
- remove timestamps from structural dominance
- weaken chapter markers
- strip simple speaker prefixes
- split long transcript stream into sentence-like units before regrouping

### layer 2. discourse noise suppression
- maintain explicit generic discourse term bucket
- downweight generic discourse tokens in topic anchor scoring
- keep suppressed discourse anchors visible instead of deleting them

### layer 3. case block aggregation
- regroup normalized units by bounded character/sentence budget
- emit block previews and block-level top topic terms
- infer bounded working-set role hints per block instead of leaving all blocks as broad topic bags
- keep block role names narrow enough to compare cases, but not stable enough to act like ontology

### current bounded role working set
- `problem_or_constraint_role`
- `mechanism_role`
- `verification_or_evaluation_role`
- `control_or_deployment_role`
- `reflection_or_gap_role`
- `observer_or_transition_role`

### role resolution stance
- `observer_or_transition_role` is visible but demoted to observer-only handling
- dominant role competition favors case-bearing roles over discourse-transition roles
- block roles are provisional evidence carriers, not promoted frame classes

### layer 4. provisional frame sketch + packet
- emit:
  - dominant topic anchors
  - suppressed discourse anchors
  - case blocks
  - provisional frame sketch
  - caution notes
- refine packet fields into:
  - dominant roles
  - secondary roles
  - observer-only roles
  - role evidence terms
  - case-specific signals
  - caution notes

### packet v1 intent
- move from compare-ready to compare-meaningful
- preserve source identity while making case-level role mix more legible
- keep final promotion and ontology decisions out of scope

## 4. known limitation
- v0 limitation was excessive `problem_or_constraint` gravity
- v1 improves role divergence across Dario / Andrej / Alex, but role evidence is still heuristic
- frame sketch is now more legible, but still not strong enough for promotion
- topic anchors are better than raw-only in some places, but still noisy

## 5. one-line lock
- current prototype proves the middle layer can be externalized and role-refined, but not yet that it is semantically mature or promotion-ready.
