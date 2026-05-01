---
package_id: pkg_intake_omx_project_memory_001
package_kind: intake
origin: local_reference_read
created_at: 2026-04-19T01:10:00Z
updated_at: 2026-04-19T01:10:00Z
source_bundle_ref: space/intake_bundles/bundle_20260419T011000Z_omx_project_memory_success.md
bounded_content_pointer: references/git_search/oh-my-codex-main/AGENTS.md
status: open
short_summary: Source evidence says `.omx/project-memory.json` is OMX cross-session memory.
next_action: Decide whether this should be digested into the OMX memory versus sidecar memory boundary.
---

# Package Notes

This intake package accepts the AGENTS.md project-memory excerpt as source evidence.

It does not define or import OMX memory behavior into the sidecar.

## Digestion Candidate Note

readiness: ready for digestion reading
why_worth_reading: The package names an OMX memory file that could be confused with our sidecar memory package.
space_question: How should the sidecar read `.omx/project-memory.json` without confusing it with sidecar memory packages?
digestion_should_clarify: Separate OMX cross-session project memory from our durable preservation records.
first_source_pointer: references/git_search/oh-my-codex-main/AGENTS.md
allowed_uncertainty: The JSON structure and update behavior can remain unread.

