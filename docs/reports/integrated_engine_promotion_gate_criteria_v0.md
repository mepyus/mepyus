# Integrated Engine Promotion Gate Criteria v0

Date: 2026-04-15

## 0. verdict

PASS

This document defines promotion gates for future extension material that appeared during round 1 visual translation.

It does not implement any extension, add panels, change scaffold read mappings, or approve runtime binding.

## 1. purpose and role

Purpose:

- protect the current integrated-engine working baseline
- make future extension discussion evaluable before implementation
- separate core promotion from stable extension and hold-only material
- prevent useful visual or workflow ideas from drifting into authority, runtime truth, or surface-role confusion

Role:

- use this as the common gate before promoting future extension material into either core baseline or stable extension
- require explicit evidence before an extension changes panel importance, read mapping, object class visibility, or route behavior
- treat request / return / reflux readability and central panel gravity as non-negotiable baseline constraints

Current baseline remains:

- user surface center: `operating_flow_panel`
- VectorFL surface center: `maturation_canvas_panel`
- engine surface center: `execution_state_panel`
- request / return / reflux packets remain separated
- scaffold read mappings remain the primary reference for panel visibility

## 2. promotion candidate classes

### core promotion candidate

A candidate may be considered for core only when it is repeatedly necessary for the baseline to remain readable across scenarios.

Core promotion candidates must:

- clarify existing surface roles
- preserve central panel gravity
- preserve request / return / reflux separation
- remain compatible with current manifest / scaffold references or come with an explicitly approved mapping revision
- avoid runtime truth, governance authority, and execution-control drift

Default stance:

- hard to approve
- requires repeated scenario evidence
- requires documentation update before implementation

### stable extension candidate

A candidate may become stable extension when it is useful, repeatable, and safe, but not required for the baseline itself to work.

Stable extension candidates must:

- sit in support layer, side inspection, optional route detail, or bounded visual/token layer
- not become the central panel
- not introduce new authority
- not obscure the packet / panel / object-class grammar
- have a clear enable/disable boundary

Default stance:

- easier than core
- still requires a promotion note or extension contract
- should be implemented only after bounded visual or render-contract review

### hold / future-only candidate

A candidate stays hold / future-only when it is promising but currently risks confusing the baseline.

Hold candidates usually have one or more risks:

- replaces the surface center
- turns a support tool into authority
- reads like live runtime truth
- requires a new state machine, permission model, watcher, or worker layer
- mixes anchor, maturation, and operating objects in one card language
- makes request / return / reflux less legible

Default stance:

- no implementation
- keep as carry-forward idea only
- revisit only after a narrower gate is written

## 3. common gate criteria

### baseline readability

Question:

- Does the candidate make the current three-surface baseline easier to read without needing a new structure?

Pass signal:

- a reader can still explain user / VectorFL / engine roles from the surface alone
- the candidate clarifies an existing panel question

Fail signal:

- the candidate requires a new primary mental model before existing panels make sense

### panel gravity preservation

Question:

- Does the candidate preserve the approved central panel of its surface?

Pass signal:

- central panel remains visually and semantically strongest
- extension stays side, support, or secondary

Fail signal:

- the extension becomes larger, more active, or more authoritative than the central panel

### request / return / reflux compatibility

Question:

- Does the candidate keep request, return, and reflux roles separated?

Pass signal:

- request remains shaped input / review material
- return remains engine-side output for validation
- reflux remains maturation-preservation route

Fail signal:

- return reads as final completion
- reflux reads as generic feedback
- request reads as direct engine command without VectorFL review or allowed follow-up note

### manifest / scaffold impact boundedness

Question:

- Can the candidate be expressed without changing manifest shape or scaffold read mapping?

Pass signal:

- visual-only or render-contract-only change
- uses existing panel reads
- no manifest key dependency added

Escalation signal:

- requires new manifest, new panel mapping, or new current-loop semantics

Fail signal:

- silently depends on unapproved keys, watcher state, file truth, or runtime-generated data

### governance / runtime-truth drift risk

Question:

- Does the candidate imply authority, live truth, supervision, or execution control?

Pass signal:

- copy and layout read as advisory, support, or display-only

Fail signal:

- reads as governance console, control room, supervisor queue, live watcher, command bridge, permission layer, or source of truth

### repeated scenario usefulness

Question:

- Has the candidate proven useful across more than one low-intensity scenario?

Pass signal:

- helps normal loop, follow-up loop, and drift/reprocess loop without role confusion

Weak signal:

- useful in one mock or one fixture only

Fail signal:

- solves only a visual preference, not a repeated structural reading problem

### support-layer sufficiency vs true core necessity

Question:

- Is support-layer treatment enough?

Pass for extension:

- side inspection, support note, optional selection, or compact detail solves the need

Pass for core:

- without it, baseline reading repeatedly fails or becomes ambiguous

Fail:

- promoted to core because it is visually attractive, not because baseline needs it

## 4. surface-specific gate lens

### user surface

Core surface question:

- Where is the operating loop, and what decision or distribution action is next?

Protected center:

- `operating_flow_panel`

Allowed direction:

- extensions may support request organization, return decision, optional distribution, or side inspection

Promotion blockers:

- team console becomes center
- role / ownership table appears before request / return / reflux
- approval alignment reads as governance authority
- user surface becomes interpretation or maturation body

### VectorFL surface

Core surface question:

- What maturation object body is being read, mediated, validated, or preserved?

Protected center:

- `maturation_canvas_panel`

Allowed direction:

- extensions may support line / axis selection, anchor criteria, validation comparison, reflux route, and evidence rows

Promotion blockers:

- line atlas becomes the surface identity
- global maturity score becomes primary truth
- validation assistance becomes staffing or authority panel
- anchor, maturation, request, return, and reflux collapse into one visual object

### engine surface

Core surface question:

- Where is processing, what input is being handled, and what return material is being drafted?

Protected center:

- `execution_state_panel`

Allowed direction:

- extensions may support processing detail, return inspection, route trace, or read-only worker/process explanation

Promotion blockers:

- engine reads as control room or final decision authority
- watcher / supervisor / bridge becomes command surface
- runtime status is presented as live truth without binding contract
- return material reads as product completion

## 5. candidate evaluations

### team / role / ownership / approval-alignment

Why not core now:

- user surface already has a protected center: `operating_flow_panel`
- team / role material can easily become assignment console or ownership board
- approval alignment can drift into governance authority

Evidence that could justify later promotion:

- repeated scenarios where decision or distribution is unreadable after request / return / reflux is visible
- a support-layer contract showing ownership hints after, not before, operating flow
- copy and layout proving no authority or standing assignment drift

Likely destination:

- stable extension candidate

### validation / translation / research-assist structure

Why not core now:

- VectorFL core is mediation / validation / maturation, not staffing or research organization
- assistance categories can make VectorFL look like a team management surface
- research-assist can imply external truth or authority if not bounded

Evidence that could justify later promotion:

- repeated validation scenarios where assistance categories clarify evidence handling without changing panel authority
- explicit tool-layer boundary that keeps assistance advisory
- render contract separating evidence support from validation decision

Likely destination:

- stable extension candidate, with hold risk until tool-layer boundary exists

### watcher / supervisor / bridge optional tool layer

Why not core now:

- these terms strongly imply live monitoring, authority, intervention, or runtime control
- current baseline explicitly holds out watchers, supervision, governance, runtime binding, and automatic routing
- bridge language can obscure which surface owns the route

Evidence that could justify later promotion:

- a separate optional-tool-layer spec proving advisory-only behavior
- no central panel displacement
- no live truth or command semantics
- repeated scenario evidence that support visibility is needed and cannot be handled by existing evidence/history panels

Likely destination:

- hold / future-only candidate

### richer line atlas / axis browser / inspection depth

Why not core now:

- VectorFL center must remain `maturation_canvas_panel`
- line atlas can easily become list browser identity
- inspection depth needs selection sync and object-class render contracts that do not exist yet

Evidence that could justify later promotion:

- selected-object view model defined as display state only
- atlas remains smaller support selection feeding the maturation body
- anchor / maturation / operating object fields remain visually separated
- repeated maturation scenarios where support selection improves readability without replacing the canvas

Likely destination:

- stable extension candidate for support selection and inspection depth
- core only if repeated scenarios prove the maturation canvas cannot be read without a selected-object support contract

### return-material inspection / worker-process detail

Why not core now:

- engine surface is processing / execution / return-draft, not a runtime worker console
- return inspection can drift into final product completion
- worker/process detail can imply live execution binding

Evidence that could justify later promotion:

- read-only execution render contract
- return fields remain validation-bound and route outward to VectorFL/user/reprocess
- process detail remains explanatory, not live control
- repeated scenarios where current return/history cards are too thin to follow route state

Likely destination:

- stable extension candidate

## 6. decision matrix

| candidate | baseline readability | central gravity risk | runtime / authority risk | repeated usefulness needed | likely destination |
|---|---|---|---|---|---|
| team / role / ownership / approval-alignment | medium if after flow | medium on user surface | medium-high if approval reads as authority | user decision / distribution scenarios | stable extension |
| validation / translation / research-assist structure | medium for evidence work | medium on VectorFL surface | medium-high without tool boundary | validation and evidence scenarios | stable extension, hold until boundary |
| watcher / supervisor / bridge optional tool layer | low until bounded | high across surfaces | high | strong evidence plus advisory-only spec | hold / future-only |
| richer line atlas / axis browser / inspection depth | high for VectorFL if support-only | high if atlas becomes center | low-medium if display-only | maturation and drift scenarios | stable extension |
| return-material inspection / worker-process detail | medium-high for engine route reading | medium if process detail dominates | medium-high if live execution implied | return / reprocess scenarios | stable extension |
| shared visual token style layer | high | low | low | already repeated in round 1 | stable extension |
| selected-object support model | high if display-only | medium | medium if treated as runtime state | cross-surface inspection scenarios | stable extension after contract |
| connection-record density | high for loop reconstruction | low-medium | low if read-only | normal, follow-up, drift loops | stable extension |

## 7. promotion process

Before any candidate moves forward:

1. Classify it as core promotion, stable extension, or hold / future-only.
2. Run the common gate criteria.
3. Run the surface-specific lens.
4. Identify required document updates before implementation.
5. Confirm whether scaffold read mapping remains unchanged.
6. If read mapping changes, stop and create a separate mapping-change proposal.

Core promotion requires:

- repeated scenario evidence
- v1 candidate document update
- manifest / scaffold impact review
- explicit statement that central gravity and request / return / reflux separation remain intact

Stable extension requires:

- support-layer boundary
- visual or render-contract note
- no central panel displacement
- no runtime truth or authority drift

Hold / future-only requires:

- no implementation
- carry-forward record only
- revisit only when a narrower gate exists

## 8. round 2 entry answer

Round 2 can start before this is fully exercised?

Yes, if round 2 stays bounded to visual refinement, shared styling, responsive layout, or read-only render-contract audit without promoting extension material.

Reason:

- The gate is needed before extension promotion, not before baseline-safe visual continuation.
