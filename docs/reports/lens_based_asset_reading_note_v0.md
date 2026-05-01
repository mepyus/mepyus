# Lens-Based Asset Reading Note v0

## 1. Why this note exists

This note records the broader reading method that emerged from the ASSETS.md layer/lens mismatch case.

The ASSETS.md proposal showed that a design can be coherent and useful in one layer while risky in another.

The goal is not to decide simply whether a proposed asset is good or bad.
The goal is to identify the layer/lens on which the asset becomes meaningful.

## 2. Core discovery

Asset value is not absolute.

Asset value changes depending on the lens used to read it.

A proposed structure may be:

- risky under the user's living-space philosophy lens
- useful under a quality / quarantine lens
- attractive under an automation / orchestration lens
- clear under an ontology / schema lens
- useful as an internal product/backstage model

Therefore the space should avoid simple fit/no-fit judgment.

## 3. Why single-lens judgment is insufficient

If the space uses only the user's core philosophy lens, it may reject useful external value too quickly.

If the space uses only governance, automation, or ontology lenses, it may over-structure living material too quickly.

The space should compare lenses before adoption.

## 4. Lens list v0

This list is provisional and non-exhaustive.

- Space Philosophy Lens
- Usability Lens
- Token / Weight Lens
- Quality / Quarantine Lens
- Worker Operation Lens
- Enterprise Knowledge Management Lens
- Automation / Orchestration Lens
- Ontology / Schema Lens
- Product / Interface Lens
- Research / Lab Lens

## 5. Reading result positions

After multi-lens reading, a material may be positioned as:

- core-fit asset
- conditional asset
- comparison asset
- quarantine asset
- lens asset
- future option asset
- archive

These positions are not baseline states.
They are placement candidates after reading.

## 6. Reading card candidate

Use this compact card when a proposed structure or external material needs multi-lens reading:

```text
asset_id:
asset_summary:

primary_space_lens_read:
  fit:
  risk:
  note:

other_lens_reads:
  - lens:
    value_seen:
    risk_seen:
    possible_use:

conflict_with_space_principle:
  yes/no/partial
  why:

recommended_position:
  core_fit / conditional / comparison / quarantine / lens / future_option / archive

use_when:
do_not_use_as:
recheck_condition:
```

## 7. ASSETS.md case as example

The ASSETS.md proposal was not simply wrong.

It was useful under governance, quality, ontology, automation, and product-backstage lenses.

However, it was risky under the user's living-space philosophy lens because it could turn living space maturation into asset management, registry, schema, or automation thinking.

Therefore the proposal should not be used as an ASSETS.md creation mandate.

It should be retained as:

- comparison material
- future option material
- over-structuring warning
- layer/lens mismatch case

## 8. Relation to layer-aware space reading

Layer-aware space reading asks:

- What layer am I answering from?
- What layer might the user be reading from?
- Which line, axis, connection, flow, or context is missing?
- Which lens makes this proposal look valuable?
- Which lens makes it risky?
- Should this be adopted, lowered, quarantined, compared, archived, or held?

Lens-based asset reading is one concrete application of layer-aware space reading.

## 9. Do not

- Do not turn this into fixed ontology.
- Do not use this as schema.
- Do not make it an automatic classifier.
- Do not make Gemini the final lens reader.
- Do not collapse all lenses into the user's philosophy lens.
- Do not adopt another lens's value directly into the core space.
- Do not treat reading result positions as locked states.
- Do not use this as an ASSETS.md creation mandate.

## 10. Status

```yaml
state: seed / candidate
not:
  - baseline
  - protocol lock
  - automation
  - schema
  - asset registry
```
