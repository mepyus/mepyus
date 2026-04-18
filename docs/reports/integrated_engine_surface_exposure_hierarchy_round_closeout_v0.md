# Integrated Engine Surface Exposure Hierarchy Round Closeout v0

## 1. Verdict

PASS_WITH_NOTE

This round moved the current main UI closer to the intended integrated-engine screen:

```text
common identity, local density
```

The UI still needs browser validation, but the code now better separates:

- User = purpose / decision / assignment
- VectorFL = evidence / packet / mediation
- Engine = request / process / return material

## 2. What This Round Was For

The user identified a real risk:

If every page shows all space information, the three-surface split loses its purpose.

This round therefore did not add multi-work board, Gemini adapter, search expansion, or automation. It corrected information exposure and hierarchy.

## 3. Completed Steps

### Step 1. Surface Exposure Budget Audit

Created:

- `docs/reports/integrated_engine_surface_exposure_budget_audit_v0.md`

Locked principle:

```text
shared spine = orientation only
User = assignment / decision density
VectorFL = evidence / mediation density
Engine = process / return density
```

### Step 2. Shared Spine Slimming

Changed:

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`

The shared spine no longer shows detailed evidence bundle reading, packet lens, expected return, or full manual-field list.

It now stays closer to:

- active turn
- short purpose
- state / route
- authority state
- evidence readiness
- surface role / next

### Step 3. User Surface Hierarchy Pruning

Changed:

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`

Created:

- `docs/reports/integrated_engine_user_surface_hierarchy_pruning_patch_note_v0.md`

User Surface now reads in this order:

1. current object as assignment / decision candidate
2. purpose and goal
3. user decision / work candidate
4. internal team / 담당 assignment
5. collapsed support route / log panels

### Step 4. Engine Surface Process Hierarchy

Changed:

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`

Created:

- `docs/reports/integrated_engine_engine_surface_process_hierarchy_patch_note_v0.md`

Engine Surface now begins with:

1. 요청 후보
2. 처리 경계
3. 반환 재료
4. 검증 / 기록 후보

Recent returns were lowered to support.

## 4. Verification

Passed after patches:

- `npm run build`
- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py app/core/runtime/viewer_server.py`

## 5. What Improved

### User Surface

Now more clearly answers:

```text
What should I decide, assign, hold, or send back?
```

### VectorFL Surface

Still holds the dense evidence / packet / CLI mediation body.

This is correct because VectorFL is the mediation surface.

### Engine Surface

Now more clearly answers:

```text
What is request material, what is process boundary, what came back, and what is only candidate material?
```

## 6. What Still Remains Thin

1. `CommandHeaderPanel` still carries mock-era stats/info boxes and may need a user-surface purpose-only pass.
2. VectorFL surface is still dense and may need a small hierarchy pass after browser validation.
3. Engine mock body is still broad and may need pruning into support-only sections.
4. The work package itself is still not persisted as a formal object.
5. The internal search gate is still refs-based, not an actual search engine.

## 7. What Was Not Opened

- Multi-work board
- Gemini adapter
- Async/background expansion
- Deposit ingestion
- Promotion/canonicalization
- Runtime binding
- Persistent team registry
- Persistent packet registry
- Final glossary / UI copy lock

## 8. Browser Validation Checklist

Open the main UI and check:

```text
User Surface:
Does it read as purpose -> decision signal -> internal team assignment?

VectorFL Surface:
Does it read as evidence gate -> packet formation -> CLI mediation?

Engine Surface:
Does it read as request candidate -> process boundary -> return material -> validation/deposit candidate?

Shared Spine:
Does it stay thin enough to orient without becoming a dashboard?
```

## 9. Next Recommendation

Do a browser validation pass before another implementation.

If continuing without user validation, the safest next bounded correction is:

```text
VectorFL density hierarchy pass
```

Reason:

- User and Engine have now been adjusted.
- VectorFL is still the densest surface.
- It must remain dense, but it should clearly separate:
  - evidence gate
  - packet formation
  - CLI send
  - latest return
  - reread/validation support
  - line atlas support

Do not open multi-work board yet.
