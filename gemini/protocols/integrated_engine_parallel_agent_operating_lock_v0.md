# Integrated Engine Parallel Agent Operating Lock v0

Date: 2026-04-15

## 0. status

proposal operating lock

This document defines how Codex and Gemini CLI may operate together around the integrated-engine workspace without colliding.

It is stored under `gemini/` intentionally. It is not yet a canonical `docs/reports` baseline. Promote it only after one or more safe parallel-use observations.

## 1. purpose

The purpose is to let Gemini CLI be used actively for design material, user-surface proposals, review, and broad reading while preserving Codex as the baseline translator and canonical editor.

This is not:

- runtime binding
- file watch
- automatic multi-agent orchestration
- scaffold ownership transfer
- docs baseline transfer
- extension promotion
- permission for Gemini to edit core files

## 2. current integrated-engine state to preserve

Current state:

- mode = `stop-and-use / use observation`
- build mode = closed
- patch planning = closed
- patch application = closed
- S1 / S2 / S3 = manually usable under current baseline
- S2 wording watch = `not promoted / watch keep`

Protected central panels:

| surface | central panel | protected reading |
|---|---|---|
| user | `operating_flow_panel` | operating / distribution / decision |
| VectorFL | `maturation_canvas_panel` | mediation / validation / maturation body reading |
| engine | `execution_state_panel` | processing / execution / return-draft |

Protected separations:

- request / return / reflux separation
- anchor / maturation / operating object separation
- support layer stays subordinate
- current loop state is current-position, not full history
- panel connection records are support trace, not live event feed

## 3. role model

Default role split:

| actor | default role | meaning |
|---|---|---|
| User | direction / promotion decision | Decides whether a direction, design, patch, or package should be opened. |
| Codex | VectorFL-side baseline translator and canonical editor | Reads space, protects current baseline, writes canonical docs/patches when explicitly scoped. |
| Gemini CLI | design/user-surface proposal worker and support reviewer | Generates proposal material, design clay, scans, comparisons, and second-opinion reports under `gemini/`. |

Working sentence:

Gemini expands possibility space; Codex filters against the integrated-engine baseline; User decides promotion.

## 4. role switch rule

Roles are task-mode based, not permanent identities.

| task mode | Codex role | Gemini CLI role |
|---|---|---|
| current-state lock / closeout | canonical recorder | read-only reviewer or inactive |
| scaffold patch | bounded patch worker | reviewer / mock supplier only |
| design ideation | baseline translator / filter | design-material generator |
| user-surface proposal | structure guard and translator | operating-flow proposal worker |
| VectorFL interpretation | primary structural interpreter | secondary comparison worker |
| use observation | primary registry / closeout writer | secondary observer under `gemini/` |
| repo scan | consumer / reviewer | read-only scanner |
| implementation | canonical editor | no direct implementation |

Role switching is allowed only if the user's task explicitly names the mode or asks for Gemini/Codex joint use.

## 5. workspace ownership

Hard workspace rule:

| path / domain | owner | other actor permission |
|---|---|---|
| `gemini/` | Gemini proposal workspace | Codex may read/review/edit when asked, but should preserve Gemini provenance. |
| `docs/reports/` | Codex canonical report workspace | Gemini read-only. |
| `runtime/views/` | Codex scaffold workspace | Gemini read-only. |
| `runtime/manifests/` | Codex/sample evidence workspace | Gemini read-only. |
| `vectorfl_status.md` | Codex/current status workspace | Gemini read-only. |
| repo root files | Codex/user scoped only | Gemini read-only. |

Gemini may write only under `gemini/`.

Codex may write outside `gemini/` only when the user has opened a package that permits it.

## 6. Gemini output status

All Gemini outputs are one of:

| status | meaning |
|---|---|
| `proposal-only` | Idea material; not accepted. |
| `needs Codex translation` | Must be filtered against current baseline. |
| `review evidence` | Useful support observation; not canonical by itself. |
| `carry-forward candidate` | Keep for future, not core now. |
| `reject / conflict` | Conflicts with current baseline or guardrails. |

Gemini output is never automatically:

- baseline
- scaffold patch
- docs canonical text
- manifest truth
- extension promotion
- implementation approval

## 7. Codex translation rule

Codex must classify Gemini output before using it:

| classification | action |
|---|---|
| `usable now` | Can be translated into current task output if the task scope allows. |
| `needs translation` | Requires baseline-language conversion before use. |
| `carry-forward` | Preserve as future material; do not implement now. |
| `reject / conflict` | Do not use; record why if relevant. |
| `needs user decision` | Ask or wait for user direction before promotion. |

Codex checks:

- central panel gravity preserved?
- request / return / reflux separation preserved?
- read map unchanged?
- manifest shape unchanged?
- selected-object behavior avoided?
- trace UI avoided?
- runtime binding avoided?
- extension promotion avoided?
- user surface not turned into team console?
- VectorFL not turned into line browser / workflow hub?
- engine not turned into control room / authority surface?

## 8. simultaneous run protocol

When Codex and Gemini run in the same package:

1. User or Codex states the package boundary.
2. Codex identifies whether Gemini is needed.
3. Gemini receives a prompt that includes:
   - read boot packet first
   - write only under `gemini/`
   - output proposal-only / needs Codex translation
   - no core edits
4. Gemini writes a handoff artifact under `gemini/handoffs/` or another scoped `gemini/` subfolder.
5. Codex reads the handoff.
6. Codex classifies each item: usable now / needs translation / carry-forward / reject / needs user decision.
7. Only Codex writes canonical docs or patches, and only if the user task allows it.
8. Closeout records how Gemini material was used or held.

No direct Gemini-to-core path exists.

## 9. handoff artifact format

Preferred handoff path:

```text
gemini/handoffs/<task_id>_gemini_to_codex_handoff_v0.md
```

Required sections:

1. Source prompt
2. Documents read
3. Active task boundary
4. Assumed Gemini role
5. Proposal or review output
6. Baseline-fit notes
7. Drift / conflict candidates
8. Held or rejected ideas
9. Questions for Codex/User
10. Final label: `proposal-only / needs Codex translation`

## 10. Gemini prompt shell

Use this shell for Gemini during parallel operation:

```text
Read gemini/gemini_cli_integrated_engine_boot_packet_v0.md first.
Read gemini/integrated_engine_parallel_agent_operating_lock_v0.md second.

Task:
- [describe task]

Role:
- You are Gemini CLI acting as [design-material generator / user-surface proposal worker / read-only reviewer / repo scanner].

Rules:
- Read broadly if needed.
- Write only under gemini/.
- Do not edit runtime/views, docs/reports, manifests, read maps, repo root, or source files.
- Do not reopen build mode, patch planning, selected-object behavior, trace UI, runtime binding, watcher/supervisor/bridge authority, or extension promotion.
- Preserve:
  - user center = operating_flow_panel
  - VectorFL center = maturation_canvas_panel
  - engine center = execution_state_panel
  - request / return / reflux separation
- Mark output as proposal-only / needs Codex translation.

Output:
1. Gemini intake digest
2. proposal or review material
3. baseline-fit notes
4. drift / conflict candidates
5. held ideas
6. Codex translation questions
```

## 11. collision stop conditions

Stop and do not proceed if:

- Gemini attempts to edit outside `gemini/`
- Gemini output requires `runtime/views/*` edits to make sense
- Gemini output requires manifest or read-map changes
- Gemini output requires selected-object behavior
- Gemini output requires trace UI or denser timeline as core
- Gemini output implies runtime binding or live manifest truth
- Gemini output promotes watcher / supervisor / bridge authority
- Gemini output turns user surface into team/role console
- Gemini output turns VectorFL surface into line browser / workflow hub
- Gemini output turns engine surface into control room or judgment authority
- Codex cannot translate the material without changing current baseline

When a stop condition appears:

- classify as `reject / conflict` or `carry-forward`
- do not implement
- record the reason if the package requires closeout

## 12. allowed task classes

| Gemini task class | allowed now? | condition |
|---|---|---|
| repo scan / folder inventory | yes | write under `gemini/`; no core edits |
| design material generation | yes | proposal-only; needs Codex translation |
| user-surface proposal | yes | keep `operating_flow_panel` gravity |
| visual option comparison | yes | no direct adoption |
| scaffold readability review | yes | read-only |
| Codex patch review | yes | review-only |
| canonical docs writing | no | Codex only unless separately opened by user |
| runtime/scaffold patch | no | Codex only under scoped package |
| manifest/read-map change | no | closed |
| wording patch planning | no by default | only official re-entry/gate package |
| extension promotion | no | promotion gate first |

## 13. promotion path from Gemini material

Gemini material can move toward core only through this path:

```text
Gemini proposal under gemini/
-> Codex translation review
-> user decision or scoped package
-> documentation brief / patch plan
-> bounded implementation if explicitly opened
-> closeout
```

Skipped steps are not allowed.

## 14. relation to current use observation mode

This lock does not reopen build mode.

Current integrated-engine state remains:

- stop-and-use / use observation
- S1/S2/S3 manually usable
- S2 wording watch not promoted
- held features still held

Parallel Gemini/Codex use is allowed only as support for reading, proposal generation, and future option preparation unless the user explicitly opens a bounded build package.

## 15. closeout sentence

Run Gemini and Codex together only with a workspace split: Gemini writes proposal material under `gemini/`, Codex translates against the current integrated-engine baseline, and the user decides what, if anything, gets promoted.
