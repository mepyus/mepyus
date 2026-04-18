# folder_status / app/ui/integrated_engine

## 1. Folder Identity

- path: `app/ui/integrated_engine`
- role_guess: Current main integrated-engine UI implementation area.
- status_mode: `manual_current_status`
- last_updated: `2026-04-16`

## 2. Origin

This folder is the stable working UI area created from / adapted out of `gemini/mock_test`.

It is not a direct copy of the mock anymore. It is now the main UI surface where the integrated-engine 3-surface body and CLI-on-top operation path are being implemented.

## 3. Current Body

The UI preserves the fixed 3-surface interpretation:

| surface | current role |
| --- | --- |
| User Surface | goal / scope / team-role assignment / work organization / user decision. |
| VectorFL Surface | CLI conversation/control, reread, mediation, validation, route sorting. |
| Engine Surface | processing return, validation feed, extraction/deposit candidate material. |

## 4. Current Active Components

| component | current role |
| --- | --- |
| `VectorFLIntegrationShell.tsx` | main 3-surface shell; current integration point. |
| `CliHostControlPanel.tsx` | VectorFL-side CLI host/control panel. |
| `CommandHeaderPanel.tsx` | User surface goal/scope/material context header. |
| `ExecutionRoutePanel.tsx` | User surface route/assignment flow support. |
| `OperationLogPanel.tsx` | User surface operating log support. |
| `vectorfl_engine_surface_mock.tsx` | Engine surface mock body and return/process view. |
| `ui-components.tsx` | local UI primitives. |

## 5. Current On-Top CLI State

Implemented:

- Codex backend path through existing local CLI.
- CLI session artifacts under `runtime/cli_sessions`.
- structured return / deposit candidate / operator report.
- VectorFL-side CLI operation panel.
- VectorFL-side CLI conversational turn layer.
- turn route labels and route marks:
  - `vectorfl_reread`
  - `user_assignment_candidate`
  - `engine_request_candidate`
  - `deposit_candidate`
  - `hold`
- User-surface CLI assignment candidate view.
- User-surface internal team / role framework.
- User-surface team/role assignment framework.
- Koreanization data loop under User surface internal team / language 담당 role.
- language loop artifacts under `runtime/language_loops`.
- Engine-surface engine request candidate view.
- VectorFL validation / reread handoff queue.
- deposit candidate artifact with route / marks / user decision / not-ingested boundary.

Not implemented yet:

- persistent team registry.
- persistent VectorFL handoff queue.
- formal request packet generation from Engine request candidates.
- automatic deposition into space.
- Gemini adapter.

## 6. Important Boundary

This folder may implement UI behavior, but it must not redefine the integrated-engine baseline.

Do not add:

- fourth surface.
- generic multi-agent dashboard.
- governance/supervisor authority as core.
- final glossary or broad UI copy replacement.
- runtime truth claims without matching runtime artifacts.

## 7. Current Next Direction

The next implementation direction is:

1. Real UI validation of the complete first operating path.
2. Read-only pruning audit of older mock-derived panels.
3. Decide which held components remain proposal/support material.
4. Only after validation, consider persistence for team assignments or handoff queue.

## 8. Relationship Reset

Current relationship map:

- `VectorFLIntegrationShell.tsx` is the current main body.
- `CliHostControlPanel.tsx` is active VectorFL CLI conversation/control.
- `UserCliAssignmentPanel`, `InternalTeamAssignmentPanel`, `EngineCliReturnPanel`, and `VectorFLValidationQueuePanel` are active in-shell bridge panels.
- Older mock-derived panels remain design/support material unless explicitly used by the shell.

Reference note:

- `docs/reports/integrated_engine_three_surface_screen_relationship_reset_note_v0.md`

## 9. 2026-04-17 Body / Packet / Memory Lock

The 04-17 Obsidian reread locked a stronger operating interpretation:

- Body stays fixed as User / VectorFL / Engine 3 surfaces.
- Process is the shared operating physiology across the body.
- Lens is the temporary task purpose, such as translation, validation, implementation, alignment, or external-material analysis.
- Work packet is the basic screen unit. A panel is useful only when it helps the current work packet show purpose, evidence, mediation, and trace.
- Internal search / memory reread must happen before CLI execution when the task depends on existing space material.
- Memory is not storage; memory is prior material that changes the current task.
- Surface language should show human-readable phrases first and keep internal labels as secondary badges.

Reference notes:

- `docs/reports/integrated_engine_20260417_obsidian_source_ingest_classification_v0.md`
- `docs/reports/integrated_engine_body_packet_memory_lock_v0.md`
- `docs/reports/integrated_engine_surface_language_and_panel_application_backlog_v0.md`
- `docs/reports/integrated_engine_20260417_operating_lock_closeout_v0.md`

## 10. Current Next Direction After 2026-04-17 Lock

Before another broad feature patch, run a read-only screen audit against the 04-17 lock:

1. Check whether the current main shell reads as a work-packet operating screen, not a card collection.
2. Check whether active panels show purpose / memory / process / decision / sedimentation.
3. Check whether the internal language appears as secondary structure, not as the only readable language.
4. Check whether User surface team/role/internal-language work is framed as assignment and operation, while VectorFL remains mediation/reread and Engine remains processing/return.

Only after that audit should a bounded UI patch begin.
