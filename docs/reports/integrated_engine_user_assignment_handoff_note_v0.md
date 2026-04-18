# Integrated Engine User Assignment Handoff Note v0

## Verdict

PASS

## This Round Goal

Step 4 was to let a VectorFL-routed CLI turn become a User-surface assignment candidate for a selected internal team/role.

This is still not persistence, automatic assignment, approval, execution, or promotion. The goal was only to make the user surface reflect that a CLI return has become work-organization material.

## Modified Files

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`
- `docs/reports/integrated_engine_user_assignment_handoff_note_v0.md`
- `docs/reports/integrated_engine_next_operating_checklist_v0.md`

## What Changed

The User surface now filters CLI turns with:

- `route_label = user_assignment_candidate`
- or mark `user_assignment_candidate`

Those turns appear in two places:

1. `CLI Work Assignment Signal`
   - shows only User-assignment candidate turns instead of treating all CLI returns as user work.

2. `Internal Team Assignment Desk`
   - shows `CLI assignment candidates` under the selected team.
   - lets the user select a target role within the selected internal team.
   - lets the user attach a candidate to that selected role as a local screen-level assignment candidate.
   - records the local attachment in the internal team operation log.

## Why This Is Bounded

The assignment is local UI state only.

It does not write a manifest, does not persist a team registry, does not auto-open an engine request, and does not promote the CLI return. The detailed return remains in VectorFL; the User surface only sees enough to organize work.

## Verification

Build verification:

```text
cd app/ui/integrated_engine
npm run build
```

Result: PASS.

State smoke:

```text
user_assignment_candidate_count: 1
first_candidate: cli_20260416T123507Z_64047d89
route_label: user_assignment_candidate
marks: implementation_return, user_assignment_candidate
```

This confirms a VectorFL-marked CLI turn is now available as a User-surface assignment candidate.

## What Passed

- User surface no longer treats every CLI return as a work assignment candidate.
- Only explicitly routed `user_assignment_candidate` turns enter the assignment area.
- Team/role selection remains on the User surface.
- Detailed reread remains in VectorFL.
- No persistence, new surface, auto-promotion, or engine execution was added.

## Watchpoints

1. Assignment candidate attachment is UI-local; persistence remains closed.
2. Role selection is currently selected-team scoped; future persistence needs a separate gate.
3. User-surface assignment does not yet create an Engine request candidate. That belongs to Step 5.

## Next Small Valid Step

Start Step 5: Engine Request Candidate Handoff.

The next step should let a VectorFL-shaped turn become visible on the Engine surface as a request candidate, without auto-execution.
