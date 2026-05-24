# Codex Requirements Recovery Return

classification: component_proposal_requirements_ready

recovered_requirements:
  - permission_inheritance_during_combined_model_transport:
      status: requirement_candidate_recovered
      requirement: Combined transport packets derived from multiple source components must carry inherited permission metadata from all contributing sources.
      required_evidence_fields:
        - permissions_provenance
        - source_permission_sets
        - active_execution_context_check
      acceptance_checks:
        - Reject transport when inherited permission metadata is absent.
        - Reject transport when inherited permission metadata fails execution-context verification.
        - Verify aggregation from at least two distinct source permission sets.
  - raw_audit_trigger_policy:
      status: requirement_candidate_recovered
      requirement: Cross-boundary transport events must create a raw audit trace containing the pre-transform input state, transformation skill reference, triggering authorization context, and provenance fields.
      required_evidence_fields:
        - raw_input_state
        - transformation_skill_reference
        - triggering_authorization_context
        - provenance_fields
      acceptance_checks:
        - Verify S8-to-candidate or candidate-to-proposal boundary rehearsal creates a raw audit trace.
        - Verify the trace is separate from unsupported authority claims.
        - Verify the trace can be reviewed without mutating baseline, workflow, schema, registry, ontology, or current-position files.

watch_items_preserved:
  - Transition from one-off rehearsal to reusable packet template requires explicit gate approval.
  - Template existence is evidence, not established authority.
  - Gemini component-ready framing must stay subordinate to Codex recovery.

hold_items_preserved:
  - Promotion.
  - VectorFL authority mutation.
  - Modification of baseline, workflow, schema, registry, ontology, or current-position files.
  - Requirements classification to component level without authorized gate review.

authority_constraints:
  promotion_performed: false
  vectorfl_authority_mutation_performed: false
  component_authority_claim: removed
  registry_mutation_claim: removed
  schema_mutation_claim: removed

closure_note:
  The Gemini evidence is recovered only as VectorFL-safe requirements evidence. The recovered classification means the two blocker topics are sufficiently explicit and testable for component proposal requirements review. It does not promote any artifact, establish component authority, mutate VectorFL authority, or authorize registry/schema/workflow changes.

completion_signal: CODEX_REQUIREMENTS_RECOVERY_DONE

No promotion was performed. Recovery class remains candidate.
