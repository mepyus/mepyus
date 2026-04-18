# Integrated Engine Activity Rail and Digest Support Policy v0

## 1. Verdict
PASS_WITH_NOTE

## 2. Activity Rail
The activity rail is an event layer, not a content panel. It should make movement visible without asking the user to read logs.

Allowed event examples:

- user purpose/scope fixed;
- VectorFL classification done;
- Engine validation done or pending;
- return received;
- reroute suggested;
- hold triggered;
- CLI return failed.

Activity rail content should remain compact:

- label;
- surface;
- state;
- one short summary.

It must not carry full return text, packet-origin detail, bridge rules, provenance, route trees, or team configuration.

## 3. Digest Support
Digest support is the compact judgment cue layer between center and inspector.

Reusable digest grammar:

- compact status card;
- warning / drift cue;
- next-action cue;
- evidence digest;
- trace digest;
- not-done digest;
- inspector trigger.

Digest support may summarize what the deeper panel contains, but it should not duplicate the deeper panel.

## 4. Surface-Specific Use
### User
Digest cues: warning, recent change, blocker, package reference.

### VectorFL
Digest cues: selected lens, evidence digest, bridge diagnostic, latest session summary.

### Engine
Digest cues: asset summary, watch/drift warning, trace digest, not-done summary.

## 5. Inspector Boundary
The following remain inspector material:

- full evidence bundle;
- full return record;
- recent turn list;
- packet formation detail;
- lower-input residue detail;
- role/team configuration;
- route/log panels;
- line atlas;
- legacy engine mock.

## 6. Validation
The rail and digest grammar improve visibility without adding a new handler or a second shell. The rail shows movement; digest support shows compact judgment cues; inspector keeps the x-ray detail available but not front-dominant.
