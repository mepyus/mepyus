# Integrated Engine CLI On-Top Current Operating State v0

## Verdict

PASS_WITH_NOTE

The stable integrated-engine UI can now operate Codex from the VectorFL surface and reflect the resulting CLI returns across all three fixed surfaces.

The note is that the UI language is still mostly internal/spatial language. The system is usable with Codex interpretation, but not yet comfortable as a human-facing Korean operating UI.

## Current Stable UI

- main UI source: `app/ui/integrated_engine`
- main URL: `http://127.0.0.1:5173/`
- engine API/reference server: `http://127.0.0.1:8421/`
- CLI artifact root: `runtime/cli_sessions`
- Gemini proposal/reference clay: `gemini/mock_test`

## Fixed Interpretation

- User surface: purpose, work organization, decision, assignment candidates
- VectorFL surface: interpretation, mediation, reread, direct CLI operation
- Engine surface: processing, return, validation, extraction/deposit material
- CLI layer: on-top tool/control layer, not a fourth surface
- Codex backend: local Codex CLI session inherited from the current machine environment

## What Currently Works

### VectorFL Surface

- Run Codex from the UI.
- Read latest structured return.
- Read deposit candidate preview.
- Mark returns as:
  - `reread_target`
  - `implementation_return`
  - `validation_target`
  - `deposit_candidate`
- Read recent Codex turns.
- Continue from latest or selected recent turn without manually copying artifact paths.
- See deposit-ready queue.
- Send selected User/Engine candidates back into VectorFL follow-up.

### User Surface

- Shows latest CLI return as a work/decision signal.
- Shows deposit-ready count.
- Shows a user work queue derived from recent CLI returns.
- Execution Route Board includes CLI-derived candidate tickets:
  - Backlog
  - Handoff
  - Review
- User surface can send selected candidate items back to VectorFL.

### Engine Surface

- Shows latest CLI return as processing/validation material.
- Shows validation queue.
- Shows extraction/deposit material queue.
- Primary Control Pipeline includes `CLI-derived engine material`.
- Engine surface can send selected validation/extraction material back to VectorFL.

## Validated This Round

- Stable UI build passes.
- Viewer server API state is readable.
- Real read-only Codex runs succeed through the stable UI proxy path.
- `suggested_next_use` inference now handles explicit validation-tail text.
- User surface route board receives CLI-derived tickets.
- Engine surface primary pipeline reflects CLI-derived material.
- Browser hand-checks passed for:
  - VectorFL direct CLI operation
  - Continue latest / recent turn follow-up
  - deposit-ready queue
  - User surface work queue and route board
  - Engine surface CLI material reflection
  - User/Engine `Send to VectorFL` handoff

## Still Closed

- Gemini adapter
- async/background runner
- full session browser/history
- automatic assignment
- automatic deposit ingestion
- automatic promotion/canonicalization
- runtime binding beyond the existing API/session artifact path
- UI language/readability rewrite

## Current Human-Usability Note

The operating path works, but the UI is still full of English and internal spatial terms. The user can verify structure, but final judgment still requires Codex to explain the state in the user's language.

This should be treated as a known usability gap, not as a blocker to continuing operational wiring.

## Next Bottleneck Candidates

1. Human-readable Korean/operator summary layer for each surface.
2. Bounded deposit ingestion bridge with explicit user approval.
3. Session history/browser beyond latest/recent turns.
4. Gemini adapter as proposal/material generator.
5. Async/background support for longer CLI runs.

## Recommended Next Step

Next should be a bounded human-readable operating summary layer, not full translation.

Reason:

- The user has already confirmed that the structure works.
- The user also confirmed that screen judgment is hard because the UI is English/internal-language heavy.
- Before opening automatic ingestion or Gemini adapter, each surface needs a thin "what this means now" summary so the user can steer without relying entirely on Codex final reports.

This should be summary/explanation only, not UI glossary replacement or final copy translation.
