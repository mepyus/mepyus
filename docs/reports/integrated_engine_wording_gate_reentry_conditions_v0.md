# Integrated Engine Wording Gate Re-Entry Conditions v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This document defines when wording gate review may be reopened for current watch entries.

It does not reopen the gate now. It does not create patch wording. It does not approve patch planning or implementation.

## 1. purpose

The purpose is to prevent recoverable ambiguity from becoming premature wording churn while preserving a clear path back to review if future use shows a stronger problem.

This applies first to:

- `request_organization_panel` / `incoming request`
- `engine_surface/work_input_panel` / generic `request`

Both are currently:

- status: `not promoted`
- watch state: `keep`
- reason: recoverable first-pass ambiguity

## 2. current lock state

Current operating mode:

- stop-and-use / use observation mode

Current gate state:

- gate review completed for S2
- no wording-only patch planning opened
- no patch wording created
- no scaffold, manifest, read-map, runtime, selected-object, trace UI, or extension work authorized

## 3. valid re-entry conditions

The wording gate may be reopened only if at least one valid re-entry condition appears during future use observation.

| condition_id | re-entry condition | why it matters |
|---|---|---|
| `reentry_001` | Similar blind ambiguity recurs in S1 or S3, not only S2. | Cross-scenario recurrence shows the wording may affect baseline reading beyond one follow-up fixture. |
| `reentry_002` | Natural use accumulates the same ambiguity again without a deliberately artificial blind delay. | Natural recurrence is stronger evidence than a controlled first-pass stress test. |
| `reentry_003` | Supported reread recovery weakens. | If connection records, packets, and intended reading order no longer recover the route, wording may be hiding a baseline rule. |
| `reentry_004` | Scenario reading is actually blocked or substantially delayed by the wording. | Blocking use crosses the threshold from recoverable ambiguity to operational confusion. |
| `reentry_005` | The same wording causes request / return / reflux or surface-role confusion across observations. | Role separation is a core baseline boundary. |

## 4. excluded re-entry conditions

The wording gate must not be reopened for the current candidates based only on:

| excluded item | why excluded |
|---|---|
| S2-only blind ambiguity reconfirmed again | It has already been observed and classified as recoverable; repetition in the same artificial pass does not add enough evidence. |
| fixture-scope limitation | Follow-up and drift samples are manually checked through panel-role grammar by current interface contract. |
| hold-feature expectation leak | Selected-object behavior, route selection, and side-inspection value behavior remain held. |
| trace density disappointment | Denser trace UI is outside current core contract. |
| selected-object absence itself | Absence is intentional and held; it is not wording confusion. |
| runtime binding absence | Current scaffold is not a runtime data binding implementation. |
| preference for more specific S2 wording | Specificity preference alone does not justify reducing generic panel coverage. |

## 5. re-entry evidence requirement

Any re-entry package should record:

- scenario family
- surface
- panel
- wording candidate
- observed ambiguity
- intended reading
- whether supported reread recovered
- whether scenario reading was blocked
- whether the issue is wording, fixture scope, trace boundary, or held extension

Do not create patch wording inside the re-entry evidence package.

## 6. re-entry outcome options

If re-entry conditions are met, the gate can return one of these outcomes:

| outcome | meaning |
|---|---|
| `continue watch` | Evidence is stronger but still recoverable or narrow. |
| `eligible for wording-only patch planning` | Evidence shows repeated use-time confusion, and a wording-only plan may be prepared separately. |
| `hold` | The issue depends on selected-object, trace UI, runtime binding, read-map changes, or extension promotion. |

No outcome in this document authorizes immediate scaffold edits.

## 7. generality protection rule

Re-entry must consider generality loss.

Do not promote wording planning if the likely fix would:

- make user request organization sound S2-only
- make engine work input sound follow-up-only or reprocess-only
- weaken S1 user-origin normal loop reading
- weaken S3 drift-reprocess reading
- imply a new behavior branch not present in current scaffolds

## 8. hold boundary

Still held:

- selected-object behavior
- selected route state
- side-inspection value rendering
- denser trace UI
- runtime binding
- manifest shape changes
- read-map changes
- extension promotion
- wording patch application

## 9. closeout sentence

The wording gate reopens only when ambiguity becomes cross-scenario, naturally recurrent, weakly recoverable, or use-blocking; S2-only recoverable blind ambiguity stays in watch.
