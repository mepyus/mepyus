---
package_id: pkg_digestion_omx_project_memory_boundary_001
package_kind: digestion
origin: local_reference_read
created_at: 2026-04-19T01:10:00Z
updated_at: 2026-04-19T01:10:00Z
source_bundle_ref: space/packages/intake/pkg_intake_omx_project_memory_001.md
bounded_content_pointer: references/git_search/oh-my-codex-main/AGENTS.md
status: open
short_summary: Interpret `.omx/project-memory.json` as OMX runtime/project memory, not sidecar memory package storage.
next_action: Clarify the boundary between OMX cross-session memory and sidecar durable preservation records.
---

# Package Notes

Interpretation work starts because the intake package directly tests the word memory across both systems.

The internal JSON shape remains out of scope.

## Digestion Note

source_read: references/git_search/oh-my-codex-main/AGENTS.md
meaning_question: Does `.omx/project-memory.json` name OMX project memory rather than our sidecar memory package layer?
clarified: `.omx/project-memory.json` can be treated as OMX cross-session memory, while sidecar memory packages are durable preservation records.
unresolved: The JSON schema and exact runtime update behavior remain unread.
next_interpretation_move: Keep OMX project memory and sidecar memory packages distinct in wording.

## Review Candidate Note

readiness: ready for review reading
digestion_work_done: Interpreted `.omx/project-memory.json` as OMX cross-session project memory.
clarified_point_for_review: Sidecar memory packages should not be read as the same thing as OMX project-memory storage.
first_review_pointer: space/packages/digestion/pkg_digestion_omx_project_memory_boundary_001.md
acceptable_uncertainty: The JSON schema and runtime update behavior remain unresolved.
review_should_check: Whether the wording keeps both uses of memory distinct without inventing routing or tooling.

