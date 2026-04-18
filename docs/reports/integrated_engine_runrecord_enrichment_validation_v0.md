# Integrated Engine RunRecord Enrichment Validation v0

## 1. Verdict

PASS_WITH_NOTE

## 2. Tested Package

- package: `pkg_openharness_structure_probe`
- target context: `references/git_search/openharness-main`
- latest observed run count: `5`
- validation mode: existing package notebook / CLI session projection reread

## 3. What Changed

RunRecord now exposes continuation-friendly fields in addition to the legacy `result_summary`:

- `answer`
- `findings[]`
- `files_artifacts[]`
- `next_continue_hint`
- `open_questions[]`
- `risks_or_limits[]`
- `source_refs[]`

The existing session, event ledger, package notebook, and result summary remain intact. The enrichment is an adapter/projection layer, not a destructive storage rewrite.

## 4. Before / After Readability

Before enrichment, the package notebook mostly exposed one coarse result blob plus artifact refs. A next turn could continue technically, but the human reading path still felt like rereading a run log.

After enrichment, the latest OpenHarness run can be read as:

- answer: directory profile summary, top directories, top files, marker files
- findings: structural observations and VectorFL reread cues
- files/artifacts: concrete session and return artifacts
- next_continue_hint: reread latest answer with artifact refs and decide the next package-specific question
- risks/limits: dry-run validates carryover, not worker reasoning quality; reread-target is not approval

This makes the same package feel more like ongoing notebook work than a stack of coarse one-shot outputs.

## 5. Validation Checks

- API projection check: `build_cli_host_control_state(Path("runtime"))` returns enriched latest package run fields.
- Spine contract check: `spine_contracts.run_records` expose `answer`, `findings`, `files_artifacts`, and `next_continue_hint`.
- Python syntax check: `python3 -m py_compile app/runtime/vectorfl_integrated_engine_api.py`
- UI build check: `npm run build` in `app/ui/integrated_engine`

All checks passed.

## 6. Remaining Weakness

The parser is still format-sensitive.

The current dry-run output has a regular structural profile format, so extraction is useful. Real worker output may be less regular. If the worker returns prose without bullets, paths, or profile cues, enrichment will fall back to the raw summary and the notebook will still be partially coarse.

The next safe improvement is not a larger UI. It is to make worker returns emit a stable structured return shape that directly supplies answer/findings/artifacts/next hint.

## 7. Boundary

This validation did not implement:

- full artifact viewer
- streaming terminal
- multi-agent orchestration
- worker switching UI
- automatic line / axis detection
- cross-package chaining
- broad visual redesign

## 8. Final Judgment

RunRecord enrichment materially improves notebook readability and next-turn setup in a bounded way.

The result is not a solved semantic parser. It is a practical continuation projection that makes the existing package workbench easier to read while preserving backward compatibility.
