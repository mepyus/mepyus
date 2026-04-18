# Attention Resolution Loop v1 Report

## What Was Added
- Derived lifecycle handling for attention items on top of queue generation.
- Queue surface now distinguishes active, background-suppressed, and resolved attention memory.

## Current Lifecycle Behavior
- Representative recent provenance-only runtime updates are suppressed into background summaries.
- Active attention is only emitted when router marks it queue-worthy.
- If a previous active attention is replaced by a newer signature, the older one is marked resolved.
- If a resolved or suppressed signature becomes active again, it is marked reopened.

## Provenance-Only Handling
- Provenance-only updates are the fastest to close.
- v1 absorbs them into background summaries instead of keeping them active.

## Strict Attention Families
- `traceability_shift`
- `grounding_shift`
- `blocker_added`
- `packet_texture_shift`
- `manual_correction_requires_attention`

These are marked with stricter auto-resolve policy and are intended to remain alive until a newer canonical routing result replaces them.

## Representative Assets
- `youtube_03_22`
- `openai_02_11`
- `knowledge_editing_youtube`
- `gary_tan_brain`

Current recent attention on all four assets remains `suppressed/background` because the latest runtime update is provenance-only.

## Limits
- `seen` and `deferred` are reserved but not yet driven by explicit operator actions.
- Reopen behavior is implemented at per-asset latest attention level, not yet as a full multi-item operator workflow.
- Stale handling is currently replacement-oriented, not time-window heavy.
