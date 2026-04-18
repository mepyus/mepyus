# build drift anchor baseline v0

## 1. Purpose

This baseline is the implementation anchor that checks and preserves drift between the original intent and the implementation result while a Claude Code build is in progress.

## 2. What this baseline is for

This baseline exists so implementation can:

1. Freeze the core intent before coding begins.
2. Prevent convenient reinterpretation and structural drift during the build.
3. Record what will not be done in this turn.
4. Re-check the implementation against the original intent at checkpoints.
5. Reduce alignment cost across user, supervisor, and Codex / Claude Code.

## 3. Core rules

### 3.1 No build starts without an intent anchor

Before implementation, record at least:

- what will be built
- what will not be built
- what counts as drift

### 3.2 The anchor must stay short

If it is too long, nobody rereads it during implementation.

Recommended:

- 5 to 12 lines
- one core purpose line
- up to 3 non-goals
- up to 3 drift questions

### 3.3 Checkpoints are mandatory

Long builds must re-check the anchor at:

- schema draft time
- after core function drafting
- before validation
- before main integration

### 3.4 Drift is not the same as “something better looks nice”

Do not change the build just because another structure looks cleaner.
Intent changes require an explicit unlock or supervisor decision.

### 3.5 Drift is a traceable asset

Wrong turns, over-structuring, and convenient simplifications are all recovery knowledge and must be recorded.

## 4. Required fields

Record:

- `build_unit_name`
- `build_intent`
- `non_goals`
- `must_preserve`
- `drift_questions`
- `checkpoints`
- `approved_scope`
- `blocked_scope`
- `reference_baselines`
- `review_mode`

During checkpoints, also record:

- `current_direction_summary`
- `drift_signals_found`
- `alignment_status`
- `correction_action`
- `needs_supervisor_review`

## 5. Minimal build anchor structure

### 5.1 build_intent

One-line core purpose for the build.

Example:

- “Implement phase as an observed decision with hold protection, not as a manually declared enum.”

### 5.2 non_goals

What will not be built in this turn.

Example:

- do not implement full tension_map in this turn
- do not redesign candidate registry
- do not add UI work

### 5.3 must_preserve

What must not be broken.

Example:

- hold must remain an explicit state
- decision must include reason and blocked_by
- append-only logging must not be replaced by console-only output

### 5.4 drift_questions

Questions that must be re-asked during the build.

Example:

- are we still building a phase evaluator, not a generic workflow engine?
- is hold truly protected when signals conflict?
- are blocked_by and next_check_trigger persisted?

### 5.5 checkpoints

When to re-check.

Example:

- after decision schema draft
- after evaluator function
- before main integration

## 6. Example build anchor format

```yaml
build_unit_name: phase_transition_and_hold_rule_v0
build_intent: >
  Implement phase as an observed decision with hold protection,
  not as a manual declared enum.
non_goals:
  - do not implement full tension_map in this turn
  - do not redesign candidate registry
  - do not add UI work
must_preserve:
  - hold must remain an explicit state
  - decision must include reason and blocked_by
  - append-only logging must not be replaced by console-only output
drift_questions:
  - are we still building a phase evaluator, not a generic workflow engine?
  - is hold truly protected when signals conflict?
  - are blocked_by and next_check_trigger persisted?
checkpoints:
  - after decision schema draft
  - after evaluator function
  - before main integration
approved_scope:
  - preflight evaluator
  - phase decision artifact
blocked_scope:
  - full refactor of runtime phase subsystem
reference_baselines:
  - phase_transition_and_hold_rule_v0
  - concept_to_implementation_map_baseline_v0
review_mode: supervisor_alignment_check
```

## 7. Drift signals

The following are drift signals:

- the build starts as a helper and becomes a generic framework
- trace structure is reduced to console output
- hold protection is replaced by enum mutation
- structural cleanliness becomes more important than intent fit
- scope widens into UI or refactoring work

## 8. Correction rules

If drift is detected, do one of the following:

1. return the build to the original intent
2. record the drift reason and park the work
3. if the direction really must change, ask for supervisor unlock and revise the baseline

Do not absorb drift silently.

## 9. One-line conclusion

> build_drift_anchor freezes intent, non-goals, preservation items, and drift questions before build time, and forces the implementation to re-check alignment at checkpoints.

