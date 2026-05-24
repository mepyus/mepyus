# QMD Isolated Fixture Trial - Codex Recovery v0

## Status

```yaml
status: codex_recovery
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
source_return: qmd_isolated_fixture_trial_execution_return_v0
verdict: PASS_WITH_WATCH_AS_RECOVERABLE_RETRIEVAL_TRACE
```

## Recovery Purpose

Recover the first real QMD fixture retrieval output into VectorFL terms without treating the QMD result as authority, memory, or implementation completion.

## Accepted Candidate Evidence Pointers

Accepted as candidate pointers:

```text
qmd://fixture001/anchor-loop-note.md
  reason: directly matched the movement sequence around Return-to-Space Value and Movement Record.

qmd://fixture001/qmd-boundary-note.md
  reason: directly matched Codex recovery rules before anything enters VectorFL memory.
```

Accepted only as:

```text
raw retrieval trace
fixture evidence pointer
contract-shape runtime evidence
future bounded-read target
```

## Held Metadata

Held as metadata, not judgment:

```text
docid values
score values
qmd:// URIs
title values
snippet text
result ordering
```

Reason:

```text
The returned scores were 0 even though the snippets were relevant to the query. This is direct runtime evidence that score must not be treated as semantic truth or promotion priority.
```

## Not Inspected / Gap

Not inspected:

```text
full source body through qmd get
multi-get output
line-number output
explain output
query/rerank behavior
vector search behavior
MCP behavior
SDK behavior
VectorFL corpus behavior
```

Gap:

```text
The retrieval contract is validated only for CLI search JSON over an isolated fixture.
```

## Downshift

Do not say:

```text
QMD is integrated with VectorFL.
QMD memory works.
QMD can replace VectorFL space memory.
QMD search quality is validated.
QMD scores are reliable.
The contract is a schema.
```

Say instead:

```text
QMD CLI search JSON can produce recoverable candidate evidence pointers in an isolated fixture trial.
```

## Return-to-Space Value

Recoverable material:

```text
The QMD_RETRIEVAL_RETURN_CARD survived its first live CLI JSON fixture trial.
```

Reusable judgment:

```text
A retrieval carrier can be attached at the evidence-pointer layer before becoming a memory writer, but Codex recovery must hold metadata and classify not-inspected scope.
```

New issue / watch:

```text
score_zero_but_semantically_matched_watch
qmd_uri_filename_normalization_watch
default_index_path_requires_isolation_watch
fixture_success_overclaim_watch
```

Future reuse note:

```text
For the next trial, use qmd get or multi-get on accepted candidate pointers to test whether retrieval pointers can support bounded follow-up reads.
```

## User Decision Point

Possible next direction:

```text
approve a qmd get / multi-get follow-up on the same isolated fixture
approve a larger but still bounded fixture
approve a carefully scoped VectorFL subset trial
hold QMD at fixture evidence-pointer level
```

## Do Not

```text
do not promote to baseline
do not update current position
do not create parser/schema
do not create automation
do not index VectorFL corpus yet
do not start MCP yet
do not treat score as truth
```

`STATUS: QMD_ISOLATED_FIXTURE_TRIAL_CODEX_RECOVERY_PREPARED`
