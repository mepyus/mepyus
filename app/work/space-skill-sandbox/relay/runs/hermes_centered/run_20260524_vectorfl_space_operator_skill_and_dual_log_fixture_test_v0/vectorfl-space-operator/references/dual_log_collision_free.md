# Dual Log Collision-Free Rules

Namespaces:
- `hermes_exec/`: Hermes write zone
- `codex_space/`: Codex write zone
- `shared_handoff/`: shared immutable handoff/index/pointer zone

Rules:
- No actor edits another actor namespace.
- No in-place overwrite of published return/trace/receipt.
- Shared latest pointers point to immutable artifacts and include sha256.
- Cross-read records must include `source_handle`, `source_sha256`, `used_for`, `changed_judgment`, `owner_namespace`, and `read_only_assertion`.

Shared handles:
- `shared_handoff/00_RUN_MANIFEST.json`
- `shared_handoff/01_SPACE_REFERENCE_REQUEST.json`
- `codex_space/10_CODEX_RETRIEVAL_RETURN.json`
- `hermes_exec/20_HERMES_MERGE_EXECUTION_TRACE.json`
- `shared_handoff/21_CODEX_READABLE_REENTRY_INDEX.json`
- `codex_space/30_CODEX_MATURATION_PROPOSAL.json`
- `hermes_exec/40_HERMES_MATURATION_MERGE_RECEIPT.json`
- `shared_handoff/90_QUICK_EXCHANGE_BOARD.json`
- `shared_handoff/99_LATEST_POINTERS.json`

Fast inspection cards:
- `hermes_exec/90_HERMES_LATEST_SUMMARY_CARD.json`
- `codex_space/90_CODEX_LATEST_SUMMARY_CARD.json`
