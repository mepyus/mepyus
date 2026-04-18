# Integrated Engine User Surface Team / Role Framework Patch Note v0

## Verdict

PASS_WITH_NOTE

## Goal

Replace hardcoded internal-role cards with a reusable User surface team / role assignment framework. The goal is not to create a new route for every loop. The goal is to create a stable operating container where the user or Codex can add teams, add roles, assign owners, open role modals, and connect only the roles that currently have allowed execution paths.

## What Changed

- Reworked `Internal Team Assignment Desk` into a configurable local team / role framework.
- Added team-level operations:
  - add team
  - edit team name / purpose
  - delete selected team
  - select team
- Added role-level operations:
  - add role
  - edit role label / owner / purpose / capability / status
  - delete role
  - open role modal
- Kept `언어담당` as the first active role using the Koreanization data loop.
- Kept `라인 추출 담당` and `외부 리서치 담당` as hold roles with no execution loop connected yet.

## Current Team Seed

| team | role | status |
| --- | --- | --- |
| 내부 언어팀 | 언어담당 | active, Koreanization loop connected |
| 내부 라인팀 | 라인 추출 담당 | hold, no loop connected |
| 외부 표현 보강팀 | 외부 리서치 담당 | hold, no external harvest opened |

## Operating Boundary

This framework belongs to the User surface because it organizes work. It does not replace VectorFL mediation or Engine processing.

- User surface: team / role / owner / assignment / modal setup.
- VectorFL surface: detailed reread, axis judgment, mediation.
- Engine surface: execution return, validation material, deposit candidate.

## What Was Intentionally Not Added

- No persistent team registry yet.
- No new runtime route per role.
- No line extraction adapter yet.
- No external research adapter yet.
- No automatic assignment or promotion.
- No final Korean UI copy.
- No fourth surface.

## Why This Is Better Than Hardcoded Cards

The previous version placed `언어담당`, `라인 추출 담당`, and `외부 리서치 담당` as fixed cards. That made the UI look like a one-off feature placement.

The new version creates a reusable assignment container first. `언어담당` is now only one configured role inside that container. This makes it easier to add, remove, or revise internal teams later without creating a new route or a new surface each time.

## Remaining Watchpoints

1. The framework is currently local UI state. A persistent registry should only be opened after the operating shape is validated by use.
2. The role capability selector can name future roles, but only `koreanization_loop` is currently executable.
3. The User surface must remain operating / distribution / decision, not become a full governance console.

## Validation

- `npm run build` passed.

