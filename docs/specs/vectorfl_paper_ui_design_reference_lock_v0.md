# vectorfl paper ui design reference lock v0

## 1. purpose

This lock records how Paperclip UI should be referenced for VectorFL Paper design work.
The goal is not to copy Paperclip screens, but to translate its operating-board rhythm,
console density, and panel role separation into VectorFL semantics.

## 2. reference summary

### design guide

Read from `ui/src/pages/DesignGuide.tsx`:

- typography hierarchy is compact and explicit
- uppercase section headings use small muted text with tracking
- mono identifiers and log text are normal parts of the surface
- badge and status systems are quiet and structural, not decorative
- breadcrumbs and command shells make the UI feel like a tool, not a landing page
- radius is restrained; large soft cards are not the visual center

### dashboard

Read from `ui/src/pages/Dashboard.tsx`:

- compact metric strips come before hero presentation
- metrics combine number, status, and small explanatory line
- recent activity and recent tasks are list surfaces with borders and dividers
- panel role separation matters more than card repetition

### org chart

Read from `ui/src/pages/OrgChart.tsx`:

- some surfaces should behave like bounded canvases, not only cards and lists
- panel UI and spatial/canvas UI may coexist with different density
- controls remain compact and border-led even on canvas surfaces

### index css

Read from `ui/src/index.css`:

- neutral and muted tones carry most of the hierarchy
- border and foreground contrast do more work than shadow
- dark mode avoids neon and keeps restrained contrast
- small text and tight spacing create the operating console tone
- large radii are mostly removed; sharpness supports structure reading

## 3. current vectorfl paper drift

The current VectorFL Paper prototype is structurally strong but visually still drifts in
three ways:

- panels are slightly too soft and card-like
- some surfaces still read as grouped cards instead of bounded operating lists
- the shell hierarchy is visible semantically, but not yet tight enough typographically

## 4. locked design translation rules

### color and tone

- prefer neutral, muted, and border-led hierarchy
- avoid warm decorative gradients and soft-card comfort as the dominant tone
- use state color sparsely and only for actual restriction or caution emphasis

### layout

- compact summary strip before large hero treatment
- primary surface should feel like an operating pane, not a marketing module
- recent lists should prefer dividers and row density over stacked cards
- contextual side panels should look subordinate but inspectable

### component shell

- repeated generic cards should be demoted
- use list shells, row shells, dividers, and small chips more aggressively
- keep mono identifiers and small labels visible
- preserve bounded panel roles: navigation, primary surface, governance carry, contextual detail

## 5. non-goals

- do not import Paperclip ontology
- do not turn VectorFL Paper into a generic startup admin dashboard
- do not rely on glow, blur, glass, or oversized hero sections
- do not explain status by color alone

## 6. current implementation target

The first target of this design lock is the shared app-shell renderer used by:

- `vectorfl_page_shell/*`
- `vectorfl_page_shell/semi_live_routes/*`

That renderer should be tightened first because it is the main operating shell for the
current prototype.
