# Package Record Minimum v0

## Purpose

This spec defines the smallest common phase-1 package record shape for our space.

The record is shared by intake, digestion, review, and memory packages.

## Minimum Record

```text
package_id:
package_kind:
origin:
created_at:
updated_at:
source_bundle_ref:
bounded_content_pointer:
status:
short_summary:
next_action:
```

## Field Reasons

- `package_id`: gives the package a stable identity inside our space.
- `package_kind`: identifies the phase-1 kind: intake, digestion, review, or memory.
- `origin`: records where the package came from without importing runtime ownership.
- `created_at`: records when the package first entered this contract.
- `updated_at`: records when the package record last changed.
- `source_bundle_ref`: points back to the intake bundle or external handoff when one exists.
- `bounded_content_pointer`: points to the actual bounded content without forcing it into this record.
- `status`: gives the package a minimal operating state without defining lifecycle automation.
- `short_summary`: gives humans and later tools a small meaning handle.
- `next_action`: records the next intended move without creating a workflow engine.

## Shared Support For Phase 1 Kinds

`intake` packages can use the record to identify source material, source bundle, current status, and the next digestion move.

`digestion` packages can use the same record to point at worked content, summarize extracted meaning, and name the next review or connection move.

`review` packages can use the same record to point at material under judgment, summarize the review target, and name the next acceptance, correction, or return move.

`memory` packages can use the same record to point at material promoted toward durable recall, summarize its remembered meaning, and name the next maturation or reuse move.

## Intentional Exclusions

The record does not include full content because content size and format should remain outside the common contract.

The record does not include validation rules because phase 1 is defining meaning, not enforcement.

The record does not include lifecycle history because a history model would prematurely define automation and storage behavior.

The record does not include embeddings, graph links, tags, labels, scores, owners, permissions, UI state, retry state, or worker state.

Those may become separate specs later if they prove necessary.

## Path Normalization

The current OMX reference path in this repo is:

```text
references/git_search/oh-my-codex-main/
```

For phase 1, specs should refer to this current path when naming the local reference checkout.

No files are moved in this package.

A shorter normalized alias such as `references/git_search/oh-my-codex/` may be introduced by a later path policy package, but this spec does not create that alias or require it.

## Non-Goals

- No package surfaces expansion.
- No schema validation system.
- No lifecycle automation.
- No storage engine design.
- No hook implementation.
- No UI work.

