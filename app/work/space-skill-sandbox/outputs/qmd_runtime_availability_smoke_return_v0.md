# QMD Runtime Availability Smoke Return v0

## Status

```yaml
status: runtime_smoke_return
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
qmd_help_executed: true
qmd_search_executed: false
qmd_indexing_executed: false
qmd_mcp_executed: false
verdict: PASS_AS_CLI_ENTRY_SMOKE_WITH_WATCH
```

## Purpose

Check whether QMD can be fetched and invoked at the CLI entry level before attempting any indexing, search, MCP startup, or retrieval-output contract validation.

## Command Trace

First attempt:

```text
npx @tobilu/qmd --help
```

Result:

```text
failed with npm EACCES against /Users/sungsookim/.npm/_cacache
```

Reason classification:

```text
local npm cache permission issue
not a QMD functional failure
not a VectorFL attachability failure
```

Second attempt:

```text
npx --cache /private/tmp/vectorfl-qmd-npm-cache @tobilu/qmd --help
```

Result:

```text
exit_code: 0
```

## Tool Output Summary

The QMD help output was successfully returned through the npx temporary-cache route.

Observed command families:

```text
query
search
vsearch
get
multi-get
skill show/install
mcp
bench
collection add/list/remove/rename/show
context add/list/rm
ls
status
update
embed
cleanup
```

Observed output formats:

```text
--files
--json
--csv
--md
--xml
default CLI output
```

Observed query/search options:

```text
-n
--all
--min-score
--full
--candidate-limit
--no-rerank
--line-numbers
--explain
-c / --collection
```

Observed MCP note:

```text
qmd mcp exposes stdio MCP.
qmd mcp --http and --daemon exist as advanced/custom transports.
```

Observed default index path:

```text
/Users/sungsookim/.cache/qmd/index.sqlite
```

## Anchor Usage Trace

The smoke followed the runtime preflight hold:

```text
do only CLI entry smoke
do not create collection
do not embed
do not search
do not start MCP
do not write parser/schema/automation
```

The QMD source inspection anchor correctly predicted the CLI command families and output surfaces.

## Not Inspected

```text
search results
JSON output structure from a live query
collection creation
index creation
embedding generation
native dependency runtime behavior beyond help startup
MCP server startup
HTTP MCP daemon behavior
SDK import/runtime
fixture corpus retrieval
VectorFL corpus retrieval
```

## Watch Items

```text
npm_home_cache_permission_watch
temporary_npx_cache_route_watch
default_qmd_index_path_outside_workspace_watch
collection_indexing_approval_watch
model_embedding_download_watch
mcp_background_process_watch
runtime_help_success_overclaim_watch
```

## Candidate Return-to-Space Value

Recoverable material:

```text
QMD CLI entry can be invoked through an npx temporary-cache route on this machine.
```

Reusable judgment:

```text
For future QMD runtime trials, avoid the user's broken home npm cache by using an explicit temporary npm cache path unless the home cache is repaired.
```

Boundary:

```text
The next step is not more help inspection. It is an isolated fixture indexing/search trial, which must control storage path and avoid accidentally indexing VectorFL.
```

## Do Not

```text
do not treat this as retrieval validation
do not treat this as QMD attachability completion
do not treat the default QMD index path as approved storage
do not start MCP from this smoke
do not create collection/index without approval
do not update current position from this alone
```

`STATUS: QMD_RUNTIME_AVAILABILITY_SMOKE_RETURN_PREPARED`
