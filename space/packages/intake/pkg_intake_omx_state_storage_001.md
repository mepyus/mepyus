---
package_id: pkg_intake_omx_state_storage_001
package_kind: intake
origin: local_reference_read
created_at: 2026-04-19T01:00:00Z
updated_at: 2026-04-19T01:00:00Z
source_bundle_ref: space/intake_bundles/bundle_20260419T010000Z_omx_state_storage_success.md
bounded_content_pointer: references/git_search/oh-my-codex-main/AGENTS.md
status: open
short_summary: Source evidence says OMX persists runtime state under `.omx/`, including `.omx/state/` for mode state.
next_action: Decide whether this runtime-state location should be digested into the sidecar boundary reading.
---

# Package Notes

This intake package accepts the AGENTS.md state-management excerpt as source evidence.

It does not define sidecar storage or state handling.

## Digestion Candidate Note

readiness: ready for digestion reading
why_worth_reading: The package captures a concrete runtime-state location that helps separate OMX runtime responsibility from the sidecar space.
space_question: How should the sidecar baseline read `.omx/state/` without absorbing OMX runtime state ownership?
digestion_should_clarify: Separate OMX mode-state storage from our space package/memory records.
first_source_pointer: references/git_search/oh-my-codex-main/AGENTS.md
allowed_uncertainty: The exact OMX state file formats can remain unread.

