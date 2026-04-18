# Integrated Engine Engine Surface Visual Translation Brief v0

Date: 2026-04-15

## 0. verdict

PASS

The selected `gemini/mock_test` engine-surface visual grammar can be translated onto the current integrated-engine baseline if it remains a visual layer only.

No scaffold read mapping, runtime binding, live manifest truth, watcher language, supervisor queue, bridge panel, script attachment claim, or control-room authority should be imported.

## 1. purpose

This brief translates only selected visual grammar from `gemini/mock_test/vectorfl_engine_surface_mock.tsx` into the current engine-surface baseline.

Current baseline stays fixed:

- engine surface = processing / execution / return-draft surface
- center panel = `execution_state_panel`
- current scaffold read mapping remains unchanged
- panels remain `work_input_panel`, `execution_state_panel`, `result_return_panel`, and `execution_history_panel`
- engine output is return material, not final judgment

## 2. selected mock grammar

Allowed visual sources:

- `IngestEntryPanel` slot-card rhythm
- `PipelineStatusPanel` step/status card rhythm
- `ValidationReturnPanel` return-material card rhythm
- compact status badges / small pills
- side inspection visual token, only as support layer
- event list style, only for execution history

Held out:

- asset inventory as a center panel
- supervisor queue
- bridge panel
- watcher recommendation
- script attachment point as UI truth
- live manifest as runtime truth
- control room / governance / maintenance-authority language

## 3. mock element -> baseline panel mapping

| mock source | visual grammar to keep | baseline panel | translation rule | do not carry |
|---|---|---|---|---|
| `IngestEntryPanel` | large slot card, header icon block, status pill, compact stat cells | `work_input_panel` | Treat as shaped input / request intake card. Show packet purpose, source surface, target surface, requested action, validation points. | `source_path` as verified truth, `actualAttachmentPoint`, script references, external ingest authority. |
| `PipelineStatusPanel` | central step/status card rhythm, active step emphasis, done / processing / hold dots | `execution_state_panel` | Use as central execution slot display. Show current slot, current surface, active packet ids, loop status, next action. | Pipeline engine identity, automatic step execution, governance check as engine authority. |
| `ValidationReturnPanel` | return material columns, accepted / hold / reasoning buckets, status pill | `result_return_panel` | Use as return-draft material layout. Show return summary, produced artifacts, open questions, suggested next route. | Final validation language, product completion, engine-side final decision. |
| `EventConsolePanel` | compact chronological event rows with type badges | `execution_history_panel` | Use only for return route trace and panel connection records. | Generic live event feed, watcher events, mock seed history as truth. |
| `StatusPill` | small colored status capsule | all engine panels | Use for `packet_status`, `current_slot`, return status, follow-up / reprocess state. | Animated authority signal, system-load signal, live health claim. |
| `SlotAttachmentNote` | small monospace support note area | support layer only | If used, rewrite as manifest read note or source record note. | `Mock:` / `Actual:` attachment claims, scripts, binding points. |
| `WorkMemoryRecordPanel` | compact hold / next direction card style | support layer under `execution_history_panel` | Only as trace-memory support if sourced from panel connection / loop state fields. | Engine final judgment, decision authority, supervisor language. |
| `AssetInventoryPanel` / `AssetInspectorPanel` | dense list / side inspection styling | support layer only | Keep as visual reference for future side inspection of fields, not as current engine body. | Asset tree as central panel, script lineage, baseline delta truth. |

## 4. panel-by-panel visual translation

### `work_input_panel`

Use:

- one primary slot card inspired by `IngestEntryPanel`
- compact header with panel name, packet kind, source / target surfaces
- small status pill at top right
- 3-4 compact stat cells for `purpose`, `directionality`, `requested_or_next_action`, and `validation_points`

Avoid:

- source-path verification
- script attachment point
- ingest pipeline authority
- live manifest freshness claims

Reading note:

- This panel receives a shaped request packet. It should never look like raw user intent or direct user-to-engine bypass.

### `execution_state_panel`

Use:

- central step/status layout inspired by `PipelineStatusPanel`
- explicit active slot card with `current_slot`, `current_surface`, `current_focus_object`, and `loop_status`
- small step cards only as visual markers for allowed movement, not as runtime automation
- active / hold / returned / reprocess color states through restrained badges

Avoid:

- naming it "control room"
- system load metrics
- automatic pipeline claims
- governance authority language
- file watcher or execution daemon hints

Reading note:

- This is the engine surface center. It should show where processing is, not decide what the result means.

### `result_return_panel`

Use:

- return material card rhythm from `ValidationReturnPanel`
- columns for `return_summary`, `produced_artifacts`, `open_questions`, and `suggested_next_route`
- visible reminder that return is not completion
- route pill for `vectorfl_validation`, `user_decision_or_vectorfl_recheck`, or `reprocess`

Avoid:

- final approval styling
- accepted / rejected language unless it belongs to a return packet field
- making the engine appear to validate meaning
- product-completion copy

Reading note:

- The panel drafts return material. VectorFL validation and user decision remain outside the engine surface.

### `execution_history_panel`

Use:

- compact event-list style from `EventConsolePanel`
- rows for panel connection records and return route traces
- small type badges for `created`, `returned`, `held`, `reprocess`, or `refluxed`
- side inspection style only as support detail for selected history row

Avoid:

- live event console framing
- watcher event feed
- supervisor recommendation queue
- bridge rules as broad policy

Reading note:

- This panel should make route trace visible. It should not become an operational command console.

## 5. allowed / forbidden by panel

| baseline panel | allowed | forbidden |
|---|---|---|
| `work_input_panel` | slot card, status pill, purpose/action cells, validation-point chips | script attachment, source verification, watcher hint, raw intent framing |
| `execution_state_panel` | central active slot, step rhythm, hold/reprocess badges, compact current-loop fields | control room label, system authority, system load, automatic pipeline truth |
| `result_return_panel` | return summary card, artifact/open-question columns, suggested route pill | final approval, product completion, engine-side validation verdict |
| `execution_history_panel` | event rows, panel connection trace, side detail support | supervisor queue, bridge panel, live watcher feed, generic asset inventory |

## 6. pseudo layout proposal

This is a layout note only. It is not an implementation instruction.

```text
engine_surface

top band:
  small surface label: Engine surface
  one-line role: processing / execution / return-draft
  boundary note: return material is not final validation

main layout:
  left column:
    work_input_panel
      slot card
      packet status pill
      source / target / purpose / requested action cells

  center column:
    execution_state_panel
      largest card, central
      current slot badge
      active packet ids
      loop status
      compact step rhythm below as visual slot markers only

  right column:
    result_return_panel
      return material card
      summary / artifacts / open questions / suggested route
    execution_history_panel
      compact event list
      selected row detail if needed
```

Support layer:

- A side inspection panel may appear only as a support detail for selected packet, return, or history row.
- It must not become a new baseline panel.
- It should show fields already read by the current panel, not introduce live asset inventory or script lineage.

## 7. visual token guidance

Use:

- dark low-contrast surface
- compact cards
- small uppercase labels
- status pills
- thin route separators
- subdued icon blocks
- clear active / hold / return / reprocess color distinctions

Avoid:

- oversized authority headers
- "control room", "governance", "maintenance", "supervisor" product language
- global health dashboards
- decorative visuals that do not answer the panel question
- any copy implying live binding or automatic execution

## 8. preservation note

This brief does not change:

- `runtime/views/engine_surface_scaffold_v0.tsx`
- panel names
- panel read mapping
- manifest paths
- runtime binding
- file watching
- execution behavior

It only defines how selected engine-surface mock visual grammar may be translated later while preserving the current working baseline.

