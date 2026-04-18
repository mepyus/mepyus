# Integrated Engine Shared Evidence Gate Continuity Patch Note v0

## 1. Verdict

PASS_WITH_NOTE

The internal search / evidence bundle gate now surfaces into the shell-level shared operating spine and each surface-local current object focus layer.

This is not a new feature, not a multi-work board, and not a search engine. It is a continuity correction so the three fixed surfaces can read the same current work package evidence readiness.

## 2. Why This Follows The Evidence Bundle Gate

The previous patch made the VectorFL packet formation layer evidence-aware:

```text
packet input details
-> internal search / evidence bundle gate
-> current work packet formation
-> Send Codex Turn
```

However, that gate was still mostly local to the VectorFL CLI panel. User and Engine could see the same latest turn, but not the current packet's evidence readiness.

That left a small but important gap:

- User could read assignment / decision candidate without seeing whether evidence was ready.
- Engine could read request / validation / deposit material without seeing whether the packet was evidence-backed.
- The shared spine could show current object continuity, but not evidence-gate continuity.

## 3. What Changed

Changed files:

- `app/ui/integrated_engine/CliHostControlPanel.tsx`
- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`

`CliHostControlPanel` now emits a thin current packet draft summary upward:

- purpose
- task lens
- internal search status
- evidence summary
- evidence limitation
- evidence count
- evidence kinds
- next route candidate
- expected return shape
- manual fields still needed

The shell stores this as the current work packet draft and shows it in:

- `SharedOperatingSpine`
- `SurfaceCurrentObjectFocus` for User
- `SurfaceCurrentObjectFocus` for VectorFL
- `SurfaceCurrentObjectFocus` for Engine

## 4. Shared Spine Continuity

The shared spine now includes a second compact row for:

- evidence gate
- evidence bundle reading
- packet lens / expected return
- still manual

This makes the shared object read as:

```text
same turn
+ same route / authority state
+ same evidence readiness
```

The spine remains shell-level and does not become a fourth surface.

## 5. Surface-Local Focus Continuity

Each surface focus layer now includes `evidence readiness`.

### User Surface

Reads evidence readiness as:

```text
organization should wait for evidence-aware packet
```

This keeps User from becoming evidence owner, while still showing that assignment / decision should not ignore evidence state.

### VectorFL Surface

Reads evidence readiness as:

```text
VectorFL forms evidence bundle first
```

This reinforces VectorFL as the mediation and packet formation surface.

### Engine Surface

Reads evidence readiness as:

```text
processing should read evidence bundle before request
```

This keeps Engine from looking like it should execute source-free request candidates.

## 6. What Still Remains Manual

- Evidence refs are still mostly user-provided.
- The gate does not run repository-wide internal search.
- The packet draft summary is not persisted as a separate operating object.
- User and Engine can read evidence readiness, but they do not yet act on it as a formal workflow gate.
- No deposit ingestion, promotion, or canonicalization was added.

## 7. Watchpoints

1. Do not mistake shared evidence visibility for completed internal search.
2. Do not make User Surface responsible for evidence assembly.
3. Do not make Engine Surface execute because evidence status exists.
4. Do not promote the draft summary into a registry before one work package path is stable.
5. Do not open multi-work board until the single-work package physiology is easier to read.

## 8. Verification

Passed:

- `npm run build`
- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py app/core/runtime/viewer_server.py`

Browser check still needed:

```text
shared spine
-> surface-local focus
-> VectorFL evidence gate
-> packet formation
```

Pass condition:

- evidence readiness appears in the shared spine
- User / VectorFL / Engine focus layers all show the same packet evidence state
- this does not read as a new surface
- this does not read as a giant dashboard

## 9. Next Smallest Validation Step

Use the UI with one bounded Codex turn and check whether the user can understand:

```text
this is the same current work package
this is its evidence readiness
this is still candidate-only
this is not ingested or canonical
```

If that passes, the next correction should be chosen between:

- Engine process concretization for one active work package
- surface language correction so human-readable language leads and internal labels become badges

Do not open multi-work board yet.
