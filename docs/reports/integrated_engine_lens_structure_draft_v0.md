# Integrated Engine Lens Structure Draft v0

## Status

PASS_WITH_NOTE

This is a working draft for operational lenses.
It is not a glossary, UI copy, or final lens registry.

## Purpose

Lenses decide what an existing camera frame reads from an object.
The same asset can be read differently depending on lens.
The same user wording can point to different objects under different lenses.

## Lens Draft Table

| lens id | purpose | typical object type | expected return | invalid target shape | verification question | common confusion | hold / use rule |
|---|---|---|---|---|---|---|---|
| `scope-reading` | Lock what the object is about before extracting details. | intake note, report intro, artifact header, sectioned note. | scope anchor, in-scope/out-of-scope note. | empty shell, path-only file. | Can I say what this object is and what it is not opening? | Mistaking topic hint for full content. | Use for all targets; hold if only source pointer exists. |
| `processing-tension` | Find the problem shift or pressure driving the object. | lecture transcript, correction report, handoff report. | tension statement and driver. | metadata-only file, index-only file. | What problem or mismatch makes this object move? | Calling a topic a tension. | Use when body text has conflict/shift; hold for intake-only. |
| `preparation-structure` | Identify what must be prepared before the mechanism acts. | source bundle, prompt packet, model explanation, handoff artifact. | input/state/evidence preparation note. | pure summary without body. | What is being prepared, bundled, shifted, or initialized? | Jumping directly from scope to output. | Use when setup state is visible; mark partial if inferred. |
| `selection-mechanism` | Read how information is selected, routed, filtered, weighed, or foregrounded. | attention explanation, UI composition rule, validation grammar. | mechanism or mediation description. | descriptive text with no action relation. | What decides what is used, hidden, routed, or weighted? | Keeping transformer-specific attention wording for non-transformer targets. | Use if a selection/foregrounding rule exists; hold if only result is described. |
| `output-result` | Identify what the process returns as representation, output, candidate, or projection. | line set, probe result, return packet, generation explanation. | output/result state with authority label. | object with no result or return. | What is produced, and is it final or candidate? | Treating candidate output as canonical. | Use when return/result exists; keep candidate status visible. |
| `support-placement` | Attach support, contrast, limitation, guard, or decision aid to a core segment. | report guard section, limitation note, generation strategy note. | support-to-core placement note. | support-only list with no core body. | Which core segment does this support protect or clarify? | Letting support become the main object. | Use only attached to a core segment; rollback if support floats. |
| `rollback-detection` | Detect drift, mismatch, forcing, and invalid promotion. | probe result, review note, target-shape check. | rollback signal table and destination. | asset with no comparison or gate context. | What would break if we forced the frame here? | Calling failure a bad asset instead of a shape mismatch. | Use after every probe/review; hold if no target-shape context. |
| `correction-reading` | Read a document as a correction to a prior misread. | direction reset note, body/camera/lens correction, closeout. | what was wrong, corrected rule, must-not. | simple content transcript without correction frame. | What misread does this correct? | Turning correction into new theory or new UI feature. | Use for correction reports; hold for neutral source material. |
| `grammar-classification` | Classify route/authority/state/boundary grammar in an artifact. | handoff artifact, grammar report, collaboration note. | grammar classification by category. | raw transcript with no handoff/authority relation. | Which grammar is operating here: route, authority, hold, validation, support, bridge? | Making grammar into final glossary. | Use for handoff/internal language docs; hold for pure domain lecture. |
| `screen-projection` | Read how one work object should appear differently across User/VectorFL/Engine surfaces. | UI correction note, screen report, scaffold analysis. | 3-surface projection rule. | content-only lecture without UI/surface relation. | What should User see, VectorFL see, and Engine see differently? | Showing all information everywhere. | Use for screen/process docs; hold for non-UI domain text. |

## Lens Composition Rule

1. Choose object scope first.
2. Choose one primary lens.
3. Add a secondary lens only if it answers a distinct verification question.
4. Do not let a lens create a new object.
5. Do not let lens output become canonical by default.

## Common Lens Confusions

| confusion | correction |
|---|---|
| scope-reading vs processing-tension | Scope says what the object is; tension says why it moves. |
| selection-mechanism vs output-result | Mechanism explains how choice happens; result explains what comes out. |
| support-placement vs rollback-detection | Support clarifies a core segment; rollback detects whether the frame should stop. |
| correction-reading vs screen-projection | Correction says what was misread; projection says how each surface should show the corrected object. |
| grammar-classification vs final glossary | Grammar classifies operating relations; glossary would fix terms, which is not open here. |

## Hold Rule

Hold a lens when:

- the target is metadata-only
- the target lacks content-bearing body
- applying the lens requires inventing missing stages
- the lens would open axis promotion, glossary, or canonical ingestion

## Use Rule

Use a lens when:

- object scope is clear
- target shape supports the lens question
- evidence can be cited
- output remains candidate / review / hold unless explicitly promoted by a separate process

## Pointers

- Provisional camera frame: `docs/reports/integrated_engine_provisional_camera_big_frame_v0.md`
- Recovery checklist: `docs/reports/integrated_engine_process_recovery_checklist_v0.md`
- Verification and rollback: `docs/reports/integrated_engine_verification_and_rollback_discipline_v0.md`
