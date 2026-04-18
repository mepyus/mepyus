# concept to implementation map baseline v0

## 1. Purpose

This baseline is the official translation rule that maps space language into implementation language.

It prevents `latent line`, `breadcrumb`, `candidate`, and `phase` from being freely reinterpreted in Claude Code, and instead forces each concept to descend into a suitable implementation unit.

## 2. What this baseline is for

This baseline exists so implementation can:

1. Prevent ad hoc translation of space concepts.
2. Project the reading space's judgment structure safely into code.
3. Reduce Claude Code's convenient re-interpretation.
4. Create the target objects for `build_drift_anchor` and `implementation_eval_criteria`.

## 3. Core rules

### 3.1 Space concepts do not become code objects immediately

Do not turn `latent line` into a class, table, or service just because the word sounds close.
First read the role, then choose the implementation unit that fits the role.

### 3.2 Implementation is chosen by role, not by naming similarity

Implementation should descend based on what the concept does:

- judgment role
- storage role
- flow control role
- display / query role
- experiment trace role

### 3.3 One concept may map to multiple implementation surfaces

For example, `breadcrumb` may split into:

- append-only event log
- UI trace surface
- decision summary artifact

The mapping does not force 1 concept = 1 implementation object.

### 3.4 Every mapping must keep its reason

The mapping must explain why it descended as a state machine, a json artifact, a table, or another structure.

### 3.5 Descent must respect existing baselines

Do not violate higher-order rules such as constitution, state change RPC constraints, or existing app/main/db contracts.

## 4. Required metadata per mapping

When mapping a concept downward, record:

- `concept_name`
- `concept_role`
- `implementation_target`
- `implementation_shape`
- `storage_surface`
- `execution_surface`
- `why_this_mapping`
- `not_chosen_options`
- `related_baseline_refs`
- `open_questions`

## 5. Minimal implementation categories

Space concepts may descend into one or more of the following.

### 5.1 Data structure

Examples:

- table
- json artifact
- typed model
- config file

### 5.2 Control structure

Examples:

- state machine
- preflight gate
- rule evaluator
- router

### 5.3 Trace structure

Examples:

- append-only log
- decision history
- rejected path log
- comparison report

### 5.4 Interface structure

Examples:

- summary panel
- debug surface
- operator view
- review page

### 5.5 Boundary structure

Examples:

- validation rule
- drift check
- non-goal guard
- unlock condition

## 6. Core mapping rules

### 6.1 latent line

Definition:

- a latent line is an entrance to rereading
- it guides how the current input should be read

Implementation rule:

- do not default to a direct DB entity
- first consider a rule set, selector, scoring lens, or state tag
- only promote into a separate registry when repeatability and judgment clarity are sufficient

Recommended descent:

- `line_selector.py`
- `latent_line_registry.json`
- `line_score_evaluator()`
- `active_line_tags`

### 6.2 breadcrumb

Definition:

- breadcrumb is the trace of judgment movement and reasoning

Implementation rule:

- do not reduce it to console logging
- use an append-only trace plus a summary surface
- preserve why the path moved

Recommended descent:

- `runtime/logs/breadcrumbs.jsonl`
- `breadcrumb_summary_latest.json`
- `append_breadcrumb_entry()`

### 6.3 candidate

Definition:

- a candidate is a pattern that has been repeatedly observed and provisionally structured

Implementation rule:

- do not hard-code it as a rule immediately
- keep it in `candidate_registry` with watch rule linkage first
- preserve observation status until promotion is justified

### 6.4 phase transition

Definition:

- phase transition is the mechanism that changes reading mode / phase based on observed signals

Implementation rule:

- do not implement it as a mere enum reassignment
- use a preflight evaluator plus decision artifact
- preserve `hold` as a distinct state

### 6.5 rejection

Definition:

- rejection is a path that was not taken, plus the reason it was not taken

Implementation rule:

- do not drop rejected paths
- keep them as recovery knowledge
- always preserve reopen conditions

## 7. Example mapping format

```yaml
concept_name: latent line
concept_variant: pre_read_eye
concept_role: turn entry guidance
implementation_target: preflight evaluator
implementation_shape: rule set + selector function + active tag
storage_surface:
  - control/turn_router.json
  - runtime/active_line_tags.json
execution_surface:
  - preflight pipeline
why_this_mapping: |
  pre_read_eye is not a stored domain entity. It acts as a turn-entry evaluator,
  so it should descend into a selector/rule evaluator rather than a database table.
not_chosen_options:
  - direct DB table
  - UI-only badge
related_baseline_refs:
  - phase_transition_and_hold_rule_v0
open_questions:
  - whether line strength scoring should be numeric or categorical
```

## 8. Explicit examples

### 8.1 `phase_transition_and_hold_rule_v0`

Space concepts:

- phase
- hold
- continuity / residue / tension / sufficiency

Implementation descent:

- `evaluate_phase_transition(input_context) -> decision`
- `current_phase.json`
- `phase_decision_log.jsonl`

Why:

- phase is a judgment result, not a stored object
- hold is a decision state and must carry decision reason

### 8.2 `rejection_log`

Space concepts:

- failed overlay
- rejected candidate
- movement blocked by drift guard

Implementation descent:

- `append_rejection_entry()`
- `runtime/logs/rejection_log.jsonl`

Why:

- rejection knowledge must remain append-only trace
- it must connect to reopen rules later

## 9. Forbidden patterns

- Do not map a concept to class/table/service just because the name is familiar.
- Do not let Claude Code collapse the concept into a single helper file for convenience.
- Do not reduce trace structure to debug print.
- Do not promote candidates into hard-coded business rules before repeatable validation.
- Do not replace phase with manual enum updates.

## 10. Forbidden mapping rules v0

This section exists to prevent the core concepts of the reading space from being lowered into implementation in the wrong way.

The central rule is:

**Core concepts of the reading space must not be implemented through direct creation, direct assignment, or immediate hardening. They must appear only as the result of observation, aggregation, evaluation, and hold.**

### 10-1. latent line -> direct entity/table forbidden

#### Forbidden

- putting `LatentLine` directly into a class/table/entity that can be created on demand
- using `line.create(...)` style direct declaration
- treating a line as a pre-registered object instead of an observed result

#### Why it is forbidden

A latent line is a rereading entrance that is discovered inside the space.
It is not a fixed entity that code or a person defines first.

If it becomes directly creatable:

- observation is no longer before declaration
- emergence is no longer before input
- “it exists because it is registered” replaces “it exists because it became visibly stronger”

#### Allowed

- line score evaluator output
- repeated observation aggregation
- active line snapshot
- registry as a result record

#### Implementation rule

- direct create is forbidden
- line may only appear as an observation / breadcrumb / trace aggregation result
- if storage is needed, store a snapshot or result, not a first-class entity

#### Bad example

```python
line = LatentLine.create(name="pre_read_eye", strength=0.8)
```

#### Good direction

```python
line_scores = evaluate_latent_lines(observation_bundle)
active_lines = select_active_lines(line_scores)
save_line_snapshot(active_lines)
```

### 10-2. breadcrumb -> console/event-only log reduction forbidden

#### Forbidden

- replacing breadcrumb with a simple execution log or console output
- keeping only “what happened” and dropping “why the movement happened”
- failing to distinguish action trace from judgment trace

#### Why it is forbidden

The core of breadcrumb is not raw execution history.
It is the trace of judgment movement and the reason for that movement.

If `why` is missing:

- the path cannot be reconstructed later
- rereading cannot follow the original judgment
- the space loses its main reread value

#### Allowed

- append-only breadcrumb log
- judgment-path summary surface
- trace entry with trigger / reason / what_changed

#### Implementation rule

Breadcrumb append must include at least:

- `reason`
- `what_changed`
- `trigger`
- `from_ref`
- `to_ref`

If these are missing, breadcrumb append is forbidden.

#### Bad example

```python
log("moved to phase: reflection")
```

#### Good direction

```python
append_breadcrumb(
    from_ref="phase:space_reading",
    to_ref="phase:reflection",
    trigger="residue_increase",
    reason="existing line no longer absorbs the new input cleanly",
    what_changed="phase widened from thickening to reflective reread"
)
```

### 10-3. phase -> manual enum assignment forbidden

#### Forbidden

- direct `current_phase = X` assignment
- reducing phase to a plain enum value and removing transition conditions / reasons
- overwriting the current value without preserving transition history

#### Why it is forbidden

Phase is not a declaration.
It is a decision result that appears when observed signal combinations reach a threshold.

If direct assignment is allowed:

- phase becomes declaration instead of emergence
- hold protection disappears
- transition reasons and failed transition reasons vanish

#### Allowed

- enum / type for representation
- phase change only through evaluator

#### Implementation rule

- direct assignment is forbidden
- only `evaluate_phase_transition(...) -> decision` is allowed
- transition / hold reasons must be written to append-only log
- `blocked_by` and `next_check_trigger` must be preserved

#### Bad example

```python
current_phase = Phase.REFLECTION
```

#### Good direction

```python
decision = evaluate_phase_transition(observation_context)
persist_phase_decision(decision)
update_current_phase_from_decision(decision)
```

### 10-4. candidate -> early implementation linkage forbidden

#### Forbidden

- attaching implementation code / features immediately after candidate registration
- treating a candidate as fact instead of a provisional structure
- hard-coding rules before watch / boundary validation

#### Why it is forbidden

A candidate is only a repeatedly observed tentative pattern.

If implementation is attached too early:

- the code hardens the candidate assumption
- counterexamples become hard to unwind
- observation starts bending around the structure instead of verifying it

#### Allowed

- candidate evaluator
- candidate registry
- watch-rule linkage
- observation-only status until boundary checks pass

#### Implementation rule

Candidate must not be linked to implementation before:

1. repeated observation is present
2. watch rule is connected
3. boundary condition is checked
4. scope is validated

Until then it remains observation + registry + trace only.

#### Bad example

```python
register_candidate("raw_to_first_pass_to_report")
build_raw_to_first_pass_to_report_pipeline()
```

#### Good direction

```python
register_candidate_observation("raw_to_first_pass_to_report")
link_watch_rule(candidate_id, "second_candidate_emergence_watch")
append_candidate_evidence(candidate_id, evidence_ref)
```

### 10-5. hold -> else branch / TODO fallback forbidden

#### Forbidden

- reducing hold to an `else` branch
- leaving it as a TODO later
- entering hold without a hold reason or reopen condition

#### Why it is forbidden

Hold is not “not implemented yet”.
It is an intentional independent state.

If it is treated like fallback:

- the structural meaning of hold disappears
- reopen conditions disappear
- the code drifts into silent abandonment or silent deletion

#### Allowed

- explicit hold state
- hold decision artifact
- reopen hint / next check trigger / review timestamp

#### Implementation rule

Hold entry must include at least:

- `hold_reason`
- `blocked_by`
- `reopen_condition`
- `held_at`
- `last_reviewed`
- `next_check_trigger`

Without those fields, hold entry is forbidden.

#### Bad example

```python
if decision_possible:
    process()
else:
    pass  # TODO: hold later
```

#### Good direction

```python
enter_hold_state(
    hold_reason="signal conflict remains unresolved",
    blocked_by=["latent_line_tension"],
    reopen_condition="priority clarified or repeated evidence appears",
    held_at=now(),
    last_reviewed=now(),
    next_check_trigger=["same conflict repeats", "tension_map added"]
)
```

## 11. One-line conclusion

> concept_to_implementation_map is the official descent rule that maps space concepts into code objects, and every implementation must obey role fit, trace preservation, and promotion restraint.
