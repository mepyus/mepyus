# Space Attachment And Reuse Manual v0

## Purpose

This manual explains how to attach outside patterns or reuse internal assets without overreaching.

## Core Rule

Prefer:

- feature attach
- bounded pattern reuse

over:

- whole-repo import
- whole-runtime replacement

## Three Reuse Modes

### 1. Direct Reuse

Use when an asset is already shaped for our space.

Typical examples:

- existing internal reports
- current contracts
- current runtime latest artifacts

### 2. Pattern Reuse

Use when an external or internal asset contains a useful pattern but should not be copied wholesale.

Typical examples:

- workflow decomposition
- permission boundary design
- packet / report sequencing
- retrieval architecture

### 3. Attach Candidate

Use when a bounded tool or function could realistically plug into our space.

Typical examples:

- retrieval sidecar
- bounded search layer
- operator support helper

## Current Practical Rule For External Tools

When reading external repos:

1. identify the smallest useful function surface
2. map that surface against our current space
3. decide:
   - attach candidate
   - bounded pattern candidate
   - reference-only

Do not start from:

- “should we adopt this repo?”

Start from:

- “which function from this repo is worth carrying?”

## Current Proven Example

See:

- [space_external_tool_repo_attach_inventory_report_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/space_external_tool_repo_attach_inventory_report_v0.md)
- [space_external_tool_repo_attach_feasibility_report_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/space_external_tool_repo_attach_feasibility_report_v0.md)

Current bounded result:

- `qmd-main` -> strong attach candidate
- `OpenHarness-main` -> bounded pattern candidate
- `oh-my-codex-main` -> bounded pattern candidate
- `ralph-main` -> bounded pattern candidate

## Internal Reuse Rule

Before building something new, check whether the same role already exists in:

- `source_assets/`
- `docs/reports/`
- `runtime/manifests/`
- `runtime/contracts/`

If a matching role exists, reuse or translate it before creating a new structure.

## What To Avoid

Do not:

- import entire external runtimes because one feature looks useful
- treat unresolved pressure as permission to redesign the whole space
- skip current-space mapping before proposing adoption

## One-Line Summary

Reuse by function and pattern first; attach only what fits; avoid wholesale import.
