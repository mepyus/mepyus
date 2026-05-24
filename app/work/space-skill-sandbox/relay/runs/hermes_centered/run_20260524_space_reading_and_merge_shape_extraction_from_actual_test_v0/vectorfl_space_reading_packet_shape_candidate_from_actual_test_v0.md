# Space Reading Packet Shape Candidate From Actual Test V0

status: FUNCTION_SHAPE_CANDIDATE_WITH_HOLD

derived_from: /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_space_reading_and_merge_actual_material_test_v0/actual_space_reading_packet_v0.json

purpose: Read actual local space materials and extract current-position anchor, safe entrypoint count, guard/layer counts, broad lens handles, candidate-only boundary, and prior packet lineage without mutation.

required_processing_checks:
- existing_materials>=7
- contains_current_position
- contains_space_wide_reread_packet
- contains_merge_doc
- safe_entry_points>=2
- guard_matrix_present
- space_wide_frame_detected
- candidate_only_merge_boundary_detected
