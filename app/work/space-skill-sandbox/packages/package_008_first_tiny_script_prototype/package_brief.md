# Package 008 - First Tiny Script Prototype

## Purpose

Implement the approved first tiny script prototype:

- `scripts/sandbox/package_metadata_scan.sh`

The script supports bounded package metadata discovery without scanning the whole md space and without replacing reviewer judgment.

## Approved Boundary

- input: one package directory under `app/work/space-skill-sandbox/packages/`
- output: `<package_dir>/metadata_scan_report.md`
- overwrite: refused by default
- reviewed status: `reviewed_by: pending`
- graph/ontology/router/controller/automation: false

## Smoke Target

- `app/work/space-skill-sandbox/packages/package_003_graphify_compact_feedback`

## Forbidden

- source-space promotion
- baseline declaration
- whole md space scan
- automation/watch/hook/MCP
- graph/ontology/router/controller
- Gemini result auto-application
- output outside the target package directory

