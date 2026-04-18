# Integrated Engine Surface Declutter Validation Note v0

## 1. Verdict

PASS_WITH_NOTE

The integrated-engine shell is less noisy in the default front view. Dense bridge, line, route, team, and legacy engine details are still reachable, but moved into support/details zones.

## 2. What Was Validated

Implementation target:

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`

Validated changes:

- shared operating spine reduced to a thinner common layer
- shared spine details moved into support
- one single-handler package panel added to User / VectorFL / Engine surfaces
- User surface now foregrounds purpose/status/next action
- VectorFL surface now foregrounds mediation/evidence/blocker/route
- Engine surface now foregrounds process/validation/return/output
- broad line atlas, route/log panels, team configuration, and legacy engine mock remain available through support/detail zones

## 3. Evaluation Questions

### Is the screen less noisy?

Yes, with note.

The top of each surface now has:

- local focus
- one single-handler package projection
- surface-specific active flow

Remaining noise:

- `CliHostControlPanel` is still inherently dense.
- The internal team panel still contains many controls, but team configuration is now under support/details.

### Does User feel purpose-first?

Yes.

User surface foregrounds:

- purpose
- scope
- current target
- current status
- next action

Team/role configuration is no longer the first reading layer.

### Does VectorFL feel like classification / validation / mediation?

Yes, with note.

VectorFL now foregrounds:

- current package under review
- evidence summary
- blocker
- next route
- mediation process map

Line atlas and selected line inspection are support details.

### Does Engine feel like processing / return?

Yes.

Engine now foregrounds:

- ingest target
- process stage
- validation state
- return/redeposit state
- output summary

Legacy engine mock is moved under support.

### Is deep detail still reachable?

Yes.

Details remain reachable through expandable support zones.

### Does the single handler package flow without all internals on the surface?

Yes.

`language_handler_loop_pkg_v0` is projected differently on each surface while keeping the same lifecycle underneath.

## 4. What Improved

- The same package no longer appears as the same dense object on every surface.
- Front surface pressure decreased.
- Support/hold zones now have explicit placement.
- One-handler flow is visible without building a team dashboard.

## 5. What Still Feels Noisy

- VectorFL remains denser than User/Engine because it still hosts CLI packet formation.
- `CliHostControlPanel` may need its own active/support split later.
- Existing mock material remains large in the DOM even when moved under details.

## 6. What Still Leaks Too Much Internals

- Packet formation controls still expose internal route language.
- Some bridge/authority language appears in package support detail.
- The shared spine still shows authority state, but now in a reduced way.

## 7. Next Demotion Candidate

The next noisy area to demote further is:

```text
CliHostControlPanel internal packet formation detail
```

But this package does not perform that deeper refactor.

## 8. Validation

- Declutter check: passed with note.
- Surface distinction check: passed.
- Detail reachability check: passed.
- Single-handler flow check: passed.
- No multi-agent expansion check: passed.

