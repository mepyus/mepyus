# Integrated Engine User Surface Visual Translation Brief v0

Date: 2026-04-15

## 0. verdict

PASS

The selected `gemini/mock_test` user-surface visual grammar can be translated onto the current integrated-engine baseline if the central gravity remains `operating_flow_panel`.

This is a visual translation brief only. It does not change scaffold read mappings, create panels, introduce runtime binding, or promote team / role management into the body skeleton.

## 1. purpose

This brief translates selected visual grammar from the user-side mock into the current user-surface baseline.

Current baseline stays fixed:

- user surface = operating / distribution / decision surface
- center panel = `operating_flow_panel`
- panels remain `request_organization_panel`, `operating_flow_panel`, `anchor_support_panel`, and `return_decision_panel`
- request / return / reflux flow must appear before any team / role extension
- team / role material is optional extension layer only
- current scaffold read mapping remains unchanged

## 2. selected mock grammar

Allowed visual sources:

- `CommandHeaderPanel` goal / scope / material context rhythm
- partial `TeamRoutingPanel` routing visual token
- partial `ExecutionRoutePanel` slot / flow column rhythm
- compact badge / small card / side support panel style
- restrained operation log row style, only if rewritten as packet / connection evidence

Held out:

- `RoleConfigurationPanel` as a core user-surface structure
- team / role management before operating flow
- org chart / assignment table dominating request flow
- governance console language
- standing assignment console
- new core panel

## 3. mock element -> baseline panel mapping

| mock source | visual grammar to keep | baseline panel | translation rule | do not carry |
|---|---|---|---|---|
| `CommandHeaderPanel` | goal / scope header card, compact context boxes, high-level intent field | `request_organization_panel` | Use as request framing visual: goal, scope, material context, expected output, requested action. | Freeform command console, goal field as runtime source of truth, large hero-like dominance over operating flow. |
| `CommandHeaderPanel` info boxes | small labeled context cards | `request_organization_panel` / `anchor_support_panel` | Translate to purpose, material context, scope guard, next surface, anchor refs. | Generic dashboard stats not tied to packet fields. |
| `ExecutionRoutePanel` | columns / ticket card rhythm | `operating_flow_panel` | Rewrite columns as packet/slot movement: inbox, VectorFL review, engine processing, validation, return ready / decision. | Backlog / Active / Handoff / Review as team work queues. |
| `TeamRoutingPanel` | compact route cards, active state, status pill | support layer below `operating_flow_panel` | Use only as optional distribution hint after request / loop state is visible. | Team identity as primary structure, add/remove team controls, role counts as core state. |
| `OperationLogPanel` | compact log row with next-action cue | support layer under `operating_flow_panel` or `return_decision_panel` | Use for panel connection records, return decision notes, or user-facing next action. | Live operation feed, team/role icons as primary identity, audit feed as runtime truth. |
| `RoleConfigurationPanel` | none for core body; small badge style only if needed | extension layer only | Keep only the "extension slot / optional tool layer" boundary idea. | Team console, edit role config, add role, selector controls, role card grid as central UI. |
| `user-surface.seed.ts` stats | small scope / material labels | `request_organization_panel` | Use labels such as goal state, scope guard, material context, next surface if tied to packet fields. | Static seed data as actual state. |

## 4. panel-by-panel visual translation

### `request_organization_panel`

Use:

- `CommandHeaderPanel` rhythm as a compact request framing card
- goal / scope / material context boxes
- small labels for `purpose`, `directionality`, `anchor_refs`, `input_materials`, and `expected_output_shape`
- one restrained next-surface badge, usually `VectorFL review` or shaped follow-up target

Avoid:

- command-center framing
- freeform control console
- runtime state claims
- team assignment as the first visible structure

Reading note:

- This panel organizes a request. It should not become an interpretation/maturation panel or a team-management console.

### `operating_flow_panel`

Use:

- `ExecutionRoutePanel` column rhythm, translated away from team tickets into packet / slot movement
- stable central card or lane group showing current loop state
- current slot badge and route arrow
- small cards for active request, active return, active reflux, current focus object

Suggested visual slot labels:

- `inbox`
- `vectorfl_review`
- `engine_processing / external_support`
- `validation`
- `return_ready / decision`
- `closed`

Avoid:

- backlog / active / handoff / review as team lifecycle
- role owner as the primary object
- standing assignment console
- organization chart

Reading note:

- This is the user-surface center. It must show where the operating loop is and what decision/distribution action is available.

### `anchor_support_panel`

Use:

- compact side support card style from `CommandHeaderPanel` context boxes
- small badge for active anchor
- short boundary / comparison text
- drift risk pill if present

Avoid:

- making anchor look like a generic health metric
- mixing anchor with team capacity or governance score
- adding a new anchor dashboard

Reading note:

- Anchor support helps the user see whether the request or decision respects the current baseline. It does not produce meaning by itself.

### `return_decision_panel`

Use:

- compact decision card rhythm
- small route badges for `accept`, `send_to_vectorfl_recheck`, `reprocess`, or `reflux`
- concise return summary and open questions
- optional next-action strip inspired by `OperationLogPanel`

Avoid:

- final product completion styling
- engine verdict as user decision
- team handoff board as the return decision

Reading note:

- This panel lets the user decide or distribute after return material has been validated or routed. It should not replace VectorFL validation.

## 5. team / role extension rule

Team and role visuals may appear only after these conditions are met:

- the active request or current loop state is visible first
- the team / role element is labeled as extension / optional tool layer
- it supports distribution or follow-up, not core structure
- it never replaces `operating_flow_panel`
- it never becomes the user-surface center

Allowed extension usage:

- small route option card after user decision
- optional executor hint
- compact status pill for a selected distribution target

Forbidden extension usage:

- central `Team Console`
- role editing as baseline operation
- add/remove team controls as primary actions
- team count / role count as core loop state
- assignment desk replacing packet movement

## 6. allowed / forbidden by panel

| baseline panel | allowed | forbidden |
|---|---|---|
| `request_organization_panel` | goal/scope card, material context cells, request field badges, next surface pill | command console, team assignment first, freeform runtime truth |
| `operating_flow_panel` | slot columns, active packet cards, current slot badge, route arrow, decision-ready marker | team lifecycle board, org chart, standing assignment queue |
| `anchor_support_panel` | anchor badge, boundary card, comparison rule note, drift risk pill | governance score, team capacity, generic health dashboard |
| `return_decision_panel` | return summary card, open question chips, next route badges, user decision strip | engine final verdict, product completion, handoff board dominance |
| support layer | compact route cards, optional executor hints, panel connection log rows | role editor, add/remove team controls, live operation feed |

## 7. pseudo layout proposal

This is a layout note only. It is not an implementation instruction.

```text
user_surface

top band:
  small surface label: User surface
  one-line role: operating / distribution / decision
  boundary note: request and decision come before team / role extension

main layout:
  left column:
    request_organization_panel
      goal / scope / material context card
      request purpose and expected output cells
      next surface badge

    anchor_support_panel
      active anchor badge
      locked boundary / comparison rule note

  center column:
    operating_flow_panel
      largest card, central
      slot / flow lanes
      active request / return / reflux cards
      current slot and loop status pills

  right column:
    return_decision_panel
      return summary
      open questions
      route choices: user decision / VectorFL recheck / reprocess / reflux

    support layer
      optional route target card
      compact connection / decision log
```

Support layer:

- Team / role visuals may live here only as distribution hints.
- They must remain smaller than the operating flow.
- They must be visually labeled as extension, not body skeleton.

## 8. visual token guidance

Use:

- compact cards
- small uppercase field labels
- subdued icon blocks
- route badges
- current-slot pill
- thin vertical or horizontal route lines
- side support cards for anchor and return decision

Avoid:

- large team console header
- edit/add/remove team controls
- assignment desk framing
- governance / supervisor / authority copy
- visual hierarchy where teams appear before packets
- dashboard stats that are not tied to request / loop / return fields

## 9. preservation note

This brief does not change:

- `runtime/views/user_surface_scaffold_v0.tsx`
- panel names
- panel read mapping
- manifest paths
- runtime binding
- team / role model
- execution behavior

It only defines how selected user-surface mock visual grammar may be translated later while preserving the current working baseline.

