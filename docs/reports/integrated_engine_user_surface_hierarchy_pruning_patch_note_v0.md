# Integrated Engine User Surface Hierarchy Pruning Patch Note v0

## 1. Verdict

PASS_WITH_NOTE

The User Surface was reorganized so its first reading is purpose -> decision signal -> internal team assignment -> support route/log.

This patch does not add features. It clarifies hierarchy and reduces support panels from reading as the user-surface body.

## 2. Round Goal

The previous surface exposure patch established:

```text
User = assignment / decision density
VectorFL = evidence / mediation density
Engine = process / return density
```

The remaining User Surface issue was that route/log support panels still appeared as part of the main operating body.

This patch makes User Surface answer first:

```text
What is the purpose?
What decision signal exists?
Which internal team / 담당 should receive this?
What support route/log detail is optional?
```

## 3. Modified File

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`

## 4. What Changed

### User Operating Order

Added a short user-surface operating order block above the user body:

```text
목적을 세우고, 결정 신호를 읽고, 내부팀/담당에게 배정한다.
```

This frames the surface as organization/decision, not evidence or engine inspection.

### Main User Body

The visible order is now:

1. Surface-local current object focus
2. User operating order
3. Command header / purpose
4. User decision / work candidate
5. Internal team / 담당 assignment
6. Collapsed support route/log panels

### Support Panels Lowered

`ExecutionRoutePanel` and `OperationLogPanel` are now inside a collapsed `support route / log panels` section.

This keeps them available without making them compete with:

- purpose
- decision signal
- internal team assignment

## 5. Why This Is Not A Feature Patch

No new data shape was added.
No new route was added.
No new team/role persistence was added.
No new CLI behavior was added.

This is only a hierarchy correction inside the existing User Surface.

## 6. What Remains Manual

- Team and role definitions remain local UI state.
- Assignment attachments remain local UI state.
- User approval / hold / package-opening authority is visible but not persisted as a formal object.
- Detailed reread, axis judgment, and validation still happen in VectorFL.

## 7. Verification

Passed:

- `npm run build`
- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py app/core/runtime/viewer_server.py`

## 8. Watchpoints

1. Do not turn User Surface into a team-management product.
2. Do not expose full evidence bundle on User Surface.
3. Do not hide decision authority behind internal team cards.
4. Do not let support route/log panels become the first reading again.
5. Do not treat local assignment attachment as stored approval.

## 9. Next Smallest Correction

Engine Surface should be checked next.

Reason:

- User now reads more clearly as purpose/decision/assignment.
- VectorFL already holds evidence/packet density.
- Engine still risks reading as a return feed rather than an active processing/return-material surface.

The next correction should be Engine process/return hierarchy, not multi-work board.
