# Integrated Engine VectorFL Density Hierarchy Patch Note v0

## 1. Verdict

PASS_WITH_NOTE

VectorFL Surface now starts with a mediation process map before the dense CLI packet panel.

This patch does not add a new feature. It reuses existing panels by assigning them to the integrated-engine process:

```text
internal search / evidence
-> packet formation
-> CLI tool call
-> return / reread
-> line / intervention support
```

## 2. Round Goal

After User and Engine hierarchy corrections, VectorFL remained the densest surface.

That density is appropriate because VectorFL is the mediation surface. The risk was not density itself. The risk was density without a visible process order.

This patch makes VectorFL first answer:

```text
Is this work package well-formed enough to move, or should it be reread/repaired?
```

## 3. Modified File

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`

## 4. What Changed

### Added VectorFL Mediation Process Map

The first VectorFL body section now shows:

1. 내부 탐색 / 근거
2. 패킷 형성
3. CLI 도구 호출
4. 반환 / 재독해

This gives the dense VectorFL surface a process spine without creating a new shared dashboard.

### Reused Existing Panels

Existing panels were not discarded.

They were reassigned:

| existing panel | reused as |
| --- | --- |
| `CliHostControlPanel` | main evidence gate / packet formation / CLI control body |
| `VectorFLValidationQueuePanel` | return-to-VectorFL reread / validation support |
| `FlowSummaryPanel` | line / intervention summary support |
| `Evidence Line Atlas` | evidence line support selector |
| selected line inspection card | line detail support |

### FlowSummary Lowered

`FlowSummaryPanel` is no longer the first large VectorFL body.

It is inside a support details section:

```text
support: line / intervention summary
```

This prevents line summary from replacing packet/evidence mediation.

### Line Atlas Kept As Support

Evidence Line Atlas remains visible as support, not central body.

This preserves useful mock-derived visual material without turning VectorFL into a line browser.

## 5. What Was Intentionally Not Done

- No new panel type.
- No multi-work board.
- No Gemini adapter.
- No actual search engine expansion.
- No deposit ingestion.
- No route automation.
- No selected-object behavior beyond the existing selected line support.

## 6. Verification

Passed:

- `npm run build`
- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py app/core/runtime/viewer_server.py`

## 7. Watchpoints

1. VectorFL is allowed to be dense, but density must stay process-ordered.
2. FlowSummary must remain support, not central body.
3. Line Atlas must remain support, not VectorFL's central gravity.
4. CLI must remain on-top tool call, not a fourth surface.
5. Evidence gate is still refs-based and not a full search engine.

## 8. Next Smallest Step

Run a browser pass across all three surfaces:

```text
User: purpose -> decision -> internal team assignment
VectorFL: evidence -> packet -> CLI -> return/reread -> line support
Engine: request -> process -> return -> validation/deposit
```

If continuing without user validation, the next safe step is a read-only panel reuse/pruning audit for remaining mock-derived panels.

Do not open multi-work board yet.
