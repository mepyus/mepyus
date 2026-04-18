# folder_status / gemini

## 1. Folder Identity

- path: `gemini`
- role_guess: Gemini reference / proposal / handoff material area.
- status_mode: `manual_current_status`
- last_updated: `2026-04-16`

## 2. Current Reading

This folder is not the integrated-engine runtime body. It is a Gemini-side reference and proposal material area.

Gemini material can provide:

- design clay
- proposal-only visual material
- external comparison notes
- handoff drafts
- collaboration scope notes
- Gemini CLI boot/context packets

Gemini material must not directly become:

- canonical integrated-engine baseline
- runtime truth
- scaffold read-map authority
- user-facing final UI copy
- automatic implementation instruction

## 3. Child Folder Roles

| folder | role |
| --- | --- |
| `analysis` | Gemini-produced or Gemini-facing analysis notes. |
| `core_docs` | stable reference packets for Gemini learning / bootstrapping. |
| `external_analysis` | external tool/project DNA analysis material. |
| `map` | repo/folder map material for Gemini orientation. |
| `mock_test` | design/prototype mock material; now used as visual/design clay and partially migrated into the main UI. |
| `outputs` | Gemini output artifacts. |
| `prompts` | prompt templates for Gemini tasks. |
| `protocols` | Codex/Gemini collaboration, dispatch, scope, and operating lock documents. |
| `session_logs` | Gemini session history and update notes. |

## 4. Mock Test Boundary

`gemini/mock_test` is a source mock/proposal folder. It is not the current main UI by itself.

Current usage:

- selected mock components and visual rhythm were copied / adapted into `app/ui/integrated_engine`.
- mock structures such as supervisor, watcher, bridge, and governance are not automatically promoted.
- mock visual material must pass integrated-engine baseline translation before becoming stable UI.

## 5. Main Integrated UI Relation

The currently used integrated-engine UI lives under:

- `app/ui/integrated_engine`

That folder contains the merged/adapted main surface shell. It is the current UI implementation area for the integrated-engine app.

Gemini remains upstream reference/proposal material. Codex must translate/adapt it before it enters the main UI.

## 6. Operating Rule

When Gemini material is used:

1. Read it as proposal material.
2. Classify whether it belongs to User / VectorFL / Engine surface.
3. Check whether it preserves fixed 3-surface roles.
4. Translate the useful part into current baseline structure.
5. Record what was accepted, held, or rejected.

## 7. Current Watchpoints

- Do not confuse `gemini/mock_test` with the current operating app.
- Do not treat Gemini design as canonical structure.
- Do not let Gemini/Codex collaboration create a fourth surface.
- Do not let CLI become an external agent system outside the integrated-engine flow.

