# Integrated Engine Provisional Human Explanation Guide v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This guide locks the provisional explanation order for human-readable integrated-engine explanations.

It is not final wording, UI copy, glossary replacement, wording patch source, scaffold work, manifest work, read-map work, external translation harvest, selected-object behavior, trace UI, runtime binding, or extension promotion.

## 1. purpose

The purpose of this guide is to help explain integrated-engine internal language to a human reader without losing:

- route
- authority
- state
- boundary
- re-entry condition
- what remains closed

The guide exists because the bridge lexicon usage trial showed that high-risk terms survive only when the explanation follows a protected order.

## 2. scope

This guide may be used for:

- integrated engine operating mode explanation
- Gemini/Codex handoff explanation
- S3 drift / reprocess / reflux explanation
- internal-to-human bridge explanation draft

This guide must not be used for:

- UI final label writing
- wording patch source
- final glossary replacement
- baseline term overwrite
- final user-facing copy
- external style-rule import

## 3. official explanation order

Use this order before simplifying terms:

1. current operating status
2. protected authority / boundary
3. what remains closed
4. possible re-entry / decision condition
5. what not to infer

This order is part of the preservation rule.

Do not begin with the friendly equivalent. The friendly equivalent is usually where flattening starts.

## 4. order details

### 4.1 current operating status

State the current mode, scenario, or route position first.

Examples of status types:

- `stop-and-use / use observation`
- `proposal-only`
- `not promoted / watch keep`
- `hold`
- `return validation`
- `drift / reprocess`

Purpose:

- prevent the explanation from sounding like immediate action
- anchor the reader before any simplified bridge language appears

### 4.2 protected authority / boundary

Name what authority or boundary is being protected.

Examples:

- user opens or does not open a package
- Codex translates/classifies against baseline when scoped
- Gemini material remains proposal-side
- VectorFL validates return/drift/reflux route
- scaffold, manifest, and read-map areas remain closed unless explicitly opened

Purpose:

- prevent proposal material from becoming canonical
- prevent support material from becoming core
- prevent explanation from becoming implicit permission

### 4.3 what remains closed

List the routes, files, modes, or features that do not open under the current explanation.

Common closed items:

- build mode
- patch planning
- patch application
- scaffold edits
- manifest shape changes
- `PANEL_MANIFEST_READ_MAP` changes
- selected-object behavior
- trace UI
- runtime binding
- extension promotion
- final glossary / UI copy

Purpose:

- keep hold/watch/carry-forward from becoming action
- keep explanation from becoming implementation scope

### 4.4 possible re-entry / decision condition

Name the condition that could reopen a route later, if any.

Examples:

- user opens a scoped package
- cross-scenario recurrence appears
- natural-use ambiguity accumulates
- supported reread recovery weakens
- scenario reading is actually blocked
- promotion gate evidence is created

Purpose:

- distinguish current closure from permanent rejection
- distinguish future readability from scheduled work

### 4.5 what not to infer

Close the explanation by naming the common false readings.

Examples:

- `watch keep` is not a patch queue
- `hold` is not discard
- `carry-forward` is not approved-later work
- `reject / conflict` is not global badness
- `collision stop condition` is not an error
- `workspace ownership` is not folder ownership
- `proposal-only` is not low-quality draft

Purpose:

- protect high-risk terms after the bridge explanation has made them easier to read

## 5. writing principles

- Bridge is allowed, flattening is not.
- Explanation may become easier, but operational meaning must survive.
- Current status and authority boundary must come before friendly simplification.
- `hold`, `carry-forward`, `reject / conflict`, and `watch keep` must not be reduced to project-management language.
- `workspace ownership` must be explained as authority/provenance before path or folder examples.
- `collision stop condition` must be explained as boundary brake before problem/error language appears.
- Skeletons may be reused, but they are not final copy.

## 6. operating mode explanation skeleton

Use this when explaining the current integrated-engine operating state.

```text
[current operating status]
The current mode is [mode/status]. [What is usable now] is available, while [build/patch/promotion paths] are not open.

[protected authority / boundary]
[Who can open the next package] holds the route-opening authority. [Support/proposal/classification material] does not enter core unless [translation/classification/decision condition] is met.

[what remains closed]
The following remain closed in this explanation: [closed mode/file/feature list].

[possible re-entry / decision condition]
This can reopen only if [official re-entry evidence or user-scoped package condition].

[what not to infer]
Do not infer [false action], [false promotion], or [false rejection]. [Watch/hold/carry-forward] means [state-preserving reading], not [flattened reading].
```

Notes:

- Put usable-now and closed-now in the same explanation.
- Do not let `stop-and-use` sound like project pause.
- Do not let `watch keep` sound like patch planning.

## 7. Gemini/Codex handoff explanation skeleton

Use this when explaining Gemini material, Codex translation, and user package-opening authority.

```text
[current operating status]
This handoff material is currently [proposal-only / needs Codex translation / documentation-only / other status].

[protected authority / boundary]
Gemini provides [proposal/design clay/support material]. Codex may [translate/classify/record] only within [scoped package]. The user controls whether [implementation/promotion/external harvest/new package] opens.

[what remains closed]
The handoff does not open [scaffold edits], [manifest/read-map changes], [runtime binding], [extension promotion], or [final glossary/UI wording].

[possible re-entry / decision condition]
The material can move only if [Codex classification outcome] and [user decision/package condition] permit it.

[what not to infer]
Do not infer that proposal material is canonical, that Codex translation is simple relay, or that workspace ownership is folder responsibility.
```

Notes:

- Separate idea proposal, baseline translation, official recording, and user decision.
- Do not describe Gemini visual strength as structural authority.
- Do not describe Codex translation as summary or cleanup.

## 8. drift / reprocess / reflux explanation skeleton

Use this when explaining S3 or any anchor-drift route.

```text
[current operating status]
The route is at [return validation / anchor check / drift detected / reprocess / reflux] rather than closure.

[protected authority / boundary]
VectorFL is protecting [anchor fit / validation route / user-decision boundary]. Engine output is return material, not final completion.

[what remains closed]
The route does not move to [user decision / closure / final acceptance] while [drift reason] remains unresolved.

[possible re-entry / decision condition]
The route can continue through [engine reprocess / user reorganization / reflux / user decision] only after [validation or anchor-fit condition].

[what not to infer]
Do not infer that drift is only a warning, that reprocess is failure, or that reflux is archive. These are route-control states.
```

Notes:

- Say the route consequence together with the drift reason.
- Keep `anchor drift` as operational brake, not a descriptive label.
- Keep `reflux` as active maturation route, not passive storage.

## 9. minimal use rule

When time is short, do not drop the order. Compress inside each step instead:

```text
Status -> boundary -> closed scope -> reopen condition -> false inference to avoid.
```

If an explanation cannot preserve all five steps, it should remain an internal note rather than become human-facing bridge text.

## 10. guide closeout

This guide is reusable as a provisional explanation structure.

It does not replace the bridge lexicon, the v1 candidate documents, the current use-state registry, or the promotion gate. It only tells how to explain those materials without flattening their route, authority, state, and boundary roles.
