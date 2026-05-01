# Package 057 — Operational Trace Layer Review

## 1. Goal
Audit the operational trace layer around `folder_status`, folder inventory manifests, and `folder_change_log.jsonl`.

This is not an implementation task. The purpose is to determine whether sandbox activity can appear in operational traces in a way that future agents might mistake for core registry state, baseline state, or source-of-truth provenance.

## 2. Required Reading
Read only the bounded files below unless a direct import/reference requires one small adjacent file.

- `app/core/registry/folder_status_sync.py`
- `app/core/registry/folder_status.md`
- `app/core/folder_status.md`
- `app/core/runtime/workspace_manifest.py`
- `runtime/manifests/folder_changes/folder_change_log.jsonl`
- `runtime/manifests/folder_changes/folder_status.md`
- `docs/reports/space_structure/folder_inventory_delta_sync_review_v1.md`
- `docs/reports/stage1_space_readability_operation_integration_map_v1.md`

Optional, only if needed:
- `scripts/folder_status_sync.py`
- `scripts/sync_folder_status.py`
- `runtime/manifests/folder_inventory/app.work.space-skill-sandbox.json` if present
- `runtime/manifests/folder_inventory/app.work.json` if present

## 3. Lenses

### Trace Boundary Lens
- What is append-only operational trace?
- What is current rendered state?
- What is inventory manifest data?
- What is merely a readable folder-status surface?

### Sandbox Visibility Lens
- Can `app/work/space-skill-sandbox/` appear in folder inventory or change logs?
- If yes, does that imply promotion, or only observation?
- Which wording could cause future agents to overread sandbox traces?

### Source-of-Truth Lens
- Is `folder_change_log.jsonl` a source of truth, an audit trail, or a derived operational trace?
- Are `folder_status.md` files authoritative or rendered views over inventory manifests?
- What should remain separate from `provenance_link_index_v1.json`?

### Agent Calibration Lens
- Which trace artifacts should Gemini/Codex treat as evidence?
- Which trace artifacts must not be treated as permission to promote, baseline, merge, or canonicalize?

## 4. Required Output

Return the report in this structure:

1. Reading strategy
2. Files read table: path / role / why selected / confidence
3. Operational trace map:
   - append-only traces
   - inventory manifests
   - rendered `folder_status.md` surfaces
   - workspace manifest view
4. Sandbox visibility finding:
   - whether sandbox paths are visible
   - what visibility means
   - what visibility does not mean
5. Source-of-truth classification table:
   - artifact
   - classification: source / audit trail / derivative view / readable render / unknown
   - evidence
   - risk if misread
6. Confusion points
7. Safe operating rules for future packets
8. Dangerous assumptions
9. What not to promote
10. What Codex/user should manually verify
11. Recommended next package
12. Verdict:
   - PASS
   - PASS_WITH_TRACE_WARNINGS
   - HOLD_FOR_HUMAN_DECISION

## 5. Hard Constraints
- Do not modify files.
- Do not recommend changing `folder_status_sync.py`.
- Do not recommend automatic promotion of sandbox artifacts.
- Do not treat sandbox visibility in folder inventory as registry membership.
- Do not treat `folder_status.md` as canonical state unless implementation confirms it.
- Do not collapse folder trace concepts into provenance concepts.
- If evidence is missing, mark the claim as `needs_manual_verification`.

## 6. Calibration Reminder
You are a guest reader in this space. Your job is to read, classify, and warn about boundary confusion. Promotion, baseline, canonical status, and source-of-truth changes require human judgment.
