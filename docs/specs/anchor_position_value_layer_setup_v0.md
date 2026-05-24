# Anchor Position Value Layer Setup v0

## Status

```yaml
status: position_value_layer_candidate
date: 2026-05-06
line: Plan from Space / Session Convergence Prevention
baseline_lock: false
automation: false
registry: false
schema: false
authority_state: candidate_reference
```

## Purpose

The Position Value layer gives small anchors compact location markers for external-tool work.

It is a transmission catalog, not a registry or ontology. The canonical seed is `docs/indexes/plan_from_space_position_map_seed_v0.md`; this setup file explains how to use those values during sessions and how to translate common worker aliases.

## Core Rule

Small anchors should transmit only the PVs needed for the next operation. The goal is to preserve position without replaying the whole space.

## Canonical PVs And Accepted Aliases

| Canonical ID | Accepted Alias | Use |
| --- | --- | --- |
| `PV_PLAN_BASIS_GATE` | same | Requires a Plan Basis grounded in Line, Axis, Camera, and Lens before planning. |
| `PV_BROAD_BOUNDED_PACKAGE` | `PV_BROAD_BOUNDED` | Marks broad-but-bounded package sizing when no blocking split reason exists. |
| `PV_RAW_TRACE_BOUNDARY` | `PV_RAW_TRACE` | Keeps Gemini/Codex/Hermes logs and reports isolated until interpreted. |
| `PV_MANUAL_RELAY_BRIDGE` | `PV_USER_RELAY_SAFE` | Allows user manual relay only as a temporary bridge that must be packaged. |
| `PV_RETURN_TO_SPACE_CLOSEOUT` | `PV_RETURN_READY` | Requires recoverable material and reusable judgment before closeout. |
| `PV_LINE_MATURITY_CAUTION` | `PV_LINE_READING`, `PV_LINE_MEMORY` | Prevents a reading lens or repeated wording from becoming a baseline line registry. |
| `PV_NON_INSPECTED_DISCLOSURE` | none | Requires explicit disclosure of bounded read scope and non-inspected material. |
| `PV_BOUNDED_REREAD_UNIT` | none | Sends Gemini or another tool into a bounded reread, not a broad scan. |

Aliases may appear in raw worker output. Movement Records and packaged reports should normalize aliases to canonical IDs.

## Recommended Small Anchor Sets

Planning:

```text
PV_PLAN_BASIS_GATE
PV_BROAD_BOUNDED_PACKAGE
PV_RETURN_TO_SPACE_CLOSEOUT
```

Bounded Gemini reread:

```text
PV_BOUNDED_REREAD_UNIT
PV_NON_INSPECTED_DISCLOSURE
PV_RAW_TRACE_BOUNDARY
```

Manual worker return intake:

```text
PV_MANUAL_RELAY_BRIDGE
PV_RAW_TRACE_BOUNDARY
PV_RETURN_TO_SPACE_CLOSEOUT
```

Line maturity check:

```text
PV_LINE_MATURITY_CAUTION
PV_NON_INSPECTED_DISCLOSURE
```

## Usage Rules

- A missing PV does not automatically block work; it triggers a compact position check.
- PVs are not static tags. Update them through Movement Records or packaged return reports.
- Do not create new PV IDs when an existing canonical ID covers the position.
- Do not promote this layer into an automated writer, database schema, line registry, or authority file.
- If a worker claims full-space authority, package the result as raw trace and apply `PV_LINE_MATURITY_CAUTION`.

## Current Watch

- Gemini recently emitted shortened aliases and authority language. The useful findings are retained, but the authority claim is downshifted.
- The PV layer remains an extension candidate derived from May 6 setup work, not an original source mandate from the nine foundational documents.
