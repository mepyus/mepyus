# phase transition and hold rule implementation baseline v0

## 1. Purpose

This baseline defines the minimum implementation standard for `phase_transition_and_hold_rule_v0`.

The rule must make phase a **judged result**, not a directly assigned value, and must preserve `hold` as a first-class decision state rather than a fallback.

## 2. What this baseline is for

This baseline exists so implementation can:

1. Treat phase transitions as evaluation results, not manual assignments.
2. Preserve `hold` as a formal state, not a TODO or placeholder.
3. Record transition / hold / no_change as append-only decision artifacts.
4. Keep reason, blockers, and next re-check conditions in the record.
5. Avoid over-generalizing into a generic workflow engine.

## 3. Core implementation rules

### 3.1 Phase assignment is forbidden

Implementation must not directly set phase like this:

```python
current_phase = "reflection"
current_phase = Phase.REFLECTION
```

Phase changes must come from an evaluator-produced decision artifact.

### 3.2 Hold is not a fallback

`hold` must be a legitimate `decision_type`, not an `else` branch, TODO, or placeholder.

### 3.3 no_change is also a decision

If phase does not change, the outcome still needs to be recorded.

- `transition`
- `hold`
- `no_change`

all remain append-only decision outcomes.

### 3.4 No reason, no decision

No decision artifact should be emitted without:

- `decision_reason`
- `evidence`
- `blocked_by` or empty list
- `next_check_trigger` or empty list

### 3.5 Keep the implementation local and minimal

Do not turn this into a generic orchestration or workflow engine.

Use only the minimum function boundary, minimum artifact, and minimum log needed to preserve the reasoning path.

## 4. Minimum implementation unit

v0 locks the following function boundaries:

```python
evaluate_phase_decision(
    current_phase: str,
    observations: list[Observation]
) -> PhaseDecision

persist_hold_if_needed(
    decision: PhaseDecision
) -> HoldRecord | None

review_hold(
    hold_id: str,
    review_reason: str
) -> HoldReviewResult
```

## 5. Function roles

### 5.1 `evaluate_phase_decision(...)`

Purpose:

- Read the current phase and observation bundle.
- Produce one of `transition`, `hold`, or `no_change`.

Must not:

- mutate `current_phase` directly
- accept arbitrary external context that bypasses observations
- expand into a generic rule engine

May:

- compute phase judgment
- produce decision reason
- link evidence
- output blocked_by / next_check_trigger

### 5.2 `persist_hold_if_needed(...)`

Purpose:

- Append a hold record only when `decision_type == "hold"`.

Must not:

- create hold outside evaluator output
- treat hold as a temporary fallback

### 5.3 `review_hold(...)`

Purpose:

- Review an existing hold
- Record whether it stays, reopens, or is dismissed

Must not:

- silently mutate hold state without review trace

## 6. Observation schema minimum

The evaluator should not take generic events directly.
It should take observable units.

Recommended minimum schema:

```python
from dataclasses import dataclass
from typing import Literal

@dataclass
class Observation:
    source_ref: str
    source_type: Literal[
        "breadcrumb",
        "candidate",
        "watch_rule",
        "latent_line",
        "tension_probe",
        "external_intake"
    ]
    signal_type: str
    signal_weight: float
    origin_layer: Literal["raw", "interpreted", "summary"]
    related_phase: str | None
    related_line: str | None
    observed_at: str
```

### Observation rules

- Do not let `signal_type` become a generic catch-all.
- Do not inject external context directly into evaluator.
- Record observations first, then judge from the accumulated observations.

## 7. Decision artifact schema

Use `PhaseDecision`, not a plain transition result.

```python
from dataclasses import dataclass
from typing import Literal

@dataclass
class PhaseDecision:
    decision_type: Literal["transition", "hold", "no_change"]
    from_phase: str
    to_phase: str | None
    decision_reason: str
    condition_met: list[str]
    evidence: list[str]
    blocked_by: list[str]
    next_check_trigger: list[str]
    decided_at: str
```

### Required field behavior

- `decision_type`: one of `transition`, `hold`, `no_change`
- `decision_reason`: explain the decision in at least one sentence
- `condition_met`: list of satisfied rules
- `evidence`: source refs used for the decision
- `blocked_by`: list of blockers, empty list allowed
- `next_check_trigger`: what should be observed next, empty list allowed

## 8. Hold artifact schema

`hold` must have a separate record.

```python
from dataclasses import dataclass
from typing import Literal

@dataclass
class HoldRecord:
    hold_id: str
    item_ref: str
    item_type: Literal["phase_decision", "candidate", "watch_rule", "latent_line"]
    hold_reason: str
    blocked_by: list[str]
    reopen_condition: str
    next_check_trigger: list[str]
    held_at: str
    last_reviewed: str
    status: Literal["active", "reopened", "dismissed"]
```

### Hold record requirements

The record must include:

- `hold_reason`
- `blocked_by`
- `reopen_condition`
- `held_at`
- `last_reviewed`
- `next_check_trigger`

## 9. Append-only logs

Prefer append-only `.jsonl` logs.

Recommended files:

- `runtime/logs/phase_decision_log.jsonl`
- `runtime/logs/hold_log.jsonl`

### Append-only rules

- decision records are append-only
- hold reviews are append-only
- `runtime/current_phase.json` is only a summary surface, not the truth ledger

## 10. Implementation skeleton

The implementation should look like:

```python
decision = evaluate_phase_decision(state.current, observations)
persist_hold_if_needed(decision)
state.apply_decision(decision)
```

And must not look like:

```python
state.current = "reflection"
```

## 11. Current repository alignment

The current runtime preflight path already aligns with parts of this baseline:

- `runtime_preflight` performs pre-read gating
- `phase_decision_log.jsonl` is append-only
- `runtime/current_phase.json` is written as a summary surface

The remaining implementation gap is that this baseline still needs a dedicated `PhaseDecision` / `HoldRecord` layer and a minimal local evaluator boundary if the phase rule is to be fully canonicalized in code.

## 12. Scope guard

Do not over-generalize this into a generic workflow engine.

This is a local minimal rule for `phase_transition_and_hold_rule_v0`, not a broad orchestration abstraction.

## 13. One-line conclusion

> Phase implementation must be decision-based, hold must be first-class, and every transition or non-transition must be recorded as an append-only artifact with reasons, blockers, and re-check triggers.

