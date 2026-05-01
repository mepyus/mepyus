# external article ingest rule v0

## purpose

This rule defines how to place and ingest external articles into the space without over-promoting them.

## default placement

- Store external article ingest notes under `inputs/external_cases/`.
- Use a bounded note form, not a full copied article.
- Assign a bounded external reference subtype when possible:
  - `broad_reference`
  - `operating_reference`
  - `api_surface_reference`
  - `raw_capture`

## default document form

- Use a paraphrased ingest memo.
- Keep source metadata at the top.
- Keep the body focused on:
  - why the source matters
  - core idea
  - structure or operating pattern
  - relevance to our current space
  - bounded judgment

## routing markers

Default markers:

- `[[DOCROLE:memo]]`
- `[[RUNMODE:ingest_only]]`
- `[[PRIORITY:normal]]`

## ingest expectation

The default expectation is:

- register the note as `structured_internal_doc`
- generate receipt / label packet / origin map
- generate local line seeds and camera support if present
- do not create a ticket by default
- do not treat a single external article as an operating rule

## promotion guard

Do not treat a single external article as:

- a new axis
- a new operating rule
- a direct replacement instruction
- a direct architecture migration order

A single article should stay as:

- external reference
- local reread material
- bounded structural note

## when to escalate

Escalate beyond ingest-only only when at least one of these is true:

- the same pressure repeats across multiple independent sources
- the article directly matches an already active internal tension
- a later package needs the article as a comparison source
- a bounded mapping question explicitly asks for adaptation or attachability

## operator reading stance

Read external article notes as:

- pattern reference first
- adoption candidate second
- replacement instruction only with separate validation

## current storage pattern

Recommended filename pattern:

- `<topic>_<source>_note_v0.md`

Example:

- `andrej_karpathy_llm_wiki_medium_note_v0.md`

Subtype examples:

- broad summary page -> `broad_reference`
- concrete workflow/tuning article -> `operating_reference`
- API/product guide -> `api_surface_reference`
- pasted transcript/raw text -> `raw_capture`

## summary

For external articles, keep the input cheap, structured, and reversible:

- store as memo
- ingest only
- keep connections thin
- wait for cross-source recurrence before thickening
