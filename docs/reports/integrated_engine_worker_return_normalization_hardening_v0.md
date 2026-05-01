# Integrated Engine Worker Return Normalization Hardening v0

## 1. Verdict

PASS

## 2. Package Purpose

Package 4 tested whether package notebook continuity survives imperfect worker output without running more real external workers.

This was fixture-first by design. Package 3 already proved real worker continuation can work. Package 4 tested the weaker cases around that boundary.

## 3. Failure-Shape Inventory

Fixture cases covered:

| Case | Fixture type | Real or synthetic | Purpose |
| --- | --- | --- | --- |
| valid worker-emitted JSON | valid delimited JSON block | synthetic shaped from Package 2/3 contract | confirm primary path |
| missing block | prose and bullets only | synthetic | confirm fallback parser path |
| invalid JSON block | delimiters present, invalid JSON body | synthetic | distinguish invalid block from missing block |
| partial worker-emitted block | valid JSON with missing fields | synthetic | confirm partial worker fields survive while missing fields are normalized |
| prose-only return | plain prose with observations and path | synthetic | confirm notebook remains readable without contract compliance |
| failed / nonzero return | failed status, exit code, error text | synthetic | confirm failed run produces inspectable failure material |
| deposit candidate | valid worker block plus `deposit_candidate` route | synthetic | confirm candidate is not treated as automatic ingestion |

No new actual worker run was used. That kept the package focused on normalization resilience rather than expanding worker scope.

## 4. Normalization Policy Summary

Rules locked in:

- valid worker block remains `worker_emitted`
- missing block falls to `parser_fallback` if useful text exists
- invalid JSON block falls to `parser_fallback` and records `invalid_json`
- partial worker block remains `worker_emitted` but records missing-field normalization risk
- prose-only return can remain continuation-readable through extracted answer/findings/path refs
- failed/nonzero return preserves failure status, exit code, error text, and session artifacts
- deposit candidates preserve the explicit rule: review only, no automatic ingestion
- worker-emitted `next_continue_hint` keeps priority when valid

## 5. Runtime Hardening Summary

Updated:

- `_extract_worker_emitted_return_with_status(...)`
- `_extract_worker_emitted_return(...)`
- `_normalize_worker_return(...)`
- actual worker run integration in `CodexCliAdapter.start_run(...)`

Hardening added:

- extraction status labels:
  - `valid`
  - `missing_block`
  - `missing_delimiter`
  - `missing_end_delimiter`
  - `invalid_json`
  - `invalid_shape`
- risk recording for invalid/missing worker-return block states
- risk recording for partial worker-emitted returns
- risk recording for failed execution status and nonzero exit code
- explicit deposit-candidate non-ingestion risk
- conservative source-ref fallback from bounded context or artifact refs
- failed-run fallback answer/finding when no readable worker answer exists

The patch stayed in the runtime normalization boundary. No UI expansion, orchestration expansion, or new worker integration was added.

## 6. Readability Validation Summary

Fixture validation result:

| Case | Extraction status | Source outcome | Notebook readability |
| --- | --- | --- | --- |
| valid worker-emitted | `valid` | `worker_emitted` | possible; worker answer/findings/hint preserved |
| missing block | `missing_block` | `parser_fallback` | possible but weaker; extraction risk visible |
| invalid JSON block | `invalid_json` | `parser_fallback` | possible but weaker; invalid JSON risk visible |
| partial worker-emitted | `valid` | `worker_emitted` | possible with risk; missing fields normalized |
| prose-only | `missing_block` | `parser_fallback` | possible; extracted observations and refs visible |
| failed/nonzero | `missing_block` | `raw_fallback` | blocked/inspect-first; failure answer/finding visible |
| deposit candidate | `valid` | `worker_emitted` | possible; non-ingestion boundary preserved |

The notebook does not collapse into a single coarse blob in these cases. The strongest degradation is failed/nonzero output, which intentionally becomes inspect-first rather than a fake continuation success.

## 7. Optional Smoke Validation

Skipped.

Reason:

- Package 3 already ran two real external Codex worker turns successfully.
- Package 4 changed normalization behavior, not prompt dispatch behavior.
- The affected path was validated through direct fixture calls into the same extraction and normalization helpers used by actual runs.
- Running more external workers would increase cost without materially improving coverage of malformed/missing/partial output shapes.

## 8. Risks

Remaining risks:

- fixture coverage does not fully cover every possible real worker formatting drift
- prose-only parsing remains intentionally weak and bullet/path dependent
- failed output can be preserved, but it cannot be made continuation-strong without a later successful run
- Gemini-style output may stress delimiter compliance differently
- source-ref fallback from artifacts is conservative but still approximate

## 9. Package 5 Readiness

Package 5 is ready.

Recommended focus:

- test supervisor continuation loop on a package notebook containing mixed sources:
  - `worker_emitted`
  - `parser_fallback`
  - `raw_fallback`
- verify whether supervisor can judge:
  - continue
  - hold
  - rerun worker
  - inspect artifacts
  - close package

