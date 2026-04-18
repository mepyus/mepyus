# Integrated Engine Koreanization Language Loop Reset Note v0

## Verdict

PASS_WITH_NOTE

## What Was Corrected

The language loop is not primarily a spatial-language cleanup loop. Its current purpose is to collect data for Koreanizing the language used inside the integrated-engine space.

The target is not instant UI copy and not a final glossary. The target is a repeatable dataset that helps convert internal engine/space terms into Korean operating language while preserving route / authority / state / boundary.

## Correct Loop Purpose

The loop should collect:

- internal phrase or signal observed
- source context where it appeared
- internal meaning / operational role
- Koreanization candidate, not final UI copy
- Korean preservation requirement
- risky Korean flattening to avoid
- why this helps the user operate
- what meaning gets lost if shortened
- repeated connection
- emerging axis candidate
- surface exposure note
- external expression support needed, if any
- next reread question

## Surface Assignment

This is a User surface internal team task, not a VectorFL core task.

| Surface | Role in this loop |
| --- | --- |
| User surface | assign language 담당 work and inspect Koreanization data |
| VectorFL surface | reread / mediate whether Koreanization preserves internal meaning |
| Engine surface | hold return artifacts, harvests, and later deposit candidates |

## Implementation Reset

- The loop prompt was changed from generic line / connection / axis harvesting to Koreanization data collection.
- The loop session now uses `requested_by_surface: user_surface`.
- The UI panel title was changed to `Internal Team / Koreanization Data Loop`.
- The control panel remains inside the User surface under the internal team / language 담당 work screen.
- The harvest script now recognizes Koreanization-specific fields and reports candidates / preservation requirements / risky flattening.

## Background Operation Note

To match the intended operating mode, the language loop action now supports background start. This keeps the loop as a task placed on top of the integrated engine instead of a terminal-only script run.

The loop is still bounded:

- no UI copy patch
- no final glossary
- no automatic deposit ingestion
- no extension promotion
- no new surface

## Current Reading

The next useful data is not "more internal vocabulary." It is Koreanization evidence:

- which internal phrases need Korean operating equivalents
- what Korean explanation preserves their role
- what Korean shortcuts would flatten them
- which phrases need outside expression support later

