# Integrated Engine VectorFL Current Work Packet Formation Layer Patch Note v0

## 1. Verdict

PASS_WITH_NOTE

The VectorFL surface now exposes a bounded current work packet formation layer before `Send Codex Turn`.

This patch does not complete automatic packet generation. It makes the packet-forming responsibility visible and reduces the chance that the CLI panel reads as a plain prompt box.

## 2. Why This Is Structural Correction, Not Input Convenience Patch

The problem was not only that the user had to paste context refs.

The structural gap was that the first CLI turn did not show itself as an integrated-engine work packet. The user was silently assembling:

- purpose
- governing locks
- evidence refs
- task lens
- do / do-not guard
- expected return shape
- next route candidate
- internal search usage

The patch moves these items into a visible VectorFL mediation layer. It does not hide manual work or pretend that the engine has fully automated packet formation.

## 3. What Was Added To The VectorFL Surface

Changed file:

- `app/ui/integrated_engine/CliHostControlPanel.tsx`

Added:

- a `current work packet formation` layer inside the VectorFL CLI conversation panel
- derived packet status from existing `purpose`, `taskType`, `contextRefs`, and `promptPayload`
- provided / inferred / missing / guard-active status badges
- packet-to-latest-return continuity preview
- packet summary injected into the Codex turn prompt before the existing user-facing purpose and message

No new surface, API, backend adapter, registry, or persistence layer was added.

## 4. Which Packet Elements Are Now Visible

| element | current visibility |
| --- | --- |
| user purpose | shown as `current packet purpose`; marked provided/missing |
| active governing locks | derived from context refs when lock/status docs are present; otherwise fixed body / CLI on-top boundary is shown as inferred |
| evidence / source pointer bundle | bounded context refs are shown as `current evidence bundle`, not only as file list input |
| task lens | task type is shown as packet lens |
| do / do-not guard | read-only, no promotion, no ingestion, no canonicalization guards are shown |
| expected return shape | inferred from prompt/task type as conflict check, route judgment, structured summary, validation finding, inspection summary, reread judgment, or bounded operating summary |
| next route candidate | inferred as VectorFL reread / validation target / user assignment candidate / engine request candidate / deposit candidate / hold |
| internal search usage | shown as refs-based reread when refs exist, otherwise not specified |

## 5. What Still Remains Manual

- The user still writes or edits the purpose.
- The user still provides or corrects evidence/source refs.
- The route candidate is inferred, not authoritative.
- Final route approval remains manual.
- Promotion, deposit, and canonicalization decisions remain manual.
- Internal search is currently visible as a refs-based reread flag, not a real search/selection engine.

This is intentional. The layer should reveal current manual assembly instead of hiding it.

## 6. What Is Intentionally Deferred

- context preset system
- automatic packet generation from current state assets
- formal operating object registry
- persistent packet history
- Gemini adapter
- async/background run support
- deposit ingestion automation
- page promotion logic
- final glossary or broad UI copy translation

## 7. Watchpoints

1. Do not let this become only a prettier prompt panel.
2. Do not treat inferred route as execution completion.
3. Do not treat inferred locks as proof that all relevant source material was read.
4. Do not hide missing refs or manual decisions.
5. Do not move packet ownership to CLI. VectorFL forms and mediates; CLI executes.

## 8. Next Smallest Validation Step

Open the main UI and inspect the VectorFL surface:

1. confirm that `current work packet formation` appears before `Send Codex Turn`
2. send one small read-only Codex turn
3. confirm that the current packet and latest return can be read as one flow
4. note whether the user still has to mentally assemble any packet field not shown in the layer

If this passes, the next correction should be a bounded read of whether this layer should receive a small source/lock bundle helper. It should not jump directly to a broad preset system.
