# Scriptable Handoff Layer Methodology v0

## 0. Status

- status: sandbox candidate
- source_space_rule: false
- baseline: false
- automation: false
- production_workflow: false

## 1. Purpose

This document defines the manual-triggered script layer that transports package packets to Gemini CLI and captures the result for Codex validation.

The script layer is transport, not judgment.

## 2. Why This Layer Exists

Manual copy/paste is not only inconvenient. It breaks package-scale feedback because waiting, result capture, and validation are scattered across chat sessions.

The target shift is:

```text
manual copy-paste relay
→ manual-triggered script relay
```

The user still explicitly triggers execution. Nothing watches folders, runs in the background, or applies results automatically.

## 3. Diagnostic Layers

Runner failures should be separated by layer:

1. Gemini CLI binary
2. non-interactive `-p/--prompt`
3. authentication state
4. output format
5. timeout behavior
6. packet path reading
7. stdout/stderr/raw/outbox capture
8. Codex-readable review bundle

Do not call all failures "handoff failure." Preserve the layer where the failure occurred.

## 4. Script Responsibilities

Scripts may:

- read a packet file
- call Gemini CLI
- record timestamp and run id
- save stdout
- save stderr
- save raw json/text
- save human-readable outbox
- record exit code
- record timeout
- collect package artifacts for Codex review

Scripts must not:

- decide next work
- validate Gemini output
- apply Gemini output
- modify source-space
- declare baseline
- execute promotion
- auto-retry
- run watch mode
- install hooks
- act as router, controller, or agent

## 5. Script Set Candidate

### run_gemini_packet.sh

Purpose: send one packet to Gemini CLI and capture raw/outbox/stderr.

Current path:

```text
scripts/sandbox/run_gemini_packet.sh
```

### package_handoff.sh

Purpose: send one package's `gemini_packet.md` through the runner and record handoff facts.

Current path:

```text
scripts/sandbox/package_handoff.sh
```

### package_collect.sh

Purpose: collect central raw/outbox runner artifacts back into the package folder and write a Codex-readable review bundle.

Current path:

```text
scripts/sandbox/package_collect.sh
```

## 6. Preflight Discipline

Before trusting a package handoff, run checks in this order:

```bash
gemini -p "Reply with exactly: GEMINI_SMOKE_OK"
gemini -p "Reply with exactly: GEMINI_SMOKE_OK" --output-format json
bash scripts/sandbox/run_gemini_packet.sh --smoke-text --timeout-seconds 60
bash scripts/sandbox/package_handoff.sh --dry-run app/work/space-skill-sandbox/packages/package_000_smoke
bash scripts/sandbox/package_collect.sh app/work/space-skill-sandbox/packages/package_000_smoke
```

Credential values must never be printed. Presence/absence is enough.

## 7. Result Capture

A useful captured result includes:

- package path
- packet path
- run id
- timestamp
- dry-run flag
- raw output path
- stderr path
- outbox path
- timeout seconds
- exit code when available

Failure is also a result. A failed handoff must leave enough evidence for Codex to read.

## 8. RUN_ID Safety

Run ids are filenames. They should match:

```text
[A-Za-z0-9._-]+
```

They must not contain:

```text
/
..
space
;
&
|
$
`
>
<
*
?
newline
```

Strong security terms should be used only when the exploit vector is actually present. In this context, unsafe run ids are first a filename/path pollution risk unless command execution context proves more.

## 9. Non-Automation Guardrail

This layer is manual-triggered transport only.

It is not:

- background automation
- watch mode
- hook
- MCP
- router
- controller
- production workflow
- source-space promotion tool
- baseline creation tool

## 10. Closeout

This is a sandbox scriptable handoff methodology candidate only.
No automation was created by this document.
No source-space promotion was performed.
No baseline was created.
No Relay v1.0 was declared.
No production workflow was created.
