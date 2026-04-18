# Integrated Engine Wording Watch Registry v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This registry records wording candidates that remain under use-observation watch.

It does not promote wording-only patch planning. It does not propose patch wording. It does not authorize scaffold, manifest, read-map, selected-object, trace UI, runtime binding, or extension work.

## 1. registry purpose

The purpose is to keep recoverable ambiguity visible without treating it as an immediate build or patch trigger.

Current operating state:

- stop-and-use / use observation mode remains active
- wording candidates are watched only when they affect use-time reading
- fixture scope, core-support trace boundary, and held-extension expectations are not wording issues by themselves

## 2. official watch entries

| watch_id | scenario family | surface | panel | wording candidate | status | watch state | reason | current classification | patch planning state |
|---|---|---|---|---|---|---|---|---|---|
| `wwr_s2_001` | `S2_vectorfl_origin_followup_reactivation` | `user_surface` | `request_organization_panel` | `incoming request` | `not promoted` | `keep` | recoverable first-pass ambiguity | repeated blind ambiguity; supported reread recovers | not opened |
| `wwr_s2_002` | `S2_vectorfl_origin_followup_reactivation` | `engine_surface` | `work_input_panel` | generic `request` | `not promoted` | `keep` | recoverable first-pass ambiguity | repeated blind ambiguity; supported reread recovers | not opened |

## 3. entry detail: `wwr_s2_001`

Candidate:

- `request_organization_panel` / `incoming request`

Observed ambiguity:

- In S2, blind first-pass can make the user surface look like it is receiving a fresh user-origin request.
- This happens when the VectorFL maturation trigger and S2 connection record are intentionally delayed.

Recovered reading:

- The user surface organizes a shaped follow-up request.
- The cause remains the VectorFL maturation-canvas signal.
- The connection record and follow-up request packet recover the intended route.

Official state:

- status: `not promoted`
- watch state: `keep`
- reason: recoverable first-pass ambiguity

Why not patch planning:

- supported reread recovers the route
- scenario reading was not blocked
- user surface role remains operating / distribution / decision
- S2-only repetition is not enough to justify narrowing general request organization language

## 4. entry detail: `wwr_s2_002`

Candidate:

- `engine_surface/work_input_panel` / generic `request`

Observed ambiguity:

- In S2, blind first-pass can make the engine surface look like it is receiving a fresh execution request.
- This happens when the follow-up packet context is intentionally delayed.

Recovered reading:

- The engine receives shaped follow-up input.
- The engine remains processing / execution / return-draft.
- The follow-up request packet and return route recover the intended reading.

Official state:

- status: `not promoted`
- watch state: `keep`
- reason: recoverable first-pass ambiguity

Why not patch planning:

- supported reread recovers the route
- scenario reading was not blocked
- engine does not become a judgment authority
- S2-only repetition is not enough to justify narrowing generic engine work-input language

## 5. non-watch items from S2

The following are not official wording watch entries in this registry:

| item | classification | reason |
|---|---|---|
| S2 connection record absent from primary read map | fixture-scope limitation | Follow-up samples are manually checked through panel-role grammar. |
| selected / selector expectation | hold-feature expectation leak | Selected-object behavior remains held and is not required for S2 reading. |
| trace density thinness | core-support trace boundary | Denser trace UI is not part of current core contract. |
| return route open state | not-a-problem | `user_decision_or_vectorfl_recheck` remains readable. |

## 6. operating rule

Do not reopen patch planning from this registry alone.

This registry only means:

- keep watching during use
- separate wording ambiguity from fixture and trace limits
- require stronger evidence before gate re-entry

## 7. hold boundary

Still held:

- selected-object behavior
- selected route state
- side-inspection value rendering
- trace UI
- runtime binding
- manifest shape changes
- read-map changes
- extension promotion
- wording patch application

## 8. closeout sentence

The two S2 wording candidates are officially registered as not promoted / watch keep items because both are recoverable first-pass ambiguities, not persistent wording confusions.
