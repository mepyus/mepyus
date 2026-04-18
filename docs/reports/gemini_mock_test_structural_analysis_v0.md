# Gemini Mock Test Structural Analysis v0

Date: 2026-04-15

## 1. verdict

translate-with-selection

`gemini/mock_test` is not usable as-is for the current integrated-engine surface, but it is valuable as a visual/design reference that can be translated into the current working baseline.

## 2. overall summary

- The mock already recognizes the three-surface split: user / VectorFL / engine.
- Its strongest structural value is the clear tab shell, dense control-room layout, status badges, and left / center / right monitoring pattern.
- The user surface mock has useful goal/scope and routing material, but its center of gravity is team/role operation rather than the current `operating_flow_panel`.
- The VectorFL mock has useful line atlas / inspection language, but it is still closer to a line browser than a current `maturation_canvas_panel` reading a maturation object with origin, maturity, linked objects, and open edges.
- The engine mock is the strongest candidate for selective translation: ingest -> pipeline -> validation return is close to `work_input_panel`, `execution_state_panel`, and `result_return_panel`.
- The engine mock also contains risky material: asset inventory, supervisor queue, bridge rules, live manifest, script links, watcher recommendations, and "control room" language can drift into runtime binding or governance tooling if copied directly.
- The current baseline must remain higher than the mock: three central panels differ, packets stay separated, panels read only their question-specific fields, and runtime truth comes from manifests, not mock seed data.
- The mock should be treated as Gemini design evidence, not as canonical structure.

## 3. screen / panel mapping table

| source mock file or section | inferred surface | inferred panel type | closest current baseline panel name | status | note |
|---|---|---|---|---|---|
| `VectorFLIntegrationShell.tsx` / side navigation | mixed | decorative / navigation | none | usable | The three-surface tab shell is useful as navigation, but not a baseline panel. |
| `VectorFLIntegrationShell.tsx` / orientation band | mixed | operating | `operating_flow_panel` | needs translation | Shows broad flow from goal to return artifact, but compresses user / VectorFL / engine into one horizontal story. |
| `CommandHeaderPanel.tsx` | user | operating | `request_organization_panel` | usable | Goal / scope / material context maps well to user organization, but should not become the central operating flow by itself. |
| `MaterialContextPanel.tsx` | user | operating | `request_organization_panel` / `anchor_support_panel` | needs translation | Material context is useful, but should be attached to request organization or anchor support instead of becoming an independent new panel. |
| `TeamRoutingPanel.tsx` | user / mixed | operating / extension | `operating_flow_panel` | needs translation | Good routing visual, but team identity is an optional tool layer, not the body skeleton. |
| `RoleConfigurationPanel.tsx` | user / mixed | operating / extension | none | conflicting | Role config can overwhelm the baseline and make user surface look like a team-management console. |
| `ExecutionRoutePanel.tsx` | user / mixed | operating | `operating_flow_panel` | needs translation | Ticket lifecycle can help show slots, but it should be translated into packet / slot movement, not team work queues. |
| `OperationLogPanel.tsx` | user / mixed | operating | `operating_flow_panel` / `evidence_history_panel` | needs translation | Useful log style, but should show panel connection records or loop state rather than generic audit feed. |
| `FlowSummaryPanel.tsx` | vectorfl | maturation | `maturation_canvas_panel` | needs translation | The stats and summary fit maturation overview, but labels like "Interpretation Lab" and aggregate percentages need grounding in maturation object fields. |
| `VectorFLIntegrationShell.tsx` / `Line Atlas` | vectorfl | maturation | `maturation_canvas_panel` | needs translation | Good candidate for axis / line list, but baseline center should read maturation object body directly, not only line cards. |
| `jang_lines.json` line cards | vectorfl | maturation / anchor | `maturation_canvas_panel` / `anchor_context_panel` | usable with translation | `anchors`, `connectedTo`, `weakPoints`, `lineage`, and `refluxFromUser` are directly translatable to maturation body support fields. |
| `Line Inspection` card | vectorfl | maturation / anchor | `maturation_canvas_panel` / `anchor_context_panel` | usable with translation | Health, purpose, connected lines, and weak points are useful if separated into maturity, linked objects, and open edges. |
| `OperationConsolePanel.tsx` | vectorfl / mixed | decorative / extension | none | conflicting | It is explicitly an optional tool layer; do not absorb into core panels. |
| `vectorfl_engine_surface_mock.tsx` / engine header | engine | decorative / execution | `execution_state_panel` | needs translation | "Control room" framing is visually strong, but it should not imply engine governance authority. |
| `IngestEntryPanel` | engine | execution | `work_input_panel` | usable | Strong match for shaped input / source state. Keep the slot card pattern, remove script attachment claims unless backed by manifest. |
| `PipelineStatusPanel` | engine | execution | `execution_state_panel` | usable | Strong match for current execution slot and processing state. Step cards can translate to slot state display. |
| `ValidationReturnPanel` | engine / vectorfl | execution / operating | `result_return_panel` | usable with translation | Good return material structure, but validation judgment must remain VectorFL-side after engine return. |
| `WorkMemoryRecordPanel` | engine / vectorfl | operating / maturation | `execution_history_panel` / `evidence_history_panel` | needs translation | Decision / hold / next direction are useful, but can make engine look like final judgment if placed too centrally. |
| `SpaceHealthPanel.tsx` | mixed | anchor / decorative | `anchor_context_panel` | needs translation | Baseline alignment and risk visualization are useful; global maturity score can blur VectorFL maturation with engine health. |
| `AssetInventoryPanel.tsx` | engine / mixed | execution / decorative | `execution_history_panel` | needs translation | Good density and health indicators, but asset tree is not a primary engine central panel. |
| `AssetInspectorPanel.tsx` | engine / mixed | execution / anchor | `execution_history_panel` / `anchor_context_panel` | needs translation | Warnings, links, delta status, and event history are useful as support trace, not as core surface body. |
| `WatchpointRegistryPanel.tsx` | vectorfl / engine | anchor | `anchor_context_panel` | usable with translation | Good way to show drift / risk / next action if grounded in anchor objects and panel connection records. |
| `EventConsolePanel.tsx` | engine | execution | `execution_history_panel` | usable with translation | Strong event list pattern; should read real connection / execution records, not mock event seed as truth. |
| `SupervisorQueuePanel.tsx` | mixed | operating / extension | none | conflicting | Supervisor recommendations risk adding a standing assignment layer outside the current baseline. |
| `BridgePanel.tsx` | mixed | operating / extension | none | conflicting | Surface bridge rules are conceptually relevant but too broad for a baseline panel without explicit packet mapping. |
| `FilterBarPanel.tsx` | mixed | decorative / support | none | usable | Search/filter controls can be retained as local UI affordances, not structural panels. |
| `live_manifest.json` | mixed | support data | none | needs translation | Useful mock evidence, but references watcher/script/live truth language that conflicts with current no-binding analysis stage. |
| `WORK_REFLUX_LOG.md` | mixed | support note | none | needs translation | Contains useful learning about ingest -> pipeline -> validation return, but also pushes active console / maintenance language beyond current baseline. |
| `integration_report_20260411.md` | mixed | support note | none | usable as context | Useful to understand the sandbox's origin; not a structural source of truth. |
| `dist/`, `node_modules/`, `.DS_Store` | none | none | none | ignore | Build/vendor/system artifacts; do not translate. |

## 4. conflict list

1. User surface center is not clearly `operating_flow_panel`.
   - `CommandHeaderPanel` is goal/scope oriented and the rest is team routing / role configuration, so current loop state and packet movement are not visually central.

2. VectorFL center is line atlas, not clearly `maturation_canvas_panel`.
   - The mock shows lines and inspection cards, but not a maturation object body with origin refs, maturity stage, linked objects, and open edges as the primary center.

3. Engine surface can look like a governance / maintenance console.
   - Asset inventory, script links, supervisor queue, bridge panel, and watcher recommendations can make the engine appear to decide or manage the system rather than process shaped input and return material.

4. Flow, anchor, and axis are visually close together.
   - Line health, space health, bridge rules, and pipeline status share similar card language, so anchor criteria, maturation axes, and operating flow are not sharply separated.

5. Mock seed data uses runtime-truth language.
   - `live_manifest.json`, sync rate, watcher recommendations, and script attachment points imply live binding, which is outside the current baseline.

6. Team / role language can reintroduce optional tool-layer dominance.
   - Team routing and role configuration are useful only as operating extensions; if central, they obscure the three-surface body.

7. Return validation is partly shown inside the engine surface.
   - `ValidationReturnPanel` is useful, but final validation and user/reflux/reprocess choice must remain VectorFL-mediated, not engine-final.

8. Global "maturation level" can blur object classes.
   - Maturation should primarily attach to maturation objects / axis candidates, not a generic space health metric.

9. Bridge rules are too abstract for current packet separation.
   - They mention surface directions, but do not enforce request / return / reflux packet kinds.

10. Visual emphasis favors dashboard density over panel questions.
   - Baseline panels should answer operating questions, not expose whole manifests or generic feature lists.

## 5. salvageable elements

1. Three-surface tab shell.
   - Useful as navigation because it preserves user / VectorFL / engine separation.

2. Left navigation plus main work area.
   - Helps keep surface identity stable while changing central panels.

3. Engine slot card sequence.
   - `IngestEntryPanel -> PipelineStatusPanel -> ValidationReturnPanel` is close to work input / execution state / result return.

4. Status pills and small badges.
   - Good for packet status, current slot, return state, drift state, and maturity stage if tied to real manifest fields.

5. Line atlas selection pattern.
   - Can become a support pattern for selecting maturation objects or axis candidates, as long as the central body remains `maturation_canvas_panel`.

6. Inspection side panel style.
   - Useful for linked objects, open edges, anchor refs, evidence density, and validation points.

7. Watchpoint / warning visual language.
   - Good candidate for anchor drift, reprocess holds, and unresolved open edges.

8. Event console list.
   - Can translate into `execution_history_panel` or `evidence_history_panel` if sourced from panel connection records.

9. Dense but legible card spacing.
   - Useful for operational surfaces where multiple small state objects must remain visible.

10. Explicit mock disclaimers.
   - The existing "mock is not runtime truth" language matches current constraints and should be retained as boundary text during analysis-only stages.

## 6. elements to discard or hold out

1. Runtime watcher / live sync recommendations.
   - They invite file watch and runtime binding, which are explicitly out of scope for current baseline translation.

2. Script attachment points as primary UI claims.
   - `actualAttachmentPoint` fields should not appear unless backed by current manifests and freshness checks.

3. Supervisor queue as a core panel.
   - It adds a standing assignment layer that v1 candidate holds out.

4. Role configuration as central user surface.
   - It makes the user surface look like team administration instead of operating / distribution / decision.

5. Bridge panel as a core contract.
   - It is too broad and may bypass packet-kind separation unless rewritten as panel connection evidence.

6. Global maturity / health scores as primary truth.
   - These are visually useful but structurally weak unless grounded in maturation object fields or anchor records.

7. Control-room language when it implies authority.
   - Engine surface can display processing state, but should not become the final judgment surface.

8. Generic asset inventory as the engine center.
   - Asset inventory belongs in secondary monitoring, not the `execution_state_panel` center.

9. Decorative gradients / large rounded cards as identity.
   - Visual style should not become the structure; panels must remain defined by their question and manifest fields.

10. Mock line affinity as direct routing.
   - `lineAffinity` is useful as a hint, not as automatic panel routing or runtime binding.

## 7. next reflection order

1. Start with the engine surface visual translation.
   - Use only the slot-card rhythm from `IngestEntryPanel`, `PipelineStatusPanel`, and `ValidationReturnPanel`.

2. Translate engine visuals into existing baseline panels.
   - Map them to `work_input_panel`, `execution_state_panel`, `result_return_panel`, and `execution_history_panel` without changing scaffold read mappings first.

3. Translate VectorFL line atlas into maturation language.
   - Keep selection / inspection pattern, but rename the structural reading around `maturation_canvas_panel`, `anchor_context_panel`, and `validation_mediation_panel`.

4. Reduce user surface mock to request organization and operating flow.
   - Keep goal/scope/material context and discard team/role dominance until operating flow is clear.

5. Only after the three central panels remain distinct, borrow shared visual tokens.
   - Status pills, risk badges, compact cards, and side inspection panels can be applied selectively.

## 8. final answer

Do not reflect this mock directly now. Structural translation must come first.

If reflection becomes appropriate, start with the engine surface because its ingest -> pipeline -> validation return sequence is closest to the current baseline and has the lowest conceptual translation cost.
