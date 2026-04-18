# Integrated Engine Three-Surface Representative Panel Layout v0

Date: 2026-04-15

## 0. purpose

This document is a working draft, not a final UI design.

It applies the screen-panel classification criteria to the three integrated-engine surfaces.

The goal is not to make a pretty UI proposal.

The goal is to define which panel groups should become central if each surface is going to perform its role.

Do not read this document as:

- final visual layout
- final component architecture
- final runtime implementation plan
- final responsive design rule
- complete panel inventory

Read it as:

- v0 representative panel-placement language
- a structure draft for keeping the three surfaces functionally different

## 1. common premise

The three surfaces should not be made the same way.

- User surface centers organization operation and request distribution.
- VectorFL surface centers mediation, translation, validation, and maturation.
- Engine surface centers processing execution and return generation.

The three surfaces are not the same information viewed differently.

They are different surfaces answering different questions inside the same circulation.

Key sentence:

> Each surface should center a different panel type so the three-surface body keeps its role separation.

## 2. common top state strip

All three surfaces should share a minimum top state strip.

This strip should show:

- current active anchor
- current active packet
- current selected object
- current loop state
- drift / hold / validation-needed signals

Role:

- This is the common coordinate layer across all surfaces.
- Even if the panels differ, the user should know what object and loop are currently being read.

Boundary:

- This is a shared orientation strip, not a command center by itself.

## 3. user surface representative layout

User surface should use:

- operating expression panels as the center
- anchor expression panels as support
- minimal return confirmation

Recommended arrangement:

```text
left   = request / organization
center = current operating flow
right  = anchor / judgment support
bottom = return / decision record
```

### 3.1 left - request / organization panel

Role:

- This is the starting panel of the user surface.

It should handle:

- current goal
- request directionality
- team / role placement as operating extension
- priority
- external support need
- distribution toward implementation, search, internal review, or engine-side work

Question:

- What are we trying to do?
- Who or what should receive it?
- Is external support needed?

Boundary:

- This is an organization operating panel.
- Team/role fields remain operating extension, not body skeleton.

### 3.2 center - operating flow panel

Role:

- This is the core panel of the user surface.

It should show:

- request packet list
- current slot
- next slot
- executor candidate
- bottleneck
- validation waiting state
- return-ready state

Question:

- How far has the request moved?
- Where is it blocked?
- Who or what receives it next?

Central-panel rule:

> The user surface center is operating flow, not maturation canvas.

### 3.3 right - anchor / judgment support panel

Role:

- This panel keeps user-side decisions attached to criteria.

It should show:

- anchors referenced by the current request
- locked boundary
- whether the request fits the anchor
- risk of bypassing validation
- purpose / anchor conflict

Question:

- Is this operating decision still aligned with the anchor?

### 3.4 bottom - return / decision record panel

Role:

- This panel receives returns and supports next distribution.

It should show:

- return packet summary
- produced artifacts
- follow-up need
- next distribution candidates
- decision log

Question:

- What came back?
- What decision or next distribution is needed?

## 4. VectorFL surface representative layout

VectorFL surface should use:

- maturation expression panels as the center
- anchor review as context
- operating mediation as side function
- reflux judgment as an explicit branch

Recommended arrangement:

```text
left         = anchor / context
center       = maturation canvas
right top    = validation / mediation
right bottom = routing / reflux
bottom       = evidence / history
```

### 4.1 left - anchor / context panel

Role:

- This panel keeps interpretation tied to criteria.

It should show:

- active anchors
- anchors referenced by the current object
- comparison criteria
- drift signals
- boundary conflicts

Question:

- On which criteria is this interpretation standing?

### 4.2 center - maturation canvas panel

Role:

- This is the heart of the VectorFL surface.

It should show:

- line candidates
- axis candidates
- interpretation notes
- comparison bundles
- linked objects
- maturity stage
- evidence density
- open edges

Question:

- What is growing?
- What is connected?
- What remains immature or open?

Central-panel rule:

> The VectorFL surface center is maturation canvas, not request list.

Boundary:

- This should not collapse into a simple card list.
- It must show connection, emergence, and open edges.

### 4.3 right top - validation / mediation panel

Role:

- This panel decides how a current object or return should be handled.

It should show:

- current judgment state
- validation points
- result confidence
- open questions
- whether reprocess, external support, return, or reflux is appropriate

Question:

- What judgment is needed before the object moves?

### 4.4 right bottom - routing / reflux panel

Role:

- This panel decides where to send the result and what should return to the space.

It should show:

- suggested next route
- reflux need
- reflux target zone
- maturation value
- next packet candidate

Question:

- Should this move to another surface, or should it be refluxed into the space?

Boundary:

- Routing remains mediation, not automatic routing lock.

### 4.5 bottom - evidence / history panel

Role:

- This panel prevents interpretation from drifting into unsupported intuition.

It should show:

- origin refs
- related packets
- route log
- comparison reasons
- last touched reason

Question:

- What evidence and route produced this interpretation?

## 5. engine surface representative layout

Engine surface should use:

- operating processing panels as the center
- input / output clarity
- minimum anchor reference
- execution trace

Recommended arrangement:

```text
left   = work input
center = execution state
right  = result / return
bottom = execution history
```

### 5.1 left - work input panel

Role:

- This panel clarifies what entered the engine surface.

It should show:

- request packet
- input materials
- request type
- expected output shape
- current anchor refs
- validation points

Question:

- What exact operating unit is being processed?

### 5.2 center - execution state panel

Role:

- This is the core panel of the engine surface.

It should show:

- current processing work
- script / CLI / executor state
- processing slot
- error / interruption / retry state
- produced-artifact state

Question:

- What is executing now and what is its processing condition?

Central-panel rule:

> The engine surface center is execution state, not interpretation notes.

### 5.3 right - result / return panel

Role:

- This panel organizes engine output into returnable form.

It should show:

- return summary draft
- produced artifacts
- result confidence
- open questions
- suggested next route
- return packet draft

Question:

- What can be returned, and how reliable is it?

Boundary:

- Report return does not mean product completion.
- Return artifact is not a chat-only note.
- Return should include trace-memory.

### 5.4 bottom - execution history panel

Role:

- This panel preserves processing trace.

It should show:

- route log
- execution log
- failure reason
- retry reason
- input / output trace

Question:

- What actually happened during processing?

## 6. one-line surface summaries

### user surface

Question:

- What should be done, why, and who or what should receive it?

Central panels:

- request / organization
- operating flow
- return / decision

### VectorFL surface

Question:

- What is connected, under which criteria, and where should it go?

Central panels:

- maturation canvas
- validation / mediation
- routing / reflux

### engine surface

Question:

- What input should be processed, what is executing, and what return can be produced?

Central panels:

- work input
- execution state
- result / return

## 7. central-panel principles v0

### principle 1

The user surface center should be operating flow, not maturation canvas.

### principle 2

The VectorFL surface center should be maturation canvas, not request list.

### principle 3

The engine surface center should be execution state, not interpretation notes.

These central panels should differ.

That difference is what keeps the three-surface structure legible.

## 8. minimum representative panel groups v0

### user surface

- request / organization panel
- operating flow panel
- anchor support panel
- return / decision panel

### VectorFL surface

- anchor / context panel
- maturation canvas panel
- validation / mediation panel
- routing / reflux panel
- evidence / history panel

### engine surface

- work input panel
- execution state panel
- result / return panel
- execution history panel

## 9. lock level

### usable now

- User surface is operating-centered.
- VectorFL surface is maturation and mediation-centered.
- Engine surface is processing execution-centered.
- The three central panels should differ.
- The top state strip should provide common coordinates across surfaces.

### not locked

- Exact visual layout
- Pixel-level design
- Component names
- Runtime data binding
- Responsive layout
- Full panel inventory
- Automation between panels

## 10. core sentence

The representative panel layout should differ by surface: user surface centers operating flow, VectorFL surface centers maturation and mediation, and engine surface centers processing execution.

v0 only needs to lock the central panel difference:

```text
user = operating flow
VectorFL = maturation canvas
engine = execution state
```

before deciding detailed UI layout or runtime component implementation.

