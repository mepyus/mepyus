# provenance_dedupe_compaction_policy_v1

## 1. Purpose
This policy defines how provenance duplicate noise should be reviewed and compacted without destroying raw trace evidence.

## 2. Core Lock
- raw provenance stays preserved by default
- compaction is a hygiene layer, not evidence deletion
- preview comes before apply
- bounded scope beats broad rewrite

## 3. Duplicate Pattern Classes
- `exact_duplicate`
  - all stored fields equal
  - safe candidate
- `same_idempotency_context_repeated_append`
  - same source / same target / same relationship repeated across re-ingest runs for stable registry relations
  - safe candidate
- `same_receipt_seed_lineage_duplicate`
  - same receipt-seed lineage repeated toward the same logical target
  - safe candidate
- `same_document_reingest_accumulation`
  - one document accumulated many provenance rows across runs
  - manual review by default
- `same_source_same_target_different_run_duplicate`
  - same source / target / relation repeated but operation history may matter
  - manual review by default
- `structurally_similar_but_not_safe_to_merge`
  - fields are similar but semantic/audit meaning may differ
  - not compacted

## 4. Safe Candidate Conditions
- exact field equality
- same source identity + same target identity + same relation identity for stable registry/origin-map relations
- same idempotency context repeated append where later rows do not add new meaning

## 5. Default No-Compaction Cases
- generated outputs whose targets differ by run-specific filename
- repeated operation history that may matter in audit
- recovery-related rows
- rows differing in relation class, lineage phase, or target identity

## 6. Preview-First Rule
- review script must run before any apply helper
- preview outputs must include:
  - total row count
  - candidate groups
  - safe vs manual-review counts
  - representative examples
  - raw provenance path

## 7. Apply Guardrails
- no silent destruction
- snapshot/backup first
- compaction summary required
- raw provenance source file is not rewritten in this policy version
- bounded compacted derivative outputs are preferred

## 8. Surface Rule
- latest compacted surface is for readability
- raw provenance index remains the audit source
- compacted surface must point back to raw path and preview manifest

## 9. Current V1 Decision
- V1 allows review, preview, and bounded derivative compaction outputs
- V1 does not authorize destructive in-place rewrite of `runtime/manifests/provenance_link_index_v1.json`
