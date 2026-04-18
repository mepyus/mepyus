# Integrated Engine Product Surface Reframe Worklog v0

## Phase 1 - Product-Surface Policy
Attempted: locked the policy for one-package focus, activity rail, digest support, and inspector separation.

Why: the current screen had working structure but still exposed too much process density by default.

Produced:

- `docs/specs/integrated_engine_product_surface_reframe_v0.md`
- `docs/reports/integrated_engine_activity_rail_and_digest_support_policy_v0.md`

Validation result: PASS_WITH_NOTE. The policy stays within one-handler scope and avoids second-handler, team, bridge, or automation expansion.

Remaining risk: policy can still be overread as a complete product redesign if separated from the guardrails.

Intentionally not done: no new shell, no new handler, no schema expansion.

## Phase 2 - UI Reframe
Attempted: updated `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`.

Why: the UI needed an actual visible separation between current object, event movement, digest support, and deep inspector.

Produced:

- `ActivityRail` component;
- `DigestSupportGrid` component;
- per-surface digest cues;
- live activity events from package lifecycle, latest CLI turn, VectorFL handoff queue, and packet draft state;
- User assignment detail demoted to inspector;
- VectorFL reread queue detail demoted behind support disclosure;
- Engine digest support added before current-object support.

Validation result: PASS_WITH_NOTE. `npm run build` passed.

Remaining risk: `EngineCliReturnPanel` and `CliHostControlPanel` can still feel dense because they remain operational cards.

Intentionally not done: no component split into a new shell, no backend change, no second handler.

## Phase 3 - One-Handler Usability Validation
Attempted: validated the one-handler product surface against User / VectorFL / Engine roles.

Produced:

- `docs/reports/integrated_engine_product_surface_reframe_validation_note_v0.md`
- `docs/reports/integrated_engine_one_handler_product_surface_run_note_v0.md`

Validation result: PASS_WITH_NOTE. The package is easier to follow and activity is more visible, but some support remains dense when expanded.

Remaining risk: users may still expect the session strip to behave like a live terminal unless backend/session feedback is made more explicit.

Intentionally not done: no CLI automation or orchestration promise.

## Phase 4 - Closeout
Attempted: closed the package with a conservative judgment.

Produced:

- `docs/reports/integrated_engine_product_surface_reframe_closeout_note_v0.md`

Validation result: PASS_WITH_NOTE. The surface changed in kind enough to be more usable, but product maturity is not fully claimed.

Remaining risk: polishing pressure could hide the fact that this is still a one-handler pilot.

Intentionally not done: no expansion to a team dashboard or second handler.
