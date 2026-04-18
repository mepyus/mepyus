# Integrated Engine Surface Exposure Budget Patch Closeout v0

## 1. Verdict

PASS_WITH_NOTE

The UI was adjusted toward the current screen principle:

```text
common identity, local density
```

This round did not add a new feature. It reduced shared/global exposure and moved surface detail back toward the surface responsible for that detail.

## 2. Round Goal

The goal was to stop the shared spine and surface focus layers from becoming an all-information dashboard.

The fixed interpretation remains:

- User Surface: assignment / decision / internal team operation.
- VectorFL Surface: evidence / mediation / packet / route / CLI control.
- Engine Surface: request / process / return / validation / deposit material.
- CLI: on-top tool layer, not a fourth surface.

## 3. Internal Reread Basis

This patch follows:

- `docs/reports/integrated_engine_direction_reset_note_v0.md`
- `docs/reports/integrated_engine_shared_operational_language_growth_note_v0.md`
- `docs/reports/integrated_engine_surface_exposure_and_shared_language_boundary_v0.md`
- `docs/reports/integrated_engine_surface_information_exposure_reread_note_v0.md`
- `docs/reports/integrated_engine_surface_exposure_budget_audit_v0.md`

Key reread:

```text
The user should not carry the full internal space at once.
The three surfaces are role-filtered readings, not duplicated state views.
```

## 4. Modified Files

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`

Added documentation:

- `docs/reports/integrated_engine_surface_exposure_budget_audit_v0.md`
- `docs/reports/integrated_engine_surface_exposure_budget_patch_closeout_v0.md`

## 5. What Was Moved Down From Shared Layer

The shared spine no longer shows a second row containing:

- detailed evidence bundle reading
- packet lens / expected return
- full manual field list

It now stays closer to orientation:

- active turn
- short purpose
- state / route
- authority state
- evidence readiness summary
- surface role / next

This keeps the same current object visible without making the shell a global dashboard.

## 6. Surface-Local Exposure Adjustments

### User Surface

User first focus now reads evidence state as decision readiness, not evidence inspection.

User text was adjusted toward:

- 내부팀 업무 배정
- 사용자 결정 / 업무 후보
- 사용자면에서 읽는 방식
- 자세한 판단 위치

Internal labels such as `user_assignment_candidate` remain as small badges or supporting text.

### VectorFL Surface

VectorFL keeps the full internal search / evidence bundle gate and packet formation area.

That is intentional because VectorFL is the mediation and evidence-density surface.

### Engine Surface

Engine first focus now reads evidence state as request readiness, not evidence inspection.

Engine text was adjusted toward:

- 처리 반환 / 검증 재료
- 엔진 요청 후보
- 최근 처리 반환
- 추출 / 기록 후보 재료

Internal labels such as `engine_request_candidate` remain as badges or supporting text.

## 7. What Was Intentionally Not Done

- No multi-work board.
- No new surface.
- No Gemini adapter.
- No async/background expansion.
- No deposit ingestion or promotion.
- No search engine expansion.
- No persistent packet registry.
- No final glossary or UI copy lock.

## 8. Verification

Passed:

- `npm run build`
- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py app/core/runtime/viewer_server.py`

## 9. Watchpoints

1. The shared spine is still visible enough to orient, but it must not grow again.
2. User Surface still contains several support panels; they should stay subordinate to assignment/decision.
3. VectorFL remains dense; this is correct, but CLI must still read as on-top tool, not a fourth surface.
4. Engine Surface still uses a mock-derived body; it should be audited before further process concretization.
5. Human-readable copy improved but is not final UI wording.

## 10. Next Smallest Step

Run a browser validation against the exposure budget:

```text
User = can I assign/decide/hold?
VectorFL = is the packet evidence-ready and well mediated?
Engine = what is request/process/return/deposit candidate material?
```

If this passes, the next bounded correction should be either:

- User Surface hierarchy pruning, if the user still feels team/work panels are too mixed.
- Engine process concretization, if Engine still feels like a return feed instead of processing surface.

Do not open multi-work board yet.
