# Integrated Engine User Surface Internal Team Assignment Patch Note v0

## Verdict

PASS_WITH_NOTE

## Goal

Correct the User surface placement of the Koreanization language loop. The loop should not appear as an isolated card with no team / role / assignment context. It should be opened from an internal team assignment desk, where the user can see which internal role owns the work and where detailed reread should continue.

## What Changed

- Replaced the standalone language-loop card placement with `Internal Team Assignment Desk`.
- Added internal role slots:
  - `언어담당`: active, opens the Koreanization data loop setup modal.
  - `라인 추출 담당`: hold slot only.
  - `외부 리서치 담당`: hold slot only.
- Moved the full Koreanization loop controls into a modal opened from the `언어담당` role.
- Kept the User surface body focused on assignment / status / recent operation log.
- Added a detail-route note that deeper processing and reread should happen in the VectorFL surface.

## Why This Is Safer

The User surface remains an operating / distribution / decision surface. It does not become a raw loop output page or a VectorFL reread surface.

The role slots show that the language loop is one internal-team assignment among future internal roles. They do not promote line extraction or external research into active features yet.

## What Was Intentionally Not Opened

- No new surface.
- No new runtime binding.
- No final Korean UI copy.
- No final glossary.
- No automatic external research.
- No line extraction loop implementation.
- No automatic deposit ingestion.

## Watchpoints

1. The internal role slots are currently UI-level assignment posture, not a first-class team registry.
2. The language loop modal still exposes some internal English because final UI copy is still closed.
3. Future role activation should require separate gates, especially line extraction and external research.

## Validation

- `npm run build` passed.
- Python compile check passed for runtime/API/loop scripts.

