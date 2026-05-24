# VECTORFL_NEXT_WORK_AFTER_HANDOFF_FILES_VALIDATION_20260524_V0

NEXT_SAFE_LANE: OPTIONAL_BOUNDED_CODEX_SPACE_STEWARD_DRY_RUN_OR_HOLD_V0

purpose:
Either HOLD, or run a bounded Codex Space Steward dry-run using the provided instruction file.

Rules if running Codex:
- read only the 6 listed files in the instruction
- no folder move
- no file edits unless user separately approves output file path
- no source/authority/current-position/registry mutation
- no API/direct/server/replay
- output JSON packet only
- Gemini step only after Codex return is reviewed
