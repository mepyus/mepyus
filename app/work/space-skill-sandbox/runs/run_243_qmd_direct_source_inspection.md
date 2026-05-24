# Run 243 - QMD Direct Source Inspection

## 1. Verdict

```text
PASS_WITH_WATCH_AS_QMD_DIRECT_SOURCE_INSPECTION
```

## 2. Files Created

```text
app/work/space-skill-sandbox/outputs/qmd_direct_source_inspection_report_v0.md
app/work/space-skill-sandbox/outputs/qmd_vectorfl_retrieval_output_contract_candidate_v0.md
app/work/space-skill-sandbox/outputs/movement_record_qmd_direct_source_inspection_v0.md
app/work/space-skill-sandbox/runs/run_243_qmd_direct_source_inspection.md
```

## 3. What Was Inspected

```text
references/git_search/qmd-main README, package metadata, CLI, formatter, MCP server, SDK index, collection config, syntax docs, and relevant tests.
```

## 4. Result

```text
QMD has concrete output surfaces useful for VectorFL retrieval-output contract design:
CLI JSON/files/markdown outputs, MCP query/get/multi_get, SDK search/get/multiGet, docid/path/context/score/snippet/line fields.
```

## 5. Main Candidate Judgment

```text
The safest first attach path is output-contract design around retrieval returns as raw evidence pointers.
It is not repo import, runtime replacement, MCP setup, storage, schema, or automation.
```

## 6. Watch

```text
QMD score/context/snippet/docid metadata can look authoritative.
Keep all retrieval metadata raw until Codex/VectorFL recovery interprets it.
No QMD runtime was executed.
No VectorFL corpus was indexed.
```

## 7. Current-Position Decision

```text
NO_CURRENT_POSITION_UPDATE_REQUIRED
```

Reason:

```text
This run creates source-backed contract candidates but does not perform runtime validation or approve attach implementation.
```

## 8. Recommended Next Direction

```text
Run a dry output-contract trial using a sample QMD return shape before any installation/indexing package.
```

`STATUS: RUN_243_QMD_DIRECT_SOURCE_INSPECTION_COMPLETE`
