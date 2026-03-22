# Space Graph View Policy

## Purpose

The first space graph view gives a human-readable visual surface over the current runtime without changing core ontology. It is a descriptive viewer for:

- local spaces
- bridge exposures
- terrain components
- quiet local-space spread
- material inspect and trace detail on demand
- modal inspect with actual material content

## Contract

- the graph view is descriptive only
- it must not flatten the core into a single network meaning
- bridge lines are exposure traces, not merge lines
- quiet local spaces must remain visible, not hidden behind bridge-heavy spans
- the graph is a camera over the space, not the space itself
- material inspect must remain descriptive and must not flatten local spaces into one global network meaning
- inspect detail should expose which materials and traces a local space carries so actual-data relation can be observed directly
- inspect detail may move out of the sidebar when content grows, so the main canvas can remain space-first and the actual material body can stay legible

## Why this matters

The runtime is now wide enough that text reports alone are no longer sufficient. A graph view helps verify that space is visibly present, that quiet terrain survives, and that bridge-heavy spans do not dominate the whole field.

As actual memo and code-like data enter the runtime, the viewer also needs a material-inspect layer so a human can check which real artifacts formed a given local space and which weak exposures surround it.
