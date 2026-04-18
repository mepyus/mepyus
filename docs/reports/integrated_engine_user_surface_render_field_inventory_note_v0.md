# Integrated Engine User Surface Render Field Inventory Note v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

The user surface render-field inventory is stable enough for current baseline documentation, with thinness limited to actual field-value rendering and selected route detail.

## 1. central panel minimum field set

Central panel:

- `operating_flow_panel`

Minimum render-field set:

- current slot
- active packet
- route state
- open decision

Primary manifest:

- `runtime/manifests/current_loop_state_axis_enrichment_001.json`

Display purpose:

- keep the request / return / reflux loop position visible so the user surface reads as operating, distribution, and decision.

## 2. support panel minimum field set

### request_organization_panel

Minimum render-field set:

- request frame
- goal
- scope
- material context
- next surface

Primary manifest:

- `runtime/manifests/packet_request_axis_enrichment_001.json`

### anchor_support_panel

Minimum render-field set:

- anchor
- boundary
- drift watch

Primary manifest:

- `runtime/manifests/active_anchor_integrated_engine_3_surface.json`

### return_decision_panel

Minimum render-field set:

- return material
- question
- recheck
- reflux

Primary manifest:

- `runtime/manifests/packet_return_axis_enrichment_001.json`

## 3. still implicit

1. `operating_flow_panel` names current-loop fields but does not bind actual values from `current_loop_state`.
2. `request_organization_panel` names goal/scope/material context as display groups, not formal manifest keys.
3. `return_decision_panel` keeps recheck/reflux open, but selected route/open-question detail is not contractually defined.

## 4. visual token vs true render field

True render fields:

- current slot
- active packet
- route state
- open decision
- goal / scope / material context
- anchor / boundary / drift watch
- return material / question / recheck / reflux

Visual tokens only:

- card density
- badge and pill shape
- route strip rhythm
- side support shell
- center-card emphasis

These visual tokens clarify reading order but are not contract fields.

## 5. future note

Selected-object:

- hold as extension later; no selected route state exists in the current scaffold.

Side inspection:

- support-only; may later show selected route, open question, or connection note after a separate display-state contract.

Trace density:

- not a user-surface core contract now; evidence density remains VectorFL/history-side carry-forward.

## 6. self-check

- central gravity preserved? yes, `operating_flow_panel`
- read mapping unchanged? yes
- semantic class separation preserved? yes, user operating surface remains operating / distribution / decision
- visual token extraction only? yes, no token is promoted to render field
- extension promotion absent? yes
