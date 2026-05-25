# Fast Cross-Inspection

Use this when Hermes or Codex needs to quickly inspect the other side's latest state.

Read order:
1. `shared_handoff/90_QUICK_EXCHANGE_BOARD.json`
2. The relevant summary card:
   - `hermes_exec/90_HERMES_LATEST_SUMMARY_CARD.json`
   - `codex_space/90_CODEX_LATEST_SUMMARY_CARD.json`
3. The latest artifact pointed to by the summary card.
4. `shared_handoff/99_LATEST_POINTERS.json` when sha/integrity verification is needed.

Quick board required sections:
- `hermes_latest`
- `codex_latest`
- `open_questions`
- `blocked_or_waiting_on`
- `latest_pointer_ref`
- `next_safe_lane`
- `boundary`
- `promotion_status`

Summary cards must include:
- `source_handle`
- `source_sha256`
- `latest_state`
- `used_for`
- `changed_judgment`
- `next_for_other_actor`
- `owner_namespace`
- `read_only_assertion`
- `promotion_status`

Rule:
The quick board is for fast reading, not authority. It points to immutable artifacts; it does not replace the full latest pointer table.
