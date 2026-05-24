# CODEX_GEMINI_HERMES_OPERATING_SPLIT_20260523_V0

status: OPERATING_SPLIT_CANDIDATE_WITH_HOLD
date: 2026-05-23
purpose: keep VectorFL program work space-referenced while separating model roles by cost and failure mode

## Verdict

CODEX_STRUCTURAL_DESIGN__GEMINI_BOUNDED_EXPLORATION__HERMES_MINIMAL_EXECUTION_WITH_HOLD

## Operating Rule

Codex should not act as an isolated answer generator for VectorFL.

Codex should:

- read the relevant repo/runtime/Obsidian space before classifying status
- design structure, boundaries, packets, and promotion gates
- decide what evidence is implementation, prototype, candidate, residue, or STOP
- write compact packets for Gemini and Hermes when wider exploration or execution is needed
- avoid using token budget for broad inventory work that Gemini can do

Gemini should:

- do bounded broad internal exploration
- scan large 05-* Obsidian surfaces or repo asset families when explicitly packeted
- return gaps, candidate groupings, repeated patterns, and non-inspected scope
- never mutate repo or Obsidian files
- never promote candidate material into authority

Hermes should:

- perform necessary local execution only
- run validators, tests, receipts, local no-model loops, and file materialization when explicitly packeted
- keep execution narrow and receipted
- avoid broad reasoning or unnecessary execution
- preserve HOLD boundaries unless an explicit packet-scoped approval says otherwise

## Current Evidence Basis

Recent verified sources:

- `CURRENT.md`: fragment-centered engine baseline
- `docs/reports/vectorfl_integrated_engine_asset_index_v0.md`: integrated-engine current working baseline
- `app/work/vectorfl_ops_phase_0_5/`: local SQLite + CLI + Markdown export prototype
- `app/work/vectorfl_ops_phase_1_web_mvp_skeleton/`: local read-only Web/API MVP skeleton
- Obsidian `05-18`: Pre-Alpha / organic readiness / guard buildup
- Obsidian `05-19`: packet-scoped real Gemini/Codex execution receipt and postmortem
- Obsidian `05-21`: local no-model operating loop, CLI skeleton candidate, receipt manifest hardening
- Obsidian `05-22`: Input Localization candidate package and Codex re-entry recognition packet

## Confirmed Working / Verified

- React integrated-engine UI build passed with `npm run build`.
- Phase 1 local Web MVP basic server tests passed.
- Phase 0.5 transition table validator passed.
- Phase 0.5 guardrail probe passed, but mutates the shared SQLite DB.
- 05-19 real S5/S8 output validator passed.
- 05-21 local operating output validator passed.
- 05-21 receipt manifest hardening validator passed.
- 05-21 decision surface replay consistency passed when allowed to write regenerated Obsidian outputs.
- 05-22 Input Localization validator passed.
- 05-22 Codex re-entry recognition packet validator passed.

## Key WATCH

The Phase 0.5 guardrail probe appends to the shared SQLite DB.

Observed effect:

- requests changed from 7 to 10
- guardrail_events changed from 22 to 25
- probe_requests changed from 3 to 6
- Phase 1 read-only/UI contract tests failed because they expected fixed counts

Interpretation:

This is not a promotion or authority failure. It is a program-design defect in test isolation and baseline replay semantics.

Program implication:

- use isolated DB copies for probe tests, or
- make probes idempotent, or
- rewrite Phase 1 tests to validate invariants instead of fixed counts, or
- separate baseline snapshot replay from live probe ledger verification

## Delegation Boundary

Do not ask Gemini to implement the fix.

Ask Gemini to inspect broad surfaces and identify:

- where the same shared-state mutation risk appears
- where fixed-count tests exist
- which 05-* assets already describe test isolation, replay, receipt, or baseline drift
- which candidate patterns should be considered for Codex structural design

Do not ask Hermes to explore broadly.

Ask Hermes only to:

- run specific tests/validators
- materialize specific receipts
- execute a bounded migration or patch only after Codex produces an exact patch packet and the user approves it

## HOLD

- authority mutation: NO
- promotion: HOLD
- Program Alpha claim: NO
- M3 confirmation: NO
- M4 module claim: NO
- router/runner claim: NO
- external model/tool/network expansion: NO
- baseline/schema/registry mutation: NO unless separately approved

## Next Smallest Action

1. Send the bounded Gemini gap-scan packet:
   `app/work/space-skill-sandbox/relay/packets/to_gemini/gemini_vectorfl_program_spine_gap_scan_20260523_v0.md`

2. Use the Hermes minimal execution packet only for specific validator reruns:
   `app/work/space-skill-sandbox/relay/packets/to_hermes/hermes_vectorfl_minimal_execution_verification_20260523_v0.md`

3. Codex should then design a concrete Phase 0.5 / Phase 1 stabilization patch packet, not apply it blindly.
