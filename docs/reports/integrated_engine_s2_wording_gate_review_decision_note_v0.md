# Integrated Engine S2 Wording Gate Review Decision Note v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

S2 follow-up / reactivation wording gate review is complete.

Decision:

- do not promote either candidate to wording-only patch planning now
- keep both as watch items
- treat both as gate-review subjects only
- continue stop-and-use / use observation mode

## 1. decision table

| candidate | observed status | gate review decision | reason |
|---|---|---|---|
| `request_organization_panel` / `incoming request` | repeated blind first-pass ambiguity; supported reread recovers | not promoted; watch keep; gate-review subject only | The phrase can bias first reading toward user-origin request, but connection record and follow-up packet recover the intended S2 route. |
| `work_input_panel` / generic `request` | repeated blind first-pass ambiguity; supported reread recovers | not promoted; watch keep; gate-review subject only | The phrase can bias first reading toward fresh engine execution, but follow-up packet and return route recover engine processing of shaped input. |

## 2. why not promoted

The wording-only patch promotion gate is not fully satisfied for patch planning because:

- neither candidate blocks scenario reading
- neither candidate remains confusing after supported reread
- neither candidate creates role collapse
- neither candidate requires structural correction
- supported reread follows the current intended reading order
- patching now risks narrowing general panel wording around one S2 fixture

Both candidates satisfy review eligibility, but not patch-planning promotion.

## 3. ambiguity vs persistent confusion

Current classification:

| candidate | blind first-pass | supported reread | final classification |
|---|---|---|---|
| `incoming request` | can sound user-origin fresh | recovers to VectorFL-origin signal organized by user surface | recoverable first-pass ambiguity |
| generic `request` | can sound fresh engine input | recovers to shaped follow-up input for engine processing | recoverable first-pass ambiguity |

Persistent confusion would require one of these:

- intended reading does not recover after support material is read
- scenario route cannot be reconstructed without a wording patch
- repeated cross-scenario use shows the same phrase hiding a baseline rule
- the phrase causes request / return / reflux role collapse

None of those conditions is active.

## 4. supported reread compatibility

Supported reread is compatible with the current baseline.

For S2, the accepted route is:

```text
VectorFL-origin maturation signal
-> user-surface follow-up organization
-> engine-side processing / return
-> user decision or VectorFL recheck remains open
```

This route is recovered through:

- S2 connection record
- maturation object
- follow-up request packet
- follow-up return packet
- protocol note that this path is shaped follow-up, not bypass

Therefore the ambiguity is not a current structure failure.

## 5. generality-loss risk

Patch planning is deferred because a narrow S2-focused wording change could create loss elsewhere.

Risk areas:

- user surface wording could become too follow-up-specific and weaken S1 user-origin request reading
- engine surface wording could become too reactivation-specific and weaken generic processing input reading
- local copy could imply a special behavior branch that the scaffold does not implement
- a wording change could accidentally suggest selected-object behavior, trace UI, or route-state selection

No patch wording is proposed in this decision note.

## 6. future promotion threshold

Either candidate may return to gate review only if future observation shows stronger evidence.

Evidence that would matter:

- persistent confusion after supported reread
- the same ambiguity blocks a scenario
- the same wording problem repeats across S1, S2, and S3
- the confusion hides a baseline rule rather than merely delaying recognition
- a future review can show that a wording-only change preserves generic panel coverage

Until then, the correct status is watch keep.

## 7. global recommendation

Recommended mode:

- continue use observation
- do not enter patch planning
- do not write patch copy
- keep the current baseline in stop-and-use mode

Next safe action:

- observe another scenario family only if a concrete use-time confusion appears during actual use

## 8. what remains on hold

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

S2 wording evidence is strong enough to keep watching, but not strong enough to promote either recoverable ambiguity into wording-only patch planning.
