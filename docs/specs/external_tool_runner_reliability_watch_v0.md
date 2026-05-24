# External Tool Runner Reliability Watch v0

## Status

```yaml
status: watch_spec_candidate
date: 2026-05-06
baseline_lock: false
automation: false
schema: false
registry: false
scope: manual_relay_and_runner_instability
```

## Purpose

Track when scripted external-tool execution is unreliable and the user becomes a temporary relay.

This is a watch spec, not a runner implementation.

## Watch Signal

```text
user_relay_burden_watch
```

Trigger when:

- the user manually copies Gemini/Codex/Hermes/OmX output back into the space
- scripted runner times out, hits quota, or waits interactively
- worker result arrives without stable outbox packaging
- the user is asked to shuttle context between tools

## Position Link

Use:

```text
PV_MANUAL_RELAY_BRIDGE
PV_RAW_TRACE_BOUNDARY
PV_RETURN_TO_SPACE_CLOSEOUT
```

## Required Handling

When manual relay happens:

- package the result immediately as worker return
- record delivery route as `user_manual_relay`
- preserve prompt/source if available
- downshift authority/status claims
- capture Return-to-Space Value
- note whether runner reliability work should be scheduled

## Escalation To Future Bounded Package

Create a future runner reliability package only when:

- manual relay repeats across multiple worker returns
- a scripted path fails for the same reason repeatedly
- relay burden blocks user progress
- the fix is a bounded runner/task-packet handoff improvement

Do not create automation from this watch alone.

## Do Not

- Do not normalize the user as permanent dispatcher.
- Do not treat manual relay as steady-state operation.
- Do not treat relayed output as space memory before packaging.
- Do not create or modify runners from this spec without a separate approved package.
