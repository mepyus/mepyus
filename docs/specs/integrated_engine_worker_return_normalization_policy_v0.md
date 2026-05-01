# Integrated Engine Worker Return Normalization Policy v0

## 1. Purpose

This policy hardens the worker return boundary after the first real worker continuation validation.

The goal is not to make imperfect worker output look complete. The goal is to keep the package notebook readable enough for supervisor judgment when worker output is missing, partial, invalid, prose-only, failed, or deposit-candidate shaped.

## 2. Normalization Boundary

Current narrow path:

`worker stdout/stderr -> worker-return block extraction -> structured_return.worker_return -> RunRecord enrichment -> package notebook`

Normalization owns only the return-read boundary. It does not:

- approve a package
- ingest a deposit candidate automatically
- promote a route
- implement multi-agent orchestration
- infer line / axis output
- hide failed or weak worker output

## 3. Worker Return Sources

The runtime uses these source labels:

- `worker_emitted`: a valid delimited worker return block was parsed
- `runtime_normalized`: controlled runtime material or context-profile output was normalized
- `parser_fallback`: no valid worker block existed, but useful findings were extracted from text
- `raw_fallback`: no reliable structured or parsed content existed, so raw/error material was preserved

The source label is a supervisor signal. It is not a quality guarantee.

## 4. Failure Shapes And Rules

| Shape | Source outcome | Preservation rule | Degradation rule |
| --- | --- | --- | --- |
| valid worker-emitted JSON | `worker_emitted` | Use worker fields as primary read path | Add only boundary risks such as reread/not-approval when applicable |
| missing structured block | `parser_fallback` when bullets/paths exist, otherwise `raw_fallback` | Preserve answer preview, extracted findings, session artifacts, bounded context refs | Mark extraction status as `missing_block` |
| invalid JSON block | `parser_fallback` when text is usable, otherwise `raw_fallback` | Preserve surrounding prose and session artifacts | Mark extraction status as `invalid_json`; do not pretend worker emitted a valid return |
| partial structured block | `worker_emitted` | Preserve valid provided fields | Fill missing fields from runtime/session fallback and record missing-field risk |
| prose-only return | `parser_fallback` when observations are extractable | Extract bounded bullets/paths only | Keep next hint generic and reread-oriented unless route gives stronger bounded signal |
| failed / timeout / nonzero exit | usually `raw_fallback`, sometimes `parser_fallback` if stdout is useful | Preserve stderr/error/session artifacts and at least one failure finding | Mark execution status and exit code; continuation should inspect failure artifacts first |
| deposit-candidate return | source depends on block validity | Preserve candidate answer/findings/artifacts | Always preserve `not automatic ingestion` boundary |

## 5. Field Rules

### `answer`

Use the worker-emitted answer first. If absent, use the first useful raw block. For failed runs with no answer, use error text or an explicit failed-run answer.

### `findings[]`

Use worker-emitted findings first. If absent, use runtime context-profile findings or bounded bullet/path extraction. For failed runs with no findings, add a single failure finding.

### `files_artifacts[]`

Always preserve session artifacts. Add worker-emitted artifact refs and path refs from raw text. Do not merge artifact refs into findings unless they are explicitly part of a finding.

### `next_continue_hint`

Worker-emitted `next_continue_hint` has priority when valid.

If missing, degrade by route:

- `validation_target`: validate before reuse
- `implementation_return`: review output for follow-up patch or validation
- `deposit_candidate`: review as deposit candidate; do not ingest automatically
- `reread_target`: reread latest answer with artifact refs
- otherwise: attach latest run artifacts and ask the next package-specific question

### `risks_or_limits[]`

Record extraction status, missing worker fields, dry-run limits, failed status, exit code, explicit error text, reread/not-approval boundary, and deposit non-ingestion boundary.

### `source_refs[]`

Use worker-emitted source refs first. If absent, use bounded context refs. If those are absent, derive only conservative refs from artifact paths.

## 6. Supervisor Reading Rule

The notebook should remain readable in three tiers:

1. Strong: `worker_emitted` with answer, findings, artifacts, and concrete next hint.
2. Usable but weaker: `parser_fallback` with answer/findings and explicit extraction risk.
3. Blocked / inspect-first: `raw_fallback` or failed status with failure risk and session artifacts.

Residue or failed output can be preserved as notebook material without being treated as successful work.

