# Integrated Engine Working Lexicon v1 Candidate

Date: 2026-04-15

## 0. purpose

This document gathers the current PASS-level vocabulary for integrated-engine v0 operation.

It is a v1 candidate, not a final schema or permanent lock.

Do not read this as:

- DB model
- final enum list
- canonical state machine
- runtime binding
- automatic routing design

Read it as:

- the minimum shared language that currently works across documents, manifests, and scaffolds

## 1. three surfaces

### user surface

The surface that sets goal, scope, material context, operating priority, and distribution decision.

Current center panel:

- `operating_flow_panel`

Working sentence:

- User surface is the operating / distribution / decision surface.

### VectorFL surface

The surface that reads requests before execution, mediates direction, validates returns, and preserves maturation value.

Current center panel:

- `maturation_canvas_panel`

Working sentence:

- VectorFL surface is the mediation / validation / maturation surface.

### engine surface

The surface that receives shaped input, performs processing, creates return material, and keeps execution trace visible.

Current center panel:

- `execution_state_panel`

Working sentence:

- Engine surface is the processing / execution / return-draft surface.

## 2. object classes

### anchor object

An anchor object is a bottom reference point for comparison, boundary, and position judgment.

Core fields:

- `anchor_scope`
- `governs_what`
- `locked_boundary`
- `comparison_rule`

Working sentence:

- Anchor objects do not produce meaning directly; they let other objects be compared by scope, boundary, and role fit.

### maturation object

A maturation object is a meaning object before or during emergence.

It preserves origin, position, maturity, linkage, and open edges.

Core fields:

- `origin_refs`
- `current_position`
- `maturity_stage`
- `linked_objects`
- `open_edges`

Working sentence:

- Maturation objects are not finished concepts; they are material that can grow into lines or axes through connection, repetition, and reread.

### operating object

An operating object is a processing object that moves through explicit slots.

Working sentence:

- Operating objects are about transition and handling, not meaning maturation.

## 3. packet kinds

### request packet

A request packet carries a request from user-side intention into VectorFL review.

Current direction:

- `user_surface -> vectorfl_surface`

Current follow-up note:

- The default request direction is `user_surface -> vectorfl_surface`.
- After a VectorFL maturation signal is recorded, a shaped follow-up request reorganized by user organization may target `engine_surface`.
- A reprocess request created by VectorFL validation or anchor check can be read as `vectorfl_surface -> engine_surface`.

Working sentence:

- A request packet is not raw intent; it carries purpose, directionality, anchors, related objects, and validation points for review.

### return packet

A return packet carries engine-side result material back to VectorFL validation.

Current direction:

- `engine_surface -> vectorfl_surface`

Working sentence:

- A return packet is processing output prepared for validation, not product completion.

### reflux packet

A reflux packet carries maturation-worthy material back toward space.

Current direction:

- `vectorfl_surface -> space`

Working sentence:

- A reflux packet is the route and reason for preserving material as future maturation input.

## 4. panel expression classes

### anchor expression panel

Shows criteria, boundary, comparison, and drift risk.

Question:

- Which criteria is this object standing on?

### maturation expression panel

Shows meaning growth, maturity, linked objects, evidence density, and open edges.

Question:

- What is growing as a line or axis, and what remains open?

### operating expression panel

Shows processing slot, active packet, route, bottleneck, and return state.

Question:

- Where is the operating object now, and what should happen next?

## 5. current central panel rule

The three central panels must differ:

- user surface = `operating_flow_panel`
- VectorFL surface = `maturation_canvas_panel`
- engine surface = `execution_state_panel`

Working sentence:

- The central panel difference is what keeps the three-surface body legible.

## 6. current PASS basis

The current v0 structure is PASS because:

- user surface reads operating flow
- VectorFL surface reads maturation object as primary
- engine surface reads execution state
- request / return / reflux roles are separated
- current loop state locates the active loop
- panel connection records make the three-surface circulation visible

## 7. held out of this candidate

Not included in this v1 candidate:

- final schema
- final enum set
- DB model
- automatic routing
- standing worker assignment
- full team/role taxonomy
- runtime data binding
- full UI component system
