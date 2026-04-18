# VectorFL Paper Surface Identity Correction and Merge Reanalysis v0

## Verdict

- The previous merge reading incorrectly treated `runtime/views/vectorfl_paper_weekend_pilot/` as the existing or legacy VectorFL Paper surface.
- That is wrong.
- `vectorfl_paper_weekend_pilot` is a weekend pilot / archive / proof surface, not the existing VectorFL Paper.
- Do not use weekend pilot as the canonical merge target.

## Why the Mistake Happened

- Recent-context overfit: the latest work had been concentrated around `vectorfl_paper_proper` and `vectorfl_paper_weekend_pilot`, so the merge analysis stayed inside those newer validation surfaces.
- Naming overfit: the folder name `vectorfl_paper_weekend_pilot` contains `paper`, which made it look like a legacy Paper branch even though its role is pilot/archive.
- Missing identity check: before making merge recommendations, the analysis should have re-read the view inventory and generator map instead of relying on the recent work thread.
- Status artifacts were not used early enough: `runtime/views/folder_status.md` and the actual `runtime/views/*/index.html` inventory should have been consulted before classifying any surface as existing, legacy, proper, or test-only.

## New Rule

Before any merge involving "existing Paper", "legacy Paper", "proper", or "weekend pilot", perform a surface identity check:

1. Read `runtime/views/folder_status.md`.
2. List `runtime/views/*/index.html`.
3. Read the page title/kicker/primary description for each candidate surface.
4. Map each surface to its generator script and runtime module.
5. Classify every surface as one of: primary existing, current shell, new bridge candidate, mock, archive/proof, or test-only.
6. Only then discuss merge target and merge source.

Hard rule:

- `vectorfl_paper_weekend_pilot != existing VectorFL Paper`.

## Corrected Surface Identity Map

### Primary Existing VectorFL Paper Candidate

- Page: `runtime/views/vectorfl_operable_surface/index.html`
- Generator: `scripts/run_vectorfl_operable_surface_set.py`
- Runtime module: `app/runtime/vectorfl_operable_surface_set.py`
- Current reading: this is the strongest candidate for the existing VectorFL Paper / operable control surface.
- Evidence: page title and kicker read as `VectorFL Paper`; generator creates operable surfaces such as case detail, case inspector, external resources, CLI setup, agent/MCP control, trace audit, and worker inbox.

### Existing Current-Reading Shell Candidate

- Page: `runtime/views/vectorfl_page_shell/index.html`
- Generator: `scripts/run_vectorfl_page_app_shell.py`
- Runtime module: `app/runtime/vectorfl_page_app_shell.py`
- Current reading: route-aware app shell around `Current Reading`.
- Evidence: surfaces include current reading, cases queue, inputs intake, history trace, and programs connections.

### Older Mock Page Index

- Page: `runtime/views/vectorfl_page_mock/index.html`
- Generator candidates: `scripts/run_vectorfl_page_mock_index.py`, `scripts/run_vectorfl_page_unified_mock.py`, and related route-aware mock generators.
- Current reading: mock/index surface, not the canonical merge target until explicitly selected.

### New Supervisor Bridge Candidate

- Page: `runtime/views/vectorfl_paper_proper/index.html`
- Generator: `scripts/run_vectorfl_paper_proper_mock.py`
- Current reading: new canonical supervisor bridge candidate created during the Paper proper work.
- Important status: this surface has been hardened as a read-only canonical current supervisor surface for the new bridge path, but it is not automatically the old existing Paper.

### Weekend Pilot Archive / Proof Surface

- Page: `runtime/views/vectorfl_paper_weekend_pilot/index.html`
- Generator: `scripts/run_vectorfl_paper_weekend_pilot_mock.py`
- Current reading: weekend pilot / archive / proof surface.
- Merge rule: may provide evidence or validated units, but must not be treated as the existing VectorFL Paper.

## Corrected Merge Reanalysis

### What Should Not Be Merged Into

- Do not merge into `vectorfl_paper_weekend_pilot` as if it were the existing Paper.
- Do not use weekend pilot as a canonical destination for current supervisor flow.
- Do not promote archive/test rows, swap/stub/v4 preview chains, candidate-by-candidate archive blocks, intake template displays, or gate-close language.

### Actual Merge Target Candidates

If the goal is "merge into the existing VectorFL Paper", the first target candidate is:

- `runtime/views/vectorfl_operable_surface/index.html`
- Generator: `app/runtime/vectorfl_operable_surface_set.py`

If the goal is "merge into the existing route-aware Current Reading shell", the target candidate is:

- `runtime/views/vectorfl_page_shell/index.html`
- Generator: `app/runtime/vectorfl_page_app_shell.py`

If the goal is "continue the new supervisor bridge separately", the target remains:

- `runtime/views/vectorfl_paper_proper/index.html`
- Generator: `scripts/run_vectorfl_paper_proper_mock.py`

These are distinct merge decisions and should not be collapsed.

## Candidate Merge Units Into Existing VectorFL Paper

The merge should be unit-based, not page-based.

### Merge-Worthy Units From `vectorfl_paper_proper`

- Current SSOT vs dry-run preview distinction
- Summary-only comparison verdict
- Hold current / bounded reopen posture
- Explicit guard language: no gate close, no slot replacement, no candidate promotion
- Actual export validator status as read-only posture, if mapped to an existing audit/control area

### Likely Existing Surface Mapping

- Current posture summary: `engine-overview` or `case-detail`
- Current context / SSOT reading: `case-detail`
- External comparison / candidate evidence: `external-resources` or `case-inspector`
- Worker handoff / result return: `worker-inbox` and possibly `agent-mcp-control`
- Gate, validation, reopen, and audit posture: `trace-audit`
- CLI / agent bridge status: `agent-mcp-control`

### Non-Merge Units

- Full `vectorfl_paper_proper` page wholesale
- Full `vectorfl_paper_weekend_pilot` page
- Post-stabilization merge-test layer wholesale
- Candidate-by-candidate archive rows
- Swap/stub/v4 preview chains
- Absorption/proper promotion stubs
- Trace-heavy archive/report sections
- Intake template or inbox display
- Any wording that implies candidate promotion, slot replacement, or gate close

## Required Next Analysis Before Implementation

Before implementing any corrected merge, inspect the existing target modules directly:

- `app/runtime/vectorfl_operable_surface_set.py`
- `app/runtime/vectorfl_page_app_shell.py`

Answer these questions first:

- Is the canonical destination the existing operable control surface or the route-aware current-reading shell?
- Which exact existing page should receive posture summary first: `engine-overview`, `case-detail`, `trace-audit`, `worker-inbox`, or `external-resources`?
- Should `vectorfl_paper_proper` remain a separate bridge surface while only selected judgment language is copied into existing Paper?
- Which generator can receive the smallest reversible read-only integration without adding new data sources or write side effects?

## Current Recommendation

- Treat `vectorfl_paper_proper` as the hardened new supervisor bridge surface.
- Treat `vectorfl_operable_surface` as the likely existing VectorFL Paper merge target.
- Treat `vectorfl_page_shell` as a separate current-reading shell candidate that may need alignment, not automatic merge.
- Treat `vectorfl_paper_weekend_pilot` only as archive/proof evidence.
- Do not perform implementation until the target existing surface and exact receiving section are explicitly selected.

## 2026-04-11 Correction Lock: Proper Grammar Into Operable Surface

The merge target is now explicitly selected:

- Source grammar: `runtime/views/vectorfl_paper_proper/`
- Source generator: `scripts/run_vectorfl_paper_proper_mock.py`
- Target body: `runtime/views/vectorfl_operable_surface/`
- Target generator: `app/runtime/vectorfl_operable_surface_set.py`

This corrects the later drift:

- `vectorfl_page_shell` is not the current merge target. It is closer to an older graph/current-reading shell modification and should be held as a non-canonical staging surface unless explicitly reopened.
- `vectorfl_paper_weekend_pilot` is still not the existing Paper. It remains archive/proof evidence only.
- `vectorfl_paper_proper` should not replace the operable surface wholesale. Its supervisor bridge grammar should be translated into existing operable surface tabs.

Hard implementation rule:

- Do not add more tabs for this merge.
- Merge into existing operable tabs and panels.
- Keep Paperclip-style flow visible inside tabs: input, select, assign, confirm, supervise, return.
- Preserve the user-facing reason for Codex/Gemini: they are operating subjects attached to handoff, review, return, and supervision seams, not decorative labels.
- Record any future drift immediately before changing page targets.
