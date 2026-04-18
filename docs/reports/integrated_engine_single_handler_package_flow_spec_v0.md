# Integrated Engine Single Handler Package Flow Spec v0

## 1. Verdict

PASS_WITH_NOTE

This spec defines one handler package pilot:

```text
language_handler_loop_pkg_v0
```

It is a single-handler operating pilot, not a general team system.

## 2. Handler Package

- Package id: `language_handler_loop_pkg_v0`
- Handler id: `language-owner`
- Handler label: `언어담당`
- Role: receive one purpose/scope, pass through VectorFL classification, move through Engine processing, return to VectorFL, and surface a next user action.

## 3. Lifecycle

| step | surface | status | purpose |
| --- | --- | --- | --- |
| user-defined purpose/scope | User | done | User sets purpose/scope and target |
| VectorFL classification/lens | VectorFL | done | VectorFL chooses interpretation lens and validates evidence state |
| Engine ingest/process/validation/output | Engine | done | Engine reads target as process material and emits return candidate |
| VectorFL return review/routing | VectorFL | active | Return is classified as usable_with_hold |
| User status/next action | User | pending | User sees next valid action, not full internals |

## 4. Surface Projection

### User

Shows:

- purpose
- scope
- current target
- status
- next action

Does not front:

- bridge internals
- raw lower traces
- full worker identity

### VectorFL

Shows:

- package under review
- state / hold / usable
- evidence summary
- blocker
- next route hint

Does not front:

- full line atlas
- full bridge control text
- raw runtime tree

### Engine

Shows:

- ingest target
- process stage
- validation state
- return/redeposit summary
- output summary

Does not front:

- full asset inventory
- watcher recommendations
- supervisor queue as main view

## 5. Validation

- One-handler rule: passed. Only `language_handler_loop_pkg_v0` is introduced.
- Same-process/different-projection rule: passed by spec.
- No fake automation: passed. Lifecycle is displayed and staged, not automatic orchestration.

