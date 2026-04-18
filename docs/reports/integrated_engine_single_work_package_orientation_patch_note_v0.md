# Integrated Engine Single Work Package Orientation Patch Note v0

## 1. Verdict

PASS

This was a bounded orientation patch, not a feature expansion.

## 2. What Changed

Modified:

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`

The shell orientation band now reads:

```text
User Purpose
-> VectorFL Packet
-> CLI / Engine Return
-> VectorFL Reread
-> Decision / Deposit Candidate
```

## 3. Why This Was Needed

The old shell wording still described a broad visual flow:

```text
Goal/Scope/Material -> Line Reading -> Engine Processing -> Return Artifact
```

That no longer matched the actual process now being built. The screen is now trying to carry a work package through:

- user purpose
- VectorFL packet formation
- CLI / engine return
- VectorFL reread
- user decision or deposit candidate

Leaving the older wording in the shared shell made the user mentally reconnect the process.

## 4. Why This Is Safe

- No surface was added.
- No panel order changed.
- No runtime contract changed.
- No manifest shape changed.
- No CLI behavior changed.
- No work package registry was introduced.

The patch only aligns the top-level orientation label with the process already visible below it.

## 5. What Remains Manual

1. User purpose and VectorFL CLI turn purpose are still not one formal persisted work package object.
2. Evidence bundle still depends on provided refs and inferred state.
3. Deposit remains a candidate, not automatic sedimentation.
4. Multi-work handling remains unopened.

## 6. Watchpoints

1. The orientation band must stay thin.
2. It must not become a dashboard.
3. It must not imply deposit is canonical or complete.

## 7. Verification

Passed:

- `npm run build`
- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py app/core/runtime/viewer_server.py`

## 8. Next Smallest Validation Step

Use the browser to walk one real work package:

```text
User Surface -> VectorFL Surface -> Send Codex Turn -> Engine Surface -> back to VectorFL
```

Pass condition:

```text
The user can tell which surface owns purpose, packet formation, return material, reread, and candidate decision without opening raw runtime files first.
```
