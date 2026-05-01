# Intake Bundle

source_tool: local_reference_read
task_intent: Capture the OMX project-memory note from the local reference repo.
source_refs: references/git_search/oh-my-codex-main/AGENTS.md
outputs_artifacts: null
short_tool_summary: AGENTS.md states that `.omx/project-memory.json` is cross-session memory under the OMX `.omx/` area.
known_risks_or_blockers: The excerpt names runtime/project memory but does not describe its JSON shape.
suggested_next_move: Create an intake package if this helps test the boundary between OMX memory and sidecar memory packages.
language_bridge_notes: Treat this as OMX runtime/project memory evidence, not as sidecar durable memory.

