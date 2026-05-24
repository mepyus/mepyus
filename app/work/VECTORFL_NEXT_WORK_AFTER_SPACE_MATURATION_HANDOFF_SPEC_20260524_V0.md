# VECTORFL_NEXT_WORK_AFTER_SPACE_MATURATION_HANDOFF_SPEC_20260524_V0

NEXT_SAFE_LANE: SPACE_MATURATION_HANDOFF_FILES_DRAFT_VALIDATION_NO_FOLDER_MOVE_V0

purpose:
Validate whether the created handoff files are readable enough for Codex/Gemini without loading the entire conversation history.

Rules:
- no folder move
- no source/authority/current-position/registry mutation
- no API/direct/server/replay
- script-only first
- validate that Codex input minimum is <=7 files
- validate that Gemini can read Codex packet schema separately
- optionally, after validation only, user may approve bounded Codex/Gemini CLI test
