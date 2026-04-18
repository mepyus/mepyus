# Integrated Engine Surface Projection Composition Patch Note v0

## 1. Verdict

PASS_WITH_NOTE.

This round corrected screen composition without adding another panel family. The patch moves the current UI away from “all information visible everywhere” and toward “same work package, different surface lens.”

## 2. Why This Is Not A New-Panel Patch

The issue was not that the integrated engine needed more visible objects. The issue was that previously created objects were too evenly exposed across surfaces, which made the screen feel like a mixed information board.

This patch therefore did three narrower things:

- reduced a large surface-local focus block into a compact projection cue
- reframed the User surface team area as current work-package assignment, not generic team management
- demoted duplicated Engine return metadata into a support detail section

No new surface, backend concept, manifest shape, CLI adapter, route automation, or promotion mechanism was added.

## 3. Reasoning Chain Used

The patch used the body / camera / lens reread as the guardrail:

- body: User / VectorFL / Engine remain the fixed integrated-engine body
- camera frame: instruction intake -> internal search -> evidence bundle -> VectorFL mediation -> User organization -> Engine processing -> VectorFL reflux -> record/sedimentation
- lens: the current CLI-on-top work package must be projected differently per surface

The same current object should not show the same density everywhere:

- User surface reads it as assignment / decision / hold material
- VectorFL surface reads it as evidence / route / reread / mediation material
- Engine surface reads it as request / process / return / validation / deposit material

## 4. What Changed

### Surface Current Object Focus

`SurfaceCurrentObjectFocus` was reduced from a large card-like focus block into a compact current-object projection cue.

It still preserves the key questions:

- what is this object on this surface?
- what authority state does it have?
- what is the next candidate action?
- what role is this surface applying?

But it no longer tries to behave like a full dashboard row.

### User Surface Assignment Area

`InternalTeamAssignmentPanel` now opens with the explicit reading:

- this is not a generic team management table
- this is where the current work package is attached to a team/role or held
- deeper evidence and engine process details stay in VectorFL / Engine

This keeps team/role visible without letting it become the whole User surface.

### Engine Surface Return Area

`EngineCliReturnPanel` keeps the front sequence:

1. request candidate
2. process boundary
3. return material
4. validation / record candidate

The older status / latest return / deposit metadata cards are still available, but now sit inside a collapsed support detail section. That keeps useful generated material without making Engine surface read like a broad feed of every state.

## 5. What Was Intentionally Not Changed

- No new panel family.
- No new surface.
- No multi-work board.
- No Gemini adapter.
- No async/background runner.
- No deposit ingestion automation.
- No manifest or read-map change.
- No UI copy finalization.
- No Koreanization final wording pass.

## 6. What Still Remains Manual

- The current work package is still not a fully persisted operating object.
- User goal, CLI purpose, and assignment candidate are related but not yet one formal object.
- Evidence bundle is still mostly ref/status based, not a deep internal search result.
- Engine process is still a bounded candidate/process/return view, not a full process execution model.
- The screen still needs browser-level validation for whether it feels like surface projection rather than information listing.

## 7. Watchpoints

1. If the compact focus cue becomes too weak, users may lose the shared-current-object thread.
2. If the User team panel expands again without current-package anchoring, it will drift back into generic team console.
3. If Engine support metadata is reopened as the primary reading, Engine surface may again look like a return feed rather than process surface.

## 8. Verification

Passed:

- `npm run build` in `app/ui/integrated_engine`
- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py app/core/runtime/viewer_server.py`

## 9. Next Smallest Validation Step

Open the main integrated-engine UI and check one live current object across User / VectorFL / Engine:

- User should feel like assignment / decision / hold.
- VectorFL should feel like evidence / mediation / route / reread.
- Engine should feel like request / process / return / validation material.

If the same object still feels like the same information dump on all three surfaces, the next correction should be another projection-composition pass, not a new feature.
