# Integrated Engine Translation Bridge Usage Retention Check v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This document checks whether high-risk bridge lexicon entries survived the current operating mode explanation trial.

It does not create final glossary, UI copy, wording patches, scaffold edits, manifest changes, read-map changes, external style harvest, selected-object behavior, trace UI, runtime binding, or extension promotion.

## 1. high-risk retention matrix

| entry | decision |
|---|---|
| `workspace ownership` | `retained_with_thinness` |
| `hold` | `retained` |
| `carry-forward` | `retained_with_thinness` |
| `reject / conflict` | `retained` |
| `collision stop condition` | `retained` |
| `watch keep` | `retained` |

## 2. `workspace ownership`

Decision:

- `retained_with_thinness`

What survived:

- The explanation tied workspace to artifact authority and provenance.
- It separated `gemini/`, `docs/reports`, `runtime/views`, and `runtime/manifests`.
- It stated that workspace is not just folder responsibility.

What almost got flattened:

- The phrase still naturally invites folder-owner reading.
- The explanation needed repeated support to preserve authority meaning.

What explanatory order helped:

1. current mode
2. authority boundary
3. workspace path examples
4. what the path permits or does not permit
5. what not to infer

What would mislead a user if shortened too much:

- "Gemini owns its folder and Codex owns docs" would erase artifact status and canonicalization boundary.

## 3. `hold`

Decision:

- `retained`

What survived:

- Hold remained current-scope boundary.
- The explanation said held items are outside current core/package, not worthless.
- It kept selected-object, trace UI, runtime binding, read-map changes, extension promotion, and wording patch application closed.

What almost got flattened:

- "Held items remain held" could sound like no future value if not followed by preservation language.

What explanatory order helped:

1. what remains closed
2. why it remains outside current mode
3. future value not erased
4. no current build or promotion

What would mislead a user if shortened too much:

- "Those features are on hold" could sound like backlog or pause, not boundary.

## 4. `carry-forward`

Decision:

- `retained_with_thinness`

What survived:

- Carry-forward was described as useful for later reread but without current operating authority.
- It was separated from approved-later status.

What almost got flattened:

- "Useful for later" can still sound like roadmap commitment.

What explanatory order helped:

1. future reread value
2. no current authority
3. not scheduled
4. later gate required

What would mislead a user if shortened too much:

- "We will carry this forward" may sound like "we will implement this later."

## 5. `reject / conflict`

Decision:

- `retained`

What survived:

- Reject/conflict was separated from hold and carry-forward.
- It was scoped to current baseline or package boundary.
- It was not described as global badness.

What almost got flattened:

- The word "reject" still has strong global judgment pressure.

What explanatory order helped:

1. current baseline conflict
2. package boundary
3. cannot enter core now
4. not universal judgment

What would mislead a user if shortened too much:

- "Rejected" alone would imply the idea is bad or impossible.

## 6. `collision stop condition`

Decision:

- `retained`

What survived:

- Collision stop remained baseline-protection brake.
- The explanation named unauthorized core drift, runtime truth, read-map changes, new authority, and direct Gemini-to-core movement.
- It stated that stop is not an error message.

What almost got flattened:

- "If proposed route would require..." is procedural and can become "if there is a problem" if shortened.

What explanatory order helped:

1. route would cross protected boundary
2. name the boundary
3. stop is brake
4. classify as hold/carry-forward/reject/needs user decision

What would mislead a user if shortened too much:

- "Stop on collision" could sound like runtime error handling.

## 7. `watch keep`

Decision:

- `retained`

What survived:

- Watch keep stayed observation-only.
- It was tied to `not promoted`.
- It did not become patch planning.
- Re-entry conditions were named.

What almost got flattened:

- "Current watch items" can sound like bug watch.

What explanatory order helped:

1. not promoted status
2. visible during use
3. no patch planning
4. official re-entry conditions

What would mislead a user if shortened too much:

- "Watch these items" could sound like TODO or patch queue.

## 8. entries strengthened by usage

Stronger after this trial:

- `watch keep`
  - because re-entry conditions make it clearly observation-only.
- `collision stop condition`
  - because naming the protected boundary keeps it from becoming error handling.
- `hold`
  - because listing closed features shows current-scope boundary.

## 9. entries still fragile

Still fragile:

- `workspace ownership`
  - needs repeated authority/provenance framing.
- `carry-forward`
  - can still sound like commitment if "future" is overemphasized.
- `reject / conflict`
  - retained here, but the word "reject" remains semantically harsh.

## 10. next reread candidates

Next lexicon reread should focus on:

- `workspace ownership`
- `carry-forward`
- `reject / conflict`

Do not add new terms before these are stable in another usage context.

## 11. retention closeout

The high-risk entries survived the usage trial when explanation followed the required order:

```text
current operating status
-> protected authority/boundary
-> what remains closed
-> possible re-entry/decision
-> what not to infer
```

The order is not optional; it is what prevented flattening.
