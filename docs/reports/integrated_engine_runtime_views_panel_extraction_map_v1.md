# Integrated Engine Runtime Views Panel Extraction Map v1

Date: 2026-04-14

## 0. Purpose

This document treats `gemini/mock_test` as a panel pattern library, not as source of truth.

This pass does not move files, implement runtime wiring, define final schemas, or promote mock labels into canonical language. It only selects which panel patterns can be considered for later `runtime/views` carry-over under `integrated_engine_setup_working_lexicon_v0`.

Current body reading:

- User surface = `goal / scope / material-context start surface`
- VectorFL surface = `intermediate-formation reading / translation surface`
- Engine surface = `ingest / process / validate / trace-memory / return surface`

Current boundary:

- Team / role / relay / routing / operation console / CLI / agent selection remain operating extension or optional tool layer.
- `live_manifest.json`, `dist/`, mock readability labels, and contract-like labels must not be treated as canonical runtime evidence.

## 1. Extraction Verdict

Use the `gemini/mock_test` page as a design and panel-shape reference only.

Do not carry it as a whole app. Extract only the patterns that strengthen the three-surface body and adapt any labels that might make mock evidence look like current truth.

## 2. Carry Now

These patterns can be carried into the next runtime/views design pass after local adaptation to the existing app structure.

| Pattern | Source refs | Judgment reason |
|---|---|---|
| Three-surface nav | `gemini/mock_test/VectorFLIntegrationShell.tsx` | Matches the body split. It keeps User / VectorFL / Engine surfaces visible without making engine execution a direct user bypass. |
| Orientation band | `gemini/mock_test/VectorFLIntegrationShell.tsx` | Useful for showing `Goal/Scope/Material -> Line/Relation/Gap/Pending -> Process/Validate -> Trace-Memory Return`. Keep it small and explanatory, not a workflow board. |
| User Goal & Scope panel | `gemini/mock_test/CommandHeaderPanel.tsx`, `gemini/mock_test/user-surface.seed.ts` | Matches user surface as the goal / scope / material-context start surface. Carry the pattern, not the mock stats as truth. |
| VectorFL Line Atlas | `gemini/mock_test/VectorFLIntegrationShell.tsx`, `gemini/mock_test/jang_lines.json` | Matches VectorFL as line-first intermediate reading. Good base for line selection and active-line reading. |
| VectorFL line inspector skeleton | `gemini/mock_test/VectorFLIntegrationShell.tsx` | Carry the field grouping pattern for `purpose`, `connectedTo`, `weakPoints`, `refluxFromUser`, `lineage`, and `notes`. Keep `health` as readability-only, not canonical enum. |
| Engine primary pipeline skeleton | `gemini/mock_test/vectorfl_engine_surface_mock.tsx` | `IngestEntryPanel -> PipelineStatusPanel -> ValidationReturnPanel` matches engine surface as ingest / process / validate / return. |
| Work memory / return trace placement | `gemini/mock_test/vectorfl_engine_surface_mock.tsx` | Supports return as trace-memory material, not just a result text. |
| Asset / Watch / Trace Audit shape | `gemini/mock_test/vectorfl_engine_surface_mock.tsx`, `AssetInventoryPanel.tsx`, `AssetInspectorPanel.tsx`, `WatchpointRegistryPanel.tsx`, `EventConsolePanel.tsx` | Useful as secondary monitoring layer. Carry only as runtime evidence display after binding to real manifests/freshness gates. |

## 3. Adapt Before Carry

These patterns are useful, but must be rewritten or rewired before they can move into `runtime/views`.

| Pattern | Source refs | Required adaptation | Reason |
|---|---|---|---|
| Panel titles | `CommandHeaderPanel.tsx`, `FlowSummaryPanel.tsx`, `vectorfl_engine_surface_mock.tsx` | Use working lexicon wording: `Goal / Scope / Material Context`, `VectorFL Line Reading`, `Engine Trace-Memory Return`. | Avoid command center / control room / contract-like overtones. |
| Status labels | `engine-surface.types.ts`, `jang_lines.json`, engine panels | Treat `health`, `status`, `stage` as view labels unless backed by runtime evidence. | Prevent mock readability labels from becoming final enums. |
| Mock evidence labels | `SlotAttachmentNote`, `live_manifest.json`, `engine-surface.seed.ts` | Rename around `mockAttachmentPoint / actualAttachmentPoint` to make mock vs runtime evidence explicit. | The attachment split is useful, but the mock side cannot become proof. |
| Return/freshness warning copy | `vectorfl_engine_surface_mock.tsx` | Keep and normalize: `latest completed != current truth without freshness gate`, `report return != product completion`, `return artifact != chat-only note`, `return includes trace-memory`. | These are engine-surface safety rails and should survive carry-over. |
| Runtime data slots | `engine-surface.seed.ts`, `live_manifest.json` | Replace mock manifest reads with the current runtime/latest manifest path and freshness-gate logic in a later implementation pass. | `live_manifest.json` is test evidence, not current truth. |
| UI wrappers | `ui-components.tsx` | Reuse only if needed as compatibility wrappers. Prefer the current runtime app's UI wrapper strategy. | Avoid importing sandbox-only assumptions into the runtime shell. |
| Space health panel wording | `SpaceHealthPanel.tsx` | Keep as mock alignment/health view only; avoid `constitution` and final baseline wording. | Health display is useful, but current basis is working lexicon, not final constitution. |
| Legacy mock shell | `vectorfl_dual_surface_ui_mock_v_1.tsx` | Treat as legacy/contrast unless it becomes active. Do not carry both shells. | Avoid duplicated shells and stale field assumptions. |

## 4. Hold As Extension

These can remain in a later extension drawer, optional tab, or experiment, but should not be part of the current body skeleton.

| Pattern | Source refs | Hold reason |
|---|---|---|
| OperationConsolePanel | `gemini/mock_test/OperationConsolePanel.tsx` | Optional tool layer. It should not become the center of VectorFL surface or imply user-to-engine CLI bypass. |
| RoleConfigurationPanel | `gemini/mock_test/RoleConfigurationPanel.tsx` | Team/role/agent/tool assignment is operating extension. Useful later, not body language now. |
| TeamRoutingPanel | `gemini/mock_test/TeamRoutingPanel.tsx` | Team routing is not user surface skeleton. Keep as extension if needed. |
| ExecutionRoutePanel | `gemini/mock_test/ExecutionRoutePanel.tsx` | Ticket lifecycle / handoff / review flow is extension language. Do not flatten VectorFL into workflow board. |
| OperationLogPanel | `gemini/mock_test/OperationLogPanel.tsx` | Report/log feed can support operation, but report return is not product completion and not body skeleton. |
| SupervisorQueuePanel | `gemini/mock_test/SupervisorQueuePanel.tsx` | Recommendation/queue language risks routing-field promotion. Hold until low-intensity tests prove need. |
| BridgePanel | `gemini/mock_test/BridgePanel.tsx` | Bridge direction is useful later, but user/VectorFL/engine surface boundaries must be stabilized first. |
| Agent / Tool / Model selection UI | `RoleConfigurationPanel.tsx`, `OperationConsolePanel.tsx` | Optional tool layer. Do not encode standing worker assignment or automatic routing. |

## 5. Do Not Treat As Canonical

These may be present in the sandbox, but must not be used as runtime truth or final model evidence.

| Artifact / label | Source refs | Reason |
|---|---|---|
| `live_manifest.json` | `gemini/mock_test/live_manifest.json` | Mock evidence only. Runtime truth requires latest manifests and freshness gate. |
| `dist/` output | `gemini/mock_test/dist/` | Generated build output. Do not edit or read as canonical source. |
| Mock readability labels | `LineHealth`, `health: strong/growing/thin`, `SpaceHealthPanel` values | Surface readability only. Not final enum or schema. |
| Contract-like labels | prior `SURFACE CONTRACT CANDIDATE`, `Surface Contract v0.1` wording | Too lock-like for current phase. Use `mock attachment candidate` or `operating view candidate` only when needed. |
| `EngineIngestSlot`, `EnginePipelineSlot`, `ValidationReturnPacket` as final types | `engine-surface.types.ts` | Useful UI test shapes, not final schema. |
| `jang_lines.json` | `gemini/mock_test/jang_lines.json` | Good line display sample. Not current integrated-engine line source of truth. |
| `WORK_REFLUX_LOG.md` | `gemini/mock_test/WORK_REFLUX_LOG.md` | Historical sandbox note. Use as lineage/contrast, not current body language. |

## 6. Panel-by-Panel Map

| Panel / file | Decision | Reason |
|---|---|---|
| `VectorFLIntegrationShell.tsx` | carry now, with adaptation | Best source for three-surface nav, orientation band, and body/extension separation. Adapt labels before runtime carry. |
| `CommandHeaderPanel.tsx` | carry now | Good user surface start panel after `infoBoxes` prop alignment. Add explicit scope/material fields later only if runtime view model supports them. |
| `MaterialContextPanel.tsx` | carry now / merge into user surface | Fits user surface material context. It may be merged with the header rather than carried as a separate card. |
| `FlowSummaryPanel.tsx` | adapt before carry | Useful VectorFL summary, but labels like strongest/weakest/current focus should remain reading aids, not maturity rules. |
| `VectorFL line inspector block` | carry now | Strong fit for line-first reading if it renders actual line fields and not invented fields. |
| `vectorfl_engine_surface_mock.tsx` | carry now, split before carry | Strong engine surface skeleton. Should be split into ingest / pipeline / validation return / memory panels before runtime integration. |
| `AssetInventoryPanel.tsx` | adapt before carry | Useful as runtime evidence browser. Must bind to real assets and freshness status. |
| `AssetInspectorPanel.tsx` | adapt before carry | Useful trace/detail view. Must avoid treating mock warnings as current proof. |
| `WatchpointRegistryPanel.tsx` | adapt before carry | Useful monitoring panel. Needs runtime evidence source. |
| `EventConsolePanel.tsx` | adapt before carry | Useful trace/event display. Needs real event source and freshness note. |
| `FilterBarPanel.tsx` | adapt before carry | Reusable utility, but only after target data model is chosen for the view. |
| `SpaceHealthPanel.tsx` | adapt before carry | Good high-level health panel if presented as working-lexicon alignment/freshness, not final constitution. |
| `OperationConsolePanel.tsx` | hold as extension | Optional tool layer. Do not place in body path yet. |
| `RoleConfigurationPanel.tsx` | hold as extension | Assignment/worker tooling. Not body skeleton. |
| `TeamRoutingPanel.tsx` | hold as extension | Routing board. Not body skeleton. |
| `ExecutionRoutePanel.tsx` | hold as extension | Workflow/ticket lifecycle. Not body skeleton. |
| `OperationLogPanel.tsx` | hold as extension | Useful operation history later; not body return semantics. |
| `SupervisorQueuePanel.tsx` | hold as extension | Queue/recommendation language risks premature routing. |
| `BridgePanel.tsx` | hold as extension | Useful later after surface boundaries stabilize. |
| `ui-components.tsx` | adapt before carry | Thin wrappers are useful, but runtime app should keep its own wrapper/design strategy. |
| `engine-surface.types.ts` | do not treat as canonical | Use only as mock UI shape reference. Not final engine schema. |
| `engine-surface.seed.ts` | do not treat as canonical | Mock data adapter. Replace later with runtime evidence adapter. |
| `user-surface.types.ts` | hold / do not canonicalize | Team/role types are extension-language in current phase. |
| `user-surface.seed.ts` | adapt before carry | Some user wording is useful; team seed remains extension mock data. |
| `vectorfl_meta.json` | do not treat as canonical | Summary seed only. |
| `jang_lines.json` | adapt before carry | Good sample for line atlas fields, not current truth. |
| `live_manifest.json` | drop as canonical | Mock manifest only. |
| `vectorfl_dual_surface_ui_mock_v_1.tsx` | drop / lineage only | Legacy duplicate shell. Keep only as contrast unless explicitly revived. |
| `dist/` | drop | Generated output. |

## 7. Before / After Wording Examples

| Before | After |
|---|---|
| `Surface Contract v0.1` | `Mock view draft` |
| `SURFACE CONTRACT CANDIDATE` | `MOCK ATTACHMENT CANDIDATE` / `OPERATING VIEW CANDIDATE` |
| `Operation Hub` | `Optional Tool Layer Console` |
| `Active Teams` | `Goal State` or extension-only team status |
| `Operational Flow: team -> role -> execution` | `Next Surface: VectorFL intermediate reading` |
| `latest completed` as proof | `latest completed != current truth without freshness gate` |
| `report returned` as completion | `report return != product completion` |

## 8. Runtime Carry Sequence

Recommended next pass, without physical folder moves:

1. Update the current runtime view plan with the selected carry/adapt/hold/drop map.
2. Identify the minimal `runtime/views` target component boundaries for:
   - surface nav
   - orientation band
   - user goal/scope/material panel
   - VectorFL line atlas/inspector
   - engine evidence summary/return panel
3. Map data slots to current runtime evidence:
   - latest manifests
   - freshness gate
   - Python engine route evidence
4. Only then implement a narrow runtime/views integration pass.

## 9. Unresolved Kept Open

- Exact runtime data adapter for engine evidence.
- Whether engine surface should remain a linked Python route only or get a React-side evidence summary mirror.
- Exact maturity display rules.
- Minimum return artifact fields.
- Whether extension panels should become collapsed drawers, separate tabs, or remain outside the first runtime pass.

