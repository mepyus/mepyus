# Integrated Engine High-Risk Explanation Sequence Note v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This note records how to explain high-risk bridge entries without flattening them.

It does not create final wording, UI copy, wording patches, scaffold edits, manifest changes, read-map changes, external harvest, selected-object behavior, trace UI, runtime binding, or extension promotion.

## 1. shared sequence

For each high-risk entry, explain in this order:

1. first sentence protects operating status or authority
2. second sentence clarifies the specific boundary
3. state what remains closed
4. state what not to imply
5. name the common flattening mistake

Do not start with the project-management equivalent.

## 2. `workspace ownership`

First sentence should protect:

- authority and provenance before folder/path.
- Explain that the material's workspace affects what authority the artifact has.

Second sentence should clarify:

- whether the material is proposal-only, canonical report, scaffold, manifest evidence, or closed scope.
- Codex/Gemini/User roles should be named as authority roles, not folder responsibilities.

What must remain closed:

- direct Gemini-to-core movement
- proposal material acting as canonical output
- scaffold or manifest writes without scoped package
- workspace path being treated as permission by itself

What not to imply:

- that Gemini owns a folder and Codex owns another folder in a simple responsibility sense
- that location alone makes material approved
- that `docs/reports` always means final authority

Common flattening mistake:

- workspace ownership becomes folder owner, owner field, or repo organization.

Sequence reminder:

- say "what authority this material has" before saying "where the material lives."

## 3. `hold`

First sentence should protect:

- current-scope boundary.
- Explain that the item is outside the current core/package while still preserved for future reading.

Second sentence should clarify:

- hold blocks current build, patch, or promotion.
- hold does not erase value or future relevance.

What must remain closed:

- current implementation
- extension promotion
- patch planning
- final wording or glossary movement
- treating held material as already accepted future work

What not to imply:

- that the item is discarded
- that it is unimportant
- that it is a low-priority task waiting in backlog

Common flattening mistake:

- hold becomes unused, backlog, parked, or "not doing it now."

Sequence reminder:

- say "outside current package but preserved" before saying "not active."

## 4. `carry-forward`

First sentence should protect:

- future readability without current authority.
- Explain that material remains available for later reread but has no current operating authority.

Second sentence should clarify:

- carry-forward is preservation without commitment.
- later movement requires a gate, evidence, or user-scoped package.

What must remain closed:

- automatic promotion
- scheduled implementation
- roadmap commitment
- assumption that future value equals future approval

What not to imply:

- that the team will implement it later
- that it is already approved
- that it is merely a backlog item

Common flattening mistake:

- carry-forward becomes approved later, TODO, roadmap item, or deferred feature.

Sequence reminder:

- say "kept readable" and "no current authority" together.

## 5. `reject / conflict`

First sentence should protect:

- scoped baseline incompatibility.
- Explain that the material conflicts with the current baseline or package boundary.

Second sentence should clarify:

- reject/conflict is not global evaluation.
- it differs from hold and carry-forward because the current route cannot safely admit it.

What must remain closed:

- current-core entry
- direct implementation
- treating the material as usable-now
- removing the conflict reason

What not to imply:

- that the idea is bad in every context
- that it has no possible future value
- that conflict means tool or agent failure

Common flattening mistake:

- reject/conflict becomes bad idea, wrong, useless, failed, or impossible.

Sequence reminder:

- name the current rule it conflicts with before using the word reject.

## 6. `collision stop condition`

First sentence should protect:

- route brake and baseline protection.
- Explain that continuing would cross a protected boundary.

Second sentence should clarify:

- the specific boundary: unauthorized core drift, runtime truth, read-map change, new authority, direct Gemini-to-core movement, or parallel write conflict.

What must remain closed:

- the unsafe route
- automatic continuation
- silent conversion of proposal into core
- implementation without user-scoped package

What not to imply:

- that a tool crashed
- that the task failed generally
- that any problem is a collision stop

Common flattening mistake:

- collision stop condition becomes error handling, bug, failure, or generic blocker.

Sequence reminder:

- state the boundary crossing first, then classify the result as hold, carry-forward, reject/conflict, or needs user decision.

## 7. `watch keep`

First sentence should protect:

- observation-only state.
- Explain that the candidate remains visible but no change is opened.

Second sentence should clarify:

- watch keep requires stronger evidence before wording gate or patch planning reopens.
- it may coexist with `not promoted`.

What must remain closed:

- wording patch planning
- patch application
- build mode
- treating one scenario's recoverable ambiguity as enough evidence

What not to imply:

- that the item is a TODO
- that a patch is expected later
- that a bug queue has been opened

Common flattening mistake:

- watch keep becomes TODO, patch candidate, bug watch, or low-priority backlog.

Sequence reminder:

- say "observation only" before naming what evidence could reopen the gate.

## 8. cross-entry warning

The main flattening pattern is stable:

- authority becomes assignment
- state becomes task management
- boundary becomes problem/error
- future readability becomes roadmap
- scoped conflict becomes global judgment

When a high-risk entry starts sounding smoother than the boundary it protects, return to the five-step explanation order.

## 9. sequence closeout

These entries are explainable, but only if status and boundary come before friendly language.

If the explanation starts with backlog, owner, error, TODO, bad idea, or later work, the entry has already flattened.
