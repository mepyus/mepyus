# minimal soft layer separation note v0

## 0. One-line conclusion

Now is the time to separate roles softly, not to hard-freeze the whole structure.

Label first, lock later.

## 1. Why this is needed now

The space has already grown enough that continuing to mix roles will make later rework expensive.

But hard-separating everything right now would freeze still-forming lines too early.

So the rule is:

- draw boundaries now
- do not fully freeze yet
- keep the surfaces readable

## 2. The five minimum layers

### 2.1 Baseline layer

Role:

- philosophy
- baselines
- forbidden rules
- classification rules
- higher-order judgment principles

Examples:

- constitution
- baseline
- tension_map criteria
- external_intake_filter criteria
- concept_to_implementation_map
- build_drift_anchor
- implementation_eval_criteria
- implementation_placement

This layer answers:

- what is correct

### 2.2 Current-state layer

Role:

- where we are now
- current active status
- fast summary surface

Examples:

- `current_phase.json`
- `active_holds.json`
- current focus
- current active latent line snapshot

This layer is a summary surface, not the source of truth.

### 2.3 Event-record layer

Role:

- what actually happened
- why it happened
- why it did not happen
- why it stopped

Examples:

- breadcrumb log
- phase decision log
- hold log
- rejection log
- review log

This layer must remain append-only.

### 2.4 Decision / implementation layer

Role:

- calculation
- evaluator
- state decision
- implementation functions
- minimal auto checks

Examples:

- `evaluate_phase_decision`
- `persist_hold_if_needed`
- `review_hold`
- `external_intake_filter` evaluator
- `trace_completeness_check`
- `allowed_types_compliance`

This layer answers:

- what should happen

### 2.5 Latent / observation layer

Role:

- still-unconfirmed lines
- watchpoints
- possible branches
- 흐릿하지만 반복되는 해석 조각

Examples:

- latent line notes
- observed line candidates
- watchpoints
- possible branches

This layer keeps not-yet-frozen signals alive without promoting them too early.

## 3. Soft separation rules

### 3.1 Tag the layer first

Every new file or note should first be labeled as one of the five layers.

### 3.2 Do not create more mixed files

New files should not mix:

- baseline
- current state
- event history
- implementation
- latent observation

### 3.3 Keep current state as summary only

Current artifacts are for fast reading.
The evidence must stay in the event-record layer.

### 3.4 Keep latent lines separate from locked structure

Do not put still-fuzzy lines into the baseline layer.

Do not treat them as current state.

### 3.5 Freeze later

Soft separation now.
Hard freeze only after lines have stabilized.

## 4. What not to do

- Do not hard-freeze fuzzy lines now
- Do not perform a full folder redesign now
- Do not promote latent lines into locked structure too early
- Do not treat current summary as truth archive
- Do not mix baseline and event history in one file

## 5. Minimum working question set

When creating or rereading a file, ask:

1. Is this a baseline?
2. Is this a current-state artifact?
3. Is this an event record?
4. Is this a decision / implementation artifact?
5. Is this a latent / observation note?

If more than one answer is true, the file is already mixed.

## 6. One-line conclusion

> The immediate task is not full structural freezing, but soft separation of baseline, current state, event records, decision / implementation, and latent observation so they stop bleeding into each other.
