# Handoff Checklist Light vs Full Mode Note v0

Status: candidate note
Authority: not baseline / not official workflow / not v1 checklist modification
Basis: Run 144 Package 033 current-position handoff application

## Purpose

This note records a usage distinction discovered while applying `whole_space_handoff_checklist_v1_candidate` to Package 033.

The point is not to revise v1. The point is to decide when a future handoff should use Light mode or Full mode.

## Full Mode

Use Full mode when the handoff is:

- cross-session
- cross-agent
- approval-gated
- whole-space oriented
- authority-sensitive
- recovering from memory/session loss
- carrying candidate evidence, invalid/orphaned status, or source provenance

Full mode should preserve:

- identity
- context
- memory_layer
- source_refs
- authority_status
- permission
- allowed_actions
- forbidden_actions
- routing
- validation
- risk
- next
- watch items
- what must not be inferred

Run 144 is a valid Full mode example because it carries Package 033 candidate evidence into current-position memory.

## Light Mode

Use Light mode when the handoff is:

- local to a stable context
- not approval-gated
- not changing authority status
- not carrying new candidate evidence
- not reopening invalid/orphaned sequence issues
- not routing across multiple agents

Light mode should usually include only:

```text
identity
context
authority_status
source_refs
forbidden_actions
next
```

Optional additions:

```text
memory_layer
risk
```

Add these only when the worker may otherwise overread context or promote evidence.

## Decision Rule

Use the smallest mode that preserves:

- role boundary
- source_refs
- authority_status
- non-promotion
- next safe action

If those can be preserved with Light mode, do not use Full mode.

If memory loss, user approval, candidate evidence, or cross-agent routing is involved, use Full mode.

## Watch Items

- Full mode can become ceremony if used for ordinary tasks.
- Light mode can become unsafe if authority status or source refs are unclear.
- Neither mode is a schema, policy, automation plan, graph, ontology, or official workflow.
- Mode choice is a judgment aid, not enforcement.

## Current Recommendation

Treat Run 144 as a Full mode example.

For future ordinary Gemini compact executions, prefer Light mode unless the task crosses authority, memory, or role boundaries.
