# Measurement Retention Policy

## Purpose

The replica must preserve ambiguous measurements, tentative judgments, and intermediate outputs instead of discarding them.

This system treats process traces as reusable assets.

## Core Rule

If a value, label, anchor, connection, or spatial judgment is not fully stable, it must still be recorded with its basis and revision path.

Do not keep only the latest result.
Keep the current result together with the reason, confidence, and revision possibility.

## What Must Be Retained

Retain all of the following when available:

- current value
- evidence or reason
- origin
- confidence
- provisional status
- source fragment reference
- previous value
- updated value
- revision reason
- revision timestamp

## Target Areas

This policy applies to:

- input segmentation
- anchor generation
- label assignment
- processing values
- dust connections
- local spatial judgments
- human corrections
- assistant and tool-generated proposals

## Operational Principle

Ambiguous output is not noise by default.

Ambiguous output is retained because:

- it may become useful later
- it can explain why a later correction happened
- it may serve as training or comparison data
- it preserves the real path of reasoning

## Revision Rule

When a value changes:

- do not silently overwrite
- append the new judgment
- preserve the previous judgment
- record why the change happened

## Logging Rule

Every meaningful implementation or policy change should also be recorded in session logs when possible.
