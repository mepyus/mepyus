# CODEX_PHASE0_5_PHASE1_STABILIZATION_DESIGN_20260523_V0

status: STRUCTURAL_DESIGN_PACKET_WITH_HOLD
date: 2026-05-23

## Verdict

PHASE0_5_PHASE1_TEST_ISOLATION_PATCH_READY_FOR_HERMES_PACKET_WITH_HOLD

## Structural Finding

VectorFL's current local program spine has a strong evidence habit: operations leave receipts, events, and dashboards.

That is good for VectorFL.

But the same habit creates a program testing problem when negative probes are rerun against the shared evidence DB. The probe is intentionally append-only, so every verification run changes the state that Phase 1 tests expect to be fixed.

Observed break:

- Phase 0.5 guardrail probe PASS added new probe rows.
- Phase 1 read-only contract tests then failed because fixed counts changed.
- Safety invariants remained healthy: fail_events=0, authority_mutations=0, non_hold_reviews=0.

## Design Decision

Do not rollback the shared SQLite DB from Codex.

Reason:

- The added probe rows are real local verification residue.
- Deleting them would erase evidence and violate VectorFL's receipt-first operating style.
- The correct program fix is isolation or invariant-based verification, not silent state cleanup.

## Patch Direction

Use:

- env-overridable DB path for mutable probes
- temp DB copies inside Phase 1 tests
- invariant assertions for live/evidence surfaces
- fixed-count assertions only for frozen fixture DBs

## Delegation

Hermes should apply the exact patch packet only if the user approves:

`app/work/space-skill-sandbox/relay/packets/to_hermes/hermes_phase0_5_phase1_test_isolation_patch_packet_20260523_v0.md`

Gemini can still perform broad scan later:

`app/work/space-skill-sandbox/relay/packets/to_gemini/gemini_vectorfl_program_spine_gap_scan_20260523_v0.md`

But this first stabilization patch does not need to wait for Gemini because the defect has a local direct cause and bounded patch surface.

## HOLD

- no authority mutation
- no promotion
- no Program Alpha claim
- no M3/M4 claim
- no router/runner claim
- no baseline/schema/registry mutation
- no external model/tool/network expansion
