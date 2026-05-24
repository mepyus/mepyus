# Camera/Lens Real-use Round 001 Closeout — 2026-05-09

## 0. Status

- closeout candidate only
- live-use with watch
- not baseline
- not schema
- not registry
- not ontology
- not automation
- not final workflow
- not replacement for user judgment

## 1. One-Paragraph Summary

Camera/Lens moved from conceptual language into practical inspection. Caller Shift Lens worked for script safety / caller boundary judgment, and Metadata-First Lens worked for package navigation / progressive loading. The recovered value is not that Camera/Lens is a finalized method, but that a camera can define the observed surface and a lens can define the active reading question in a way that changes what should be inspected next.

## 2. Working Distinction Confirmed

```text
Camera:
Where / what surface are we observing?

Lens:
How / by what interpretive question are we reading it?
```

This is a working distinction only. It is not a final definition, ontology, registry, or schema.

## 3. Trial A — Caller Shift Lens

Target:
`scripts/cli/space_boundary_lookup_packet.py`

Camera:
operational tool surface

Lens:
Caller Shift Lens

Recovered judgment:

```text
read-only helper is not automatically agent-safe.
Caller shift from human -> Codex-light -> Gemini-heavy -> autonomous agent changes safety.
```

Verdict:
`CALLER_SHIFT_LENS_WORKED_WITH_WATCH`

Evidence basis:
`USER_PROVIDED_SUMMARY` from the recent Caller Shift Lens trial.

What worked:
- The lens separated read/write safety from caller safety.
- It exposed that bounded Codex-light use and autonomous repeated use are different risk classes.
- It made script safety review easier by asking who the tool was implicitly designed for.

Safe scope:
- Use as a candidate script safety review lens.
- Apply to one explicit tool surface at a time.
- Keep caller categories separate: human manual, Codex-light, Gemini-heavy, autonomous agent.

Watch items:
- read-only mistaken as agent-safe
- one script result overgeneralized to all scripts
- filename signal mistaken as safety evidence
- Caller Shift becoming a rigid schema

Missing evidence:
- This closeout did not directly re-inspect the script.
- Additional scripts have not yet been tested under the same lens.

## 4. Trial B — Metadata-First Lens

Target:
`package_003_graphify_compact_feedback/metadata_scan_report.md`

Camera:
large-context navigation surface

Lens:
Metadata-First Lens

Recovered judgment:

```text
metadata is useful as routing / neighbor-selection signal,
but not as final semantic judgment.
```

Verdict:
`METADATA_FIRST_LENS_WORKED_WITH_WATCH`

Evidence basis:
`USER_PROVIDED_SUMMARY` from the metadata-first trial.

What worked:
- Metadata identified the package as bounded.
- Metadata separated what to read next from what to skip.
- Metadata pointed to `analysis_result.md` as the likely semantic neighbor.

What metadata could provide:
- package purpose / scope signal
- deep-read candidate selection
- skip candidates for raw / outbox / stderr except debugging
- progressive loading route

What metadata could not provide:
- Graphify judgment itself
- final closeout or user acceptance
- raw execution behavior
- package-level recovery decision

Watch items:
- metadata mistaken for full understanding
- index entries becoming authority
- shallow reading
- progressive loading becoming under-context

## 5. Trial C — Metadata + One Neighbor

Neighbor:
`analysis_result.md`

Recovered judgment:

```text
metadata_scan_report.md + analysis_result.md worked as a minimal pair:
metadata selected the route;
analysis_result recovered the semantic judgment.
```

Verdict:
`METADATA_PLUS_ONE_NEIGHBOR_WORKED_WITH_WATCH`

Evidence basis:
`OBSERVED_FILE_EVIDENCE` from `analysis_result.md` in the one-neighbor follow-up, plus prior `USER_PROVIDED_SUMMARY` for the metadata selection step.

What worked:
- `analysis_result.md` contained the semantic judgment: Graphify is useful as a metadata-first discovery lens, not as an implementation target.
- The file separated Borrow / Hold / Reject For Now / Boundary.
- One neighbor was enough for the current semantic check.

What remains missing:
- final closeout / user-summary judgment
- raw / outbox / stderr / debug details
- root-cause or execution-behavior evidence

When to stop:
- Stop when the current question is semantic routing or package-level meaning.
- Do not keep adding neighbors after the lens has answered the current question.

When another neighbor is needed:
- Add `package_closeout.md` only if the question becomes final recovery / acceptance.
- Add raw or debug material only if the question becomes execution failure or root cause.

## 6. Reusable Rules

### Rule 1 — Caller Shift Rule

```text
Do not judge tool safety only by read/write behavior.
Also judge by caller type:
human / Codex-light / Gemini-heavy / autonomous agent.
```

Status:
candidate-with-watch

### Rule 2 — Read-only Is Not Agent-safe

```text
A read-only helper may still expose context or become unsafe if called repeatedly by an agent.
```

Status:
candidate-with-watch

### Rule 3 — Metadata Is Routing Signal

```text
Metadata can select the next neighbor, but should not be treated as recovered judgment.
```

Status:
candidate-with-watch

### Rule 4 — Metadata + One Semantic Neighbor

```text
For package navigation, metadata + one semantic neighbor may be enough before reading closeout/raw/debug files.
```

Status:
candidate-with-watch

### Rule 5 — Stop When the Current Question Is Answered

```text
Do not keep adding neighbors after the current lens has recovered enough judgment.
```

Status:
candidate-with-watch

## 7. Compounding Check

This round makes the following easier next time:

- next script safety review: use Caller Shift before deciding whether a helper is LLM/agent-safe.
- next package navigation: read metadata first, then one semantic neighbor if needed.
- next active bundle selection: choose the neighbor that matches the missing layer instead of reading the whole package.
- next Codex instruction: specify camera, lens, target, stop condition, and not-inspected scope.
- next Gemini prompt: ask for lens-specific recovery value, not broad conceptual synthesis.
- next watch item: separate routing signal from semantic judgment and semantic judgment from final authority.

## 8. Watch Items

- Camera/Lens becoming schema
- one script result overgeneralized to all scripts
- metadata mistaken for full understanding
- analysis mistaken for final authority
- progressive loading becoming under-context
- read-only mistaken as safe for autonomous agent use
- examples becoming registry
- user judgment bypassed

## 9. Recommended Next Test

Recommended:
Option A — ASSETS.md mismatch

Purpose:
Test philosophical / usability conflict under different lenses.

Reason:
Caller Shift tested operational safety, and Metadata-First tested package navigation. ASSETS.md mismatch is the better next contrast because it tests whether Camera/Lens can handle a conceptual usability conflict without turning the lens set into a registry or fixed method.

Do not run it by default. Use it only when the next real task needs a philosophy / usability conflict reading.

## 10. Final Verdict

`CAMERA_LENS_REAL_USE_ROUND_CLOSED_WITH_WATCH`

confidence level:
candidate confidence with watch

strongest confirmed value:
Camera/Lens can guide practical inspection by separating observed surface from reading question.

weakest missing evidence:
Only two lens families have been tested in real use, and Trial A is represented here from user-provided summary rather than direct reinspection.

immediate next action:
Use Caller Shift and Metadata-First in real tasks before expanding Camera/Lens into more examples or formal structures.

## 11. Final Note

This closeout ends the first Camera/Lens real-use round.
Next work should use these examples in a real task, not expand them into a registry.
