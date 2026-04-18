# VectorFL Page Shell Codex/Gemini Operating Subject Merge Plan v0

## Verdict

- `vectorfl_operable_surface` is where the Codex/Gemini bridge behavior has been validated as an operable surface.
- `vectorfl_page_shell` is the better long-term candidate for the future integrated operating engine shell.
- Do not turn `page_shell` into a page for only one current pilot process.
- Do not paste the full Paper proper surface into `page_shell`.
- Translate the verified bridge loop into a small, read-only operating-flow preview that `page_shell` can carry across its existing primary surfaces.

Core sentence:

- The immediate goal is operation/test/realization, but the process must remain in the architecture as a future operating-subject capability inside the integrated engine.

## Condensed-Brief Reading

The previous supervisor briefs imply four constraints that matter here:

- The goal is not to keep expanding Paper proper.
- The goal is not to merge weekend pilot or archive surfaces.
- The goal is to preserve a canonical operating flow: input/context -> handoff -> worker return -> cross-check -> supervisor decision -> validation/gate trace.
- The long-term target is not a one-off paper for one process, but a surface that can become an operating subject in the integrated runtime engine.

Therefore the merge unit is not a page.

The merge unit is:

- a read-only bridge state summary
- a flow-position label
- a return route
- a supervisor guard

## Current Structure Findings

### Operable Surface

Likely existing VectorFL Paper candidate:

- `runtime/views/vectorfl_operable_surface/index.html`
- `scripts/run_vectorfl_operable_surface_set.py`
- `app/runtime/vectorfl_operable_surface_set.py`

Relevant existing surfaces:

- `engine-overview`
- `case-detail`
- `external-resources`
- `agent-mcp-control`
- `trace-audit`
- `worker-inbox`

Current role:

- This surface already behaves like a Paperclip-style operable control surface.
- It has BOARD / INTAKE / WORK / TEAMS / CLI groups.
- It is the right place to verify concrete behavior and page-class mappings.

### Page Shell

Long-term integrated shell candidate:

- `runtime/views/vectorfl_page_shell/index.html`
- `scripts/run_vectorfl_page_app_shell.py`
- `app/runtime/vectorfl_page_app_shell.py`

Current primary surfaces:

- `current-reading`
- `cases-queue`
- `inputs-intake`
- `history-trace`
- `programs-connections`

Current role:

- `Current Reading` remains the semantic center.
- Other surfaces are entry/material/carry/boundary states.
- Contextual organ panels remain secondary drill-ins, not primary routes.

Important gap:

- `page_shell` currently does not read the Paper proper / Codex / Gemini / actual-export validation manifests directly.
- It uses route-aware mock data from `vectorfl_page_route_aware_mock` and `vectorfl_page_unified_mock`.

## Paperclip Application Rule

Paperclip's useful lesson is not "make more tabs".

The useful lesson is:

- Each tab/page has a setup role.
- Each tab/page preserves the current object.
- Each tab/page has a return route.
- Detail tabs keep work/comment/activity/config/runs close to the current object.
- Inbox and audit pages are first-class operational surfaces, not archive dumps.

For VectorFL:

- Tabs are acceptable only if they preserve the process.
- A tab that only lists content will hide flow.
- A tab must say: what it sets up, where it sits in the process, and where the result returns.

## Page Shell Translation Map

### `current-reading`

Purpose:

- Keep the current case / current reading as the semantic center.

Bridge material it should receive:

- compact live supervisor posture
- current SSOT label
- current decision posture
- next gate sentence

It should not receive:

- full validator dry-run detail
- candidate archive rows
- full Codex/Gemini raw prompts

Flow meaning:

- "This is what the supervisor is currently reading and why the loop is held or allowed."

### `cases-queue`

Purpose:

- Show operating cases / queues without forcing the user into detail too early.

Bridge material it should receive:

- small status chip for a bridge-backed case
- hold/current/reopen posture if tied to a visible case

It should not receive:

- full comparison manifest
- worker return text

Flow meaning:

- "This tells the supervisor which loop to enter, not the full loop outcome."

### `inputs-intake`

Purpose:

- Prepare and inspect material before it becomes current reading or worker input.

Bridge material it should receive:

- actual export candidate readiness
- reference-derived vs true host/export boundary
- selected validation anchor pointer
- handoff material readiness

It should not receive:

- slot replacement logic
- gate close declaration
- inbox_latest rendering without a true candidate

Flow meaning:

- "This is where material becomes candidate input, but not yet canonical replacement."

### `history-trace`

Purpose:

- Preserve trace, return, validation, and gate evidence.

Bridge material it should receive:

- Codex return summary
- Gemini review summary
- supervisor decision summary
- actual_export_only validator result
- dry-run preview status as preview-only
- comparison summary as summary-only

It should not receive:

- full archive rows
- weekend pilot surface content
- raw prompts unless explicitly opened later

Flow meaning:

- "This is the audit and gate trail for why the supervisor is holding, reopening, or continuing."

### `programs-connections`

Purpose:

- Show connected programs, adapters, and boundary state.

Bridge material it should receive:

- Codex bridge availability
- Gemini cross-check availability
- worker role distinction
- external worker return route

It should not receive:

- fake execution controls
- generalized multi-worker orchestration
- queue/scheduler abstractions

Flow meaning:

- "This is where the shell understands that Codex/Gemini are connected operating subjects, not page decorations."

### Contextual Organ Panels

Purpose:

- Keep the current organ and governance candidate close to the current reading.

Bridge material it should receive:

- accepted handoff input kinds
- recent return summary
- stop/hold conditions
- release condition / continue gate

It should not receive:

- complete proper page layout
- broad Paperclip ontology

Flow meaning:

- "This is where a worker-facing handoff or governance check becomes actionable without leaving current reading."

## Smallest Safe Implementation Shape

Add one read-only bridge preview object to the page shell data.

Candidate name:

- `paper_operating_bridge_preview`

It should be built from existing manifests only:

- `runtime/manifests/vectorfl_paper_codex_handoff_latest_v0.json`
- `runtime/manifests/vectorfl_paper_codex_return_latest_v0.json`
- `runtime/manifests/vectorfl_paper_gemini_review_latest_v0.json`
- `runtime/manifests/vectorfl_paper_supervisor_decision_latest_v0.json`
- `runtime/manifests/vectorfl_paper_actual_export_host_record_slot_v0.json`
- `runtime/manifests/vectorfl_paper_actual_export_gate_validation_latest_v0.json`
- `runtime/manifests/vectorfl_paper_actual_export_gate_validation_dry_run_v0.json`
- `runtime/manifests/vectorfl_paper_reference_candidate_validation_comparison_v0.json`

It should expose only compressed fields:

- `current_posture`
- `current_ssot_label`
- `preview_only_label`
- `summary_only_label`
- `codex_bridge_status`
- `gemini_review_status`
- `supervisor_decision`
- `gate_effect`
- `next_gate`
- `return_route`
- `guard_language`

It must not:

- write manifests
- emit handoffs
- run Codex
- run Gemini
- replace the current slot
- promote a candidate
- declare gate close

## Recommended Render Distribution

First render only compact blocks:

- `current-reading`: one posture strip.
- `history-trace`: one audit/gate summary block.
- `programs-connections`: one adapter/worker bridge status block.

Defer:

- `inputs-intake` candidate readiness rendering until the current-reading and history-trace reading stays clear.
- `cases-queue` bridge chips until there is more than one real case using this loop.

## Why This Matches The Long-Term Goal

This keeps the process in the shell without making a one-off process page.

The same pattern later generalizes to other operating loops:

- a bridge preview object
- surface-specific role projection
- current-reading center
- history-trace audit
- programs-connections adapter boundary
- governance/contextual panel for decision gates

That is closer to an integrated operating engine than a single Paper proper page.

## Next Step Before Implementation

Do not implement a full merge yet.

First implementation candidate, if approved:

- Add `paper_operating_bridge_preview` as a read-only data object in `build_vectorfl_page_app_shell_state`.
- Render one compact posture strip in `current-reading`.
- Render one compact audit/gate block in `history-trace`.
- Render one compact bridge availability block in `programs-connections`.
- Regenerate `runtime/views/vectorfl_page_shell/*`.

Verification must check:

- default page_shell generation remains read-only except writing its own HTML/JSON outputs
- no proper surface modification
- no weekend pilot dependency
- no slot replacement
- no gate close declaration
- current-reading remains the semantic center

