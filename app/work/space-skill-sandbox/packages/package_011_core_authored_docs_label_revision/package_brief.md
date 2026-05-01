# Package 011 - Core Authored Docs Label Revision

## Purpose

Implement the approved small revision to `scripts/sandbox/package_metadata_scan.sh`.

The revision adds a metadata-level `Core Authored Doc Candidates` section.
It does not interpret, rank, validate, or promote document meaning.

## Approved Changes

- add `Core Authored Doc Candidates`
- identify root-level markdown files that are not standard package records
- keep `reviewed_by: pending`
- keep package-local input/output boundary
- keep overwrite refusal

## Smoke Targets

- `app/work/space-skill-sandbox/packages/package_006_small_execution_unit_registry`
- `app/work/space-skill-sandbox/packages/package_003_graphify_compact_feedback`

## Forbidden

- meaning judgment
- ranking judgment
- promotion judgment
- source-space promotion
- whole md scan
- graph/index/ontology/router/controller
- automation/watch/hook/MCP
- package-external output

