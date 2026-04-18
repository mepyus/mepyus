# Integrated Engine Panel Wording Confusion Candidates v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

The following are wording confusion candidates only. They do not require scaffold restructuring, manifest changes, read-map changes, selected-object behavior, trace UI, or extension promotion.

No wording patch is applied in this document.

## 1. user surface

| candidate | current wording or current reading | why it may confuse use-time reading | wording-only candidate direction | why this is not a structure issue |
|---|---|---|---|---|
| follow-up request origin | `request_organization_panel`: "Shapes the incoming request..." | In scenario 2, the request is created by user organization but originates from a VectorFL maturation signal. "Incoming" can sound user-origin only. | Say "Shapes request material, including user-origin requests and organized follow-up signals." | Lexicon/protocol already allow VectorFL maturation signal -> user organization -> engine follow-up. |
| support inspection | "Side detail can expose a selected route, open question, or connection note..." | "selected route" can sound like selected-object behavior, which is held out. | Say "Side detail may later describe route or open-question support when separately contracted." | The side support shell is already subordinate; only the wording reaches ahead. |
| return decision | `return_decision_panel`: "Return material and next route" | Could be read as the final user decision panel if the support note is skipped. | Emphasize "decision input / recheck route, not completion." | The panel already reads return packet and keeps recheck/reflux open. |

## 2. VectorFL surface

| candidate | current wording or current reading | why it may confuse use-time reading | wording-only candidate direction | why this is not a structure issue |
|---|---|---|---|---|
| evidence history density | `evidence_history_panel`: "selected connection records and lineage-style rows" | Can sound like a denser trace UI or selected-row inspection. | Say "current primary connection record, with broader traces checked manually." | Interface note already keeps first primary record in read map and broader records as manual supporting traces. |
| support selection | "Line / axis selector stays smaller than the canvas" | "selector" can sound like line atlas or selected-object model. | Say "Line / axis support pointers stay smaller than the canvas." | The center remains `maturation_canvas_panel`; no selection behavior exists. |
| anchor drift action | `anchor_context_panel`: "Baseline criteria before mediation" | In scenario 3, anchor context actively detects drift; the wording can understate its braking role. | Say "Baseline criteria before mediation; may explain drift holds through connection records." | Anchor remains a criteria panel; drift route is already recorded through panel connection, not new structure. |

## 3. engine surface

| candidate | current wording or current reading | why it may confuse use-time reading | wording-only candidate direction | why this is not a structure issue |
|---|---|---|---|---|
| work input | `work_input_panel`: "What request is ready for engine processing?" | Follow-up and reprocess scenarios may involve shaped follow-up or reprocess packets, not only the first request. | Say "What shaped request or reprocess packet is ready for engine processing?" | Engine already reads shaped input; lexicon permits VectorFL reprocess request to target engine. |
| slot rhythm | "Visual slot rhythm" with input / processing / return / trace | Could be mistaken for an actual state machine if copied without the disclaimer. | Keep or strengthen "visual-only slot rhythm." | Round 6 already forbids runtime status and trace UI. |
| result return | `result_return_panel`: "What return material is being prepared?" | Could sound like engine owns return meaning if read without support note. | Say "What return material is being drafted for validation or follow-up route?" | Return validation principle already keeps meaning validation outside engine. |

## 4. boundary

These candidates should only become wording patches if they recur during further manual use.

They should not be treated as:

- structure drift
- evidence for new panels
- read-map change request
- selected-object requirement
- trace UI requirement
- extension promotion
