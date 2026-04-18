# VectorFL Operable Surface Server-Backed Migration v0

## Verdict

Do not keep growing `vectorfl_operable_surface` as static generated HTML.

The static generator remains useful for snapshot/export reports, but the canonical operator surface needs a server-backed boundary before it grows into fake controls.

## Current Split

- Static snapshot/export: `scripts/run_vectorfl_operable_surface_set.py`
- Current generator module: `app/runtime/vectorfl_operable_surface_set.py`
- Live server candidate: `app/core/runtime/viewer_server.py`
- Canonical surface target: `runtime/views/vectorfl_operable_surface/`
- Paper proper grammar source: `runtime/views/vectorfl_paper_proper/`

## Migration Rule

- Keep the existing tab/page grammar.
- Do not add new tabs to solve action problems.
- Move action state behind `/api/vectorfl-paper/*`.
- Keep static HTML as a fallback snapshot, not the final operating surface.

## First Server-Backed Boundary

Minimum read endpoint:

- `GET /api/vectorfl-paper/state`

Required state groups:

- `current_ssot`
- `dry_run_preview`
- `comparison_summary`
- `worker_handoff`
- `codex_return`
- `gemini_review`
- `supervisor_decision`
- `guard`

Future write/action endpoints should be added only after the read boundary is stable:

- `POST /api/vectorfl-paper/actions/select-candidate`
- `POST /api/vectorfl-paper/actions/emit-handoff`
- `POST /api/vectorfl-paper/actions/run-codex-bridge`
- `POST /api/vectorfl-paper/actions/run-gemini-review`
- `POST /api/vectorfl-paper/actions/record-supervisor-decision`

## Guard

- No fake launch buttons.
- No browser-only controls that appear to persist but do not.
- No slot replacement.
- No candidate promotion.
- No gate close declaration.
- No weekend pilot merge.
- No page-shell continuation unless explicitly reopened.

## JSX Decision

JSX/React is the likely next UI shell once the state/action boundary is stable.

Do not scaffold a full React app before the API boundary is clear, because that would move the same ambiguity into a larger frontend. The next JSX step should consume `/api/vectorfl-paper/state` first and only then attach write actions.

## 2026-04-11 Layer Correction

The first `/vectorfl-paper` server-backed shell must not be treated as the final integrated operating page.

Correct classification:

- `/api/vectorfl-paper/state`: canonical state boundary.
- `/vectorfl-paper`: engine status console / substrate console.
- future top page: Paperclip-like integrated operating layer.

Why:

- `vectorfl_paper_proper` and `vectorfl_operable_surface` are internal/substrate surfaces.
- The integrated operating page is a higher product layer, closer to Paperclip's native company control plane than to the current internal VectorFL surface grammar.
- If the top page is built at the same layer as `proper` or `operable_surface`, it will become another status dashboard instead of an operating product.

Paperclip-native top-layer target:

- `Inbox triage -> Issues list -> IssueDetail -> IssueProperties -> runs/comments/approvals/activity`
- `Agents list -> AgentDetail -> instructions/configuration/skills/runs/budget`
- `Dashboard / Goals / Costs / Approvals / Activity / Org / Settings`

VectorFL top-layer translation:

- `work intake`: what needs attention now.
- `case/work board`: scenario-bearing work units.
- `work detail`: selected work packet, comments, runs, returns, approvals.
- `right inspector`: assignment, organ/lane, gate, refs, status.
- `organ detail`: instruction bundle, configuration, skills/tools, runs, budget/limits.
- `audit/governance`: append-only trace, approvals, hold/reopen decisions.

New rule:

- Do not label the server-backed status shell as the canonical integrated operating page.
- Use it as substrate state and debugging console.
- The real integrated page should imitate Paperclip's product layer structure first, then translate names into VectorFL.
