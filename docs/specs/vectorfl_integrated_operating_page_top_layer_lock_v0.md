# VectorFL Integrated Operating Page Top Layer Lock v0

## Verdict

The integrated operating page is not `vectorfl_paper_proper`, not `vectorfl_operable_surface`, and not the first `/vectorfl-paper` server-backed status shell.

It must be a higher product layer.

## Why

`vectorfl_paper_proper` and `vectorfl_operable_surface` expose internal/substrate state:

- current SSOT
- handoff/return/review manifests
- validation gates
- internal organ/lane surfaces
- trace/governance substrate

Those are necessary, but they are not yet the product-level operating surface.

The top page must behave more like Paperclip itself:

- a company/control-plane style shell
- work allocation first
- detail operation second
- right-side inspector for assignment/config/gate
- organ/agent detail for instruction/config/run/budget
- audit/governance as a first-class page class

## Native Paperclip Reference Line

Paperclip's high-level product line is:

- `Inbox triage`
- `Issues list`
- `IssueDetail`
- `IssueProperties`
- `runs / comments / approvals / activity`
- `Agents list`
- `AgentDetail`
- `instructions / configuration / skills / runs / budget`
- `Dashboard / Goals / Costs / Approvals / Activity / Org / Settings`

This is not a generic tabbed dashboard. It is a control plane.

## VectorFL Translation

Use Paperclip's product structure, but translate the names:

- `company boundary` -> `VectorFL operating workspace`
- `issue` -> `scenario-bearing work packet`
- `issue list` -> `work board`
- `issue detail` -> `work packet detail`
- `issue properties` -> `right-side assignment/gate inspector`
- `agent` -> `organ / lane / worker runtime`
- `agent detail` -> `organ runtime detail`
- `heartbeat run` -> `bounded organ/worker run`
- `approval` -> `hold / continue / reopen gate`
- `activity` -> `append-only trace/audit`
- `inbox` -> `work/return triage`
- `settings` -> `operating workspace policy`

## First Top-Layer Page Shape

The first real integrated page should have these zones:

- left navigation: workspace, work board, organ runtimes, approvals/gates, audit, settings
- top strip: current workspace posture, active work count, blocked gates, active worker runs
- main column: work board and selected work packet detail
- right inspector: assignment, current organ/lane, handoff, gate, relevant refs
- bottom or adjacent return lane: latest Codex/Gemini returns and trace events

## Relationship To Current Shell

- `/api/vectorfl-paper/state` stays useful as the first substrate state endpoint.
- `/vectorfl-paper` is only a status/substrate console.
- The future top page should consume the same state but present it as work/organ/governance control plane.

## Hard Rule

Do not keep enlarging the substrate console as if it were the final operating page.

The next implementation should create a higher page class that starts from the Paperclip product structure and maps VectorFL state into it.

## 2026-04-11 Deep Paperclip UI Rereading Lock

After rereading Paperclip `ui/src`, the top-layer target must be stricter:

- Paperclip's top structure is not tab enumeration.
- Paperclip uses a company-scoped app frame: `CompanyRail`, `Sidebar`, breadcrumbs, properties panel, command palette, creation dialogs, toast, and mobile nav.
- Paperclip separates operating resources first: issues, agents, heartbeats, approvals, activity, budgets, companies.
- `Issues -> IssueDetail -> IssueProperties` is the work allocation and execution spine.
- `Agents -> AgentDetail -> dashboard/instructions/configuration/skills/runs/budget` is the operable organ spine.
- `Inbox -> Approvals -> Activity -> Settings` is the triage/governance/audit/policy spine.

VectorFL translation:

- Do not keep adding tabs inside `operable_surface` and call it integrated operation.
- Do not render Codex/Gemini as labels without input, selection, assignment, confirmation, and supervisor controls.
- Do not promote `paper_proper` bridge cards directly as final product UI.
- Create a higher control-plane page class where current proper/operable outputs become work packets, organ runs, gate decisions, and audit events.

The next real page should be designed as:

`work packet control plane + organ runtime control plane + supervisor gate/audit plane`

not:

`static substrate dashboard + extra bridge panels`.

## 2026-04-11 Integrated Engine Ignition Lock

The integrated operating page is still one layer higher than the control-plane surface described above.

It is not only a page that displays work packets, organ runtimes, gate decisions, and audit events. It is the visible operating face of the integrated engine itself.

The engine-level scenario is:

- user enters a topic, memo, or directive
- the supervisor interprets the directive
- the supervisor assigns line generation work
- the line generation worker returns a report
- the supervisor analyzes, interprets, and integrates that report
- the supervisor assigns internal-space exploration work, using the generated line as the search criterion
- the internal exploration worker searches prior code, locked docs, mistakes, references, and usable materials
- the supervisor judges whether the internal material is enough or whether external resources are needed
- if needed, the supervisor assigns external reference search / reading work
- the supervisor thickens the line from internal and external evidence
- the supervisor translates the thickened line into human-readable design / structure / method / purpose material
- the supervisor packages that material as an implementation brief
- the implementation worker builds or modifies code from that brief
- the implementation worker requests internal or external resources when blocked
- the verification worker checks the result
- the supervisor routes fixes back to implementation or internal exploration
- the user sees and controls this whole chain from the operating page

This means the page must expose not only outputs, but commandable responsibility transitions:

- input interpretation
- line generation request
- line generation return
- internal-space exploration request
- internal-space evidence return
- external reference request
- translation / synthesis
- implementation handoff
- implementation return
- verification handoff
- verification return
- supervisor decision
- trace / audit return

Paperclip remains relevant because it already separates the product problem into:

- triage
- work allocation
- work detail
- right-side assignment / gate inspection
- agent / organ runtime operation
- approval / governance
- activity / audit

VectorFL must apply that separation to its own engine loop. Codex, Gemini, line generation, internal exploration, external research, implementation, and verification are not just labels. They are assignable operating roles with inputs, returns, gates, and audit trails.

Therefore the next implementation target is not:

`make the current Paper page look more like Paperclip`

It is:

`create an engine-level operating surface where the supervisor can interpret input, assign workers, receive reports, route evidence, hand off implementation, request verification, and show the user every transition`

The current substrate surfaces remain useful only as source material for that engine-level surface.
