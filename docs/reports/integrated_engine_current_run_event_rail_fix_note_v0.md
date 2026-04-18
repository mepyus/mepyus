# Integrated Engine Current Run Event Rail Fix Note v0

## 1. Verdict

PASS_WITH_NOTE

## 2. Problem

The event rail still looked mixed and hard to interpret because it showed event records as one flat stream.

That created three issues:

- current run and older records were not visually separated
- event cards did not make the run path obvious
- a runtime-tested package could be missing from the left package stack if localStorage still held an older stack

## 3. Fix Applied

### Current Run Split

The rail now separates:

- current run events
- previous records for the same package

The current run uses the newest runtime `session_id` for the selected package.

### Ordered Run Path

Current run events are shown in chronological order:

1. vessel
2. line/axis
3. line/axis source profile
4. digest
5. return
6. redeposit / reread

The cards are labeled as numbered steps instead of a flat log.

### History Demotion

Older events for the same package now move into a collapsed `previous records for this package` section.

### Package Stack Visibility

The OpenHarness test package was added to the default stack:

`pkg_openharness_structure_probe`

When stored package stack data exists in localStorage, missing default seed packages are merged instead of being hidden by stale local data.

## 4. Test Result

The OpenHarness package has three dry-run executions.

The runtime state currently reports:

- total OpenHarness events: `18`
- latest session current run events: `6`
- previous history events: `12`

This confirms the UI now has enough data to separate current run from older records.

## 5. Remaining Limit

The current run split is based on newest `session_id`. This is correct for one selected package, but not a full multi-run browser history manager.

This still does not implement:

- live streaming during CLI execution
- automatic package dispatch
- multi-handler orchestration
- line / axis promotion

## 6. Next Safe Check

Open the UI, select `OpenHarness 구조 분석`, and confirm the event rail shows:

- current run path on top
- previous records collapsed below
- source profile in packet digest

If the screen is still confusing, the next fix should adjust wording and density, not add automation.
