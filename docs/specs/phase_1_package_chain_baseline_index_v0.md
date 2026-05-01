# Phase 1 Package Chain Baseline Index v0

## Purpose

This baseline freezes the current phase-1 package chain:

```text
intake bundle -> intake package -> digestion package -> review package -> memory package
```

It freezes the manual, human-readable structure that exists now.

It does not solve automation, routing, validation, lifecycle, UI, runtime ingestion, line/axis extraction, or field renaming.

## Core Chain Summary

- intake bundle: 외부 결과를 package 이전에 작게 붙잡아 두는 capture note.
- intake package: space 안으로 받아들인 첫 기록.
- digestion package: intake material을 의미로 읽기 시작한 interpretation 기록.
- review package: digestion 결과를 확인하고 판단하기 시작한 checking 기록.
- memory package: review된 wording/value를 오래 보존할지 다루는 preservation 기록.

## Core Spec List

- `docs/specs/space_sidecar_baseline_v0.md`
- `docs/specs/package_core_v0.md`
- `docs/specs/package_record_minimum_v0.md`
- `docs/specs/package_vocabulary_minimum_v0.md`
- `docs/specs/package_file_placement_minimum_v0.md`
- `docs/specs/package_authoring_minimum_v0.md`
- `docs/specs/intake_bundle_authoring_minimum_v0.md`
- `docs/specs/intake_bundle_file_placement_minimum_v0.md`
- `docs/specs/intake_bundle_to_intake_package_handoff_minimum_v0.md`
- `docs/specs/intake_package_to_digestion_package_handoff_minimum_v0.md`
- `docs/specs/digestion_package_to_review_package_handoff_minimum_v0.md`
- `docs/specs/review_package_to_memory_package_handoff_minimum_v0.md`
- `docs/specs/source_bundle_ref_naming_pressure_note_v0.md`

## Actual Example File List

- `space/intake_bundles/bundle_20260419T000000Z_omx_path_check_success.md`
- `space/packages/intake/pkg_intake_omx_path_check_001.md`
- `space/packages/digestion/pkg_digestion_omx_path_policy_001.md`
- `space/packages/review/pkg_review_omx_path_policy_001.md`
- `space/packages/memory/pkg_memory_omx_path_policy_001.md`

## Known Held Items

- Automation.
- Routing.
- Line/axis extraction.
- Lifecycle engine.
- UI surface expansion.
- Rename of `source_bundle_ref`.
- Tooling, validation, and migration.

## Working Interpretation Note

For phase 1, `source_bundle_ref` means the pointer to the immediately relevant prior source record. That prior source record may be an intake bundle path or a prior package path. The name is imperfect, but acceptable while the chain is manual and human-readable.

## Phase-1 Usage Note

A human uses the chain by capturing an external result as an intake bundle, accepting it as an intake package, interpreting it as digestion, checking it as review, and preserving reviewed wording or value as memory.

Each step stays manual.

Each step should remain small enough to read directly.

