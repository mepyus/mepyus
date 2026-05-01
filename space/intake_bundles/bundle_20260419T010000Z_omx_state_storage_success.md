# Intake Bundle

source_tool: local_reference_read
task_intent: Capture the OMX state storage note from the local reference repo.
source_refs: references/git_search/oh-my-codex-main/AGENTS.md
outputs_artifacts: null
short_tool_summary: AGENTS.md states that OMX persists runtime state under `.omx/`, with `.omx/state/` used for mode state.
known_risks_or_blockers: The excerpt is an operating contract note, not an implementation proof.
suggested_next_move: Create an intake package if the `.omx/state/` convention is useful for sidecar boundary reading.
language_bridge_notes: Treat this as runtime-layer source evidence, not as a request to implement state handling.

