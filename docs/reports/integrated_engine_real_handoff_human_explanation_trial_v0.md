# Integrated Engine Real Handoff Human Explanation Trial v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This document tests a human-readable explanation layer for the formal handoff artifact.

It is not final user-facing wording, not UI copy, not glossary, not patch language, and not external translation guidance.

## 1. explanation boundary

The goal is not to make the easiest possible explanation.

The goal is to make an explanation that remains readable while preserving:

- route
- authority
- state
- boundary
- workspace ownership
- hold / carry-forward / reject distinction

## 2. explanation trial table

| internal reading | human explanation attempt | preserved boundary | flattened risk | do-not-lose note |
|---|---|---|---|---|
| `proposal-only / needs Codex translation` | Gemini material can give us ideas, but it cannot enter the engine as-is. Codex has to check what fits the baseline first. | proposal is not canonical; Codex translation required | could sound like "draft needs review" | proposal-only is an authority state, not quality level |
| Gemini as design clay source | Gemini can make visual material and possible shapes for the interface. Those shapes are raw material. | visual material differs from approved structure | could sound like Gemini is the designer of the final UI | visual strength does not grant core authority |
| Codex as baseline translator | Codex reads the Gemini material and sorts it into usable, needs translation, carry-forward, reject/conflict, or needs user decision. | Codex performs structural filtering | could sound like Codex merely summarizes Gemini | translation includes boundary and collision checks |
| User decision role | The user decides whether a direction becomes a real package, a later candidate, or stays closed. | promotion authority stays with user | could sound like a normal approval click | user opens scope; without that, no promotion |
| Workspace ownership | Gemini works in the proposal area; Codex writes official reports only when the task allows it; scaffold and manifest areas stay closed here. | file location expresses authority and collision prevention | could sound like folder assignment | location controls what can become canonical |
| Collision stop condition | If a Gemini idea would require core drift, runtime truth, read-map changes, or new authority, the flow stops and the idea is held or rejected for core. | stop is a brake protecting baseline | could sound like an error or failure | stop can preserve future value as carry-forward |
| Hold / carry-forward | Some ideas are kept visible because they may matter later, but they are not core now. | hold is not discard; carry-forward is not approval | could collapse into "unused" | held material needs a later gate before promotion |
| Reject / conflict | Some material conflicts with the current baseline and should not be used in core. | conflict differs from hold | could sound like the idea is bad | reject/conflict is about current baseline fit |
| Needs user decision | Some material cannot be classified into action without the user opening a package. | Codex does not self-promote | could sound like Codex is waiting for permission only | user decision is part of route grammar |

## 3. separated human explanation

### Gemini가 하는 일

Gemini는 아이디어와 디자인 재료를 만든다. 여기서 만들어진 것은 바로 엔진의 구조가 아니라, 나중에 걸러볼 수 있는 raw material이다. Gemini가 만든 것이 좋아 보여도 그 자체로 baseline이나 implementation이 되지는 않는다.

Preserved:

- Gemini = proposal / design clay source
- Gemini output = not canonical

Flattened risk:

- "Gemini가 디자인한다"라고만 말하면 최종 구조 권위가 Gemini에게 있는 것처럼 보일 수 있다.

### Codex가 하는 일

Codex는 Gemini material을 현재 integrated-engine baseline에 맞춰 읽는다. 무엇이 지금 쓸 수 있는 시각 리듬인지, 무엇이 번역이 필요한지, 무엇이 carry-forward인지, 무엇이 현재 core와 충돌하는지 나눈다. 이 작업은 단순 요약이 아니라 route, authority, state, boundary를 보존하는 baseline translation이다.

Preserved:

- Codex = baseline translator / canonical report writer under scoped package
- Codex translation = classification and boundary check

Flattened risk:

- "Codex가 Gemini 결과를 정리한다"라고만 하면 validation과 collision check가 사라진다.

### User가 여는 결정 권한

User는 어떤 방향을 실제 package로 열지 결정한다. Gemini material이 있고 Codex classification이 있어도, user가 package를 열기 전에는 scaffold patch, wording patch, extension promotion, external harvest가 시작되지 않는다.

Preserved:

- User = promotion / package opening authority
- package scope controls action

Flattened risk:

- "User approves"라고만 하면 어떤 범위가 열리는지, 무엇은 여전히 닫혀 있는지 흐려진다.

### 아직 hold / carry-forward 상태인 것

Supervisor queue, watcher recommendation, bridge panel, live manifest truth, team/role console dominance, line atlas as center, engine control-room framing은 현재 core가 아니다. 어떤 것은 나중에 쓸 수 있는 carry-forward material이고, 어떤 것은 현재 baseline과 충돌한다.

Preserved:

- hold / carry-forward / reject-conflict separation
- extension promotion remains closed

Flattened risk:

- "아직 안 씀"이라고만 하면 hold와 reject의 차이가 사라진다.

## 4. human explanation stress points

The explanation weakens first at these points:

1. `proposal-only`
   - easy wording wants to say "draft"
   - but proposal-only marks non-canonical status

2. `needs Codex translation`
   - easy wording wants to say "Codex reviews"
   - but translation includes baseline filtering and authority protection

3. `workspace ownership`
   - easy wording wants to say "Gemini folder / Codex folder"
   - but ownership controls write authority and collision prevention

4. `collision stop`
   - easy wording wants to say "stop if problem"
   - but stop is a route brake, not generic problem handling

5. `hold`
   - easy wording wants to say "not used"
   - but hold keeps future value visible without promotion

## 5. trial closeout

The human explanation layer is possible, but only if it keeps four separations explicit:

1. idea proposal vs accepted structure
2. baseline translation vs simple review
3. official recording vs implementation
4. user decision vs automatic promotion

This trial should not be converted into final wording. It is retention evidence for a later bridge lexicon.
