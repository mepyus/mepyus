# Gemini CLI and Codex Collaboration Scope v0

Date: 2026-04-15

## 0. purpose

This document defines how Gemini CLI and Codex can be used together on the integrated engine without colliding.

It is a local Gemini-side coordination note. It does not change the current integrated-engine baseline and does not authorize scaffold, manifest, read-map, runtime, selected-object, trace UI, or extension work.

## 1. current need

The integrated engine needs two kinds of support:

1. Baseline-safe structural interpretation and implementation.
2. Fresh design material and user-facing operating-flow proposals.

Codex is currently stronger for:

- canonical workspace edits
- baseline translation
- closeout notes
- scaffold patches
- read-map and manifest boundary protection
- turning accepted material into repo artifacts

Gemini CLI may be useful for:

- design-material generation
- visual alternatives
- user-surface flow proposals
- mock prompt drafting
- broad repo scan
- second-opinion review
- source-backed comparison

## 2. role model

Default model:

| role | primary actor | meaning |
|---|---|---|
| VectorFL-side structural interpreter | Codex | Reads space, current baseline, drift, hold/watch, and translates outputs into safe packages. |
| user-surface proposal worker | Gemini CLI | Generates operating-flow, request-shaping, and design proposal material when asked. |
| engine worker / canonical editor | Codex | Applies approved patches and writes canonical reports outside `gemini/`. |
| design clay source | Gemini CLI | Produces mock or visual material that can later be translated, filtered, or rejected. |

This split can change per task, but only if the task explicitly says so.

## 3. Gemini as design material generator

Gemini may be asked to produce:

- visual grammar options
- rough surface layout alternatives
- user-facing request / operating-flow copy options
- mock component concepts
- design comparison notes
- prompt packets for Gemini Web / Gemini CLI

Allowed write location:

- `gemini/` only

Preferred folders:

- `gemini/reports/`
- `gemini/briefs/`
- `gemini/mock_prompts/`
- `gemini/design_materials/`
- `gemini/checklists/`

Status of Gemini design output:

- proposal only
- not implementation
- not baseline
- not approved UI
- needs Codex/user translation before use

## 4. Codex as baseline translator

Codex should translate Gemini output by checking:

- does it preserve `operating_flow_panel`, `maturation_canvas_panel`, and `execution_state_panel` gravity?
- does it preserve request / return / reflux separation?
- does it avoid selected-object behavior unless separately contracted?
- does it avoid trace UI unless separately contracted?
- does it avoid runtime binding and live manifest truth?
- does it avoid turning Gemini mock material into current authority?
- can it be expressed as visual token, wording note, or bounded patch?

If not, Codex should keep the Gemini output as design carry-forward only.

## 5. collision prevention

Gemini must not:

- edit outside `gemini/`
- patch `runtime/views/*`
- patch `docs/reports/*`
- change manifests
- change read maps
- run build-mode tasks by itself
- promote wording or extension candidates
- declare final baseline decisions

Codex must not:

- treat Gemini mock output as automatically accepted
- copy Gemini design structure directly into core
- skip baseline translation because the mock looks visually strong
- allow user-surface design proposals to become team/role console by accident

Shared rule:

- Gemini can expand possibility space.
- Codex filters against baseline.
- User decides when to promote a direction.

## 6. safe task classes for Gemini

| task class | safe? | output |
|---|---|---|
| repo scan / folder inventory | yes | `gemini/reports/*` |
| mock/design ideation | yes | `gemini/design_materials/*` |
| user-surface proposal | yes with guardrails | `gemini/briefs/*` |
| scaffold readability review | yes, read-only | `gemini/reports/*` |
| diff review after Codex patch | yes, read-only | `gemini/reports/*` |
| canonical docs update | no | Codex only unless user explicitly scopes otherwise |
| runtime/scaffold patch | no | Codex only |
| manifest/read-map change | no | hold unless explicitly opened |
| extension promotion | no | promotion gate first |

## 7. Gemini prompt shell

Use this shell when asking Gemini for design or user-surface material:

```text
Read gemini/gemini_cli_integrated_engine_boot_packet_v0.md first.

Task:
- Generate proposal material only for [surface / design question].
- Write only under gemini/.
- Do not edit runtime/views, docs/reports, manifests, read maps, or repo root files.
- Preserve current integrated-engine baseline:
  - user center = operating_flow_panel
  - VectorFL center = maturation_canvas_panel
  - engine center = execution_state_panel
  - request / return / reflux remain separate
- Do not introduce selected-object behavior, trace UI, runtime binding, watcher/supervisor/bridge authority, or extension promotion.
- Mark all outputs as proposal-only and needs Codex translation.

Output:
1. Gemini intake digest
2. proposal material
3. baseline-fit notes
4. risk / drift candidates
5. what needs Codex translation
```

## 8. handoff artifact shape

Gemini design or proposal artifacts should include:

- source prompt
- documents read
- assumed surface
- proposal summary
- baseline-fit notes
- drift risks
- rejected / held ideas
- Codex translation questions
- final label: `proposal-only / needs Codex translation`

## 9. closeout sentence

Gemini CLI can be used actively, but not as an uncontrolled second editor: let Gemini generate design clay and user-surface proposal material under `gemini/`, then let Codex translate it through the current VectorFL/integrated-engine baseline before anything enters core.
