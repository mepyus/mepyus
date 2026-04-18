# Integrated Engine Surface-Local Current Object Focus Layer Patch Note v0

## 1. Verdict

PASS_WITH_NOTE

Each surface now starts with a surface-local current object focus layer under the shared operating spine.

The shared spine keeps the same object visible across User / VectorFL / Engine, and the local focus layer explains how the active surface should read that same object.

## 2. Why This Is Hierarchy Correction, Not Feature Expansion

This patch does not add a new tool, queue, backend, preset, session history, or ingestion path.

The problem was hierarchy:

- the shell-level spine made the current object common
- but each surface still began with its older local panels
- users still had to infer what the same object means on that surface

The correction adds a first-reading layer so the page reads:

```text
shared spine
-> surface-local current object focus
-> existing secondary/support panels
```

## 3. Shared Spine To Local Focus Relationship

The shared spine answers:

- what is the current object?
- what is its route / mark?
- what authority state does it have?
- which surface is currently active?

The surface-local focus answers:

- what does this same object mean here?
- what is this surface allowed to do with it?
- what remains candidate-only?
- what is the next candidate action?

This keeps the object continuous while preserving surface roles.

## 4. User Focus Reading

Added first focus layer:

- title: `현재 객체를 배정/결정 후보로 읽기`
- reads the object as `assignment / decision candidate`
- shows assignment relevance
- shows authority state
- shows next action candidate such as `attach to team/role`

User Surface remains an organization / assignment / decision surface. It does not become the packet evidence owner.

## 5. VectorFL Focus Reading

Added first focus layer:

- title: `현재 객체를 재독해/중재/검증 재료로 읽기`
- reads the object as `reread / mediation material`
- shows packet continuity such as `latest return -> route`
- shows authority state
- shows next action candidate such as route marking or reread

VectorFL remains the mediation surface. It does not become an execution or deposition surface.

## 6. Engine Focus Reading

Added first focus layer:

- title: `현재 객체를 처리/검증/퇴적 재료로 읽기`
- reads the object as `request / validation / deposit material`
- shows execution boundary such as `not executed yet` or `not ingested / not canonical`
- shows authority state
- shows next engine-side candidate action

Engine Surface remains processing / validation / return-material focused. It does not decide canonical promotion.

## 7. What Remains Secondary / Supporting

Existing panels remain in place:

- User: command header, user assignment candidate panel, internal team desk, route/log support
- VectorFL: FlowSummary, CLI packet lane, validation/reread queue, evidence line atlas, inspection
- Engine: CLI return/validation feed, engine mock body

These panels are now downstream of the local focus layer in the reading hierarchy.

## 8. Watchpoints

1. Do not expand the local focus layer into another dashboard.
2. Do not duplicate every detail from the shared spine.
3. Do not imply that a candidate is completed, executed, assigned, ingested, or canonical.
4. Do not move packet evidence ownership to User.
5. Do not move route judgment ownership to Engine.
6. Do not add persistence or history as part of this hierarchy correction.

## 9. Next Smallest Validation Step

Open the UI and switch through:

```text
User -> VectorFL -> Engine
```

Pass condition:

- shared spine remains the same current object
- the first layer in each surface immediately says how that surface reads the object
- authority state remains visible as candidate / not complete / not ingested / not canonical where relevant
- older panels feel secondary rather than competing first-read centers

If this passes, the next work should be real-use validation of one turn across all 3 surfaces. It should not add new features.
