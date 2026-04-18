# Integrated Engine VectorFL Surface Visual Translation Brief v0

Date: 2026-04-15

## 0. verdict

PASS

The selected `gemini/mock_test` VectorFL visual grammar can be translated onto the current integrated-engine baseline if the line atlas remains a support selection layer and the center remains `maturation_canvas_panel`.

This is a visual translation brief only. It does not change scaffold read mappings, create panels, introduce runtime binding, or promote line browsing into the VectorFL body skeleton.

## 1. purpose

This brief translates selected visual grammar from the VectorFL mock into the current VectorFL-surface baseline.

Current baseline stays fixed:

- VectorFL surface = mediation / validation / maturation surface
- center panel = `maturation_canvas_panel`
- center reading = maturation object body reading
- panels remain `anchor_context_panel`, `maturation_canvas_panel`, `validation_mediation_panel`, `routing_reflux_panel`, and `evidence_history_panel`
- line / axis / inspection visuals are support readings
- anchor, maturation, and operating objects stay visually separated
- current scaffold read mapping remains unchanged

## 2. selected mock grammar

Allowed visual sources:

- line atlas selection rhythm, only as support selection
- line inspection side card visual token
- weak point / risk / open edge presentation
- connected lines / anchors / lineage tokens that can be translated to baseline fields
- compact cards and small badges for maturity stage, evidence density, open edges, and drift risk
- health-like indicators only when rewritten as maturity / open-edge indicators

Held out:

- VectorFL center as atlas / list browser
- line cards visually dominating maturation object body
- global maturity score as primary truth
- `OperationConsolePanel` as a core panel
- anchor, line, request, return, and reflux in one undifferentiated card language
- watcher / governance / supervisor authority language
- runtime or live manifest truth
- new core panel

## 3. mock element -> baseline panel mapping

| mock source | visual grammar to keep | baseline panel | translation rule | do not carry |
|---|---|---|---|---|
| `FlowSummaryPanel` | compact summary boxes and small stat cards | `maturation_canvas_panel` support header | Rewrite stats as selected maturation object fields: `maturity_stage`, `evidence_density`, linked object count, open edge count. | Global `Total Lines`, global `Maturation %`, "Interpretation Lab" as primary identity. |
| `Line Atlas` list in `VectorFLIntegrationShell.tsx` | selectable list rhythm | support selection layer | Use only to select a candidate line / axis / maturation object. Keep visually smaller than center. | Atlas/list as center, line browser as VectorFL identity. |
| selected line inspection card | side inspection layout | `maturation_canvas_panel` support detail | Translate `purpose`, `health`, `connectedTo`, `weakPoints`, `lineage` into current position, maturity, linked objects, open edges, origin/support notes. | Mock health as truth, generic line score, selection-only behavior as core structure. |
| `jang_lines.json.anchors` | small anchor tokens | `anchor_context_panel` | Translate to anchor refs or criteria chips. | Mixing anchors into maturation body without boundary labels. |
| `jang_lines.json.connectedTo` | relation chips / linked-object rows | `maturation_canvas_panel` | Translate to `linked_objects` or related line/axis support rows. | Treating connected lines as execution route. |
| `jang_lines.json.weakPoints` | warning chips / open edge rows | `maturation_canvas_panel` | Translate to `open_edges`. | Generic risk dashboard or global health alert. |
| `jang_lines.json.lineage` | compact provenance row | `maturation_canvas_panel` / `evidence_history_panel` | Translate to origin / reread / evidence trail support. | Runtime provenance truth without manifest support. |
| `jang_lines.json.refluxFromUser` | reflux note token | `routing_reflux_panel` | Translate to reflux reason or maturation value support. | User feedback as final validation. |
| `WatchpointRegistryPanel` | severity / status badge rhythm | `anchor_context_panel` support | Use for anchor drift / unresolved criteria when grounded in anchor or connection records. | Watcher registry, live intervention command. |
| `SpaceHealthPanel` | thin risk indicator / progress bar token | support only | Use sparingly for open-edge density or anchor-drift warning. | Baseline sync %, global maturity %, intervention authority. |
| `OperationConsolePanel` | none for core body | none | Keep only its own boundary phrase: optional tool layer after line shaping. | CLI input, play button, command console, tool layer as core panel. |

## 4. panel-by-panel visual translation

### `maturation_canvas_panel`

Use:

- largest central body card
- selected maturation object name and kind
- field groups for `origin_refs`, `current_position`, `maturity_stage`, `linked_objects`, `evidence_density`, and `open_edges`
- weak point / open edge chips from line inspection grammar
- connected object rows from line atlas inspection grammar
- small maturity / evidence badges, not global scores

Avoid:

- making line atlas the center
- showing only a list of lines
- global maturation percentage as primary truth
- merging anchor criteria, request packets, return packets, and reflux into one untyped story card

Reading note:

- The central question is not "which line is selected?" but "what maturation object body is growing, and what remains open?"

### `anchor_context_panel`

Use:

- compact criteria card
- anchor ref chips
- boundary / comparison rule note
- drift-risk badge if present
- watchpoint-style severity badge only when tied to anchor mismatch or comparison rule

Avoid:

- health dashboard framing
- governance score
- live baseline sync percentage
- treating anchor as a line tag only

Reading note:

- Anchor context answers which criteria the current object stands on. It should remain visually distinct from maturation and operating panels.

### `validation_mediation_panel`

Use:

- compact two-material comparison rhythm
- request packet / return packet summary cards
- validation-point chips
- route decision badge: validate, recheck, reprocess, user decision, reflux
- hold / drift / follow-up badge if the route is not ready

Avoid:

- final decision authority
- command console
- line browser interaction as mediation
- engine execution controls

Reading note:

- This is where VectorFL mediates request and return material before next route. It should look like review / mediation, not execution.

### `routing_reflux_panel`

Use:

- reflux reason card
- target zone badge
- maturation value note
- linked line / axis support chips
- route arrow from return to reflux / maturation body

Avoid:

- user feedback score as primary truth
- global reflux rate as current route truth
- treating reflux as product completion

Reading note:

- Reflux is preservation and reread route. It should stay separate from return packet and maturation object body.

### `evidence_history_panel`

Use:

- compact evidence / lineage row style
- selected connection record rows
- small source / emitted state / target panel labels
- lineage token style from `jang_lines.json.lineage`

Avoid:

- live history feed
- watcher event feed
- generic audit log
- full manifest dump

Reading note:

- This panel makes circulation visible through connection records and evidence trails. It should not become a runtime event console.

## 5. line atlas support rule

Line atlas visuals may appear only after these conditions are met:

- the `maturation_canvas_panel` remains the largest and central body
- line selection controls are visually smaller than the maturation object body
- selected line data is translated into maturation fields, not shown as raw line browser data
- `anchors`, `connectedTo`, `weakPoints`, `lineage`, and `refluxFromUser` are separated into anchor / maturation / reflux / evidence areas
- line cards do not define the VectorFL surface by themselves

Allowed line atlas usage:

- left-side candidate selector
- small related object picker
- linked object support list
- axis candidate support rail

Forbidden line atlas usage:

- central line browser
- card grid larger than maturation object body
- selected line as final concept
- raw health score as maturity truth
- line affinity as automatic route

## 6. allowed / forbidden by panel

| baseline panel | allowed | forbidden |
|---|---|---|
| `anchor_context_panel` | anchor chips, boundary note, comparison rule card, drift-risk badge | global sync score, governance authority, line tag-only anchor |
| `maturation_canvas_panel` | object body card, maturity/evidence badges, linked object rows, open edge chips | atlas as center, global maturity score, raw line list dominance |
| `validation_mediation_panel` | request/return comparison cards, validation chips, route badge, hold/recheck badge | command console, final verdict, engine controls |
| `routing_reflux_panel` | reflux target badge, maturation value note, linked axis chips, preserve trace rows | user feedback score as truth, reflux as completion |
| `evidence_history_panel` | connection record rows, lineage tokens, emitted state labels | live watcher feed, audit console, full manifest dump |
| support layer | line selector, side inspection, weak point list, connected lines | new core panel, atlas identity, operation console |

## 7. pseudo layout proposal

This is a layout note only. It is not an implementation instruction.

```text
vectorfl_surface

top band:
  small surface label: VectorFL surface
  one-line role: mediation / validation / maturation
  boundary note: line atlas is support selection; maturation object body is center

main layout:
  left column:
    anchor_context_panel
      active anchor chips
      boundary / comparison rule note
      drift risk badge if present

    support selection layer
      compact line / axis candidate selector
      no global maturity truth

  center column:
    maturation_canvas_panel
      largest card, central
      object name / kind
      origin refs
      current position
      maturity stage / evidence density
      linked objects
      open edges

  right column:
    validation_mediation_panel
      request / return review cards
      validation points
      next route badge

    routing_reflux_panel
      reflux target
      maturation value
      preserve trace items

    evidence_history_panel
      compact connection / lineage rows
```

Support layer:

- The line atlas can help choose what the center reads.
- The line atlas must not be the center.
- Side inspection may appear only as translated support detail for the selected maturation object, anchor, or route.

## 8. visual token guidance

Use:

- compact object body cards
- small field labels
- anchor chips distinct from linked-object chips
- open-edge warning chips
- maturity / evidence badges
- thin relation lines
- side inspection cards with clear support status

Avoid:

- list-browser dominance
- "Interpretation Lab" as central product identity
- health score as maturity truth
- OperationConsolePanel / CLI controls
- global dashboard metrics
- anchor, line, request, return, and reflux in one visual grammar
- copy implying live binding or automatic routing

## 9. preservation note

This brief does not change:

- `runtime/views/vectorfl_surface_scaffold_v0.tsx`
- panel names
- panel read mapping
- manifest paths
- runtime binding
- file watching
- routing behavior

It only defines how selected VectorFL mock visual grammar may be translated later while preserving the current working baseline.

