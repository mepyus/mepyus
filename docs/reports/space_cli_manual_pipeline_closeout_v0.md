# Space-CLI Manual Pipeline Closeout v0

## 1. core conclusion

The space-CLI structure can be made pipeline-shaped.

At this stage it must remain a manual operating pipeline, not an automation pipeline.

The pipeline is useful because it keeps the space as the body and treats Codex / Gemini / scripts as bounded workers.

## 2. why manual first

Manual operation comes first because:

- source surface judgment still needs space / human reading
- worker assignment is risky if automated too early
- reflux memory must not auto-promote
- Gemini and Codex outputs both require `worker_return` review
- actual repeated runs are needed to see whether the space becomes heavy
- `next_move_candidate` must remain a candidate, not an action

## 3. where scripts may start later

Possible first script areas:

- template generation
- required field missing check
- memory card count check
- forbidden expression scanning
- 4-line user card presence check
- worker_return field presence check

Still not scriptable:

- judgment
- assignment
- reflux finalization
- automatic execution
- baseline promotion
- source surface final decision
- file edit / revert decision

## 4. next step

Next step is to run one real material through the manual pipeline template.

Recommended materials:

- Gemini role over-promotion incident
- actual external material
- Codex worker_return
- user conversation_material

Do not implement scripts yet.

Do not create runtime structure, JSON schema, bridge, dispatcher, or controller.

## 5. final compression

The space does not feed its whole memory to the CLI.

The space retrieves only needed memory cards and builds a lightweight task packet.

The CLI acts as a worker.

The result returns as `worker_return`.

The difference becomes a reflux memory candidate.

The user receives a 4-line card:

```text
쓸 수 있나?
왜?
다음엔?
조심할 점은?
```

## 6. closeout verdict

```yaml
verdict: PASS_WITH_NOTE
manual_pipeline_documented: true
stage_io_documented: true
run_template_created: true
script_candidates_separated: true
automation_pipeline_created: false
script_created: false
runtime_structure_created: false
json_schema_created: false
bridge_created: false
dispatcher_created: false
baseline_lock: false
next_allowed_move: run_one_manual_pipeline_case
```
