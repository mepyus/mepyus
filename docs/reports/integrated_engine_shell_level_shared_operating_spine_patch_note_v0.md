# Integrated Engine Shell-Level Shared Operating Spine Patch Note v0

## 1. Verdict

PASS_WITH_NOTE

A thin shell-level shared operating spine was added above the User / VectorFL / Engine surface tabs.

It makes the latest CLI turn readable as the same current operating object across all 3 surfaces without adding a new surface or changing the underlying route/mark mechanics.

## 2. Why This Is Shell-Level Shared Spine, Not A New Surface

The spine is not an independent workspace, dashboard, or fourth surface.

It is a compact shared layer inside `VectorFLIntegrationShell` that reads the same `cliHostState.latest_readable_return` used by existing User / VectorFL / Engine panels.

It does not replace surface-local panels:

- User Surface still handles assignment / decision.
- VectorFL Surface still handles packet formation / reread / mediation.
- Engine Surface still handles processing / return / validation / deposit material.

The spine only answers: "What current object are all surfaces reading right now?"

## 3. What Shared Operating Object Fields Are Now Visible

Added fields:

| field | source |
| --- | --- |
| active turn / session id | latest CLI return session id |
| current purpose | latest CLI return purpose text |
| packet state | derived from latest turn status and marks |
| route / current mark | latest route label or marks |
| authority state | derived from candidate / validation / hold / deposit marks |
| current surface-local role | derived from selected surface |
| next action candidate | derived from selected surface and marks |

The spine remains compact. It does not expose full refs, full prompt, full return, or session history.

## 4. How Authority State Is Clarified

Authority state is now shown as a dedicated field in the shell spine.

Examples:

- `candidate only / unmarked / not canonical`
- `validation target / not complete`
- `engine request candidate / not executed`
- `user assignment candidate / not assigned`
- `deposit candidate / not ingested / not canonical`
- `hold / not advanced`

This is meant to reduce the risk that a route label reads as completion.

## 5. How Surface-Local Role Is Shown

The same current turn is read differently depending on active surface:

- User: `assignment / decision candidate`
- VectorFL: `reread / mediation material`
- Engine: `request / validation / deposit material`

When there is no active turn:

- User reads setup as purpose / assignment setup.
- VectorFL reads setup as packet mediation setup.
- Engine reads setup as waiting for process material.

## 6. What Still Remains Outside The Spine

- formal work packet object registry
- persistent selected current object across sessions
- full lifecycle timeline
- session browsing/history
- automatic route decision
- automatic deposit ingestion
- canonical promotion
- Gemini adapter
- async/background runner

The spine is a shared reading layer, not a state machine.

## 7. Watchpoints

1. Do not add too many fields to the spine.
2. Do not make the spine look like a fourth surface.
3. Do not treat inferred authority state as canonical truth.
4. Do not let `deposit_candidate` read as ingested memory.
5. Do not let `validation_target` read as validation complete.
6. Do not replace surface-local roles; the spine should clarify them.

## 8. Next Smallest Validation Step

Use the main UI and switch across:

```text
User Surface -> VectorFL Surface -> Engine Surface
```

Check whether the same current turn remains visible in the spine while the surface-local role changes.

Pass condition:

- same current object stays visible
- authority state remains clear
- surface role changes without implying completion
- spine feels like a thin shared layer, not a new dashboard

If it passes, the next correction should be user/engine local panel alignment against this spine, not another global layer.
