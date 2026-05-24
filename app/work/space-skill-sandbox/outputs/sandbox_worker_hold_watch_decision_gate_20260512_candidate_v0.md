# Sandbox / Worker / HOLD-WATCH Decision Gate 2026-05-12 Candidate v0

## 1. Status

```text
Document = decision gate candidate
Status = CANDIDATE_DECISION_GATE
Authority = pre-action structure only
Not baseline
Not official workflow
Not automation
Not router
Not schema
Not current-position update
```

## 2. Why This Exists

The minimum operating structure map identified the missing piece:

```text
Sandbox / Worker / HOLD-WATCH Decision Gate
```

The gate exists to prevent this drift:

```text
interesting idea -> immediate sandbox
unclear task -> worker packet
smooth language -> assumed structure
return record -> approval
```

## 3. Direct Rule

```text
Do not choose an action mode until the trigger, failure condition, and return path are visible.
```

## 4. Inputs To The Gate

Before this gate can be used, record:

```text
Trigger:
Existing Contact:
Selected Active Flow:
Blurry Field:
Line / Axis Candidate:
Failure Condition:
Return Path:
User Judgment Needed?:
```

If these are missing:

```text
Placement = HOLD_NEEDS_STRUCTURE
```

## 5. Output Options

The gate can return only one of these:

```text
THINK_MORE
SANDBOX_TRIAL
WORKER_PACKET
WATCH
HOLD
USER_JUDGMENT_REQUIRED
RETURN_ONLY
```

## 6. Option Meanings

### THINK_MORE

Use when:

```text
Line/Axis is still unclear.
The idea is promising but not yet testable.
Failure condition is not nameable.
```

Must return:

```text
what is unclear
which field is blurry
next smallest reading
```

### SANDBOX_TRIAL

Use when:

```text
There is a bounded transformation to try.
The original space will not be modified.
The test can fail visibly.
The return path is known.
The result can be small.
```

Must not use when:

```text
the goal is only to make the structure look real
failure condition is vague
the sandbox output would be mistaken for product/original
```

### WORKER_PACKET

Use when:

```text
a bounded worker can act without inferring the whole space
read/do-not-read scope is clear
forbidden actions are clear
success criteria are clear
return format is clear
```

Must not use when:

```text
worker would need hidden context
placement judgment is required
baseline/current-position decision is required
the task is actually philosophical direction setting
```

### WATCH

Use when:

```text
there is value, but evidence is thin
over-promotion risk is visible
the idea should remain available but not acted on yet
```

Must return:

```text
what to watch
what evidence would strengthen it
what would make it drop to HOLD/DISCARD
```

### HOLD

Use when:

```text
source is missing
trigger is unclear
failure condition is absent
return path is absent
action would create premature structure
```

Must return:

```text
what is missing
what must be supplied before retry
```

### USER_JUDGMENT_REQUIRED

Use when the next move would:

```text
promote candidate to baseline
accept a workflow as official
choose a real practical input with user consequences
approve helper/script implementation
update current-position as an anchor
change source-space behavior
```

### RETURN_ONLY

Use when:

```text
the result is useful as memory,
but no action should follow yet.
```

Example:

```text
recover a judgment, write watch, stop.
```

## 7. Gate Questions

Ask in order:

```text
1. Is the trigger clear?
2. Is the existing contact clear?
3. Is a Line or Axis visible?
4. Is there a failure condition?
5. Is there a return path?
6. Is original space protected?
7. Can a small sandbox test fail visibly?
8. Can a worker act without hidden context?
9. Is user judgment required?
10. What is the smallest non-promoting next action?
```

## 8. Quick Decision Table

| Condition | Gate output |
|---|---|
| trigger/contact missing | `HOLD` |
| Line/Axis unclear but promising | `THINK_MORE` |
| useful but evidence thin | `WATCH` |
| bounded trial exists + failure visible + return path exists | `SANDBOX_TRIAL` |
| read/do-not-read + forbidden + success + return format clear | `WORKER_PACKET` |
| candidate promotion / baseline / current-position / script implementation | `USER_JUDGMENT_REQUIRED` |
| useful judgment recovered but no action needed | `RETURN_ONLY` |

## 9. Apply To Current 05-12 State

Input:

```text
05-12 Common Growth Frame
```

Current knowns:

```text
Trigger = continue building while referencing space
Existing Contact = objective asset inventory + trace-to-memory + quick map
Line = Common Growth Frame Line
Axis = depth/surface, non-premature pipeline, execution boundary, falsification
Failure Condition = named but not yet stressed
Return Path = growth trace / active surface / line-axis detection records
```

Gate output:

```text
THINK_MORE -> SANDBOX_TRIAL_PREP
```

Reason:

```text
Line/Axis is clearer now.
But the next sandbox trial target is not chosen.
Choosing a practical real-world input may require user judgment.
So the safe next step is to prepare sandbox trial criteria, not launch a sandbox trial yet.
```

## 10. Next Non-Promoting Action

```text
Create Sandbox Trial Criteria for:
  what qualifies for sandbox,
  what remains WATCH/HOLD,
  what requires worker packet,
  what requires user judgment.
```

Do not yet:

```text
run a sandbox trial
dispatch Gemini
create automation
declare workflow
update current-position
```

## 11. Watch

```text
gate becomes router
gate output becomes approval
sandbox becomes default action
worker packet used to avoid user judgment
WATCH becomes hidden backlog
HOLD becomes forgotten material
```

`STATUS: SANDBOX_WORKER_HOLD_WATCH_DECISION_GATE_PREPARED`
