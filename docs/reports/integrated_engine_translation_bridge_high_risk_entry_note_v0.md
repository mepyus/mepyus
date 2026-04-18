# Integrated Engine Translation Bridge High-Risk Entry Note v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This note isolates the high-risk bridge lexicon entries that flatten most easily during human explanation.

It does not create final translations, UI copy, wording patches, scaffold edits, manifest changes, read-map changes, external style harvest, selected-object behavior, trace UI, runtime binding, or extension promotion.

## 1. why these entries are high-risk

The risky entries are not difficult because the words are obscure.

They are difficult because ordinary explanation tries to turn operating states into familiar work-management labels:

- workspace ownership -> folder owner
- hold -> unused
- carry-forward -> backlog
- reject/conflict -> bad idea
- collision stop condition -> error
- watch keep -> TODO

Those replacements erase route, authority, state, or boundary.

## 2. `workspace ownership`

Why it flattens:

- People hear "workspace" as folder or work area.
- They hear "ownership" as responsibility.

What disappears first:

- write authority
- artifact status
- proposal vs canonical boundary
- collision prevention

What must be said first:

- "This tells us what authority the material has."
- Then name the workspace.

Avoid this direction:

- "Gemini owns this folder."
- "Codex owns that folder."
- "This is just file organization."

Safer preservation direction:

- workspace ownership controls whether material is proposal-only, canonical report, scaffold work, manifest evidence, or closed scope.

## 3. `hold`

Why it flattens:

- Ordinary project language treats held items as unused, parked, or rejected.

What disappears first:

- current-scope boundary
- future reread value
- no-promotion state

What must be said first:

- "This is outside the current core/package, but still kept as readable material."

Avoid this direction:

- "We are not using it."
- "It is in backlog."
- "It is not important now."

Safer preservation direction:

- hold preserves future material while blocking current build or promotion.

## 4. `carry-forward`

Why it flattens:

- It sounds like a future task or implicit promise.

What disappears first:

- no current implementation
- no automatic promotion
- later gate requirement

What must be said first:

- "This remains available for future reread, but it has no current operating authority."

Avoid this direction:

- "We'll do it later."
- "It's approved for later."
- "Put it in backlog."

Safer preservation direction:

- carry-forward is preservation without commitment.

## 5. `reject / conflict`

Why it flattens:

- Reject sounds like global evaluation.
- Conflict sounds like failure.

What disappears first:

- scoped baseline reason
- distinction from hold and carry-forward
- future-context possibility

What must be said first:

- "This conflicts with current baseline rules under this package."

Avoid this direction:

- "Bad idea."
- "Wrong."
- "Not useful."

Safer preservation direction:

- reject/conflict records current incompatibility, not universal worthlessness.

## 6. `collision stop condition`

Why it flattens:

- Stop conditions are often heard as errors, blockers, or tool failures.

What disappears first:

- route brake
- baseline protection
- explicit boundary reason
- carry-forward possibility

What must be said first:

- "Continuing would cross a protected boundary."

Avoid this direction:

- "Something went wrong."
- "The task failed."
- "Stop if there is a problem."

Safer preservation direction:

- collision stop protects the baseline by stopping a route before unauthorized core drift happens.

## 7. `watch keep`

Why it flattens:

- Watch lists are often treated as TODOs, bug queues, or low-priority tasks.

What disappears first:

- evidence requirement
- no patch planning
- official re-entry conditions

What must be said first:

- "This remains under observation only; no change is opened."

Avoid this direction:

- "We'll fix it later."
- "Keep it in TODO."
- "This is a patch candidate."

Safer preservation direction:

- watch keep keeps ambiguity visible while requiring stronger evidence before action.

## 8. shared preservation rule

For all six high-risk entries, explain in this order:

1. current operating status
2. authority or boundary protected
3. what remains closed
4. what future condition could reopen it, if any
5. what not to infer

Do not start with the friendly equivalent.

The friendly equivalent is usually where flattening begins.

## 9. closeout sentence

The high-risk entries are safe enough for controlled explanation only when their operating status is stated before any simplified explanation.
