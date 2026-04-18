# Integrated Engine Visual Translation Consolidation Note v0

Date: 2026-04-15

## 0. verdict

PASS

The three surface visual translation briefs can be consolidated into a shared visual rule set, as long as the current working baseline remains the top authority and no scaffold read mapping changes before implementation.

## 1. scope

This note consolidates:

- `integrated_engine_engine_surface_visual_translation_brief_v0.md`
- `integrated_engine_user_surface_visual_translation_brief_v0.md`
- `integrated_engine_vectorfl_surface_visual_translation_brief_v0.md`

It is not an implementation plan, component spec, or runtime binding plan.

Fixed constraints:

- current working baseline stays above mock visuals
- no new core panels
- no scaffold read mapping changes
- no runtime binding or live manifest truth
- no watcher / supervisor / governance authority
- each surface keeps its central panel gravity
- visual tokens can be shared, but surface identity and object class separation must remain visible

## 2. common visual tokens

### badge / small pill

Use for:

- packet status
- current slot
- maturity stage
- evidence density
- open edge / drift / hold
- suggested next route

Do not use for:

- authority claims
- live sync truth
- global health verdict
- supervisor priority
- automatic execution state unless manifest-backed

### compact card density

Use for:

- request fields
- active loop state
- maturation object fields
- return material
- connection records
- anchor criteria

Do not use for:

- whole-manifest display
- generic dashboards
- team / role management as a primary body
- asset inventory as central engine content

### side inspection usage

Use as support layer only:

- selected packet details
- selected maturation object support fields
- selected anchor criteria
- selected route / connection record detail
- return open questions

Never use as:

- a new core panel
- central authority panel
- live asset inspector
- script lineage or watcher console

### risk / watchpoint expression

Use for:

- anchor drift
- open edges
- hold reason
- reprocess route
- validation uncertainty

Do not use for:

- global governance score
- live risk dashboard
- supervisor intervention
- generalized "system health" truth

### left / center / right layout rhythm

Use as a repeated visual rhythm:

- left = context / input / anchor / support selection
- center = surface central panel
- right = decision / return / validation / history support

The center must be visually largest and semantically strongest on each surface.

## 3. surface-specific use of shared tokens

### user surface

Central gravity:

- `operating_flow_panel`

Token use:

- badges show current slot, active request, return decision route, or distribution state
- compact cards show request organization, loop state, anchor support, and return decision
- side inspection supports anchor or return decision, not interpretation
- risk/watchpoint style appears only as anchor drift or decision caution
- left / center / right rhythm keeps request organization and anchor support on the left, operating flow in the center, return decision and optional support on the right

Special rule:

- team / role visuals are extension layer only and must never precede request / return / reflux flow.

### VectorFL surface

Central gravity:

- `maturation_canvas_panel`

Token use:

- badges show maturity stage, evidence density, open edge state, route hold, drift, or recheck
- compact cards show maturation body fields, anchor criteria, validation points, reflux value, and evidence records
- side inspection supports selected maturation object, anchor, route, or evidence row
- risk/watchpoint style is valid for anchor drift and open edges only
- left / center / right rhythm keeps anchor context and line/axis support selection on the left, maturation object body in the center, validation/reflux/evidence support on the right

Special rule:

- line atlas is support selection only. It must not become the center or define the surface identity.

### engine surface

Central gravity:

- `execution_state_panel`

Token use:

- badges show packet status, current slot, returned, hold, follow-up, or reprocess
- compact cards show work input, execution state, return material, and route history
- side inspection supports selected packet, return, or history row only
- risk/watchpoint style appears only as processing hold, return open question, or reprocess marker
- left / center / right rhythm keeps shaped input on the left, execution state in the center, return material and execution history on the right

Special rule:

- engine surface is processing / execution / return-draft. It must not look like a control room, governance console, supervisor desk, or maintenance authority.

## 4. visual collisions that must not happen

### anchor vs maturation vs operating object

Do not merge these into one card language.

- anchor visuals must look like criteria / boundary / comparison
- maturation visuals must look like object body / emergence / open edges
- operating visuals must look like slot / route / packet movement

Collision signal:

- one card simultaneously acts as anchor, axis, request, return, and route.

### user flow vs team / role extension

User surface must show operating flow before team / role hints.

Collision signal:

- team console, role editor, org chart, or assignment queue visually dominates `operating_flow_panel`.

### engine processing vs governance authority

Engine surface must show processing state and return draft, not final authority.

Collision signal:

- labels like control room, governance, maintenance, supervisor, intervention required, live sync, or script authority become primary.

### VectorFL maturation vs line browser

VectorFL surface must read maturation object body, not just browse lines.

Collision signal:

- line cards are larger than `maturation_canvas_panel`, or the user can understand only selected line but not origin refs, maturity, linked objects, and open edges.

### return material vs product completion

Return panels must not imply final completion.

Collision signal:

- accepted / done / product-ready styling replaces VectorFL validation, user decision, reflux, or reprocess routing.

### visual dashboard vs panel question

Panels must answer their own question.

Collision signal:

- generic stat grids, global health percentages, live feeds, or full inventories obscure the panel's manifest fields.

## 5. implementation reflection order

### 1차: engine surface bounded visual patch

Why first:

- lowest conceptual translation cost
- mock slot rhythm maps cleanly to `work_input_panel`, `execution_state_panel`, `result_return_panel`, and `execution_history_panel`
- fewer risks around maturation/anchor/line identity

Allowed scope:

- visual styling only
- no read mapping change
- no new panel
- no live truth
- no control-room language

### 2차: user surface operating-flow visual patch

Why second:

- user surface needs stronger central flow before any team / role material can be safely shown

Allowed scope:

- make `operating_flow_panel` visually central
- translate `ExecutionRoutePanel` rhythm into packet/slot movement
- keep `CommandHeaderPanel` rhythm as request organization support
- keep team/role extension out of the core center

### 3차: VectorFL surface maturation-canvas visual patch

Why third:

- highest risk of confusing line browser, anchor, operating route, and maturation object body

Allowed scope:

- central maturation object body card
- line atlas only as support selection
- anchor context visually distinct
- validation/reflux/evidence panels remain support on the side

## 6. implementation entry gate

Start a bounded engine scaffold visual patch only when all conditions are true:

- the patch scope is limited to `runtime/views/engine_surface_scaffold_v0.tsx`
- panel names remain unchanged
- panel read mapping remains unchanged
- no new manifest is required
- no runtime binding is introduced
- no watcher / supervisor / governance / live manifest truth appears
- `execution_state_panel` remains the central visual gravity
- `work_input_panel`, `result_return_panel`, and `execution_history_panel` remain recognizable support panels
- engine copy says processing / execution / return-draft, not control room or final judgment
- final review checks that return material still routes outward for VectorFL validation / user decision / reprocess

If any condition fails, hold implementation and return to visual translation notes.

## 7. final rule

Shared visual tokens are allowed only when they clarify the existing baseline panels.

They are not allowed to import Gemini mock structure, promote optional tool layers, or blur surface roles.

First implementation surface: engine surface.
