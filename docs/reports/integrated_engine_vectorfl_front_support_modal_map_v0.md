# Integrated Engine VectorFL Front Support Modal Map v0

## 1. Verdict

PASS_WITH_NOTE

VectorFL now has a more explicit front/support/modal reading map. The session strip is front-visible, but the selected package/object remains the main center.

## 2. Front Layer

Front-visible:

- compact CliHost session strip
- selected object/package identity
- current interpreted state
- concise evidence summary
- blocker/open edge summary
- next route hint
- mediation process map

Implementation reading:

- `CliHostControlPanel` now opens with a compact session strip.
- `SurfaceCurrentObjectFocus` and `SingleHandlerPackagePanel` remain the current-object center.
- `VectorFLMediationProcessMap` shows the mediation flow without expanding all packet internals.

## 3. Support Layer

Support-visible:

- session templates / purpose / context refs
- internal search / evidence gate
- work packet formation fields
- full session action bar
- recent turns
- deposit-ready queue
- latest return details
- mark history
- validation queue
- line / intervention summary
- evidence line atlas
- selected line inspection

Implementation reading:

These are now mostly behind collapsible `details` blocks or below the center region.

## 4. Hold / Not Front

Not front:

- full bridge rules
- full packet-origin explanation
- full lower-input trace
- worker/team routing detail
- packet field provenance full text
- supervisor-like queue behavior

## 5. Remaining Noise

Some density remains because `CliHostControlPanel` still owns real session execution, recent turn loading, marking, and packet formation support. The difference is that these are no longer the default conceptual center.

## 6. Validation

- Front layer now answers current-object mediation first.
- Support layer keeps details reachable.
- Hold layer blocks bridge/team/trace material from becoming front-surface content.

