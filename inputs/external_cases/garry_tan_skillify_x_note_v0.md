[[DOCROLE:memo]]
[[RUNMODE:ingest_only]]
[[PRIORITY:normal]]

# Garry Tan skillify X note v0

## source metadata

- source_url: `https://x.com/garrytan/status/2046876981711769720`
- source_title: `How to really stop your agents from making the same mistakes`
- source_author: `Garry Tan`
- source_type: `external social post`
- source_capture_date: `2026-04-23`
- source_note_kind: `paraphrased ingest memo from local raw capture`
- raw_source_file: `inputs/external_cases/garry_tan.txt`

## why this source matters

This source is relevant to our current space because it argues for turning repeated agent failures into durable procedural assets instead of repeated prompt-time recovery.

It directly overlaps with active pressures in our space around:

- thin harness / stronger procedure layer
- deterministic script use before free-form latent reasoning
- repeat failure capture
- test and validation loops
- filing / resolver / maintenance discipline

## core claim

The post argues that agent reliability does not come from larger prompts or vague monitoring alone.

It comes from a repeatable repair loop:

1. detect a failure
2. convert it into a reusable skill or procedure
3. create deterministic code where the work is actually deterministic
4. add tests and evals
5. add resolver or trigger coverage
6. audit overlap and routing ambiguity
7. run smoke tests
8. file outputs in the right place

The author's label for this pattern is `skillify`.

## operating distinction

The strongest distinction in the source is between:

- latent work: judgment-heavy work that needs model interpretation
- deterministic work: precision work that should be handled by code or scripts

The source argues that many agent failures happen because deterministic work is wrongly performed in latent space.

Examples given in the source:

- historical calendar lookup should use local indexed search first
- time arithmetic should use an existing script instead of mental model reasoning

## structural pattern

The source implies a layered operating pattern:

### 1. failure capture

Record the concrete mistake instead of patching it with a prompt reminder.

### 2. skill or procedure creation

Write an explicit reusable procedure that forces the agent to approach the task the right way.

### 3. deterministic tooling

Where the task is precise and repeatable, generate or call code instead of reasoning through it again.

### 4. validation loop

Add:

- unit tests
- evals
- resolver checks
- duplicate audits
- end-to-end smoke tests

### 5. filing discipline

Make sure any durable output lands in the right place and follows shared filing rules.

## relevance to our current space

This source does not map directly onto our current engine, but it does strengthen several already-active directions:

- script-first for bounded probe / gate / validation work
- Codex-first for interpretation and structural judgment
- hybrid loops where scripts collect evidence and Codex decides
- durable procedural assets instead of repeated free-form correction
- explicit resolver / routing / filing discipline

It also matches our current concern that as the space grows, Codex should not spend tokens redoing deterministic inspection work that scripts already handle better.

## bounded judgment

Current bounded judgment:

- useful as a structural and operating reference
- especially relevant for execution split and script-first discipline
- not a direct architecture replacement order
- worth keeping as an external source that reinforces deterministic-first repair loops
