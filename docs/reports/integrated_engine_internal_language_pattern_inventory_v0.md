# Integrated Engine Internal Language Pattern Inventory v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This inventory groups harvested internal language into recurring patterns.

It does not convert the patterns into user-facing wording, patch language, UI labels, scaffold changes, manifest changes, read-map changes, or extension proposals.

## 1. purpose

The harvest shows that the integrated-engine language is not mainly a term list. It is a set of repeated movements:

- route movement
- authority and boundary movement
- state transition and lockback movement
- reread and recovery movement
- support dependency movement
- collaboration handoff movement

This document groups those movements so later bridge work can preserve them instead of flattening them.

## 2. route pattern

Representative phrases:

- `request -> return -> reflux`
- `user request -> VectorFL review -> engine processing / external support`
- `engine result -> VectorFL validation -> user decision / reflux / reprocess`
- `VectorFL maturation signal -> user organization -> engine follow-up`
- `anchor drift -> reprocess / rewind`
- `user_decision_or_vectorfl_recheck`

What repeats:

- A route is not just motion; it carries source, target, reason, and validation context.
- Request starts a shaped route, not raw execution.
- Return is routed material for validation, not completion.
- Reflux preserves future maturation value, not failure residue.
- Follow-up and reprocess are special route forms, but both require recorded cause.

What must not be flattened:

- Request, return, and reflux must not collapse into a generic "task update."
- Follow-up must not look like a fresh user-origin request when it begins from VectorFL maturation.
- Reprocess must not look like accidental retry or execution failure.
- Reflux must not be translated as simple archive or rollback.

What risks distortion if simplified:

- "Send work to engine" erases VectorFL review and anti-bypass.
- "Engine finishes" erases return validation.
- "Save for later" erases reflux route/reason.
- "Redo it" erases anchor drift and validation-based rewind.

## 3. authority / boundary pattern

Representative phrases:

- `user surface is operating / distribution / decision`
- `VectorFL surface is mediation / validation / maturation`
- `engine surface is processing / execution / return-draft`
- `proposal-only / needs Codex translation`
- `Gemini expands possibility space; Codex filters against baseline; User decides promotion`
- `workspace ownership`
- `no direct Gemini-to-core path`
- `collision stop condition`

What repeats:

- Authority is scoped by role and surface.
- Processing authority is not validation authority.
- Proposal authority is not promotion authority.
- Workspace ownership is part of the authority model, not just file hygiene.
- Core entry requires translation, classification, and user/scoped package permission.

What must not be flattened:

- Gemini proposal material must not be read as accepted baseline.
- Codex translation must not be read as autonomous promotion authority.
- User surface decision must not become semantic maturation authority.
- Engine processing must not become judgment authority.

What risks distortion if simplified:

- "Gemini designs, Codex implements" is too broad; Gemini outputs are proposal-only.
- "Codex decides" erases user promotion authority.
- "Engine validates" erases VectorFL return validation.
- "Workspace rule" sounds bureaucratic unless the authority boundary is preserved.

## 4. state transition pattern

Representative phrases:

- `current_loop_state`
- `current-slot, not full history`
- `closed means current-loop closure, not permanent deletion`
- `hold`
- `not promoted`
- `watch keep`
- `closeout`
- `stop-and-use / use observation`
- `build mode closed`

What repeats:

- State terms often mean "where this loop stands now," not total truth.
- Hold/watch states keep material visible without opening action.
- Closeout records what is locked, watched, held, or closed.
- PASS_WITH_NOTE states usable baseline with explicitly retained thinness.

What must not be flattened:

- `current_loop_state` must not become full timeline.
- `hold` must not become rejection.
- `not promoted` must not become ignored.
- `watch keep` must not become patch planning.
- `closed` must not become permanent deletion.

What risks distortion if simplified:

- "Current state" can imply full history unless connection records are mentioned.
- "Needs watching" can sound like a bug queue unless promotion gate remains closed.
- "Closed" can sound like final lock unless current-loop closure is preserved.

## 5. reread recovery pattern

Representative phrases:

- `blind first-pass ambiguity`
- `supported reread recovers`
- `support reread recovery`
- `manual reread through same panel-role grammar`
- `first-fixture scaffold mapping`
- `recoverable first-pass ambiguity`

What repeats:

- A first-pass reading can be thin without being wrong.
- Support packets, connection records, and panel-role grammar can restore intended meaning.
- Recoverable ambiguity remains watch evidence, not patch evidence.
- Use observation separates "hard to read once" from "persistent confusion."

What must not be flattened:

- Recoverability must not be treated as proof that wording is perfect.
- First-pass ambiguity must not be treated as immediate patch requirement.
- Manual support reread must not be confused with runtime trace UI.

What risks distortion if simplified:

- "It confused me once" can over-trigger patch planning.
- "It recovers" can understate actual use-time friction.
- "Use support records" can sound like missing feature demand unless fixture scope is preserved.

## 6. support dependency pattern

Representative phrases:

- `support-dependent meaning`
- `core-support trace boundary`
- `connection records for route reconstruction`
- `support layer stays subordinate`
- `anchor_context_panel as support brake`
- `evidence_history_panel primary record plus supporting trace`
- `fixture-scope limitation`

What repeats:

- Some meaning is intentionally recovered by reading support material after the central panel.
- Support can have operational force without becoming the center.
- Trace can support route reading without becoming a full timeline or selected-object UI.
- Fixture scope explains sample coverage limits without changing scaffold read maps.

What must not be flattened:

- Support layer must not be promoted to core because it has operational relevance.
- Anchor support must not become the maturation body.
- Evidence history must not be read as live event feed.
- Fixture limitations must not be mistaken for failed structure.

What risks distortion if simplified:

- "Support panel" can sound optional decoration even when it carries a brake reason.
- "Trace" can imply dense interactive history.
- "Evidence" can imply canonical live truth if runtime binding is assumed.

## 7. collaboration handoff pattern

Representative phrases:

- `proposal-only`
- `needs Codex translation`
- `design clay`
- `Codex baseline translator`
- `Gemini design/user-surface proposal worker`
- `User decides promotion`
- `Gemini may write only under gemini/`
- `Codex writes canonical docs or patches only if user task allows`

What repeats:

- Collaboration is a routed handoff, not simultaneous authority sharing.
- Gemini can broaden material but cannot enter core directly.
- Codex can translate and record but must stay within scoped package authority.
- User promotion decision remains the final gate.

What must not be flattened:

- Gemini output is not a second source of truth.
- Codex filtering is not the same as user approval.
- Design clay must not be copied directly into scaffold structure.
- Active parallel use must not bypass workspace ownership.

What risks distortion if simplified:

- "Use Gemini for design" can become uncontrolled mock adoption.
- "Codex checks Gemini" can hide that some outputs should remain carry-forward.
- "Together" can imply both agents edit the same files unless ownership is explicit.

## 8. inventory closeout

The recurring patterns point to an internal grammar built around:

- route with reason
- authority with boundary
- state with lockback
- ambiguity with supported reread
- support with subordination
- handoff with translation before promotion

These patterns are candidates for the next grammar layer, not final public language.
