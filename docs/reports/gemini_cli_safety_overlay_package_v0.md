# Gemini CLI Safety Overlay Package v0

## 1. status

```yaml
package_status: safety_overlay
verdict: PASS_WITH_NOTE
default_permission: no-write
baseline_lock: false
schema_enforcement: false
controller_implementation: false
runtime_manifest: false
index_update: false
```

## 2. purpose

This package is a safety overlay on top of the Gemini CLI orientation and execution documents.

It does not create a new Gemini system. It narrows Gemini's authority before Gemini is used as an execution, validation, listing, or test assistant.

Core rule:

```text
Gemini is not an editor.
Gemini is an execution / validation / listing / draft worker.
```

Gemini output must be reread as `worker_return` before acceptance.

## 3. Gemini default position

Gemini may be used as:

- read-only learner
- material lister
- draft generator
- validation checker
- sandbox executor
- stdout/stderr interpreter
- HOLD candidate finder

Gemini must not be used as:

- editor
- deleter
- refactorer
- architecture decider
- final judge
- baseline owner
- controller modifier
- schema modifier
- runtime modifier
- index or microspace modifier

## 4. default permission

```text
default_permission: no-write
```

Any write, modification, deletion, move, overwrite, cleanup, or direct patch is forbidden unless a later instruction explicitly grants a narrower exception.

The default answer to "Can Gemini modify this?" is:

```text
No. Gemini may propose. Codex applies only after separate instruction.
```

## 5. allowed Gemini levels

### Level G0 - Read only

Allowed:

- read specified files
- restate roles and guardrails
- identify missing context

Forbidden:

- file creation
- file modification
- deletion
- movement
- overwrite

### Level G1 - List only

Allowed:

- list candidate materials
- mark source surface candidates
- mark risks
- suggest task types

Forbidden:

- trial execution
- file creation
- file modification
- material merging into one summary

### Level G2 - Draft only

Allowed:

- draft 4-line cards
- draft self-checks
- draft validation summaries
- draft patch proposals without applying them

Forbidden:

- direct edits
- append to existing files
- creating new records

### Level G3 - Sandbox execution only

Allowed:

- run explicitly specified command or script
- capture stdout/stderr
- write only to explicitly specified sandbox output path

Required sandbox path when output files are allowed:

```text
runtime/gemini_sandbox/<case_id>/
```

Forbidden:

- existing repo file modification
- deletion
- overwrite
- runtime manifest creation
- index update
- cleanup

### Level G4 - Append only exceptional

Allowed only when explicitly instructed:

- one specified file
- one specified section
- append at document end only

Still forbidden:

- modifying existing sections
- deleting content
- rewriting headings
- formatting entire document
- applying patches on Gemini's own authority

G4 is not Gemini's default. It is exceptional.

## 6. core principles

- Gemini does not fix existing files.
- Gemini does not delete existing files.
- Gemini does not move existing files.
- Gemini does not overwrite existing files.
- Gemini may propose changes, but must not apply them.
- Gemini may execute only in read-only, dry-run, stdout-only, or explicit sandbox-output mode.
- Gemini returns must be reread as `worker_return`.
- Codex or the user decides whether any proposed change is applied.

## 7. relationship to prior Gemini docs

This overlay narrows any broad reading of earlier Gemini documents.

If an older Gemini document says append or execution is allowed, read that through this overlay:

```text
append: exceptional only
execution: read-only / dry-run / stdout-only / sandbox-output only
write: default no
delete / move / overwrite: no
```

## 8. do not

- Do not baseline lock.
- Do not grant Gemini final judgment.
- Do not let Gemini directly patch repo files.
- Do not let Gemini delete, move, overwrite, or clean up files.
- Do not treat Gemini's speed as reliability.
- Do not let Gemini create schema, controller, runtime manifest, or index updates.
- Do not let Gemini modify helper or code.
