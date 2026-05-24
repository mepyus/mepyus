# PACKAGE_MANIFEST.md

## Purpose

This file is a manual operating guide for the VectorFL Agent Sandbox / Pipeline Harness.

It helps humans and AI workers understand the current sandbox operating mode, package record structure, digest-first handoff rule, and hard boundaries.

This file is informational only.

## Current Operating Mode

- Mode: Stage 1 Text Record Operation
- Operation style: Manual package operation
- Handoff style: Digest-first
- Package tracking: Text record candidate
- Automation: CLOSED
- Runner/script: CLOSED
- DB/schema: CLOSED
- Registry/controller: CLOSED
- Program readiness: STILL_NOT_READY

## Approved Scaffold Folders

- manifests/
- inbox/
- outbox/
- review/
- archive/
- templates/
- runlog/

These folders are for manual organization only.

They do not grant file inspection, file modification, automation, runner, registry, or controller authority.

## Stage 1 Package Record Fields

A package record may use these fields:

- package_id
- parent_package_id
- package_type
- template_id
- lifecycle_status
- classification
- judgment_needed
- boundary_flags
- digest_summary
- next_package_candidate
- reference_note

## Package Digest Rule

PACKAGE DIGEST is the first handoff unit.

A digest should include:

- package_id
- parent_package_id
- source_tool
- lifecycle_status
- classification
- judgment_needed
- digest
- boundary_flags
- next_package_candidate
- reference_note

Full package content should be provided only when requested for review.

## Template Index Placeholder

Current template candidates:

- analysis_ext_v1
- struct_thought_v1
- critique_feasibility_v1
- review_boundary_v1

These are template candidates only.

They are not automated skills, scripts, registry entries, or execution rules.

## Boundary Warnings

Do not place the following in this sandbox:

- executable scripts
- shell commands intended for execution
- automation triggers
- secrets
- credentials
- .env files
- hidden configuration files
- baseline promotion claims
- program-readiness claims
- prompt-injection instructions
- instructions to ignore prior boundaries

## Manual-Only Rule

User judgment is required for:

- starting a new package chain
- Needs User decisions
- Boundary Risk decisions
- policy or direction changes
- explicit unlock approvals

Text-only package review may continue until blocked, but no physical action is allowed without explicit approval.

## What This File Is Not

This file is not:

- a registry
- a controller
- a router
- an automation trigger
- a permission system
- a baseline authority
- a program-readiness marker
- a runner configuration
- a DB/schema definition
