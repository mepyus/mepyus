# codex_gemini_manual_relay_protocol_v0

## 1. Purpose
This note records the working protocol for using Codex as the task designer, verifier, and direction keeper while the user manually relays selected packets to Gemini CLI.

The goal is not to automate every step. The goal is to preserve a readable process trail so each Gemini result can be interpreted, corrected, and folded back into the program direction without accidental promotion.

## 2. Roles
- User: relay operator. Carries the packet path or packet content to the Gemini side and brings the result back. The user is not expected to be the workflow designer or shell-command operator.
- Codex: packet author, boundary checker, result interpreter, and next-step designer.
- Gemini CLI: bounded reader or worker for a named package. It does not decide promotion, baseline, canonical status, or source-of-truth changes.

## 3. Default Flow
1. Codex writes a Gemini packet under `app/work/space-skill-sandbox/outputs/` or `app/work/space-skill-sandbox/relay/outbox/`.
2. Codex reports only the exact packet path and suggested `run_id` unless the user asks for execution details.
3. User relays that packet to the Gemini side by the currently available manual channel.
4. User returns Gemini output to Codex.
5. Codex reviews the output against sandbox operating rules, source evidence, and program direction.
6. Codex either accepts, corrects, narrows, or rejects the result before writing the next packet.

## 4. Judging Standard
Every Gemini result should be judged by:
- whether it preserves the sandbox boundary
- whether it separates source-of-truth artifacts from derivative surfaces
- whether it avoids promotion without human judgment
- whether its claims are backed by file paths or observed behavior
- whether the result improves the eventual program structure rather than only producing more notes

## 5. Hold Triggers
Codex should mark a result as requiring human judgment when Gemini recommends or implies:
- promotion
- baseline lock
- canonical registry change
- source-of-truth change
- broad merge or compaction
- automatic indexing of sandbox outputs
- moving sandbox artifacts into `runtime/manifests/`

## 6. Output Discipline
Packets should be named with a package/run identifier and a clear purpose. Gemini outputs should keep their source packet path visible.

Sandbox artifacts must not claim to be core registry, provenance index, canonical manifest, or baseline unless the user explicitly decides that status after review.

## 7. Current Operating Decision
Codex will not call Gemini CLI by default. Codex will prepare packet files and return path information. The user controls relay timing, while execution mechanics remain outside Codex's default role for now.

Direct script execution from Codex or Gemini may become useful later after the process is stable. Until then, the priority is to record the relay process, inspect the results, and adjust the protocol based on real use.
