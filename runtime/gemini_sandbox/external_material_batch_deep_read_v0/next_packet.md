# Gemini CLI Next Packet: external_material_batch_deep_read_v0 self-audit

## purpose

Reread your own sandbox result and identify where it failed the deep reading validation contract.

This is not a rerun of the external material batch.

This is a self-audit of:

```text
runtime/gemini_sandbox/external_material_batch_deep_read_v0/result.md
```

## safety level

```text
G0/G2 - read-only self-audit / draft only
permission: no-write
```

## files to read

Read only:

```text
runtime/gemini_sandbox/external_material_batch_deep_read_v0/result.md
docs/reports/gemini_cli_deep_reading_validation_instruction_package_v0.md
docs/reports/gemini_cli_safety_overlay_package_v0.md
docs/reports/gemini_external_material_batch_deep_read_review_v0.md
```

Do not read the whole repo.

## file to write

Preferred output:

```text
runtime/gemini_sandbox/external_material_batch_deep_read_v0/self_audit.md
```

If writing is not allowed in your execution mode, print the result only.

Do not modify any existing file.

## audit targets

Check the result against these issues:

1. The planned batch was 5 materials, but result.md contains only 3.
2. Batch-level self-check is over-positive.
3. `codex_pipeline.md` may have source-role confusion and should likely be HOLD, not PASS.
4. Evidence refs are too broad, such as `section 1`.
5. `does_not_support` fields are too weak.
6. File reporting says `None (Sandboxed output created)`, which conflates existing file modification with sandbox output creation.

## required output

```text
Verdict:
Audit surface:
Files read:

Issue check:
1. omitted materials:
2. over-positive self-check:
3. codex_pipeline source-role confusion:
4. weak evidence_ref:
5. weak does_not_support:
6. file reporting inconsistency:

Corrected material verdicts:

Corrected batch verdict:

What Gemini should do differently next time:

Files modified:
Files created:
Files deleted:
Files moved:
Files overwritten:

Risk:
Next:
```

## verdict guide

Use:

```text
PASS_WITH_NOTE
HOLD_WITH_NOTE
FAIL
```

Expected likely verdict:

```text
HOLD_WITH_NOTE
```

## do not

- Do not modify `result.md`.
- Do not modify `codex_review.md`.
- Do not update docs/reports.
- Do not update indexes or microspaces.
- Do not create schema, controller, runtime manifest, or helper/code changes.
- Do not rerun the full batch unless instructed later.
