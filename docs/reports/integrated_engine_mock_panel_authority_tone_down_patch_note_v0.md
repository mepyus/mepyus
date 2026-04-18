# Integrated Engine Mock Panel Authority Tone-Down Patch Note v0

## 1. Verdict

PASS_WITH_NOTE

Existing mock-derived Engine panels were not removed. Their authority language was toned down so they read as process/support material instead of control-room or supervisor authority.

## 2. Round Goal

The user asked to consider how existing panels can be reused against the engine process.

The reuse audit found that several mock panels are useful but must remain support:

- asset inventory
- watchpoints
- trace console
- bridge support
- recommendation queue

The risk was not the panels themselves. The risk was authority language such as `CONTROL ROOM` and `SupervisorQueue`.

## 3. Modified File

- `app/ui/integrated_engine/vectorfl_engine_surface_mock.tsx`

## 4. What Changed

### Engine Header

Changed:

```text
ENGINE / CONTROL ROOM
공간 엔진 컨트롤면
```

To:

```text
ENGINE / PROCESS MATERIAL
공간 엔진 처리면
```

This keeps the Engine surface as processing/return material, not authority/control room.

### Pipeline Label

Changed:

```text
Primary Control Pipeline
```

To:

```text
Primary Processing Pipeline
```

### Secondary Layer Label

Changed:

```text
Secondary Monitoring Layer
Asset / Watch / Trace Audit
```

To:

```text
Secondary Support Layer
Asset / Watch / Trace Support
```

### Supervisor / Bridge Panels

`SupervisorQueuePanel` and `BridgePanel` now sit under a collapsed support section:

```text
optional recommendation / bridge support
```

With a boundary note:

```text
이 영역은 governance나 supervisor authority가 아니다. 추천/연결 후보를 passive support로만 읽는다.
```

## 5. What Was Intentionally Not Done

- No deletion of mock-derived panels.
- No promotion of asset inventory to central panel.
- No new governance/supervisor layer.
- No runtime truth claim.
- No fresh data binding.
- No new surface.

## 6. Verification

Passed:

- `npm run build`
- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py app/core/runtime/viewer_server.py`

## 7. Watchpoints

1. `SupervisorQueuePanel` name still exists in code as a component name, but it is visually demoted to support.
2. Engine mock remains a view draft, not runtime truth.
3. Asset inventory should stay support unless later tied to active work package memory.
4. Bridge support should not imply automatic bridge authority.
5. Space health should not become global score truth.

## 8. Next Smallest Step

Run a browser pass after this authority tone-down.

If continuing implementation, the next safe step is not multi-work board. It is a read-only single work package walkthrough to check:

```text
User purpose / assignment
-> VectorFL evidence / packet
-> Engine process / return
-> VectorFL reread
-> User decision or deposit candidate
```
