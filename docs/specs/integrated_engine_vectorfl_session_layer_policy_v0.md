# Integrated Engine VectorFL Session Layer Policy v0

## 1. Verdict

PASS_WITH_NOTE

CliHost is a session layer. It is important, but it is not the conceptual center of the VectorFL surface.

VectorFL's center remains the selected object or package under interpretation.

## 2. Corrected Reading

The previous dense CliHost placement was only partially correct.

It correctly recognized that CLI conversation is part of current operation, but it overexposed the session mechanics. That made VectorFL read too much like a host-control console.

The corrected policy is:

```text
session strip supports the selected object reading
selected object reading remains the VectorFL center
```

## 3. VectorFL Center

The front center of VectorFL must answer:

- what object/package is currently being read
- what interpreted state it is in
- whether it is hold / usable / pending / review-needed
- what concise evidence supports the reading
- what blocker or open edge remains
- what next route candidate is visible

## 4. Session Layer

The session layer may show:

- compact current package/session label
- one-line purpose or instruction
- compact state pill
- compact route hint
- command input
- send / revise / stop-hold / refresh controls
- one-line latest session event

It must not default-open:

- full recent turn history
- full latest return text
- full marks list
- bridge rules
- lower-input trace details
- packet origin detail
- worker/team routing detail

## 5. Support Layer

Support may contain:

- latest session result summary
- recent turn list
- selected lens summary
- bridge diagnostic summary
- lower-derived / upper-added summary
- expanded evidence detail
- route classification reasons
- mark history

These should be collapsible by default where practical.

## 6. Modal / Inspector Layer

Deep x-ray content belongs below or behind the main surface:

- full evidence bundle
- full return record
- provenance / trace detail
- stop-rule reasoning
- packet origin detail
- lower-input residue detail
- bridge dependency-heavy explanation

## 7. Boundaries

This policy does not authorize:

- multi-handler expansion
- automatic bridge implementation
- worker-centric UI
- supervisor-free CLI handoff
- upper/lower unification
- canonical lower-to-upper bridge

## 8. Validation

- VectorFL first question is clearer: the selected package/object remains central.
- Session vs center is separated: CliHost becomes compact session support.
- One-handler flow is preserved: `language_handler_loop_pkg_v0` still projects across User / VectorFL / Engine.

