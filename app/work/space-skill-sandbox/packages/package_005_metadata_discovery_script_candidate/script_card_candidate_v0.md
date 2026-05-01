# Script Card Candidate v0 - package_metadata_scan.sh

## 0. Status

- status: candidate
- implemented: false
- automation: false
- source_space_rule: false
- baseline: false

## 1. Intended Caller

- Codex package orchestrator
- User-approved terminal execution

Not intended for:

- autonomous Gemini execution
- watch mode
- hooks
- background automation
- source-space promotion

## 2. Purpose

Produce a compact metadata scan for one bounded package directory so Codex can decide what to read deeply.

## 3. Input

```text
PACKAGE_DIR
```

Constraints:

- must be an existing directory
- must be under `app/work/space-skill-sandbox/packages/`
- must not be the whole sandbox root
- must not contain `..`

## 4. Output

Candidate output:

```text
<PACKAGE_DIR>/metadata_scan_report.md
```

Output should be compact and include:

- files seen
- found facts
- candidate guesses
- review needed
- deep-read candidates
- boundary check

## 5. May Read

- package-local markdown filenames
- package-local raw/outbox/stderr filenames
- first N lines of selected package-level markdown files
- file sizes

## 6. May Write

- one package-local metadata report

## 7. Must Not

- scan whole md space
- read outside PACKAGE_DIR
- install tools
- create graph
- create ontology
- create baseline
- modify existing package results
- overwrite output by default
- classify guesses as reviewed
- decide next package
- validate Gemini content

## 8. Failure Behavior

On failure, the script should:

- exit non-zero
- print a short reason
- avoid partial overwrite
- leave existing package files unchanged

## 9. Stop Points

User approval required before implementation.

User approval required again before using it outside a test package.

## 10. Candidate Verdict

Suitable as a first tiny script prototype candidate, but only after user approval.

Reason:

- small bounded read scope
- package-local output
- clear non-judgment boundary
- repeated manual work observed in Package 004

## 11. Closeout

This is a script card candidate only.
No script was implemented.
No source-space promotion was performed.
No baseline was created.
No automation, hook, MCP, watch mode, graph, ontology, router, controller, schema, Gemini result auto-application, or production workflow was created.
