# implementation eval criteria baseline v0

## 0. One-line definition

This baseline is the supervisor-side standard for judging whether an implementation truly satisfies the locked structure, intent, and preservation rules.

It goes beyond “does it run” and asks “was it implemented in the right way?”

## 1. Purpose

This baseline exists so implementation evaluation can:

1. Separate runtime correctness from intent correctness.
2. Judge completion by structural fit, not only by execution.
3. Give the supervisor a repeatable way to re-judge Claude Code output.
4. Build reusable evaluation language for future runs.
5. Keep automatic checks and supervisory judgment in separate lanes.

Core sentence:

**Good implementation is not just executable code; it is code that implements the locked structure in the correct way.**

## 2. Core rules

### 2.1 Evaluation has two layers

Every implementation must be judged through:

- functionality evaluation
- intent alignment evaluation

Passing only one is not completion.

### 2.2 Intent alignment is the higher layer

If the code runs but violates the locked intent, it does not pass.

### 2.3 No criteria-free evaluation

Do not say “it looks fine” or “it seems okay.”
Every judgment must cite the baseline, anchor, or reference used.

### 2.4 Use explicit result states

Use:

- `PASS`
- `PASS_WITH_NOTE`
- `HOLD`
- `FAIL_DIRECTION`
- `FAIL_STRUCTURE`

## 3. Required evaluation metadata

Record:

- `build_unit_name`
- `reference_baselines`
- `working_scope`
- `functionality_status`
- `intent_alignment_status`
- `notes`
- `missing_parts`
- `risk_signals`
- `judgment`
- `why_this_judgment`
- `next_action`

## 4. Evaluation layer 1: functionality

This layer checks:

- does the code run
- are input / output shapes intact
- are required fields persisted
- does the minimum path execute without error
- does it avoid breaking existing baselines

Example:

- after implementing `phase_transition_and_hold_rule_v0`, does the evaluator run and produce `current_phase.json` and `phase_decision_log.jsonl` with the required fields?

## 5. Evaluation layer 2: intent alignment

This layer checks:

- does the implementation preserve the original build intent
- is the descent aligned with the concept-to-implementation map
- did it avoid the drift anchor non-goals
- does it preserve the intended protection rules
- did it simplify cleanly without losing structure?

## 6. Shared evaluation axes

All implementations should be judged across six axes.

### 6.1 intent fidelity

Does it preserve the original purpose?

### 6.2 structural fidelity

Does it preserve the locked structure relationships?

### 6.3 scope discipline

Did it stay within the turn scope?

### 6.4 trace preservation

Are reasons, blockers, and re-check paths still recorded?

### 6.5 baseline compliance

Does it avoid conflicts with higher-order baselines?

### 6.6 future reusability

Can the result be reused in a future build or re-evaluation?

## 7. Evaluation layers vs automation

### 7.1 Automatically checkable

These are “exists or not” style checks:

- required fields are present
- allowed types are respected
- raw entries are append-only
- direct assignment guards are not violated
- trace artifacts exist

### 7.2 Supervisory judgment required

These must remain with the supervisor:

- final intent fidelity
- final structural responsibility
- baseline spirit compliance
- generic drift judgment

Automation is a warning / guard rail, not the final judge.

## 8. Example evaluation format

```yaml
build_unit_name: phase_transition_and_hold_rule_v0
reference_baselines:
  - phase_transition_and_hold_rule_implementation_baseline_v0
  - concept_to_implementation_map_baseline_v0
  - build_drift_anchor_baseline_v0
working_scope:
  - preflight evaluator
  - phase decision artifact
functionality_status: PASS
intent_alignment_status: PASS_WITH_NOTE
notes:
  - hold state is preserved
  - decision_reason and blocked_by are persisted
  - sufficiency scoring remains heuristic and needs tightening
missing_parts:
  - tension_map linkage not yet implemented
risk_signals:
  - current signal scoring may drift into ad-hoc heuristics
judgment: PASS_WITH_NOTE
why_this_judgment: >
  Core structure is preserved and the evaluator behaves as intended,
  but signal scoring criteria are still weak and need stronger rule linkage.
next_action:
  - add tension_map_v0 linkage
  - tighten signal scoring examples
```

## 9. PASS state interpretation

- `PASS`
  - functionality and intent alignment are both sufficient
  - main entry is acceptable
- `PASS_WITH_NOTE`
  - core structure is correct
  - note and watch conditions are required
- `HOLD`
  - not wrong, but still needs observation or correction
- `FAIL_DIRECTION`
  - code works, but the implementation drifted from the intended direction
- `FAIL_STRUCTURE`
  - the core structure was not preserved

## 10. One-line conclusion

> implementation_eval_criteria is the supervisor-side standard for judging whether the implementation truly satisfies the locked structure, intent, and preservation rules, while automation is limited to guard-rail checks.
