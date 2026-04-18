# Integrated Engine Surface Information Exposure Reread Note v0

## 1. Verdict

PASS_WITH_NOTE

The shared operating spine is useful as an orientation layer, but it must not become a place where every surface sees all space information.

The reason for three surfaces is not duplication. The reason is role-filtered exposure:

```text
same current work object
-> different surface responsibility
-> different information density
-> different allowed action
```

## 2. Why The Three Surfaces Exist

The three surfaces exist because the user should not carry the full internal space at once.

If every page shows all packet details, all evidence, all authority states, all route candidates, all engine outputs, and all trace records, then the UI collapses back into a single overloaded workspace.

The body split protects the user from that collapse:

- User Surface should reduce the object to purpose, assignment, decision, and approval relevance.
- VectorFL Surface should expand the object enough for reread, evidence, mediation, route, and validation.
- Engine Surface should reduce the object to input, process, return material, validation, extraction, and deposit candidate.

The surfaces are not three copies of the same state. They are three role-specific readings of the same state.

## 3. What Should Be Shared Everywhere

Only the minimum orientation fields should be shared everywhere:

- current object identity
- current purpose in short form
- route / mark candidate
- authority state
- evidence readiness summary
- next surface-local action candidate

This is enough to prevent disorientation.

It is not enough to perform mediation, assignment, or processing. Those should remain surface-local.

## 4. What Should Not Be Shared Everywhere

The following should not be fully exposed on every page:

- full evidence bundle
- full refs list
- full prompt
- full return text
- line atlas
- engine process detail
- deposit candidate body
- mark history
- full trace / logs
- team/role detail
- internal language harvest detail

These are not forbidden. They should appear only where their surface role needs them.

## 5. Surface Exposure Rule

### User Surface

Primary exposure:

- What is the user trying to do?
- What task or role should receive it?
- What decision is needed?
- Is this still candidate-only?
- Is the evidence ready enough to assign or decide?

Should not expose by default:

- full evidence details
- full VectorFL packet formation
- full Engine return internals
- raw CLI logs

User Surface should answer:

```text
Can I assign, decide, hold, or send this back for mediation?
```

### VectorFL Surface

Primary exposure:

- What is the evidence bundle?
- What is missing or thin?
- What route is appropriate?
- What must be reread?
- What guard applies?
- What should be sent to Codex or returned to User/Engine?

VectorFL can show the highest density because it is the mediation surface.

VectorFL Surface should answer:

```text
Is this work package well-formed enough to move, or should it be reread/repaired?
```

### Engine Surface

Primary exposure:

- What input/request material arrived?
- What process stage is relevant?
- What output/return material exists?
- What is validation or extraction material?
- Is this deposit candidate, not canonical memory?

Should not expose by default:

- User assignment structure
- full VectorFL evidence atlas
- surface-wide mediation reasoning

Engine Surface should answer:

```text
What should be processed, what came back, and what is only candidate material?
```

## 6. Current UI Risk

The recent shared spine and evidence gate continuity patches solved one real problem:

- the same current object no longer disappears across tabs.

But they create a new risk:

- evidence readiness and packet details may start appearing like common global data that every surface must inspect.

That is not the desired endpoint.

The shared spine should be a thin navigation/orientation layer. It should not become a global dashboard.

## 7. Corrected Principle

The corrected principle is:

```text
common identity, local density
```

Meaning:

- All surfaces share enough object identity to avoid losing the turn.
- Each surface expands only the information needed for its responsibility.
- Detailed evidence belongs mostly to VectorFL.
- Assignment and decision context belongs mostly to User.
- Process and return material belongs mostly to Engine.

## 8. Implication For Next Work

The next correction should not add more shared fields.

The next correction should define exposure budgets:

- shared spine = minimal orientation
- surface-local focus = one-sentence role translation
- surface body = role-specific detail
- support panels = expandable detail only when needed

This should happen before any multi-work board.

If a multi-work board is built before this rule is stable, it will likely multiply overload across many work objects.

## 9. Watchpoints

1. Do not let shared spine become a universal state dashboard.
2. Do not make User Surface read like VectorFL evidence workspace.
3. Do not make Engine Surface read like VectorFL mediation workspace.
4. Do not hide authority state; it is one of the few things that must remain shared.
5. Do not remove surface-local detail; reduce it to the right surface.
6. Do not build multi-work view until single-work exposure density is stable.

## 10. Single Next Correction

Create a surface exposure budget correction:

```text
shared spine: identity / route / authority / evidence readiness only
User: assignment-decision detail
VectorFL: evidence-mediation detail
Engine: process-return detail
```

This is a hierarchy and information-density correction, not a new feature.
