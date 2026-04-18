# VectorFL Paperclip Tab Flow Merge Plan v0

## Verdict

- Do not copy Paperclip's company / agent / issue ontology.
- Do copy Paperclip's operable screen grammar.
- The corrected merge target is not `vectorfl_paper_weekend_pilot`.
- The likely existing VectorFL Paper target is `vectorfl_operable_surface`.
- The merge should make Paper easier to operate, not broader.

Core point:

- VectorFL Paper may converge toward tabbed/page-listed navigation.
- If tabs only list surfaces, the process becomes harder to read.
- Therefore each tab/page must carry its own setup, return path, and supervisor posture.

## Paperclip Structure Reading

Paperclip does not use tabs as passive buckets.

It uses a layered operating shell:

- Global app shell: company rail, sidebar navigation, breadcrumb, main content, optional properties panel.
- Route-backed page classes: dashboard, inbox, issues, issue detail, agents, agent detail, projects, approvals, costs, activity, settings.
- Entity detail tabs: issue detail has comments / sub-issues / activity; agent detail has dashboard / instructions / skills / configuration / runs / budget; project detail has overview / issues / workspaces / configuration / budget.
- Right-side inspector: issue properties and related property panels keep assignment/status/project/config close to the object.
- Triage tabs: inbox has mine / recent / unread / all, but those tabs remain triage views over the same inbox role.

This means the Paperclip pattern is not "many tabs".

The pattern is:

- stable navigation class outside
- current work object inside
- setup and operation inside the current tab
- audit/return as first-class pages
- right-side inspector for object-level adjustment

## Why Paperclip Tabs Work

Paperclip tabs work because each tab has a clear job:

- Issue detail comments tab is where the work return, discussion, and live run widget converge.
- Issue detail sub-issues tab keeps decomposition inside the same work object.
- Issue detail activity tab keeps audit close to the issue without replacing the global activity page.
- Agent detail instructions/configuration/runs/budget tabs turn an agent into an operable node, not just a label.
- Inbox mine/recent/unread/all tabs are filtered triage states, not separate workflows.
- Project tabs keep overview, work list, workspace, configuration, and budget separated while preserving the project as the current object.

The reason this matters for VectorFL:

- If VectorFL only exposes tabs like `current`, `history`, `bridge`, `validation`, `decision`, the user will lose the operating flow.
- If each tab says what it sets up, what it reads as SSOT, what is preview-only, and where the result returns, the flow survives even in a tabbed shell.

## Current VectorFL Paper Reading

Existing candidate:

- Page root: `runtime/views/vectorfl_operable_surface/index.html`
- Generator: `scripts/run_vectorfl_operable_surface_set.py`
- Runtime module: `app/runtime/vectorfl_operable_surface_set.py`

Current navigation groups already exist:

- BOARD: `engine-overview`, `cases`, `trace-audit`, `worker-inbox`
- INTAKE: `internal-recall`, `external-resources`
- WORK: `case-detail`, `case-inspector`, `line-review`, `case-routing`
- TEAMS: `organs`, `organ-registry`, `contracts-workspace`, `program-workspaces`
- CLI: `lanes`, `cli-setup`, `agent-mcp-control`, `lane-runs`

This is directionally compatible with Paperclip.

But the risk is:

- The navigation reads as many surfaces rather than one process.
- The actual supervisor flow may be harder to see if validation/comparison/hold posture is scattered across pages.
- New Paper proper material should not be pasted wholesale; it should become setup/posture units inside the existing page classes.

## Mapping Paperclip Grammar To VectorFL Paper

### Dashboard / Overview

Paperclip analogue:

- Dashboard

VectorFL target:

- `engine-overview`

What belongs here:

- Current operating posture summary
- Waiting-for-actual-export / hold-current state
- No gate close / no slot replacement guard
- One sentence that points to the next page to read

What does not belong here:

- Full dry-run artifact detail
- Candidate archive rows
- Intake template display

### Work List

Paperclip analogue:

- Issues list

VectorFL target:

- `cases`

What belongs here:

- Case queue / current loop list
- Status and next-action readable rows
- Minimal guard chips

What does not belong here:

- Full supervisor reconciliation prose
- Full validator comparison output

### Work Detail

Paperclip analogue:

- Issue detail

VectorFL target:

- `case-detail`

What belongs here:

- Current context
- Selected source / line / evidence
- The process strip: input -> handoff -> return -> decision
- Worker setup summary if it is tied to the current case

Paperclip cue:

- Issue detail keeps comments, sub-issues, activity, workspace, live run, and properties close to one work object.

VectorFL translation:

- Keep the current case as the center.
- Do not make the user jump to a separate archive page just to understand the current loop.
- But keep dry-run and comparison detail subordinate to the current SSOT.

### Inspector

Paperclip analogue:

- IssueProperties / PropertiesPanel

VectorFL target:

- `case-inspector`

What belongs here:

- Current SSOT vs preview-only distinction
- Validation anchor pointer
- Selected evidence / ambiguity / missing material
- Guard language that prevents preview from being read as replacement

Why:

- This is where the user should inspect what is mutable, provisional, or blocked without changing the case detail center.

### Intake / External Candidate Setup

Paperclip analogue:

- Company import/export, project setup, issue creation setup

VectorFL target:

- `external-resources`

What belongs here:

- Candidate evidence setup
- Actual export candidate readiness
- Reference-derived vs true host/export distinction
- External material selection

What does not belong here:

- Slot replacement
- Gate close declaration
- Inbox_latest rendering before a real candidate arrives

### Worker Return / Inbox

Paperclip analogue:

- Inbox

VectorFL target:

- `worker-inbox`

What belongs here:

- Codex return
- Gemini review summary if it is a return/check result
- Reopen/redirect/hold next action
- Return route back to trace-audit and case-detail

Paperclip cue:

- Inbox tabs are triage filters over actionable items.

VectorFL translation:

- Worker inbox should not become a general archive.
- It should answer: what came back, does it require supervisor action, where does it return?

### Audit / Gate

Paperclip analogue:

- Activity, approvals

VectorFL target:

- `trace-audit`

What belongs here:

- Validator result
- Reference comparison summary
- Hold/reopen decision reading
- Gate effect
- No gate close / no promotion guard

Why:

- This is the strongest receiving point for the proper-side judgment units.
- It already describes trace as a dedicated audit surface and includes approval gate semantics.

### Agent / Runtime Control

Paperclip analogue:

- Agent detail tabs: dashboard / instructions / skills / configuration / runs / budget

VectorFL target:

- `agent-mcp-control`

What belongs here:

- Codex / Gemini runtime binding status
- Adapter role distinction
- Return route
- Contract pointer

What must be avoided:

- Importing Paperclip agent/company ontology.
- Making this a fake execution console.

## Recommended Merge Order

### First

- Merge hold/reopen/gate posture into `trace-audit` as a compact read-only judgment unit.
- Include current SSOT vs preview-only guard if it is needed to understand the gate.

Reason:

- `trace-audit` is already the approval/audit page class.
- It is closest to Paperclip's activity/approval role.
- It reduces confusion without making proper or weekend pilot the target.

### Second

- Add worker return posture to `worker-inbox`.
- Keep it focused on latest return / review / required supervisor action.

Reason:

- Paperclip uses inbox as triage, not archive.
- Our existing route already says `worker-inbox -> trace-audit -> case-detail reinjection`.

### Third

- Add a top-level posture pointer to `engine-overview`.

Reason:

- The overview should orient the user, not repeat the audit.
- It should say: current state is hold/waiting, read trace-audit for gate details, read worker-inbox for returns.

### Fourth

- Add candidate setup language to `external-resources` only after the audit/inbox reading is clear.

Reason:

- External resources is where candidate setup belongs.
- But adding it too early can make candidate material look promoted.

## Do Not Merge

- Do not merge `vectorfl_paper_weekend_pilot` as a target.
- Do not merge full `vectorfl_paper_proper` wholesale.
- Do not merge candidate-by-candidate archive rows.
- Do not render intake template or inbox_latest before a real candidate arrives.
- Do not add gate close logic.
- Do not add slot replacement logic.
- Do not convert VectorFL into Paperclip company/agent/issue ontology.

## Practical UI Rule For Our Tabbed Surface

If VectorFL Paper becomes tab-heavy, each tab/page must show three things:

- Setup: what this tab lets the supervisor prepare or inspect.
- Flow position: where this tab sits in input -> handoff -> return -> decision -> trace.
- Return route: what page receives the result and what page remains current SSOT.

Without these three, tabs become a list and the process disappears.

## Next Implementation Candidate

Implement only after explicit approval:

- Add a compact, read-only `gate posture` block to `trace-audit`.
- Data source should be existing manifests only.
- It should show current SSOT, preview-only dry-run, comparison summary, hold/reopen posture, and guard language.
- It should not write manifests.
- It should not reference weekend pilot as the canonical Paper.

