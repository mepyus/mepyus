# provenance_compaction_guardrails_v1

## 1. Guardrail Goal
This report locks the operational guardrails for provenance hygiene work so that readability improves without evidence loss.

## 2. Required Guardrails
- preview before apply
- snapshot before bounded apply
- raw provenance preserved
- compacted outputs clearly marked as derivative
- representative examples included in latest compacted surface

## 3. Forbidden Moves
- silent destructive rewrite
- broad merge of rows that only look similar
- collapsing run-specific generated outputs into one row without review
- removing recovery-relevant history

## 4. V1 Allowed Moves
- read-only review of duplicate candidates
- compacted latest surface generation
- bounded derivative compaction artifact generation
- snapshot creation before derivative apply

## 5. Review Labels
- `safe`
  - stable repeated relations with no new meaning added
- `manual_review`
  - likely compactable for readability, but audit meaning may remain
- `unsafe`
  - not compacted in V1

## 6. Expected Outputs
- preview manifest
- compacted latest markdown surface
- apply summary
- snapshot path

## 7. One-Line Guardrail
Compaction may simplify reading, but the raw provenance index remains the source of truth.
