# Integrated Engine Trace Inclusion Rule Note v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

Trace can be included only as compact support for the current panel question. Connection-record density is not promoted to core, and no trace UI, selected-object behavior, runtime feed, watcher, supervisor, or bridge authority is approved.

## 1. current core trace boundary

Current core render contract allows trace only when it answers one of these scaffold-level questions:

- Which mapped manifest explains this panel's current material?
- Which minimal route record explains how material moved between panels?
- Which reflux or return route should remain visible as support context?

Current trace may include:

- mapped manifest path
- read role
- read reason
- primary connection record named in the read map
- reflux route label already present in the mapped packet
- visual route rhythm explicitly marked as visual-only

Current trace may not include:

- full timeline
- live event feed
- selected-object drilldown
- worker/process telemetry
- watcher or supervisor recommendation
- bridge/control command
- new connection-record aggregation

## 2. why connection-record trace density is not core

Connection-record trace density is not core because:

- current read mappings name representative records, not a full trace set
- broader trace inclusion rules are not defined per scenario
- denser trace could make support panels visually stronger than the central panel
- trace density could imply live runtime truth or route authority
- selected-object behavior would be needed for row-level inspection, and that is held out of the v1 candidate

Current status:

- compact trace support is core-safe
- denser trace rendering needs promotion gate review

## 3. surface-specific allowed trace

### user surface

Allowed now:

- route-state labels inside `operating_flow_panel`
- visual route rhythm: request, vectorfl_review, return, decision_or_reflux
- return/recheck/reflux wording inside `return_decision_panel`
- mapped manifest read reason per panel

Not allowed now:

- connection-record timeline as user central content
- ownership/approval trace
- selected route drilldown

Reason:

- user center must remain operating / distribution / decision, not evidence-history or governance.

### VectorFL surface

Allowed now:

- `evidence_history_panel` reads the primary connection record named in the current read map
- `routing_reflux_panel` reads return and reflux packet route material
- `maturation_canvas_panel` may show supporting reflux and return contribution as context
- object-class labels may distinguish anchor criteria, maturation body, and operating route

Not allowed now:

- broader connection-record timeline
- global maturity trace as primary truth
- selected line/axis trace drilldown

Reason:

- VectorFL center must remain `maturation_canvas_panel`, with trace as mediation/evidence support only.

### engine surface

Allowed now:

- `execution_history_panel` reads the engine-return-to-VectorFL validation connection record
- work input / execution / return / trace slot rhythm as visual-only support
- mapped read reason explaining shaped input, current slot, return draft, and route trace

Not allowed now:

- worker-process timeline
- runtime status feed
- supervisor queue
- trace as engine command history

Reason:

- engine remains processing / execution / return-draft, not a control room.

## 4. trace classification

| class | allowed meaning | examples |
|---|---|---|
| core-support trace | compact route or read evidence that supports an existing panel question | manifest path, read reason, mapped connection record, reflux route label |
| future extension trace | denser but still read-only trace that may help loop reconstruction later | broader connection-record rows, return-material trace, selected evidence row |
| hold | trace that implies live truth, authority, control, or selected-object state without a contract | watcher feed, supervisor recommendation, bridge command, worker telemetry, selected-object drilldown |

## 5. central gravity boundary

Trace must not compete with central panel gravity.

Protected centers:

- user: `operating_flow_panel`
- VectorFL: `maturation_canvas_panel`
- engine: `execution_state_panel`

Trace is safe only while it explains or supports these centers. It becomes unsafe when it becomes the largest, most authoritative, or most actionable region of a surface.

## 6. selected-object boundary

Trace must not slide into selected-object behavior.

Disallowed implications:

- clicking a trace row changes panel state
- a selected trace becomes the source of truth
- side inspection renders trace-specific fields
- trace rows imply live routing or intervention

Allowed current stance:

- trace can be named and bounded as support evidence
- selected-object behavior stays future extension after a display-state contract

## 7. boundary sentence

Round 6 permits trace as compact support evidence only. It does not approve trace density, trace UI, selected-object inspection, or runtime/event-feed semantics.
