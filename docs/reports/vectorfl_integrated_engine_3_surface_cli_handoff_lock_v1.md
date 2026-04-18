# VectorFL Integrated Engine 3-Surface CLI Handoff Lock v1

Date: 2026-04-14

## verdict

- This is a baseline interpretation lock for CLI workers.
- This is not a new implementation plan, schema lock, worker-orchestration plan, or UI expansion directive.
- The current integrated engine should be read as a three-surface translation of the existing VectorFL/engine internals, not as a newly invented body.
- CLI/agent layers are optional tool layers on top of the body. They must not replace the three-surface body.

## locked body

The body has three surfaces:

- User surface: sets request, goal, scope, and material context.
- VectorFL surface: reads and translates the request as intermediate formations before execution.
- Engine surface: ingests, processes, validates, records trace/memory, and returns output.

Minimum invariant:

- User surface: `Goal`, `Scope`, `Material Context`
- VectorFL surface: `Active Line`, `Relation / Gap`, `Pending / Reflux traces`
- Engine surface: `Ingest`, `Process / Validate`, `Memory / Return`

## current reading rule

Read the current three-surface structure as a surface translation of the existing engine:

- User surface pulls forward the existing purpose, scope, and material-context start.
- VectorFL surface foregrounds the existing middle reading layer: line, relation, gap, pending, and reflux.
- Engine surface separates the existing ingest, process, validate, trace, memory, and return layer.

The core loop is:

1. User surface sets goal and scope.
2. The goal attaches to material context.
3. VectorFL surface reveals intermediate formations such as line, relation, gap, and pending.
4. Some formations become processable candidates.
5. Engine surface processes and validates them.
6. Return comes back with trace and memory, not only result text.
7. That return becomes material for the next goal and next reading.

Compressed rule:

The integrated engine sets goal and scope on the user surface, reveals intermediate formations on the VectorFL surface, processes/validates/memorizes/returns on the engine surface, and uses that return as material for the next cycle.

## extension-layer boundary

Treat the following as operating extensions or future layers, not the body skeleton:

- standing team structure on the user surface
- Team Relay Board as a first-class operating node
- Handoff / Waiting / Report as body-critical nodes
- VectorFL surface as a full workflow or coordination hub
- detailed activation / ingest / return formulas
- external research automation
- CLI auto-calling structure
- automatic team assignment, routing, or queue distribution

These may become useful, but they must not be promoted into the body without an explicit later lock.

## section classification

Current user-surface sections:

- `Goal Declaration`: body skeleton
- `Material Context`: body skeleton
- `Team Relay Board`: operating extension layer
- `Handoff / Waiting / Report`: operating extension layer

Current VectorFL-surface sections:

- `Flow Summary`: body-compatible reading surface
- `Active Line Atlas`: body skeleton
- `Relation / Gap Field`: body skeleton
- `Ingress / Reflux / Pending Trace`: body skeleton

Current engine-surface sections:

- `Ingest Entry`: body skeleton
- `Pipeline Status`: process/status surface
- `Validation Return`: body skeleton
- `Asset / Watch / Trace / Memory`: body skeleton, especially because trace/memory prevents the engine surface from collapsing into a simple result generator

## CLI working rules

- Do not mix the body three-surface structure with the optional tool layer.
- Do not connect the user surface directly to the engine surface as the main interpretation; the VectorFL intermediate reading surface must remain between them.
- Keep the VectorFL surface as intermediate-formation reading, not a flat workflow board.
- Keep the user surface centered on goal, scope, and material context, not team management.
- Keep the engine surface centered on processing plus trace/memory/return.
- Prefer clarification of the natural flow over premature automation, schema, state machine, or canonical DB decisions.

## supersession note

This note refines earlier integrated-engine three-surface wording where the user surface could be over-read as an assignment desk and the VectorFL surface could be over-read as an operations board. Those units remain valid as extension or lineage material, but the current body lock is:

`purpose/scope/material context -> intermediate formation reading -> process/validate/trace-memory-return -> next-cycle material`

