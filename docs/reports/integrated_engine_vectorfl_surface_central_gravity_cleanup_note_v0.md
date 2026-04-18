# Integrated Engine VectorFL Surface Central Gravity Cleanup Note v0

## 1. Verdict

PASS_WITH_NOTE

The VectorFL surface was reorganized so the current work packet / CLI mediation lane reads as the central operating body, while Line Atlas and Inspection read as support evidence.

## 2. Why This Cleanup Was Needed

The previous VectorFL surface mixed three competing centers:

- Line Atlas as the largest left-side visual object
- CLI Conversation Layer as the actual operating tool
- Current Work Packet Formation as the intended mediation layer, but nested mid-panel

This made the page feel like a mix of mock line browser, CLI input form, and result cards. The cleanup makes the central question clearer:

```text
What packet is VectorFL forming, and what happens when that packet is sent?
```

## 3. What Changed

Changed files:

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
- `app/ui/integrated_engine/CliHostControlPanel.tsx`
- `app/ui/integrated_engine/FlowSummaryPanel.tsx`

Changes:

- VectorFL main grid now places `CliHostControlPanel` in the wide central column.
- `VectorFLValidationQueuePanel` stays below the CLI/work-packet lane as return-to-reread support.
- `Line Atlas` moved to a narrower right support column and is labeled `Evidence Line Atlas`.
- selected line `Inspection` remains in the right support column.
- `FlowSummaryPanel` title changed from `VectorFL Surface: Line Atlas` to `VectorFL Surface: Work Packet Mediation`.
- `Send Codex Turn`, `Refresh`, and `Continue latest` moved directly after `current work packet formation`.

## 4. What Did Not Change

- no new surface
- no new API
- no Gemini adapter
- no async/background support
- no session history expansion
- no deposit ingestion
- no automatic packet generation
- no deletion of old mock-derived support panels

## 5. Current Panel Reading After Cleanup

| area | current role |
| --- | --- |
| `FlowSummaryPanel` | VectorFL orientation / work packet mediation heading |
| `CliHostControlPanel` | central VectorFL operating lane |
| `current work packet formation` | packet mediation body before send |
| send controls | packet confirmation action |
| `VectorFLValidationQueuePanel` | reread / validation return queue |
| `Evidence Line Atlas` | support selector, not central body |
| `Inspection` | selected line support detail |
| conversation turns / deposit queue | after-send trace and candidate support |

## 6. Watchpoints

1. The screen may still carry too much English/internal language.
2. The packet layer is visible, but automatic source/lock bundle formation is still not implemented.
3. Line Atlas is support now, but it still has visual weight and should stay subordinate.
4. Send flow is closer to packet confirmation, but actual browser feeling still needs user validation.

## 7. Next Smallest Validation Step

Open the VectorFL surface and check whether the page now reads in this order:

```text
work packet mediation
-> packet confirmation / send
-> return trace and reread/deposit support
-> line evidence support
```

If it still feels like a CLI input form or line browser first, the next patch should further reduce support column weight or collapse secondary queues. It should not add new features.
