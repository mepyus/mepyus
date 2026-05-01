# Package 009 - Metadata Scan Second Application

## Purpose

Apply the approved `package_metadata_scan.sh` prototype to a second bounded package and evaluate whether the generated report is useful for Codex package validation.

## Target

- `app/work/space-skill-sandbox/packages/package_006_small_execution_unit_registry`

## Why This Target

Package 006 contains multiple package-level authored documents and no raw/outbox transcript set.
It is a good target for checking whether metadata-first discovery highlights the right review surface without reading the whole md space.

## Boundary

- no script modification
- no source-space promotion
- no baseline declaration
- no automation/watch/hook/MCP
- no graph/ontology/router/controller
- no whole md space scan
- output must remain inside the target package

