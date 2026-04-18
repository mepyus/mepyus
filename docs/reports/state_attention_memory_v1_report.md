# State Attention Memory v1 Report

## What It Reads
- canonical diff-derived attention events replayed from asset history
- priority routing
- resolution loop outputs
- queue-style statuses such as `suppressed`, `resolved`, and `reopened`

## How Recurrence Is Detected
- repeated attention reason or repeated shift family within the recent memory window
- provenance-only clusters are counted as operating tendency, not as high-priority failure

## Current Representative Reading
- `youtube_03_22`
- `openai_02_11`
- `knowledge_editing_youtube`
- `gary_tan_brain`

Current recent tendency on all four is dominated by provenance-only background handling, so the memory summary is expected to stay thin and non-dramatic.

## Summary Logic
- high provenance density yields `mostly provenance_only background updates`
- repeated grounding/blocker/traceability/packet-texture families can override with family-specific summary
- low event count yields `insufficient_attention_history`

## Limits
- v1 memory is asset-centric only
- it replays recent history-derived attention rather than storing a separate long-horizon memory ledger
- operator-driven `seen/deferred` behavior is not yet rich enough to shape dominant memory patterns
