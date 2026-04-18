# Integrated Engine Screen Panel Classification Criteria v0

Date: 2026-04-15

## 0. purpose

This document is a working draft, not a final UI specification.

It translates the current object grammar into screen-panel reading criteria.

The screen should not be read as a collection of feature buttons.

The screen should be read as an expression surface that makes visible:

- anchor criteria
- meaning maturation state
- operating-object slot movement

Do not read this document as:

- final UI layout
- final component taxonomy
- final design system
- automatic dashboard generation rule
- complete panel inventory

Read it as:

- v0 panel classification language for integrated-engine setup
- a guide for deciding whether a panel expresses anchor, maturation, or operating movement

## 1. why panel classification is needed

The integrated engine currently needs to show:

- what is the reference point
- what is maturing
- what is moving through processing slots
- where the current bottleneck is
- what should return to the space as reflux material

If the screen becomes only a pretty dashboard, it loses the integrated-engine reading.

Screen panels should therefore answer operational reading questions, not only expose functions.

Key sentence:

> The screen is not a feature-button collection. It is an expression surface that makes anchor criteria, meaning maturation, and operating movement visible.

## 2. three panel classes v0

v0 classifies panels into three classes:

- anchor expression panel
- maturation expression panel
- operating expression panel

These parallel the current object classes:

- anchor object
- maturation object
- operating object

Boundary:

- This is a reading/classification rule.
- It is not yet a final component architecture.

## 3. anchor expression panel

### role

An anchor expression panel shows what standard the current object or action is being read against.

It should make visible:

- current active anchor
- anchors referenced by the current request or maturation object
- allowed range
- prohibited boundary
- whether the current state fits the anchor
- whether drift signals are present

Representative display items:

- active anchor
- comparison criteria
- locked boundary
- current mismatch / drift warning

Minimum v0 display:

- `active_anchor`
- `anchor_scope`
- `locked_boundary`
- `current_comparison_result`

Working sentence:

> An anchor expression panel shows which criteria the current object is standing on.

## 4. maturation expression panel

### role

A maturation expression panel shows how meaning objects are developing.

This panel class is central to the VectorFL surface.

It should make visible:

- line candidates
- axis candidates
- interpretation notes
- harvest bundles
- comparison bundles
- linked objects
- maturity stage
- evidence density
- open edges

The core question is not simply what the object is.

The panel should show:

- how far it has matured
- what it is connected to
- what remains open
- whether external enrichment is needed
- whether axis emergence is possible

Representative display items:

- line / axis candidate zone
- linked objects map
- maturity stage
- open edges
- reread priority

Minimum v0 display:

- `object_name`
- `object_kind`
- `current_position`
- `maturity_stage`
- `linked_objects`
- `open_edges`

Working sentence:

> A maturation expression panel shows which meaning objects are growing and how.

## 5. operating expression panel

### role

An operating expression panel shows work movement and processing state.

It should make visible:

- current request packet
- current operating slot
- current holder or executor
- next slot
- validation waiting state
- external support branch
- return-ready state
- closed state

The panel should expose flow, bottleneck, and assignment context.

Representative display items:

- inbox queue
- VectorFL review queue
- engine processing queue
- validation queue
- return-ready queue
- packet route log

Minimum v0 display:

- `packet_id`
- `packet_kind`
- `current_slot`
- `next_slot`
- `assigned_team_or_executor`
- `packet_status`

Boundary:

- `assigned_team_or_executor` remains operating-extension language.
- It should not promote standing worker assignment or automatic routing into the body skeleton.

Working sentence:

> An operating expression panel shows what work has reached which processing slot.

## 6. panel emphasis by surface

### user surface

Primary emphasis:

- operating expression panels

Secondary emphasis:

- anchor expression panels

Reason:

- The user surface sets purpose, request direction, priority, distribution, and final direction.

Working sentence:

> The user surface is operating-panel centered with anchor support.

### VectorFL surface

Primary emphasis:

- maturation expression panels

Secondary emphasis:

- anchor expression panels
- partial operating expression panels

Reason:

- The VectorFL surface reads, mediates, validates, rearranges, and judges reflux value.

Working sentence:

> The VectorFL surface is maturation-panel centered with anchor and operating mediation panels.

### engine surface

Primary emphasis:

- operating expression panels

Secondary emphasis:

- minimal anchor references

Reason:

- The engine surface processes inputs, executes work, produces results, and returns trace-memory.

Working sentence:

> The engine surface is execution/processing-panel centered with minimum anchor reference.

## 7. panels as questions

Panels should be understood by the questions they answer.

### anchor expression panel questions

- Which criteria is this standing on?
- Where is the boundary?
- Is there drift?

### maturation expression panel questions

- What is growing into a line or axis?
- What is connected?
- What is still immature or open?

### operating expression panel questions

- How far has this request moved?
- Where is it blocked?
- Who or what should receive it next?

This question-based reading prevents the screen from collapsing into generic tabs.

## 8. wrong directions to avoid

### do not make maturation panels into note lists

Maturation panels must show:

- linkage
- stage
- open edges
- reread / enrichment possibility

### do not make operating panels into todo lists

Operating panels must show:

- slot movement
- route reason
- current / next slot
- validation state

### do not make anchor panels into settings pages

Anchor panels must show:

- current comparison
- boundary
- mismatch / drift signal

Panel rule:

> Each panel is not an information list. It is a reading surface for operating state.

## 9. relation to current mock and runtime views

Use this document to classify panel patterns before carrying them into `runtime/views`.

### carry direction

Panel patterns are useful when they expose:

- three-surface orientation
- anchor criteria
- line / axis / maturation state
- operating slot movement
- return / validation / reflux position

### adapt direction

Panel patterns need rewriting when they expose:

- mock evidence as current truth
- contract/final-schema language
- status labels without route meaning
- team routing as body skeleton

### hold direction

Panel patterns should stay extension-layer when they expose:

- optional tool layer selection
- role configuration
- team routing
- execution route controls
- standing worker or automatic routing assumptions

## 10. lock level

### usable now

- Panels are classified in parallel with object materiality.
- Anchor expression panels show criteria, boundary, and comparison.
- Maturation expression panels show connection, maturity, and open edges.
- Operating expression panels show slot movement, bottleneck, and next route.
- User surface is operating-centered with anchor support.
- VectorFL surface is maturation-centered with anchor and operating mediation.
- Engine surface is execution/processing-centered.
- Panels should answer questions, not only expose functions.

### not locked

- Exact UI layout
- Full panel list
- Final component names
- Visual design system
- Automatic panel generation
- Full runtime data binding

## 11. core sentence

Screen panels are not feature collections. They are expression surfaces that show anchor criteria, meaning maturation state, and operating-object slot movement.

v0 should only classify which panel class each surface needs first:

```text
anchor expression + maturation expression + operating expression
```

before committing to detailed UI layout or runtime component implementation.

