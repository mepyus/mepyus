# T_BRAIN_MIND_SIZED_MAINTAINABILITY_LENS_CARD_V0

classification: HOLD_CANDIDATE_LENS_CARD

Space is not the answer; it is a layered record of memory, trace, mistakes, failures, successes, extension, and prior answer-bearing strata. Model reasoning must reference it when the task affects space.

## lenses

### T_brain_operator_load
question: What review/decision burden does this lane impose on the human operator?
default_action: keep next lane smaller if load is high

### mind_sized_bite
question: Is the next output small enough to be absorbed and acted on?
default_action: split lane if not mind-sized

### maintainability_debt_watch
question: Could this pass locally while degrading architecture or space coherence?
default_action: add architecture coherence note, not automatic post-review

### ai_native_vs_assisted
question: Is this actually completing a workflow or merely assisting with reports/artifacts?
default_action: label assisted if only artifact production

### slow_ai_guard
question: Does the lane preserve learning/understanding instead of dopamine delegation?
default_action: prefer fast/local unless heavy trigger is real


HOLD: no authority/registry/current-position/promotion.
