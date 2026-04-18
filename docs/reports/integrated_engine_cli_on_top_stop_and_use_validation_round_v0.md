# Integrated Engine CLI On-Top Stop-And-Use Validation Round v0

## Verdict
PASS_WITH_NOTE

Package 1.1 was used in stop-and-use mode with three tiny real read-only Codex runs. The runs used the same `/api/vectorfl-engine/actions/cli-session/run` path that the VectorFL CLI Host / Control panel calls. The VectorFL page was opened first, but the run actions were triggered through the panel endpoint rather than browser-click automation.

## Runs

| run | session_id | task_type | target | status | mark |
| --- | --- | --- | --- | --- | --- |
| 1 | `cli_20260416T094731Z_97d5f828` | `summarize` | `docs/reports/integrated_engine_cli_on_top_package1_1_closeout_note_v0.md` | `done` | `validation_target` |
| 2 | `cli_20260416T094801Z_ea262a3b` | `inspect` | `app/runtime/vectorfl_integrated_engine_shell.py` | `done` | `reread_target` |
| 3 | `cli_20260416T094830Z_7b2f3fa5` | `reread` | `docs/reports/integrated_engine_cli_on_top_package1_closeout_note_v0.md` | `done` | `deposit_candidate` |

All three runs were real Codex runs with dry-run off, read-only sandbox posture, captured stdout/stderr, generated `structured_return.json`, and generated `deposit_candidate.md`.

## What Felt Immediately Usable

- The latest-return card is enough for first-pass reading of the most recent run.
- Session id, backend, task type, status, purpose, marks, structured preview, and deposit preview give enough context without opening raw files.
- The mark buttons are enough for first-pass operation when the user only needs to classify the latest return as reread, validation, implementation return, or deposit candidate.
- The status `done` plus exit code 0 in the generated session makes the run outcome clear enough for tiny tasks.
- The CLI layer still reads as on-top: it is visible through VectorFL, leaves engine-facing artifacts, and does not become a fourth surface.

## What Still Felt Manual Or Broken

- The page is latest-session centered. After running a new task, the previous task is no longer directly readable from the page without going to raw artifacts or reconstructing from memory.
- Marking is enough for current-session classification, but it does not give a small visible history of the three validation runs beyond the latest mark history.
- The structured return preview is readable, but when Codex returns nested bullets or repeated headings, the preview can feel dense.
- For a real-use validation round with multiple tiny runs, the bottleneck was not async execution. It was remembering and comparing the last few sessions.

## First-Pass Page Reading Judgment

For a single latest return, the VectorFL page now removes the need to open raw artifact files. For a sequence of runs, manual file opening or mental reconstruction returns because only the latest session is visible.

Status flow is understandable for these tiny synchronous runs: each task returns as `done`, and the latest card updates to the new session. This is sufficient for stop-and-use validation, but it does not yet support looking back across several recent runs from the page.

Marks are sufficient for first-pass operation on the current return. They are not sufficient as a lightweight validation-round memory across multiple runs.

## Single Highest-Priority Next Package

The next true bottleneck is not background execution or Gemini. The immediate use problem is that multiple successful runs disappear behind the latest-session view.

Recommended next package target: **session browsing/history**
