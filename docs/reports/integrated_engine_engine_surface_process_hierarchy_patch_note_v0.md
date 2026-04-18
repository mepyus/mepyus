# Integrated Engine Engine Surface Process Hierarchy Patch Note v0

## 1. Verdict

PASS_WITH_NOTE

The Engine Surface was adjusted so it reads first as request -> process boundary -> return material -> validation/deposit candidate, rather than only as a return feed.

This patch does not implement real processing automation. It clarifies the visible hierarchy of existing engine-side CLI return material.

## 2. Round Goal

After User Surface hierarchy pruning, the next risk was Engine Surface reading as a list of returned Codex sessions.

The intended Engine Surface question is:

```text
What should be processed, what came back, and what is only candidate material?
```

This patch makes that question appear before recent return history.

## 3. Modified File

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`

## 4. What Changed

### Engine Operating Order

Added an engine-side operating order block:

```text
요청 후보를 확인하고, 처리 경계를 본 뒤, 반환/검증/기록 후보를 나눈다.
```

This reinforces that Engine is a processing/return surface, not a judgment authority.

### Four-Step Engine Reading

Added a four-card first reading:

1. 요청 후보
2. 처리 경계
3. 반환 재료
4. 검증 / 기록 후보

This makes the active material read as a process chain.

### Recent Returns Lowered

Recent processing returns were moved into a collapsed support section:

```text
support recent processing returns
```

This reduces the return-feed feel while keeping trace access available.

## 5. What Was Intentionally Not Done

- No actual engine process runner.
- No request packet generation.
- No deposit ingestion.
- No canonical promotion.
- No validation automation.
- No new surface.
- No multi-work board.

## 6. Verification

Passed:

- `npm run build`
- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py app/core/runtime/viewer_server.py`

## 7. Watchpoints

1. The Engine Surface still uses `vectorfl_engine_surface_mock.tsx` as a support/mock body.
2. Request candidates are not executed automatically.
3. Return material is still not validation complete.
4. Deposit candidates remain not ingested and not canonical.
5. Engine must not absorb route judgment from VectorFL.

## 8. Next Smallest Step

Write a round closeout for the current surface exposure and hierarchy pass.

Then browser-check whether:

- User reads as purpose / decision / assignment.
- VectorFL reads as evidence / packet / mediation.
- Engine reads as request / process / return material.

Only after this should another implementation target be selected.
