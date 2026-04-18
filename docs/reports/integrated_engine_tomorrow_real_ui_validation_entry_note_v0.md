# Integrated Engine Tomorrow Real UI Validation Entry Note v0

## Verdict

READY

## Purpose

Tomorrow should not start by adding more features.

Tomorrow should start by validating whether today's first operating path works in the actual main UI.

## Entry URL

```text
http://127.0.0.1:5173/
```

API server expected:

```text
http://127.0.0.1:8421/
```

## Validation Path

1. Open the main UI.
2. Go to VectorFL Surface.
3. Send one small Codex turn.
4. Confirm latest return is readable without raw file opening.
5. Mark a turn as `user_assignment_candidate`.
6. Go to User Surface.
7. Confirm the candidate appears in User work/assignment area.
8. Attach candidate to a selected internal team role.
9. Mark or use a turn as `engine_request_candidate`.
10. Go to Engine Surface.
11. Confirm it appears as request candidate only.
12. Send it back to VectorFL.
13. Confirm it appears in VectorFL validation/reread queue.
14. Mark one turn as `deposit_candidate`.
15. Confirm candidate artifact says `not_ingested`.

## Pass Criteria

- The user can understand the flow from the screen.
- The user does not need to inspect raw artifact files for first-pass reading.
- Candidate labels do not look like execution completion.
- User / VectorFL / Engine roles stay separated.
- Deposit remains candidate-only.

## If It Fails

Do not open Gemini adapter or package 2.

Record the first actual bottleneck:

- unreadable latest return
- route label confusion
- User assignment candidate not visible
- Engine candidate looks like execution
- VectorFL validation queue unclear
- deposit candidate looks canonical

Then patch only that bottleneck.
