# Intake Bundle

source_tool: local_artifact_check
task_intent: Inspect a referenced artifact before deciding whether it can become intake material.
source_refs: null
outputs_artifacts: runtime/logs/missing_example.log
short_tool_summary: The referenced artifact was not found at the expected path.
known_risks_or_blockers: The missing artifact blocks confident intake because the source content cannot be inspected.
suggested_next_move: Verify whether the artifact path was copied incorrectly before creating an intake package.
language_bridge_notes: Treat this as blocked source evidence, not as a failed package record.

