# Phase 1 Boundary Card

classification: PHASE_1_BOUNDARY_CARD_NOT_APPROVAL

## Current position
Phase 0.5 local loop prototype has run and passed with WATCH.

## What this unlocks safely
- Review of local loop design.
- Patch small local prototype gaps inside the same root.
- Derive Phase 1 requirements candidate.
- Draft Web MVP candidate requirements.

## What this does not unlock
- Web MVP implementation.
- production UI/API/server.
- deployment.
- real company data.
- external Codex/Gemini execution.
- authority mutation.
- promotion to Program Alpha.

## Gate before Phase 1
Before Phase 1 implementation, require a new approval packet with:
- exact root path
- exact framework/server choice
- exact DB migration boundary
- exact data policy
- exact external tool policy
- exact rollback plan
- explicit no-authority/no-promotion clauses

## Recommended next smallest safe move
PATCH_PHASE_0_5_GUARDRAIL_PROBES_V0:
Add explicit negative probes for G1, G6, G8 and a local validator, still inside the Phase 0.5 root.
