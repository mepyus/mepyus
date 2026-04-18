# Integrated Engine Use Observation Protocol v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

The current integrated-engine baseline is in use observation mode, not build mode.

This protocol defines how to repeat manual use observations without changing scaffold files, manifest shapes, read maps, token systems, runtime behavior, or extension status.

## 1. purpose

The purpose is to observe whether wording confusion repeats during real use.

The purpose is not to:

- find every missing feature
- restart visual redesign
- add selected-object behavior
- add trace UI
- bind runtime data
- promote extensions
- patch wording immediately

Current baseline status:

- usable for manual scenario reading
- stable enough for stop-and-use
- still PASS_WITH_NOTE because wording and trace/render-field thinness remain

## 2. observation target

Observe only repeated wording confusion.

Do not treat these as wording confusion:

- known fixture scope limits
- compact core-support trace boundary
- lack of selected-object behavior
- lack of trace UI
- lack of runtime binding
- lack of actual empty-state UI
- support layer being intentionally subordinate

These are already held or bounded by the current baseline documents.

## 3. baseline surfaces to protect

Protected central panels:

| surface | central panel | protected reading |
|---|---|---|
| user | `operating_flow_panel` | operating / distribution / decision |
| VectorFL | `maturation_canvas_panel` | mediation / validation / maturation body reading |
| engine | `execution_state_panel` | processing / execution / return-draft |

Observation must not recommend a change that weakens these centers.

## 4. repeatable scenario set

Use these three scenario families:

| scenario id | scenario | entry surface | expected route |
|---|---|---|---|
| S1 | user-origin normal loop | user surface | user request -> VectorFL review -> engine return -> VectorFL validation -> reflux / user decision |
| S2 | VectorFL-origin follow-up / reactivation loop | VectorFL surface | maturation signal -> user organization -> engine follow-up return -> user decision / VectorFL recheck |
| S3 | anchor drift -> reprocess / reflux loop | VectorFL surface | engine return -> anchor drift hold -> engine reprocess request -> loop remains open |

Additional scenarios may be added later only as use observations, not as new structure.

## 5. observation unit

Record confusion at this unit:

- scenario
- surface
- panel
- current wording or current reading
- intended reading
- actual confusion
- repeat status
- whether it is wording-only
- whether it is fixture scope, trace boundary, or held extension

Do not record broad statements like:

- "the UI needs more features"
- "the trace is missing"
- "the side panel should be interactive"
- "the engine should show live status"

Those are build-mode statements, not use-observation units.

## 6. structural issue vs wording issue

### wording issue

A wording issue is present when:

- the current structure works
- central panel gravity remains correct
- the panel's mapped manifest still makes sense
- the confusion comes from phrasing, label, or explanatory copy
- a future wording-only patch could clarify the existing boundary

Example:

- "incoming request" may sound user-origin only in a VectorFL-origin follow-up loop.

### structural issue

A structural issue would require:

- new panel
- read-map change
- manifest shape change
- runtime binding
- selected-object behavior
- trace UI
- extension promotion

Current stance:

- no structural issue has been observed in the current manual scenario set.

## 7. fixture scope vs confusion

Fixture scope limit:

- current scaffold read maps are centered on the first sample fixture
- follow-up and drift-reprocess samples are checked manually through the same panel-role grammar

This is not wording confusion by itself.

It becomes wording confusion only if a panel label or support note makes the manual reread path sound invalid, forbidden, or structurally wrong.

## 8. core-support trace boundary vs confusion

Core-support trace allows:

- mapped manifest path
- read role
- read reason
- mapped connection record
- compact route / reflux / return wording

Core-support trace does not include:

- full timeline
- trace UI
- selected row drilldown
- live event feed
- worker telemetry
- watcher / supervisor / bridge authority

Trace thinness is not a wording confusion unless wording implies a denser trace than the baseline actually supports.

## 9. observation pass process

For each manual observation pass:

1. Select one scenario family: S1, S2, or S3.
2. Read the current central panel for the active surface.
3. Read the mapped packet/object for the panel.
4. Read support panels only after the center is understood.
5. Read connection records when reconstructing route.
6. Record wording confusion only if it affects use-time reading.
7. Classify the item as:
   - already observed candidate
   - repeated confusion
   - fixture scope, not confusion
   - core-support trace boundary, not confusion
   - held extension, not confusion
   - possible structural issue
8. Do not patch during the observation pass.

## 10. stop condition

Stop observation and escalate only if:

- the scenario cannot be read without selected-object behavior
- trace UI is required for the baseline to work
- central panel gravity collapses during use
- request / return / reflux cannot be separated
- a wording issue repeatedly hides a baseline rule across scenarios

Current state:

- no stop condition is active.

## 11. output expected from each use observation

Each observation round should produce:

- scenario observed
- panels read
- route readability
- support-layer behavior
- confusion items, if any
- non-confusion thinness items
- recommended mode:
  - continue use
  - log more observations
  - wording-only gate review
  - hold

## 12. closeout sentence

Use observation exists to protect the current baseline from premature build work: observe repeated wording confusion, separate it from fixture and trace thinness, and only then consider wording-only promotion.
