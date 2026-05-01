# Space Sidecar Baseline v0

## Purpose

This spec establishes the minimum layer split for our space as a sidecar over OMX.

## Layer Split

OMX/Codex is the execution and runtime layer.

Our space is the digestion, recording, connection, and maturation layer.

## OMX Responsibilities

- Run tools, commands, agents, and runtime actions.
- Own execution state that belongs to OMX.
- Expose usable outputs for intake when explicitly handed off.
- Remain independent from our space memory model.

## Space Responsibilities

- Receive bounded intake from OMX or other external tools.
- Record packages using the shared package meaning contract.
- Digest material into lines, axes, digests, and indexes.
- Support review and memory maturation without becoming the runtime.

## Baseline Boundary

This baseline does not define hooks, UI, MCP extensions, agent orchestration, or runtime code.

The sidecar boundary is filesystem structure plus concise contracts only.

