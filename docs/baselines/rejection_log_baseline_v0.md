# rejection_log baseline v0

## 0. One-line definition

`rejection_log` is not an error log.
It is a repository of avoidance knowledge that records paths we tried but chose not to adopt, why we did not adopt them, and when they may be reopened.

## 1. Purpose

This baseline exists so the system can:

1. Separate failure / rejection / hold from generic error logs.
2. Record what was not adopted and why.
3. Distinguish `blocked`, `parked`, and `rejected` so the next reread condition stays clear.
4. Preserve reopenability instead of turning rejection into a graveyard.
5. Keep records append-only for later re-evaluation and supervisory review.

Core sentence:

**A good space remembers not only what it read, but also what it chose not to pursue and why.**

## 2. Core rules

### 2.1 Rejection is not an error log

An error log records events and exceptions.
A rejection log records **a judged non-adoption path**.

Each rejection entry must include:

- what was tried
- why it failed
- why it is not adopted now
- when it may be reopened

### 2.2 Rejection is not a TODO bucket

The following are not acceptable on their own:

- "later"
- "to be revisited"
- "undecided"
- "when ready"

If they appear without concrete detail, the entry is a TODO, not a rejection.

### 2.3 `reopen_condition` is mandatory

If `reopen_condition` is missing, the rejection becomes a graveyard.

- `"never"` is allowed as an explicit value.
- conditional reopen must state a concrete trigger.

### 2.4 Reopen is not automatic

Even if the condition is met, auto-reopen is forbidden.

Condition satisfaction is only a review signal.
Actual reopen still requires a separate judgment.

### 2.5 Append-only rule

Do not modify rejection entries in place.

Reviews / reopen decisions are appended as new entries.
The latest state is computed by a summary surface.

## 3. Disposition rule

The base dispositions are:

- `rejected`
- `blocked`
- `parked`

`reopenable` is not a base disposition.
It is a derived review flag.

## 4. Disposition definitions

### 4.1 rejected

Definition:

- Fundamentally incompatible with the current structure or rule set
- Repeating the same conditions is low-value

Examples:

- a candidate that breaks the latent line first principle
- an overlay that directly violates raw return preservation

Possible `reopen_condition`:

- `"never"`
- `"only if higher baseline changes"`

### 4.2 blocked

Definition:

- The direction is not inherently wrong, but current conditions are insufficient
- It may reopen if more evidence or external support appears

Examples:

- not enough observations to promote a candidate
- missing external bridge evidence

Possible `reopen_condition`:

- `"same pattern observed 3 more times"`
- `"required evidence_ref added"`

### 4.3 parked

Definition:

- The judgment itself is not yet stable enough, so the item is intentionally paused
- Internal judgment timing or tension resolution is still incomplete

Examples:

- latent line conflict exists but tension_map is not yet available
- decision lineage is too thin to make a final call

Possible `reopen_condition`:

- `"after tension_map_v0 exists"`
- `"when conflict is observed again with evidence"`

## 5. Base disposition vs derived review signal

### Base disposition

- `rejected`
- `blocked`
- `parked`

### Derived review signal

- `reopen_ready = true`
- `reopen_recommended = true`

`reopenable` is therefore a computed state, not a raw status.

## 6. Minimum schema

```python
from dataclasses import dataclass
from typing import Literal

@dataclass
class RejectionEntry:
    rejection_id: str
    item_id: str
    item_type: Literal["candidate", "overlay", "path", "judgment"]
    disposition: Literal["rejected", "blocked", "parked"]
    rejection_reason: str
    decided_by: Literal["watch_rule", "evaluator", "manual"]
    what_was_tried: str
    why_it_failed: str
    reopen_condition: str
    evidence_refs: list[str]
    blocked_by: list[str]
    related_phase: str | None
    related_line: str | None
    rejected_at: str
```

## 7. Schema rules

### Required fields

Do not create an entry if any of the following are empty:

- `rejection_reason`
- `what_was_tried`
- `why_it_failed`
- `reopen_condition`

### Recommended fields

If possible, also keep:

- `evidence_refs`
- `blocked_by`
- `related_phase`
- `related_line`

Core point:
If the explanation exists without source refs, the rejection is hard to reread later.

## 8. Review / reopen schema

Reviews are also append-only.

```python
from dataclasses import dataclass
from typing import Literal

@dataclass
class RejectionReviewEntry:
    rejection_id: str
    review_action: Literal["reviewed", "reopen_ready", "reopened", "kept_closed"]
    review_reason: str
    evidence_refs: list[str]
    reviewed_at: str
```

## 9. Allowed log types

```python
ALLOWED_REJECTION_LOG_TYPES = {
    "rejection_entered",
    "rejection_reviewed",
    "rejection_reopened",
}
```

Do not add new types unless actual observed need and supervisor judgment justify it.

## 10. Append-only rules

### 10.1 Raw rejection entries are not edited

The first rejection entry must not be rewritten.

### 10.2 Reviews are appended

Do not mutate `last_reviewed` on the raw entry.
Append a review entry and let the summary calculate the latest state.

### 10.3 Reopen happens only after review

Even if the reopen condition is satisfied, automatic reopen is forbidden.

## 11. Drift smells

### 11.1 TODO bucketization

Bad pattern:

```python
RejectionEntry(
    rejection_reason="revisit later",
    what_was_tried="",
    why_it_failed="",
    reopen_condition="later"
)
```

### 11.2 Mixing error logs and rejection logs

Do not merge errors and rejection judgments into one schema.

### 11.3 Status bloat

Do not proliferate the base status set:

- rejected
- dismissed
- archived
- deprecated
- legacy
- dormant

The base disposition set must stay at three.

### 11.4 Automatic reopen

```python
if condition_met(entry.reopen_condition):
    auto_reopen(entry)
```

This is forbidden.
Reopen is a review signal, not an automatic event.

## 12. Implementation example skeleton

```python
import json
from dataclasses import asdict
from datetime import datetime

def _now_iso() -> str:
    return datetime.utcnow().isoformat() + "Z"

def _append_rejection_jsonl(path: str, payload: dict) -> None:
    assert payload["type"] in ALLOWED_REJECTION_LOG_TYPES
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")

def append_rejection_entry(entry: RejectionEntry) -> None:
    if not entry.rejection_reason:
        raise ValueError("rejection_reason required")
    if not entry.what_was_tried:
        raise ValueError("what_was_tried required")
    if not entry.why_it_failed:
        raise ValueError("why_it_failed required")
    if entry.reopen_condition is None or entry.reopen_condition == "":
        raise ValueError("reopen_condition required")

    _append_rejection_jsonl(
        "runtime/logs/rejection_log.jsonl",
        {
            "type": "rejection_entered",
            "entry": asdict(entry),
        },
    )

def append_rejection_review(entry: RejectionReviewEntry) -> None:
    _append_rejection_jsonl(
        "runtime/logs/rejection_log.jsonl",
        {
            "type": "rejection_reviewed",
            "review": asdict(entry),
        },
    )
```

## 13. Evaluation linkage

If any of the following appear, it should not pass:

- rejection is implemented like a generic error log
- `reopen_condition` is missing
- `what_was_tried` / `why_it_failed` are missing
- `reopenable` is stored as a raw status
- `last_reviewed` is mutated in place on the raw entry
- automatic reopen is implemented

Recommended judgment:

- structural violation -> `FAIL_STRUCTURE`
- direction over-generalization -> `FAIL_DIRECTION`
- mostly correct but evidence/review is thin -> `PASS_WITH_NOTE`

## 14. One-line conclusion

`rejection_log` is an avoidance-knowledge store, not a failure log; it must remember what was tried, why it was not adopted, what is blocking it, and when it may be reopened, all in append-only form.
