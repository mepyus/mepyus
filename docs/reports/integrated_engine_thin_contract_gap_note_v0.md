# Integrated Engine Thin Contract Gap Note v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

The current render contract is thin enough to protect the baseline and avoid false runtime precision, but it is not yet deep enough for selected-object rendering, denser trace display, or actual manifest value extraction.

## 1. sufficiently thin and locked

Locked now:

- panel identities and central panels
- panel-to-manifest read references
- display purpose per panel
- primary vs supporting read roles where current scaffolds expose them
- surface role separation:
  - user = operating / distribution / decision
  - VectorFL = mediation / validation / maturation
  - engine = processing / execution / return-draft
- support-layer subordination
- visual-token non-authority boundary

Why this is enough now:

- the current v1 candidate is a scaffold-level render contract, not a runtime data-binding contract
- each panel can be read without changing manifest shape or read mapping
- no selected-object or live state behavior is required to understand current baseline roles

## 2. thin but incomplete

Still incomplete:

1. Formal manifest key-to-render-field mapping is not defined.
2. Empty states are not defined in any scaffold panel.
3. Selected-object, side inspection, and deeper trace fields are only support ideas, not contract fields.

These are gaps to record, not failures of the current baseline.

## 3. minimum additional document before deeper data rendering

Before deeper rendering, add a separate read-only document that defines:

- per-panel allowed manifest keys or value groups
- empty-state wording per panel
- support-field limits for selected detail
- trace inclusion rules for connection records
- explicit "display state only" boundary if selected-object behavior is introduced

This should happen before any scaffold starts reading actual data values.

## 4. risky to implement now

Do not implement now:

- selected route or selected object behavior
- side inspection populated from object-specific fields
- denser connection-record timelines
- worker/process detail
- live manifest reads
- shared view model layer
- runtime truth, watcher, supervisor, bridge, or governance language

Reason:

- these require contracts that do not yet exist and could create false precision or authority drift.

## 5. why connection-record trace density is not core contract yet

Connection-record trace density remains outside core because:

- current scaffold read maps use representative sample connection records
- broader trace inclusion rules are not specified
- trace density could imply live event feed or route authority if rendered too strongly
- normal, follow-up, and drift loops have proven trace usefulness, but not yet a stable trace rendering contract

Current status:

- promotion gate needed before stable extension

## 6. why selected-object and side inspection stay hold / extension

Selected-object and side inspection remain outside core because:

- v1 candidate explicitly holds out selection sync and component props
- current scaffolds show support shells, not selected-object state
- object-class-specific secondary fields are not defined
- promoting inspection too early could make support layers look like core panels

Current status:

- selected-object support: extension later after display-state contract
- side inspection: extension later after object-class render-field rules
- deeper trace: promotion gate needed

## 7. boundary sentence

The current contract is intentionally thin: it fixes what each panel asks and which manifest it reads, while holding actual value extraction, selection behavior, and trace-density rules for later documentation.
