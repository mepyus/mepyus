# Minimum Trace Packet - Run 322 Gemini v2 Strict Full-Package Test

## Purpose

Rerun the visible-failure Gemini packet test after the user correctly flagged v1 as insufficiently operational.

## Source Refs

```text
app/work/space-skill-sandbox/outputs/gemini_v1_visible_failure_result_downshift_20260512_candidate_v0.md
app/work/space-skill-sandbox/relay/prompts/gemini_visible_failure_packet_test_v2_strict_full_package_20260512.md
app/work/space-skill-sandbox/relay/outbox/run_322_gemini_v2_strict_full_package_visible_failure_test_gemini_outbox_20260512_222115.md
app/work/space-skill-sandbox/outputs/gemini_v2_strict_full_package_return_packaging_20260512_v0.md
```

## Thin Plan

```text
Downshift v1 PASS to WATCH_INSUFFICIENT_DEPTH.
Require Gemini v2 to read F01-F17.
Require one extracted evidence item per file.
Require missing-file check.
Recover result as worker evidence with watch.
```

## What Was Read

```text
Gemini reported reading all F01-F17 required files.
Gemini extracted one evidence item from each file.
```

## What Was Not Read

```text
No output_manifest.md.
No full Obsidian source folder.
No runtime manifests.
No full repo tree.
No external web pages.
```

## Output Created

```text
app/work/space-skill-sandbox/relay/outbox/run_322_gemini_v2_strict_full_package_visible_failure_test_gemini_outbox_20260512_222115.md
app/work/space-skill-sandbox/outputs/gemini_v2_strict_full_package_return_packaging_20260512_v0.md
app/work/space-skill-sandbox/outputs/movement_record_gemini_v2_strict_full_package_20260512_v0.md
```

## Feedback Or Mismatch

```text
v1 was insufficient because it did not demonstrate full package traversal.
v2 fixed that by reading F01-F17.
Gemini returned PASS_V2_STRICT_PACKAGE_WORKED_WITH_WATCH.
Gemini also judged v2 too heavy for ordinary use.
```

## Recovered Judgment

```text
Strict full-package traversal is useful after a shallow worker return or for high-risk packet verification.
It should not become the daily default.
Use explicit read set, restricted vocabulary, concrete falsifiers, and missing-file checks when depth matters.
```

## Watch

```text
strict packet becomes ceremony
full-package traversal becomes daily default
worker PASS becomes approval
packet-depth ladder becomes workflow too early
```

## Next Condition

```text
Draft a candidate packet-depth ladder without automation.
```

## Return Placement

```text
RETURN_TO_SPACE_VALUE_WITH_WATCH
```

## Boundary

```text
Not automation
Not schema
Not registry
Not baseline
Not official workflow
Not current-position update
```

`STATUS: RUN_322_GEMINI_V2_STRICT_FULL_PACKAGE_MINIMUM_TRACE_PACKET_PREPARED`
