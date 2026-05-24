# VectorFL Original Intake Packet Shape Candidate V0

status: FUNCTION_SHAPE_CANDIDATE_WITH_HOLD

Purpose: preserve raw user original before space/model interpretation.

Required fields:
- packet_id: stable id for this intake artifact
- classification: candidate_packet_input_layer_no_authority_mutation
- source_layer: must be input_layer
- raw_user_original: verbatim user input; never rewritten
- interpreted_constraints: explicit constraints extracted from original; must not overwrite raw original
- watch_notes: risks such as summary-only failure, model-only drift, space refs required
- guard_status: PASS_WITH_HOLD or STOP
- authority_effect: NO_AUTHORITY_MUTATION
- promotion_status: HOLD

Forbidden:
- mutating raw original
- collapsing original and interpretation
- claiming approval/authority
- calling model/API/endpoint
