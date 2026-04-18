# Integrated Engine Surface Projection Policy v0

## 1. Verdict

PASS_WITH_NOTE

The integrated engine may share one process underneath, but User / VectorFL / Engine surfaces must not expose the same information density.

This policy is for bounded operating mode. It is not a full redesign and not a multi-agent orchestration spec.

## 2. Core Rule

```text
same process underneath
different projection on top
```

The default surface should answer the first question of that surface. Deep bridge, trace, origin, and packet-origin detail belong in support / inspector / drill-down layers.

## 3. Surface First Questions

| surface | first question |
| --- | --- |
| User | What is the current purpose, target, status, and next decision/action? |
| VectorFL | What object is being interpreted, what is its state, what evidence/blocker matters, and where can it route next? |
| Engine | What is the ingest target, process stage, validation state, return/redeposit state, and output summary? |

## 4. Projection Rules

### User Surface

Active:

- purpose
- scope
- current target
- current status
- next action

Support:

- material context summary
- light request history
- optional package id

Hold / not front:

- full team routing detail
- full role configuration
- bridge rule detail
- lower-input trace detail
- packet origin detail

### VectorFL Surface

Active:

- current package/object being interpreted
- state / hold / usable / pending
- evidence summary
- blocker / open edge
- next route hint

Support:

- selected lens summary
- lower-derived vs upper-added detail
- bridge diagnostic summary
- expandable evidence detail

Hold / not front:

- full line atlas
- full raw lower trace
- full bridge rules
- full worker routing detail
- full packet-origin explanation

### Engine Surface

Active:

- ingest target
- current process stage
- validation state
- return / redeposit state
- output summary

Support:

- compact artifacts created
- what was not done
- gate result summary
- drill-down return record

Hold / not front:

- full asset inventory
- supervisor queue as main view
- watcher recommendations as main view
- bridge control contract full text
- full runtime artifact tree

## 5. Single-Handler Rule

This package allows one handler package only:

```text
language_handler_loop_pkg_v0
```

This is not a team system and not multi-agent orchestration.

## 6. Implementation Target

The current shell should:

- show one handler package in all three surfaces
- change what each surface projects from the same package
- keep full details in support / details elements
- avoid front-surface trace flooding
- avoid foregrounding bridge internals or worker identity

## 7. Validation

- Distinct first-question check: passed by policy.
- Active/support/hold separation: passed by policy.
- Bridge/team/trace demotion rule: passed by policy.

