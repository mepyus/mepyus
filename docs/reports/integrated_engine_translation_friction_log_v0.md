# Integrated Engine Translation Friction Log v0

Date: 2026-04-15

## 0. verdict

PASS_WITH_NOTE

This log records translation friction observations only.

No patch wording is proposed. No UI, scaffold, manifest, read-map, runtime, selected-object, trace UI, or extension work is opened.

## 1. log table

| friction_id | scenario | surface / context | internal phrase or panel wording | first-pass reading | supported reread reading | user-facing easy translation attempt | where friction appears | classification | carry_forward? | patch_candidate_now? |
|---|---|---|---|---|---|---|---|---|---|---|
| `tf_0001` | S1 normal request loop | protocol / route | `VectorFL review -> engine processing / external support` | Looks like a missing explicit connection step. | Request route intent plus later return packet confirms transition. | "VectorFL checks before work proceeds." | Easy wording hides that evidence is reconstructed from packet and return. | `support-dependent meaning` | yes | no |
| `tf_0002` | S1 normal request loop | VectorFL / return route | `return validation` | May sound like engine validates its own result. | Engine output returns for VectorFL validation before user decision / reflux / reprocess. | "The result comes back for checking." | Easy wording can blur who owns validation. | `internal-to-user wording gap` | yes | no |
| `tf_0003` | S1 normal request loop | reflux route | `reflux` | Unfamiliar; can sound like failure/rollback. | Preserves maturation-worthy material for reread and line/axis growth. | "Keep useful residue for later growth." | Easy wording can erase packet route/reason. | `internal-to-user wording gap` | yes | no |
| `tf_0004` | S1 normal request loop | loop state | `current_loop_state` | Can sound like full workflow history. | Minimum current-position state; connection records reconstruct movement. | "Where the loop is right now." | Users may expect timeline from state. | `support-dependent meaning` | yes | no |
| `tf_0005` | S3 drift / reprocess loop | VectorFL / anchor | `anchor drift` | Technical mismatch label. | Anchor mismatch is a route-braking reason that can trigger reprocess. | "The result no longer fits the reference point." | Easy wording may understate braking power. | `internal-to-user wording gap` | yes | no |
| `tf_0006` | S3 drift / reprocess loop | `anchor_context_panel` | support panel as brake | Looks advisory because it is support layer. | Connection record shows anchor criteria can stop progression. | "Reference check panel." | User may miss that support criterion can hold the route. | `support-dependent meaning` | yes | no |
| `tf_0007` | S3 drift / reprocess loop | loop route | `reprocess / rewind` | Can sound like confusion or undo. | Structured correction route; loop remains open by design. | "Send it back for correction." | Easy wording can make correction look like failure. | `scenario-specific compression` | yes | no |
| `tf_0008` | S3 drift / reprocess loop | loop state fields | `held_from_closure_reason` / `rewind_reason` | Internal state labels are not user-natural. | Explain why loop did not close and why it moved back. | "Why this was not finished yet." | Friendly phrase loses closure-hold vs rewind-cause distinction. | `internal-to-user wording gap` | yes | no |
| `tf_0009` | S3 drift / reprocess loop | evidence/history | drift record outside primary read map | Looks like missing evidence mapping. | Fixture scope says drift samples are manually checked through panel-role grammar. | "Use the extra route record for this scenario." | This is fixture scope, not translation failure. | `fixture-scope limitation` | no | no |
| `tf_0010` | real-use-like Gemini/Codex handoff | collaboration status | `proposal-only / needs Codex translation` | Can sound like delay or weak output. | Protects baseline by keeping Gemini design material as clay until Codex translation. | "Gemini drafts ideas; Codex checks what can enter." | Easy phrase loses formal promotion boundary. | `internal-to-user wording gap` | yes | no |
| `tf_0011` | real-use-like Gemini/Codex handoff | collaboration model | `Gemini expands possibility space; Codex filters against baseline` | Understandable collaboration metaphor. | Maps to Gemini design proposal worker and Codex baseline translator. | "Gemini explores options; Codex keeps them aligned." | Low friction. | `not-a-problem` | no | no |
| `tf_0012` | real-use-like Gemini/Codex handoff | workspace rule | `workspace ownership` | File-system bureaucracy. | Prevents simultaneous writes and preserves authority split. | "Each agent has its own work area." | Easy phrase hides authority boundary. | `internal-to-user wording gap` | yes | no |
| `tf_0013` | real-use-like Gemini/Codex handoff | stop rule | `collision stop condition` | Technical process language. | Defines when joint work must stop to avoid core drift. | "Stop if the idea would change the engine body." | Easy phrase compresses many guardrails. | `scenario-specific compression` | yes | no |
| `tf_0014` | real-use-like Gemini/Codex handoff | design material | `design clay` | Understandable. | Raw Gemini design material, not approved UI. | "Raw design material." | Low friction if paired with translation rule. | `not-a-problem` | no | no |

## 2. classification summary

| classification | count | friction ids |
|---|---:|---|
| `internal-to-user wording gap` | 7 | `tf_0002`, `tf_0003`, `tf_0005`, `tf_0008`, `tf_0010`, `tf_0012`, `tf_0013` |
| `support-dependent meaning` | 3 | `tf_0001`, `tf_0004`, `tf_0006` |
| `scenario-specific compression` | 2 | `tf_0007`, `tf_0013` |
| `fixture-scope limitation` | 1 | `tf_0009` |
| `hold-feature expectation leak` | 0 | none in this audit |
| `not-a-problem` | 2 | `tf_0011`, `tf_0014` |

Note:

- `tf_0013` is counted as `scenario-specific compression` in the table but also has an internal-to-user wording aspect. Its primary classification remains `scenario-specific compression`.

## 3. non-promotion note

None of these entries are wording patch candidates now.

Reason:

- this is translation friction, not repeated wording confusion
- supported reread recovers intended meanings
- scenario reading is not blocked
- patching individual terms now could flatten internal boundaries

## 4. hold boundary

Still out of scope:

- scaffold edits
- runtime/view edits
- patch wording
- manifest shape changes
- read-map changes
- selected-object behavior
- trace UI
- runtime binding
- extension promotion

## 5. closeout sentence

This log should be used as friction evidence for future translation-rule harvest, not as a wording patch queue.
