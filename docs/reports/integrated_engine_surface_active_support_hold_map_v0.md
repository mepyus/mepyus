# Integrated Engine Surface Active Support Hold Map v0

## 1. Verdict

PASS_WITH_NOTE

The current shell should be read as an operating surface, not a verification dashboard. Existing panels are not deleted; they are reclassified as active, support, or hold.

## 2. User Surface Map

| layer | content | implementation reading |
| --- | --- | --- |
| active | current purpose, scope, target, status, next action | `SurfaceCurrentObjectFocus` + single handler projection |
| active | decision / assignment candidate | user-facing package and assignment summary |
| support | team/role configuration | details block under internal team assignment |
| support | route/log panels | collapsed support route/log panel |
| hold | full bridge, lower trace, full packet origin | not front |

## 3. VectorFL Surface Map

| layer | content | implementation reading |
| --- | --- | --- |
| active | package/object under mediation | `SingleHandlerPackagePanel` projected as VectorFL |
| active | packet and evidence summary | `CliHostControlPanel` and mediation process map |
| active | blocker / next route | package panel and local focus |
| support | line atlas and selected line inspection | collapsed details |
| support | flow summary | collapsed details |
| hold | full bridge rules and lower traces | not front |

## 4. Engine Surface Map

| layer | content | implementation reading |
| --- | --- | --- |
| active | ingest target, process stage, validation, return state, output | engine package projection + `EngineCliReturnPanel` top flow |
| support | current return metadata | collapsed support details |
| support | recent returns / validation / deposit queues | support panels below active flow |
| hold | old engine mock, asset inventory, watcher/queue detail | collapsed legacy support |

## 5. What Changed In Priority

- Shared spine is thinner and hides detail in support.
- Single-handler package appears before broad team/line/detail surfaces.
- User surface foregrounds decision/action, not team management.
- VectorFL foregrounds mediation and evidence, not full atlas.
- Engine foregrounds process/return, not maintenance dashboard.

## 6. Validation

- Surface first-question check: passed.
- Overlap reduction check: passed. Same package is projected differently per surface.
- Detail demotion check: passed. Line atlas, team config, engine mock, and shared spine detail are support/drill-down.

