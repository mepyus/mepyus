# Source Bundle Ref Naming Pressure Note v0

## Purpose

This note documents the phase-1 naming pressure around `source_bundle_ref`.

It does not rename the field.

## Original Reading

`source_bundle_ref` originally sounds like a pointer to an intake bundle.

That reading fits the intake package case, where an intake package points back to a preserved manual intake bundle.

## Actual Phase-1 Usage

Across the current phase-1 chain, `source_bundle_ref` is used more broadly.

Working meaning for phase 1:

```text
source_bundle_ref is the pointer to the immediately relevant prior source record.
```

That prior source record may be:

- an intake bundle path;
- an intake package path;
- a digestion package path;
- a review package path.

In other words, the field currently means source record reference more than source bundle reference.

## Why This Is Acceptable For Now

The phase-1 chain is manual and human-readable.

No loader, validator, migration, UI, or runtime behavior depends on the field name.

The examples remain easy to inspect because each package points to the prior record that gave rise to it.

The name is imperfect, but the meaning is now explicit enough for phase 1.

## Why We Are Not Renaming Yet

Renaming now would create churn across specs and examples before tooling exists.

The current field still preserves the intended direction: this package came from that prior source record.

The broader meaning can be carried safely as a documented phase-1 convention.

## Future Rename Trigger

Reconsider a rename such as `source_record_ref` before any of these happen:

- schema validation is introduced;
- loaders or parsers depend on package fields;
- package files are generated or migrated by tools;
- UI displays or filters depend on this field;
- cross-package references become numerous enough that the word `bundle` causes real confusion.

The likely future name is `source_record_ref`, but this note does not reserve or implement it.

## Risk

The risk is that readers may assume `source_bundle_ref` always points to an intake bundle.

That is no longer true after intake.

The risk is manageable before tooling because the field values are visible paths and the chain remains manually inspected.

## Non-Goals

- No rename now.
- No schema migration.
- No compatibility layer.
- No code changes.
- No package file rewrites.
- No loader or validator behavior.
- No UI logic.

