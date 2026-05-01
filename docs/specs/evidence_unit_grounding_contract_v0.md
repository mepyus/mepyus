# Evidence Unit Grounding Contract v0

## Status

- phase: `phase1_6_evidence_grounding_hardening`
- authority: `working_spec`
- compatibility: additive to Phase 1/1.5 evidence units

## Execution

Grounded evidence unit minimum fields:

- `source_ref`: source path or artifact ref.
- `pointer`: stable pointer, usually path plus line range or section hint.
- `excerpt_window`: bounded local text used as evidence.
- `excerpt_mode`: how the excerpt was selected.
- `why_it_matters`: relation between excerpt and interpreted goal.
- `relation_type`: evidence relation.
- `local_confidence`: confidence in this local evidence unit.
- `cross_support_refs`: other evidence refs that support this evidence.
- `contradiction_note`: local contradiction or tension.
- `grounding_status`: depth of grounding.

Allowed `grounding_status` values:

- `pointer_only`: source is identified but no useful local text was extracted.
- `weak_grounded`: excerpt exists but only weakly supports the reason.
- `direct_grounded`: excerpt directly supports the reason.
- `cross_supported`: direct or weak evidence is reinforced by other evidence units.

Allowed `excerpt_mode` values:

- `pointer_only`
- `line_window`
- `paragraph_block`
- `heading_plus_block`
- `bullet_cluster`

Existing `relation_type` values remain:

- `direct_support`
- `contextual_support`
- `tension`
- `contrast`
- `weak_candidate`

## Interpretation

`source_ref` alone is not enough because it only says where Codex looked. It does not show what Codex read or why that local text was treated as evidence. `excerpt_window` makes the evidence inspectable, while `why_it_matters` prevents raw quotes from becoming unexplained decoration.

`confidence` and `grounding_status` are separated because they answer different questions. Grounding status says how much local source material is attached. Confidence says how strongly that material supports the current use. A direct excerpt from a low-authority report can be direct-grounded but still only medium confidence for a baseline claim.

`contradiction_note` matters before merge because merge is risky when the evidence unit itself contains tension. A contradiction should travel into merge/diff/hold rather than being hidden inside exploration.

## Validation

- Evidence is readable by a human without opening every file first.
- Schema is additive, not a replacement for v0.
- Pointer-only fallback remains valid.
- Cross-support can be represented without a graph engine.

## Stage Closeout

- Verdict: `PASS`
- Files created: this contract plus v1 runtime template and examples.
- Evidence unit changes: pointer fields are retained; excerpt/depth/confidence fields are added.
- Compatibility note with phase1.5: v0 consumers can still read `source_ref`, `excerpt_or_pointer`, `why_it_matters`, `relation_type`, and `confidence`.
- Entry condition for next stage: excerpt extraction rules can fill the new fields.
