# Integrated Engine Lens / Slot Compatibility Matrix v0

## Status

PASS_WITH_NOTE

This matrix connects working lenses to C0-C6 provisional camera slots.
It does not create a final lens registry or promoted camera.

## Lens Details

| lens | purpose | strong/likely slots | weak fit slots | invalid target shapes | typical object types | expected return | false-positive risk | confusion | hold condition | verification question |
|---|---|---|---|---|---|---|---|---|---|---|
| scope-reading | Lock object range. | C0 | C4-C6 | empty shell, path-only | report intro, artifact header, intake note | scope anchor | topic hint treated as content | processing-tension | only source pointer exists | What is this object opening and not opening? |
| processing-tension | Find driving pressure. | C1 | C5-C6 | metadata-only, index-only | transcript, correction report, handoff | tension statement | topic called tension | scope-reading | no mismatch or pressure | What makes this object move? |
| preparation-structure | Read setup before mechanism. | C2 | C6 | pure summary | prompt packet, source bundle, model explanation | preparation state | invented setup | output-result | setup implicit only | What is prepared before action? |
| selection-mechanism | Read selection/routing/filtering. | C3 | C0, C6 | descriptive no-action text | attention explanation, validation grammar, screen rule | mechanism note | mechanism forcing | correction-reading | no selection rule visible | What decides use/route/foregrounding? |
| output-result | Read produced candidate/result. | C4 | C1-C2 | no return/result | probe result, return packet, generation explanation | result state | candidate read as canonical | selection-mechanism | result absent | What is produced, and is it final? |
| support-placement | Attach support to core. | C5, C6 | C0-C2 | support-only list | limitation note, guard section | support placement | support becomes center | rollback-detection | no core segment | Which core does this support protect? |
| rollback-detection | Detect drift/forcing. | C6, all as check | none as primary content | no comparison context | probe result, review note | rollback signal table | used as universal lens | support-placement | no gate context | What breaks if forced? |
| correction-reading | Read correction to prior misread. | C1, C5, C6 | C2-C3 | neutral transcript | direction reset, correction note | misread/correction/must-not | correction becomes new theory | screen-projection | no correction frame | What did this correct? |
| grammar-classification | Classify route/authority/state/boundary. | C1-C4, C6 | C5 | raw domain lecture | handoff report, grammar note | grammar categories | glossary drift | final glossary | no authority/route relation | Which grammar is operating? |
| screen-projection | Read 3-surface visibility. | C3-C4, C6 | C1-C2 | non-UI domain text | scaffold analysis, screen report | surface projection | show all info everywhere | correction-reading | no surface relation | What should each surface see? |

## Matrix

Legend: strong / usable / weak / avoid

| lens \ slot | C0 Scope | C1 Tension | C2 Prep | C3 Selection | C4 Output | C5 Support | C6 Guard |
|---|---|---|---|---|---|---|---|
| scope-reading | strong | usable | weak | avoid | weak | weak | usable |
| processing-tension | usable | strong | usable | weak | weak | weak | usable |
| preparation-structure | weak | usable | strong | usable | weak | weak | avoid |
| selection-mechanism | weak | usable | usable | strong | usable | weak | weak |
| output-result | weak | weak | weak | usable | strong | weak | usable |
| support-placement | weak | weak | avoid | weak | usable | strong | strong |
| rollback-detection | usable | usable | usable | usable | usable | usable | strong |
| correction-reading | usable | strong | usable | usable | usable | strong | strong |
| grammar-classification | usable | strong | usable | strong | strong | usable | strong |
| screen-projection | usable | usable | weak | strong | strong | usable | strong |

## Row Reasons

- `scope-reading`: starts at C0; should not fill process slots by itself.
- `processing-tension`: strongest at C1; can support C0/C2 but cannot create mechanism.
- `preparation-structure`: strongest at C2; must not invent downstream result.
- `selection-mechanism`: strongest at C3; risky if the target only describes correction or support.
- `output-result`: strongest at C4; must keep candidate/canonical distinction.
- `support-placement`: belongs to C5/C6; should not become core content.
- `rollback-detection`: can check all slots but should not become the primary reading lens.
- `correction-reading`: works across C1/C5/C6 for misread/correction/guard reports.
- `grammar-classification`: works when route/authority/state/boundary are present.
- `screen-projection`: strongest when surface-specific visibility is the object.

## Required Verification

- Lens broader than slot? controlled by matrix and row reasons.
- `selection-mechanism` mixed with `correction-reading`? watch C3; mark partial if correction has no mechanism.
- `rollback-detection` as universal lens? allowed as check, not primary content.

## Pointers

- Lens draft: `docs/reports/integrated_engine_lens_structure_draft_v0.md`
- Camera procedure: `docs/reports/integrated_engine_provisional_camera_usage_procedure_v0.md`
