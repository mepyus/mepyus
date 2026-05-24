# Promotion Gate

## 1. Status

Status:
  PROMOTION_GATE_PREPARED_WITH_WATCH

Purpose:
  Define when a candidate artifact from the 05-15 execution may be promoted, automated, or wired into a more official surface.

Not:
  promotion approval
  automation approval
  baseline

## 2. Promotion Requires Explicit Decision

No candidate artifact in this folder promotes itself.

Promotion can be considered only if all are true:

1. repeated real use shows value
2. current candidate wording is stable enough
3. failure without promotion is clear
4. target destination is explicit
5. rollback or downgrade path is clear
6. user explicitly approves the promotion

## 3. Promotion Types

### Stable Reference

Potential destination:
  docs/specs, docs/reports, app/work stable note

Required proof:
  repeated use and no unresolved WATCH that affects wording

### Automation

Potential destination:
  script, queue helper, packet builder helper

Required proof:
  candidate-only manual use is too costly and automation scope is read-only or explicitly bounded

Hard stop:
  no credential/API/account/browser/memory/write action without separate approval

### External Tool Dispatch

Potential destination:
  Codex/Gemini/CLI/browser/API packet execution

Required proof:
  exact action, boundary, allowed/forbidden scope, Return Packet requirement

Hard stop:
  packet draft is not dispatch

### Current-position / Manifest

Potential destination:
  current-position note or output manifest

Required proof:
  user wants this candidate to become active state, not just workspace material

Hard stop:
  no automatic update

### Product/UI

Potential destination:
  route, board, dashboard, app shell

Required proof:
  user explicitly wants product surface work, not operating note work

Hard stop:
  no app route attachment by implication

## 4. Default For All Candidates

Default placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH

Default action:
  use manually as candidate material

Default HOLD:
  promotion, automation, dispatch, baseline, official memory

`STATUS: PROMOTION_GATE_PREPARED_WITH_WATCH`
