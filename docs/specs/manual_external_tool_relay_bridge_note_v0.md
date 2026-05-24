# Manual External Tool Relay Bridge Note v0

## Status

```yaml
status: bridge_note_candidate
date: 2026-05-06
baseline_lock: false
automation: false
scope: temporary_user_relay_for_unstable_tool_runner
```

## Purpose

When a scripted external-tool path is unreliable, the user may temporarily deliver worker output manually.

This is a bridge, not the desired operating mode.

## Rule

Manual relay is acceptable only when:

- the user explicitly supplies an external-tool result
- the scripted runner failed, timed out, or is unavailable
- Codex immediately packages the result as a worker return or Movement Record candidate
- the output is not treated as final authority

## Required Packaging

For each manually relayed external-tool result, Codex should record:

- source worker
- delivery route: `user_manual_relay`
- original prompt or task packet when available
- assets the worker claims to have consulted
- Codex judgment of reusable value
- issue / watch item
- Return-to-Space Value
- whether the relay should trigger runner reliability work later

## Do Not

- Do not normalize the user as permanent dispatcher.
- Do not ask the user to repeatedly copy/paste between tools when a space packet can be used.
- Do not treat relayed text as raw space memory.
- Do not promote relayed output without Codex/space interpretation.
- Do not build automation from this bridge note.

## Watch

If manual relay repeats, classify it as:

```text
user_relay_burden_watch
```

Then create a future bounded package for external-tool runner reliability or task-packet handoff improvement.

