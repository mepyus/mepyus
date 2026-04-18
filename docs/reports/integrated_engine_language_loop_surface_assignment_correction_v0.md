# Integrated Engine Language Loop Surface Assignment Correction v0

## Verdict

PASS_WITH_NOTE

## Correction

The internal language loop was first mounted in the VectorFL surface because it is executed through the existing CLI-on-top path. That placement was too literal.

The loop itself is not the same as direct VectorFL mediation. It is a user-surface internal team assignment: a language 담당 work screen that asks Codex to repeatedly collect internal-language material, then turns that material into line / connection / axis evidence for later reread.

## Correct Surface Assignment

| Item | Correct reading |
| --- | --- |
| Language loop request | User surface work organization |
| Role | Internal team / language 담당 |
| Execution path | Existing CLI-on-top path |
| Reread / mediation of outputs | VectorFL surface |
| Artifact / deposit material | Engine-facing return material |

## What Changed

- `Internal Team / Language Loop` was moved from the VectorFL surface into the User surface.
- It now sits under an explicit `Internal team / language 담당 work screen` band.
- VectorFL keeps the direct CLI host/control panel for operation, reread, and mediation.
- The loop still uses the same runtime artifacts under `runtime/language_loops`.

## Boundary

- No new surface was added.
- No read map or manifest shape was changed.
- This is not final UI copy or a final translation layer.
- The correction is about operational ownership: the language loop is assigned by the user surface, then reread by VectorFL.

## Why This Matters

The integrated engine should not put every CLI-backed activity into VectorFL just because the CLI path is visible there. A task that collects language material for an internal role is a work assignment, so it belongs to the user surface. VectorFL can still interpret the result, but it should not absorb the user surface's job organization role.

