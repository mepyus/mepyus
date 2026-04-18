# State Change Attention Queue v1 Report

## What Gets Queued
- Critical and high changes
- Medium changes when canonical drift is present and not suppressed

## What Does Not Flood the Queue
- Provenance-only runtime adoption runs
- Repeated background updates on the same asset

## Current Representative Outcome
- `youtube_03_22`, `openai_02_11`, `knowledge_editing_youtube`, `gary_tan_brain`
  - recent update reads as `provenance_only`
  - routed to `background`
  - shown through background summary instead of active queue entry

## Queue Surface
- Active queue surface: `runtime/views/state_change_attention_queue/index.json`
- Asset-specific queue summaries are also written for direct lookup.

## Process Console Connection
- Top strip shows selected asset attention state.
- Active queue items link directly into process console.
- Background summaries remain visible without overwhelming the main surface.

## Limits
- Current recent runs do not yet produce canonical shift queue items in representative assets.
- Queue status lifecycle beyond `new/suppressed` is not yet operator-driven.
