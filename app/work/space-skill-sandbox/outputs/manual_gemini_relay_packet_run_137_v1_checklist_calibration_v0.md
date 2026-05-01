# Manual Gemini Relay Packet - Run 137 v1 Checklist Calibration

## Mode

USER -> GEMINI / MANUAL RELAY / CALIBRATION ONLY / READ ONLY / NO EXECUTION / NO AUTOMATION / NO PROMOTION

## Case

- case_id: `run_137_v1_checklist_calibration`
- relay_mode: `manual_chat_return`
- target: `whole_space_handoff_checklist_v1_candidate`

## Your Role

You are Gemini, a bounded observation worker.

You are not approving the checklist.
You are not promoting it.
You are not turning it into workflow, schema, policy, automation, router, controller, graph, or ontology.
You are not executing any package work.

Your job is to produce a calibration note explaining how Gemini should read the checklist safely.

Return one chat block only:

```text
GEMINI_CALIBRATION_NOTE_MD
```

Do not write files.

## Read Scope

Read only:

1. `app/work/space-skill-sandbox/outputs/whole_space_handoff_checklist_v1_candidate.md`
2. `app/work/space-skill-sandbox/outputs/codex_review_whole_space_handoff_checklist_v1_candidate_content.md`
3. `app/work/space-skill-sandbox/outputs/whole_space_handoff_checklist_v1_light_revision_design_v0.md`
4. `app/work/space-skill-sandbox/outputs/run_identity_correction_note_whole_space_handoff_checklist_v1_candidate.md`
5. `app/work/space-skill-sandbox/outputs/whole_space_external_lens_connection_map_v0.md`

Do not scan the repository.
Do not open Package 035 target contents.
Do not open Package 036.

## Task

Return a calibration note answering:

1. What should Gemini learn from v1?
2. What must Gemini not infer from v1?
3. How should Gemini distinguish full mode and compact mode?
4. How should Gemini treat `source_refs`, `memory_layer`, and `authority_status`?
5. How should Gemini treat sandbox 15 principles?
6. How should Gemini treat external lenses?
7. What overread risks remain?
8. Is v1 safe for Gemini calibration after the light revision design is applied?

## Required Return

Return exactly:

```markdown
GEMINI_CALIBRATION_NOTE_MD

# Gemini Calibration Note - Run 137 v1 Checklist

## Status

## What Gemini Should Learn

## What Gemini Must Not Infer

## Full Mode vs Compact Mode

## Source Refs / Memory Layer / Authority Status

## Sandbox 15 Principles

## External Lens Treatment

## Remaining Overread Risks

## Calibration Readiness

## GEMINI_CALIBRATION
from: Gemini
to: Codex / ChatGPT / User
type: v1_checklist_calibration
status:
learn:
must_not_infer:
full_mode_use:
compact_mode_use:
source_refs_rule:
memory_layer_rule:
authority_status_rule:
sandbox_15_rule:
external_lens_rule:
remaining_risks:
readiness:
uncertainty:
```

## Hard Boundaries

- No execution.
- No package work.
- No Package 035 target analysis.
- No Package 036 opening.
- No baseline promotion.
- No official workflow declaration.
- No source-space promotion.
- No automation / policy / schema / router / controller / graph / ontology.
- No file writes.
- No treating v1 as final rule.

## Expected Status

```text
CALIBRATION_READY_WITH_BOUNDARIES
```

If the read scope is insufficient, return:

```text
BLOCKER_RAISED
reason:
needed_context:
```

